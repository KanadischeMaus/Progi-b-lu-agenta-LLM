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
| D12 | 2026-10-07 | Każda cytowana pozycja ma być sprawdzalna bez opłat: czytelnik dociera z odnośnika w bibliografii do pełnego tekstu legalnie i za darmo. Kategorie A/B/C i lista wyjątków w docs/03 | Weryfikowalność twierdzeń przez promotora, recenzenta i czytelnika | autor | przyjęta |
| D13 | 2026-10-07 | Konwencje bibliografii: forma zapisu według przykładów szablonu; do 3 autorów, przy większej liczbie pierwszy autor i „i in.”; numer strony obowiązkowy przy cytacie dosłownym, zalecany przy konkretnym twierdzeniu z książki lub długiego raportu; odnośniki: A – DOI jako „Dostępne online: … [dostęp: …]”, B – DOI i adres bezpłatnej kopii z datą dostępu. Kolejność spisu domyślnie alfabetyczna, do potwierdzenia z promotorem (pytanie 6) | Zgodność z szablonem WMiFS i poradnikiem Biblioteki PRz; sprawdzalność (D12) | autor | przyjęta (kolejność: do potwierdzenia) |
| D14 | 2026-10-08 | Porównanie promptów: test ilorazu wiarygodności (wspólne θ vs osobne θ, p z symulacji Monte Carlo, B_MC = 2000) jako test istotności; bootstrap Δθ jako miara wielkości efektu; korekta Holma na wartości p z testu IW | Standard porównań w psychofizyce (prins2018applying); Holm wymaga wartości p, których bootstrap nie daje | autor | przyjęta (do omówienia z promotorem razem z D5; implementacja po etapie lektury) |
| D15 | 2026-10-08 | Kopia wersji wydawniczej udostępniona przez autora bez zgody wydawcy nie spełnia D12. Liczą się: wersja wydawcy w otwartym dostępie, wersja autorska, preprint, kopia w repozytorium lub archiwum o jasnym statusie. Dotyczy: `graham2015opportunistic`, `starzyk2017mlecog`, `starzyk2017needs`, `ryan2000self` (wyjątki w docs/03) | Doprecyzowanie warunku „legalnie” z D12 po audycie dostępności z 08.10 | autor | przyjęta |
| D16 | 2026-10-08 | Łagodzimy D12: każda pozycja ma DOI albo stały odnośnik do wydawcy; legalną bezpłatną kopię (A/B) podajemy, gdy istnieje; pozycje C nie wymagają wyjątku ani zamiennika | Ustalenie z promotorem 08.10.2026 | promotor, autor | przyjęta |
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

### 2026-10-08: konsultacja (forma: Wskazówka - od czego zacząć)
Ustalenia:
1. źródła płatne (np. IEEE) cytujemy przez DOI (D16);
2. zalecenie promotora: zacząć od przestudiowania tematu, czyli przeglądu literatury.

## Pytania otwarte

Lista zbiorcza. Szczegóły w `01_temat_i_cel.md`, sekcja „Pytania do promotora”.
1. Akceptacja definicji progu (D5).
2. Podział zakresu z pracą Kingi.
3. Limit objętości.
4. Drugi model (E9): tak czy nie?
5. Sprzęt do obliczeń.
6. Kolejność bibliografii: alfabetyczna (poradnik Biblioteki PRz, do którego odsyła szablon) czy według pierwszego cytowania? Szablon tego nie określa.
