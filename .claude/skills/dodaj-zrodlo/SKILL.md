---
name: dodaj-zrodlo
description: Dodaje nową pozycję do literatury pracy po sprawdzeniu jej istnienia i danych bibliograficznych online, aktualizując docs/literatura.bib i docs/03_literatura.md. Użyj, gdy autor lub agent chce zacytować źródło, którego nie ma jeszcze w bibliografii, albo poprawić dane istniejącej pozycji.
---

# Dodanie źródła do literatury

## 1. Weryfikacja (obowiązkowa)

- Znajdź pozycję online w źródle pierwotnym:
  - strona wydawcy, DOI, ACL Anthology, PMLR, OpenReview albo arXiv,
  - dla książek katalog biblioteki lub wydawcy.
- Pobierz stamtąd dane: pełna lista autorów, tytuł, miejsce publikacji, rok, tom/numer/strony, DOI albo URL.
- Jeśli preprint ma wersję opublikowaną (konferencja lub czasopismo), cytuj wersję opublikowaną, a arXiv podaj jako URL.
- Jeśli nie udało się potwierdzić pozycji albo któregoś pola:
  - nie dodawaj pozycji jako zweryfikowanej,
  - wpisz `status = {?}` i opisz braki w polu `weryfikacja`,
  - poinformuj autora.
- Nigdy nie uzupełniaj brakujących pól z pamięci ani „na oko”.

## 2. Wpis do `docs/literatura.bib`

- Klucz: `nazwiskopierwszegoautoraROKpierwszesłowotytułu`, małymi literami, bez polskich znaków, np. `starzyk2017needs`.
- Typy:
  - `@article`,
  - `@inproceedings`,
  - `@incollection`,
  - `@book`,
  - `@misc` (preprinty: pole `eprint` z numerem arXiv),
  - `@mastersthesis`,
  - `@online` (strony WWW: pole `urldate` w formacie RRRR-MM-DD).
- Pola własne (skrypt je pomija przy generowaniu bibliografii):
  - `status = {Z}` (zweryfikowano online), `{K}` (pozycja klasyczna, dane standardowe) albo `{?}` (brakuje potwierdzenia pola),
  - `rozdzial = {1.4, 3.2}`, czyli gdzie pozycja jest używana,
  - `weryfikacja = {...}`, czyli co i gdzie sprawdzono, z datą.
- Znaki specjalne w LaTeX-u: `\&`, `\%`. Nazwy własne i skróty w tytule chroń klamrami: `{LLM}`, `{DeepSeek-R1}`.

## 3. Wpis do `docs/03_literatura.md`

- Dodaj wiersz w odpowiedniej sekcji tematycznej:
  - klucz,
  - krótki opis (autor, rok, tytuł),
  - do czego służy (jedno zdanie),
  - rozdział,
  - priorytet: R (rdzeń) albo U (uzupełniająca),
  - status.
- Jeśli liczba pozycji przekracza 55, zaproponuj autorowi, które pozycje U usunąć.

## 4. Sprawdzenie

- Uruchom `python tools/bib2bibitem.py --bib docs/literatura.bib --all --out /tmp/test_bib.tex` i sprawdź, czy wpis formatuje się poprawnie (autorzy, kursywa, strony).
- Wpis do `docs/11_rejestr_AI.md`, obszar b).
