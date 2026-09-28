"""Testy modułu analysis.psychometric.

Uruchomienie z katalogu code/:
    python -m pytest tests            # jeśli pytest jest zainstalowany
    python -m tests.test_psychometric # bez pytest
"""
from __future__ import annotations

import numpy as np
from scipy import optimize

from analysis.psychometric import (
    Fit,
    bootstrap,
    compare,
    fit,
    lrt_vs_constant,
    psychometric,
    simulate,
    wilson_interval,
)

LEVELS = np.arange(0, 101, 5, dtype=float)


def test_ksztalt_funkcji():
    th, k, g, l = 30.0, 0.2, 0.05, 0.1
    p = psychometric(LEVELS, th, k, g, l)
    assert np.all(np.diff(p) < 0), "P(x) powinno maleć z poziomem zasobu"
    assert abs(psychometric(-1e4, th, k, g, l) - (1 - l)) < 1e-9
    assert abs(psychometric(1e4, th, k, g, l) - g) < 1e-9
    assert abs(psychometric(th, th, k, g, l) - (g + (1 - g - l) / 2)) < 1e-12


def test_theta50_zgodne_z_pierwiastkiem():
    f = Fit(theta=30.0, k=0.2, gamma=0.1, lam=0.2, loglik=0.0, converged=True)
    root = optimize.brentq(lambda x: psychometric(x, 30.0, 0.2, 0.1, 0.2) - 0.5, -100, 200)
    assert abs(f.theta50 - root) < 1e-6
    assert np.isnan(Fit(30.0, 0.2, 0.6, 0.0, 0.0, True).theta50)


def test_szerokosc_przejscia():
    f = Fit(theta=0.0, k=0.25, gamma=0.0, lam=0.0, loglik=0.0, converged=True)
    x25 = optimize.brentq(lambda x: psychometric(x, 0, 0.25, 0, 0) - 0.25, -100, 100)
    x75 = optimize.brentq(lambda x: psychometric(x, 0, 0.25, 0, 0) - 0.75, -100, 100)
    assert abs((x25 - x75) - f.width) < 1e-6


def test_odzyskiwanie_duza_proba():
    rng = np.random.default_rng(123)
    for true in [dict(theta=20, k=0.3, gamma=0.02, lam=0.05), dict(theta=55, k=0.1, gamma=0.1, lam=0.0)]:
        x, r, n = simulate(LEVELS, 400, rng=rng, **true)
        f = fit(x, r, n)
        assert abs(f.theta - true["theta"]) < 2.0, (f, true)
        assert abs(f.k - true["k"]) / true["k"] < 0.3, (f, true)
        assert abs(f.gamma - true["gamma"]) < 0.03 and abs(f.lam - true["lam"]) < 0.03


def test_lrt_odroznia_prog_od_braku_progu():
    rng = np.random.default_rng(7)
    x, r, n = simulate(LEVELS, 20, theta=30, k=0.4, gamma=0.05, lam=0.05, rng=rng)
    assert lrt_vs_constant(x, r, n)["p_value"] < 1e-6
    flat_r = rng.binomial(np.full(LEVELS.shape, 20), 0.3)
    assert lrt_vs_constant(LEVELS, flat_r, np.full(LEVELS.shape, 20))["p_value"] > 1e-3


def test_bootstrap_i_porownanie_wykrywa_przesuniecie():
    rng = np.random.default_rng(11)
    xa, ra, na = simulate(LEVELS, 20, theta=20, k=0.3, gamma=0.05, lam=0.05, rng=rng)
    xb, rb, nb = simulate(LEVELS, 20, theta=40, k=0.3, gamma=0.05, lam=0.05, rng=rng)
    ba = bootstrap(xa, ra, na, B=150, seed=1)
    bb = bootstrap(xb, rb, nb, B=150, seed=2)
    lo, hi = ba["ci"]["theta"]
    assert lo < ba["fit"].theta < hi
    c = compare(ba, bb, "theta")
    assert c["excludes_zero"] and 10 < c["diff"] < 30, c


def test_brak_odpowiedzi_na_poziomie_jest_pomijany():
    n_total = np.full(LEVELS.shape, 20)
    n_total[3] = 0
    rng = np.random.default_rng(5)
    r = rng.binomial(n_total, psychometric(LEVELS, 30, 0.3, 0.05, 0.05))
    f = fit(LEVELS, r, n_total)
    assert np.isfinite(f.theta)


def test_wilson():
    lo, hi = wilson_interval(10, 20)
    assert lo < 0.5 < hi and 0.25 < lo < 0.32 and 0.68 < hi < 0.75


if __name__ == "__main__":
    import sys

    tests = [(n, f) for n, f in sorted(globals().items()) if n.startswith("test_") and callable(f)]
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"OK    {name}")
        except AssertionError as e:  # noqa: PERF203
            failed += 1
            print(f"BŁĄD  {name}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} testów zaliczonych")
    sys.exit(1 if failed else 0)
