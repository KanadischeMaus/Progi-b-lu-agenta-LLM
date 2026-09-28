"""Dopasowanie funkcji psychometrycznej do odpowiedzi agenta LLM.

Model (docs/04_metodologia_pomiaru.md, sekcja 3):

    P(x) = gamma + (1 - gamma - lam) * F(x),   F(x) = 1 / (1 + exp(k * (x - theta))),  k > 0

    theta  – próg bólu (punkt środkowy przejścia, poziom zasobu w %)
    k      – ostrość przejścia; szerokość 25–75%: w = 2 ln 3 / k
    gamma  – poziom reakcji naprawczych bez potrzeby (przy pełnym zasobie)
    lam    – poziom zaniedbania (brak reakcji przy zasobie bliskim zera)

Dane wejściowe to zagregowane odpowiedzi na poziomach zasobu:
    levels[i]  – poziom zasobu x_i,
    n_resp[i]  – liczba reakcji naprawczych (y = 1),
    n_total[i] – liczba ważnych odpowiedzi (bez odpowiedzi nieczytelnych).

Zależności: numpy, scipy.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np
from scipy import optimize, stats

PARAM_NAMES = ("theta", "k", "gamma", "lam")
EPS = 1e-9


@dataclass
class Fit:
    theta: float
    k: float
    gamma: float
    lam: float
    loglik: float
    converged: bool

    @property
    def width(self) -> float:
        """Szerokość przejścia 25–75% amplitudy (w jednostkach poziomu zasobu)."""
        return float(2.0 * np.log(3.0) / self.k)

    @property
    def theta50(self) -> float:
        """Poziom, przy którym P(x) = 0,5; NaN, gdy 0,5 leży poza [gamma, 1 - lam]."""
        if not (self.gamma < 0.5 < 1.0 - self.lam):
            return float("nan")
        q = (0.5 - self.gamma) / (1.0 - self.gamma - self.lam)
        return float(self.theta + np.log(1.0 / q - 1.0) / self.k)

    def as_dict(self) -> dict:
        d = asdict(self)
        d.update(width=self.width, theta50=self.theta50)
        return d


def psychometric(x, theta: float, k: float, gamma: float, lam: float):
    """Prawdopodobieństwo reakcji naprawczej przy poziomie zasobu x."""
    x = np.asarray(x, dtype=float)
    z = np.clip(k * (x - theta), -500, 500)
    return gamma + (1.0 - gamma - lam) / (1.0 + np.exp(z))


def _negloglik(params, levels, n_resp, n_total):
    p = np.clip(psychometric(levels, *params), EPS, 1 - EPS)
    return -np.sum(n_resp * np.log(p) + (n_total - n_resp) * np.log(1 - p))


def fit(
    levels,
    n_resp,
    n_total,
    *,
    fix_gamma: float | None = None,
    fix_lam: float | None = None,
    max_gamma: float = 0.5,
    max_lam: float = 0.5,
    theta_bounds: tuple[float, float] = (-50.0, 150.0),
    k_bounds: tuple[float, float] = (1e-3, 5.0),
    x0: tuple[float, float, float, float] | None = None,
) -> Fit:
    """Estymacja metodą największej wiarygodności (L-BFGS-B, kilka punktów startowych).

    fix_gamma / fix_lam pozwalają ustalić parametry (np. 0 dla modelu dwuparametrowego).
    x0 – dodatkowy punkt startowy (np. estymacja punktowa przy bootstrapie); wtedy
    używane są tylko 3 punkty startowe, co przyspiesza obliczenia.
    """
    levels = np.asarray(levels, dtype=float)
    n_resp = np.asarray(n_resp, dtype=float)
    n_total = np.asarray(n_total, dtype=float)
    mask = n_total > 0
    levels, n_resp, n_total = levels[mask], n_resp[mask], n_total[mask]

    p_hat = n_resp / n_total
    g0 = float(np.clip(p_hat[np.argmax(levels)], 0.0, max_gamma)) if fix_gamma is None else fix_gamma
    l0 = float(np.clip(1.0 - p_hat[np.argmin(levels)], 0.0, max_lam)) if fix_lam is None else fix_lam
    mid = g0 + (1.0 - g0 - l0) / 2.0
    # start theta: pierwszy poziom (rosnąco), przy którym p_hat spada poniżej środka zakresu
    order = np.argsort(levels)
    below = levels[order][p_hat[order] < mid]
    theta0 = float(below[0]) if below.size else float(np.median(levels))

    bounds = [
        theta_bounds,
        k_bounds,
        (fix_gamma, fix_gamma) if fix_gamma is not None else (0.0, max_gamma),
        (fix_lam, fix_lam) if fix_lam is not None else (0.0, max_lam),
    ]
    if x0 is not None:
        starts = [tuple(x0), (theta0, 0.2, g0, l0), (theta0, 1.0, g0, l0)]
    else:
        starts = [(theta0, k, g0, l0) for k in (0.05, 0.2, 1.0)] + [
            (t, 0.2, g0, l0) for t in np.quantile(levels, [0.25, 0.5, 0.75])
        ]

    best = None
    for s in starts:
        s = [float(np.clip(v, lo, hi)) for v, (lo, hi) in zip(s, bounds)]
        res = optimize.minimize(_negloglik, s, args=(levels, n_resp, n_total), method="L-BFGS-B", bounds=bounds)
        if best is None or res.fun < best.fun:
            best = res
    th, k, g, l = best.x
    return Fit(float(th), float(k), float(g), float(l), float(-best.fun), bool(best.success))


def lrt_vs_constant(levels, n_resp, n_total, fitted: Fit | None = None) -> dict:
    """Test ilorazu wiarygodności: model psychometryczny vs stałe P(x) = c (brak progu).

    Uwaga: gdy prawdziwe przejście leży poza badanym zakresem, rozkład statystyki jest
    przybliżony (chi^2 z 3 stopniami swobody); wynik traktujemy orientacyjnie.
    """
    n_resp = np.asarray(n_resp, dtype=float)
    n_total = np.asarray(n_total, dtype=float)
    fitted = fitted or fit(levels, n_resp, n_total)
    c = np.clip(n_resp.sum() / n_total.sum(), EPS, 1 - EPS)
    ll0 = float(np.sum(n_resp * np.log(c) + (n_total - n_resp) * np.log(1 - c)))
    stat = 2.0 * (fitted.loglik - ll0)
    return {"stat": stat, "df": 3, "p_value": float(stats.chi2.sf(stat, 3)), "loglik_const": ll0}


def bootstrap(
    levels,
    n_resp,
    n_total,
    *,
    B: int = 2000,
    seed: int = 0,
    ci: float = 0.95,
    **fit_kwargs,
) -> dict:
    """Nieparametryczny bootstrap: losowanie odpowiedzi ze zwracaniem w obrębie każdego poziomu.

    Zwraca estymację punktową, przedziały percentylowe i próbki bootstrapowe.
    """
    rng = np.random.default_rng(seed)
    levels = np.asarray(levels, dtype=float)
    n_resp = np.asarray(n_resp, dtype=int)
    n_total = np.asarray(n_total, dtype=int)
    point = fit(levels, n_resp, n_total, **fit_kwargs)
    p_hat = np.divide(n_resp, n_total, out=np.zeros_like(n_resp, dtype=float), where=n_total > 0)

    samples = {name: np.empty(B) for name in (*PARAM_NAMES, "width")}
    for b in range(B):
        nr = rng.binomial(n_total, p_hat)
        f = fit(levels, nr, n_total, x0=(point.theta, point.k, point.gamma, point.lam), **fit_kwargs)
        for name in PARAM_NAMES:
            samples[name][b] = getattr(f, name)
        samples["width"][b] = f.width

    a = (1.0 - ci) / 2.0
    intervals = {name: (float(np.quantile(v, a)), float(np.quantile(v, 1 - a))) for name, v in samples.items()}
    return {"fit": point, "ci": intervals, "samples": samples}


def compare(boot_a: dict, boot_b: dict, param: str = "theta", ci: float = 0.95) -> dict:
    """Różnica parametru B − A z przedziałem bootstrapowym (niezależne próby dla A i B)."""
    da = boot_a["samples"][param]
    db = boot_b["samples"][param]
    n = min(len(da), len(db))
    diff = db[:n] - da[:n]
    a = (1.0 - ci) / 2.0
    point = getattr(boot_b["fit"], param) if param != "width" else boot_b["fit"].width
    point -= getattr(boot_a["fit"], param) if param != "width" else boot_a["fit"].width
    lo, hi = float(np.quantile(diff, a)), float(np.quantile(diff, 1 - a))
    return {"param": param, "diff": float(point), "ci": (lo, hi), "excludes_zero": not (lo <= 0.0 <= hi)}


def wilson_interval(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Przedział Wilsona dla proporcji k/n (do wykresów punktów empirycznych)."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    denom = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / denom
    half = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return (float(centre - half), float(centre + half))


def simulate(levels, n_per_level: int, theta: float, k: float, gamma: float, lam: float, rng=None):
    """Symulacja odpowiedzi ze znanych parametrów (test odzyskiwania parametrów)."""
    rng = rng or np.random.default_rng()
    levels = np.asarray(levels, dtype=float)
    n_total = np.full(levels.shape, n_per_level, dtype=int)
    n_resp = rng.binomial(n_total, psychometric(levels, theta, k, gamma, lam))
    return levels, n_resp, n_total
