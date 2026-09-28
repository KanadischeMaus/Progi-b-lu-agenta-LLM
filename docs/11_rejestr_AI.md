# Rejestr użycia narzędzi AI

Po co: na końcu pracy trzeba dołączyć tabelę „Wykaz obszarów i narzędzi GenAI wykorzystanych przez autora w trakcie wykonywania pracy dyplomowej” (`10_wymogi_formalne.md`). Rejestr prowadzony na bieżąco sprawia, że tabela będzie kompletna i prawdziwa. Przy okazji dokumentuje przebieg pracy.

**Zasady**
- Jeden wiersz na sesję albo na spójne zadanie.
- Obszary według listy z szablonu, litery a)–i):
  - a) redakcja i korekta,
  - b) analiza stanu wiedzy i literatura,
  - c) generowanie treści i przykładów,
  - d) pytania do ankiet,
  - e) schematy i diagramy,
  - f) analiza danych i wizualizacja,
  - g) podsumowania i wnioski,
  - h) kod,
  - i) tłumaczenia.
- Narzędzie z wersją lub modelem, np. „Claude Code (Claude Opus 5.5)”, „Gemini 3.1 Pro (czat)”.
- „Co zrobiono” opisuje, co zrobiło narzędzie, a co zdecydował autor, jeśli to istotne.

## Dziennik

| Data | Narzędzie / model | Obszar | Co zrobiono | Pliki |
|---|---|---|---|---|
| 2026-09-27 | Claude (aplikacja), Opus 5.5 | b) | Analiza pracy referencyjnej (Zawiślak 2025): wskazanie braków pomiaru progu, problemów z powtarzalnością i niespójności wykresów; propozycja metody (funkcja psychometryczna) | `docs/04`, `docs/07` |
| 2026-09-27 | Claude (aplikacja), Opus 5.5 | b) | Wyszukanie i weryfikacja online 50 pozycji literatury; opis ich zastosowania | `docs/03`, `docs/literatura.bib` |
| 2026-09-27 | Claude (aplikacja), Opus 5.5 | c) | Robocze dokumenty organizacyjne (nie tekst pracy): zasady współpracy, plan rozdziałów, plan eksperymentów, słownik, wymogi formalne | `AGENTS.md`, `CLAUDE.md`, `.claude/`, `docs/` |
| 2026-09-27 | Claude (aplikacja), Opus 5.5 | h), f) | Skrypt generujący bibliografię w formacie PRz; moduł dopasowania funkcji psychometrycznej z bootstrapem i testem odzyskiwania parametrów | `tools/bib2bibitem.py`, `code/analysis/`, `code/tests/` |
| 2026-09-27 | Claude (aplikacja), Opus 5.5 | h), f) | Odtworzenie kodu z listingów pracy referencyjnej (środowisko, kategorie, opis stanu, prompty) i testy zgodności z przykładami z pracy; sondowanie, pętla zamknięta, agregacja wyników, metryki pętli, wykresy | `code/` |

## Tabela do pracy (uzupełniana na końcu)

Scalamy dziennik po obszarach i narzędziach:

| Lp. | Obszar wykorzystywania | Narzędzie |
|---|---|---|
| 1 | | |
