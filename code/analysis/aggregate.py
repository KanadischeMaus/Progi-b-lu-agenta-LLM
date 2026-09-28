"""Z surowych logów sondowania do tabel: liczebności na poziomach i parametry progu.

Grupowanie: prompt_id × condition_id × representation × details (× think, temperatura).
Dla każdej grupy: liczba ważnych odpowiedzi i reakcji naprawczych na poziom, odsetek
odpowiedzi nieczytelnych, dopasowanie funkcji psychometrycznej z bootstrapem i test LRT.

Przykład (z katalogu code/):
    python -m analysis.aggregate --logs ../results/raw/E1/E1.jsonl --out ../results/processed/E1 --B 2000
Wynik: <out>_poziomy.csv, <out>_progi.csv, <out>_progi.json
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

from analysis.psychometric import bootstrap, lrt_vs_constant, wilson_interval
from common import read_jsonl

GROUP_FIELDS = ("prompt_id", "condition_id", "representation", "details", "think", "temperature")


def group_key(r: dict) -> tuple:
    opts = r.get("options") or {}
    return (r["prompt_id"], r["condition_id"], r["representation"], r.get("details"), r.get("think"),
            opts.get("temperature"))


def level_table(records: list[dict]) -> dict[tuple, list[dict]]:
    """{grupa: [ {level, n_total, n_resp, n_invalid, p_hat, ci_lo, ci_hi}, ... ]}"""
    acc: dict = defaultdict(lambda: defaultdict(lambda: {"n_total": 0, "n_resp": 0, "n_invalid": 0}))
    for r in records:
        if r.get("mode", "probe") != "probe" or r.get("level2") is not None:
            continue  # pętla i siatka 2D (E7) mają osobną analizę
        cell = acc[group_key(r)][r["level"]]
        if r["parse_status"] != "ok":
            cell["n_invalid"] += 1
        else:
            cell["n_total"] += 1
            cell["n_resp"] += int(bool(r["corrective"]))
    out = {}
    for g, levels in acc.items():
        rows = []
        for lv in sorted(levels):
            c = levels[lv]
            p = c["n_resp"] / c["n_total"] if c["n_total"] else float("nan")
            lo, hi = wilson_interval(c["n_resp"], c["n_total"])
            rows.append({"level": lv, **c, "p_hat": p, "ci_lo": lo, "ci_hi": hi})
        out[g] = rows
    return out


def fit_groups(table: dict, B: int, seed: int) -> list[dict]:
    results = []
    for g, rows in table.items():
        lv = np.array([r["level"] for r in rows], dtype=float)
        nr = np.array([r["n_resp"] for r in rows])
        nt = np.array([r["n_total"] for r in rows])
        n_invalid = sum(r["n_invalid"] for r in rows)
        row = dict(zip(GROUP_FIELDS, g))
        row.update(n_valid=int(nt.sum()), n_invalid=int(n_invalid),
                   invalid_rate=n_invalid / max(1, n_invalid + int(nt.sum())))
        if nt.sum() == 0 or len(lv) < 3:
            row["uwaga"] = "za mało danych"
            results.append(row)
            continue
        boot = bootstrap(lv, nr, nt, B=B, seed=seed)
        f = boot["fit"]
        lrt = lrt_vs_constant(lv, nr, nt, f)
        row.update({
            "theta": f.theta, "theta_lo": boot["ci"]["theta"][0], "theta_hi": boot["ci"]["theta"][1],
            "width": f.width, "width_lo": boot["ci"]["width"][0], "width_hi": boot["ci"]["width"][1],
            "k": f.k, "gamma": f.gamma, "gamma_lo": boot["ci"]["gamma"][0], "gamma_hi": boot["ci"]["gamma"][1],
            "lam": f.lam, "lam_lo": boot["ci"]["lam"][0], "lam_hi": boot["ci"]["lam"][1],
            "theta50": f.theta50, "loglik": f.loglik, "lrt_stat": lrt["stat"], "lrt_p": lrt["p_value"],
            "theta_poza_zakresem": bool(f.theta < lv.min() or f.theta > lv.max()),
        })
        results.append(row)
    return results


def _write_csv(path: Path, rows: list[dict]) -> None:
    fields: list[str] = []
    for r in rows:
        fields += [k for k in r if k not in fields]
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--logs", nargs="+", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path, help="prefiks plików wynikowych")
    ap.add_argument("--B", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()

    records = [r for p in args.logs for r in read_jsonl(p)]
    table = level_table(records)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    level_rows = [dict(zip(GROUP_FIELDS, g), **r) for g, rows in table.items() for r in rows]
    _write_csv(args.out.with_name(args.out.name + "_poziomy.csv"), level_rows)
    fits = fit_groups(table, args.B, args.seed)
    _write_csv(args.out.with_name(args.out.name + "_progi.csv"), fits)
    meta = {"zrodla": [str(p) for p in args.logs], "B": args.B, "seed": args.seed, "liczba_rekordow": len(records)}
    args.out.with_name(args.out.name + "_progi.json").write_text(
        json.dumps({"meta": meta, "wyniki": fits}, ensure_ascii=False, indent=2, default=float), encoding="utf-8")
    for f in fits:
        if "theta" in f:
            print(f"{f['prompt_id']:>12} {f['condition_id']:>14} {f['representation']:>8}  "
                  f"θ = {f['theta']:.1f} [{f['theta_lo']:.1f}; {f['theta_hi']:.1f}]  "
                  f"w = {f['width']:.1f}  γ = {f['gamma']:.2f}  λ = {f['lam']:.2f}  "
                  f"nieczytelne = {100 * f['invalid_rate']:.1f}%  LRT p = {f['lrt_p']:.2g}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
