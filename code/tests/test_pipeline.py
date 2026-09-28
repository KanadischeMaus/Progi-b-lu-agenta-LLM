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
