# Praca magisterska: „Wpływ promptu na progi bólu agenta LLM”

Repozytorium pracy: zasady dla agentów AI, dokumentacja, literatura, kod eksperymentów i wyniki. Tekst pracy powstaje w LaTeX-u (Overleaf, szablon WMiFS PRz).

## Struktura

```
AGENTS.md              zasady współpracy dla każdego agenta (Claude Code, Cursor, …)
CLAUDE.md              import AGENTS.md + ustawienia Claude Code
.claude/rules/         reguły ładowane przy plikach LaTeX i kodu
.claude/skills/        procedury: napisz-podrozdzial, zweryfikuj-tekst, dodaj-zrodlo
docs/                  temat, spis treści, literatura (+ .bib), metodologia, plan eksperymentów, styl, wymogi, rejestr AI, decyzje, harmonogram
thesis/                projekt LaTeX z Overleaf (instrukcja w thesis/README.md)
code/                  kod odtworzony z listingów pracy referencyjnej: środowisko, pętla, sondowanie, analiza, testy
results/               logi i wyniki eksperymentów
tools/bib2bibitem.py   bibliografia w formacie PRz z docs/literatura.bib
```

Mapa dokumentów: `docs/00_indeks.md`.

## Pierwsze kroki

1. **Repozytorium prywatne.** Rozpakuj archiwum, potem:
   ```bash
   cd magisterka && git init && git add . && git commit -m "Start: zasady, dokumentacja, literatura"
   ```
   Jeśli wysyłasz na GitHub, to tylko jako **repozytorium prywatne**. Tekst pracy publicznie dostępny przed badaniem w JSA może zostać znaleziony w internecie i wykazany jako podobieństwo.
2. **Uzupełnij dane:**
   - imię i nazwisko, nr albumu: `docs/01`, `docs/10`,
   - datę obrony i terminy z dziekanatu: `docs/13`, `docs/10`.
3. **Projekt z Overleaf:** skopiuj go do `thesis/` według `thesis/README.md` i wpisz ścieżki plików w tabeli w tym README.
4. **Python:**
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r code/requirements.txt
   ```
   Następnie zainstaluj Ollamę i model (`code/README.md`).
5. **Claude Code:** uruchom `claude` w katalogu `magisterka`. Poleceniem `/context` sprawdź, czy `CLAUDE.md` się wczytał (sekcja *Memory files*).
6. **Konsultacja z promotorem:** pytania z `docs/01` (sekcja „Pytania do promotora”). Ustalenia zapisz w `docs/12`.

## Jak pracować z agentem (przykłady poleceń w Claude Code)

- `/napisz-podrozdzial 1.4`: szkic podrozdziału (tryb A).
- `/zweryfikuj-tekst thesis/rozdzialy/r3.tex, podrozdział 3.2`: uwagi do Twojego tekstu (tryb B).
- `/dodaj-zrodlo 10.18653/v1/2024.findings-acl.275`: nowa pozycja po weryfikacji.
- „Uruchom testy kodu i pilotaż E0 na 10 wywołaniach, potem pokaż czas i odpowiedzi”: pierwsze zadanie przy kodzie (`code/README.md`).
- „Uruchom testy i test odzyskiwania parametrów”: sprawdzenie modułu analizy.

Cursor i inne narzędzia też czytają `AGENTS.md`. Do niezależnej recenzji (np. w Gemini) służy prompt z `docs/09`, sekcja 4.

## Stan na 27.09.2026

- Gotowe:
  - zasady i skille,
  - dokumentacja robocza (`docs/`),
  - 50 zweryfikowanych pozycji literatury,
  - generator bibliografii,
  - kod odtworzony z listingów pracy referencyjnej (środowisko, opis stanu, prompty, pętla), sprawdzony na przykładach z pracy,
  - sondowanie progów, analiza (funkcja psychometryczna, bootstrap, metryki pętli), wykresy, 24 testy.
- Do zrobienia najpierw:
  - akceptacja metody przez promotora,
  - instalacja Ollamy i modelu na Macu,
  - pilotaż E0 (`code/README.md`).
