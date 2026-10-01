---
name: zweryfikuj-tekst
description: Tryb B. Agent sprawdza fragment pracy magisterskiej napisany przez autora (logika, źródła, liczby, terminologia, styl, wymogi WMiFS) i zwraca tabelę uwag. Zmiany wprowadza dopiero po akceptacji. Użyj, gdy autor prosi o sprawdzenie, weryfikację, recenzję albo korektę swojego tekstu.
---

# Weryfikacja tekstu autora (tryb B)

## 1. Przygotowanie

- Ustal dokładny zakres: plik i akapity. Jeśli autor wkleił tekst w rozmowie, pracuj na nim i zapytaj, gdzie ma trafić.
- Przeczytaj opis danego podrozdziału w `docs/02_spis_tresci.md`, żeby ocenić, czy tekst realizuje zakładany cel.

## 2. Sprawdź po kolei

1. **Merytoryka i logika:**
   - czy wnioski wynikają z przesłanek,
   - czy nie ma przeskoków ani sprzeczności z innymi rozdziałami,
   - czy definicje zgadzają się z `docs/04_metodologia_pomiaru.md`.
2. **Źródła:**
   - czy każde twierdzenie merytoryczne ma odwołanie,
   - czy klucz istnieje w `docs/literatura.bib`,
   - czy źródło rzeczywiście to mówi. Jeśli masz dostęp do tekstu źródła, sprawdź. Jeśli nie, oznacz jako „do sprawdzenia”.
3. **Liczby:** czy zgadzają się z plikami w `results/`. Przelicz, jeśli to możliwe.
4. **Parafraza:** czy fragment nie jest zbyt bliski oryginałowi (ta sama struktura zdań, zamienione tylko słowa). Taki fragment wskaż do przeredagowania albo do ujęcia jako cytat.
5. **Terminologia:** zgodność z `docs/08_slownik_pojec.md`, ta sama nazwa dla tego samego pojęcia w całym tekście.
6. **Styl i język:** według `docs/09_styl_i_rzetelnosc.md`. Błędy gramatyczne, interpunkcja, powtórzenia, zdania wielokrotnie złożone trudne do śledzenia. Wskaż też nawyki z tabeli „Dziesięć nawyków słabego tekstu” (sekcja 1), z konkretnym zdaniem i propozycją, ale bez przepisywania stylu autora na siłę.
7. **Wymogi formalne i typografia:** według `docs/10_wymogi_formalne.md` i `.claude/rules/latex.md`.

## 3. Zwróć uwagi

Tabela:

| nr | miejsce (akapit/linia) | typ | waga | uwaga | propozycja |
|---|---|---|---|---|---|

- Typy: merytoryka, logika, źródło, liczba, parafraza, terminologia, styl, język, typografia, wymóg.
- Wagi:
  - **krytyczna:** błąd merytoryczny, brak źródła, zła liczba,
  - **istotna:** niejasność, niespójność,
  - **drobna:** styl, typografia.
- Na końcu dwa lub trzy zdania oceny ogólnej: co działa, co jest największym problemem.
- Nie wprowadzaj zmian w pliku na tym etapie.

## 4. Wprowadzenie zmian

- Autor wskazuje numery uwag do przyjęcia, np. „przyjmuję 1–4, 7”. Wprowadź tylko te.
- Zachowaj styl autora. Poprawiasz błąd, a nie przepisujesz zdanie po swojemu.
- Pokaż zmiany w wersji „przed/po”.

## 5. Zamknij sesję

- Wpis do `docs/11_rejestr_AI.md`. Obszar a) to redakcja i korekta. Jeśli sprawdzano źródła, dodaj b).
