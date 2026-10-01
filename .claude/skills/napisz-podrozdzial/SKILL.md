---
name: napisz-podrozdzial
description: Tryb A. Agent pisze szkic podrozdziału pracy magisterskiej w LaTeX-u na podstawie spisu treści, zweryfikowanej literatury i wyników, a potem poprawia go według uwag autora. Użyj, gdy autor prosi o napisanie, rozpisanie albo szkic fragmentu pracy.
---

# Szkic podrozdziału (tryb A)

## 1. Ustal zakres

1. Znajdź podrozdział w `docs/02_spis_tresci.md`. Przepisz jego opis, przypisane źródła i szacowaną objętość.
2. Jeśli autor podał dodatkowe wskazówki, zestaw je z opisem. Przy sprzeczności zapytaj, zanim zaczniesz.
3. Potwierdź zakres jednym zdaniem, np. „Piszę 4.3: definicja funkcji psychometrycznej, estymacja ML, bootstrap. Około 2 stron, źródła: wichmann2001psychometric, kingdom2016psychophysics”.

## 2. Zbierz materiał

- **Literatura:** tylko pozycje z `docs/literatura.bib`, najlepiej te przypisane do podrozdziału w `docs/03_literatura.md`. Jeśli pozycja jest dostępna (PDF w `docs/zrodla/` albo online), przeczytaj fragment, na który się powołujesz. Nie cytuj z pamięci.
- **Wyniki:** tylko pliki z `results/processed/` i `results/figures/`. Zanotuj ścieżki.
- **Terminologia:** `docs/08_slownik_pojec.md`.
- Jeśli czegoś brakuje (źródła do kluczowego twierdzenia albo wyników), przerwij i napisz, czego brakuje. Nie uzupełniaj luk ogólnikami.

## 3. Napisz szkic

- Plik: podrozdział w `thesis/` (nazwę i lokalizację podaje `thesis/README.md`). Jeśli plik zawiera tekst autora, nie nadpisuj go. Dopisz szkic w zaznaczonym miejscu albo zapytaj.
- Struktura: pierwsze zdanie mówi, co ten fragment robi w pracy. Dalej treść. Na końcu przejście do następnego fragmentu, tylko jeśli jest potrzebne.
- Styl według `docs/09_styl_i_rzetelnosc.md`, typografia według `.claude/rules/latex.md`.
- Przed oddaniem przejdź szkic tabelą „Dziesięć nawyków słabego tekstu” z `docs/09`, sekcja 1, i popraw to, co znajdziesz. Szczególnie: myślniki, sztuczne przejścia, trójki, kontrasty „to nie X, tylko Y” i podsumowania na końcu akapitów.
- Każde twierdzenie merytoryczne ma `\cite{}` albo wynik z `results/`. Gdy nie ma pokrycia, wstaw `\dower{brak źródła: ...}`.
- Liczby z wyników opatrz komentarzem `% źródło: ...`.
- Nie przekraczaj szacowanej objętości o więcej niż 25%. Jeśli materiał jest większy, zaproponuj podział.

## 4. Oddaj szkic

W odpowiedzi podaj:
1. ścieżkę pliku i liczbę słów,
2. listę użytych źródeł, każde z jednym zdaniem, do czego posłużyło,
3. wszystkie `\dower{}` i twierdzenia, które autor powinien sprawdzić,
4. 1–3 pytania do autora, jeśli są decyzje do podjęcia.

## 5. Poprawki po uwagach

- Zmieniaj wyłącznie fragmenty wskazane przez autora. Resztę tekstu zostaw bez zmian, łącznie ze słowami, które autor zmienił ręcznie.
- Jeśli uwaga wymaga zmiany w innym miejscu (np. spójność terminu), zapytaj albo zaproponuj, ale nie wprowadzaj sam.
- Pokaż zmienione akapity w wersji „przed/po” albo w diffie.

## 6. Zamknij sesję

- Dopisz wpis do `docs/11_rejestr_AI.md`. Obszar c) to generowanie treści; jeśli były poprawki redakcyjne, dodaj a).
- Jeśli w trakcie zapadła decyzja (np. zmiana zakresu podrozdziału), dopisz ją do `docs/12_decyzje_i_konsultacje.md` i zaktualizuj `docs/02_spis_tresci.md`.
