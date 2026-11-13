# Zmiany w literatura.bib po selekcji literatury (część 2)

> Stan na 13.11.2026. To lista zmian do naniesienia przez Claude Code (skill `dodaj-zrodlo`, potem audyt `tools/sprawdz_bib.py`). W tej sesji niczego w `literatura.bib` nie zmieniono.
>
> Narzędzie: aplikacja Claude (projekt, wątek „Uzupełnić luki w literaturze, część 2”), model claude-fable-5-2.

Po naniesieniu: 85 wpisów (83 dotychczasowe i 2 nowe). Żaden istniejący klucz, status ani kategoria dostępu się nie zmienia.

## 1. Nowe wpisy (2)

Oba do sekcji „F. Metodologia” w `literatura.bib`. Kategoria dostępu C, więc bez pól `url` i `urldate`.

```bibtex
@book{agresti2013categorical,
  author    = {Agresti, Alan},
  title     = {Categorical Data Analysis},
  edition   = {3},
  publisher = {Wiley},
  address   = {Hoboken, NJ},
  year      = {2013},
  isbn      = {978-0-470-46363-5},
  status    = {Z},
  dostep    = {C},
  rozdzial  = {4.3},
  weryfikacja = {2026-11-12: strona produktu wiley.com (tytuł, 3. wydanie, 752 s., ISBN 978-0-470-46363-5, e-book 978-1-118-71094-4, data wydania XII 2012); strona tytułowa w próbce dystrybutora e-bookshelf.de (Copyright 2013 by John Wiley \& Sons, Hoboken, New Jersey; dane Library of Congress: 3rd ed., ISBN 978-0-470-46363-5, Wiley Series in Probability and Statistics 792); katalog Texas A\&M University: Hoboken, N.J.: Wiley, [2013]; rok 2013 według strony tytułowej i katalogu; brak bezpłatnej kopii (u wydawcy tylko fragmenty); spis treści: 1.4 Statistical Inference for Binomial Parameters (s. 13), rozdz. 5 Logistic Regression (s. 163), 8.1 Nominal Responses: Baseline-Category Logit Models (s. 293); nazwa „przedział Wilsona” w 1.4 do potwierdzenia przy lekturze; zamiennik według decyzji autora z 2026-11-12: Agresti 2019, An Introduction to Categorical Data Analysis, wyd. 3}
}

@book{kleijnen2015design,
  author    = {Kleijnen, Jack P. C.},
  title     = {Design and Analysis of Simulation Experiments},
  edition   = {2},
  publisher = {Springer},
  address   = {Cham},
  year      = {2015},
  isbn      = {978-3-319-18086-1},
  doi       = {10.1007/978-3-319-18087-8},
  status    = {Z},
  dostep    = {C},
  rozdzial  = {4.5},
  weryfikacja = {2026-11-12: portal badawczy Tilburg University (tytuł, 2. wydanie, 2015, International Series in Operations Research \& Management Science t. 230, 322 s., ISBN druk 978-3-319-18086-1, ISBN elektroniczny 978-3-319-18087-8, DOI); springerprofessional.de (spis rozdziałów i streszczenia; streszczenie rozdz. 3: podrozdział 3.5 dotyczy wspólnych liczb losowych, CRN); RePEc (rozdz. 3, s. 83--133, DOI 10.1007/978-3-319-18087-8_3); 2026-11-13: miejsce wydania Cham według katalogów University of Patras, Santa Clara University i College of the Holy Cross (Cham: Springer International Publishing: Imprint: Springer, 2015; XV, 322 s.); portal Tilburg podaje New York; link.springer.com nie odpowiada automatowi, więc brak bezpłatnej kopii przyjęty na podstawie RePEc i braku oznaczenia otwartego dostępu, do potwierdzenia na stronie wydawcy; treść podrozdziału 3.5 do potwierdzenia przy lekturze}
}
```

Uwagi do wpisów:

- Serii wydawniczej nie wpisałem jako pola `series`, bo żaden istniejący wpis `@book` go nie ma i nie wiem, czy `tools/bib2bibitem.py` je obsługuje. Nazwa serii jest w polu `weryfikacja`.
- Pole `rozdzial` dla Agrestiego to 4.3. Regresję logistyczną dla odpowiedzi w trzech kategoriach opisuje docs/04 §6, a docs/02 nie mówi, w którym podrozdziale rozdziału 4 trafi ten opis (sprawa O10 w docs/12). Jeśli opis trafi gdzie indziej, pole trzeba poprawić.
- Znak `&` w polu `weryfikacja` zapisałem jako `\&`, tak jak wymaga BibTeX.

## 2. Poprawki w istniejących wpisach

Dotyczą tylko pola `weryfikacja` siedmiu preprintów z wyboru. Źródła: etap 2 części 2 (`raporty/literatura_selekcja_cz2_etap2.md`).

| Klucz | Pole | Było | Powinno być | Źródło i data |
|---|---|---|---|---|
| `schulhoff2024prompt` | weryfikacja | „…; data v6 i ewentualna wersja recenzowana nieustalone” | zamiast tego fragmentu: „v6 z 2025-02-26 (strona arXiv, 2026-11-12); wersji recenzowanej nie znaleziono (OpenAlex W4399597451: preprint; Semantic Scholar: bez miejsca publikacji; wyszukiwarka), 2026-11-12; pełna strona arXiv bez wierszy Comments, Journal reference i Related DOI (odczyt autora w innej sesji Claude, 2026-11-12)” | arXiv abs 2406.06608, OpenAlex, Semantic Scholar, 12.11.2026; informacja autora z 13.11.2026 |
| `li2023large` | weryfikacja | „arXiv 2307.11760 (raport techniczny; krótka wersja: LLM@IJCAI'23); arXiv API 2026-10-08: najnowsza wersja v7 z 2023-11-12” | dopisać na końcu: „; strona arXiv 2026-11-12: pole Comments podaje, że krótka wersja (v1) została przyjęta na LLM@IJCAI'23, wierszy Journal reference i Related DOI nie ma; wersji w czasopiśmie ani w materiałach konferencji nie znaleziono (OpenAlex W4385291101: preprint; Semantic Scholar: bez miejsca publikacji), 2026-11-12; cytujemy v7 jako preprint (decyzja autora 2026-11-13)” | arXiv abs 2307.11760, OpenAlex, Semantic Scholar, 12.11.2026 |
| `keeling2024can` | weryfikacja | kończy się na „…arXiv API 2026-10-08: najnowsza wersja v1 z 2024-11-01” | dopisać na końcu: „; strona arXiv 2026-11-12: jedyna wersja v1, wierszy Journal reference i Related DOI nie ma; wersji recenzowanej nie znaleziono (OpenAlex W4404355701: preprint; wyszukiwarka), 2026-11-12” | arXiv abs 2411.02432, OpenAlex, 12.11.2026 |
| `bianco2026beyond` | weryfikacja | „wg raportu z 2026-10-08: arXiv abs i PDF” | dopisać na końcu: „; strona arXiv 2026-11-12: v1 z 2026-02-22; wersji recenzowanej nie znaleziono (OpenAlex W7131426686: preprint; wyszukiwarka), 2026-11-12; pełna strona arXiv bez wierszy Comments, Journal reference i Related DOI (odczyt autora w innej sesji Claude, 2026-11-12)” | arXiv abs 2602.19159, OpenAlex, 12.11.2026; informacja autora z 13.11.2026 |
| `masumori2025survival` | weryfikacja | kończy się na „…arXiv API 2026-10-08: najnowsza wersja v1 z 2025-08-18” | dopisać na końcu: „; 2026-11-12: wersji recenzowanej nie znaleziono (OpenAlex W4414491860: preprint; strona publikacji laboratorium Ikegamiego: dział Pre Print; wyszukiwarka); pełna strona arXiv bez wierszy Comments, Journal reference i Related DOI (odczyt autora w innej sesji Claude, 2026-11-12)” | arXiv abs 2508.12920, OpenAlex, strona laboratorium, 12.11.2026; informacja autora z 13.11.2026 |
| `tagliabue2025probing` | weryfikacja | „wg raportu z 2026-10-08: arXiv abs” | dopisać na końcu: „; strona arXiv 2026-11-12: bieżąca wersja v2 z 2026-05-23; wersji recenzowanej nie znaleziono (OpenAlex W4416068638: cztery lokalizacje, same repozytoria; PhilArchive TAGPTP bez czasopisma), 2026-11-12; pełna strona arXiv bez wierszy Comments, Journal reference i Related DOI (odczyt autora w innej sesji Claude, 2026-11-12)” | arXiv abs 2509.07961, OpenAlex, PhilArchive, 12.11.2026; informacja autora z 13.11.2026 |
| `qwen2024qwen25` | weryfikacja | kończy się na „…arXiv API 2026-10-08: najnowsza wersja v2 z 2025-01-03” | dopisać na końcu: „; strona arXiv 2026-11-12: wierszy Comments, Journal reference i Related DOI nie ma; wersji recenzowanej nie znaleziono (OpenAlex W4405655184: preprint), 2026-11-12” | arXiv abs 2412.15115, OpenAlex, 12.11.2026 |

Nie proponuję zmian w polach `title`, `author`, `year`, `eprint`, `status` ani `dostep`: w etapie 2 nie znalazłem w nich rozbieżności ze stronami arXiv. Dwie obserwacje bez zmiany:

- `li2023large`: arXiv zapisuje tytuł „…Can be Enhanced…”, `.bib` „…Can Be Enhanced…”. To różnica w wielkości jednej litery; `.bib` stosuje własną pisownię tytułów wielkimi literami (tak samo w `keeling2024can`).
- `qwen2024qwen25`: strona arXiv wymienia autorów z nazwiska (lista zaczyna się od „Qwen”, potem 42 nazwiska i dopisek o kolejnych autorach), a `.bib` ma autora zbiorowego „Qwen Team”. Zasada 2 dla preprintów mówi o pełnej liście autorów z dokumentu, więc to pole warto sprawdzić przy lekturze PDF. Pozycja jest w pakiecie dla Perplexity.

## 3. Propozycja do decyzji: pole `note` w trzech preprintach

`keeling2024can`, `bianco2026beyond`, `masumori2025survival` i `tagliabue2025probing` mają pole `note = {preprint}` (albo z datą wersji). `li2023large`, `schulhoff2024prompt` i `qwen2024qwen25` tego pola nie mają, choć etap 2 potwierdził, że to preprinty bez wersji recenzowanej.

| Klucz | Pole | Było | Proponuję | Źródło i data |
|---|---|---|---|---|
| `li2023large` | note | brak pola | `note = {preprint}` | etap 2, 12.11.2026 |
| `schulhoff2024prompt` | note | brak pola | `note = {preprint; v6 z 26.02.2025}` | etap 2, 12.11.2026 |
| `qwen2024qwen25` | note | brak pola | `note = {preprint; raport techniczny}` | etap 2, 12.11.2026 |

Rekomendacja: dodać, bo zasada 4 dla preprintów i D13 wymagają zaznaczenia preprintu, a cztery pozostałe wpisy już to pole mają. Zanim Claude Code to naniesie, niech sprawdzi w `tools/bib2bibitem.py`, czy pole `note` trafia do bibliografii; skryptu nie widziałem.

## 4. Zmiana odłożona (nie wykonywać teraz)

| Klucz | Zmiana | Dlaczego odłożona | Kiedy |
|---|---|---|---|
| `liu2024agentbench` | usunąć wpis z `literatura.bib`; usunąć klucz ze źródeł 4.5 w docs/02 i z thesis/ | wpis jest cytowany w docs/02 (zamrożony, D18) i w thesis/; usunięcie teraz zepsułoby cytowania | przy przeglądzie planu po lekturze rdzenia |
| `kuss2005bayesian` | usunąć wpis z `literatura.bib`; usunąć klucz ze źródeł 4.3 w docs/02 i z thesis/ | jak wyżej | przy przeglądzie planu po lekturze rdzenia |

Decyzja autora z 12.11.2026 (usunięcie), doprecyzowana 13.11.2026 (wykonanie odłożone). Do tego czasu obie pozycje są w docs/03 w sekcji „Rezerwowe i usunięte”.

## 5. Czego ta lista nie obejmuje

- Pól `rozdzial` pozycji rezerwowych: zostają, bo docs/02 jest zamrożony.
- Wpisów dla rezerwy spoza `.bib` (Agresti 2019, Law 2024): powstaną dopiero po decyzji o powrocie pozycji. Dane Law 2024 potwierdzone u wydawcy 12.11.2026: wyd. 6, McGraw Hill, © 2024, ISBN 978-1-264-26824-5; liczba stron rozbieżna w księgarniach (688 i 656).
- Liczby stron sześciu pozycji rdzenia bez pola `pages`: do odczytania z PDF przy lekturze.
