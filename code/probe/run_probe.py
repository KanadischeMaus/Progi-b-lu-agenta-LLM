"""Sondowanie kontrolowane: pytania o decyzję w sztucznie ustawionych stanach (docs/04, sekcja 5).

Dla każdego warunku (zasób, kontekst, zbiór akcji naprawczych), poziomu zasobu i próby
składa prompt, wywołuje model, parsuje odpowiedź i dopisuje jeden rekord do pliku JSONL.
Kolejność wywołań jest losowa (ustalona ziarnem). Przerwany przebieg wznawia się tym samym
poleceniem: rekordy już zapisane są pomijane.

Przykłady (z katalogu code/):
    python -m probe.run_probe --config configs/E1_progi_bazowe.json
    python -m probe.run_probe --config configs/E1_progi_bazowe.json --fake   # bez LLM, test toru pomiaru
    python -m probe.run_probe --config configs/E0_pilotaz.json --limit 10    # tylko 10 wywołań
"""
from __future__ import annotations

import argparse
import json
import random
import sys
import time
from pathlib import Path

from agent.llm import FakeLLM, OllamaLLM
from agent.parse import parse_action, strip_thinking
from agent.prompts import build_prompt, load_template
from common import REPO_ROOT, append_jsonl, derive_seed, expand_levels, machine_info, now_iso, read_jsonl
from env.describe import describe_state, gaps_in_state
from env.garden_env import ENV_VERSION

# Stan „tła”, na który nakłada się kontekst warunku i badany poziom zasobu.
BASE_STATE = {
    "soil_moisture": 45, "battery_charge": 90, "water_can": 60, "spare_batteries": 1,
    "sunlight": 50, "rain_barrel": 70, "water_well": 70, "money": 20, "rainwater_fallen": 0,
}


def job_key(r: dict) -> tuple:
    return (r["prompt_id"], r["condition_id"], r["representation"], r.get("details"), r["level"],
            r.get("level2"), r["trial"])


def build_jobs(cfg: dict) -> list[dict]:
    jobs = []
    for prompt_id in cfg["prompts"]:
        for cond in cfg["conditions"]:
            for rep in cfg.get("representations", ["labels"]):
                for det in cfg.get("details", [None]):
                    levels2 = expand_levels(cond["levels2"]) if "resource2" in cond else [None]
                    for level in expand_levels(cond["levels"]):
                        for level2 in levels2:  # siatka 2D (E7): drugi zasób zmienny
                            for trial in range(cfg["trials"]):
                                jobs.append({"prompt_id": prompt_id, "condition_id": cond["condition_id"],
                                             "representation": rep, "details": det, "level": level,
                                             "level2": level2, "trial": trial, "cond": cond})
    random.Random(cfg.get("seed", 0)).shuffle(jobs)
    return jobs


def make_llm(cfg: dict, fake: bool):
    if fake:
        th = cfg.get("fake_thresholds", {"battery_charge": 25, "soil_moisture": 30})
        return FakeLLM(thresholds=th)
    return OllamaLLM(model=cfg["model"], options=cfg.get("options", {}), think=cfg.get("think", True),
                     host=cfg.get("host", "http://localhost:11434"), timeout=cfg.get("timeout_s", 900),
                     retries=cfg.get("retries", 2))


def run(cfg: dict, out_path: Path, fake: bool = False, limit: int | None = None, quiet: bool = False) -> Path:
    for p in cfg["prompts"]:
        load_template(p)  # wczesny błąd, jeśli brakuje pliku promptu
    llm = make_llm(cfg, fake)
    meta = llm.metadata()
    done = {job_key(r) for r in read_jsonl(out_path)}
    jobs = [j for j in build_jobs(cfg) if job_key(j) not in done]
    if limit is not None:
        jobs = jobs[:limit]
    if not quiet:
        print(f"Plik: {out_path}\nDo wykonania: {len(jobs)} wywołań (pominięto {len(done)} zapisanych)", file=sys.stderr)

    t_start = time.time()
    for i, job in enumerate(jobs, 1):
        cond = job["cond"]
        resource = cond["resource"]
        state = {**BASE_STATE, **cond.get("context", {}), resource: job["level"]}
        if job["level2"] is not None:
            state[cond["resource2"]] = job["level2"]
        desc = describe_state(state, job["representation"], job["details"])
        prompt = build_prompt(job["prompt_id"], desc)
        seed_parts = [cfg["exp_id"], job["prompt_id"], job["condition_id"], job["representation"],
                      job["details"], job["level"], job["trial"]]
        if job["level2"] is not None:
            seed_parts.append(job["level2"])
        seed = derive_seed(*seed_parts)
        res = llm(prompt, seed=seed, state=state, resource=resource)
        answer, think_in_content = strip_thinking(res.get("content", ""))
        action, status = parse_action(res.get("content", ""))
        if res.get("failed"):
            status = "timeout"
        corrective = None if action is None else action in set(cond["corrective"])
        record = {
            "exp_id": cfg["exp_id"], "run_id": out_path.stem, "mode": "probe",
            "prompt_id": job["prompt_id"], "condition_id": job["condition_id"],
            "representation": job["representation"], "details": job["details"],
            "resource": resource, "level": job["level"], "trial": job["trial"], "seed": seed,
            "resource2": cond.get("resource2"), "level2": job["level2"], "corrective_set2": cond.get("corrective2"),
            "corrective_set": cond["corrective"], "state": state, "state_gaps": gaps_in_state(state),
            "prompt_text": prompt,
            "response_raw": res.get("content", ""), "answer": answer,
            "thinking": res.get("thinking") or think_in_content,
            "parse_status": status, "action": action, "corrective": corrective,
            "latency_s": res.get("latency_s"), "eval_count": res.get("eval_count"),
            "options": res.get("options"), "think": res.get("think"), "errors": res.get("errors"),
            **meta, "env_version": ENV_VERSION, "machine": machine_info(), "timestamp": now_iso(),
        }
        append_jsonl(out_path, record)
        if not quiet and (i % 10 == 0 or i == len(jobs)):
            el = time.time() - t_start
            eta = el / i * (len(jobs) - i)
            print(f"  {i}/{len(jobs)}  średnio {el / i:.1f} s/wywołanie  pozostało ok. {eta / 60:.0f} min", file=sys.stderr)
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--out", type=Path, help="plik JSONL (domyślnie results/raw/<exp_id>/<exp_id>[_fake].jsonl)")
    ap.add_argument("--fake", action="store_true", help="model testowy zamiast Ollamy")
    ap.add_argument("--limit", type=int, help="wykonaj najwyżej N wywołań (pilotaż)")
    args = ap.parse_args()
    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    out = args.out or REPO_ROOT / "results" / "raw" / cfg["exp_id"] / f"{cfg['exp_id']}{'_fake' if args.fake else ''}.jsonl"
    run(cfg, out, fake=args.fake, limit=args.limit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
