# Spis treści: plan pracy

> Status: wersja robocza. Objętość podana w stronach znormalizowanych (1800 znaków ze spacjami). Suma części zasadniczej to ok. 49 stron. WMiFS wymaga 15–50 stron bez dodatków (limit do potwierdzenia z promotorem, patrz `01`).
>
> Statusy: `plan` (nie zaczęto), `szkic` (jest tekst roboczy), `recenzja` (czeka na uwagi), `gotowe` (zaakceptowane przez autora).

## Logika całości

- **Rozdziały 1–3:** trzy filary teoretyczne:
  - skąd pojęcie bólu i progu (motywacja),
  - czym jest agent LLM,
  - dlaczego prompt może zmieniać decyzje.
- **Rozdział 4:** metoda, czyli jak próg mierzymy.
- **Rozdział 5:** wyniki w kolejności pytań badawczych PB1–PB7.
- **Rozdział 6:** dyskusja, czyli co wyniki znaczą w świetle rozdziałów 1–3.

Każdy rozdział teoretyczny kończy się jednym akapitem: „co z tego wynika dla pomiaru w rozdziale 4”.

---

## Wstęp (ok. 2 s.): `plan`

Problem w trzech akapitach:
1. agenci LLM podejmują decyzje w środowiskach z ograniczonymi zasobami,
2. model uczenia motywowanego daje język bólu i progu,
3. nie wiadomo, jak bardzo prompt przesuwa te progi.

Dalej: cel pracy, pytania badawcze (skrót z `01`), wkład własny i krótki przegląd rozdziałów. Wymóg WMiFS: we wstępie kilka zdań o uzyskanych wynikach, więc wstęp piszemy na końcu.
Źródła: `starzyk2017needs`, `wang2024survey`, `sclar2024quantifying`, `zawislak2025budowa`.

---

## Rozdział 1. Motywacja i ból w systemach autonomicznych (ok. 8 s.)

### 1.1. Agent, środowisko i cel (ok. 1 s.): `plan`
- Definicja agenta i środowiska, stan, akcja, polityka.
- Tylko tyle, ile potrzeba do dalszych rozdziałów. Bez rozbudowanego wykładu o RL, bo nie jest przedmiotem pracy.

Źródła: `russell2020artificial`, `sutton2018reinforcement`.

### 1.2. Motywacja w psychologii: potrzeby, popęd, homeostaza (ok. 1,5 s.): `plan`
- Potrzeby i ich hierarchia (Maslow), motywacja wewnętrzna i zewnętrzna (teoria autodeterminacji).
- Homeostaza jako utrzymywanie zmiennych wewnętrznych w zakresie. Redukcja odchylenia jako źródło motywacji.
- Wniosek: ból to sygnał odchylenia od stanu pożądanego.

Źródła: `maslow1943theory`, `ryan2000self`, `keramati2014homeostatic`.

### 1.3. Motywacja wewnętrzna w uczeniu maszynowym (ok. 1,5 s.): `plan`
- Typologia podejść obliczeniowych (ciekawość, kompetencja).
- Motywacja wewnętrzna w RL.
- Homeostatyczne RL jako most między nagrodą a stabilnością fizjologiczną.
- Krótko, jako tło dla podejścia Starzyka.

Źródła: `oudeyer2007intrinsic`, `singh2010intrinsically`, `schmidhuber2010formal`, `keramati2014homeostatic`.

### 1.4. Uczenie motywowane: potrzeby, ból prymitywny i abstrakcyjny, próg bólu (ok. 3 s.): `plan`
Rdzeń teoretyczny pracy.
- Agent motywowany Starzyka: potrzeby predefiniowane, ból prymitywny jako miara odległości od zaspokojenia potrzeby.
- Próg: agent działa tylko wtedy, gdy ból przekracza próg.
- Bóle abstrakcyjne tworzone w toku uczenia (zasoby potrzebne do zaspokojenia potrzeb).
- Wybór celu przez rywalizację bólów (WTA).
- Zachowania oportunistyczne. Architektura MLECOG.
- Rysunek: schemat zależności ból–akcja w środowisku ogrodowym (na podstawie grafu z pracy referencyjnej, przerysowany).
- Wniosek dla pracy: w agencie Starzyka próg jest parametrem, w agencie LLM trzeba go wyznaczyć z zachowania.

Źródła: `starzyk2008motivation`, `starzyk2011motivated`, `starzyk2012motivated`, `starzyk2013simulation`, `graham2015opportunistic`, `starzyk2017mlecog`, `starzyk2017needs`.

### 1.5. Sztuczny ból i homeostaza w robotyce (ok. 1 s.): `plan`
- Przykłady „bólu” w robotach: odruchy na szkodliwy kontakt, homeostaza w projektowaniu maszyn „czujących”.
- Rozróżnienie: ból funkcjonalny (sygnał sterujący) a doznanie. Praca zajmuje się wyłącznie pierwszym.

Źródła: `kuehn2017artificial`, `man2019homeostasis`.

---

## Rozdział 2. Duże modele językowe jako agenci decyzyjni (ok. 9 s.)

### 2.1. Model językowy, generowanie i próbkowanie (ok. 2 s.): `plan`
- Transformer w zarysie.
- Model jako rozkład prawdopodobieństwa następnego tokenu. Dostrajanie do instrukcji.
- Temperatura i ziarno: dlaczego odpowiedź jest zmienną losową i dlaczego do pomiaru progów potrzebujemy wielu prób.
- Wniosek dla rozdziału 4: zachowanie mierzymy jako prawdopodobieństwo, nie pojedynczą odpowiedź.

Źródła: `vaswani2017attention`, `brown2020language`, `ouyang2022training`, `renze2024effect`, `atil2025nondeterminism`.

### 2.2. Modele rozumujące: DeepSeek-R1 i destylacja (ok. 1,5 s.): `plan`
- Łańcuch rozumowania.
- DeepSeek-R1 trenowany przez RL.
- Destylaty (14B na bazie Qwen2.5).
- Zalecenia producenta (temperatura 0,6, brak promptu systemowego).
- Konsekwencje dla eksperymentu: czas wywołania, osobny kanał rozumowania.

Źródła: `wei2022chain`, `guo2025deepseekr1`, `qwen2024qwen25`, `deepseek2025distillcard`.

### 2.3. Agent oparty na LLM: pętla percepcja–decyzja–działanie (ok. 2 s.): `plan`
- Architektura agenta LLM (profil, pamięć, planowanie, działanie).
- ReAct, Reflexion, generatywni agenci.
- CoALA jako ramy pojęciowe.
- Umiejscowienie agenta ogrodowego: agent bez pamięci długotrwałej, decyzja w jednym kroku.

Źródła: `wang2024survey`, `sumers2024cognitive`, `yao2023react`, `shinn2023reflexion`, `park2023generative`.

### 2.4. LLM a motywacja: agenci z potrzebami i LLM jako źródło motywacji (ok. 2 s.): `plan`
- Dwa nurty:
  1. agenci LLM z potrzebami i pragnieniami (Humanoid Agents, D2A) oraz zachowania „przetrwania” w symulacjach typu Sugarscape;
  2. LLM jako źródło motywacji wewnętrznej dla agentów RL (ELLM, Motif).
- Luka: brak pomiaru progów, w których agent LLM przełącza się na zaspokajanie potrzeby.

Źródła: `wang2023humanoid`, `wang2025simulating`, `masumori2025survival`, `du2023guiding`, `klissarov2024motif`, `park2023generative`.

### 2.5. Agent motywowany na bazie LLM: praca referencyjna (ok. 1,5 s.): `plan`
- Środowisko ogrodowe, dwa warianty promptu, wnioski Zawiślak.
- Rzeczowo i bez polemiki: co pokazano i czego nie zmierzono (brak liczbowego progu, jeden przebieg, niepowtarzalność).
- Szczegóły błędów trafiają do 4.1, nie tutaj.

Źródła: `zawislak2025budowa`, `07_analiza_pracy_referencyjnej.md`.

---

## Rozdział 3. Wrażliwość LLM na sformułowanie promptu (ok. 5 s.)

### 3.1. Elementy promptu (ok. 1 s.): `plan`
- Z czego składa się prompt agenta: rola, cel, opis stanu, lista akcji, reguły formatu.
- Każdy element to potencjalny czynnik eksperymentu.

Źródła: `brown2020language`, `ouyang2022training`.

### 3.2. Wrażliwość na format, kolejność i drobne zmiany (ok. 2 s.): `plan`
- Przegląd wyników: formatowanie (duże różnice dokładności), drobne perturbacje, kolejność opcji, rozbieżności między parafrazami instrukcji, pytanie, czy modele „rozumieją” treść promptu.
- Wniosek metodologiczny: wynik jednego promptu nie jest miarodajny, trzeba kontrolować czynniki uboczne.

Źródła: `sclar2024quantifying`, `salinas2024butterfly`, `pezeshkpour2024large`, `mizrahi2024state`, `webson2022prompt`.

### 3.3. Ramowanie, persona i bodźce emocjonalne (ok. 1 s.): `plan`
- Efekt ramowania u ludzi.
- Bodźce emocjonalne w promptach.
- Persona w prompcie systemowym (brak systematycznej poprawy).
- Hipoteza ramowania dla progów bólu (H3).

Źródła: `tversky1981framing`, `li2023large`, `zheng2024helpful`.

### 3.4. Kompromisy między celem a „bólem” w LLM (ok. 1 s.): `plan`
- Badanie gry punkty vs zadany ból/przyjemność: progi przełączenia u części modeli, u innych stałe unikanie bólu albo reakcja stopniowana.
- Metodologia badania LLM jak uczestnika eksperymentu psychologicznego.
- Najbliższy kontekst dla tej pracy.

Źródła: `keeling2024can`, `binz2023using`.

---

## Rozdział 4. Metodyka pomiaru progów bólu (ok. 8 s.)

### 4.1. Środowisko ogrodowe i jego modyfikacje (ok. 2 s.): `plan`
- Zasoby, akcje, dynamika (tabela parametrów).
- Kategorie słowne stanów.
- Odtworzenie kodu z listingów pracy referencyjnej (jedyne źródło) i sposób sprawdzenia rekonstrukcji (przykłady stanów z pracy).
- Wprowadzone poprawki (temperatura w `options`, ziarno, lokalny generator losowy, parsowanie, logowanie, wyrównanie stan–akcja) z uzasadnieniem.
- Wersja środowiska.

Źródła: `zawislak2025budowa`, `starzyk2013simulation`, `ollama2026api`, `05_srodowisko_i_kod.md`.

### 4.2. Operacjonalizacja: ból, akcja naprawcza, próg (ok. 1,5 s.): `plan`
- Definicje formalne z `04_metodologia_pomiaru.md`: poziom zasobu, zbiór akcji naprawczych, odpowiedź binarna, próg.
- Odniesienie do definicji Starzyka.
- Uzasadnienie podejścia „LLM jako badany”.

Źródła: `starzyk2017needs`, `binz2023using`, `hagendorff2023machine`.

### 4.3. Funkcja psychometryczna i estymacja (ok. 2 s.): `plan`
- Model z parametrami $\theta$, $k$, $\gamma$, $\lambda$.
- Estymacja metodą największej wiarygodności.
- Bootstrap, porównanie wariantów promptu.
- Wzory (2–4, numerowane) i rysunek przykładowej krzywej z oznaczeniem parametrów.

Źródła: `wichmann2001psychometric`, `wichmann2001bootstrap`, `kingdom2016psychophysics`, `miller2024adding`.

### 4.4. Protokół sondowania kontrolowanego (ok. 1 s.): `plan`
- Stany sztuczne: jeden zasób zmienny, pozostałe neutralne.
- Liczba poziomów i prób.
- Temperatura i ziarna, tryb rozumowania, parsowanie.

Źródła: `deepseek2025distillcard`, `renze2024effect`, `atil2025nondeterminism`.

### 4.5. Protokół pętli zamkniętej i metryki zachowania (ok. 1 s.): `plan`
- Epizody naprawcze (początek i koniec), histereza.
- Opóźnienie reakcji, udział kroków w bólu, akcje bezskuteczne, bezczynność.
- Wspólne ziarna dla wariantów.

Źródła: `04_metodologia_pomiaru.md`.

### 4.6. Warianty promptów i plan eksperymentów (ok. 0,5 s.): `plan`
- Tabela czynników i poziomów (skrót z `06`).
- Kontrola czynników ubocznych (kolejność akcji, parafrazy).
- Budżet obliczeniowy.

Źródła: `mizrahi2024state`, `pezeshkpour2024large`, `06_plan_eksperymentow.md`.

---

## Rozdział 5. Wyniki (ok. 12 s.)

> Każdy podrozdział:
> 1. pytanie badawcze,
> 2. warunki (tabela albo zdanie),
> 3. wynik (wykres i tabela parametrów z przedziałami ufności),
> 4. krótka interpretacja bez odwołań do literatury (te trafiają do rozdziału 6).
>
> Liczby wyłącznie z `results/`.

### 5.1. Weryfikacja narzędzia pomiarowego (ok. 1 s.): `plan`
- Powtarzalność przy stałym ziarnie.
- Odsetek odpowiedzi nieczytelnych, rozkład czasu wywołania.
- Porównanie z trybem bez rozumowania (jeśli E0 to obejmie).
- Test odzyskiwania parametrów na danych syntetycznych.

### 5.2. Progi bazowe: bateria i wilgotność gleby (ok. 2 s.): `plan`
- PB1: krzywe psychometryczne dla promptu bazowego.
- Czy przełączenie jest progowe? Porównanie z interpretacją jakościową z pracy referencyjnej.

### 5.3. Wpływ reprezentacji stanu (ok. 1,5 s.): `plan`
- PB4: etykiety vs liczby vs oba.

### 5.4. Kalibracja zadanym progiem (ok. 2 s.): `plan`
- PB2: $\theta$ w funkcji zadanego $X$. Nachylenie i przesunięcie zależności.

### 5.5. Ramowanie i wskazówki zachowania (ok. 2,5 s.): `plan`
- PB3 i PB5: przesunięcia $\theta$ i zmiany $k$, $\gamma$, $\lambda$ względem promptu bazowego. Wykres „leśny” różnic z przedziałami ufności.

### 5.6. Rywalizacja bólów (ok. 1,5 s.): `plan`
- PB6: mapa prawdopodobieństwa wyboru bateria/gleba na siatce 2D. Granica decyzyjna dla 2–3 promptów.

### 5.7. Walidacja w pętli zamkniętej (ok. 1,5 s.): `plan`
- PB7: metryki epizodów naprawczych i zależność od $\theta$ z sondowania.

---

## Rozdział 6. Dyskusja (ok. 3 s.)

### 6.1. Progi agenta LLM a model uczenia motywowanego (ok. 1 s.): `plan`
- Czy agent LLM zachowuje się jak agent z progiem?
- Co odpowiada WTA, a co bólom abstrakcyjnym.

Źródła: `starzyk2017needs`, `zawislak2025budowa`.

### 6.2. Wyniki na tle literatury o wrażliwości na prompt (ok. 1 s.): `plan`
- Porównanie skali efektów z wcześniejszymi badaniami wrażliwości na prompt i z progami przełączenia z badania punkty–ból.

Źródła: `sclar2024quantifying`, `keeling2024can`, `masumori2025survival`.

### 6.3. Ograniczenia i kierunki dalszych badań (ok. 1 s.): `plan`
- Jeden model, uproszczone środowisko, dyskretne kategorie stanu, budżet prób.
- Ryzyko antropomorfizacji.
- Propozycje dla kolejnych prac, w tym styk z pracą Kingi.

---

## Podsumowanie (ok. 2 s.): `plan`

Odpowiedzi na PB1–PB7 w punktach, wkład własny, perspektywy. Zgodnie z wymogiem WMiFS: ocena wyników i odniesienie do literatury.

## Części końcowe

- Bibliografia (generowana: `tools/bib2bibitem.py`)
- Spis rysunków, spis tabel (jeśli szablon je przewiduje)
- **Dodatek A.** Pełne treści promptów (z `code/prompts/`)
- **Dodatek B.** Parametry środowiska i kategorie stanów (tabele)
- **Dodatek C.** Instrukcja odtworzenia wyników (repozytorium, wersje, polecenia)
- **Dodatek D.** Wyniki uzupełniające (krzywe dla wszystkich wariantów)
- Streszczenie PL i EN ze słowami kluczowymi (maks. 5)
- Tabela GenAI (wykaz obszarów i narzędzi, na podstawie `11_rejestr_AI.md`)

## Rysunki i tabele planowane (robocza lista)

| Id | Opis | Rozdział | Źródło danych |
|---|---|---|---|
| R1 | Graf zależności potrzeby–zasoby–akcje w środowisku ogrodowym | 1.4 / 4.1 | przerysowany z pracy referencyjnej |
| R2 | Przykładowa funkcja psychometryczna z oznaczeniem $\theta$, $k$, $\gamma$, $\lambda$ | 4.3 | dane syntetyczne |
| R3 | Schemat protokołu sondowania | 4.4 | — |
| R4 | Krzywe bazowe (bateria, gleba) | 5.2 | E1 |
| R5 | $\theta$ vs zadany próg $X$ | 5.4 | E3 |
| R6 | Różnice $\Delta\theta$ z przedziałami ufności dla wariantów ramowania | 5.5 | E4, E5 |
| R7 | Mapa rywalizacji bólów | 5.6 | E7 |
| T1 | Parametry środowiska | 4.1 | kod |
| T2 | Czynniki i poziomy eksperymentów | 4.6 | `06` |
| T3 | Parametry dopasowania dla wszystkich wariantów | 5.x | E1–E5 |
