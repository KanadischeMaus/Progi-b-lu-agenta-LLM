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
| 2026-09-30 | Claude (aplikacja), Opus 5.5 | a) | Zasady stylu: tabela dziesięciu nawyków słabego tekstu, uwaga o ofertach sprawdzania pracy „w systemie uczelnianym” | `docs/09`, `AGENTS.md`, `.claude/` |
| 2026-09-27 | Claude (aplikacja), Opus 5.5 | h), f) | Odtworzenie kodu z listingów pracy referencyjnej (środowisko, kategorie, opis stanu, prompty) i testy zgodności z przykładami z pracy; sondowanie, pętla zamknięta, agregacja wyników, metryki pętli, wykresy | `code/` |
| 2026-09-28 – 2026-10-07 | Claude (aplikacja), Opus 5.5 | c) | Dokumenty organizacyjne: metryczka i harmonogram, diagnostyka instalacji Ollamy i środowiska na Macu, ocena sprzętu i opcji chmurowych, omówienie pytań do promotora, propozycje decyzji D11–D13, prompty dla Claude Code; decyzje podjął autor | `docs/01`, `docs/10`, `docs/12`, `docs/13` |
| 2026-10-07 | Claude Code (CLI), Opus 5.5 MAX | b) | Weryfikacja online metadanych bibliograficznych i propozycja poprawionego literatura.bib; część propozycji odrzucona przez autora (m.in. Zawiślak 2026, Benjamini–Hochberg, Lakens, ręczna thebibliography) | `docs/raporty/bib_2026-10-07.md` |
| 2026-10-07 | Claude (aplikacja), Opus 5.5 | b) | Ocena raportu bibliograficznego z 07.10 (10 uwag, przyjęte przez autora), weryfikacja poradnika Biblioteki PRz i szablonu WMiFS w zakresie bibliografii, kryterium dostępności źródeł (D12), weryfikacja danych Holm 1979 | `docs/03`, `docs/09`, `docs/10`, `docs/12`, `docs/literatura.bib` |
| 2026-10-07 – 2026-10-08 | Claude Code (CLI), Opus 5.5 MAX | b), h) | Porządkowanie literatury według decyzji autora: D12–D13 i D15–D16 w `docs`; scalenie raportu z 08.10 z `literatura.bib` (80 pozycji po decyzjach), zmiana klucza Atıla; weryfikacja online nowych pozycji (Holm, Li i in., Butlin i in., ren2026ai ze strony tytułowej PDF z kopią w Web Archive); skrypt audytu (OpenAlex, doi.org) i `bib_audyt.csv`; wyszukanie legalnych kopii pozycji C; odnośniki NeurIPS, OpenReview i PMLR; generator bibliografii (kolejność alfabetyczna lub cytowań, „i in.”, odnośniki A/B/C) z testami; wersje preprintów arXiv; decyzje podjął autor | `.gitignore`, `docs/00`–`04`, `docs/09`–`13`, `docs/literatura.bib`, `docs/bib_audyt.csv`, `docs/raporty/`, `docs/zrodla/README.md`, `tools/`, `thesis/README.md` |
| 2026-10-08 | Claude (aplikacja, tryb badania), Opus 5.5 | b) | Scalona lista literatury (83 pozycje): weryfikacja online nowych pozycji, kategorie dostępu D12, pokrycie podrozdziałów; autor usunął schmidhuber2010formal i odrzucił kocielnik2026rethinking | `docs/raporty/literatura_2026-10-08.md` |
| 2026-10-08 | Claude (aplikacja), Opus 5.5 | b), f) | Weryfikacja online 3 nowych pozycji (m.in. recenzowana wersja Cedro i in. w CACM 2026), uzasadnienie testu ilorazu wiarygodności (D14), złagodzenie kryterium dostępności po konsultacji (D16), plan lektury; decyzje podjął autor | `docs/01`, `docs/02`, `docs/03`, `docs/04`, `docs/12`, `docs/notatki/`, `docs/literatura.bib` |
| 2026-10-08 | Claude Code (CLI), Opus 5.5 MAX | b), h) | Wprowadzenie ustaleń z konsultacji 08.10 i decyzji D14, D16 do docs (01, 02, 03, 04, 12, 00); weryfikacja online i dopisanie 3 pozycji (Crossref, doi.org, OpenAlex, arXiv; yoshida2025linking jako A, bo u wydawcy jest otwarty dostęp); ISBN podręczników z katalogu K10plus; generator: pozycje C przez DOI albo stały adres, z testami; szablon notatek i kolejka lektury (bez treści); decyzje podjął autor | `docs/00`–`04`, `docs/11`, `docs/12`, `docs/literatura.bib`, `docs/bib_audyt.csv`, `docs/notatki/`, `tools/`, `thesis/README.md` |

## Tabela do pracy (uzupełniana na końcu)

Scalamy dziennik po obszarach i narzędziach:

| Lp. | Obszar wykorzystywania | Narzędzie |
|---|---|---|
| 1 | | |
