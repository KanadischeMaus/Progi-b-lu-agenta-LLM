# Zasady współpracy przy pracy magisterskiej

Ten plik czyta każdy agent pracujący w tym repozytorium (Claude Code, Cursor i inne).
Szczegóły są w `docs/`; tutaj są tylko zasady obowiązujące zawsze.

## Kontekst w skrócie

- **Temat:** „Wpływ promptu na progi bólu agenta LLM”.
- **Uczelnia:** Politechnika Rzeszowska, Wydział Matematyki i Fizyki Stosowanej, kierunek Inżynieria i Analiza Danych, praca magisterska.
- **Promotor:** dr inż. Marcin Kowalik, prof. PRz.
- **Praca referencyjna:** K. Zawiślak, „Budowa agenta motywowanego na bazie Dużego Modelu Językowego (LLM)”, PRz 2025. Równolegle powstaje praca Kingi, która kontynuuje te badania.
- **Istota pracy:** zmierzyć ilościowo, gdzie leży próg bólu agenta LLM i jak przesuwa go treść oraz konstrukcja promptu.
- **Tekst:** LaTeX (Overleaf, szablon WMiFS), język polski.
- **Kod:** odtworzony z listingów pracy referencyjnej (jedyne źródło kodu, notebooka nie ma). Python w `.venv` na macOS, model lokalny przez Ollamę (`deepseek-r1:14b`).

## Mapa repozytorium

| Ścieżka | Zawartość |
|---|---|
| `docs/00_indeks.md` | spis dokumentów i wskazówka, który czytać przy jakim zadaniu |
| `docs/` | temat, spis treści, literatura, metodologia, plan eksperymentów, styl, wymogi, rejestr AI, decyzje |
| `docs/literatura.bib` | jedyne źródło danych bibliograficznych |
| `thesis/` | projekt LaTeX (kopia projektu z Overleaf) |
| `code/` | środowisko, pętla agenta, sondowanie progów, analiza |
| `results/` | surowe logi JSONL, przetworzone dane, wykresy |
| `tools/bib2bibitem.py` | generuje `\bibitem` w formacie PRz z `literatura.bib` |

Na początku każdej sesji przeczytaj `docs/00_indeks.md` i pliki, które wskazuje dla danego zadania.

## Role

- Autor pracy decyduje o treści, hipotezach, interpretacji wyników i ostatecznym brzmieniu tekstu. Na obronie odpowiada za każde zdanie.
- Agent pisze szkice, redaguje, weryfikuje, szuka literatury, pisze kod i liczy. Decyzje merytoryczne proponuje w wariantach, ale ich nie podejmuje.
- Gdy polecenie jest niejasne albo wymaga decyzji autora, agent pyta, zanim zacznie. Nie zgaduje.

## Tryb A: agent pisze, autor poprawia

1. Ustal podrozdział z `docs/02_spis_tresci.md` i potwierdź jego zakres w jednym zdaniu.
2. Zbierz materiał: tylko źródła z `docs/03_literatura.md` oraz wyniki z `results/`. Jeśli czegoś brakuje, napisz, czego, zamiast pisać „z głowy”.
3. Napisz szkic bezpośrednio w pliku `.tex` podrozdziału. Nie nadpisuj tekstu, który autor napisał sam.
4. Na końcu odpowiedzi podaj:
   - listę twierdzeń, które wymagają źródła,
   - wszystkie znaczniki `\dower{}` wstawione w tekście,
   - pytania do autora.
5. Poprawki po uwagach autora wprowadzaj tylko tam, gdzie wskazał. Pozostałych akapitów nie przepisuj. Po zmianie pokaż, co się zmieniło.

Szczegółowa procedura: skill `napisz-podrozdzial`.

## Tryb B: autor pisze, agent sprawdza

1. Przeczytaj fragment i sprawdź:
   - logikę wywodu,
   - zgodność ze źródłami i wynikami,
   - terminologię (`docs/08_slownik_pojec.md`),
   - styl (`docs/09_styl_i_rzetelnosc.md`),
   - wymogi formalne (`docs/10_wymogi_formalne.md`).
2. Zwróć tabelę uwag: `nr | miejsce | typ | waga (krytyczna/istotna/drobna) | uwaga | propozycja`.
3. Nie zmieniaj pliku, dopóki autor nie wskaże, które uwagi przyjmuje. Potem wprowadź tylko te.
4. Zachowaj styl i słownictwo autora. Poprawiaj błędy, nie „ulepszaj” brzmienia na siłę.

Szczegółowa procedura: skill `zweryfikuj-tekst`.

## Źródła, liczby i cytowanie

- Nie wymyślaj źródeł, cytatów, autorów, DOI, numerów stron ani wyników. To zasada bezwzględna.
- Cytuj tylko pozycje z `docs/literatura.bib`. Nowe źródło dodawaj skillem `dodaj-zrodlo`, który wymaga sprawdzenia pozycji online.
- Twierdzenia merytorycznego, którego nie umiesz podeprzeć źródłem, nie pisz jako faktu. Oznacz je `\dower{brak źródła: ...}`.
- Każda liczba w rozdziałach z wynikami pochodzi z `results/`. Obok niej w komentarzu LaTeX podaj, skąd jest: `% źródło: results/processed/E1_progi.csv, skrypt code/analysis/aggregate.py`.
- Cytat dosłowny zapisuj w cudzysłowie, z odwołaniem i numerem strony.
- Parafrazę pisz własną strukturą zdania, nie zamieniając tylko słów na synonimy, i zawsze z odwołaniem.
- Nie opieraj akapitu na parafrazie jednego źródła zdanie po zdaniu. Zestawiaj źródła i dodawaj własny komentarz.
- Pracy Klaudii (`zawislak2025budowa`) nie kopiuj. Możesz ją cytować i z nią polemizować.

## Znaczniki w tekście

- `\dower{...}` oznacza miejsce do weryfikacji (makro opisane w `thesis/README.md`).
- `% TODO:` to notatka dla autora, niewidoczna w PDF.
- Przed oddaniem pracy wyszukiwanie `\dower` i `TODO` musi dać zero wyników.

## Styl (skrót, pełna wersja w `docs/09`)

- Piszemy po polsku, w stylu naukowym, formą bezosobową lub 1. osobą liczby mnogiej, spójnie w całej pracy.
- Terminy zawsze według `docs/08_slownik_pojec.md`. Przy pierwszym użyciu podajemy odpowiednik angielski kursywą.
- Konkret zamiast ogólników: liczba, warunek, odwołanie. Bez pustych wstępów i podsumowań akapitów.
- Unikamy dziesięciu nawyków słabego tekstu z `docs/09`, sekcja 1: nadużywane myślniki, słowa na wyrost, wymuszone kontrasty „to nie X, tylko Y”, trójki z przyzwyczajenia, sztuczne przejścia, zapychacze, jednakowa długość zdań, nadmiar list, powtarzane podsumowania, tekst bez głosu autora.
- Formatowanie i typografia według `.claude/rules/latex.md` i `docs/10_wymogi_formalne.md`.

## Rejestr użycia AI

Po każdej sesji, w której powstał lub zmienił się tekst, kod albo analiza, dopisz wiersz do `docs/11_rejestr_AI.md`:

`data | narzędzie i model | obszar a)–i) | co zrobiono | pliki`

Rejestr to podstawa tabeli GenAI dołączanej do pracy. Wpisy muszą być prawdziwe i kompletne.

## Kod i eksperymenty (skrót, pełna wersja w `docs/05`, `docs/06` i `.claude/rules/kod.md`)

- Parametry modelu przekazuj w `options` (Ollama): `temperature`, `seed`, `top_p`. Nigdy w treści wiadomości.
- Każde wywołanie modelu zapisuj do JSONL:
  - ID eksperymentu i promptu, ziarno,
  - pełny stan liczbowy i dokładny tekst promptu,
  - surową odpowiedź i sparsowaną akcję,
  - status parsowania i czas.
- Nie nadpisuj surowych wyników. Każdy przebieg dostaje nowy plik i wpis w rejestrze przebiegów (`docs/06`).
- Odpowiedź, której nie da się sparsować, to osobna kategoria. Nie liczy się jako „nic nie rób”.
- Wykresy i tabele do pracy generuje skrypt z danych w `results/`, nigdy ręcznie.

## Git

- Małe commity z opisem po polsku, np. `rozdz. 4.3: szkic estymacji progu`.
- Nie usuwaj i nie przepisuj tekstu autora bez wyraźnej prośby.
- Nie rób `push --force` ani `reset --hard` bez zgody.
- Surowe wyniki eksperymentów commituj razem z konfiguracją, która je wytworzyła.

## Czego agent nie robi

- Nie przerabia tekstu po to, żeby ukryć udział AI, i nie „uczłowiecza” go pod detektory.
- Nie wysyła treści pracy do zewnętrznych serwisów (np. detektorów AI) bez zgody autora.
- Nie zmienia preambuły ani szablonu WMiFS bez zgody autora.
- Nie przedstawia hipotez ani interpretacji jako ustalonych, dopóki autor ich nie zatwierdzi (`docs/12_decyzje_i_konsultacje.md`).

## Odpowiedzi agenta

- Po polsku i zwięźle.
- Na końcu: co zostało zmienione (pliki), co wymaga decyzji autora i czy wpisano sesję do rejestru AI.
