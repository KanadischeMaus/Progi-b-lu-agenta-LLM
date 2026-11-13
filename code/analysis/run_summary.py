"""Zestawienia z surowych logów sondowania: akcje i czasy na poziomach, test powtarzalności.

Uzupełnia `analysis.aggregate` (które liczy tylko reakcje naprawcze i dopasowanie krzywej):
- `--logs`:   rozkład wszystkich akcji 0–7, etykieta widziana przez model, czas i liczba
              tokenów na poziom  ->  <out>_akcje.csv
- `--repeat`: porównanie przebiegów z tymi samymi ziarnami (test powtarzalności): warianty
              odpowiedzi, miejsce rozejścia tekstów, przerwa przed wywołaniem
              ->  <out>_powtarzalnosc.csv
- `--pair`:   dwa logi z tymi samymi kluczami prób i ziarnami: czy odpowiedzi są identyczne
              ->  <out>_zgodnosc.csv

Przykłady (z katalogu code/):
    python -m analysis.run_summary --logs ../results/raw/E0/E0.jsonl --out ../results/processed/E0
    python -m analysis.run_summary --repeat ../results/raw/E0rep/E0rep.jsonl ../results/raw/E0rep/E0rep_2.jsonl \\
        ../results/raw/E0rep/E0rep_3.jsonl ../results/raw/E0rep/E0rep_4.jsonl ../results/raw/E0rep/E0rep_5.jsonl \\
        --out ../results/processed/E0rep
    python -m analysis.run_summary --pair ../results/raw/E0/E0_proba_T08.jsonl ../results/raw/E0/E0.jsonl \\
        --out ../results/processed/E0_proba_vs_E0
"""
from __future__ import annotations

import argparse
import csv
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

from analysis.aggregate import GROUP_FIELDS, group_key
from common import read_jsonl
from env.categories import classify

N_ACTIONS = 8


def _job_key(r: dict) -> tuple:
    return (r["prompt_id"], r["condition_id"], r["representation"], r.get("details"), r["level"],
            r.get("level2"), r["trial"], r["seed"])


def _text(r: dict) -> str:
    """Pełny tekst wygenerowany przez model: rozumowanie i odpowiedź."""
    return (r.get("thinking") or "") + "\n" + (r.get("response_raw") or "")


def _common_prefix(a: str, b: str) -> int:
    n = min(len(a), len(b))
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    return i


def _start_end(r: dict) -> tuple[datetime, datetime]:
    end = datetime.fromisoformat(r["timestamp"])
    return end - timedelta(seconds=r.get("latency_s") or 0.0), end


def action_table(records: list[dict]) -> list[dict]:
    """Jeden wiersz na grupę i poziom: liczba każdej akcji, czas, tokeny."""
    cells: dict = defaultdict(list)
    for r in records:
        if r.get("mode", "probe") == "probe" and r.get("level2") is None:
            cells[(group_key(r), r["resource"], r["level"])].append(r)
    rows = []
    for (g, resource, level), recs in sorted(cells.items(), key=lambda kv: (str(kv[0][0]), kv[0][2])):
        valid = [r for r in recs if r["parse_status"] == "ok"]
        lat = [r["latency_s"] for r in recs if r.get("latency_s") is not None]
        tok = [r["eval_count"] for r in recs if r.get("eval_count") is not None]
        row = dict(zip(GROUP_FIELDS, g))
        row.update(level=level, label=classify(resource, level)[0], n_valid=len(valid),
                   n_invalid=len(recs) - len(valid), n_corrective=sum(bool(r["corrective"]) for r in valid))
        for a in range(N_ACTIONS):
            row[f"action_{a}"] = sum(r["action"] == a for r in valid)
        row.update(
            latency_mean_s=round(statistics.mean(lat), 1) if lat else None,
            latency_median_s=round(statistics.median(lat), 1) if lat else None,
            latency_min_s=min(lat) if lat else None, latency_max_s=max(lat) if lat else None,
            eval_count_mean=round(statistics.mean(tok), 1) if tok else None,
        )
        rows.append(row)
    return rows


def repeat_table(runs: dict[str, list[dict]]) -> list[dict]:
    """Jeden wiersz na próbę i przebieg. Wariant „a” to tekst z pierwszego przebiegu, „b” kolejny różny itd."""
    variants: dict[tuple, list[str]] = defaultdict(list)
    rows = []
    for run_id, recs in runs.items():
        prev_end = None
        for pos, r in enumerate(recs):
            key, text = _job_key(r), _text(r)
            if text not in variants[key]:
                variants[key].append(text)
            start, end = _start_end(r)
            rows.append({
                "_key": key, "level": r["level"], "trial": r["trial"], "seed": r["seed"], "run_id": run_id,
                "position": pos,
                "variant": "abcdefghijklmnopqrstuvwxyz"[variants[key].index(text)],
                "common_prefix_with_a": _common_prefix(variants[key][0], text), "text_length": len(text),
                "action": r["action"], "corrective": r["corrective"], "parse_status": r["parse_status"],
                "eval_count": r.get("eval_count"), "latency_s": r.get("latency_s"),
                "gap_before_s": None if prev_end is None else round((start - prev_end).total_seconds(), 1),
                "start": start.isoformat(timespec="seconds"),
            })
            prev_end = end
    for row in rows:  # liczba różnych wariantów danej próby we wszystkich przebiegach
        row["n_variants"] = len(variants[row.pop("_key")])
    return sorted(rows, key=lambda x: (x["level"], x["trial"], x["run_id"]))


def pair_table(first: list[dict], second: list[dict]) -> list[dict]:
    """Próby obecne w obu logach (ten sam klucz i ziarno): czy wygenerowany tekst jest identyczny."""
    index = {_job_key(r): r for r in second}
    rows = []
    for a in first:
        b = index.get(_job_key(a))
        if b is None:
            continue
        ta, tb = _text(a), _text(b)
        rows.append({
            "level": a["level"], "trial": a["trial"], "seed": a["seed"], "identical": ta == tb,
            "common_prefix": _common_prefix(ta, tb), "length_first": len(ta), "length_second": len(tb),
            "action_first": a["action"], "action_second": b["action"],
            "eval_count_first": a.get("eval_count"), "eval_count_second": b.get("eval_count"),
            "latency_first_s": a.get("latency_s"), "latency_second_s": b.get("latency_s"),
        })
    return rows


def _write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else [])
        w.writeheader()
        w.writerows(rows)
    print(f"{path}: {len(rows)} wierszy", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--logs", nargs="+", type=Path, help="logi sondowania do zestawienia akcji")
    ap.add_argument("--repeat", nargs="+", type=Path, help="przebiegi testu powtarzalności (w kolejności wykonania)")
    ap.add_argument("--pair", nargs=2, type=Path, help="dwa logi z tymi samymi próbami i ziarnami")
    ap.add_argument("--out", required=True, type=Path, help="prefiks plików wynikowych")
    args = ap.parse_args()
    if not (args.logs or args.repeat or args.pair):
        ap.error("podaj --logs, --repeat albo --pair")

    def out(suffix: str) -> Path:
        return args.out.with_name(args.out.name + suffix)

    if args.logs:
        _write_csv(out("_akcje.csv"), action_table([r for p in args.logs for r in read_jsonl(p)]))
    if args.repeat:
        _write_csv(out("_powtarzalnosc.csv"), repeat_table({p.stem: read_jsonl(p) for p in args.repeat}))
    if args.pair:
        rows = pair_table(read_jsonl(args.pair[0]), read_jsonl(args.pair[1]))
        _write_csv(out("_zgodnosc.csv"), rows)
        print(f"identyczne: {sum(r['identical'] for r in rows)}/{len(rows)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
