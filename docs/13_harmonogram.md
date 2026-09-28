# Harmonogram

> Data obrony: `\dower{do ustalenia}`. Terminy formalne (karta pracy, wgranie do APD): `\dower{sprawdzić w dziekanacie WMiFS}`.
>
> Plan poniżej zakłada obronę pod koniec czerwca 2027. Przy innej dacie przesuwamy kolumnę „do”, zachowując długości etapów.

| Etap | Zakres | Wynik | Do (propozycja) |
|---|---|---|---|
| 0. Start | repozytorium, zasady, literatura, konsultacja metody z promotorem (D5, D6) | zaakceptowane `01`, `04` | 2026-10-18 |
| 1. Kod i narzędzie | rekonstrukcja z listingów, ENV 1.1, logowanie, parser, sondowanie, pętla, testy: **gotowe 27.09.2026**; do zrobienia: instalacja na Macu, E0 | `results/` E0 | 2026-10-31 |
| 2. E0–E2 | pilotaż, budżet, progi bazowe, reprezentacja stanu | krzywe bazowe, decyzje po E0 w `12` | 2026-12-13 |
| 3. Teoria | rozdziały 1–3 (tryb A lub B), recenzja | szkice rozdz. 1–3 u promotora | 2027-01-24 |
| 4. E3–E6 | kalibracja, ramowanie, wskazówki, kontrole | tabela parametrów, wykresy | 2027-03-07 |
| 5. E7–E8 (+E9) | rywalizacja bólów, pętla zamknięta | mapy, metryki pętli | 2027-04-04 |
| 6. Metoda i wyniki | rozdziały 4–5 | szkic rozdz. 4–5 u promotora | 2027-04-30 |
| 7. Dyskusja i całość | rozdz. 6, wstęp, podsumowanie, streszczenia, dodatki, tabela GenAI | pełna wersja robocza | 2027-05-23 |
| 8. Poprawki | uwagi promotora, recenzja niezależna, korekta, kontrola `\dower`/TODO | wersja końcowa | 2027-06-06 |
| 9. Formalności | APD, JSA (maks. 3 próby), dokumenty do obrony | praca złożona | `\dower{wg terminów dziekanatu}` |

## Ryzyka

| Ryzyko | Skutek | Zabezpieczenie |
|---|---|---|
| Model rozumujący jest wolny na posiadanym sprzęcie | plan E3–E8 się nie mieści | E0 wcześnie; przycięcie planu (`06`); tryb `think=False` jako czynnik; serwer uczelni |
| Rekonstrukcja z listingów różni się od kodu, na którym liczyła Klaudia (np. teksty zapasu baterii, białe znaki w promptach) | wyniki nieporównywalne 1:1 z pracą referencyjną | porównujemy wnioski, nie liczby; różnice jawnie opisane (`05`, sekcja 10); wersjonowanie `ENV_VERSION` |
| Brak przejścia progowego w E1 | brak podstawy do E3–E5 | zmiana kontekstu neutralnego / zbioru $A_r$; to również wynik (H1 odrzucona) |
| Limit 50 stron | skracanie na końcu | objętości w `02`; pełne prompty i wyniki w dodatkach |
