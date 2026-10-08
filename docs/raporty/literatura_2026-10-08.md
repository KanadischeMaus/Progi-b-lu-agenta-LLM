> Raport roboczy wygenerowany przez AI (Claude), 2026-10-08. Nie jest źródłem do cytowania. Część propozycji autor odrzucił. Decyzje: docs/12 i historia commitów. Klucze w raporcie mogą być nieaktualne; obowiązuje literatura.bib.

# Lista literatury do pracy „Wpływ promptu na progi bólu agenta LLM”: wersja scalona i zweryfikowana (stan na 8.10.2026)

## TL;DR
- Bibliografia rośnie z 55 do 83 pozycji: 55 istniejących kluczy (zmienia się tylko atil2024 → atil2025), 11 pozycji przyjętych wcześniej przez autora i 17 nowych. Każdy podrozdział teoretyczny i metodyczny ma teraz co najmniej 3 źródła, w tym przynajmniej jedno recenzowane. Wcześniej puste 4.5 i 6.3 mają odpowiednio 5 i 9 pozycji.
- Najważniejsza luka, 3.4 (kompromis cel–„ból”), rośnie z 2 do 9 pozycji. Jedyną recenzowaną jest tu Binz i Schulz (PNAS). Keeling i in. (2024), Masumori i Ikegami (2025) oraz oba artykuły Tagliabue nadal są tylko preprintami arXiv. Numer arXiv 2609.16247 istnieje: aktualna wersja v2 z 25.09.2026 nosi tytuł „The Pain Axis: LLMs Represent Self-Directed Harm and Act on It”, a v1 miała tytuł „…Act to Relieve It”.
- Dostępność wg D12: 58 pozycji A, 7 B, 7 C (głównie podręczniki i klasyka, wyjątki uzasadnione niżej), 11 nieustalonych (theraulaz1998response ma bezpłatny pełny tekst w PMC, PMC1688885). Wśród nieustalonych jest 6 kluczowych prac Starzyka, dla których trzeba zdobyć legalne kopie autorskie. To jedyna poważna przeszkoda formalna przed dalszą pracą.

## 1. Podsumowanie

**Liczby.** Przed zmianami było 55 pozycji, po zmianach jest 83: 55 istniejących, 11 przyjętych przez autora (holm1979simple, li2024evaluating, butlin2026identifying, schutt2016painfree, kuss2005bayesian, song2025good, shanahan2023role, sharma2024towards, tagliabue2025probing, tagliabue2026pain, long2024taking) i 17 nowych. Liczba mieści się w założonym przedziale 70–90. Dwie pozycje WWW (opi2023jsa, wmifs2025wymagania) nie trafiają do pracy, więc w bibliografii pracy będzie 81 pozycji.

**Skład 83 pozycji:**
- artykuły w czasopismach: 32;
- materiały konferencji recenzowanych: 25;
- książki i rozdziały: 6;
- preprinty arXiv: 14;
- WWW i manuskrypty: 5;
- praca dyplomowa: 1.

**Dostęp:**
- A: 58, w tym 14 preprintów arXiv, gdzie miejscem publikacji jest otwarty serwer, oraz theraulaz1998response (pełny tekst w PMC, PMC1688885);
- B: 7;
- C: 7;
- nieustalone: 11.

**Ważne zastrzeżenie dotyczące weryfikacji.** W tej sesji sprawdziłem online u źródła wszystkie nowe pozycje oraz pozycje: keeling2024can, masumori2025survival, hagendorff2023machine, butlin2026identifying, tagliabue2025probing, tagliabue2026pain, long2024taking, atil2025nondeterminism, li2024evaluating, holm1979simple, kuehn2017artificial, man2019homeostasis i sutton2018reinforcement. Pozostałe pozycje oznaczone wcześniej jako K mają nadal status K. Wynika to z budżetu wyszukiwań, a nie z wykrytych błędów. Ich lista jest w sekcji 6. Nie dopisywałem do nich DOI ani stron „z pamięci”.

**Tabela pokrycia** (przed = według pola „rozdzial” w obecnym pliku; „recenz.” = czasopismo lub konferencja recenzowana)

| Podrozdział | Przed | Po | W tym recenz. | Ocena |
|---|---|---|---|---|
| 1.1 Agent, środowisko | 2 | 4 | 1 | wystarczające (podręczniki) |
| 1.2 Motywacja w psychologii | 3 | 3 | 3 | wystarczające |
| 1.3 Motywacja wewnętrzna w ML | 4 | 6 | 6 | wystarczające |
| 1.4 Uczenie motywowane Starzyka | 7 | 7 | 5 | wystarczające (problem dostępu) |
| 1.5 Sztuczny ból w robotyce | 2 | 4 | 4 | wystarczające |
| 2.1 Model językowy, próbkowanie | 4 | 4 | 4 | wystarczające |
| 2.2 Modele rozumujące | 4 | 4 | 2 | wystarczające |
| 2.3 Agent oparty na LLM | 5 | 5 | 5 | wystarczające |
| 2.4 LLM a motywacja | 6 | 6 | 5 | wystarczające |
| 2.5 Praca referencyjna | 1 | 1 | 0 | wystarczające (z natury) |
| 3.1 Elementy promptu | 2 | 5 | 4 | wystarczające |
| 3.2 Wrażliwość na format | 5 | 5 | 5 | wystarczające |
| 3.3 Ramowanie, persona | 3 | 6 | 5 | wystarczające |
| 3.4 Kompromisy cel–„ból” | 2 | 9 | 1 | do wzmocnienia (recenzowanych prawie brak w literaturze) |
| 4.1 Środowisko, kwantyzacja | 4 | 5 | 2 | wystarczające |
| 4.2 LLM jako badany | 3 | 5 | 3 | wystarczające |
| 4.3 Funkcja psychometryczna | 4 | 7 | 6 | wystarczające |
| 4.4 Protokół sondowania | 4 | 5 | 3 | wystarczające |
| 4.5 Pętla zamknięta, metryki | 0 | 5 | 3 | wystarczające (brak prac stricte o histerezie agentów LLM) |
| 4.6 Plan eksperymentów | 4 | 7 | 6 | wystarczające |
| 6.1 Progi a uczenie motywowane | 2 | 7 | 6 | wystarczające (brak źródła na teorię popędu Hulla) |
| 6.2 Wyniki a literatura promptu | 3 | 6 | 3 | wystarczające |
| 6.3 Ograniczenia | 0 | 9 | 7 | wystarczające |

## 2. Pełna lista robocza

Legenda kolumn:
- **St.** – status: Z = zweryfikowane, K = do kontroli, ? = niepewne.
- **Dost.** – kategoria dostępu.
- **Zm.** – rodzaj zmiany: bz = istniejąca bez zmian, pop = istniejąca poprawiona, now = nowa, przyj = przyjęta przez autora.
- **Priorytet:** W = wysoki, Ś = średni, N = niski.

### A. Motywacja, potrzeby, ból (rozdz. 1)

| Klucz | Opis | Rola | Pr. | St. / źródło | Dost. + adres | Zm. |
|---|---|---|---|---|---|---|
| starzyk2008motivation | J. A. Starzyk, „Motivation in Embodied Intelligence”, w: *Frontiers in Robotics, Automation and Control*, I-Tech, 2008 | 1.4: pierwotne sformułowanie potrzeb i bólu | W | Z (wcześniej) | A(K): rozdział książki I-Tech/InTech w otwartym dostępie – potwierdzić adres | bz |
| starzyk2011motivated | J. A. Starzyk, „Motivated Learning for Computational Intelligence”, IGI Global, 2011 | 1.4: ból abstrakcyjny, hierarchia celów | Ś | Z | ? – prawdopodobnie C | bz |
| starzyk2012motivated | J. A. Starzyk i in., *Cognitive Systems Research*, 2012 | 1.4: ML a RL | W | Z | ? | bz |
| starzyk2013simulation | J. A. Starzyk i in., AIAI 2013 | 1.4, 4.1: symulacja agenta | Ś | Z | ? | bz |
| graham2015opportunistic | J. Graham, J. A. Starzyk, D. Jachyra, „Opportunistic Behavior in Motivated Learning Agents”, *IEEE TNNLS* 26(8):1735–1746, 2015, DOI 10.1109/TNNLS.2014.2354400 | 1.4: zachowania oportunistyczne (PB6) | W | Z (poprawka potwierdzona przez autora) | ? | pop (autorzy, tom, strony, DOI) |
| starzyk2017mlecog | J. A. Starzyk i in., „MLECOG…”, *IEEE Systems Journal*, 2017 | 1.4: architektura | Ś | K | ? | bz |
| starzyk2017needs | J. A. Starzyk i in., „Needs, Pains, and Motivations in Autonomous Agents”, *IEEE TNNLS* 28(11):2528–2540, 2017 | 1.4, 4.2, 6.1: definicja bólu i progu, punkt odniesienia operacjonalizacji | W | Z | ? | bz |
| maslow1943theory | A. H. Maslow, „A Theory of Human Motivation”, *Psychological Review* 50(4), 1943 | 1.2: hierarchia potrzeb | Ś | K | B(K): kopia w York Univ. „Classics in the History of Psychology” – potwierdzić | bz |
| ryan2000self | R. M. Ryan, E. L. Deci, *American Psychologist*, 2000 | 1.2: teoria autodeterminacji | Ś | K | B(K): strona selfdeterminationtheory.org – potwierdzić | bz |
| keramati2014homeostatic | M. Keramati, B. Gutkin, *eLife*, 2014 | 1.2, 1.3, 4.5, 6.1: popęd jako odległość od punktu nastawy; formalny pomost między homeostazą a progiem | W | K | A (eLife) | pop (dodane 4.5, 6.1) |
| oudeyer2007intrinsic | P.-Y. Oudeyer, F. Kaplan, *Frontiers in Neurorobotics*, 2007 | 1.3: typologia | W | K | A (Frontiers) | bz |
| singh2010intrinsically | S. Singh i in., *IEEE TAMD*, 2010 | 1.3: IMRL | Ś | K | ? | bz |
| schmidhuber2010formal | J. Schmidhuber, *IEEE TAMD*, 2010 | 1.3: ciekawość i kompresja | N | K | B(K): strona autora (IDSIA) | bz |
| man2019homeostasis | K. Man, A. Damasio, „Homeostasis and soft robotics in the design of feeling machines”, *Nature Machine Intelligence* 1(10):446–452, 2019, DOI 10.1038/s42256-019-0103-7 | 1.5: homeostaza jako podstawa „czujących maszyn”, kontrast dla bólu funkcjonalnego | W | Z (nature.com, 2026-10) | C: brak PMC/arXiv; link SharedIt niepotwierdzony – patrz sekcja 5 | pop (DOI, numer 10) |
| kuehn2017artificial | J. Kuehn, S. Haddadin, „An Artificial Robot Nervous System To Teach Robots How To Feel Pain And Reflexively React To Potentially Damaging Contacts”, *IEEE RA-L* 2(1):72–79, 2017, DOI 10.1109/LRA.2016.2536360 | 1.5: nocycepcja i odruch w robocie | W | Z (DOI, tom i strony zgodne w kilku źródłach; wydanie online 2016, numer 2017) | C: brak legalnej kopii – sekcja 5 | pop (status ? → Z) |
| sharkey2025could | A. Sharkey, „Could a robot feel pain?”, *AI & Society* 40(5):3641–3651, 2025, DOI 10.1007/s00146-024-02110-y | 1.5, 6.3: nocycepcja ≠ ból; przegląd robotów „z bólem”; argument przeciw tezie o odczuwaniu – uzasadnia czysto funkcjonalne rozumienie bólu | W | Z (Springer, White Rose, 2026-10) | A: open access CC BY, link.springer.com/article/10.1007/s00146-024-02110-y | now |
| asada2019artificial | M. Asada, „Artificial Pain May Induce Empathy, Morality, and Ethics in the Conscious Mind of Robots”, *Philosophies* 4(3):38, 2019, DOI 10.3390/philosophies4030038 | 1.5: projekt sztucznego nocyceptora i rola bólu w architekturze robota (stanowisko przeciwne do Sharkey) | Ś | Z (MDPI, 2026-10) | A (CC BY) | now |

### B. Agenci i uczenie ze wzmocnieniem

| Klucz | Opis | Rola | Pr. | St. | Dost. | Zm. |
|---|---|---|---|---|---|---|
| russell2020artificial | S. Russell, P. Norvig, *AI: A Modern Approach*, 4th ed., Pearson, 2020 | 1.1: definicja agenta | Ś | K | C – wyjątek (podręcznik klasyczny); zamiennik bezpłatny: sutton2018reinforcement, rozdz. 3 | bz |
| sutton2018reinforcement | R. S. Sutton, A. G. Barto, *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018 | 1.1: agent, środowisko, stan, akcja, polityka | W | Z (adres z kilku źródeł, errata autora potwierdza drugi druk 2020) | B: http://incompleteideas.net/book/RLbook2020.pdf (drugi druk 2020, treść zgodna z wydaniem 2018 + errata) | pop (url, dostęp) |
| astrom2021feedback | K. J. Åström, R. M. Murray, *Feedback Systems: An Introduction for Scientists and Engineers*, 2nd ed., Princeton University Press, 2021 (wyd. 2.02.2021, 528 s., ISBN 978-0691193984, e-ISBN 9780691213477) | 1.1, 4.5: pętla sprzężenia zwrotnego; regulator dwupołożeniowy z histerezą („output depends on the value of past inputs”) – wzorzec pojęciowy histerezy i oscylacji w PB7 | W | Z (data wydania i ISBN wg portalu badawczego Lund University i Google Books; PDF autorski z 24.07.2020) | B: fbswiki.org (wiki autorów, pełny PDF 2. wyd.) | now |

### C. Duże modele językowe

| Klucz | Opis | Rola | Pr. | St. | Dost. | Zm. |
|---|---|---|---|---|---|---|
| vaswani2017attention | A. Vaswani i in., NeurIPS 30, 2017 | 2.1 | Ś | K (strony do odczytu z proceedings.neurips.cc) | A | bz |
| brown2020language | T. B. Brown i in., NeurIPS 33, 2020 | 2.1, 3.1: prompt jako interfejs | Ś | K | A | bz |
| ouyang2022training | L. Ouyang i in., NeurIPS 35, 2022 | 2.1, 3.1: dostrajanie do instrukcji | Ś | K | A | bz |
| wei2022chain | J. Wei i in., NeurIPS 35, 2022 | 2.2: CoT | Ś | K | A | bz |
| guo2025deepseekr1 | D. Guo i in., *Nature*, 2025 | 2.2: R1, destylacja | W | Z | A(K): open access w *Nature* – potwierdzić | bz |
| qwen2024qwen25 | Qwen Team, arXiv 2412.15115, 2024 | 2.2, 4.1 | Ś | Z (wersji recenzowanej nie szukano – sekcja 6) | A (arXiv) | bz |
| deepseek2025distillcard | DeepSeek-AI, karta modelu, 2025 | 2.2, 4.4: zalecenia producenta (temperatura) | W | Z | A (WWW) | bz |
| renze2024effect | M. Renze, Findings of EMNLP 2024 | 2.1, 4.4 | Ś | Z | A (ACL Anthology) | bz |
| li2024evaluating | S. Li, X. Ning, L. Wang, T. Liu, X. Shi, S. Yan, G. Dai, H. Yang, Y. Wang, „Evaluating Quantized Large Language Models”, ICML 2024, PMLR 235:28480–28524 | 4.1, 6.3: wpływ kwantyzacji na zdolności i zachowanie; uzasadnienie ograniczenia Q4_K_M | W | Z (wynik PMLR i ACM DL; klucz PMLR li24bb, nie li24bf) | A: proceedings.mlr.press/v235/li24bb.html | przyj |

### D. Agenci oparci na LLM, LLM a motywacja

| Klucz | Opis | Rola | Pr. | St. | Dost. | Zm. |
|---|---|---|---|---|---|---|
| yao2023react | S. Yao i in., ICLR 2023 | 2.3 | Ś | K | A (OpenReview) | bz |
| shinn2023reflexion | N. Shinn i in., NeurIPS 36, 2023 | 2.3 | N | K (wersja NeurIPS bez E. Bermana; strony do odczytu) | A | pop (autorzy) |
| park2023generative | J. S. Park i in., UIST 2023 | 2.3, 2.4, 4.5: długie symulacje i ocena zachowania agentów | W | K | B: arXiv 2304.03442 (preprint, treść zbliżona) | pop (dodane 4.5) |
| wang2024survey | L. Wang i in., *Frontiers of Computer Science*, 2024 | 1.1, 2.3: definicja i architektura agenta LLM | W | K | B: arXiv 2308.11432 (wersja preprint) | pop (dodane 1.1) |
| sumers2024cognitive | T. R. Sumers i in., TMLR, 2024 | 2.3: CoALA | Ś | K | A (OpenReview/TMLR) | bz |
| wang2023humanoid | Z. Wang i in., EMNLP 2023 Demos, s. 167–176 | 2.4: potrzeby podstawowe agenta | Ś | Z | A (ACL Anthology) | bz |
| wang2025simulating | Y. Wang i in., ICLR 2025 | 2.4: pragnienia jako źródło autonomii | W | Z | A (OpenReview) | bz |
| masumori2025survival | A. Masumori, T. Ikegami, „Do Large Language Model Agents Exhibit a Survival Instinct? An Empirical Study in a Sugarscape-Style Simulation”, arXiv 2508.12920, 2025 | 2.4, 3.4, 4.5, 6.2: zachowania przetrwania przy energii ginącej przy zerze; najbliższy odpowiednik pętli zamkniętej | W | Z (arXiv, DBLP CoRR, strona laboratorium; stan X.2026: **tylko preprint**) | A (arXiv) | pop (dodane 3.4, 4.5; adnotacja „preprint”) |
| du2023guiding | Y. Du i in., ICML 2023 | 1.3, 2.4 | N | K | A (PMLR) | pop (dodane 1.3) |
| klissarov2024motif | M. Klissarov i in., ICLR 2024 | 1.3, 2.4 | N | K | A (OpenReview) | pop (dodane 1.3) |
| zawislak2025budowa | K. Zawiślak, praca magisterska, PRz WMiFS, Rzeszów 2025 | 2.5, 4.1, 4.5, 6.1 | W | Z (rok 2025 – NIE zmieniać) | C – wyjątek (praca referencyjna; dostęp przez bibliotekę lub APD PRz) | pop (dodane 4.5) |
| liu2024agentbench | X. Liu, H. Yu, H. Zhang, Y. Xu, X. Lei, H. Lai, Y. Gu, H. Ding, K. Men, K. Yang, S. Zhang, X. Deng, A. Zeng, Z. Du, C. Zhang, S. Shen, T. Zhang, Y. Su, H. Sun + 3 autorów, „AgentBench: Evaluating LLMs as Agents”, ICLR 2024 | 4.5: wieloturowa ewaluacja agentów LLM w środowiskach interaktywnych; rejestruje wynik zadania i sposób zakończenia przebiegu (wzorzec metryk epizodycznych, akcji niepoprawnych i bezczynności) | W | K (19 autorów potwierdzonych; 3 ostatnich do odczytu z OpenReview) | A: arXiv 2308.03688 / OpenReview | now |

### E. Wrażliwość na prompt, ramowanie, „ból” w LLM

| Klucz | Opis | Rola | Pr. | St. | Dost. | Zm. |
|---|---|---|---|---|---|---|
| schulhoff2024prompt | S. Schulhoff, M. Ilie, N. Balepur, K. Kahadze, A. Liu, C. Si, Y. Li, A. Gupta, H. Han, S. Schulhoff, P. S. Dulepet, S. Vidyadhara, D. Ki, S. Agrawal, C. M. Pham, G. C. Kroiz, F. Li, H. Tao, A. Srivastava, H. Da Costa, S. Gupta, M. L. Rogers, I. Goncearenco, G. Sarli, I. Galynker, D. Peskoff, M. Carpuat, J. White, S. Anadkat, A. M. Hoyle, P. Resnik, „The Prompt Report: A Systematic Survey of Prompt Engineering Techniques”, arXiv 2406.06608v6 | 3.1: słownik 33 terminów i taksonomia 58 technik tekstowych; nazewnictwo elementów promptu (rola, kontekst, format) | W | Z (arXiv, Semantic Scholar; 31 autorów); tytuł v1: „…of Prompting Techniques”; data v6 i ewentualna wersja recenzowana – „?” | A (arXiv) | now |
| webson2022prompt | A. Webson, E. Pavlick, NAACL 2022 | 3.2 | Ś | K | A | bz |
| sclar2024quantifying | M. Sclar i in., ICLR 2024 | 3.2, 4.6, 6.2 | W | K | A | pop (dodane 4.6) |
| salinas2024butterfly | A. Salinas, F. Morstatter, Findings of ACL 2024 | 3.2 | Ś | K | A | bz |
| mizrahi2024state | M. Mizrahi i in., TACL, 2024 | 3.2, 4.6, 6.2 | W | K | A | pop (dodane 6.2) |
| pezeshkpour2024large | P. Pezeshkpour, E. Hruschka, Findings of NAACL 2024 | 3.2, 4.6 | Ś | K | A | bz |
| li2023large | C. Li i in., arXiv 2307.11760, 2023 | 3.3: bodźce emocjonalne | Ś | Z (wersji recenzowanej nie sprawdzono – sekcja 6) | A (arXiv) | bz |
| zheng2024helpful | M. Zheng i in., Findings of EMNLP 2024 | 3.1, 3.3: rola/persona w prompcie systemowym | W | K | A | pop (dodane 3.1) |
| tversky1981framing | A. Tversky, D. Kahneman, *Science*, 1981 | 3.3: efekt ramowania | W | K | ? (prawdopodobnie C – wyjątek dla klasyki) | bz |
| shanahan2023role | M. Shanahan, K. McDonell, L. Reynolds, „Role Play with Large Language Models”, *Nature* 623(7987):493–498, 2023, DOI 10.1038/s41586-023-06647-8 | 3.1, 3.3, 6.3: LLM odgrywa rolę zadaną w prompcie; „ból” agenta jako odgrywanie, a nie stan | W | Z (dane autora) | A(K): open access – potwierdzić | przyj |
| sharma2024towards | M. Sharma i in., „Towards Understanding Sycophancy in Language Models”, ICLR 2024 | 3.3, 6.2: uleganie sugestiom; interpretacja PB2 i PB5 | W | Z (dane autora); pełna lista autorów do odczytu z OpenReview | A | przyj |
| jones2022capturing | E. Jones, J. Steinhardt, „Capturing Failures of Large Language Models via Human Cognitive Biases”, NeurIPS 2022, arXiv 2202.12299 | 3.3: replikacja Tversky–Kahneman 1981 na GPT-3 (wybór opcji ryzykownej: 45% vs 28% u ludzi w ramie „ratowania”, 74% vs 78% w ramie „śmierci”) | Ś | Z (autorzy Erik Jones i Jacob Steinhardt; poster NeurIPS 2022, neurips.cc/virtual/2022/poster/53539; arXiv 2202.12299v2 z 24.11.2022 z adnotacją „Published at NeurIPS 2022”) | A (arXiv) | now |
| keeling2024can | G. Keeling, W. Street, M. Stachaczyk, D. Zakharova, I. M. Comşa, A. Sakovych, I. Logothetis, Z. Zhang, B. Agüera y Arcas, J. Birch, „Can LLMs make trade-offs involving stipulated pain and pleasure states?”, arXiv 2411.02432, 2024 | 3.4, 4.2, 6.2: **najbliższa praca pokrewna**: punkty vs zadany ból; przełączenie większości odpowiedzi po progu intensywności; skale jakościowe i liczbowe (odpowiednik PB4) | W | Z (arXiv; w pracach z IX 2026 nadal cytowana jako preprint; **tylko preprint**) | A (arXiv) | pop (pełna lista autorów, dodane 4.2) |
| binz2023using | M. Binz, E. Schulz, *PNAS*, 2023 | 3.4, 4.2 | W | Z | A(K) | bz |
| tagliabue2025probing | V. Tagliabue, L. Dung, „Probing the Preferences of a Language Model: Integrating Verbal and Behavioral Tests of AI Welfare”, arXiv 2509.07961v2 (23.05.2026) | 3.4: deklarowane preferencje a kosztowne wybory w środowisku wirtualnym | W | Z (arXiv; **tylko preprint**) | A (arXiv) | przyj |
| tagliabue2026pain | V. Tagliabue, L. Dung, C. Berg, „The Pain Axis: LLMs Represent Self-Directed Harm and Act on It”, arXiv 2609.16247v2 (25.09.2026) | 3.4, 6.2: liniowy „kierunek bólu” w 25 modelach otwartych (2B–72B); sterowane modele Qwen 2.5 wybierają szkodliwe przyciski w 50–94% prób vs 0–5% bez sterowania | W | Z (arXiv abs, 2026-10; numer istnieje; tytuł v1: „…Act to Relieve It”; **tylko preprint**) | A (arXiv) | przyj (tytuł wg v2) |
| bianco2026beyond | F. Bianco, D. Shiller, „Beyond Behavioural Trade-Offs: Mechanistic Tracing of Pain-Pleasure Decisions in an LLM”, arXiv 2602.19159v1 (22.02.2026) | 3.4: replikacja paradygmatu Keelinga (gemma-2-9b-it, 50 prób na poziom, T = 1,0) z analizą mechanistyczną; odpowiedzi zależne od formatu intensywności (liczby vs etykiety) – bezpośrednio dotyczy PB4 | W | Z (arXiv; **preprint**) | A (arXiv) | now |
| ren2026ai | R. Ren, K. Li, M. Mazeika i in. (Center for AI Safety; ost. D. Hendrycks), „AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs”, manuskrypt, 2026 | 3.4, 6.3: funkcjonalny „dobrostan” mierzony zbieżnie (użyteczność, samoopis, zachowanie, kończenie rozmów) | Ś | ? (lista autorów niespójna między README repozytorium a cytowaniami – 20 vs 21 nazwisk; brak arXiv) | A: www.ai-wellbeing.org/paper.pdf (manuskrypt) | now |
| berg2026language | C. Berg, C. Kaiser, „Language Models Act on Hidden Valence”, arXiv 2609.35591v1 (28.09.2026) | 3.4: preferencje ujawnione; model usuwa narzucony stan negatywny zależnie od dawki; zależność wyboru od walencji pojawia się podczas DPO – argument, że „unikanie bólu” jest wytworem dostrajania | Ś | Z (arXiv HTML, 2026-10; **preprint**) | A (arXiv, CC BY) | now |
| schlatter2026incomplete | J. Schlatter, B. Weinstein-Raun, J. Ladish, „Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs”, arXiv 2509.14260v2 (26.01.2026) | 3.4, 6.2: zachowania samozachowawcze silnie zależne od promptu; instrukcja w prompcie systemowym działała słabiej niż w prompcie użytkownika; ramowanie „samozachowawcze” zwiększało opór | Ś | Z (arXiv; tytuł v1: „Shutdown Resistance in Large Language Models”; **preprint**) | A (arXiv) | now |

### F. Metodologia pomiaru

| Klucz | Opis | Rola | Pr. | St. | Dost. | Zm. |
|---|---|---|---|---|---|---|
| hagendorff2023machine | T. Hagendorff, I. Dasgupta, M. Binz, S. C. Y. Chan, A. Lampinen, J. X. Wang, Z. Akata, E. Schulz, „Machine Psychology”, arXiv 2303.13988v6, 2024 | 4.2, 6.3: LLM jako uczestnik eksperymentu; standardy projektowania promptów | W | Z (arXiv; brak wersji recenzowanej – *Nature Reviews Psychology* 2025 cytuje ją jako preprint) | A (arXiv) | pop (8 autorów, wersja v6, rok 2024) |
| dominguezolmedo2024questioning | R. Dominguez-Olmedo, M. Hardt, C. Mendler-Dünner, „Questioning the Survey Responses of Large Language Models”, NeurIPS 37, 2024, s. 45850–45878, DOI 10.52202/079017-1458 | 4.2, 6.3: odpowiedzi 43 modeli zdominowane przez skrzywienia kolejności i etykiet („A”); po randomizacji dążą do rozkładu jednostajnego | W | Z (NeurIPS, proceedings.com, arXiv) | A: papers.nips.cc / arXiv 2306.07951 | now |
| kocielnik2026rethinking | R. Kocielnik + 7 autorów, „Rethinking Psychometric Evaluation of LLMs: When and Why Self-Reports Predict Behavior”, arXiv 2606.12730v1, ICML 2026 Workshop CTB | 6.3: rozbieżność samoopisu i zachowania; persona stabilizuje samoopis, ale nie zachowanie – uzasadnia pomiar behawioralny zamiast pytania „czy czujesz ból” | N | ? (pełna lista autorów nieustalona) | A (arXiv) | now |
| wichmann2001psychometric | F. A. Wichmann, N. J. Hill, *Perception & Psychophysics*, 2001 | 4.3 | W | K | ? (kopia autorska do sprawdzenia) | bz |
| wichmann2001bootstrap | F. A. Wichmann, N. J. Hill, *P&P* 63(8):1314–1329, 2001 | 4.3: bootstrap PU | W | Z | ? | bz |
| kingdom2016psychophysics | F. A. A. Kingdom, N. Prins, *Psychophysics*, 2nd ed., Academic Press, 2016 | 4.3 | Ś | K | C – zamiennik: prins2018applying (A) | bz |
| prins2018applying | N. Prins, F. A. A. Kingdom, „Applying the Model-Comparison Approach to Test Specific Research Hypotheses in Psychophysical Research Using the Palamedes Toolbox”, *Frontiers in Psychology* 9:1250, 2018, DOI 10.3389/fpsyg.2018.01250 | 4.3, 4.6: test różnicy progów jako porównanie modeli (współdzielone vs osobne θ) metodą ilorazu wiarygodności – alternatywa lub uzupełnienie bootstrapu | W | Z (Frontiers, PMC6064978) | A | now |
| schutt2016painfree | H. H. Schütt, S. Harmeling, J. H. Macke, F. A. Wichmann, *Vision Research* 122:105–123, 2016, DOI 10.1016/j.visres.2016.02.002 | 4.3: nadrozproszenie (20 decyzji na poziom), psignifit 4 | W | Z (dane autora) | A(K) | przyj |
| kuss2005bayesian | M. Kuss, F. Jäkel, F. A. Wichmann, *Journal of Vision* 5(5):478–492, 2005, DOI 10.1167/5.5.8 | 4.3: alternatywa bayesowska | Ś | Z (dane autora) | A(K) (JOV) | przyj |
| miller2024adding | E. Miller, arXiv 2411.00640, 2024 | 4.3, 4.6 | W | Z (wersji recenzowanej nie sprawdzono) | A | bz |
| atil2025nondeterminism | B. Atıl, S. Aykent, A. Chittams, L. Fu, R. J. Passonneau, E. Radcliffe, G. R. Rajagopal, A. Sloan, T. Tudrej, F. Ture, Z. Wu, L. Xu, B. Baldwin, „Non-Determinism of »Deterministic« LLM System Settings in Hosted Environments”, Eval4NLP 2025, ACL, s. 135–148, DOI 10.18653/v1/2025.eval4nlp-1.12 | 4.4, 4.6, 6.3 | W | Z (ACL Anthology) | A | pop (klucz atil2024 → atil2025, 13 autorów, strony) |
| song2025good | Y. Song, G. Wang, S. Li, B. Y. Lin, NAACL 2025, s. 4195–4206, DOI 10.18653/v1/2025.naacl-long.211 | 4.4, 4.6, 6.3 | W | Z (dane autora) | A | przyj |
| holm1979simple | S. Holm, „A Simple Sequentially Rejective Multiple Test Procedure”, *Scandinavian Journal of Statistics* 6(2):65–70, 1979; JSTOR 4615733 | 4.6: korekta Holma | W | Z (tom, numer, strony, JSTOR); DOI 10.2307/4615733 – „?” (cytowany w CRAN i Academia, rozwiązywalność niesprawdzona) | C: JSTOR (bezpłatny odczyt po rejestracji – sekcja 5) | przyj |

### G. Źródła techniczne, formalne i modele progowe (6.1)

| Klucz | Opis | Rola | Pr. | St. | Dost. | Zm. |
|---|---|---|---|---|---|---|
| ollama2026api | Ollama, dokumentacja API | 4.1, 4.4 | W | Z | A (WWW) | bz |
| opi2023jsa | OPI PIB, 2023 | nie do pracy | – | Z | A | bz |
| wmifs2025wymagania | WMiFS PRz, 2025 | nie do pracy | – | Z | A | bz |
| bonabeau1996quantitative | E. Bonabeau, G. Theraulaz, J.-L. Deneubourg, „Quantitative study of the fixed threshold model for the regulation of division of labour in insect societies”, *Proc. R. Soc. Lond. B* 263(1376):1565–1569, 1996, DOI 10.1098/rspb.1996.0229 | 6.1: model progu stałego – sigmoidalna funkcja odpowiedzi s^n/(s^n+θ^n), bezpośredni odpowiednik funkcji psychometrycznej | W | Z (strona wydawcy Royal Society: DOI, numer, opublikowano online 22.11.1996) | ? (archiwum Royal Society – sprawdzić) | now |
| bonabeau1998fixed | E. Bonabeau, G. Theraulaz, J.-L. Deneubourg, „Fixed response thresholds and the regulation of division of labor in insect societies”, *Bulletin of Mathematical Biology* 60:753–807, 1998, DOI 10.1006/bulm.1998.0041 | 6.1: pełna analiza modelu progów odpowiedzi | Ś | Z (Springer) | C: zamiennik ulrich2021response (A) | now |
| theraulaz1998response | G. Theraulaz, E. Bonabeau, J.-L. Deneubourg, „Response threshold reinforcement and division of labour in insect societies”, *Proc. R. Soc. Lond. B* 265(1393):327–332, 1998, DOI 10.1098/rspb.1998.0299 | 6.1: progi zmienne (uczenie progu) – analogia do kalibracji progu promptem (PB2) | Ś | Z (rekord PubMed Central; 22.02.1998) | A: pełny tekst w PMC, PMC1688885 | now |
| ulrich2021response | Y. Ulrich, M. Kawakatsu, C. K. Tokita, J. Saragosti, V. Chandra, C. E. Tarnita, D. J. C. Kronauer, „Response thresholds alone cannot explain empirical patterns of division of labor in social insects”, *PLOS Biology* 19(6):e3001269, 2021, DOI 10.1371/journal.pbio.3001269 | 6.1: probabilistyczna funkcja progowa z parametrem stromości η (η → ∞: funkcja schodkowa) – odpowiednik k; krytyka „same progi nie wystarczą” | W | Z (rekordy PubMed i PLOS; opublikowano 17.06.2021) | A (PLOS, CC BY) | now |

### H. Antropomorfizacja, świadomość i dobrostan AI (6.3)

| Klucz | Opis | Rola | Pr. | St. | Dost. | Zm. |
|---|---|---|---|---|---|---|
| butlin2026identifying | P. Butlin, R. Long, T. Bayne, Y. Bengio, J. Birch, D. Chalmers, A. Constant, G. Deane, E. Elmoznino, S. M. Fleming, X. Ji, R. Kanai, C. Klein, G. Lindsay, M. Michel, L. Mudrik, M. A. K. Peters, E. Schwitzgebel, J. Simon, R. VanRullen, „Identifying indicators of consciousness in AI systems”, *Trends in Cognitive Sciences* 30(6):488–501, 2026, DOI 10.1016/j.tics.2025.10.011 | 6.3: wskaźniki świadomości wynikają z architektury, nie z zachowania – progi behawioralne nie są dowodem odczuwania | W | Z (CRIS TAU/IUCC, LSE; online 2025, numer VI 2026) | A: © The Authors; kopia researchonline.lse.ac.uk/id/eprint/130322 | przyj |
| long2024taking | R. Long, J. Sebo, P. Butlin, K. Finlinson, K. Fish, J. Harding, J. Pfau, T. Sims, J. Birch, D. Chalmers, „Taking AI Welfare Seriously”, arXiv 2411.00986v1, 2024 | 6.3 | Ś | Z (arXiv) | A | przyj |

## 3. Plik literatura.bib

Zasada: pola, których nie sprawdzałem ponownie, są „bez zmian z obecnego pliku”. Oznacza to komentarz `% [bez zmian]` i należy w tym miejscu zachować z obecnego pliku pola journal, volume, pages i doi. Nie wpisuję DOI ani stron, których nie potwierdziłem.

```bibtex
% ===== A. Motywacja, potrzeby, ból =====
@incollection{starzyk2008motivation, author={Starzyk, Janusz A.}, title={Motivation in Embodied Intelligence}, booktitle={Frontiers in Robotics, Automation and Control}, publisher={I-Tech}, year={2008}, % [bez zmian]
  status={Z}, rozdzial={1.4}, weryfikacja={dane z obecnego pliku; dostep do potwierdzenia (InTech OA) 2026-10}, dostep={A}}
@incollection{starzyk2011motivated, author={Starzyk, Janusz A.}, title={Motivated Learning for Computational Intelligence}, booktitle={Computational Modeling and Simulation of Intellect}, publisher={IGI Global}, year={2011}, % [bez zmian]
  status={Z}, rozdzial={1.4}, weryfikacja={dane z obecnego pliku; dostep nieustalony 2026-10}, dostep={?}}
@article{starzyk2012motivated, author={Starzyk, Janusz A. and others}, title={Motivated Learning for the Development of Autonomous Systems}, journal={Cognitive Systems Research}, year={2012}, % [bez zmian: pelna lista autorow, tom, strony, doi]
  status={Z}, rozdzial={1.4}, weryfikacja={dane z obecnego pliku; dostep nieustalony 2026-10}, dostep={?}}
@inproceedings{starzyk2013simulation, author={Starzyk, Janusz A. and others}, title={Simulation of a Motivated Learning Agent}, booktitle={AIAI 2013}, year={2013}, % [bez zmian]
  status={Z}, rozdzial={1.4, 4.1}, weryfikacja={dane z obecnego pliku 2026-10}, dostep={?}}
@article{graham2015opportunistic, author={Graham, James and Starzyk, Janusz A. and Jachyra, Daniel}, title={Opportunistic Behavior in Motivated Learning Agents}, journal={IEEE Transactions on Neural Networks and Learning Systems}, volume={26}, number={8}, pages={1735--1746}, year={2015}, doi={10.1109/TNNLS.2014.2354400},
  status={Z}, rozdzial={1.4, 6.1}, weryfikacja={poprawka potwierdzona przez autora (IEEE); dostep nieustalony 2026-10}, dostep={?}}
@article{starzyk2017mlecog, author={Starzyk, Janusz A. and others}, title={MLECOG: Motivated Learning Embodied Cognitive Architecture}, journal={IEEE Systems Journal}, year={2017}, % [bez zmian]
  status={K}, rozdzial={1.4}, weryfikacja={nie sprawdzono ponownie w 2026-10}, dostep={?}}
@article{starzyk2017needs, author={Starzyk, Janusz A. and others}, title={Needs, Pains, and Motivations in Autonomous Agents}, journal={IEEE Transactions on Neural Networks and Learning Systems}, volume={28}, number={11}, pages={2528--2540}, year={2017}, % [bez zmian: doi, pelni autorzy]
  status={Z}, rozdzial={1.4, 4.2, 6.1}, weryfikacja={dane z obecnego pliku; dostep nieustalony 2026-10}, dostep={?}}
@article{maslow1943theory, author={Maslow, A. H.}, title={A Theory of Human Motivation}, journal={Psychological Review}, year={1943}, % [bez zmian]
  status={K}, rozdzial={1.2}, weryfikacja={nie sprawdzono ponownie 2026-10}, dostep={B}, url={DO UZUPELNIENIA: kopia York Univ. Classics in the History of Psychology}, urldate={2026-10-08}}
@article{ryan2000self, author={Ryan, Richard M. and Deci, Edward L.}, title={Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being}, journal={American Psychologist}, year={2000}, % [bez zmian]
  status={K}, rozdzial={1.2}, weryfikacja={nie sprawdzono ponownie 2026-10}, dostep={B}, url={DO UZUPELNIENIA: selfdeterminationtheory.org}, urldate={2026-10-08}}
@article{keramati2014homeostatic, author={Keramati, Mehdi and Gutkin, Boris}, title={Homeostatic Reinforcement Learning for Integrating Reward Collection and Physiological Stability}, journal={eLife}, year={2014}, % [bez zmian]
  status={K}, rozdzial={1.2, 1.3, 4.5, 6.1}, weryfikacja={nie sprawdzono ponownie 2026-10}, dostep={A}}
@article{oudeyer2007intrinsic, author={Oudeyer, Pierre-Yves and Kaplan, Frederic}, title={What is Intrinsic Motivation? A Typology of Computational Approaches}, journal={Frontiers in Neurorobotics}, year={2007}, % [bez zmian]
  status={K}, rozdzial={1.3}, weryfikacja={nie sprawdzono ponownie 2026-10}, dostep={A}}
@article{singh2010intrinsically, author={Singh, Satinder and others}, title={Intrinsically Motivated Reinforcement Learning: An Evolutionary Perspective}, journal={IEEE Transactions on Autonomous Mental Development}, year={2010}, % [bez zmian]
  status={K}, rozdzial={1.3}, weryfikacja={nie sprawdzono ponownie 2026-10}, dostep={?}}
@article{schmidhuber2010formal, author={Schmidhuber, J{\"u}rgen}, title={Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990--2010)}, journal={IEEE Transactions on Autonomous Mental Development}, year={2010}, % [bez zmian]
  status={K}, rozdzial={1.3}, weryfikacja={nie sprawdzono ponownie 2026-10}, dostep={B}, url={DO UZUPELNIENIA: strona autora IDSIA}, urldate={2026-10-08}}
@article{man2019homeostasis, author={Man, Kingson and Damasio, Antonio}, title={Homeostasis and Soft Robotics in the Design of Feeling Machines}, journal={Nature Machine Intelligence}, volume={1}, number={10}, pages={446--452}, year={2019}, doi={10.1038/s42256-019-0103-7},
  status={Z}, rozdzial={1.5}, weryfikacja={nature.com: DOI, numer, strony 2026-10; brak legalnej kopii bezplatnej}, dostep={C}}
@article{kuehn2017artificial, author={Kuehn, Johannes and Haddadin, Sami}, title={An Artificial Robot Nervous System To Teach Robots How To Feel Pain And Reflexively React To Potentially Damaging Contacts}, journal={IEEE Robotics and Automation Letters}, volume={2}, number={1}, pages={72--79}, year={2017}, doi={10.1109/LRA.2016.2536360},
  status={Z}, rozdzial={1.5}, weryfikacja={DOI/tom/strony zgodne w cytowaniach Springer i komunikacie TUM 2026-10; online 2016; brak kopii}, dostep={C}}
@article{sharkey2025could, author={Sharkey, Amanda}, title={Could a Robot Feel Pain?}, journal={AI \& Society}, volume={40}, number={5}, pages={3641--3651}, year={2025}, doi={10.1007/s00146-024-02110-y},
  status={Z}, rozdzial={1.5, 6.3}, weryfikacja={Springer (OA CC BY), White Rose eprints 227884, 2026-10}, dostep={A}}
@article{asada2019artificial, author={Asada, Minoru}, title={Artificial Pain May Induce Empathy, Morality, and Ethics in the Conscious Mind of Robots}, journal={Philosophies}, volume={4}, number={3}, pages={38}, year={2019}, doi={10.3390/philosophies4030038},
  status={Z}, rozdzial={1.5}, weryfikacja={MDPI, OA CC BY, 2026-10}, dostep={A}}

% ===== B. Agenci i RL =====
@book{russell2020artificial, author={Russell, Stuart and Norvig, Peter}, title={Artificial Intelligence: A Modern Approach}, edition={4}, publisher={Pearson}, year={2020},
  status={K}, rozdzial={1.1}, weryfikacja={podrecznik; brak legalnej kopii bezplatnej 2026-10}, dostep={C}}
@book{sutton2018reinforcement, author={Sutton, Richard S. and Barto, Andrew G.}, title={Reinforcement Learning: An Introduction}, edition={2}, publisher={MIT Press}, year={2018},
  status={Z}, rozdzial={1.1}, weryfikacja={adres PDF autorow z wielu zrodel; errata autorow potwierdza drugi druk 2020; PDF nie otwierany 2026-10}, dostep={B}, url={http://incompleteideas.net/book/RLbook2020.pdf}, urldate={2026-10-08}}
@book{astrom2021feedback, author={{\AA}str{\"o}m, Karl Johan and Murray, Richard M.}, title={Feedback Systems: An Introduction for Scientists and Engineers}, edition={2}, publisher={Princeton University Press}, year={2021}, isbn={978-0691193984},
  status={Z}, rozdzial={1.1, 4.5}, weryfikacja={wydanie 2.02.2021, 528 s., ISBN 978-0691193984, e-ISBN 9780691213477 (portal badawczy Lund University, Google Books); fbswiki (pelny PDF 2. wyd., 24.07.2020) 2026-10}, dostep={B}, url={https://fbswiki.org/wiki/index.php/Feedback_Systems:_An_Introduction_for_Scientists_and_Engineers}, urldate={2026-10-08}}

% ===== C. LLM =====
@inproceedings{vaswani2017attention, author={Vaswani, Ashish and others}, title={Attention Is All You Need}, booktitle={Advances in Neural Information Processing Systems 30}, year={2017}, % [bez zmian; strony do odczytu z proceedings.neurips.cc]
  status={K}, rozdzial={2.1}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{brown2020language, author={Brown, Tom B. and others}, title={Language Models are Few-Shot Learners}, booktitle={Advances in Neural Information Processing Systems 33}, year={2020}, % [bez zmian]
  status={K}, rozdzial={2.1, 3.1}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{ouyang2022training, author={Ouyang, Long and others}, title={Training Language Models to Follow Instructions with Human Feedback}, booktitle={Advances in Neural Information Processing Systems 35}, year={2022}, % [bez zmian]
  status={K}, rozdzial={2.1, 3.1}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{wei2022chain, author={Wei, Jason and others}, title={Chain-of-Thought Prompting Elicits Reasoning in Large Language Models}, booktitle={Advances in Neural Information Processing Systems 35}, year={2022}, % [bez zmian]
  status={K}, rozdzial={2.2}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@article{guo2025deepseekr1, author={Guo, Daya and others}, title={DeepSeek-R1 Incentivizes Reasoning in LLMs through Reinforcement Learning}, journal={Nature}, year={2025}, % [bez zmian]
  status={Z}, rozdzial={2.2}, weryfikacja={dane z obecnego pliku; OA do potwierdzenia 2026-10}, dostep={A}}
@misc{qwen2024qwen25, author={{Qwen Team}}, title={Qwen2.5 Technical Report}, howpublished={arXiv:2412.15115}, year={2024},
  status={Z}, rozdzial={2.2, 4.1}, weryfikacja={wersji recenzowanej nie szukano 2026-10}, dostep={A}}
@misc{deepseek2025distillcard, author={{DeepSeek-AI}}, title={DeepSeek-R1-Distill-Qwen-14B: karta modelu}, howpublished={Hugging Face}, year={2025}, % [bez zmian: url, urldate]
  status={Z}, rozdzial={2.2, 4.4}, weryfikacja={dane z obecnego pliku}, dostep={A}}
@inproceedings{renze2024effect, author={Renze, Matthew}, title={The Effect of Sampling Temperature on Problem Solving in Large Language Models}, booktitle={Findings of EMNLP 2024}, year={2024}, % [bez zmian]
  status={Z}, rozdzial={2.1, 4.4}, weryfikacja={dane z obecnego pliku}, dostep={A}}
@inproceedings{li2024evaluating, author={Li, Shiyao and Ning, Xuefei and Wang, Luning and Liu, Tengxuan and Shi, Xiangsheng and Yan, Shengen and Dai, Guohao and Yang, Huazhong and Wang, Yu}, title={Evaluating Quantized Large Language Models}, booktitle={Proceedings of the 41st International Conference on Machine Learning}, series={PMLR}, volume={235}, pages={28480--28524}, year={2024}, url={https://proceedings.mlr.press/v235/li24bb.html},
  status={Z}, rozdzial={4.1, 6.3}, weryfikacja={wynik PMLR + ACM DL 2026-10 (klucz li24bb)}, dostep={A}}

% ===== D. Agenci LLM, motywacja =====
@inproceedings{yao2023react, author={Yao, Shunyu and others}, title={ReAct: Synergizing Reasoning and Acting in Language Models}, booktitle={ICLR 2023}, year={2023}, % [bez zmian]
  status={K}, rozdzial={2.3}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{shinn2023reflexion, author={Shinn, Noah and others}, title={Reflexion: Language Agents with Verbal Reinforcement Learning}, booktitle={Advances in Neural Information Processing Systems 36}, year={2023}, % [poprawka: lista autorow wg NeurIPS bez E. Bermana; strony do odczytu]
  status={K}, rozdzial={2.3}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{park2023generative, author={Park, Joon Sung and others}, title={Generative Agents: Interactive Simulacra of Human Behavior}, booktitle={UIST 2023}, year={2023}, % [bez zmian]
  status={K}, rozdzial={2.3, 2.4, 4.5}, weryfikacja={nie sprawdzono 2026-10}, dostep={B}, url={https://arxiv.org/abs/2304.03442}, urldate={2026-10-08}}
@article{wang2024survey, author={Wang, Lei and others}, title={A Survey on Large Language Model Based Autonomous Agents}, journal={Frontiers of Computer Science}, year={2024}, % [bez zmian]
  status={K}, rozdzial={1.1, 2.3}, weryfikacja={nie sprawdzono 2026-10}, dostep={B}, url={https://arxiv.org/abs/2308.11432}, urldate={2026-10-08}}
@article{sumers2024cognitive, author={Sumers, Theodore R. and others}, title={Cognitive Architectures for Language Agents}, journal={Transactions on Machine Learning Research}, year={2024}, % [bez zmian]
  status={K}, rozdzial={2.3}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{wang2023humanoid, author={Wang, Zhilin and others}, title={Humanoid Agents: Platform for Simulating Human-like Generative Agents}, booktitle={EMNLP 2023: System Demonstrations}, pages={167--176}, year={2023}, % [bez zmian]
  status={Z}, rozdzial={2.4}, weryfikacja={dane z obecnego pliku}, dostep={A}}
@inproceedings{wang2025simulating, author={Wang, Yiding and others}, title={Simulating Human-like Daily Activities with Desire-driven Autonomy}, booktitle={ICLR 2025}, year={2025}, % [bez zmian]
  status={Z}, rozdzial={2.4}, weryfikacja={dane z obecnego pliku}, dostep={A}}
@misc{masumori2025survival, author={Masumori, Atsushi and Ikegami, Takashi}, title={Do Large Language Model Agents Exhibit a Survival Instinct? An Empirical Study in a Sugarscape-Style Simulation}, howpublished={arXiv:2508.12920}, year={2025}, note={preprint},
  status={Z}, rozdzial={2.4, 3.4, 4.5, 6.2}, weryfikacja={arXiv, DBLP CoRR, strona lab. Ikegami 2026-10: brak wersji recenzowanej}, dostep={A}}
@inproceedings{du2023guiding, author={Du, Yuqing and others}, title={Guiding Pretraining in Reinforcement Learning with Large Language Models}, booktitle={ICML 2023}, year={2023}, % [bez zmian]
  status={K}, rozdzial={1.3, 2.4}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{klissarov2024motif, author={Klissarov, Martin and others}, title={Motif: Intrinsic Motivation from Artificial Intelligence Feedback}, booktitle={ICLR 2024}, year={2024}, % [bez zmian]
  status={K}, rozdzial={1.3, 2.4}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@mastersthesis{zawislak2025budowa, author={Zawi{\'s}lak, Klaudia}, title={Budowa agenta motywowanego na bazie Du{\.z}ego Modelu J{\k{e}}zykowego (LLM)}, school={Politechnika Rzeszowska, WMiFS}, address={Rzesz{\'o}w}, year={2025},
  status={Z}, rozdzial={2.5, 4.1, 4.5, 6.1}, weryfikacja={strona tytulowa (rok 2025)}, dostep={C}}
@inproceedings{liu2024agentbench, author={Liu, Xiao and Yu, Hao and Zhang, Hanchen and Xu, Yifan and Lei, Xuanyu and Lai, Hanyu and Gu, Yu and Ding, Hangliang and Men, Kaiwen and Yang, Kejuan and Zhang, Shudan and Deng, Xiang and Zeng, Aohan and Du, Zhengxiao and Zhang, Chenhui and Shen, Sheng and Zhang, Tianjun and Su, Yu and Sun, Huan and others}, title={AgentBench: Evaluating LLMs as Agents}, booktitle={The Twelfth International Conference on Learning Representations (ICLR 2024)}, year={2024}, eprint={2308.03688}, archiveprefix={arXiv},
  status={K}, rozdzial={4.5}, weryfikacja={arXiv PDF + cytowania 2026-10; 3 ostatnich autorow do odczytu z OpenReview}, dostep={A}}

% ===== E. Prompt, ramowanie, bol w LLM =====
@misc{schulhoff2024prompt, author={Schulhoff, Sander and Ilie, Michael and Balepur, Nishant and Kahadze, Konstantine and Liu, Amanda and Si, Chenglei and Li, Yinheng and Gupta, Aayush and Han, HyoJung and Schulhoff, Sevien and Dulepet, Pranav Sandeep and Vidyadhara, Saurav and Ki, Dayeon and Agrawal, Sweta and Pham, Chau Minh and Kroiz, Gerson C. and Li, Feileen and Tao, Hudson and Srivastava, Ashay and Da Costa, Hevander and Gupta, Saloni and Rogers, Megan L. and Goncearenco, Inna and Sarli, Giuseppe and Galynker, Igor and Peskoff, Denis and Carpuat, Marine and White, Jules and Anadkat, Shyamal and Hoyle, Alexander Miserlis and Resnik, Philip}, title={The Prompt Report: A Systematic Survey of Prompt Engineering Techniques}, howpublished={arXiv:2406.06608v6}, year={2024},
  status={Z}, rozdzial={3.1}, weryfikacja={arXiv v6 + Semantic Scholar 2026-10; data v6 i wersja recenzowana nieustalone}, dostep={A}}
@inproceedings{webson2022prompt, author={Webson, Albert and Pavlick, Ellie}, title={Do Prompt-Based Models Really Understand the Meaning of Their Prompts?}, booktitle={NAACL 2022}, year={2022}, % [bez zmian]
  status={K}, rozdzial={3.2}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{sclar2024quantifying, author={Sclar, Melanie and others}, title={Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design}, booktitle={ICLR 2024}, year={2024}, % [bez zmian]
  status={K}, rozdzial={3.2, 4.6, 6.2}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{salinas2024butterfly, author={Salinas, Abel and Morstatter, Fred}, title={The Butterfly Effect of Altering Prompts}, booktitle={Findings of ACL 2024}, year={2024}, % [bez zmian]
  status={K}, rozdzial={3.2}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@article{mizrahi2024state, author={Mizrahi, Moran and others}, title={State of What Art? A Call for Multi-Prompt LLM Evaluation}, journal={Transactions of the Association for Computational Linguistics}, year={2024}, % [bez zmian]
  status={K}, rozdzial={3.2, 4.6, 6.2}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{pezeshkpour2024large, author={Pezeshkpour, Pouya and Hruschka, Estevam}, title={Large Language Models Sensitivity to the Order of Options in Multiple-Choice Questions}, booktitle={Findings of NAACL 2024}, year={2024}, % [bez zmian]
  status={K}, rozdzial={3.2, 4.6}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@misc{li2023large, author={Li, Cheng and others}, title={Large Language Models Understand and Can Be Enhanced by Emotional Stimuli}, howpublished={arXiv:2307.11760}, year={2023},
  status={Z}, rozdzial={3.3}, weryfikacja={wersji recenzowanej nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{zheng2024helpful, author={Zheng, Mingqian and others}, title={When ``A Helpful Assistant'' Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models}, booktitle={Findings of EMNLP 2024}, year={2024}, % [bez zmian]
  status={K}, rozdzial={3.1, 3.3}, weryfikacja={nie sprawdzono 2026-10}, dostep={A}}
@article{tversky1981framing, author={Tversky, Amos and Kahneman, Daniel}, title={The Framing of Decisions and the Psychology of Choice}, journal={Science}, year={1981}, % [bez zmian]
  status={K}, rozdzial={3.3}, weryfikacja={nie sprawdzono 2026-10}, dostep={?}}
@article{shanahan2023role, author={Shanahan, Murray and McDonell, Kyle and Reynolds, Laria}, title={Role Play with Large Language Models}, journal={Nature}, volume={623}, number={7987}, pages={493--498}, year={2023}, doi={10.1038/s41586-023-06647-8},
  status={Z}, rozdzial={3.1, 3.3, 6.3}, weryfikacja={dane przyjete przez autora; OA do potwierdzenia}, dostep={A}}
@inproceedings{sharma2024towards, author={Sharma, Mrinank and others}, title={Towards Understanding Sycophancy in Language Models}, booktitle={ICLR 2024}, year={2024},
  status={Z}, rozdzial={3.3, 6.2}, weryfikacja={dane przyjete; pelna lista autorow z OpenReview do uzupelnienia}, dostep={A}}
@inproceedings{jones2022capturing, author={Jones, Erik and Steinhardt, Jacob}, title={Capturing Failures of Large Language Models via Human Cognitive Biases}, booktitle={Advances in Neural Information Processing Systems 35}, year={2022}, eprint={2202.12299}, archiveprefix={arXiv},
  status={Z}, rozdzial={3.3}, weryfikacja={poster NeurIPS 2022 (neurips.cc/virtual/2022/poster/53539); arXiv 2202.12299v2 z 24.11.2022 z adnotacja Published at NeurIPS 2022; tresc (dodatek B.2, framing) 2026-10}, dostep={A}}
@misc{keeling2024can, author={Keeling, Geoff and Street, Winnie and Stachaczyk, Martyna and Zakharova, Daria and Comşa, Iulia M. and Sakovych, Anastasiya and Logothetis, Isabella and Zhang, Zejia and Ag{\"u}era y Arcas, Blaise and Birch, Jonathan}, title={Can LLMs Make Trade-offs Involving Stipulated Pain and Pleasure States?}, howpublished={arXiv:2411.02432}, year={2024}, note={preprint},
  status={Z}, rozdzial={3.4, 4.2, 6.2}, weryfikacja={arXiv PDF 2026-10; w pracach z IX 2026 nadal cytowany jako preprint}, dostep={A}}
@article{binz2023using, author={Binz, Marcel and Schulz, Eric}, title={Using Cognitive Psychology to Understand GPT-3}, journal={Proceedings of the National Academy of Sciences}, year={2023}, % [bez zmian]
  status={Z}, rozdzial={3.4, 4.2}, weryfikacja={dane z obecnego pliku}, dostep={A}}
@misc{tagliabue2025probing, author={Tagliabue, Valen and Dung, Leonard}, title={Probing the Preferences of a Language Model: Integrating Verbal and Behavioral Tests of AI Welfare}, howpublished={arXiv:2509.07961v2}, year={2025}, note={preprint; v2 z 23.05.2026},
  status={Z}, rozdzial={3.4}, weryfikacja={arXiv abs 2026-10}, dostep={A}}
@misc{tagliabue2026pain, author={Tagliabue, Valen and Dung, Leonard and Berg, Cameron}, title={The Pain Axis: LLMs Represent Self-Directed Harm and Act on It}, howpublished={arXiv:2609.16247v2}, year={2026}, note={preprint; v2 z 25.09.2026; tytul v1: ``...Act to Relieve It''},
  status={Z}, rozdzial={3.4, 6.2}, weryfikacja={arXiv abs (v2) 2026-10}, dostep={A}}
@misc{bianco2026beyond, author={Bianco, Francesca and Shiller, Derek}, title={Beyond Behavioural Trade-Offs: Mechanistic Tracing of Pain-Pleasure Decisions in an LLM}, howpublished={arXiv:2602.19159v1}, year={2026}, note={preprint},
  status={Z}, rozdzial={3.4}, weryfikacja={arXiv abs + PDF 2026-10}, dostep={A}}
@misc{ren2026ai, author={Ren, Richard and Li, Kunyang and Mazeika, Mantas and others and Hendrycks, Dan}, title={AI Wellbeing: Measuring and Improving the Functional Pleasure and Pain of AIs}, howpublished={manuskrypt, Center for AI Safety}, year={2026}, url={https://www.ai-wellbeing.org/paper.pdf},
  status={?}, rozdzial={3.4, 6.3}, weryfikacja={README repozytorium i cytowania 2026-10: lista autorow niespojna (20 vs 21); brak arXiv/recenzji}, dostep={A}}
@misc{berg2026language, author={Berg, Cameron and Kaiser, Caspar}, title={Language Models Act on Hidden Valence}, howpublished={arXiv:2609.35591v1}, year={2026}, note={preprint},
  status={Z}, rozdzial={3.4}, weryfikacja={arXiv HTML v1 (28.09.2026) 2026-10}, dostep={A}}
@misc{schlatter2026incomplete, author={Schlatter, Jeremy and Weinstein-Raun, Benjamin and Ladish, Jeffrey}, title={Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs}, howpublished={arXiv:2509.14260v2}, year={2026}, note={preprint; v1 (2025): ``Shutdown Resistance in Large Language Models''},
  status={Z}, rozdzial={3.4, 6.2}, weryfikacja={arXiv abs (v2, 26.01.2026) 2026-10}, dostep={A}}

% ===== F. Metodologia =====
@misc{hagendorff2023machine, author={Hagendorff, Thilo and Dasgupta, Ishita and Binz, Marcel and Chan, Stephanie C. Y. and Lampinen, Andrew and Wang, Jane X. and Akata, Zeynep and Schulz, Eric}, title={Machine Psychology}, howpublished={arXiv:2303.13988v6}, year={2024}, note={preprint},
  status={Z}, rozdzial={4.2, 6.3}, weryfikacja={arXiv/alphaXiv (v6, 08.2024), Nature Rev. Psychol. 2025 cytuje jako preprint 2026-10}, dostep={A}}
@inproceedings{dominguezolmedo2024questioning, author={Dominguez-Olmedo, Ricardo and Hardt, Moritz and Mendler-D{\"u}nner, Celestine}, title={Questioning the Survey Responses of Large Language Models}, booktitle={Advances in Neural Information Processing Systems 37}, pages={45850--45878}, year={2024}, doi={10.52202/079017-1458},
  status={Z}, rozdzial={4.2, 6.3}, weryfikacja={papers.nips.cc, proceedings.com, arXiv 2306.07951v4 2026-10}, dostep={A}}
@misc{kocielnik2026rethinking, author={Kocielnik, Rafal and others}, title={Rethinking Psychometric Evaluation of LLMs: When and Why Self-Reports Predict Behavior}, howpublished={arXiv:2606.12730v1; ICML 2026 Workshop on Combining Theory and Benchmarks}, year={2026},
  status={?}, rozdzial={6.3}, weryfikacja={arXiv abs 2026-10; 7 wspolautorow nieustalonych}, dostep={A}}
@article{wichmann2001psychometric, author={Wichmann, Felix A. and Hill, N. Jeremy}, title={The Psychometric Function: I. Fitting, Sampling, and Goodness of Fit}, journal={Perception \& Psychophysics}, year={2001}, % [bez zmian]
  status={K}, rozdzial={4.3}, weryfikacja={nie sprawdzono 2026-10}, dostep={?}}
@article{wichmann2001bootstrap, author={Wichmann, Felix A. and Hill, N. Jeremy}, title={The Psychometric Function: II. Bootstrap-Based Confidence Intervals and Sampling}, journal={Perception \& Psychophysics}, volume={63}, number={8}, pages={1314--1329}, year={2001}, % [bez zmian: doi]
  status={Z}, rozdzial={4.3}, weryfikacja={dane z obecnego pliku}, dostep={?}}
@book{kingdom2016psychophysics, author={Kingdom, Frederick A. A. and Prins, Nicolaas}, title={Psychophysics: A Practical Introduction}, edition={2}, publisher={Academic Press}, year={2016},
  status={K}, rozdzial={4.3}, weryfikacja={podrecznik; brak kopii bezplatnej}, dostep={C}}
@article{prins2018applying, author={Prins, Nicolaas and Kingdom, Frederick A. A.}, title={Applying the Model-Comparison Approach to Test Specific Research Hypotheses in Psychophysical Research Using the Palamedes Toolbox}, journal={Frontiers in Psychology}, volume={9}, pages={1250}, year={2018}, doi={10.3389/fpsyg.2018.01250},
  status={Z}, rozdzial={4.3, 4.6}, weryfikacja={Frontiers PDF, PMC6064978 2026-10}, dostep={A}}
@article{schutt2016painfree, author={Sch{\"u}tt, Heiko H. and Harmeling, Stefan and Macke, Jakob H. and Wichmann, Felix A.}, title={Painfree and Accurate Bayesian Estimation of Psychometric Functions for (Potentially) Overdispersed Data}, journal={Vision Research}, volume={122}, pages={105--123}, year={2016}, doi={10.1016/j.visres.2016.02.002},
  status={Z}, rozdzial={4.3}, weryfikacja={dane przyjete przez autora; OA do potwierdzenia}, dostep={A}}
@article{kuss2005bayesian, author={Kuss, Malte and J{\"a}kel, Frank and Wichmann, Felix A.}, title={Bayesian Inference for Psychometric Functions}, journal={Journal of Vision}, volume={5}, number={5}, pages={478--492}, year={2005}, doi={10.1167/5.5.8},
  status={Z}, rozdzial={4.3}, weryfikacja={dane przyjete przez autora}, dostep={A}}
@misc{miller2024adding, author={Miller, Evan}, title={Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations}, howpublished={arXiv:2411.00640}, year={2024},
  status={Z}, rozdzial={4.3, 4.6}, weryfikacja={wersji recenzowanej nie sprawdzono 2026-10}, dostep={A}}
@inproceedings{atil2025nondeterminism, author={At{\i}l, Berk and Aykent, Sarp and Chittams, Alexa and Fu, Lisheng and Passonneau, Rebecca J. and Radcliffe, Evan and Rajagopal, Guru Rajan and Sloan, Adam and Tudrej, Tomasz and Ture, Ferhan and Wu, Zhe and Xu, Lixinyu and Baldwin, Breck}, title={Non-Determinism of ``Deterministic'' LLM System Settings in Hosted Environments}, booktitle={Proceedings of the 5th Workshop on Evaluation and Comparison of NLP Systems (Eval4NLP 2025)}, pages={135--148}, address={Mumbai, India}, publisher={Association for Computational Linguistics}, year={2025}, doi={10.18653/v1/2025.eval4nlp-1.12},
  status={Z}, rozdzial={4.4, 4.6, 6.3}, weryfikacja={ACL Anthology 2026-10; zastepuje atil2024nondeterminism (arXiv 2408.04667)}, dostep={A}}
@inproceedings{song2025good, author={Song, Yifan and Wang, Guoyin and Li, Sujian and Lin, Bill Yuchen}, title={The Good, The Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism}, booktitle={Proceedings of NAACL 2025 (Long Papers)}, pages={4195--4206}, year={2025}, doi={10.18653/v1/2025.naacl-long.211},
  status={Z}, rozdzial={4.4, 4.6, 6.3}, weryfikacja={dane przyjete przez autora}, dostep={A}}
@article{holm1979simple, author={Holm, Sture}, title={A Simple Sequentially Rejective Multiple Test Procedure}, journal={Scandinavian Journal of Statistics}, volume={6}, number={2}, pages={65--70}, year={1979}, url={https://www.jstor.org/stable/4615733},
  status={Z}, rozdzial={4.6}, weryfikacja={okladka JSTOR (stable 4615733) 2026-10; DOI 10.2307/4615733 cytowany, rozwiazywalnosc niesprawdzona -- nie wpisano}, dostep={C}}

% ===== G. Techniczne, formalne, modele progowe =====
@misc{ollama2026api, author={{Ollama}}, title={Ollama API Reference: Generate a Chat Completion}, year={2026}, % [bez zmian: url, urldate]
  status={Z}, rozdzial={4.1, 4.4}, weryfikacja={dane z obecnego pliku}, dostep={A}}
@misc{opi2023jsa, author={{OPI PIB}}, title={Analiza u{\.z}ycia sztucznej inteligencji -- Jednolity System Antyplagiatowy}, year={2023}, % [bez zmian]
  status={Z}, rozdzial={nie do pracy}, weryfikacja={dane z obecnego pliku}, dostep={A}}
@misc{wmifs2025wymagania, author={{WMiFS PRz}}, title={Wymagania dotycz{\k{a}}ce przygotowania pracy dyplomowej}, year={2025}, % [bez zmian]
  status={Z}, rozdzial={nie do pracy}, weryfikacja={dane z obecnego pliku}, dostep={A}}
@article{bonabeau1996quantitative, author={Bonabeau, Eric and Theraulaz, Guy and Deneubourg, Jean-Louis}, title={Quantitative Study of the Fixed Threshold Model for the Regulation of Division of Labour in Insect Societies}, journal={Proceedings of the Royal Society of London B}, volume={263}, number={1376}, pages={1565--1569}, year={1996}, doi={10.1098/rspb.1996.0229},
  status={Z}, rozdzial={6.1}, weryfikacja={strona wydawcy Royal Society (online 22.11.1996) 2026-10; dostep do sprawdzenia}, dostep={?}}
@article{bonabeau1998fixed, author={Bonabeau, Eric and Theraulaz, Guy and Deneubourg, Jean-Louis}, title={Fixed Response Thresholds and the Regulation of Division of Labor in Insect Societies}, journal={Bulletin of Mathematical Biology}, volume={60}, pages={753--807}, year={1998}, doi={10.1006/bulm.1998.0041},
  status={Z}, rozdzial={6.1}, weryfikacja={link.springer.com 2026-10}, dostep={C}}
@article{theraulaz1998response, author={Theraulaz, Guy and Bonabeau, Eric and Deneubourg, Jean-Louis}, title={Response Threshold Reinforcement and Division of Labour in Insect Societies}, journal={Proceedings of the Royal Society of London B}, volume={265}, number={1393}, pages={327--332}, year={1998}, doi={10.1098/rspb.1998.0299},
  status={Z}, rozdzial={6.1}, weryfikacja={rekord PubMed Central PMC1688885 (22.02.1998) 2026-10}, dostep={A}}
@article{ulrich2021response, author={Ulrich, Yuko and Kawakatsu, Mari and Tokita, Christopher K. and Saragosti, Jonathan and Chandra, Vikram and Tarnita, Corina E. and Kronauer, Daniel J. C.}, title={Response Thresholds Alone Cannot Explain Empirical Patterns of Division of Labor in Social Insects}, journal={PLOS Biology}, volume={19}, number={6}, pages={e3001269}, year={2021}, doi={10.1371/journal.pbio.3001269},
  status={Z}, rozdzial={6.1}, weryfikacja={rekordy PubMed i PLOS (17.06.2021) 2026-10}, dostep={A}}

% ===== H. Antropomorfizacja, swiadomosc, dobrostan =====
@article{butlin2026identifying, author={Butlin, Patrick and Long, Robert and Bayne, Tim and Bengio, Yoshua and Birch, Jonathan and Chalmers, David and Constant, Axel and Deane, George and Elmoznino, Eric and Fleming, Stephen M. and Ji, Xu and Kanai, Ryota and Klein, Colin and Lindsay, Grace and Michel, Matthias and Mudrik, Liad and Peters, Megan A. K. and Schwitzgebel, Eric and Simon, Jonathan and VanRullen, Rufin}, title={Identifying Indicators of Consciousness in AI Systems}, journal={Trends in Cognitive Sciences}, volume={30}, number={6}, pages={488--501}, year={2026}, doi={10.1016/j.tics.2025.10.011},
  status={Z}, rozdzial={6.3}, weryfikacja={CRIS TAU i IUCC (RIS), LSE eprint 130322 2026-10; online 2025}, dostep={A}}
@misc{long2024taking, author={Long, Robert and Sebo, Jeff and Butlin, Patrick and Finlinson, Kathleen and Fish, Kyle and Harding, Jacqueline and Pfau, Jacob and Sims, Toni and Birch, Jonathan and Chalmers, David}, title={Taking AI Welfare Seriously}, howpublished={arXiv:2411.00986v1}, year={2024}, note={preprint},
  status={Z}, rozdzial={6.3}, weryfikacja={arXiv abs 2026-10}, dostep={A}}

% ===== LISTA KONTROLNA 55 obecnych kluczy =====
% [x] starzyk2008motivation [x] starzyk2011motivated [x] starzyk2012motivated [x] starzyk2013simulation
% [x] graham2015opportunistic [x] starzyk2017mlecog [x] starzyk2017needs [x] maslow1943theory
% [x] ryan2000self [x] oudeyer2007intrinsic [x] singh2010intrinsically [x] schmidhuber2010formal
% [x] keramati2014homeostatic [x] man2019homeostasis [x] kuehn2017artificial [x] russell2020artificial
% [x] sutton2018reinforcement [x] vaswani2017attention [x] brown2020language [x] ouyang2022training
% [x] wei2022chain [x] guo2025deepseekr1 [x] qwen2024qwen25 [x] yao2023react [x] shinn2023reflexion
% [x] park2023generative [x] wang2024survey [x] sumers2024cognitive [x] wang2023humanoid
% [x] wang2025simulating [x] masumori2025survival [x] du2023guiding [x] klissarov2024motif
% [x] keeling2024can [x] webson2022prompt [x] sclar2024quantifying [x] salinas2024butterfly
% [x] mizrahi2024state [x] pezeshkpour2024large [x] li2023large [x] zheng2024helpful
% [x] tversky1981framing [x] binz2023using [x] hagendorff2023machine [x] wichmann2001psychometric
% [x] wichmann2001bootstrap [x] kingdom2016psychophysics [x] renze2024effect
% [x] atil2024nondeterminism -> atil2025nondeterminism (jedyna dozwolona zmiana klucza)
% [x] miller2024adding [x] zawislak2025budowa [x] ollama2026api [x] deepseek2025distillcard
% [x] opi2023jsa [x] wmifs2025wymagania   => 55/55
```

## 4. Tabela zmian w istniejących wpisach

| Klucz | Zmiana | Źródło |
|---|---|---|
| atil2024nondeterminism → atil2025nondeterminism | nowy klucz, wersja recenzowana Eval4NLP 2025, 13 autorów, s. 135–148, DOI | ACL Anthology 2025.eval4nlp-1.12 |
| graham2015opportunistic | autorzy (J. Graham, J. A. Starzyk, D. Jachyra), 26(8):1735–1746, DOI; status ? → Z | potwierdzenie autora (IEEE) |
| keeling2024can | pełna lista 10 autorów; adnotacja „preprint”; dodany podrozdział 4.2 | arXiv 2411.02432 |
| hagendorff2023machine | 8 autorów, wersja v6 (2024) zamiast jednoautorskiej v1; rok w polu year: 2024 (klucz bez zmian) | arXiv/alphaXiv; *Nat. Rev. Psychol.* 4:363–364 |
| masumori2025survival | pełni autorzy (Masumori, Ikegami); „preprint”; dodane 3.4, 4.5 | DBLP, arXiv |
| man2019homeostasis | DOI 10.1038/s42256-019-0103-7, numer 10; status ? → Z | nature.com |
| kuehn2017artificial | status ? → Z (DOI, tom i strony zgodne); adnotacja: online 2016 | cytowania Springer, TUM |
| sutton2018reinforcement | dodany url do bezpłatnego wydania autorskiego, dostep = B | incompleteideas.net |
| shinn2023reflexion | lista autorów wg NeurIPS (bez E. Bermana) | decyzja autora; strony nadal do odczytu |
| keramati2014homeostatic, park2023generative, wang2024survey, zheng2024helpful, sclar2024quantifying, mizrahi2024state, du2023guiding, klissarov2024motif, zawislak2025budowa | tylko pole rozdzial (nowe przypisania 1.1, 1.3, 3.1, 4.5, 4.6, 6.1, 6.2) | – |
| wszystkie | dodane pola dostep i weryfikacja | – |

## 5. Pozycje kategorii C: zamienniki lub uzasadnienie wyjątku

| Klucz | Rekomendacja |
|---|---|
| russell2020artificial | Wyjątek dla podręcznika klasycznego. Definicje z 1.1 można oprzeć na sutton2018reinforcement (B, rozdz. 3) i wang2024survey (B). Russell–Norvig cytować tylko pomocniczo. |
| kingdom2016psychophysics | Zamiennik: prins2018applying (A). Ci sami autorzy, ta sama funkcja psychometryczna i porównania modeli. Podręcznik zostawić jako uzupełnienie. |
| kuehn2017artificial | Kopii legalnej nie znalazłem. Opis tej pracy jest w sharkey2025could (A), co daje czytelnikowi dostęp przynajmniej do streszczenia. Proponuję poprosić autorów o kopię lub sprawdzić repozytorium TUM (mediaTUM). Do czasu znalezienia kopii: wyjątek „praca pierwotna”. |
| man2019homeostasis | Brak PMC i arXiv. Link Springer Nature SharedIt („free read”) jest niepotwierdzony; jeśli zadziała, zmienić na B. Funkcjonalnym zamiennikiem jest asada2019artificial (A), choć nie zastępuje argumentu homeostatycznego. |
| holm1979simple | JSTOR pozwala czytać bezpłatnie po rejestracji („Register & Read”), czyli legalnie, ale wymaga konta. Wyjątek: pierwotne źródło metody, którą praca stosuje. |
| bonabeau1998fixed | Zamiennik: ulrich2021response (A, PLOS Biology), który opisuje tę samą funkcję progową. |
| zawislak2025budowa | Wyjątek: praca referencyjna. Wskazać dostęp przez Bibliotekę PRz i ewentualnie poprosić o udostępnienie w repozytorium. |

**Pozycje „?” (11):** 6 prac Starzyka, singh2010intrinsically, tversky1981framing, oba Wichmann 2001 i bonabeau1996quantitative (theraulaz1998response ma już pełny tekst w PMC, PMC1688885). Dla prac Starzyka trzeba uzyskać od promotora lub autora wersje autorskie (dozwolone przez politykę IEEE dla zaakceptowanych manuskryptów) i umieścić je w repozytorium uczelni albo na stronie autora. Bez tego D12 nie jest spełnione dla rdzenia teoretycznego (1.4).

## 6. Pozycje niezweryfikowane lub niepewne

- **Status K, nie sprawdzone ponownie w tej sesji:** maslow1943theory, ryan2000self, oudeyer2007intrinsic, singh2010intrinsically, schmidhuber2010formal, keramati2014homeostatic, starzyk2017mlecog, park2023generative, wang2024survey, sumers2024cognitive, yao2023react, webson2022prompt, sclar2024quantifying, salinas2024butterfly, mizrahi2024state, pezeshkpour2024large, zheng2024helpful, tversky1981framing, du2023guiding, klissarov2024motif, russell2020artificial, kingdom2016psychophysics. Strony w NeurIPS (Brown, Ouyang, Wei, Vaswani, Shinn) również nie zostały sprawdzone. Należy je kliknąć na stronach wydawców przed oddaniem rozdziałów.
- **Nie sprawdzono, czy istnieją wersje recenzowane:** qwen2024qwen25, li2023large, miller2024adding. Dla keeling2024can, masumori2025survival i hagendorff2023machine sprawdziłem: stan na X.2026 to tylko preprinty.
- **Nowe pozycje z brakami:** ren2026ai (lista autorów niespójna, manuskrypt bez recenzji); kocielnik2026rethinking (7 współautorów); liu2024agentbench (3 ostatnich autorów); schulhoff2024prompt (data v6). Uzupełniono i potwierdzono: ulrich2021response (7 autorów, *PLoS Biol* 19(6):e3001269, rekordy PubMed i PLOS), jones2022capturing (Jones i Steinhardt, poster NeurIPS 2022), bonabeau1996quantitative (DOI 10.1098/rspb.1996.0229, strona Royal Society), theraulaz1998response (DOI 10.1098/rspb.1998.0299, PMC1688885), astrom2021feedback (wydanie 2.02.2021, ISBN 978-0691193984, wg portalu Lund University).
- **DOI Holma:** 10.2307/4615733 pojawia się w cytowaniach, ale jego rozwiązywalności nie sprawdziłem, więc nie wpisałem go do pliku.
- **Kandydaci znalezieni, ale nie dodani z powodu braku metadanych:** „Linking homeostasis to reinforcement learning: internal state control of motivated behavior” (*Current Opinion in Behavioral Sciences* 2025, arXiv 2507.04998; dobre źródło teorii redukcji popędu dla 1.3 i 6.1, autorzy nieustaleni); „Cash or Comfort? How LLMs Value Your Inconvenience” (arXiv 2506.17367; definiuje „cenę niewygody” jako punkt P = 0,5, czyli dokładnie próg psychometryczny); „Beyond Mimicry: Preference Coherence in LLMs” (arXiv 2511.13630).

## 7. Propozycje usunięcia (tylko propozycje)

- **schmidhuber2010formal** (priorytet N): teoria ciekawości jest daleko od bólu i homeostazy. Typologię wystarczająco pokrywa oudeyer2007intrinsic. Można usunąć, jeśli 1.3 ma być zwięzłe.
- **du2023guiding albo klissarov2024motif**: obie pełnią tę samą funkcję (LLM jako źródło nagrody wewnętrznej). Jedna wystarczy, chyba że 2.4 ma pokazać obie drogi.
- **kocielnik2026rethinking**: warsztat i niepełne metadane. Usunąć, jeśli do kwietnia 2027 nie pojawi się wersja z pełną listą autorów. Funkcję w 6.3 pełni dominguezolmedo2024questioning.
- **ren2026ai**: manuskrypt bez recenzji. Zostawić tylko wtedy, gdy autor chce wątku „dobrostanu funkcjonalnego”; w przeciwnym razie wystarczy berg2026language.

## 8. Pytania i decyzje dla autora

1. **Dostęp do prac Starzyka (1.4)**: czy promotor może pozyskać wersje autorskie? To warunek spełnienia D12 dla rdzenia pracy.
2. **Preprinty w 3.4**: 8 z 9 pozycji to preprinty, bo tak wygląda ta dziedzina w 2026 r. Czy przyjąć jawne zastrzeżenie w 6.3 („zależność od preprintów”), zamiast dopychać słabe pozycje recenzowane?
3. **Analiza dodatkowa**: czy dodać test ilorazu wiarygodności (prins2018applying) jako drugą metodę porównania θ obok bootstrapu? Wymaga to jednego zdania w 4.3.
4. **Analogia z owadami społecznymi (6.1)**: czy rozwijać wątek modeli progów odpowiedzi? Daje on gotową, opublikowaną postać funkcji progowej z parametrem stromości, ale wymaga 1–2 akapitów dyskusji.
5. **Klucze z rokiem wersji**: hagendorff2023machine (year = 2024) zostaje pod starym kluczem. Dla schlatter2026incomplete przyjąłem rok cytowanej wersji v2. Czy to akceptowalne?
6. **Kandydaci z sekcji 6**: dodać po uzupełnieniu metadanych, zwłaszcza „Cash or Comfort?”, które bezpośrednio stosuje próg P = 0,5?
