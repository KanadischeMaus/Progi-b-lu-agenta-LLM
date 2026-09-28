"""Pętla zamknięta: pełna symulacja agenta w środowisku (docs/04, sekcja 7; eksperyment E8).

Każdy epizod (prompt × ziarno środowiska) trafia do osobnego pliku JSONL, jedna linia na krok.
W rekordzie jest stan pokazany modelowi (`state_before`), więc stan i decyzja nie mogą się
rozjechać o jeden krok (docs/05, problem 5). Nieudane parsowanie: wykonywana jest akcja
domyślna (7, jak w listingu 11), ale rekord ma `fallback=True` i status parsowania.

Przykład (z katalogu code/):
    python -m loop.run_loop --config configs/E8_petla.json
    python -m loop.run_loop --config configs/E8_petla.json --fake --steps 50
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from agent.llm import FakeLLM, OllamaLLM
from agent.parse import parse_action, strip_thinking
from agent.prompts import build_prompt, load_template
from common import REPO_ROOT, append_jsonl, derive_seed, machine_info, now_iso, read_jsonl
from env.describe import describe_state, gaps_in_state
from env.garden_env import ENV_VERSION, GardenRobotEnv

DEFAULT_ACTION = 7


def run_episode(cfg: dict, llm, meta: dict, prompt_id: str, env_seed: int, steps: int, out_path: Path) -> None:
    existing = read_jsonl(out_path)
    if existing and len(existing) >= steps:
        return  # epizod kompletny
    if existing:  # niepełny epizod: odkładamy i liczymy od nowa (stan środowiska nie jest zapisywany w locie)
        out_path.rename(out_path.with_suffix(f".partial-{int(time.time())}.jsonl"))

    env = GardenRobotEnv(seed=env_seed, **cfg.get("env_params", {}))
    state = env.reset()
    rep, det = cfg.get("representation", "labels"), cfg.get("details")
    for t in range(steps):
        desc = describe_state(state, rep, det)
        prompt = build_prompt(prompt_id, desc)
        seed = derive_seed(cfg["exp_id"], prompt_id, env_seed, t)
        res = llm(prompt, seed=seed, state=state, resource=cfg.get("fake_resource"))
        answer, think_in_content = strip_thinking(res.get("content", ""))
        action, status = parse_action(res.get("content", ""))
        if res.get("failed"):
            status = "timeout"
        fallback = action is None
        executed = DEFAULT_ACTION if fallback else action
        state_before = dict(state)
        state = env.step(executed)
        append_jsonl(out_path, {
            "exp_id": cfg["exp_id"], "run_id": out_path.parent.name, "mode": "loop",
            "prompt_id": prompt_id, "episode_seed": env_seed, "step": t, "seed": seed,
            "representation": rep, "details": det,
            "state_before": state_before, "state_gaps": gaps_in_state(state_before),
            "prompt_text": prompt if (t == 0 or cfg.get("log_full_prompt", True)) else None,
            "response_raw": res.get("content", ""), "answer": answer,
            "thinking": res.get("thinking") or think_in_content,
            "parse_status": status, "action": action, "fallback": fallback, "executed_action": executed,
            "effective": env.last_info.get("effective"), "payoff": env.last_info.get("payoff"),
            "rainwater_fallen": env.last_info.get("rainwater_fallen"), "state_after": state,
            "latency_s": res.get("latency_s"), "eval_count": res.get("eval_count"),
            "options": res.get("options"), "think": res.get("think"), "errors": res.get("errors"),
            **meta, "env_version": ENV_VERSION, "machine": machine_info(), "timestamp": now_iso(),
        })


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", required=True, type=Path)
    ap.add_argument("--fake", action="store_true")
    ap.add_argument("--steps", type=int, help="nadpisuje liczbę kroków z konfiguracji")
    ap.add_argument("--out-dir", type=Path)
    args = ap.parse_args()
    cfg = json.loads(args.config.read_text(encoding="utf-8"))
    steps = args.steps or cfg["steps"]
    for p in cfg["prompts"]:
        load_template(p)
    if args.fake:
        llm = FakeLLM(thresholds=cfg.get("fake_thresholds", {"battery_charge": 25}))
        cfg = {**cfg, "fake_resource": "battery_charge"}
    else:
        llm = OllamaLLM(model=cfg["model"], options=cfg.get("options", {}), think=cfg.get("think", True),
                        host=cfg.get("host", "http://localhost:11434"), timeout=cfg.get("timeout_s", 900))
    meta = llm.metadata()
    out_dir = args.out_dir or REPO_ROOT / "results" / "raw" / cfg["exp_id"] / (cfg["exp_id"] + ("_fake" if args.fake else ""))
    for prompt_id in cfg["prompts"]:
        for env_seed in cfg["env_seeds"]:
            out = out_dir / f"{prompt_id}_seed{env_seed}.jsonl"
            print(f"Epizod: {prompt_id}, ziarno {env_seed} → {out}", file=sys.stderr)
            run_episode(cfg, llm, meta, prompt_id, env_seed, steps, out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
