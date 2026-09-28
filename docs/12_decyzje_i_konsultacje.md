# Decyzje i konsultacje

Krótki rejestr ustaleń: co, kiedy, dlaczego i kto zdecydował. Agent **nie** wpisuje decyzji w imieniu autora ani promotora. Może zaproponować wpis ze statusem „propozycja”.

## Decyzje

| Id | Data | Decyzja | Uzasadnienie | Kto | Status |
|---|---|---|---|---|---|
| D1 | 2026-09-27 | Tekst w LaTeX-u (Overleaf, szablon WMiFS) | szablon w .tex jest gotowy; tekst jest czytelny dla agentów i wersjonowalny | autor | przyjęta |
| D2 | 2026-09-27 | Główne narzędzie AI: Claude Code; Gemini jako niezależny recenzent | jedno repozytorium i jeden zestaw zasad; recenzja przez model, który nie pisał tekstu | autor | przyjęta |
| D3 | 2026-09-27 | Tryby pracy: A (agent pisze, autor poprawia) i B (autor pisze, agent weryfikuje) | preferencja autora | autor | przyjęta |
| D4 | 2026-09-27 | Bibliografia: jedno źródło danych (`docs/literatura.bib`), `\bibitem` generowane skryptem | spójność i brak ręcznych błędów przy formacie z szablonu | autor | przyjęta |
| D9 | 2026-09-27 | Kod odtworzony z listingów pracy referencyjnej; elementy nieobecne w listingach zrekonstruowane i opisane (`05`, sekcja 10) | listingi to jedyne źródło kodu; promotor nie przekaże plików | autor | przyjęta |
| D10 | 2026-09-27 | Prompt bazowy P0 = `ref_v1` (listing 9a bez zmian w treści) | ciągłość z pracą referencyjną; poprawki tylko w kodzie | autor | przyjęta |
| D5 | — | Próg bólu jako punkt środkowy funkcji psychometrycznej z parametrami $\theta$, $k$, $\gamma$, $\lambda$ | `04_metodologia_pomiaru.md` | promotor | propozycja |
| D6 | — | Model główny `deepseek-r1:14b`, T = 0,6, top_p = 0,95, bez promptu systemowego | ciągłość z pracą referencyjną; zalecenia producenta | promotor | propozycja |
| D7 | — | Konsekwencja pustej baterii w pętli (ENV 2.0) | `05`, problem 6 | promotor | do ustalenia |
| D8 | — | Forma narracji: bezosobowa czy 1. osoba liczby mnogiej | spójność stylu | autor / promotor | do ustalenia |

## Plan analizy zapisany przed eksperymentem

Wypełnić przed uruchomieniem E3, E4, E5 (ochrona przed dopasowywaniem analizy do wyników).

| Eksperyment | Hipoteza | Metryka główna | Test / kryterium | Data zapisu |
|---|---|---|---|---|
| E3 | | | | |
| E4 | | | | |
| E5 | | | | |

## Konsultacje z promotorem

Szablon wpisu:

```
### RRRR-MM-DD: konsultacja (forma: spotkanie/e-mail)
Omówione: ...
Ustalenia: ... (→ przenieść do tabeli decyzji)
Zadania do następnego spotkania: ...
```

## Pytania otwarte

Lista zbiorcza. Szczegóły w `01_temat_i_cel.md`, sekcja „Pytania do promotora”.
1. Akceptacja definicji progu (D5).
2. Podział zakresu z pracą Kingi.
3. Limit objętości.
4. Drugi model (E9): tak czy nie?
5. Sprzęt do obliczeń.
6. Format bibliografii, DOI.
