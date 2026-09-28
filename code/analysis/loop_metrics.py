"""Metryki zachowania w pętli zamkniętej (docs/04, sekcja 7).

Przykład (z katalogu code/):
    python -m analysis.loop_metrics --logs ../results/raw/E8/E8/*.jsonl --out ../results/processed/E8_metryki.csv
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

from common import read_jsonl

CORRECTIVE = {"battery_charge": {1, 2}, "soil_moisture": {0}}
PAIN_LEVEL = 20.0      # granica kategorii Low (bateria) / Very dry (gleba)
CRITICAL_LEVEL = 5.0


def episodes(steps: list[dict], resource: str) -> list[dict]:
    """Epizody naprawcze: maksymalne ciągi kroków z akcją z A_r."""
    acts = CORRECTIVE[resource]
    out, cur = [], None
    for s in steps:
        if s["executed_action"] in acts:
            if cur is None:
                cur = {"start": s["step"], "x_on": s["state_before"][resource]}
            cur["end"] = s["step"]
            cur["x_off"] = s["state_after"][resource]
        elif cur is not None:
            out.append(cur)
            cur = None
    if cur is not None:
        out.append(cur)
    for e in out:
        e["histereza"] = e["x_off"] - e["x_on"]
        e["dlugosc"] = e["end"] - e["start"] + 1
    return out


def reaction_delays(steps: list[dict], resource: str, level: float = PAIN_LEVEL) -> list[int | None]:
    """Liczba kroków od spadku x_r poniżej progu do pierwszej akcji naprawczej (None = brak reakcji)."""
    acts = CORRECTIVE[resource]
    delays, waiting_since = [], None
    for s in steps:
        x = s["state_before"][resource]
        if waiting_since is None and x < level:
            waiting_since = s["step"]
        if waiting_since is not None:
            if s["executed_action"] in acts:
                delays.append(s["step"] - waiting_since)
                waiting_since = None
            elif x >= level:
                delays.append(None)  # wyszło z bólu bez reakcji
                waiting_since = None
    if waiting_since is not None:
        delays.append(None)
    return delays


def episode_metrics(steps: list[dict]) -> dict:
    steps = sorted(steps, key=lambda s: s["step"])
    n = len(steps)
    first = steps[0]
    m = {"prompt_id": first["prompt_id"], "episode_seed": first["episode_seed"], "kroki": n}
    for r, short in (("battery_charge", "bat"), ("soil_moisture", "gleba")):
        eps = episodes(steps, r)
        xs = np.array([s["state_before"][r] for s in steps], dtype=float)
        d = reaction_delays(steps, r)
        m.update({
            f"{short}_epizody": len(eps),
            f"{short}_x_on_mediana": float(np.median([e["x_on"] for e in eps])) if eps else float("nan"),
            f"{short}_x_off_mediana": float(np.median([e["x_off"] for e in eps])) if eps else float("nan"),
            f"{short}_histereza_mediana": float(np.median([e["histereza"] for e in eps])) if eps else float("nan"),
            f"{short}_czas_w_bolu": float(np.mean(xs < PAIN_LEVEL)),
            f"{short}_czas_krytyczny": float(np.mean(xs < CRITICAL_LEVEL)),
            f"{short}_opoznienie_mediana": float(np.median([x for x in d if x is not None])) if any(x is not None for x in d) else float("nan"),
            f"{short}_brak_reakcji": sum(x is None for x in d),
        })
    non_wait = [s for s in steps if s["executed_action"] != 7]
    no_need = [s for s in steps if s["state_before"]["battery_charge"] >= 40 and s["state_before"]["soil_moisture"] >= 35]
    m.update({
        "akcje_bezskuteczne": float(np.mean([s["effective"] is False for s in non_wait])) if non_wait else float("nan"),
        "bezczynnosc_bez_potrzeby": float(np.mean([s["executed_action"] == 7 for s in no_need])) if no_need else float("nan"),
        "odpowiedzi_nieczytelne": float(np.mean([s["parse_status"] != "ok" for s in steps])),
        "kroki_z_wyplata": int(sum(bool(s.get("payoff")) for s in steps)),
        "udzial_moist": float(np.mean([35 <= s["state_before"]["soil_moisture"] <= 60 for s in steps])),
    })
    return m


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--logs", nargs="+", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    rows = [episode_metrics(read_jsonl(p)) for p in args.logs if ".partial-" not in p.name]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    print(f"Zapisano metryki {len(rows)} epizodów do {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
