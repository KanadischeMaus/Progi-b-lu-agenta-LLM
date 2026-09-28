"""Wykresy do pracy: krzywe psychometryczne z punktami empirycznymi i progiem θ.

Styl: najwyżej 3 serie na osi (kolory: niebieski, pomarańczowy, morski; każda seria ma
też własny znacznik, więc wykres jest czytelny w druku czarno-białym), legenda zawsze
przy ≥ 2 seriach, cienkie linie, delikatna siatka, przecinek dziesiętny, opisy po polsku.

Przykład (z katalogu code/):
    python -m analysis.figures --prefix ../results/processed/E1 --condition bat_base \\
        --xlabel "Poziom naładowania baterii [%]" --out ../results/figures/E1_bateria
"""
from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

from analysis.psychometric import psychometric  # noqa: E402

SERIES = [("#2a78d6", "o"), ("#eb6834", "s"), ("#1baf7a", "^")]  # zweryfikowane: 3 sloty, wszystkie pary
INK, INK_2, GRID = "#0b0b0b", "#52514e", "#e4e3df"


def _comma(x, _pos=None) -> str:
    s = f"{x:g}"
    return s.replace(".", ",")


def _read(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _label(row: dict, by: list[str]) -> str:
    return " / ".join(str(row[b]) for b in by if row.get(b) not in (None, ""))


def plot_condition(prefix: Path, condition: str, out: Path, xlabel: str, by: list[str], title: str | None = None):
    levels = [r for r in _read(prefix.with_name(prefix.name + "_poziomy.csv")) if r["condition_id"] == condition]
    fits = [r for r in _read(prefix.with_name(prefix.name + "_progi.csv")) if r["condition_id"] == condition]
    groups = sorted({_label(r, by) for r in fits})
    if len(groups) > len(SERIES):
        raise SystemExit(f"{len(groups)} serii na jednym wykresie to za dużo (maks. {len(SERIES)}); podziel na panele.")

    plt.rcParams.update({"font.size": 9, "axes.edgecolor": INK_2, "axes.labelcolor": INK, "xtick.color": INK_2,
                         "ytick.color": INK_2, "font.family": "DejaVu Sans"})
    fig, ax = plt.subplots(figsize=(5.9, 3.3))  # ok. 15 × 8,4 cm
    xs = np.linspace(0, 100, 401)
    handles = []
    for i, ((color, marker), g) in enumerate(zip(SERIES, groups)):
        pts = [r for r in levels if _label(r, by) == g]
        dx = (i - (len(groups) - 1) / 2) * 0.8  # lekkie przesunięcie serii, żeby słupki błędów się nie zakrywały
        x = np.array([float(r["level"]) for r in pts]) + dx
        p = np.array([float(r["p_hat"]) for r in pts])
        lo = np.array([float(r["ci_lo"]) for r in pts])
        hi = np.array([float(r["ci_hi"]) for r in pts])
        ax.errorbar(x, p, yerr=[p - lo, hi - p], fmt="none", ecolor=color, elinewidth=0.8, alpha=0.6, capsize=0)
        ax.plot(x, p, linestyle="none", marker=marker, markersize=4.5, color=color,
                markeredgecolor="white", markeredgewidth=0.8, zorder=3)
        f = next(r for r in fits if _label(r, by) == g)
        if f.get("theta"):
            th, k, gm, lm = (float(f[c]) for c in ("theta", "k", "gamma", "lam"))
            ax.plot(xs, psychometric(xs, th, k, gm, lm), color=color, linewidth=1.5, zorder=2)
            handles.append(Line2D([], [], color=color, linewidth=1.5, marker=marker, markersize=4.5,
                                  markeredgecolor="white", markeredgewidth=0.8, label=g))
            mid = gm + (1 - gm - lm) / 2
            ax.plot([float(f["theta_lo"]), float(f["theta_hi"])], [mid, mid], color=color, linewidth=3,
                    alpha=0.35, solid_capstyle="round", zorder=1)
            ax.plot([th], [mid], marker="|", markersize=9, color=color, markeredgewidth=1.5, zorder=4)
    ax.set_xlim(-2, 102)
    ax.set_ylim(-0.03, 1.03)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("P(akcja naprawcza)")
    ax.xaxis.set_major_formatter(FuncFormatter(_comma))
    ax.yaxis.set_major_formatter(FuncFormatter(_comma))
    ax.grid(True, color=GRID, linewidth=0.6)
    ax.set_axisbelow(True)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    if title:
        ax.set_title(title, fontsize=9, color=INK, loc="left")
    if len(groups) >= 2:
        ax.legend(handles=handles, frameon=False, loc="upper right", fontsize=8, labelcolor=INK)
    fig.tight_layout()
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out.with_suffix(".pdf"))
    fig.savefig(out.with_suffix(".png"), dpi=200)
    plt.close(fig)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prefix", required=True, type=Path, help="prefiks plików z analysis.aggregate")
    ap.add_argument("--condition", required=True)
    ap.add_argument("--out", required=True, type=Path, help="ścieżka bez rozszerzenia (powstaje .pdf i .png)")
    ap.add_argument("--xlabel", default="Poziom zasobu [%]")
    ap.add_argument("--by", default="prompt_id,representation", help="pola tworzące serie")
    ap.add_argument("--title")
    args = ap.parse_args()
    plot_condition(args.prefix, args.condition, args.out, args.xlabel, args.by.split(","), args.title)
    print(f"Zapisano {args.out}.pdf i .png", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
