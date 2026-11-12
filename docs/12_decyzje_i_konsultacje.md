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
| D11 | 2026-11-12 | Obliczenia na komputerze stacjonarnym autora (Windows 10, WSL 2, GTX 1060 6 GB), dostępnym z Maca przez Tailscale. Pełny plan przy zmierzonym czasie wywołania to ok. 50 dni ciągłej pracy komputera; autor to akceptuje pod warunkiem dokładnego sprawdzenia pierwszej próby | Mac ma 8 GB pamięci; komputer stacjonarny może pracować bez przerwy; opis w `05`, sekcja 7 | autor | przyjęta |
| D12 | 2026-10-07 | Każda cytowana pozycja ma być sprawdzalna bez opłat: czytelnik dociera z odnośnika w bibliografii do pełnego tekstu legalnie i za darmo. Kategorie A/B/C i lista wyjątków w docs/03 | Weryfikowalność twierdzeń przez promotora, recenzenta i czytelnika | autor | przyjęta |
| D13 | 2026-10-07 | Konwencje bibliografii: forma zapisu według przykładów szablonu; do 3 autorów, przy większej liczbie pierwszy autor i „i in.”; numer strony obowiązkowy przy cytacie dosłownym, zalecany przy konkretnym twierdzeniu z książki lub długiego raportu; odnośniki: A – DOI jako „Dostępne online: … [dostęp: …]”, B – DOI i adres bezpłatnej kopii z datą dostępu. Kolejność spisu domyślnie alfabetyczna, do potwierdzenia z promotorem (pytanie 6) | Zgodność z szablonem WMiFS i poradnikiem Biblioteki PRz; sprawdzalność (D12) | autor | przyjęta (kolejność: do potwierdzenia) |
| D14 | 2026-10-08 | Porównanie promptów: test ilorazu wiarygodności (wspólne θ vs osobne θ, p z symulacji Monte Carlo, B_MC = 2000) jako test istotności; bootstrap Δθ jako miara wielkości efektu; korekta Holma na wartości p z testu IW | Standard porównań w psychofizyce (prins2018applying); Holm wymaga wartości p, których bootstrap nie daje | autor | przyjęta (do omówienia z promotorem razem z D5; implementacja po etapie lektury) |
| D15 | 2026-10-08 | Kopia wersji wydawniczej udostępniona przez autora bez zgody wydawcy nie spełnia D12. Liczą się: wersja wydawcy w otwartym dostępie, wersja autorska, preprint, kopia w repozytorium lub archiwum o jasnym statusie. Dotyczy: `graham2015opportunistic`, `starzyk2017mlecog`, `starzyk2017needs`, `ryan2000self` (wyjątki w docs/03) | Doprecyzowanie warunku „legalnie” z D12 po audycie dostępności z 08.10 | autor | przyjęta |
| D16 | 2026-10-08 | Łagodzimy D12: każda pozycja ma DOI albo stały odnośnik do wydawcy; legalną bezpłatną kopię (A/B) podajemy, gdy istnieje; pozycje C nie wymagają wyjątku ani zamiennika | Ustalenie z promotorem 08.10.2026 | promotor, autor | przyjęta |
| D17 | 2026-11-11 | Podział narzędzi AI (zastępuje D2): aplikacja Claude do planowania, literatury, szkiców i weryfikacji; sesja z podłączonym repozytorium albo Claude Code do zmian w plikach; Gemini jako niezależny recenzent; Perplexity i Consensus pomocniczo. Opis w `projekt_claude_instrukcje.md`, sekcja 6 | praktyka pracy od 11.11.2026 | autor | propozycja |
| D18 | 2026-11-11 | Plan pracy w wersji 1 (`01`, `02`, `06`) jest zamrożony. Wątpliwości trafiają na listę „Sprawy odłożone” poniżej, do której wracamy dwa razy: po lekturze rdzenia literatury i po pilotażu modelu | ochrona przed ciągłym poprawianiem planu | autor | przyjęta |
| D5 | — | Próg bólu jako punkt środkowy funkcji psychometrycznej z parametrami $\theta$, $k$, $\gamma$, $\lambda$ | `04_metodologia_pomiaru.md` | promotor | propozycja |
| D6 | 2026-11-12 | Model główny `deepseek-r1:14b`, T = 0,8, top_p = 0,9 (ustawione jawnie w `options`), `think` włączone, bez promptu systemowego | Zgodność z pracą referencyjną. Jej `temperature: 0` nie zadziałało (`07`, ograniczenie 2), a model nie ma własnych parametrów próbkowania (`ollama show deepseek-r1:14b --parameters` zwraca tylko znaczniki stopu, sprawdzone 12.11.2026), więc działał na wartościach domyślnych Ollamy: według dokumentacji Modelfile temperatura 0,8 i top_p 0,9 (dostęp 12.11.2026). Praca referencyjna nie podaje wersji Ollamy, więc zgodność wartości domyślnych jest założeniem; w pracy zaznaczamy to i podajemy naszą wersję (z logu). Rozumowanie włączone, bo kod pracy referencyjnej wycina znaczniki `<think>`. Poprzednia propozycja: T = 0,6, top_p = 0,95 (zalecenia producenta) | autor | przyjęta przez autora; do przedstawienia promotorowi |
| D7 | — | Konsekwencja pustej baterii w pętli (ENV 2.0) | `05`, problem 6 | promotor | do ustalenia |
| D8 | — | Forma narracji: bezosobowa czy 1. osoba liczby mnogiej | spójność stylu | autor / promotor | do ustalenia |

## Sprawy odłożone

Lista do D18. Niczego z niej nie wprowadzamy do planu przed wskazanym momentem.

| Nr | Sprawa | Skąd | Wracamy |
|---|---|---|---|
| O1 | Reprezentacja stanu a E1 i H1: przy samych etykietach model widzi 6 różnych stanów baterii, a H1 w obecnym brzmieniu nie jest testowalna | audyt 11.11, M1 i M2 | po pilotażu |
| O2 | Rdzeń i rozszerzenia czynników promptu. Rekomendacja agenta: reprezentacja stanu, próg podany wprost, ramowanie w 3 wariantach, kontrola skrócona; wskazówki zachowania jako rozszerzenie | rozmowa 11.11 | po lekturze rdzenia |
| O3 | Budżet czasu: przy ok. 170–180 s na wywołanie pełny plan (24 675 wywołań) to ok. 50 dni ciągłej pracy. Kolejność eksperymentów i liczba prób | pomiar 11–12.11 | po pilotażu |
| O4 | Moc testu dla różnicy progów (M3), zapas baterii w kontekście neutralnym (M4), powtórzenie testu odzyskiwania parametrów (M6) | audyt 11.11 | po pilotażu |
| O5 | Objętość planu 49,5 strony przy limicie 50 (M7) i nadmiar źródeł w części podrozdziałów (M8) | audyt 11.11 | po lekturze rdzenia |
| O6 | Kto pisze notatki z lektury (obecna zasada w `notatki/README.md`: autor) | audyt 11.11, S10 | przy pierwszej notatce |
| O7 | Pytania do promotora (audyt 11.11, sekcja 8), w tym akceptacja D5 i D6 oraz wersja Ollamy użyta w pracy referencyjnej | audyt 11.11 | po lekturze rdzenia |
| O8 | Tryb bez rozumowania (`E0_pilotaz_bez_think.json`): autor nie stosuje go w przebiegach głównych; porównanie opcjonalne | decyzja 12.11 | po pilotażu |

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
