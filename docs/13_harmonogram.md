# Harmonogram

> Jedyny termin: obrona pod koniec czerwca 2027 (datę ogłasza dziekanat). Dat pośrednich nie prowadzimy; plan z września 2026 miał je, ale są nieaktualne.

## Stan bieżący (12.11.2026)

**Etap:** przygotowanie dobiega końca; następny etap to weryfikacja literatury i lektura.

Zrobione 11–12.11.2026:
- repozytorium prywatne, z pracą referencyjną i szablonem w `docs/zrodla/`,
- szkielet pracy w `thesis/` (plan v1 z `02`, bibliografia z `literatura.bib`), wgrany do Overleaf i skompilowany; kolejne wgrania ręcznie, przy kamieniach milowych,
- środowisko obliczeniowe działa (`05`, sekcja 7),
- parametry modelu ustalone (D6), sprzęt ustalony (D11), plan zamrożony (D18).

W toku:
- próba 10 wywołań przy T = 0,8 do dokładnego sprawdzenia przed długim przebiegiem. Pięć punktów: prompt zgodny z listingiem 9a; stan pokazany modelowi poprawnie; odczytana akcja zgodna z odpowiedzią; rozumowanie odnosi się do stanu; ustawienia i wersje zapisane w logu.

Trzy najbliższe zadania:
1. Sprawdzić próbę i uruchomić pierwszy długi przebieg (E0) w `tmux`.
2. Założyć projekt w aplikacji Claude według `projekt_claude_instrukcje.md`.
3. Zweryfikować literaturę w trzech krokach: audyt `tools/sprawdz_bib.py`; pobranie PDF-ów do `docs/zrodla/`; sprawdzenie w tekście, czy źródło podpiera przypisane twierdzenie (najpierw rozdziały 1–3). Bibliografia w `thesis/` to do tego czasu źródła planowane, niezweryfikowane przez autora.

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
