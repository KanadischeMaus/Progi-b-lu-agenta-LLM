# Harmonogram

> Jedyny termin: obrona pod koniec czerwca 2027 (datę ogłasza dziekanat). Dat pośrednich nie prowadzimy; plan z września 2026 miał je, ale są nieaktualne.

## Stan bieżący (13.11.2026)

**Etap:** przygotowanie zakończone; zaczyna się lektura rdzenia literatury; pilotaż przeanalizowany, E1 gotowy do uruchomienia.

Zrobione 11–13.11.2026:
- projekt w aplikacji Claude założony (`projekt_claude_instrukcje.md`),
- selekcja literatury zakończona: 47 pozycji naukowych w wyborze (14 w rdzeniu), 31 w rezerwie; nowa wersja `03`, kolejka lektury w `notatki/README.md`, raporty w `raporty/`,
- pilotaż E0 (100 wywołań) i test powtarzalności (5 przebiegów po 5 wywołań) wykonane; wpisy w rejestrze przebiegów w `06`. Wszystkie odpowiedzi sparsowane; średnio 170 s na wywołanie; przy T = 0 i tym samym ziarnie odpowiedzi nie są identyczne,
- analiza pilotażu (`raporty/E0_analiza_2026-11-13.md`) i wybór wariantów dla E1 (`raporty/E1_warianty_2026-11-13.md`; decyzje D19–D24 w `12`): siatka bez zmian, najpierw blok „bateria”, zapas baterii 2 od E1, E0 pozostaje pilotażem poza porównaniami,
- test powtarzalności po wczytaniu modelu wykonany 13.11.2026: przy T = 0 wynik powtarza się co do znaku, gdy sekwencja wywołań od wczytania modelu jest ta sama (`raporty/E0_analiza_2026-11-13.md`, sekcja 9),
- repozytorium prywatne, z pracą referencyjną i szablonem w `docs/zrodla/`,
- szkielet pracy w `thesis/` (plan v1 z `02`, bibliografia z `literatura.bib`), wgrany do Overleaf i skompilowany; kolejne wgrania ręcznie, przy kamieniach milowych,
- środowisko obliczeniowe działa (`05`, sekcja 7),
- parametry modelu ustalone (D6), sprzęt ustalony (D11), plan zamrożony (D18).

W toku:
- zmiany z `raporty/literatura_zmiany_bib.md` są naniesione w `literatura.bib` (85 wpisów). Do zrobienia na komputerze autora: audyt `python tools/sprawdz_bib.py --bib docs/literatura.bib --out docs/bib_audyt.csv`, bo wymaga dostępu do OpenAlex.

Trzy najbliższe zadania:
1. Lektura rdzenia w kolejności z `notatki/README.md`, zaczynając od `zawislak2025budowa` (prompt 4 w `prompty_startowe.md`, jeden wątek na źródło). PDF-y do `docs/zrodla/`. Dopiero notatka z lektury potwierdza, że źródło podpiera przypisane twierdzenie; bibliografia w `thesis/` to do tego czasu źródła planowane.
2. Obliczenia w kolejności z `raporty/E1_uruchomienie_2026-11-13.md`: E0nt, blok „bateria” (E1, słabe słońce, E2), potem blok „gleba”. Po bloku „bateria”: analiza według planu zapisanego w `12`, wybór reprezentacji dla E3, moc testu (M3). Równolegle na Macu: test odzyskiwania parametrów (M6).
3. Zewnętrzna weryfikacja metadanych 19 pozycji pakietem `raporty/pakiet_perplexity.md`.

## Etapy (kolejność orientacyjna)

| Etap | Zakres | Wynik |
|---|---|---|
| 0. Start | repozytorium, zasady, literatura, konsultacja metody z promotorem (D5, D6) | zaakceptowane `01`, `04` |
| 1. Kod i narzędzie | rekonstrukcja z listingów, ENV 1.1, logowanie, parser, sondowanie, pętla, testy: **gotowe 27.09.2026**; środowisko obliczeniowe: **gotowe 12.11.2026**; do zrobienia: E0 | `results/` E0 |
| 2. E0–E2 | pilotaż, budżet, progi bazowe, reprezentacja stanu | krzywe bazowe, decyzje po E0 w `12` |
| 3. Teoria | rozdziały 1–3 (tryb A lub B), recenzja | szkice rozdz. 1–3 u promotora |
| 4. E3–E6 | kalibracja, ramowanie, wskazówki, kontrole | tabela parametrów, wykresy |
| 5. E7–E8 (+E9) | rywalizacja bólów, pętla zamknięta | mapy, metryki pętli |
| 6. Metoda i wyniki | rozdziały 4–5 | szkic rozdz. 4–5 u promotora |
| 7. Dyskusja i całość | rozdz. 6, wstęp, podsumowanie, streszczenia, dodatki, tabela GenAI | pełna wersja robocza |
| 8. Poprawki | uwagi promotora, recenzja niezależna, korekta, kontrola `\dower`/TODO; ponowne sprawdzenie dostępu do pozycji bronze i kopii na stronach autorów (D12) | wersja końcowa |
| 9. Formalności | APD, JSA (maks. 3 próby), dokumenty do obrony | praca złożona |

## Ryzyka

| Ryzyko | Skutek | Zabezpieczenie |
|---|---|---|
| Model rozumujący jest wolny na posiadanym sprzęcie: zmierzono ok. 170–180 s na wywołanie, czyli ok. 50 dni ciągłej pracy na pełny plan | brak zapasu na powtórki i błędy | start przebiegów jak najwcześniej; najważniejsze eksperymenty najpierw (`12`, O3); wznawianie i `tmux` (`05`, sekcja 7); w razie potrzeby przycięcie planu (`06`) albo serwer uczelni |
| Rekonstrukcja z listingów różni się od kodu, na którym liczyła Klaudia (np. teksty zapasu baterii, białe znaki w promptach) | wyniki nieporównywalne 1:1 z pracą referencyjną | porównujemy wnioski, nie liczby; różnice jawnie opisane (`05`, sekcja 10); wersjonowanie `ENV_VERSION` |
| Brak przejścia progowego w E1 | brak podstawy do E3–E5 | zmiana kontekstu neutralnego / zbioru $A_r$; to również wynik (H1 odrzucona) |
| Limit 50 stron | skracanie na końcu | objętości w `02`; pełne prompty i wyniki w dodatkach |
