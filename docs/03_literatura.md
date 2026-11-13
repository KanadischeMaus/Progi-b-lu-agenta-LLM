# Literatura

Dane bibliograficzne są w `literatura.bib`. Ten plik mówi, **do czego** każda pozycja służy.

> Wersja po selekcji literatury (część 1 z 12.11.2026, część 2 z 12–13.11.2026). Podstawa: `raporty/literatura_selekcja_cz1.md` (mapa twierdzeń L1–L7, oceny pozycji) oraz raporty z etapów 1 i 2 części 2. Oznaczenia L1.1, L1.2, … w tabelach to twierdzenia z tej mapy.
>
> Plan pracy (docs/01, 02, 06) jest zamrożony (D18), więc docs/02 nadal wymienia w źródłach także pozycje rezerwowe i dwie pozycje do usunięcia. Przypisania w docs/02 uzgodnimy przy przeglądzie planu po lekturze rdzenia.

- **Liczba pozycji w wyborze:** 47 naukowych i 3 techniczne (sekcja G). Zakres założony dla pozycji naukowych: 30–50.
- **Poza wyborem:** 31 rezerwowych, 2 do usunięcia (wykonanie odłożone) i 2 formalne, których w pracy nie cytujemy. Lista z powodami: sekcja „Rezerwowe i usunięte”.
- **Wpisy w `literatura.bib`** po naniesieniu zmian z `raporty/literatura_zmiany_bib.md`: 85 (80 naukowych, 5 technicznych lub formalnych).
- **Priorytet** (według selekcji z 12.11.2026; zastępuje wcześniejszy podział R 52 i U 26):
  - R (rdzeń, 14 pozycji naukowych): bez nich nie da się postawić pytania, hipotezy albo metody; czytam w całości i robię notatkę,
  - U (uzupełniająca, 33 pozycje naukowe): podpiera pojedyncze twierdzenie; czytam całość albo wskazany fragment.
- **Status** (sprawdzone 27.09.2026, uzupełnione 07–08.10.2026 i 12–13.11.2026; źródło i data w polu `weryfikacja`). W wyborze: Z 37, K 9, ? 1.
  - **Z:** istnienie i dane sprawdzone online (strona wydawcy, DOI, ACL Anthology, PMLR, arXiv albo strona autora),
  - **K:** pozycja klasyczna, dane standardowe, nie sprawdzano ich w tej sesji; przy pierwszym cytowaniu warto potwierdzić strony i DOI,
  - **?:** pozycja potwierdzona, ale konkretne pole wymaga sprawdzenia (opis w polu `weryfikacja` w `.bib`).
- **Dostęp w wyborze** (47 naukowych): A 34, B 4, C 9. Pozycje C: `starzyk2017needs`, `graham2015opportunistic`, `bonabeau1996quantitative`, `russell2020artificial`, `tversky1981framing`, `kingdom2016psychophysics`, `holm1979simple`, `agresti2013categorical`, `kleijnen2015design`. Ich pełny tekst trzeba zdobyć przez bibliotekę.
- **Zasada:** zanim coś zacytujemy, czytamy odpowiedni fragment źródła. Kolumna „Twierdzenie” mówi, co praca chce na tej pozycji oprzeć, a nie co pozycja na pewno zawiera. Potwierdzenie daje dopiero notatka z lektury.
- **Kolumna „Co przeczytać”:** „całość” ze stronami z `literatura.bib` albo fragment opisany tematem. Dopisek „do potwierdzenia” znaczy, że tekstu nie widziałem i fragment trzeba odnaleźć w spisie treści.

## Kryterium dostępności (D12)

Złagodzone przez D16.

| Kat. | Warunek | Zapis w bibliografii |
|---|---|---|
| A | pełny tekst bezpłatny u wydawcy (OpenAlex: diamond, gold, hybrid, bronze) | DOI |
| B | wydawca pobiera opłatę, legalna kopia w repozytorium (arXiv, PMC, repozytorium uczelni, strona autora) | DOI + odnośnik do kopii; zaznaczamy, jeśli to preprint |
| C | brak bezpłatnej kopii | cytujemy przez DOI lub stronę wydawcy |
| ? | nieustalone | do ustalenia w audycie (etap 3) |

- Kopie z serwisów pirackich (np. Sci-Hub) nie są kopią legalną.
- Kopia wersji wydawniczej udostępniona przez autora bez zgody wydawcy nie spełnia D12 (D15).
- Cytat dosłowny i numer strony podajemy według wersji, do której prowadzi odnośnik.
- Dostępność typu bronze może zniknąć; przed oddaniem pracy sprawdzamy ją ponownie.
- W `literatura.bib`: pole `dostep = {A|B|C|?}`, dla B pole `url` z adresem kopii i `urldate`.
- Książki: wystarcza pełny opis (autorzy, tytuł, wydanie, wydawca, miejsce, rok); ISBN dopisujemy, jeśli jest potwierdzony u wydawcy lub w katalogu bibliotecznym.
- Rok w kluczu nowej pozycji = rok cytowanej wersji (np. `schlatter2026incomplete`, `cedro2026cash`, `agresti2013categorical`). Istniejących kluczy nie zmieniamy.
- `zawislak2025budowa`: dostęp przez Bibliotekę PRz.

### Preprinty i manuskrypty

Brak recenzji sam w sobie nie wyklucza pozycji. Preprint lub manuskrypt dopuszczamy, jeśli:
1. ma stały identyfikator z wersją (arXiv vN, Zenodo, OSF) albo zarchiwizowaną kopię (Web Archive) z datą;
2. ma kompletne metadane wzięte z samego dokumentu (pełna lista autorów, tytuł danej wersji);
3. pełni w pracy konkretną funkcję;
4. w tekście zaznaczamy, że wynik pochodzi z preprintu, gdy opiera się na nim kluczowe twierdzenie.

W wyborze jest siedem preprintów: `keeling2024can`, `bianco2026beyond`, `masumori2025survival`, `tagliabue2025probing`, `li2023large`, `schulhoff2024prompt`, `qwen2024qwen25`. Wersji recenzowanej nie znaleziono dla żadnego z nich (stan na 12.11.2026: strony arXiv, OpenAlex, Semantic Scholar, wyszukiwarka; szczegóły w `raporty/literatura_selekcja_cz2_etap2.md`). Sprawdzenie powtarzamy raz, na miesiąc przed oddaniem pracy.

Twierdzenia oparte wyłącznie na preprintach. Przy każdym zaznaczamy w tekście, że wynik pochodzi z preprintu (zasada 4):
1. L3.3: LLM przełączają się po przekroczeniu progu intensywności w grze punkty–ból: `keeling2024can`, replikacja `bianco2026beyond` (3.4, 4.2, 6.2);
2. L3.2: agenci LLM w symulacji z ograniczonymi zasobami wykazują zachowania „przetrwania”: `masumori2025survival` (2.4, 3.4, 4.5, 6.2);
3. L3.5: preferencje deklarowane nie muszą zgadzać się z wyborami: `tagliabue2025probing` (3.4);
4. L4.1: nazewnictwo elementów promptu: `schulhoff2024prompt` (3.1);
5. część L3.4, format bodźca (liczby a etykiety): `bianco2026beyond` (3.4);
6. część L4.6, bodźce emocjonalne w prompcie: `li2023large` (3.3); recenzowaną część L4.6 podpiera `jones2022capturing`;
7. część L2.5, model bazowy destylatu: `qwen2024qwen25` (2.2, 4.1).

Osiem preprintów jest w rezerwie (`tagliabue2026pain`, `ren2026ai`, `berg2026language`, `schlatter2026incomplete`, `mikaelson2025beyond`, `hagendorff2023machine`, `miller2024adding`, `long2024taking`). Ich wersje recenzowane sprawdzamy dopiero wtedy, gdy pozycja wraca do wyboru.

## A. Motywacja, potrzeby, ból (teoria): rozdz. 1 i 6.1

| Klucz | Pozycja | Twierdzenie, które podpiera | Podrozdział | Prio | St. | Co przeczytać |
|---|---|---|---|---|---|---|
| `starzyk2017needs` | Starzyk, Graham, Puzio 2017, IEEE TNNLS | L1.5–L1.7: ból prymitywny rośnie z odległością od zaspokojenia potrzeby, agent działa po przekroczeniu progu; bóle abstrakcyjne dotyczą zasobów; cel wybiera rywalizacja (WTA) | 1.4, 4.2, 6.1 | R | Z | całość, s. 2528–2540 (13 s.) |
| `keramati2014homeostatic` | Keramati, Gutkin 2014, eLife | L1.2, L1.4: redukcja odchylenia zmiennych wewnętrznych od wartości zadanej jako źródło motywacji; homeostatyczne RL | 1.2, 1.3, 4.5, 6.1 | R | Z | całość (artykuł e04811; liczba stron do uzupełnienia) |
| `sharkey2025could` | Sharkey 2025, *AI & Society* | L1.8, L6.4: ból rozumiany funkcjonalnie, jako sygnał sterujący; próg behawioralny nie dowodzi odczuwania | 1.5, 6.3 | R | Z | całość, s. 3641–3651 (11 s.) |
| `starzyk2012motivated` | Starzyk, Graham, Raif, Tan 2012, Cognitive Systems Research | L1.6, L1.4: tworzenie celów abstrakcyjnych w toku uczenia; różnica względem RL (przypisanie do potwierdzenia przy lekturze) | 1.4 | U | Z | całość, s. 10–25 (16 s.) |
| `graham2015opportunistic` | Graham, Starzyk, Jachyra 2015, IEEE TNNLS | L1.9: agent motywowany działa też oportunistycznie, poniżej progu bólu | 1.4, 6.1 | U | Z | całość, s. 1735–1746 (12 s.) |
| `maslow1943theory` | Maslow 1943, Psychological Review | L1.3: potrzeby mają różne pierwszeństwo (hierarchia); tło rywalizacji bólów | 1.2 | U | K | fragment: część o hierarchii potrzeb i ich pierwszeństwie (do potwierdzenia); artykuł ma s. 370–396 |
| `oudeyer2007intrinsic` | Oudeyer, Kaplan 2007, Frontiers in Neurorobotics | L1.4: obliczeniowe modele motywacji wewnętrznej (typologia podejść) | 1.3 | U | Z | całość (artykuł nr 6; liczba stron do uzupełnienia) |
| `bonabeau1996quantitative` | Bonabeau, Theraulaz, Deneubourg 1996, *Proc. R. Soc. B* | L7.1: sigmoidalna funkcja progowa odpowiedzi na bodziec w modelach podziału pracy; czy ma parametr stromości: do potwierdzenia przy lekturze | 6.1 | U | Z | całość, s. 1565–1569 (5 s.) |

## B. Agenci i uczenie ze wzmocnieniem: rozdz. 1.1

| Klucz | Pozycja | Twierdzenie, które podpiera | Podrozdział | Prio | St. | Co przeczytać |
|---|---|---|---|---|---|---|
| `russell2020artificial` | Russell, Norvig 2020, *AI: A Modern Approach*, wyd. 4 | L1.1: agent odbiera stan środowiska i wybiera akcje | 1.1 | U | K | fragment: rozdział o agentach i środowiskach (do potwierdzenia) |
| `sutton2018reinforcement` | Sutton, Barto 2018, *Reinforcement Learning*, wyd. 2 | L1.1, L1.4: stan, akcja, nagroda, polityka; tło dla motywacji w RL | 1.1 | U | K | fragment: wprowadzenie i rozdział definiujący stan, akcję, nagrodę i politykę (do potwierdzenia) |
| `astrom2021feedback` | Åström, Murray 2021, *Feedback Systems*, wyd. 2 | L5.7: histereza i regulacja dwupołożeniowa jako wzorzec pojęciowy dla $x_{on}$ i $x_{off}$ | 1.1, 4.5 | U | Z | fragment: regulacja dwupołożeniowa i histereza (do potwierdzenia) |

## C. Duże modele językowe: rozdz. 2.1–2.2

| Klucz | Pozycja | Twierdzenie, które podpiera | Podrozdział | Prio | St. | Co przeczytać |
|---|---|---|---|---|---|---|
| `guo2025deepseekr1` | Guo i in. (DeepSeek-AI) 2025, Nature | L2.5: DeepSeek-R1 uzyskał rozumowanie przez RL; badany model to destylat | 2.2 | R | Z | całość, s. 633–638 (6 s.) |
| `vaswani2017attention` | Vaswani i in. 2017, NeurIPS | L2.1: architektura Transformer; model wyznacza rozkład następnego tokenu | 2.1 | U | K | fragment: wstęp i opis architektury (do potwierdzenia) |
| `brown2020language` | Brown i in. 2020, NeurIPS | L2.2 (pierwsza część): uczenie w kontekście, sterowanie modelem przez prompt | 2.1, 3.1 | U | K | fragment: wstęp i opis podejścia (do potwierdzenia) |
| `ouyang2022training` | Ouyang i in. 2022, NeurIPS | L2.2 (druga część): dostrajanie do instrukcji sprawia, że model wykonuje polecenia | 2.1, 3.1 | U | K | fragment: wstęp i opis metody (do potwierdzenia) |
| `wei2022chain` | Wei i in. 2022, NeurIPS | L2.4: łańcuch rozumowania przed odpowiedzią | 2.2 | U | K | fragment: wstęp i definicja łańcucha rozumowania (do potwierdzenia) |
| `qwen2024qwen25` | Qwen Team 2024, arXiv (v2); preprint | L2.5 (część): model bazowy destylatu `deepseek-r1:14b` to Qwen2.5-14B | 2.2, 4.1 | U | Z | fragment: opis rodziny modeli i wariantu 14B (do potwierdzenia) |
| `li2024evaluating` | Li S. i in. 2024, ICML (PMLR 235) | L6.3: kwantyzacja zmienia wyniki modelu; badany model jest kwantyzowany | 4.1, 6.3 | U | Z | fragment: streszczenie, wnioski i wyniki dla kwantyzacji wag (do potwierdzenia); artykuł ma s. 28480–28524 |

## D. Agenci oparci na LLM, LLM a motywacja: rozdz. 2.3–2.4, 3.4

| Klucz | Pozycja | Twierdzenie, które podpiera | Podrozdział | Prio | St. | Co przeczytać |
|---|---|---|---|---|---|---|
| `keeling2024can` | Keeling i in. 2024, arXiv (v1); preprint | L3.3, L3.6: w grze punkty kontra zadany ból część modeli przełącza się po przekroczeniu progu intensywności; najbliższy precedens pomiaru progu | 3.4, 4.2, 6.2 | R | Z | całość (liczba stron do uzupełnienia) |
| `bianco2026beyond` | Bianco, Shiller 2026, arXiv (v1); preprint | L3.3, L3.4: replikacja wyniku Keelinga; wybory zależą od formatu bodźca (liczby a etykiety) | 3.4 | R | Z | całość (liczba stron do uzupełnienia) |
| `wang2024survey` | Wang L. i in. 2024, Frontiers of Computer Science | L2.7: architektura agenta LLM (profil, pamięć, planowanie, działanie) | 1.1, 2.3 | U | Z | całość (artykuł nr 186345; liczba stron do uzupełnienia); najważniejsza część o budowie agenta (do potwierdzenia) |
| `wang2023humanoid` | Wang Z., Chiu, Chiu 2023, EMNLP Demo | L3.1, L3.6: agenci LLM z jawnie zadanymi potrzebami podstawowymi | 2.4 | U | Z | całość, s. 167–176 (10 s.) |
| `wang2025simulating` | Wang Y. i in. 2025, ICLR | L3.1, L3.6: agent LLM kierowany pragnieniami zamiast zadań | 2.4 | U | Z | całość (liczba stron do uzupełnienia) |
| `masumori2025survival` | Masumori, Ikegami 2025, arXiv (v1); preprint | L3.2, L3.6: zachowania „przetrwania” agentów LLM w symulacji z ograniczonymi zasobami | 2.4, 3.4, 4.5, 6.2 | U | Z | całość (liczba stron do uzupełnienia) |
| `tagliabue2025probing` | Tagliabue, Dung 2025, arXiv (v2); preprint | L3.5: deklaracje modelu o preferencjach nie muszą zgadzać się z wyborami | 3.4 | U | Z | całość (liczba stron do uzupełnienia) |
| `cedro2026cash` | Cedro i in. 2026, *Communications of the ACM* | L3.4: wybory LLM w kompromisach zależą od sformułowania promptu; czy to decyzje tego rodzaju co w pracy: do potwierdzenia przy lekturze | 3.4, 6.2 | U | Z | całość, s. 58–66 (9 s.) |

## E. Wrażliwość na prompt, ramowanie: rozdz. 3

| Klucz | Pozycja | Twierdzenie, które podpiera | Podrozdział | Prio | St. | Co przeczytać |
|---|---|---|---|---|---|---|
| `sclar2024quantifying` | Sclar i in. 2024, ICLR | L4.2: drobne zmiany formatu promptu wyraźnie zmieniają wyniki LLM | 3.2, 4.6, 6.2 | R | Z | całość (liczba stron do uzupełnienia) |
| `tversky1981framing` | Tversky, Kahneman 1981, Science | L4.5: u ludzi sposób przedstawienia tej samej decyzji zmienia wybór (efekt ramowania); podstawa H3 | 3.3 | R | K | całość, s. 453–458 (6 s.) |
| `shanahan2023role` | Shanahan, McDonell, Reynolds 2023, *Nature* | L4.7, L6.4: model odgrywa rolę zadaną w prompcie; „ból” agenta jako odgrywana rola | 3.1, 3.3, 6.3 | R | Z | całość, s. 493–498 (6 s.) |
| `sharma2024towards` | Sharma i in. 2024, ICLR | L4.8: model ulega sugestiom z promptu; konkurencyjne wyjaśnienie przesunięć progu (PB2, PB5); czy pojęcie sykofancji to obejmuje: do potwierdzenia przy lekturze | 3.3, 6.2 | U | ? | całość (liczba stron do uzupełnienia) |
| `schulhoff2024prompt` | Schulhoff i in. 2024, arXiv (v6); preprint | L4.1: nazwy elementów promptu (rola, cel, opis stanu, lista akcji, format) | 3.1 | U | Z | fragment: słownik terminów i część o składnikach promptu (do potwierdzenia) |
| `pezeshkpour2024large` | Pezeshkpour, Hruschka 2024, Findings NAACL | L4.3: kolejność opcji wpływa na wybory, więc kolejność listy akcji trzeba kontrolować | 3.2, 4.6 | U | Z | całość, s. 2006–2017 (12 s.) |
| `mizrahi2024state` | Mizrahi i in. 2024, TACL | L4.4: parafrazy tej samej instrukcji dają różne wyniki | 3.2, 4.6, 6.2 | U | Z | całość, s. 933–949 (17 s.) |
| `li2023large` | Li C. i in. 2023, arXiv (v7); preprint | L4.6 (część): bodźce emocjonalne w prompcie zmieniają wyniki LLM | 3.3 | U | Z | całość (32 strony według pola Comments na arXiv, odczyt 12.11.2026) |
| `jones2022capturing` | Jones, Steinhardt 2022, NeurIPS | L4.6: LLM reagują na ramowanie (replikacja efektu ramowania); tło H3 | 3.3 | U | Z | całość, s. 11785–11799 (15 s.) |

## F. Metodologia pomiaru: rozdz. 4

| Klucz | Pozycja | Twierdzenie, które podpiera | Podrozdział | Prio | St. | Co przeczytać |
|---|---|---|---|---|---|---|
| `binz2023using` | Binz, Schulz 2023, PNAS | L5.1: LLM można badać metodami eksperymentu psychologicznego, jak uczestnika badania | 3.4, 4.2 | R | Z | całość (artykuł e2218523120; liczba stron do uzupełnienia) |
| `wichmann2001psychometric` | Wichmann, Hill 2001 (I), Perception & Psychophysics | L5.3: funkcja psychometryczna z progiem, nachyleniem, poziomem zgadywania i lapsów; estymacja i ocena dopasowania | 4.3 | R | Z | całość, s. 1293–1313 (21 s.) |
| `wichmann2001bootstrap` | Wichmann, Hill 2001 (II), Perception & Psychophysics | L5.4: przedziały ufności progu i nachylenia metodą bootstrap | 4.3 | R | Z | całość, s. 1314–1329 (16 s.) |
| `prins2018applying` | Prins, Kingdom 2018, *Frontiers in Psychology* | L5.5: progi z dwóch warunków porównuje się jako modele, testem ilorazu wiarygodności (D14) | 4.3, 4.6 | R | Z | całość (artykuł nr 1250; liczba stron do uzupełnienia) |
| `atil2025nondeterminism` | Atıl i in. 2025, Eval4NLP 2025 (ACL) | L6.1, L6.2, L2.3: LLM bywa niedeterministyczny nawet przy ustawieniach „deterministycznych”; wniosków nie opiera się na pojedynczym przebiegu | 2.1, 4.4, 4.6, 6.3 | R | Z | całość, s. 135–148 (14 s.) |
| `kingdom2016psychophysics` | Kingdom, Prins 2016, *Psychophysics*, wyd. 2 | L5.3, L5.5: podręcznikowe wprowadzenie do funkcji psychometrycznych, metod adaptacyjnych i porównywania warunków | 4.3 | U | K | fragmenty: funkcje psychometryczne, metody adaptacyjne, porównywanie modeli (do potwierdzenia) |
| `dominguezolmedo2024questioning` | Dominguez-Olmedo, Hardt, Mendler-Dünner 2024, NeurIPS | L5.2: odpowiedzi LLM na pytania zadawane wprost są obciążone skrzywieniami kolejności i etykiet | 4.2, 6.3 | U | Z | fragment: streszczenie i część o skrzywieniach kolejności i etykiet (do potwierdzenia); artykuł ma s. 45850–45878 |
| `holm1979simple` | Holm 1979, *Scandinavian Journal of Statistics* | L5.6: korekta Holma przy wielu porównaniach z wariantem bazowym (D14) | 4.3, 4.6 | U | Z | całość, s. 65–70 (6 s.) |
| `song2025good` | Song i in. 2025, NAACL | L6.2: ewaluacja LLM musi uwzględniać próbkowanie; potrzeba wielu prób i podanej niepewności | 4.4, 4.6, 6.3 | U | Z | całość, s. 4195–4206 (12 s.) |
| `agresti2013categorical` | Agresti 2013, *Categorical Data Analysis*, wyd. 3, Wiley | L5.8: przedział Wilsona, regresja logistyczna jako kontrola, regresja logistyczna dla odpowiedzi w trzech kategoriach (siatka 2D) | 4.3 | U | Z | trzy fragmenty według spisu treści (odczyt 12.11.2026): 1.4 od s. 13, rozdz. 5 od s. 163, 8.1 od s. 293; czy 1.4 nazywa przedział Wilsona: do potwierdzenia |
| `kleijnen2015design` | Kleijnen 2015, *Design and Analysis of Simulation Experiments*, wyd. 2, Springer | L5.8: wspólne liczby losowe (wspólne ziarna dla wariantów promptu) | 4.5 | U | Z | podrozdział 3.5 w rozdz. 3 (s. 83–133), numer według streszczenia rozdziału (odczyt 12.11.2026); czy mówi o porównaniach parami: do potwierdzenia |

## G. Źródła techniczne i formalne (nie liczą się do 30–50 „artykułów”)

| Klucz | Pozycja | Twierdzenie, które podpiera | Podrozdział | Prio | St. | Co przeczytać |
|---|---|---|---|---|---|---|
| `zawislak2025budowa` | Zawiślak 2025, praca magisterska, PRz | L3.7: praca referencyjna pokazała reakcje agenta ogrodowego jakościowo, bez liczbowego progu i na jednym przebiegu | 2.5, 4.1, 4.5, 6.1 | R | Z | całość; czytana jako pierwsza |
| `ollama2026api` | Dokumentacja API Ollama | L2.6, L2.3 (część): parametry próbkowania (`temperature`, `top_p`, `seed`), `think` | 4.1, 4.4 | U | Z | opis obiektu `options` i parametru `think` |
| `deepseek2025distillcard` | Karta modelu DeepSeek-R1-Distill-Qwen-14B | L2.6: zalecenia producenta dla destylatów (temperatura, brak promptu systemowego, wiele prób) | 2.2, 4.4 | U | Z | sekcja z zaleceniami użycia; sprawdzić zalecaną temperaturę (0,6 w docs/02 i docs/04, 0,5–0,7 w poprzedniej wersji tego pliku) |
| `opi2023jsa` | OPI, opis modułu analizy SI w JSA | — (tylko do `09`, nie do pracy) | — | — | Z | — |
| `wmifs2025wymagania` | WMiFS, wymagania dotyczące pracy | — (tylko do `10`, nie do pracy) | — | — | Z | — |

## H. Antropomorfizacja, świadomość i dobrostan AI: rozdz. 6.3

| Klucz | Pozycja | Twierdzenie, które podpiera | Podrozdział | Prio | St. | Co przeczytać |
|---|---|---|---|---|---|---|
| `butlin2026identifying` | Butlin i in. 2026, *Trends in Cognitive Sciences* | L6.5: ocena świadomości i dobrostanu AI to osobny problem z własnymi metodami, którego praca nie rozstrzyga | 6.3 | U | Z | całość, s. 488–501 (14 s.) |

## Pozycje z pracy referencyjnej: jak z nich korzystać

Bibliografia Zawiślak (78 pozycji) zawiera duplikaty i opisy niepełne. Nie przenosimy jej hurtem.
- **Duplikaty:**
  - *Attention Is All You Need*: [28], [46], [70],
  - Sutton i Barto: [55], [67], [74],
  - Brown i in.: [32], [45], [64], [71].
- **Opisy bez miejsca wydania**, podane jako „[miejsce wydania: Ohio University]”: [1], [8]–[13], [17]–[19], [22]–[24]. Część to prawdopodobnie prezentacje lub raporty Starzyka. Zamiast nich używamy zweryfikowanych publikacji z sekcji A.
- **Pozycje niepotwierdzone** (nie cytujemy bez sprawdzenia):
  - [2] Starzyk, Príncipe 2017, „Motivated learning for adaptive intelligent systems”, IEEE TNNLS 28(3),
  - [72] Lake, Murphy 2023, „Emergent behaviors in large language models”, JAIR,
  - [39] zbiorcze „źródła dotyczące teorii bólu”.
- **Źródła nienaukowe** (wideo, blogi, Wikipedia): [35], [44], [65], [66], [77]. W tej pracy ich nie używamy.

## Do znalezienia lub decyzji

- [ ] Praca Kingi (lub jej konspekt), jeśli promotor udostępni. Cytujemy dopiero wersję obronioną albo za zgodą.
- [ ] Czy Starzyk lub zespół PRz/WSIiZ opublikowali coś o agentach motywowanych z LLM (2023–2026)? Sprawdzić stronę J. Starzyka, WSIiZ i dorobek promotora.
- [ ] Polskojęzyczne źródło o uczeniu motywowanym lub motywacji w AI (opcjonalnie; np. Galus, Starzyk, *Świadomość? Ależ to bardzo proste!*, 2018).
- [x] Wersje recenzowane siedmiu preprintów z wyboru: sprawdzone 12.11.2026, brak dla wszystkich.
- [ ] Powtórzyć sprawdzenie wersji recenzowanych preprintów raz, na miesiąc przed oddaniem pracy.
- [ ] Uzupełnić pole ze statusem `?` w wyborze: `sharma2024towards` (pełna lista autorów i dane z OpenReview; OpenReview blokuje automat, pozycja jest w pakiecie do zewnętrznej weryfikacji).
- [ ] Zewnętrzna weryfikacja metadanych: `raporty/pakiet_perplexity.md` (pozycje nowe, K, ? i preprinty; 19 pozycji).
- [ ] `agresti2013categorical`: przy lekturze 1.4 potwierdzić, że pada tam nazwa „przedział Wilsona”. Jeśli nie albo jeśli wydanie będzie niedostępne, wraca Agresti 2019 (sekcja „Rezerwowe i usunięte”).
- [ ] Uzupełnić liczbę stron pozycji rdzenia bez pola `pages`: `keramati2014homeostatic`, `binz2023using`, `prins2018applying`, `keeling2024can`, `bianco2026beyond`, `sclar2024quantifying`.

**Luki nazwane po imieniu** (stan na 13.11.2026)

| Twierdzenie | Stan |
|---|---|
| L3.6 (luka badawcza) | z natury bez pojedynczego źródła; opiera się na pozycjach z L3.1–L3.3 |
| L2.3 (definicja temperatury i top_p) | bez źródła naukowego; cytujemy `ollama2026api`, a losowość odpowiedzi podpiera `atil2025nondeterminism` |
| L4.8 (warunkowa) | jedyne źródło to `sharma2024towards`; jeśli lektura pokaże, że pojęcie nie obejmuje tego przypadku, PB2 i PB5 zostają bez tła |
| L7.1 (warunkowa) | jedyne źródło to `bonabeau1996quantitative`; jeśli nie podaje parametru stromości, wraca `ulrich2021response` |

## Rezerwowe i usunięte

Pozycje rezerwowe zostają w `literatura.bib`, ale nie są w kolejce lektury. Wracają do wyboru decyzją autora; warunek powrotu jest w ostatniej kolumnie tam, gdzie go ustalono. Z1–Z12 to kandydaci do skrócenia planu z `raporty/literatura_selekcja_cz1.md`.

### Rezerwowe (31)

| Klucz | Pozycja | Powód | Wraca, gdy |
|---|---|---|---|
| `starzyk2008motivation` | Starzyk 2008, rozdział w *Frontiers in Robotics, Automation and Control* | Wcześniejsze ujęcie pojęcia, które podpiera `starzyk2017needs`; rozdział nie jest recenzowany. | — |
| `starzyk2011motivated` | Starzyk 2011, rozdział w *Computational Modeling and Simulation of Intellect* | Przegląd powielający `starzyk2017needs`. | potrzebne będzie wprowadzenie do uczenia motywowanego |
| `starzyk2013simulation` | Starzyk, Graham, Puzio 2013, AIAI | Pochodzenie środowiska ogrodowego dokumentuje praca referencyjna. | Zawiślak wskazuje ją jako wzorzec środowiska |
| `starzyk2017mlecog` | Starzyk, Graham 2017, IEEE Systems Journal | Definicje powielają `starzyk2017needs`, a architektura MLECOG to Z2. | — |
| `ryan2000self` | Ryan, Deci 2000, American Psychologist | Przypisana wyłącznie do Z1 (teoria autodeterminacji). | — |
| `singh2010intrinsically` | Singh, Lewis, Barto, Sorg 2010, IEEE TAMD | Powiela rolę `oudeyer2007intrinsic`. | — |
| `man2019homeostasis` | Man, Damasio 2019, Nature Machine Intelligence | L1.8 podpiera `sharkey2025could`, reszta to Z3. | — |
| `kuehn2017artificial` | Kuehn, Haddadin 2017, IEEE RA-L | Przykład robotyczny do Z3. | — |
| `asada2019artificial` | Asada 2019, *Philosophies* | Przypisana wyłącznie do Z3. | — |
| `theraulaz1998response` | Theraulaz, Bonabeau, Deneubourg 1998, *Proc. R. Soc. B* | Przypisana wyłącznie do Z12 (progi zmienne z doświadczeniem). | — |
| `ulrich2021response` | Ulrich i in. 2021, *PLOS Biology* | W L7.1 powiela `bonabeau1996quantitative`, a krytyka progów to Z12. | `bonabeau1996quantitative` nie podaje parametru stromości |
| `yoshida2025linking` | Yoshida, Sprekeler, Gutkin 2025, *Current Opinion in Behavioral Sciences* | Przegląd powielający `keramati2014homeostatic`. | — |
| `yao2023react` | Yao i in. 2023, ICLR | Przykład wzorca agenta; L2.7 podpiera `wang2024survey`. | — |
| `shinn2023reflexion` | Shinn i in. 2023, NeurIPS | Przypisana wyłącznie do Z4. | — |
| `park2023generative` | Park i in. 2023, UIST | Przypisana wyłącznie do Z4; w 2.4 i 4.5 nie podpiera żadnego twierdzenia z mapy. | — |
| `sumers2024cognitive` | Sumers, Yao, Narasimhan, Griffiths 2024, TMLR | Drugie ramy pojęciowe dla L2.7; powiela rolę `wang2024survey`. | — |
| `du2023guiding` | Du i in. 2023, ICML | Przypisana wyłącznie do Z5 (LLM jako źródło motywacji dla agentów RL). | — |
| `klissarov2024motif` | Klissarov i in. 2024, ICLR | Przypisana wyłącznie do Z5. | — |
| `tagliabue2026pain` | Tagliabue, Dung, Berg 2026, arXiv (v2); preprint | Przypisana wyłącznie do Z7 („oś bólu” w reprezentacjach). | — |
| `ren2026ai` | Ren i in. 2026, manuskrypt | Przypisana wyłącznie do Z8; manuskrypt bez recenzji. | — |
| `berg2026language` | Berg, Kaiser 2026, arXiv; preprint | Przypisana wyłącznie do Z8. | — |
| `schlatter2026incomplete` | Schlatter, Weinstein-Raun, Ladish 2026, arXiv (v2); preprint | Dodatkowy przykład do L3.4, które podpierają `bianco2026beyond` i `cedro2026cash`. | — |
| `mikaelson2025beyond` | Mikaelson, Shiller, Clatterbuck 2025, arXiv; preprint | Dodatkowy przykład do L3.3, które podpierają `keeling2024can` i `bianco2026beyond`. | — |
| `webson2022prompt` | Webson, Pavlick 2022, NAACL | Przypisana wyłącznie do Z6. | — |
| `salinas2024butterfly` | Salinas, Morstatter 2024, Findings ACL | Powiela rolę `sclar2024quantifying`. | docs/01 ma dalej cytować obie pozycje |
| `zheng2024helpful` | Zheng i in. 2024, Findings EMNLP | Dotyczy części L4.7 o personie (waga T); rolę zadaną w prompcie podpiera `shanahan2023role`. | — |
| `hagendorff2023machine` | Hagendorff i in. 2024 (v6), arXiv; preprint | Powiela rolę `binz2023using`. | — |
| `renze2024effect` | Renze 2024, Findings EMNLP | Dotyczy trafności zadań, a nie losowości decyzji; L2.3 podpiera `atil2025nondeterminism`. | — |
| `miller2024adding` | Miller 2024, arXiv; preprint | Powiela recenzowaną `song2025good`. | podeprze porównania parami przy wspólnych ziarnach |
| `schutt2016painfree` | Schütt i in. 2016, *Vision Research* | W L5.3 powiela `wichmann2001psychometric`, a estymacji bayesowskiej docs/04 nie stosuje. | dane pokażą nadrozproszenie |
| `long2024taking` | Long i in. 2024, arXiv; preprint | Przypisana wyłącznie do Z11 (dobrostan AI jako temat). | — |

### Do usunięcia, wykonanie odłożone (2)

Decyzja autora z 12.11.2026, doprecyzowana 13.11.2026: wpisy zostają w `literatura.bib` do przeglądu planu po lekturze rdzenia, bo są cytowane w docs/02 i w thesis/.

| Klucz | Pozycja | Powód |
|---|---|---|
| `liu2024agentbench` | Liu X. i in. 2024, ICLR | Nie podpiera żadnego twierdzenia z mapy: metryki z 4.5 są definicjami własnymi (docs/04). |
| `kuss2005bayesian` | Kuss, Jäkel, Wichmann 2005, *Journal of Vision* | Alternatywa bayesowska, której docs/04 nie stosuje; nie podpiera żadnego twierdzenia z mapy. |

### Rezerwa spoza `literatura.bib` (2)

Pozycje sprawdzone w części 2, bez wpisu w `.bib`. Wpis powstaje dopiero po decyzji o powrocie.

| Pozycja | Powód | Wraca, gdy |
|---|---|---|
| Agresti A., *An Introduction to Categorical Data Analysis*, wyd. 3, Wiley, 2019 | Krótszy podręcznik tego samego autora, drugi do tych samych metod; ISBN i liczba stron niepotwierdzone u wydawcy. | 1.4 w `agresti2013categorical` nie nazywa przedziału Wilsona albo wydanie z 2013 r. jest niedostępne |
| Law A. M., *Simulation Modeling and Analysis*, wyd. 6, McGraw Hill, 2024 | Spisu treści 6. wydania nie udało się potwierdzić u wydawcy, więc nie wiadomo, gdzie są wspólne liczby losowe. | podrozdział 3.5 w `kleijnen2015design` nie wystarczy do opisu wspólnych ziaren |
