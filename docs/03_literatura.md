# Literatura

Dane bibliograficzne są w `literatura.bib`. Ten plik mówi, **do czego** każda pozycja służy.

- **Liczba pozycji:** 50 naukowych i 5 technicznych lub formalnych.
- **Priorytet:**
  - R (rdzeń, 33 pozycje): na pewno cytujemy,
  - U (uzupełniająca, 17 pozycji): cytujemy, jeśli podrozdział tego potrzebuje; kandydatki do usunięcia przy skracaniu.
- **Status** (sprawdzone 27.09.2026):
  - **Z:** istnienie i dane sprawdzone online (strona wydawcy, DOI, ACL Anthology, PMLR, arXiv albo strona autora),
  - **K:** pozycja klasyczna, dane standardowe, nie sprawdzano ich w tej sesji; przy pierwszym cytowaniu warto potwierdzić strony i DOI,
  - **?:** pozycja potwierdzona, ale konkretne pole wymaga sprawdzenia (opis w polu `weryfikacja` w `.bib`).
- **Zasada:** zanim coś zacytujemy, czytamy odpowiedni fragment źródła. Opisy poniżej to streszczenia robocze, nie podstawa do cytowania.

## Kryterium dostępności (D12)

| Kat. | Warunek | Zapis w bibliografii |
|---|---|---|
| A | pełny tekst bezpłatny u wydawcy (OpenAlex: diamond, gold, hybrid, bronze) | DOI |
| B | wydawca pobiera opłatę, legalna kopia w repozytorium (arXiv, PMC, repozytorium uczelni, strona autora) | DOI + odnośnik do kopii; zaznaczamy, jeśli to preprint |
| C | brak legalnej bezpłatnej kopii | zamiennik A/B albo wyjątek z uzasadnieniem |

- Kopie z serwisów pirackich (np. Sci-Hub) nie są kopią legalną.
- Cytat dosłowny i numer strony podajemy według wersji, do której prowadzi odnośnik.
- Dostępność typu bronze może zniknąć; przed oddaniem pracy sprawdzamy ją ponownie.
- W `literatura.bib`: pole `dostep = {A|B|C}`, dla B pole `url` z adresem kopii i `urldate`.

### Wyjątki

| Klucz | Powód | Jak czytelnik może sprawdzić |
|---|---|---|
| `zawislak2025budowa` | praca dyplomowa, brak publicznego egzemplarza (do potwierdzenia) | `\dower{ustalić z promotorem lub dziekanatem}` |

## A. Motywacja, potrzeby, ból (teoria): rozdz. 1

| Klucz | Pozycja | Do czego | Rozdz. | Prio | St. |
|---|---|---|---|---|---|
| `starzyk2017needs` | Starzyk, Graham, Puzio 2017, *Needs, Pains, and Motivations in Autonomous Agents*, IEEE TNNLS | **Najważniejsza pozycja teoretyczna.** Ból prymitywny jako miara odległości od zaspokojenia potrzeby, próg bólu („agent działa, gdy ból przekracza próg”), bóle abstrakcyjne, wybór celu przez WTA | 1.4, 4.2, 6.1 | R | Z |
| `starzyk2017mlecog` | Starzyk, Graham 2017, *MLECOG*, IEEE Systems Journal | Architektura kognitywna agenta motywowanego; definicje potrzeby, bólu prymitywnego i progu | 1.4 | R | Z |
| `starzyk2012motivated` | Starzyk, Graham, Raif, Tan 2012, Cognitive Systems Research | Uczenie motywowane vs RL; tworzenie celów abstrakcyjnych | 1.4 | R | Z |
| `graham2015opportunistic` | Graham, Starzyk, Jachyra 2015, IEEE TNNLS | Zachowania oportunistyczne agenta motywowanego (działanie przy okazji, poniżej progu) | 1.4 | U | ? |
| `starzyk2013simulation` | Starzyk, Graham, Puzio 2013, AIAI, IFIP AICT 412 | Symulacja agenta motywowanego w środowisku z zasobami; wzorzec dla środowiska ogrodowego | 1.4, 4.1 | U | Z |
| `starzyk2008motivation` | Starzyk 2008, rozdział w *Frontiers in Robotics, Automation and Control* | Pierwotne ujęcie motywacji i bólu w „inteligencji ucieleśnionej” | 1.4 | U | Z |
| `starzyk2011motivated` | Starzyk 2011, rozdział w *Computational Modeling and Simulation of Intellect* | Przegląd uczenia motywowanego dla inteligencji obliczeniowej | 1.4 | U | Z |
| `maslow1943theory` | Maslow 1943, Psychological Review | Hierarchia potrzeb; tło psychologiczne dla rywalizacji bólów | 1.2 | R | K |
| `ryan2000self` | Ryan, Deci 2000, American Psychologist | Motywacja wewnętrzna i zewnętrzna (teoria autodeterminacji) | 1.2 | U | Z |
| `keramati2014homeostatic` | Keramati, Gutkin 2014, eLife | Homeostatyczne RL: nagroda jako redukcja odchylenia stanu wewnętrznego od wartości zadanej; formalny odpowiednik „bólu” | 1.2, 1.3 | R | Z |
| `oudeyer2007intrinsic` | Oudeyer, Kaplan 2007, Frontiers in Neurorobotics | Typologia obliczeniowych podejść do motywacji wewnętrznej | 1.3 | R | Z |
| `singh2010intrinsically` | Singh, Lewis, Barto, Sorg 2010, IEEE TAMD | Motywacja wewnętrzna w RL z perspektywy ewolucyjnej | 1.3 | U | Z |
| `schmidhuber2010formal` | Schmidhuber 2010, IEEE TAMD | Ciekawość i motywacja wewnętrzna jako postęp w kompresji/predykcji | 1.3 | U | Z |
| `man2019homeostasis` | Man, Damasio 2019, Nature Machine Intelligence | Homeostaza i „odczucia” w projektowaniu maszyn; argument za bólem jako sygnałem regulacyjnym | 1.5 | U | ? |
| `kuehn2017artificial` | Kuehn, Haddadin 2017, IEEE RA-L | Sztuczny „układ nerwowy” robota: klasy bólu i odruchy; przykład bólu funkcjonalnego z progami | 1.5 | U | ? |

## B. Agenci i uczenie ze wzmocnieniem: rozdz. 1.1

| Klucz | Pozycja | Do czego | Rozdz. | Prio | St. |
|---|---|---|---|---|---|
| `russell2020artificial` | Russell, Norvig 2020, *AI: A Modern Approach*, wyd. 4 | Definicja agenta i środowiska | 1.1 | R | K |
| `sutton2018reinforcement` | Sutton, Barto 2018, *Reinforcement Learning*, wyd. 2 | Stan, akcja, nagroda, polityka; kontrast z uczeniem motywowanym | 1.1, 1.3 | R | K |

## C. Duże modele językowe: rozdz. 2.1–2.2

| Klucz | Pozycja | Do czego | Rozdz. | Prio | St. |
|---|---|---|---|---|---|
| `vaswani2017attention` | Vaswani i in. 2017, NeurIPS | Architektura Transformer | 2.1 | R | K |
| `brown2020language` | Brown i in. 2020, NeurIPS | Uczenie w kontekście, prompt jako sposób sterowania modelem | 2.1, 3.1 | R | K |
| `ouyang2022training` | Ouyang i in. 2022, NeurIPS | Dostrajanie do instrukcji (RLHF); dlaczego model „słucha” promptu | 2.1 | R | K |
| `wei2022chain` | Wei i in. 2022, NeurIPS | Łańcuch rozumowania | 2.2 | R | K |
| `guo2025deepseekr1` | Guo i in. (DeepSeek-AI) 2025, Nature | DeepSeek-R1: rozumowanie uzyskane przez RL; destylaty | 2.2 | R | Z |
| `qwen2024qwen25` | Qwen Team 2024, arXiv | Model bazowy destylatu `deepseek-r1:14b` (Qwen2.5-14B) | 2.2, 4.1 | U | Z |

## D. Agenci oparci na LLM, LLM a motywacja: rozdz. 2.3–2.4, 3.4

| Klucz | Pozycja | Do czego | Rozdz. | Prio | St. |
|---|---|---|---|---|---|
| `wang2024survey` | Wang L. i in. 2024, Frontiers of Computer Science | Przegląd architektur agentów LLM (profil, pamięć, planowanie, działanie) | 2.3 | R | Z |
| `sumers2024cognitive` | Sumers, Yao, Narasimhan, Griffiths 2024, TMLR | CoALA: ramy pojęciowe agenta językowego, odwołania do architektur kognitywnych (most do MLECOG) | 2.3 | R | Z |
| `yao2023react` | Yao i in. 2023, ICLR | ReAct: przeplatanie rozumowania i działania | 2.3 | R | K |
| `shinn2023reflexion` | Shinn i in. 2023, NeurIPS | Reflexion: werbalne „wzmocnienie” agenta | 2.3 | U | K |
| `park2023generative` | Park i in. 2023, UIST | Generatywni agenci: pamięć, refleksja, planowanie w symulacji | 2.3, 2.4 | R | K |
| `wang2023humanoid` | Wang Z., Chiu, Chiu 2023, EMNLP Demo | Agenci LLM z potrzebami podstawowymi (głód, energia, zdrowie), emocjami i relacjami; najbliższa analogia „bólu prymitywnego” u agenta LLM | 2.4 | R | Z |
| `wang2025simulating` | Wang Y. i in. 2025, ICLR | D2A: agent LLM kierowany wielowymiarowymi pragnieniami (inspiracja teorią potrzeb) zamiast zadań | 2.4 | R | Z |
| `masumori2025survival` | Masumori, Ikegami 2025, arXiv | Agenci LLM w symulacji typu Sugarscape: zachowania „przetrwania”, porzucanie zadań w obliczu śmiertelnego zagrożenia, agresja przy niedoborze | 2.4, 6.2 | R | Z |
| `du2023guiding` | Du i in. 2023, ICML | ELLM: LLM proponuje cele na podstawie opisu stanu; LLM jako źródło motywacji wewnętrznej | 2.4 | U | Z |
| `klissarov2024motif` | Klissarov i in. 2024, ICLR | Motif: nagroda wewnętrzna z preferencji LLM | 2.4 | U | Z |
| `keeling2024can` | Keeling i in. 2024, arXiv | **Kluczowa pozycja empiryczna.** Gra punkty vs zadany ból/przyjemność: u części modeli przełączenie po przekroczeniu progu intensywności, u innych stałe unikanie bólu albo reakcja stopniowana. Bezpośredni precedens pomiaru progu | 3.4, 6.2 | R | Z |

## E. Wrażliwość na prompt, ramowanie: rozdz. 3

| Klucz | Pozycja | Do czego | Rozdz. | Prio | St. |
|---|---|---|---|---|---|
| `sclar2024quantifying` | Sclar i in. 2024, ICLR | Drobne zmiany formatu promptu zmieniają wyniki nawet o kilkadziesiąt punktów procentowych; argument za kontrolą formatu | 3.2, 6.2 | R | Z |
| `salinas2024butterfly` | Salinas, Morstatter 2024, Findings ACL | Minimalne perturbacje (np. spacja, format odpowiedzi) zmieniają etykiety nadawane przez LLM | 3.2 | R | Z |
| `mizrahi2024state` | Mizrahi i in. 2024, TACL | Ocena na wielu parafrazach instrukcji zamiast jednego promptu; uzasadnienie parafraz jako czynnika kontrolnego | 3.2, 4.6 | R | Z |
| `pezeshkpour2024large` | Pezeshkpour, Hruschka 2024, Findings NAACL | Wrażliwość na kolejność opcji; uzasadnienie permutacji listy akcji | 3.2, 4.6 | R | Z |
| `webson2022prompt` | Webson, Pavlick 2022, NAACL | Czy modele „rozumieją” treść promptu: wpływ instrukcji mylących i nieistotnych | 3.2 | U | Z |
| `li2023large` | Li i in. 2023, arXiv | EmotionPrompt: bodźce emocjonalne w prompcie zmieniają wyniki; tło dla ramowania „bólem” | 3.3 | R | Z |
| `zheng2024helpful` | Zheng i in. 2024, Findings EMNLP | Persona w prompcie systemowym nie poprawia systematycznie wyników; tło dla czynnika „rola agenta” | 3.3 | U | Z |
| `tversky1981framing` | Tversky, Kahneman 1981, Science | Efekt ramowania decyzji u ludzi; hipoteza H3 | 3.3 | R | K |

## F. Metodologia pomiaru: rozdz. 4

| Klucz | Pozycja | Do czego | Rozdz. | Prio | St. |
|---|---|---|---|---|---|
| `binz2023using` | Binz, Schulz 2023, PNAS | LLM jako uczestnik eksperymentów psychologicznych; uzasadnienie podejścia behawioralnego | 3.4, 4.2 | R | Z |
| `hagendorff2023machine` | Hagendorff i in. 2023, arXiv | „Psychologia maszyn”: dobre praktyki badań behawioralnych LLM | 4.2 | U | Z |
| `wichmann2001psychometric` | Wichmann, Hill 2001 (I), Perception & Psychophysics | Dopasowanie funkcji psychometrycznej, parametr lapsów, dobroć dopasowania | 4.3 | R | Z |
| `wichmann2001bootstrap` | Wichmann, Hill 2001 (II), Perception & Psychophysics | Przedziały ufności progu i nachylenia metodą bootstrap | 4.3 | R | Z |
| `kingdom2016psychophysics` | Kingdom, Prins 2016, *Psychophysics*, wyd. 2 | Podręcznik: progi, funkcje psychometryczne, porównywanie warunków | 4.3 | R | K |
| `miller2024adding` | Miller 2024, arXiv | Przedziały ufności i porównania par w ewaluacji LLM | 4.3, 4.6 | R | Z |
| `renze2024effect` | Renze 2024, Findings EMNLP | Wpływ temperatury (0–1) na trafność rozwiązywania zadań | 2.1, 4.4 | U | Z |
| `atil2025nondeterminism` | Atıl i in. 2025, Eval4NLP 2025 (ACL) | Niedeterminizm LLM nawet przy ustawieniach „deterministycznych”; argument przeciw pojedynczemu przebiegowi | 4.4, 4.6 | R | Z |

## G. Źródła techniczne i formalne (nie liczą się do 30–50 „artykułów”)

| Klucz | Pozycja | Do czego |
|---|---|---|
| `zawislak2025budowa` | Zawiślak 2025, praca magisterska, PRz | Praca referencyjna: środowisko, prompty, wyniki jakościowe |
| `ollama2026api` | Dokumentacja API Ollama | Parametry `options` (temperature, seed), `think`, pole `thinking` |
| `deepseek2025distillcard` | Karta modelu DeepSeek-R1-Distill-Qwen-14B | Zalecenia: temperatura 0,5–0,7, bez promptu systemowego, wiele prób |
| `opi2023jsa` | OPI, opis modułu analizy SI w JSA | Tylko do `09`, nie do pracy |
| `wmifs2025wymagania` | WMiFS, wymagania dotyczące pracy | Tylko do `10`, nie do pracy |

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
- [ ] Sprawdzić wersje recenzowane preprintów: `keeling2024can`, `masumori2025survival`, `li2023large`.
- [ ] Uzupełnić pola ze statusem `?` (sekcja A).
