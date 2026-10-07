# Wymogi formalne (WMiFS PRz i szablon)

Źródła:
- strona WMiFS „Wymagania dotyczące przygotowania pracy dyplomowej” (załącznik 1 do procedury z 23.06.2021)~\cite{wmifs2025wymagania},
- procedura postępowania z pracą dyplomową na WMiFS,
- szablon pracy dyplomowej 2025 (PDF/TeX).

Sprawdzono 27.09.2026. Przed złożeniem pracy sprawdź, czy nie ma nowszej wersji.

## Objętość i układ

- **Objętość:** 15–50 stron znormalizowanych A4, bez dodatków, aneksów i załączników. Praca referencyjna ma ponad 80 stron treści, więc interpretację limitu potwierdzamy z promotorem.
- **Układ obowiązkowy:**
  1. strona tytułowa (szablon: `strona_tytulowa-1` klasyczna albo `-2` pod okienko okładki PRz; aktywna tylko jedna),
  2. spis treści,
  3. wstęp,
  4. część zasadnicza (co najmniej dwa rozdziały),
  5. podsumowanie,
  6. spis literatury,
  7. załączniki (jeśli potrzebne),
  8. streszczenie,
  9. tabela z wykazem obszarów i narzędzi GenAI.
- **Wstęp:** krótkie omówienie problematyki, przegląd treści pracy w kilku zdaniach, **zwrócenie uwagi na uzyskane wyniki**.
- **Część zasadnicza:**
  - część wstępna (opisowa): zagadnienia na podstawie literatury, założenia, metody i techniki badawcze, materiały źródłowe;
  - część merytoryczna: opis problematyki, wyniki badań i ich analiza.
- **Podsumowanie:** ustosunkowanie się do wyników, ich ocena, **odniesienie do literatury**, perspektywy dalszych badań.
- **Spis literatury:** wszystkie wykorzystane źródła. Strony WWW z autorem i tytułem.
- **Streszczenie:** kilkuzdaniowe, po polsku i po angielsku, z tytułem i słowami kluczowymi (**najwyżej 5**). Szablon ma gotową stronę streszczenia PL/EN.
- **Tabela GenAI:** obowiązuje od roku akademickiego 2025/2026. Kolumny: Lp. | Obszar wykorzystywania | Narzędzie. Gdy AI nie używano, wpisuje się „nie korzystano”.
  Przykładowe obszary:
  - a) redakcja i korekta tekstu (m.in. poprawa stylistyczna i gramatyczna, synonimy i parafrazowanie, sprawdzenie spójności językowej),
  - b) analiza stanu wiedzy, przegląd literatury,
  - c) generowanie treści lub przykładów,
  - d) tworzenie pytań do ankiet i kwestionariuszy,
  - e) tworzenie schematów, diagramów i map myśli,
  - f) analiza danych i wizualizacja wyników (m.in. obliczenia statystyczne, tworzenie wykresów i tabel),
  - g) tworzenie podsumowań i wniosków,
  - h) pisanie i testowanie kodu,
  - i) tłumaczenia językowe.

## Cele pracy dyplomowej na kierunku Inżynieria i Analiza Danych

Praca ma wykazać umiejętność:
1. samodzielnej pracy z tekstem naukowym;
2. analizy informacji zawartej w literaturze;
3. analizy porównawczej wybranych zagadnień na podstawie kilku pozycji literatury naukowej;
4. doboru metod i narzędzi badawczych do celów głównych i szczegółowych;
5. opracowania problemów badawczych, zadań projektowych czy informatycznych związanych z analizą danych.

Punkt 4 dobrze realizuje rozdział 4 (metoda pomiaru). Punkt 5 realizują rozdziały 4–5.

## Formatowanie (szablon; preambuła LaTeX już to ustawia)

- **Strona:** A4, druk dwustronny.
- **Marginesy:** górny 25 mm, dolny 25 mm, wewnętrzny 30 mm, zewnętrzny 25 mm.
- **Tekst:** czcionka 10–12 pt, interlinia 1,5, justowanie.
- **Tytuły:** rozdziały pogrubione 16 pt, podrozdziały 14 pt. Styl nagłówka rozdziału: `\def\chapterstyletype{classic}` („Rozdział X” nad tytułem) albo `inline`.
- **Numeracja stron:** automatyczna.
- **Nowa strona:** od niej zaczynają się wstęp, rozdziały, spisy, bibliografia, aneksy i streszczenie. Szablon zaleca `\cleardoublepage` przed zasadniczymi częściami.
- Tytuł podrozdziału nie może zostać sam na końcu strony.
- **Kropki:** tytuły rozdziałów oraz podpisy rysunków i tabel bez kropki na końcu.
- **Wzory:** wyśrodkowane, numerowany wzór w osobnej linii.
- **Rysunki i tabele:** wyśrodkowane. Podpis rysunku pod nim, tabeli nad nią, czcionką mniejszą (9–11 pt). Każdy rysunek i każda tabela musi mieć odwołanie w tekście.
- **Typografia:** twarde spacje po jednoliterowych wyrazach i między liczbą a jednostką; bez spacji przed %, °C, ′, ″. Szczegóły w `.claude/rules/latex.md`.
- **Podziękowania:** strona opcjonalna. Jeśli jej nie ma, usuwamy ją razem z następującą pustą stroną.
- **Kompilacja:** po większych zmianach co najmniej dwukrotnie, dla spisu treści i odwołań.

## Bibliografia (szablon)

- **Odwołanie w tekście:** `\cite{klucz}`. Pozycje w środowisku `thebibliography`. U nas generuje je `tools/bib2bibitem.py` z `docs/literatura.bib`.
- **Wzór zapisu z szablonu:**
  - książka: W. Lipski, W. Marek, *Analiza kombinatoryczna*, Wyd. Naukowe PWN, Warszawa 1986.
  - artykuł: A. Nowak, B. Kowalski, „Tytuł”, *Czasopismo*, nr 123, s. 45–56, 2019.
  - strona WWW: Autor, *Tytuł*. Dostępne online: adres [dostęp: 30.04.2025].
- Dodatkowe wytyczne: poradnik Biblioteki PRz „Jak sporządzić bibliografię?” (biblio.prz.edu.pl).
- **Hierarchia:** forma zapisu według przykładów z szablonu; poradnik Biblioteki PRz (poz. [5] szablonu) jako wytyczne uzupełniające. Oba źródła sprawdzone 07.10.2026.
- **Zgodne w obu:** spis numerowany; jednolita interpunkcja i wyróżnienia w całej pracy; dla dokumentów online adres i data dostępu („Dostępne online: … [dostęp: …]”).
- **Poradnik dodatkowo:** spis alfabetyczny według nazwisk autorów (bez autora: według tytułu); książki i rozdziały do 3 autorów, przy większej liczbie pierwszy autor i „i in.”; przy odwołaniu do konkretnej informacji podaje się stronę. Norma: PN-ISO 690:2012.
- **Nierozstrzygnięte:** kolejność spisu. Szablon jej nie określa, a lista przykładowa nie jest ani alfabetyczna, ani ułożona według cytowań. Pytanie 6 do promotora; `bib2bibitem.py` ma obsługiwać oba warianty.
- **Przyjęte (D13):** do 3 autorów dla wszystkich typów pozycji, przy większej liczbie pierwszy autor i „i in.”; odnośniki według kategorii z D12 (docs/03).

## Procedura (skrót)

- Student wgrywa pracę (plik elektroniczny) i wymagane dane do systemu APD.
- Promotor akceptuje dane i kieruje plik do sprawdzenia w JSA.
- W ramach jednego badania można wykonać **najwyżej trzy próby** sprawdzenia pliku.
- Na podstawie raportu promotor decyduje o dopuszczeniu pracy do obrony. Przy niejasnym raporcie może wymagać usunięcia manipulacji tekstem.
- **Dokumenty do obrony:** zgodnie z załącznikiem 2 procedury („Wykaz dokumentów wymaganych przed przystąpieniem do obrony”), strona WMiFS „Dokumenty do obrony”. `\dower{uzupełnić listę i terminy po sprawdzeniu w dziekanacie}`
- **Terminy** (złożenie tematu i karty pracy, wgranie do APD przed obroną) nie są podane na stronie z wymaganiami. Uzupełnić w `13_harmonogram.md` po sprawdzeniu w dziekanacie WMiFS.

## Metryczka do strony tytułowej i streszczenia

| Pole | Wartość |
|---|---|
| Autor | [imię i nazwisko] |
| Tytuł | Wpływ promptu na progi bólu agenta LLM |
| Title | The Influence of Prompt Wording on the Pain Thresholds of an LLM Agent (do zatwierdzenia) |
| Promotor / Supervisor | dr inż. Marcin Kowalik, prof. PRz (w wersji EN wg wzoru szablonu, do potwierdzenia) |
| Rodzaj | Praca magisterska |
| Kierunek | Inżynieria i Analiza Danych |
| Miejsce i rok | Rzeszów 2027 (jeśli obrona w 2027) |
| Słowa kluczowe (propozycja, maks. 5) | agent LLM, prompt, próg bólu, uczenie motywowane, funkcja psychometryczna |
| Key words | LLM agent, prompt, pain threshold, motivated learning, psychometric function |
