"""Tor pomiaru od początku do końca na modelu testowym o znanym progu (bez Ollamy)."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

import numpy as np

from analysis.aggregate import fit_groups, level_table
from analysis.loop_metrics import episode_metrics
from common import read_jsonl

CFG = json.loads((Path(__file__).resolve().parent.parent / "configs" / "E1_progi_bazowe.json").read_text(encoding="utf-8"))


def test_sondowanie_odzyskuje_prog_i_wznawia():
    from probe.run_probe import run

    cfg = {**CFG, "trials": 20, "fake_thresholds": {"battery_charge": 25, "soil_moisture": 30}}
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "E1_fake.jsonl"
        run(cfg, out, fake=True, limit=300, quiet=True)
        assert len(read_jsonl(out)) == 300
        run(cfg, out, fake=True, quiet=True)  # wznowienie: dopisuje brakujące, bez duplikatów
        recs = read_jsonl(out)
        assert len(recs) == 2 * 21 * 20
        keys = {(r["condition_id"], r["level"], r["trial"]) for r in recs}
        assert len(keys) == len(recs)
        assert {r["parse_status"] for r in recs} >= {"ok", "wiele_liczb"}
        fits = {f["condition_id"]: f for f in fit_groups(level_table(recs), B=100, seed=1)}
        assert abs(fits["bat_base"]["theta"] - 25) < 4, fits["bat_base"]
        assert abs(fits["soil_base"]["theta"] - 30) < 4, fits["soil_base"]
        assert fits["bat_base"]["theta_lo"] < 25 < fits["bat_base"]["theta_hi"]


def test_wybor_warunku_i_dokonczenie():
    from probe.run_probe import run

    cfg = {**CFG, "trials": 2}
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "E1_fake.jsonl"
        run(cfg, out, fake=True, quiet=True, conditions=["bat_base"])
        part = read_jsonl(out)
        assert len(part) == 21 * 2 and {r["condition_id"] for r in part} == {"bat_base"}
        run(cfg, out, fake=True, quiet=True)  # bez wyboru: dopisuje pozostały warunek, bez duplikatów
        full = read_jsonl(out)
        assert len(full) == 2 * 21 * 2 and full[: len(part)] == part
        ref = Path(d) / "calosc.jsonl"
        run(cfg, ref, fake=True, quiet=True)
        seeds = {(r["condition_id"], r["level"], r["trial"]): r["seed"] for r in read_jsonl(ref)}
        assert seeds == {(r["condition_id"], r["level"], r["trial"]): r["seed"] for r in full}
        try:
            run(cfg, out, fake=True, quiet=True, conditions=["nie_ma"])
        except SystemExit:
            pass
        else:
            raise AssertionError("nieznany warunek powinien przerwać przebieg")


def test_kontekst_neutralny_od_e1_ma_zapas_2():
    cfg_dir = Path(__file__).resolve().parent.parent / "configs"
    for path in sorted(cfg_dir.glob("*.json")):
        cfg = json.loads(path.read_text(encoding="utf-8"))
        expected = 1 if cfg["exp_id"].startswith("E0") else 2  # rodzina E0 to pilotaż (docs/12, D22)
        for cond in cfg.get("conditions", []):
            assert cond["context"].get("spare_batteries", expected) == expected, (path.name, cond["condition_id"])


def test_ollama_zwraca_pola_czasu():
    from agent.llm import OllamaLLM

    class Client:
        def chat(self, **kwargs):
            return {"message": {"content": "2", "thinking": "x"}, "eval_count": 5, "prompt_eval_count": 250,
                    "total_duration": 10, "load_duration": 3, "prompt_eval_duration": 2, "eval_duration": 5,
                    "done_reason": "stop"}

    llm = OllamaLLM.__new__(OllamaLLM)  # bez serwera i bez biblioteki ollama
    llm.model, llm.options, llm.think, llm.retries, llm.client = "m", {"temperature": 0.8}, True, 0, Client()
    res = llm("prompt", seed=7)
    assert res["options"] == {"temperature": 0.8, "seed": 7} and res["content"] == "2"
    assert (res["load_duration_ns"], res["total_duration_ns"], res["prompt_eval_count"]) == (3, 10, 250)
    assert res["done_reason"] == "stop"


def test_zestawienia_przebiegu():
    from analysis.run_summary import action_table, pair_table, repeat_table
    from probe.run_probe import run

    cfg = {**CFG, "trials": 3, "conditions": CFG["conditions"][:1]}
    with tempfile.TemporaryDirectory() as d:
        first, second = Path(d) / "A.jsonl", Path(d) / "B.jsonl"
        run(cfg, first, fake=True, quiet=True)
        run(cfg, second, fake=True, quiet=True)
        a, b = read_jsonl(first), read_jsonl(second)
    rows = action_table(a)
    assert len(rows) == 21 and {r["label"] for r in rows} == {"Critical", "Low", "Moderate low", "Medium", "High", "Full"}
    for r in rows:  # akcje sumują się do liczby ważnych odpowiedzi
        assert sum(r[f"action_{i}"] for i in range(8)) == r["n_valid"] == 3 - r["n_invalid"]
    # model testowy zależy tylko od ziarna: dwa przebiegi są identyczne
    assert all(r["identical"] for r in pair_table(a, b)) and len(pair_table(a, b)) == len(a)
    assert {r["variant"] for r in repeat_table({"A": a, "B": b})} == {"a"}
    b[0]["thinking"] = "inny tekst"
    rep = repeat_table({"A": a, "B": b})
    assert sorted(r["variant"] for r in rep).count("b") == 1 and max(r["n_variants"] for r in rep) == 2


def test_petla_zamknieta_i_metryki():
    from agent.llm import FakeLLM
    from loop.run_loop import run_episode

    cfg = {"exp_id": "T", "prompts": ["ref_v1"], "representation": "labels", "fake_resource": "battery_charge"}
    llm = FakeLLM(thresholds={"battery_charge": 25})
    with tempfile.TemporaryDirectory() as d:
        out = Path(d) / "ep.jsonl"
        run_episode(cfg, llm, llm.metadata(), "ref_v1", 11, 120, out)
        steps = read_jsonl(out)
        assert len(steps) == 120
        for a, b in zip(steps, steps[1:]):  # stan pokazany modelowi = stan po poprzednim kroku
            assert b["state_before"] == a["state_after"]
        m = episode_metrics(steps)
        assert m["bat_epizody"] >= 1 and m["kroki"] == 120
        assert np.isfinite(m["bat_x_on_mediana"])
