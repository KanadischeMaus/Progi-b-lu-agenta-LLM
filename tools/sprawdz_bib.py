#!/usr/bin/env python3
"""Audyt metadanych i dostępności pozycji z docs/literatura.bib (OpenAlex, doi.org).

Skrypt tylko czyta plik .bib. Dla każdej pozycji:
- z DOI: rekord OpenAlex po DOI i sprawdzenie DOI w doi.org (Handle API);
- z numerem arXiv (bez DOI): rekord OpenAlex po DOI arXiv (10.48550/arXiv.<numer>);
- bez DOI i arXiv: wyszukiwanie w OpenAlex po tytule (uwaga „dopasowanie po tytule”);
- książki, strony WWW, praca dyplomowa: klasyfikacja ręczna (słownik RECZNIE, uwaga „ręcznie”).

Porównuje autorów, tytuł, rok, tom i strony. Wyznacza kategorię dostępności według D12
(docs/03): A = diamond/gold/hybrid/bronze albo otwarty serwis wydawcy, B = green, C = closed.
Preprint, którego miejscem publikacji jest arXiv, ma kategorię A.

Wynik: CSV (domyślnie docs/bib_audyt.csv), podsumowanie i tabela pokrycia podrozdziałów
na standardowe wyjście.

OpenAlex działa bez klucza (dzienny budżet). Jeśli ustawiono zmienną OPENALEX_API_KEY,
skrypt dołącza ją do zapytań i nigdzie jej nie zapisuje.

Przykład:
  python tools/sprawdz_bib.py --bib docs/literatura.bib --out docs/bib_audyt.csv

Kod wyjścia: 0 = OK, 3 = limit OpenAlex wyczerpany (HTTP 429); ustaw OPENALEX_API_KEY i uruchom ponownie.
Bez zależności zewnętrznych (Python 3.9+).
"""
from __future__ import annotations

import argparse
import csv
import difflib
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bib2bibitem import latex_to_unicode, parse_bib  # noqa: E402

OPENALEX = "https://api.openalex.org"
UA = "sprawdz_bib.py (audyt bibliografii pracy magisterskiej)"
KOLUMNY = ["klucz", "kategoria", "oa_status", "oa_url", "wersja", "rozbieżności", "uwagi",
           "typ", "recenzowana", "cited_by_count", "is_retracted"]
KAT_OA = {"diamond": "A", "gold": "A", "hybrid": "A", "bronze": "A", "green": "B", "closed": "C"}

# Pozycje spoza OpenAlex: kategoria nadana ręcznie (uzasadnienie w uwagach).
RECZNIE = {
    "russell2020artificial": ("C", "podręcznik, brak legalnej bezpłatnej kopii (wyjątek w docs/03)"),
    "sutton2018reinforcement": ("B", "PDF autorów (drugi druk 2020) na incompleteideas.net"),
    "kingdom2016psychophysics": ("C", "podręcznik, brak bezpłatnej kopii (zamiennik: prins2018applying)"),
    "astrom2021feedback": ("B", "PDF 2. wydania na wiki autorów (fbswiki.org)"),
    "zawislak2025budowa": ("C", "praca dyplomowa bez publicznego egzemplarza (wyjątek w docs/03)"),
    "ollama2026api": ("A", "strona WWW, bezpłatna"),
    "deepseek2025distillcard": ("A", "strona WWW, bezpłatna"),
    "opi2023jsa": ("A", "strona WWW, bezpłatna (nie do pracy)"),
    "wmifs2025wymagania": ("A", "strona WWW, bezpłatna (nie do pracy)"),
    "ren2026ai": ("A", "manuskrypt na stronie autorów; kopia w Web Archive (pole weryfikacja)"),
}

# Rozbieżności sprawdzone u źródła pierwotnego (2026-10-08): wyjaśnienie trafia do uwag.
ZNANE = {
    "vaswani2017attention": "błąd OpenAlex: rekord scalony z przedrukiem z 2025 r. (DOI 10.65215/2q58a426, Crossref: Shenzhen Medical Academy); tego DOI nie dopisywać, dane NeurIPS 2017 w .bib są poprawne",
    "long2024taking": "błąd OpenAlex: rekord arXiv ma tytuł innej pracy; arXiv API potwierdza tytuł i autorów z .bib",
    "tagliabue2026pain": "błąd OpenAlex: rekord arXiv ma tytuł innej pracy (replikacji); arXiv API potwierdza tytuł v2 i autorów z .bib",
    "oudeyer2007intrinsic": "błąd OpenAlex i Crossref (1 autor); strona Frontiers i Europe PMC (PMC2533589) podają 2 autorów jak .bib",
    "theraulaz1998response": "tytuł w .bib poprawiony 2026-10-08 według Crossref (Royal Society) i PMC1688885; nazwisko „Denuebourg” to literówka w metadanych wydawcy",
    "kuss2005bayesian": "OpenAlex podaje numer artykułu (8) zamiast stron 478–492; oba zapisy funkcjonują",
    "starzyk2012motivated": "rok OpenAlex = wersja online (2011), .bib = numer (2012)",
    "graham2015opportunistic": "rok OpenAlex = wersja online (IX 2014), .bib = numer (VIII 2015)",
    "starzyk2017mlecog": "rok OpenAlex = wersja online (2015), .bib = numer (2017)",
    "starzyk2017needs": "rok OpenAlex = wersja online (2016), .bib = numer (2017)",
    "kuehn2017artificial": "rok OpenAlex = wersja online (2016), .bib = numer (2017)",
    "sharkey2025could": "rok OpenAlex = wersja online (2024), .bib = numer (2025)",
    "butlin2026identifying": "rok OpenAlex = wersja online (2025), .bib = numer (VI 2026)",
    "hagendorff2023machine": "rok OpenAlex = v1 (2023), .bib = cytowana wersja v6 (2024)",
    "schlatter2026incomplete": "rok OpenAlex = v1 (2025), .bib = cytowana wersja v2 (2026)",
}

# Legalne kopie pozycji C i spornych B, wyszukane ręcznie (2026-10-08): strona autora,
# repozytorium uczelni, PMC. Serwisów pirackich i materiałów kursów nie uwzględniamy.
STARZYK = "http://ace.cs.ohio.edu/~starzyk/network/Research/Papers/"
KOPIE = {
    "starzyk2011motivated": STARZYK + "Motivated%20Learning%20for%20Computational%20Intelligence.pdf (strona autora, wersja autorska)",
    "starzyk2012motivated": STARZYK + "Motivated_Learning_for_Autonomous_Development.pdf (strona autora, preprint); kopia SMU z OpenAlex niesprawdzalna automatycznie",
    "graham2015opportunistic": "nie spełnia D12 (decyzja autora 2026-10-08): " + STARZYK + "Opportunistic%20agent%202015.pdf (strona autora, wersja wydawnicza)",
    "starzyk2017mlecog": "nie spełnia D12 (decyzja autora 2026-10-08): " + STARZYK + "MLECOG%202017.pdf (strona autora, wersja wydawnicza)",
    "starzyk2017needs": "nie spełnia D12 (decyzja autora 2026-10-08): " + STARZYK + "Needs,%20pains,%20motivations%202017.pdf (strona autora, wersja wydawnicza)",
    "maslow1943theory": "https://psychclassics.yorku.ca/Maslow/motivation.htm (Classics in the History of Psychology, York University; z paginacją oryginału)",
    "ryan2000self": "https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf (Center for Self-Determination Theory, strona autorów; skan wersji wydawniczej APA)",
    "singh2010intrinsically": "https://web.eecs.umich.edu/~baveja/Papers/IMRLIEEETAMDFinal.pdf (strona autora, wersja autorska z inną paginacją)",
    "kuehn2017artificial": "mediaTUM node 1438519 (wskazana przez OpenAlex, wersja zgłoszona); ochrona przed botami, do sprawdzenia w przeglądarce",
    "theraulaz1998response": "https://pmc.ncbi.nlm.nih.gov/articles/PMC1688885/ (PMC, sprawdzone)",
    "man2019homeostasis": "brak",
    "bonabeau1996quantitative": "brak (Royal Society: closed, brak kopii w repozytoriach)",
    "russell2020artificial": "brak",
    "tversky1981framing": "brak (kopie tylko w materiałach kursów i serwisach bez zgody wydawcy)",
    "kingdom2016psychophysics": "brak",
    "holm1979simple": "JSTOR: bezpłatny odczyt po rejestracji (wg raportu z 08.10; JSTOR blokuje automat)",
    "zawislak2025budowa": "brak",
}

# Serwisy, w których pełny tekst jest bezpłatny u wydawcy (D12, kategoria A),
# także gdy OpenAlex zna tylko kopię w repozytorium.
OTWARTE_SERWISY = [
    (lambda e: e.get("doi", "").startswith("10.18653/"), "ACL Anthology"),
    (lambda e: "International Conference on Learning Representations" in e.get("booktitle", ""), "OpenReview (ICLR)"),
    (lambda e: "Transactions on Machine Learning Research" in e.get("journal", ""), "OpenReview (TMLR)"),
    (lambda e: "Neural Information Processing Systems" in e.get("booktitle", ""), "proceedings.neurips.cc"),
    (lambda e: "Proceedings of Machine Learning Research" in e.get("series", ""), "PMLR"),
    (lambda e: "Transactions of the Association for Computational Linguistics" in e.get("journal", ""), "TACL (MIT Press, otwarty dostęp)"),
]


class LimitWyczerpany(Exception):
    pass


# ---------------------------------------------------------------------------
# Sieć (z opcjonalną pamięcią podręczną, żeby powtórne uruchomienie nie zużywało budżetu)
# ---------------------------------------------------------------------------

class Siec:
    def __init__(self, cache: Path | None, api_key: str | None):
        self.cache, self.api_key = cache, api_key
        if cache:
            cache.mkdir(parents=True, exist_ok=True)

    def _plik(self, url: str) -> Path | None:
        return self.cache / (hashlib.sha1(url.encode()).hexdigest() + ".json") if self.cache else None

    def get_json(self, url: str, openalex: bool = False) -> tuple[int, dict | None]:
        plik = self._plik(url)
        if plik and plik.exists():
            d = json.loads(plik.read_text(encoding="utf-8"))
            return d["status"], d["body"]
        full = url
        if openalex and self.api_key:
            full += ("&" if "?" in url else "?") + "api_key=" + urllib.parse.quote(self.api_key)
        req = urllib.request.Request(full, headers={"User-Agent": UA, "Accept": "application/json"})
        for proba in range(3):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    status, body = r.status, json.loads(r.read().decode("utf-8"))
                break
            except urllib.error.HTTPError as e:
                if e.code == 429 and openalex:
                    raise LimitWyczerpany(url)
                if e.code in (404, 410):
                    status, body = e.code, None
                    break
                if proba == 2:
                    raise
            except urllib.error.URLError:
                if proba == 2:
                    raise
            time.sleep(2 * (proba + 1))
        if plik:
            plik.write_text(json.dumps({"status": status, "body": body}), encoding="utf-8")
        time.sleep(0.15)
        return status, body

    def url_dziala(self, url: str) -> str:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": UA, "Range": "bytes=0-1023"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return f"HTTP {r.status}"
        except urllib.error.HTTPError as e:
            return f"HTTP {e.code}"
        except Exception as e:  # noqa: BLE001
            return f"błąd: {type(e).__name__}"


# ---------------------------------------------------------------------------
# Normalizacja i porównania
# ---------------------------------------------------------------------------

def norm(s: str) -> str:
    s = latex_to_unicode(s or "").replace("{", "").replace("}", "").replace("\\", "")
    s = s.replace("``", '"').replace("''", '"').replace("--", "-")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).replace("ı", "i")
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def nazwiska_bib(field: str) -> tuple[list[str], bool]:
    names = [n.strip() for n in re.split(r"\s+and\s+", field or "") if n.strip()]
    others = bool(names) and names[-1].lower() == "others"
    if others:
        names = names[:-1]
    out = []
    for n in names:
        if n.startswith("{") and n.endswith("}"):
            return [], others  # autor instytucjonalny: bez porównania
        out.append(norm(n.split(",")[0] if "," in n else n.split()[-1]))
    return out, others


def nazwiska_oa(rec: dict) -> list[str]:
    return [norm(a.get("raw_author_name") or a.get("author", {}).get("display_name") or "")
            for a in rec.get("authorships", [])]


def zgodny_autor(bib_last: str, oa_full: str) -> bool:
    if not bib_last or not oa_full:
        return False
    return bib_last in oa_full or oa_full.split()[-1] in bib_last.split()


def porownaj(e: dict, rec: dict) -> list[str]:
    roz = []
    # tytuł
    tb, to = norm(e.get("title", "")), norm(rec.get("title") or rec.get("display_name") or "")
    if tb != to:
        if to.startswith(tb) or tb.startswith(to):
            roz.append(f"tytuł: różnica w podtytule (OpenAlex: „{rec.get('title')}”)")
        else:
            roz.append(f"tytuł: OpenAlex „{rec.get('title')}”")
    # rok
    yb, yo = str(e.get("year", "")), str(rec.get("publication_year") or "")
    if yb and yo and yb != yo:
        roz.append(f"rok: .bib {yb}, OpenAlex {yo}")
    # autorzy
    nb, others = nazwiska_bib(e.get("author", ""))
    no = nazwiska_oa(rec)
    if nb and no:
        if not others and len(nb) != len(no):
            roz.append(f"autorzy: liczba .bib {len(nb)}, OpenAlex {len(no)}")
        elif others and len(nb) > len(no):
            roz.append(f"autorzy: .bib wymienia {len(nb)} + „others”, OpenAlex {len(no)}")
        for i, (b, o) in enumerate(zip(nb, no)):
            if not zgodny_autor(b, o):
                roz.append(f"autorzy: poz. {i + 1} .bib „{b}”, OpenAlex „{o}”")
                break
    # tom i strony
    bib = rec.get("biblio") or {}
    vb, vo = (e.get("volume") or "").strip(), (bib.get("volume") or "").strip()
    if vb and vo and vb != vo:
        roz.append(f"tom: .bib {vb}, OpenAlex {vo}")
    elif not vb and vo and e["_type"] == "article":
        roz.append(f"brak w .bib: tom {vo}")
    pb = [p for p in re.split(r"-+|–", e.get("pages", "")) if p.strip()]
    fo, lo = (bib.get("first_page") or "").strip(), (bib.get("last_page") or "").strip()
    if pb and fo:
        if pb[0].strip() != fo or (len(pb) == 2 and lo and pb[1].strip() != lo):
            roz.append(f"strony: .bib {e.get('pages')}, OpenAlex {fo}–{lo}".rstrip("–"))
    elif not pb and fo and lo and fo != lo:
        roz.append(f"brak w .bib: strony {fo}–{lo}")
    return roz


# ---------------------------------------------------------------------------
# Typ pozycji i kategoria
# ---------------------------------------------------------------------------

def typ_pozycji(e: dict) -> str:
    t = e["_type"]
    if t == "article":
        return "czasopismo"
    if t in ("inproceedings", "conference"):
        return "konferencja"
    if t in ("book", "incollection", "inbook"):
        return "książka"
    if t == "online":
        return "WWW"
    if t in ("mastersthesis", "phdthesis"):
        return "praca dyplomowa"
    return "preprint"  # misc: preprint arXiv albo manuskrypt


def arxiv_id(e: dict) -> str | None:
    ep = e.get("eprint", "")
    return re.sub(r"v\d+$", "", ep) if ep else None


def czy_arxiv(rec: dict) -> bool:
    src = ((rec.get("primary_location") or {}).get("source") or {}).get("display_name", "") or ""
    return "arxiv" in src.lower() or (rec.get("doi") or "").lower().startswith("https://doi.org/10.48550/")


def szukaj_po_tytule(net: Siec, e: dict) -> dict | None:
    q = re.sub(r"[^\w\s-]", " ", latex_to_unicode(e.get("title", "")).replace("{", "").replace("}", ""))
    q = " ".join(q.split())
    url = f"{OPENALEX}/works?filter=title.search:{urllib.parse.quote(q)}&per-page=10"
    status, body = net.get_json(url, openalex=True)
    if status != 200 or not body:
        return None
    tb, yb = norm(e.get("title", "")), int(e.get("year", 0) or 0)
    nb, _ = nazwiska_bib(e.get("author", ""))
    best, best_score = None, 0.0
    for r in body.get("results", []):
        s = difflib.SequenceMatcher(None, tb, norm(r.get("title") or "")).ratio()
        if nb and nazwiska_oa(r) and zgodny_autor(nb[0], nazwiska_oa(r)[0]):
            s += 0.05
        if yb and r.get("publication_year") and abs(int(r["publication_year"]) - yb) <= 1:
            s += 0.02
        if not czy_arxiv(r):
            s += 0.01  # przy remisie wersja opublikowana przed preprintem
        if s > best_score:
            best, best_score = r, s
    return best if best_score >= 0.9 else None


def doi_zarejestrowany(net: Siec, doi: str) -> bool | None:
    status, body = net.get_json(f"https://doi.org/api/handles/{urllib.parse.quote(doi)}")
    if status == 200 and body:
        return body.get("responseCode") == 1
    if status == 404:
        return False
    return None


# ---------------------------------------------------------------------------

def audyt_pozycji(net: Siec, e: dict) -> dict:
    k = e["_key"]
    typ = typ_pozycji(e)
    row = dict.fromkeys(KOLUMNY, "")
    row.update(klucz=k, typ=typ, recenzowana="tak" if typ in ("czasopismo", "konferencja") else "nie")
    roz, uw = [], []

    # DOI z .bib w doi.org
    if e.get("doi"):
        ok = doi_zarejestrowany(net, e["doi"])
        if ok is False:
            roz.append(f"DOI {e['doi']} niezarejestrowany w doi.org")
        elif ok is None:
            uw.append("doi.org: brak odpowiedzi")

    rec, sposob = None, ""
    if e.get("doi"):
        st, rec = net.get_json(f"{OPENALEX}/works/doi:{urllib.parse.quote(e['doi'])}", openalex=True)
        sposob = "po DOI"
    elif arxiv_id(e):
        st, rec = net.get_json(f"{OPENALEX}/works/doi:10.48550/arXiv.{arxiv_id(e)}", openalex=True)
        sposob = "po arXiv"
    if rec is None and k not in RECZNIE and e["_type"] not in ("book", "online", "mastersthesis"):
        rec = szukaj_po_tytule(net, e)
        if rec is not None:
            sposob = "dopasowanie po tytule"
    # pozycja opublikowana, a znaleziony tylko preprint: spróbuj wersji opublikowanej po tytule
    if rec is not None and typ in ("czasopismo", "konferencja") and czy_arxiv(rec):
        alt = szukaj_po_tytule(net, e)
        if alt is not None and not czy_arxiv(alt):
            rec, sposob = alt, sposob + " → wersja opublikowana po tytule"
        else:
            uw.append("OpenAlex zna tylko preprint arXiv")

    if rec is not None:
        oa = rec.get("open_access") or {}
        best = rec.get("best_oa_location") or {}
        row.update(oa_status=oa.get("oa_status") or "", oa_url=oa.get("oa_url") or "",
                   wersja=best.get("version") or "", cited_by_count=rec.get("cited_by_count", ""),
                   is_retracted="tak" if rec.get("is_retracted") else "nie")
        roz += porownaj(e, rec)
        uw.insert(0, f"OpenAlex {rec.get('id', '').rsplit('/', 1)[-1]} ({sposob})")
        uw.append("pełny tekst w repozytorium: " + ("tak" if oa.get("any_repository_has_fulltext") else "nie"))
        oa_doi = (rec.get("doi") or "").replace("https://doi.org/", "")
        if oa_doi and not e.get("doi") and not oa_doi.lower().startswith("10.48550/"):
            ok = doi_zarejestrowany(net, oa_doi)
            stan = {True: "zarejestrowany", False: "NIEZAREJESTROWANY", None: "nie sprawdzono"}[ok]
            roz.append(f"brak w .bib: DOI {oa_doi} (OpenAlex; w doi.org: {stan})")
        kat = KAT_OA.get(row["oa_status"], "?")
        if typ == "preprint" and kat in ("B", "C") and czy_arxiv(rec):
            kat = "A"
            uw.append("preprint: arXiv jest miejscem publikacji")
        for warunek, serwis in OTWARTE_SERWISY:
            if kat != "A" and warunek(e):
                kat = "A"
                uw.append(f"A według serwisu wydawcy: {serwis}")
                break
        row["kategoria"] = kat
    elif k in RECZNIE:
        row["kategoria"], opis = RECZNIE[k]
        uw.append(f"ręcznie: {opis}")
    else:
        row["kategoria"] = "?"
        uw.append("nie znaleziono w OpenAlex (także po DOI arXiv)")
        for warunek, serwis in OTWARTE_SERWISY:
            if warunek(e):
                row["kategoria"] = "A"
                uw.append(f"ręcznie: A według serwisu wydawcy: {serwis}")
                break

    if rec is not None and typ in ("czasopismo", "konferencja") and czy_arxiv(rec) \
            and str(rec.get("publication_year")) != str(e.get("year")):
        uw.append("rok OpenAlex = wersja arXiv, .bib = wersja opublikowana")
    if k in ZNANE:
        uw.append(f"zweryfikowano: {ZNANE[k]}")
    if k in KOPIE:
        uw.append(f"legalna kopia (2026-10-08): {KOPIE[k]}")
    dois = [e.get("doi", "")] + re.findall(r"DOI (\S+) \(OpenAlex", "; ".join(roz))
    if any(d.startswith("10.52202/") for d in dois):
        uw.append("DOI Curran 10.52202 prowadzi do płatnego wydania drukowanego (proceedings.com); "
                  "bezpłatny tekst: proceedings.neurips.cc")

    if e.get("url") and (k in RECZNIE or row["kategoria"] == "B"):
        uw.append(f"url .bib: {net.url_dziala(e['url'])}")
    if e.get("dostep") and e["dostep"] != row["kategoria"]:
        uw.append(f"w .bib: dostep={e['dostep']}")
    row["rozbieżności"] = "; ".join(roz)
    row["uwagi"] = "; ".join(uw)
    return row


def pokrycie(entries: dict, order: list[str], rows: dict, spis: Path) -> list[tuple[str, int, int]]:
    podrozdzialy = re.findall(r"^###\s+(\d\.\d)\.", spis.read_text(encoding="utf-8"), re.M)
    wynik = []
    for p in podrozdzialy:
        klucze = [k for k in order if p in [x.strip() for x in entries[k].get("rozdzial", "").split(",")]]
        wynik.append((p, len(klucze), sum(1 for k in klucze if rows[k]["recenzowana"] == "tak")))
    return wynik


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bib", type=Path, default=Path("docs/literatura.bib"))
    ap.add_argument("--out", type=Path, default=Path("docs/bib_audyt.csv"))
    ap.add_argument("--spis", type=Path, default=Path("docs/02_spis_tresci.md"), help="spis treści do tabeli pokrycia")
    ap.add_argument("--cache", type=Path, help="katalog pamięci podręcznej odpowiedzi (poza repozytorium)")
    args = ap.parse_args()

    entries = parse_bib(args.bib.read_text(encoding="utf-8"))
    order: list[str] = entries.pop("__order__")  # type: ignore[assignment]
    net = Siec(args.cache, os.environ.get("OPENALEX_API_KEY"))

    rows: dict[str, dict] = {}
    try:
        for k in order:
            rows[k] = audyt_pozycji(net, entries[k])
            print(f"{k:32} {rows[k]['kategoria']}  {rows[k]['rozbieżności'][:90]}", file=sys.stderr)
    except LimitWyczerpany as exc:
        print(f"STOP: limit OpenAlex wyczerpany (HTTP 429) przy {exc}. Ustaw OPENALEX_API_KEY "
              "i uruchom ponownie (z --cache, żeby nie powtarzać zapytań).", file=sys.stderr)
        return 3

    with args.out.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=KOLUMNY)
        w.writeheader()
        for k in order:
            w.writerow(rows[k])

    from collections import Counter
    print(f"\nZapisano {len(rows)} pozycji do {args.out}")
    print("Kategorie:", dict(sorted(Counter(r["kategoria"] for r in rows.values()).items())))
    print("Z rozbieżnościami:", sum(1 for r in rows.values() if r["rozbieżności"]))
    print("\n| Podrozdział | Pozycje | W tym recenzowane | Uwaga |\n|---|---|---|---|")
    for p, n, rec in pokrycie(entries, order, rows, args.spis):
        uwaga = "wyniki: bez literatury z założenia" if p.startswith("5.") else ("0–1 pozycji" if n <= 1 else "")
        print(f"| {p} | {n} | {rec} | {uwaga} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
