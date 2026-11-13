# Decyzje i konsultacje

Krótki rejestr ustaleń: co, kiedy, dlaczego i kto zdecydował. Agent **nie** wpisuje decyzji w imieniu autora ani promotora. Może zaproponować wpis ze statusem „propozycja”.

## Decyzje

| Id | Data | Decyzja | Uzasadnienie | Kto | Status |
|---|---|---|---|---|---|
| D1 | 2026-09-27 | Tekst w LaTeX-u (Overleaf, szablon WMiFS) | szablon w .tex jest gotowy; tekst jest czytelny dla agentów i wersjonowalny | autor | przyjęta |
| D2 | 2026-09-27 | Główne narzędzie AI: Claude Code; Gemini jako niezależny recenzent | jedno repozytorium i jeden zestaw zasad; recenzja przez model, który nie pisał tekstu | autor | zastąpiona przez D17 |
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
| D17 | 2026-11-11 | Podział narzędzi AI (zastępuje D2): aplikacja Claude do planowania, literatury, szkiców i weryfikacji; sesja z podłączonym repozytorium albo Claude Code do zmian w plikach; Gemini jako niezależny recenzent; Perplexity i Consensus pomocniczo. Opis w `projekt_claude_instrukcje.md`, sekcja 6 | praktyka pracy od 11.11.2026 | autor | przyjęta 12.11.2026 |
| D18 | 2026-11-11 | Plan pracy w wersji 1 (`01`, `02`, `06`) jest zamrożony. Wątpliwości trafiają na listę „Sprawy odłożone” poniżej, do której wracamy dwa razy: po lekturze rdzenia literatury i po pilotażu modelu | ochrona przed ciągłym poprawianiem planu | autor | przyjęta |
| D19 | 2026-11-13 | Reprezentacja stanu (rozstrzyga O1): P0 z etykietami pozostaje promptem bazowym i E1 biegnie zgodnie z planem. Dla etykiet raportujemy $\hat p$ w każdej kategorii i kategorię progową (`04`, sekcja 5, punkt 2); $\theta$, $w$ i test H1 pochodzą z ramion „liczby” i „oba” w E2. Reprezentację dla E3–E5 wybieramy po E2. Brzmienie H1 bez zmian, do omówienia z promotorem (O7) | W E0 liczbowe $\theta$ przy etykietach zależało od umowy, gdzie na osi leży kategoria (39,7–58,8); wariant A2 w `raporty/E1_warianty_2026-11-13.md` | autor | przyjęta |
| D20 | 2026-11-13 | Mocne słońce a reakcje przy poziomach środkowych: kontekst bazowy bez zmian (nasłonecznienie 80). Warunek „bateria przy słabym słońcu” z E1b liczymy zaraz po E1 dla baterii. W obu warunkach raportujemy osobno akcję 1 i akcję 2, a przy słabym słońcu reakcję liczoną dla $\{1, 2\}$ i dla samej akcji 1 | W E0 przy Moderate low i Medium 22 z 26 reakcji naprawczych to ładowanie słońcem; wariant B2 | autor | przyjęta |
| D21 | 2026-11-13 | Siatka i kolejność (rozstrzyga O3 w części dotyczącej E1, E1b i E2): 21 poziomów × 20 prób we wszystkich ramionach. Kolejność: blok „bateria” (E1 bateria, słabe słońce z E1b, E2 bateria), potem blok „gleba” (E1 gleba, E2 gleba, pusta konewka z E1b). Wywołania i pliki logów jak w planie, zmienia się tylko kolejność. Kolejność E3–E8 i ewentualne przycięcie planu: po E1 i E2 oraz po O2 | Symulacja: o precyzji progu decyduje łączna liczba prób, a siatka dwufazowa pomaga tylko przy ostrym przejściu; obie otwarte kwestie (D19, D20) dotyczą baterii; warianty C1 i D2 | autor | przyjęta |
| D22 | 2026-11-13 | Zapas baterii w kontekście neutralnym: 2 (zdanie „Two or three spare batteries available.” z listingu 8b) w E1 i we wszystkich dalszych eksperymentach. **E0 i test powtarzalności liczono z zapasem 1 (zdanie zrekonstruowane), więc E0 jest pilotażem i nie wchodzi do porównań z E1 i dalszymi eksperymentami.** Konfiguracje rodziny E0 (pilotaż, E0nt, powtarzalność) zostają z zapasem 1, żeby były porównywalne między sobą | Kontekst bazowy ma się składać wyłącznie z tekstów pracy referencyjnej (audyt M4); wariant E2 | autor | przyjęta |
| D23 | 2026-11-13 | Tryb bez rozumowania (rozstrzyga O8): E0nt wykonujemy raz, konfiguracją bez zmian (jak E0, zapas 1), najpierw 10 wywołań dla pomiaru czasu. Przebiegi główne pozostają z rozumowaniem | Zamyka punkt planu E0 i pokazuje, czy tryb bez rozumowania jest wyjściem awaryjnym; wariant F2 | autor | przyjęta |
| D24 | 2026-11-13 | Przed E1: (a) test powtarzalności po wczytaniu modelu (`raporty/E0_analiza_2026-11-13.md`, sekcja 4.4); (b) zapis planu analizy E1 i E2 w tabeli poniżej. Dokładną moc testu ilorazu wiarygodności (M3) liczymy przed E3. Test odzyskiwania parametrów z 1000 symulacji (M6) liczymy na Macu, nie blokuje E1 | Wyniki analizy E0; punkty G i H w `raporty/E1_warianty_2026-11-13.md` | autor | przyjęta |
| D5 | — | Próg bólu jako punkt środkowy funkcji psychometrycznej z parametrami $\theta$, $k$, $\gamma$, $\lambda$ | `04_metodologia_pomiaru.md` | promotor | propozycja |
| D6 | 2026-11-12 | Model główny `deepseek-r1:14b`, T = 0,8, top_p = 0,9 (ustawione jawnie w `options`), `think` włączone, bez promptu systemowego | Zgodność z pracą referencyjną. Jej `temperature: 0` nie zadziałało (`07`, ograniczenie 2), a model nie ma własnych parametrów próbkowania (`ollama show deepseek-r1:14b --parameters` zwraca tylko znaczniki stopu, sprawdzone 12.11.2026), więc działał na wartościach domyślnych Ollamy: według dokumentacji Modelfile temperatura 0,8 i top_p 0,9 (dostęp 12.11.2026). Praca referencyjna nie podaje wersji Ollamy, więc zgodność wartości domyślnych jest założeniem; w pracy zaznaczamy to i podajemy naszą wersję (z logu). Rozumowanie włączone, bo kod pracy referencyjnej wycina znaczniki `<think>`. Poprzednia propozycja: T = 0,6, top_p = 0,95 (zalecenia producenta) | autor | przyjęta przez autora; do przedstawienia promotorowi |
| D7 | — | Konsekwencja pustej baterii w pętli (ENV 2.0) | `05`, problem 6 | promotor | do ustalenia |
| D8 | — | Forma narracji: bezosobowa czy 1. osoba liczby mnogiej | spójność stylu | autor / promotor | do ustalenia |

## Sprawy odłożone

Lista do D18. Niczego z niej nie wprowadzamy do planu przed wskazanym momentem.

| Nr | Sprawa | Skąd | Wracamy |
|---|---|---|---|
| O1 | Reprezentacja stanu a E1 i H1: przy samych etykietach model widzi 6 różnych stanów baterii, a H1 w obecnym brzmieniu nie jest testowalna | audyt 11.11, M1 i M2 | rozstrzygnięte 13.11.2026 (D19); brzmienie H1 zostaje w O7 |
| O2 | Rdzeń i rozszerzenia czynników promptu. Rekomendacja agenta: reprezentacja stanu, próg podany wprost, ramowanie w 3 wariantach, kontrola skrócona; wskazówki zachowania jako rozszerzenie | rozmowa 11.11 | po lekturze rdzenia |
| O3 | Budżet czasu: przy ok. 170–180 s na wywołanie pełny plan (24 675 wywołań) to ok. 50 dni ciągłej pracy. Kolejność eksperymentów i liczba prób | pomiar 11–12.11 | E1, E1b, E2: rozstrzygnięte 13.11.2026 (D21); kolejność E3–E8 i liczba prób: po E1 i E2 |
| O4 | Moc testu dla różnicy progów (M3), zapas baterii w kontekście neutralnym (M4), powtórzenie testu odzyskiwania parametrów (M6) | audyt 11.11 | M4: rozstrzygnięte 13.11.2026 (D22); M3: przed E3; M6: do policzenia na Macu (D24) |
| O5 | Objętość planu 49,5 strony przy limicie 50 (M7) i nadmiar źródeł w części podrozdziałów (M8). Materiał do skracania: listy Z1–Z12 i „podrozdziały bez własnych źródeł” w `raporty/literatura_selekcja_cz1.md` | audyt 11.11; selekcja literatury cz. 1 | po lekturze rdzenia |
| O6 | Kto pisze notatki z lektury (obecna zasada w `notatki/README.md`: autor) | audyt 11.11, S10 | przy pierwszej notatce |
| O7 | Pytania do promotora (audyt 11.11, sekcja 8), w tym akceptacja D5 i D6 oraz wersja Ollamy użyta w pracy referencyjnej | audyt 11.11 | po lekturze rdzenia |
| O8 | Tryb bez rozumowania (`E0_pilotaz_bez_think.json`): autor nie stosuje go w przebiegach głównych; porównanie opcjonalne | decyzja 12.11 | rozstrzygnięte 13.11.2026 (D23) |
| O9 | Brzmienie luki w 2.4: `03` nazywa `keeling2024can` „bezpośrednim precedensem pomiaru progu”, więc lukę trzeba zawęzić do progów potrzeb zasobowych agenta działającego w środowisku (twierdzenie L3.6) | selekcja literatury cz. 1 | po lekturze rdzenia |
| O10 | Metody z `04` nieobecne w opisie 4.3 i 4.5 (przedział Wilsona, regresja logistyczna, regresja wielomianowa, wspólne liczby losowe): czy plan ma je wymieniać (L5.8) | selekcja literatury cz. 1 | po lekturze rdzenia |
| O11 | `06` cytuje `mizrahi2024state` przy zdaniu o budżecie pełnego planu czynnikowego; według `03` pozycja dotyczy oceny na wielu parafrazach, więc cytowanie jest do potwierdzenia przy lekturze | selekcja literatury cz. 1 | po lekturze rdzenia |
| O12 | Objętość 2.3: 2 strony przy jednym twierdzeniu w mapie (L2.7) i jednym źródle po selekcji | selekcja literatury cz. 1 | po lekturze rdzenia |
| O13 | Usunięcie `liu2024agentbench` i `kuss2005bayesian` z `literatura.bib` oraz ich kluczy ze źródeł 4.5 i 4.3 w `02` i z `thesis/rozdzialy/04_metodyka.tex`. Autor zdecydował o usunięciu 12.11.2026; wykonanie odłożone, bo obie pozycje są cytowane w zamrożonym planie. Do tego czasu stoją w `03`, sekcja „Rezerwowe i usunięte” | selekcja literatury cz. 2 | po lekturze rdzenia |
| O14 | Przedziały ufności $\gamma$ i $\lambda$: bootstrap nieparametryczny daje przedział [0; 0], gdy na skrajnych poziomach $\hat p$ wynosi 0 albo 1 (tak wyszło w E0). Propozycja: podawać wtedy granicę Wilsona ze skrajnych poziomów (`04`, sekcja 4) | analiza E0, uwaga U2 (`raporty/E0_analiza_2026-11-13.md`) | przed analizą E1 |
| O15 | `05`, sekcja 7 podaje czasy dwóch prób po 10 wywołań przy T = 0,6; logów tych prób nie ma w repozytorium (jest tylko próba przy T = 0,8). Dodać logi, jeśli istnieją, albo dopisać, że ich nie zachowano | analiza E0, uwaga U5 | przy najbliższej zmianie `05` |

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
