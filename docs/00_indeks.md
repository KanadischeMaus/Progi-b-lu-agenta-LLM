# Indeks dokumentów

Każdy plik ma jedno zadanie. Nie powielamy treści między plikami. Odsyłamy.

| Plik | Co zawiera | Status |
|---|---|---|
| `01_temat_i_cel.md` | temat, cel, pytania badawcze, hipotezy, zakres, wkład własny | wersja robocza do akceptacji promotora |
| `02_spis_tresci.md` | rozdziały i podrozdziały: opis, źródła, objętość, status | wersja robocza |
| `03_literatura.md` | opis 83 pozycji (78 naukowych i 5 technicznych): do czego służą, gdzie, priorytet, status weryfikacji | zweryfikowane 27.09.2026, uzupełnione 07–08.10.2026 |
| `literatura.bib` | dane bibliograficzne (jedyne źródło) | jw. |
| `bib_audyt.csv` | audyt metadanych i dostępności literatury (OpenAlex, doi.org) | stan 08.10.2026 |
| `notatki/` | notatki z lektury (tekst autora): szablon i kolejka lektury | prowadzone na bieżąco |
| `raporty/` | raporty robocze AI (archiwum z notą, nie są źródłem do cytowania) | archiwum |
| `04_metodologia_pomiaru.md` | definicje (ból, akcja naprawcza, próg), funkcja psychometryczna, metryki, statystyka | propozycja do akceptacji |
| `05_srodowisko_i_kod.md` | środowisko ogrodowe (parametry, akcje, kategorie), znane błędy, rekonstrukcja kodu z listingów, instalacja, schemat logów | rekonstrukcja gotowa i sprawdzona testami |
| `06_plan_eksperymentow.md` | eksperymenty E0–E9, warianty promptów, budżet, rejestr przebiegów | propozycja |
| `07_analiza_pracy_referencyjnej.md` | co zrobiła K. Zawiślak, co przejmujemy, co poprawiamy | gotowe |
| `08_slownik_pojec.md` | terminy PL/EN i oznaczenia | żywy dokument |
| `09_styl_i_rzetelnosc.md` | styl naukowy, cytowanie i parafraza, JSA, recenzja zewnętrzna | gotowe |
| `10_wymogi_formalne.md` | wymagania WMiFS i szablonu, dokumenty do obrony | gotowe, do uzupełnienia o terminy |
| `11_rejestr_AI.md` | dziennik użycia narzędzi AI (podstawa tabeli GenAI) | prowadzony na bieżąco |
| `12_decyzje_i_konsultacje.md` | decyzje projektowe, ustalenia z promotorem, pytania otwarte | prowadzony na bieżąco |
| `13_harmonogram.md` | etapy prac i terminy | do uzupełnienia o datę obrony |
| `projekt_claude_instrukcje.md` | nazwa, opis i instrukcje projektu w aplikacji Claude | gotowe do wklejenia |

## Co przeczytać przy danym zadaniu

| Zadanie | Pliki |
|---|---|
| Pisanie lub redakcja rozdziału | 02 (opis podrozdziału), 03 i `literatura.bib`, 08, 09, `.claude/rules/latex.md` |
| Weryfikacja tekstu autora | to samo co wyżej, plus 04 (rozdziały 4–6) i `results/` |
| Szukanie lub dodawanie literatury | 03, `literatura.bib`, skill `dodaj-zrodlo` |
| Lektura i notatki | `notatki/README.md`, `notatki/_szablon.md`, 03 |
| Kod środowiska, pętli, sondowania | 04, 05, 06, `.claude/rules/kod.md` |
| Analiza wyników, wykresy | 04 (metryki i statystyka), 06 (rejestr przebiegów), `results/README.md` |
| Rozmowa o zakresie i celach | 01, 12, 13 |
| Formalności (APD, JSA, streszczenie, GenAI) | 10, 11 |

## Zasada aktualizacji

- Zmiana zakresu pracy: zaktualizuj 01 i 02 oraz dopisz decyzję w 12.
- Nowe źródło: `literatura.bib` i 03 (skill `dodaj-zrodlo`).
- Nowy przebieg eksperymentu: dopisz go do rejestru w 06.
- Każda sesja pracy z AI: wpis w 11.
