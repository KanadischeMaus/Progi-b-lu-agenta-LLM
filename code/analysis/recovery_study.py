"""Test odzyskiwania parametrów funkcji psychometrycznej (docs/04, sekcja 4).

Symuluje odpowiedzi ze znanych parametrów przy planie pomiaru z eksperymentu
(domyślnie 21 poziomów 0, 5, ..., 100 i 20 prób na poziom), dopasowuje model,
liczy przedziały bootstrapowe i raportuje obciążenie, RMSE, pokrycie przedziałów
95% oraz medianę szerokości przedziału dla theta.

Uruchomienie (z katalogu code/):
    OMP_NUM_THREADS=1 python -m analysis.recovery_study --sims 100 --B 200 --workers 4
(OMP_NUM_THREADS=1 zapobiega konkurencji wątków BLAS między procesami.)
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ProcessPoolExecutor

import numpy as np

from analysis.psychometric import bootstrap, simulate

SCENARIOS = {
    "ostry": dict(theta=25.0, k=0.30, gamma=0.05, lam=0.05),
    "rozmyty": dict(theta=40.0, k=0.08, gamma=0.10, lam=0.10),
}


def one_run(args):
    scen, true, levels, n, B, seed = args
    rng = np.random.default_rng(seed)
    x, r, t = simulate(levels, n, rng=rng, **true)
    res = bootstrap(x, r, t, B=B, seed=seed + 1)
    f = res["fit"]
    out = {"scenario": scen}
    for name in ("theta", "k", "gamma", "lam"):
        est = getattr(f, name)
        lo, hi = res["ci"][name]
        out[name] = (est, lo, hi, lo <= true[name] <= hi)
    true_w = 2 * np.log(3) / true["k"]
    lo, hi = res["ci"]["width"]
    out["width"] = (f.width, lo, hi, lo <= true_w <= hi)
    return out


def summarize(runs, true):
    rows = {}
    true = dict(true, width=2 * np.log(3) / true["k"])
    for name in ("theta", "width", "k", "gamma", "lam"):
        est = np.array([r[name][0] for r in runs])
        cov = np.mean([r[name][3] for r in runs])
        ciw = np.median([r[name][2] - r[name][1] for r in runs])
        rows[name] = {
            "prawda": round(float(true[name]), 3),
            "srednia_est": round(float(est.mean()), 3),
            "obciazenie": round(float(est.mean() - true[name]), 3),
            "rmse": round(float(np.sqrt(np.mean((est - true[name]) ** 2))), 3),
            "pokrycie_95": round(float(cov), 3),
            "mediana_szer_PU": round(float(ciw), 3),
        }
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sims", type=int, default=100)
    ap.add_argument("--B", type=int, default=200)
    ap.add_argument("--n", type=int, default=20, help="próby na poziom")
    ap.add_argument("--step", type=int, default=5, help="odstęp poziomów (0..100)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--json", type=str, default=None)
    ap.add_argument("--scenarios", type=str, default=",".join(SCENARIOS), help="lista scenariuszy, np. ostry,rozmyty")
    args = ap.parse_args()

    levels = np.arange(0, 101, args.step, dtype=float)
    report = {"plan": {"poziomy": len(levels), "proby_na_poziom": args.n, "symulacje": args.sims, "B": args.B}}
    for scen in args.scenarios.split(","):
        true = SCENARIOS[scen]
        jobs = [(scen, true, levels, args.n, args.B, 1000 * i + 7) for i in range(args.sims)]
        with ProcessPoolExecutor(max_workers=args.workers) as ex:
            runs = list(ex.map(one_run, jobs))
        report[scen] = summarize(runs, true)
        print(f"\n== scenariusz: {scen} {true}", flush=True)
        print(f"{'param':>6} {'prawda':>8} {'śr.est':>8} {'obc.':>7} {'RMSE':>7} {'pokr.':>6} {'med.szer.PU':>11}")
        for name, row in report[scen].items():
            print(f"{name:>6} {row['prawda']:>8} {row['srednia_est']:>8} {row['obciazenie']:>7} "
                  f"{row['rmse']:>7} {row['pokrycie_95']:>6} {row['mediana_szer_PU']:>11}", flush=True)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(report, fh, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
