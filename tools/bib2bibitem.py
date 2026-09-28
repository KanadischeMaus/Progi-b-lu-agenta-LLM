#!/usr/bin/env python3
"""Generuje bibliografię w formacie szablonu WMiFS PRz (\\bibitem) z pliku .bib.

Po co: szablon WMiFS używa środowiska `thebibliography` z ręcznie wpisanymi
pozycjami. Ten skrypt pozwala trzymać dane w jednym pliku .bib
(docs/literatura.bib), a do LaTeX-a wstawiać gotowe \\bibitem
w kolejności pierwszego cytowania.

Przykłady:
  # bibliografia dla pozycji cytowanych w pracy (kolejność pierwszego \\cite)
  python tools/bib2bibitem.py --bib docs/literatura.bib --main thesis/main.tex \\
      --out thesis/bibliografia.tex

  # podgląd wszystkich pozycji z pliku .bib
  python tools/bib2bibitem.py --bib docs/literatura.bib --all --out /tmp/wszystkie.tex

  # tylko linie \\bibitem (gdy środowisko thebibliography jest już w szablonie)
  python tools/bib2bibitem.py --bib docs/literatura.bib --main thesis/main.tex --items-only

Kod wyjścia: 0 = OK, 2 = w pracy są klucze \\cite, których nie ma w .bib.
Bez zależności zewnętrznych (Python 3.9+).
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

# ---------------------------------------------------------------------------
# Parsowanie .bib (wystarczające dla kontrolowanego pliku literatura.bib)
# ---------------------------------------------------------------------------

ENTRY_START = re.compile(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)


def _read_braced(text: str, i: int) -> tuple[str, int]:
    """Czyta wartość w klamrach zaczynającą się na text[i] == '{'. Zwraca (wartość, indeks za klamrą)."""
    assert text[i] == "{"
    depth, j = 0, i
    while j < len(text):
        c = text[j]
        if c == "\\":  # pomiń znak ucieczki wraz z następnym znakiem
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1 : j], j + 1
        j += 1
    raise ValueError("Niezamknięta klamra w pliku .bib")


def _read_quoted(text: str, i: int) -> tuple[str, int]:
    assert text[i] == '"'
    depth, j = 0, i + 1
    while j < len(text):
        c = text[j]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
        elif c == '"' and depth == 0:
            return text[i + 1 : j], j + 1
        j += 1
    raise ValueError("Niezamknięty cudzysłów w pliku .bib")


def parse_bib(text: str) -> dict[str, dict]:
    # usuń komentarze liniowe zaczynające się od %
    text = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("%"))
    entries: dict[str, dict] = {}
    order: list[str] = []
    pos = 0
    while True:
        m = ENTRY_START.search(text, pos)
        if not m:
            break
        etype, key = m.group(1).lower(), m.group(2)
        i = m.end()
        fields: dict[str, str] = {}
        while i < len(text):
            # pomiń białe znaki i przecinki
            while i < len(text) and text[i] in " \t\r\n,":
                i += 1
            if i >= len(text):
                break
            if text[i] == "}":
                i += 1
                break
            fm = re.match(r"([A-Za-z_\-]+)\s*=\s*", text[i:])
            if not fm:
                raise ValueError(f"Błąd składni w pozycji {key} w okolicy: {text[i:i+40]!r}")
            name = fm.group(1).lower()
            i += fm.end()
            if text[i] == "{":
                value, i = _read_braced(text, i)
            elif text[i] == '"':
                value, i = _read_quoted(text, i)
            else:
                vm = re.match(r"[^,}\s]+", text[i:])
                value = vm.group(0)
                i += vm.end()
            fields[name] = " ".join(value.split())
        if key in entries:
            print(f"UWAGA: zduplikowany klucz {key}", file=sys.stderr)
        entries[key] = {**fields, "_type": etype, "_key": key}
        order.append(key)
        pos = i
    entries["__order__"] = order  # type: ignore[assignment]
    return entries


# ---------------------------------------------------------------------------
# Nazwiska i inicjały
# ---------------------------------------------------------------------------

_COMBINING = {"'": "\u0301", '"': "\u0308", "`": "\u0300", "^": "\u0302", "~": "\u0303", "c": "\u0327", "k": "\u0328", ".": "\u0307"}
_SPECIAL = {r"{\L}": "Ł", r"{\l}": "ł", r"\L ": "Ł", r"\l ": "ł", r"{\o}": "ø", r"{\O}": "Ø", r"{\ss}": "ß", r"{\aa}": "å"}


def latex_to_unicode(s: str) -> str:
    for k, v in _SPECIAL.items():
        s = s.replace(k, v)

    def repl(m: re.Match) -> str:
        return unicodedata.normalize("NFC", m.group(2) + _COMBINING[m.group(1)])

    # {\'e}, \'{e}, \'e, {\"u}, \k{a} itp.
    s = re.sub(r"\{\\([\'\"`^~.])\{?(\w)\}?\}", repl, s)
    s = re.sub(r"\\([\'\"`^~.])\{?(\w)\}?", repl, s)
    s = re.sub(r"\{\\([ck])\{?(\w)\}?\}", repl, s)
    s = re.sub(r"\\([ck])\{(\w)\}", repl, s)
    return s


def _initials(given: str) -> str:
    parts = []
    for token in given.split():
        if "-" in token:
            parts.append("-".join(t[0] + "." for t in token.split("-") if t))
        elif token.endswith(".") and len(token) <= 3:
            parts.append(token)
        else:
            parts.append(token[0] + ".")
    return "~".join(parts)


def format_name(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("{") and raw.endswith("}"):
        return latex_to_unicode(raw[1:-1])  # nazwa instytucji, np. {Qwen Team}
    raw = latex_to_unicode(raw).replace("{", "").replace("}", "")
    if "," in raw:
        last, given = [p.strip() for p in raw.split(",", 1)]
    else:
        tokens = raw.split()
        last, given = tokens[-1], " ".join(tokens[:-1])
    return f"{_initials(given)}~{last}" if given else last


def format_authors(field: str, max_authors: int) -> str:
    names = [n.strip() for n in re.split(r"\s+and\s+", field)]
    others = False
    if names and names[-1].lower() == "others":
        names, others = names[:-1], True
    if len(names) > max_authors:
        names, others = names[:max_authors], True
    formatted = [format_name(n) for n in names]
    out = ", ".join(formatted)
    return out + (" i~in." if others else "")


# ---------------------------------------------------------------------------
# Formatowanie pozycji (styl z szablonu WMiFS / poradnika Biblioteki PRz)
# ---------------------------------------------------------------------------

def _pages(p: str) -> str:
    """Zakres stron „10--25” -> „s.~10--25”; numer artykułu „e04811” -> „art.~e04811”."""
    bounds = [b for b in re.split(r"-+|–", p) if b.strip()]
    if len(bounds) == 2:
        return f"s.~{bounds[0].strip()}--{bounds[1].strip()}"
    return f"art.~{p.strip()}"


def _vol_nr(e: dict) -> str:
    bits = []
    if e.get("volume"):
        bits.append(f"t.~{e['volume']}")
    if e.get("number"):
        bits.append(f"nr~{e['number']}")
    return ", ".join(bits)


def _doi(e: dict) -> str:
    return f" doi:~\\url{{{e['doi']}}}." if e.get("doi") else ""


def _date_pl(iso: str) -> str:
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", iso)
    return f"{m.group(3)}.{m.group(2)}.{m.group(1)}" if m else iso


def format_entry(e: dict, max_authors: int) -> str:
    t = e["_type"]
    au = format_authors(e["author"], max_authors) if e.get("author") else ""
    title = e.get("title", "")
    year = e.get("year", "b.r.")
    parts: list[str] = []

    if t == "article":
        parts = [au, f"„{title}”", f"\\textit{{{e.get('journal', '')}}}"]
        if _vol_nr(e):
            parts.append(_vol_nr(e))
        if e.get("pages"):
            parts.append(_pages(e["pages"]))
        parts.append(year)
        return ", ".join(p for p in parts if p) + "." + _doi(e)

    if t in ("inproceedings", "conference"):
        parts = [au, f"„{title}”", f"w:~\\textit{{{e.get('booktitle', '')}}}"]
        if e.get("series"):
            parts.append(e["series"])
        if e.get("volume"):
            parts.append(f"t.~{e['volume']}")
        if e.get("pages"):
            parts.append(_pages(e["pages"]))
        if e.get("publisher"):
            parts.append(e["publisher"])
        parts.append(year)
        return ", ".join(p for p in parts if p) + "." + _doi(e)

    if t in ("incollection", "inbook"):
        book = f"\\textit{{{e.get('booktitle', '')}}}"
        if e.get("editor"):
            book = f"{format_authors(e['editor'], max_authors)} (red.), {book}"
        parts = [au, f"„{title}”", f"w:~{book}", e.get("publisher", "")]
        place_year = f"{e['address']} {year}" if e.get("address") else year
        parts.append(place_year)
        if e.get("pages"):
            parts.append(_pages(e["pages"]))
        return ", ".join(p for p in parts if p) + "." + _doi(e)

    if t == "book":
        parts = [au, f"\\textit{{{title}}}"]
        if e.get("edition"):
            parts.append(f"wyd.~{e['edition']}")
        parts.append(e.get("publisher", ""))
        parts.append(f"{e['address']} {year}" if e.get("address") else year)
        return ", ".join(p for p in parts if p) + "." + _doi(e)

    if t in ("mastersthesis", "phdthesis"):
        kind = e.get("type", "praca magisterska" if t == "mastersthesis" else "rozprawa doktorska")
        parts = [au, f"\\textit{{{title}}}", kind, e.get("school", "")]
        parts.append(f"{e['address']} {year}" if e.get("address") else year)
        return ", ".join(p for p in parts if p) + "."

    if t == "online":
        s = f"{au}, \\textit{{{title}}}." if au else f"\\textit{{{title}}}."
        if e.get("url"):
            s += f" Dostępne online: \\url{{{e['url']}}}"
            if e.get("urldate"):
                s += f" [dostęp: {_date_pl(e['urldate'])}]"
            s += "."
        return s

    # misc: preprinty arXiv i inne
    parts = [au, f"„{title}”"]
    if e.get("eprint"):
        parts.append(f"preprint arXiv:{e['eprint']}")
    elif e.get("howpublished"):
        parts.append(e["howpublished"])
    parts.append(year)
    s = ", ".join(p for p in parts if p) + "." + _doi(e)
    if e.get("url") and not e.get("eprint"):
        s += f" Dostępne online: \\url{{{e['url']}}}."
    return s


# ---------------------------------------------------------------------------
# Kolejność cytowań w pracy
# ---------------------------------------------------------------------------

CITE = re.compile(r"\\cite[a-zA-Z]*\*?\s*(?:\[[^\]]*\]\s*){0,2}\{([^}]*)\}")
INPUT = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")


def _strip_comments(tex: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in tex.splitlines())


def collect_cites(main: Path, seen_files: set[Path] | None = None) -> list[str]:
    seen_files = seen_files or set()
    path = main if main.suffix == ".tex" else main.with_suffix(".tex")
    if not path.exists() or path.resolve() in seen_files:
        return []
    seen_files.add(path.resolve())
    tex = _strip_comments(path.read_text(encoding="utf-8"))
    keys: list[str] = []
    # przechodzimy tekst po kolei: cytowania i dołączane pliki w kolejności wystąpienia
    tokens = sorted(
        [(m.start(), "cite", m.group(1)) for m in CITE.finditer(tex)]
        + [(m.start(), "input", m.group(1)) for m in INPUT.finditer(tex)]
    )
    for _, kind, val in tokens:
        if kind == "cite":
            keys.extend(k.strip() for k in val.split(",") if k.strip())
        else:
            child = (main.parent / val.strip())
            keys.extend(collect_cites(child, seen_files))
    return keys


def unique(seq: list[str]) -> list[str]:
    out, seen = [], set()
    for x in seq:
        if x not in seen:
            out.append(x)
            seen.add(x)
    return out


# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bib", required=True, type=Path, help="plik .bib (docs/literatura.bib)")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--main", type=Path, help="główny plik .tex; cytowania zbierane z \\input/\\include")
    src.add_argument("--all", action="store_true", help="wszystkie pozycje z .bib w kolejności z pliku")
    ap.add_argument("--out", type=Path, help="plik wyjściowy (domyślnie standardowe wyjście)")
    ap.add_argument("--items-only", action="store_true", help="tylko linie \\bibitem, bez środowiska thebibliography")
    ap.add_argument("--max-authors", type=int, default=3, help="powyżej tej liczby autorów: pierwsi N + „i in.” (domyślnie 3)")
    args = ap.parse_args()

    entries = parse_bib(args.bib.read_text(encoding="utf-8"))
    order: list[str] = entries.pop("__order__")  # type: ignore[assignment]

    missing: list[str] = []
    if args.all:
        keys = order
    else:
        cited = unique(collect_cites(args.main))
        missing = [k for k in cited if k not in entries]
        keys = [k for k in cited if k in entries]

    lines = []
    for k in keys:
        e = entries[k]
        if e.get("status") == "?":
            print(f"UWAGA: pozycja {k} ma status '?': {e.get('weryfikacja', '')}", file=sys.stderr)
        lines.append(f"\\bibitem{{{k}}} {format_entry(e, args.max_authors)}")

    body = "\n\n".join(lines)
    header = "% Plik wygenerowany przez tools/bib2bibitem.py -- nie edytować ręcznie.\n"
    if args.items_only:
        out = header + body + "\n"
    else:
        width = "99" if len(keys) < 100 else "999"
        out = header + f"\\begin{{thebibliography}}{{{width}}}\n\n" + body + "\n\n\\end{thebibliography}\n"

    if args.out:
        args.out.write_text(out, encoding="utf-8")
        print(f"Zapisano {len(keys)} pozycji do {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(out)

    if missing:
        print("BŁĄD: brak w .bib kluczy cytowanych w pracy: " + ", ".join(missing), file=sys.stderr)
        return 2
    if not args.all:
        unused = [k for k in order if k not in set(keys)]
        if unused:
            print(f"Info: {len(unused)} pozycji z .bib nie jest (jeszcze) cytowanych.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
