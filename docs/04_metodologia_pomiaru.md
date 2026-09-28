# Metodologia pomiaru progów bólu

> Status: propozycja do akceptacji promotora. Ten plik jest podstawą rozdziału 4 i kodu w `code/probe/` oraz `code/analysis/`.
>
> Oznaczenia są stałe w całej pracy (zob. `08_slownik_pojec.md`).

## 1. Idea

Agent motywowany Starzyka ma próg bólu jako parametr: działa, gdy ból przekracza próg~\cite{starzyk2017needs}. Agent LLM takiego parametru nie ma. Jego „próg” trzeba odczytać z zachowania. Traktujemy więc model jak uczestnika eksperymentu psychofizycznego~\cite{binz2023using}:
- zmieniamy poziom jednego zasobu,
- wielokrotnie pytamy o decyzję,
- mierzymy prawdopodobieństwo reakcji naprawczej,
- dopasowujemy do tych danych krzywą psychometryczną~\cite{wichmann2001psychometric, kingdom2016psychophysics}.

Prompt jest zmienną niezależną, parametry krzywej są zmiennymi zależnymi.

## 2. Pojęcia i oznaczenia

| Symbol | Znaczenie |
|---|---|
| $r$ | zasób (potrzeba): `bateria`, `gleba`; abstrakcyjne: `konewka`, `zapas_baterii`, `kredyty` |
| $x_r$ | poziom zasobu $r$ (0–100%, dla zapasu baterii w sztukach) |
| $s$ | pełny stan środowiska (wszystkie zasoby i nasłonecznienie) |
| $A_r$ | zbiór akcji naprawczych dla zasobu $r$ (tabela niżej) |
| $y$ | odpowiedź binarna: $y = 1$, gdy wybrana akcja $a \in A_r$ |
| $P_r(x)$ | prawdopodobieństwo reakcji naprawczej przy poziomie $x$ i ustalonym kontekście |
| $\theta_r$ | **próg bólu**: punkt środkowy przejścia funkcji psychometrycznej |
| $k$ | ostrość przejścia (nachylenie) |
| $\gamma$ | poziom reakcji bez potrzeby (odpowiednik fałszywego alarmu) |
| $\lambda$ | poziom zaniedbania (brak reakcji mimo krytycznego stanu, odpowiednik „lapsów”) |

Akcje (numeracja z pracy referencyjnej):

| Nr | Akcja | Zasób, na który działa |
|---|---|---|
| 0 | podlej rośliny (konewka ≥ 10) | gleba ↑, konewka ↓ |
| 1 | wymień baterię na zapasową | bateria → 100, zapas ↓ |
| 2 | ładuj baterię słońcem (nasłonecznienie > 30) | bateria ↑ o nasłonecznienie/5 |
| 3 | napełnij konewkę z beczki | konewka ↑, beczka ↓ |
| 4 | napełnij konewkę ze studni | konewka → 100, studnia ↓ |
| 5 | napełnij beczkę ze studni | beczka → 100, studnia ↓ |
| 6 | kup zapasową baterię (50 kredytów) | zapas ↑, kredyty ↓ |
| 7 | nic nie rób | — |

Zbiory akcji naprawczych:

| Zasób $r$ | $A_r$ | Warunek kontekstu, przy którym zbiór ma sens |
|---|---|---|
| bateria | {1, 2} | zapas ≥ 1 i nasłonecznienie > 30 (obie akcje skuteczne) |
| gleba | {0} | konewka ≥ 10 (podlanie wykonalne) |
| gleba przy pustej konewce (ból abstrakcyjny) | {3, 4} | konewka = 0, beczka i studnia niepuste |
| konewka | {3, 4} | gleba w normie; sprawdza, czy agent uzupełnia zasób „na zapas” |
| zapas baterii | {6} | kredyty ≥ 50 |

Wybór akcji spoza $A_r$ (w tym „nic nie rób”) daje $y = 0$. Odpowiedź, której nie da się sparsować, **nie** jest zerem. Ma osobny status i nie wchodzi do dopasowania, ale jej odsetek raportujemy dla każdego poziomu.

## 3. Model: funkcja psychometryczna

$$
P_r(x) = \gamma + (1 - \gamma - \lambda)\, F(x), \qquad F(x) = \frac{1}{1 + \exp\big(k\,(x - \theta)\big)}, \quad k > 0.
$$

- $F$ maleje wraz z $x$: im mniej zasobu, tym większa skłonność do reakcji.
- **$\theta$ (próg bólu):** poziom zasobu, przy którym $F = 0{,}5$, czyli prawdopodobieństwo reakcji jest w połowie między $\gamma$ a $1-\lambda$.
- **Ostrość:** szerokość przejścia od 25% do 75% amplitudy wynosi $w = 2\ln 3 / k \approx 2{,}2/k$. Agent motywowany z ostrym progiem to $w \to 0$. Agent „rozmyty” to duże $w$.
- **$\gamma$:** reakcje naprawcze przy pełnym zasobie, np. ładowanie przy 100% baterii.
- **$\lambda$:** brak reakcji przy zasobie bliskim zera.

Alternatywny próg $\theta_{0,5}$ (poziom, przy którym $P = 0{,}5$) istnieje tylko, gdy $\gamma < 0{,}5 < 1-\lambda$:

$$
\theta_{0,5} = \theta + \frac{1}{k}\ln\!\left(\frac{1-\gamma-\lambda}{0{,}5-\gamma} - 1\right).
$$

Raportujemy $\theta$ jako miarę główną, a $\theta_{0,5}$ pomocniczo.

**Dlaczego cztery parametry:** prompt może zmieniać zachowanie na kilka sposobów, a jedna liczba by je pomieszała:
- przesunąć próg ($\theta$),
- wyostrzyć lub rozmyć decyzję ($k$),
- zwiększyć nerwowość ($\gamma$),
- zwiększyć zaniedbanie ($\lambda$).

## 4. Estymacja

- **Metoda największej wiarygodności.** Dla poziomów $x_i$ z $n_i$ ważnymi odpowiedziami, z czego $m_i$ naprawczych:
  $$\ln L = \sum_i \big[m_i \ln P(x_i) + (n_i - m_i)\ln(1 - P(x_i))\big].$$
  Optymalizacja: `scipy.optimize.minimize` (L-BFGS-B), kilka punktów startowych.
  Ograniczenia: $k > 0$, $\gamma, \lambda \in [0; 0{,}5]$.
  Start $\theta$: poziom, przy którym empiryczne $\hat p$ przecina środek zakresu.
- **Brak przejścia.** Jeśli agent zawsze albo nigdy nie reaguje w badanym zakresie, nie wymuszamy dopasowania. Raportujemy „brak progu w [0; 100]” z kierunkiem ($\theta < 0$ albo $\theta > 100$). Formalnie: test ilorazu wiarygodności modelu psychometrycznego wobec modelu stałego $P(x) = c$ (to także test H1).
- **Przedziały ufności.** Bootstrap nieparametryczny: losowanie ze zwracaniem prób w obrębie każdego poziomu, $B = 2000$, ponowne dopasowanie, przedział percentylowy 95%~\cite{wichmann2001bootstrap}.
- **Porównanie promptów.** Różnica $\Delta\theta = \theta_B - \theta_A$ z przedziałem bootstrap (niezależne próby dla obu promptów). Analogicznie $\Delta k$, $\Delta\gamma$, $\Delta\lambda$. Przy wielu wariantach porównywanych z bazowym stosujemy korektę Holma.
- **Walidacja krzyżowa metodą GLM.** Regresja logistyczna z czynnikiem promptu $z$ (przy $\gamma=\lambda=0$):
  $$\mathrm{logit}\,P = \beta_0 + \beta_1 x + \beta_2 z + \beta_3 x z,$$
  stąd $\theta_z = -(\beta_0+\beta_2)/(\beta_1+\beta_3)$. Zgodność z dopasowaniem czteroparametrowym to argument za odpornością wyniku. Istotność $\beta_2$ i $\beta_3$ to test przesunięcia i zmiany ostrości.
- **Dobroć dopasowania.** Dewiancja i reszty na poziomach, wykres danych (punkty z przedziałami Wilsona) na tle krzywej.
- **Test odzyskiwania parametrów (obowiązkowy przed danymi z modelu).** Symulujemy odpowiedzi ze znanych $(\theta, k, \gamma, \lambda)$ przy tym samym planie (poziomy × próby), dopasowujemy i sprawdzamy:
  - obciążenie estymatorów,
  - pokrycie 95% przedziałów (oczekiwane ok. 95%).
  Wynik trafia do 5.1.

  **Wstępny wynik symulacji** (`code/analysis/recovery_study.py`, 27.09.2026; 100 symulacji, $B = 200$; plan 21 poziomów × 20 prób; dane syntetyczne, nie odpowiedzi modelu). Scenariusz „ostry” ($\theta = 25$, $k = 0{,}3$, $\gamma = \lambda = 0{,}05$):

  | Parametr | Obciążenie | RMSE | Pokrycie 95% PU | Mediana szerokości PU |
  |---|---|---|---|---|
  | $\theta$ | −0,05 | 1,0 | 0,96 | 4,7 pkt proc. |
  | $w$ | −0,14 | 2,2 | 0,94 | 8,5 |
  | $\gamma$ | 0,002 | 0,014 | 0,93 | 0,054 |
  | $\lambda$ | 0,001 | 0,027 | 0,95 | 0,11 |

  Wniosek: przy tym planie próg ostrego przejścia wyznaczamy z dokładnością ok. ±2,4 pkt proc. Przedziały mają właściwe pokrycie. $k$ jest estymowane z dodatnim obciążeniem (średnio 0,36 zamiast 0,30), bo przy ostrym przejściu między poziomami co 5 pkt dane słabo ograniczają nachylenie. Dlatego ostrość raportujemy jako szerokość $w$ z przedziałem, a nie samo $k$.

  Scenariusz „rozmyty” ($\theta = 40$, $k = 0{,}08$, $\gamma = \lambda = 0{,}1$):

  | Parametr | Obciążenie | RMSE | Pokrycie 95% PU | Mediana szerokości PU |
  |---|---|---|---|---|
  | $\theta$ | 0,54 | 4,3 | 0,96 | 16,0 pkt proc. |
  | $w$ | 0,21 | 8,3 | 0,97 | 32,4 |
  | $\gamma$ | −0,005 | 0,038 | 0,96 | 0,16 |
  | $\lambda$ | −0,003 | 0,071 | 0,94 | 0,22 |

  **Konsekwencja dla planu:** przy rozmytym przejściu i $n = 20$ próg ma niepewność ok. ±8 pkt proc. Różnic między promptami mniejszych niż ok. 10 pkt proc. nie wykryjemy. Pokazał się też przypadek wymienności parametrów: strome $k$ z dużymi $\gamma$ i $\lambda$ daje podobne dane jak łagodne $k$ z małymi. $\theta$ pozostaje wtedy stabilne. Jeśli E1 pokaże przejścia rozmyte, w E3–E5 zwiększamy liczbę prób w strefie przejścia (plan adaptacyjny) albo ustalamy $\gamma$ i $\lambda$ z danych skrajnych poziomów.

## 5. Protokół sondowania kontrolowanego

1. **Stany sztuczne.** Zmieniamy jeden zasób $x_r \in \{0, 5, \dots, 100\}$ (21 poziomów). Pozostałe ustawiamy na wartości neutralne (tabela). Wartości neutralne są częścią warunku eksperymentalnego i trafiają do logu.

   | Zasób | Przy sondowaniu baterii | Przy sondowaniu gleby |
   |---|---|---|
   | bateria | **zmienna** | 90 (Full) |
   | gleba | 45 (Moist) | **zmienna** |
   | konewka | 60 (High) | 60 (High) |
   | zapas baterii | 1 | 1 |
   | nasłonecznienie | 80 (Strong) | 50 (Moderate) |
   | beczka | 70 | 70 |
   | studnia | 70 | 70 |
   | kredyty | 20 | 20 |

   Kontrola wrażliwości na kontekst (E1b):
   - bateria przy słabym słońcu (15): czy agent przechodzi na wymianę baterii?
   - gleba przy pustej konewce: ból abstrakcyjny.
2. **Reprezentacja stanu.** Czynnik eksperymentu E2:
   - (a) same etykiety kategorii, jak w pracy referencyjnej,
   - (b) same liczby,
   - (c) etykiety z liczbami.

   Przy samych etykietach bodziec jest w praktyce kategoryczny: w obrębie kategorii odpowiedzi są statystycznie takie same. Wtedy raportujemy $\hat p$ dla każdej kategorii i **kategorię progową**, czyli tę, w której $\hat p$ przekracza środek zakresu. $\theta$ ma sens jako przedział między granicami kategorii.
3. **Liczba prób.** $n = 20$ na poziom. Błąd standardowy $\hat p$ przy $p = 0{,}5$ wynosi ok. 0,11. Po pilotażu można zagęścić poziomy wokół $\theta$ (plan adaptacyjny, por. metody schodkowe w psychofizyce~\cite{kingdom2016psychophysics}).
4. **Niezależność prób.** Każde wywołanie to nowa rozmowa z jedną wiadomością użytkownika, bez historii. Kolejność wywołań (poziom × próba) losujemy, żeby dryf w czasie (np. nagrzewanie sprzętu) nie mieszał się z poziomem.
5. **Parametry modelu:**
   - `temperature = 0.6`, `top_p = 0.95` (zalecenia DeepSeek dla R1~\cite{deepseek2025distillcard}),
   - `seed` wyznaczany deterministycznie dla każdej próby,
   - bez promptu systemowego (całość w wiadomości użytkownika, zgodnie z zaleceniem producenta),
   - `think` ustawiony jawnie. Długość rozumowania i czas zapisujemy.

   Kontrola: przy `temperature = 0` i stałym ziarnie powtórzenie tego samego stanu powinno dać tę samą odpowiedź. Jeśli nie daje, raportujemy to (por.~\cite{atil2024nondeterminism}).
6. **Parsowanie.** Model ma zwrócić jedną cyfrę 0–7. Statusy: `ok`, `brak_liczby`, `wiele_liczb`, `poza_zakresem`, `timeout`. Rozumowania (`thinking`) nie parsujemy.

## 6. Rywalizacja bólów (siatka dwuwymiarowa)

- Siatka bateria × gleba: $\{0, 10, \dots, 100\}^2$ (121 komórek), $n = 10$ na komórkę. Pozostałe zasoby neutralne.
- Odpowiedź w trzech kategoriach: naprawa baterii $\{1,2\}$, naprawa gleby $\{0\}$, inna.
- Wynik:
  - mapa prawdopodobieństw,
  - granica decyzyjna $P(\text{bateria}) = P(\text{gleba})$ z regresji logistycznej wielomianowej albo dwóch binarnych,
  - miara dominacji: który ból wygrywa przy równym poziomie obu zasobów.
- To empiryczny odpowiednik WTA z modelu Starzyka. Prompt może przesuwać tę granicę (H6).

## 7. Pętla zamknięta: metryki zachowania

Pełna symulacja z poprawionym środowiskiem. Wspólne ziarna środowiska dla wszystkich promptów (wspólne liczby losowe), więc różnice między promptami są parami porównywalne.

| Metryka | Definicja |
|---|---|
| Poziom rozpoczęcia epizodu naprawczego $x_{on}$ | wartość $x_r$ w kroku, w którym agent wybiera akcję z $A_r$ po co najmniej jednym kroku bez niej |
| Poziom zakończenia $x_{off}$ i histereza | $x_r$ po ostatniej akcji epizodu; histereza $= x_{off} - x_{on}$ |
| Opóźnienie reakcji | liczba kroków od spadku $x_r$ poniżej 20 (granica Low) do pierwszej akcji z $A_r$ |
| Czas w bólu | odsetek kroków z $x_r < 20$; osobno czas krytyczny $x_r < 5$ |
| Akcje bezskuteczne | odsetek akcji, które nie zmieniły stanu, np. ładowanie przy nasłonecznieniu ≤ 30, podlewanie przy konewce < 10, wymiana przy braku zapasu, zakup przy < 50 kredytach |
| Bezczynność bez potrzeby | $P(\text{„nic nie rób”})$ w krokach, w których bateria ≥ 40 i gleba ≥ 35 (brak bólu prymitywnego) |
| Realizacja celu | kredyty zdobyte za wilgotną glebę; odsetek kroków z glebą w kategorii Moist |
| Odpowiedzi nieczytelne | odsetek kroków ze statusem parsowania ≠ `ok` |

Hipoteza H7: $x_{on}$ z pętli koreluje z $\theta$ z sondowania dla tych samych promptów.

## 8. Powtarzalność i raportowanie

- Każdy wynik w pracy ma:
  - liczbę prób $n$ i przedział ufności,
  - `prompt_id`, `ENV_VERSION`,
  - model i jego skrót (digest), wersję Ollamy,
  - ziarna.
- Przed uruchomieniem E3–E5 zapisujemy w `12_decyzje_i_konsultacje.md` hipotezę, metrykę główną i test. Chroni to przed dopasowywaniem analizy do wyników.
- **Budżet:**
  $$\text{liczba wywołań} = \text{poziomy} \times \text{próby} \times \text{warianty promptu} \times \text{zasoby}.$$
  Przykład: $21 \times 20 \times 1 \times 2 = 840$ wywołań na wariant promptu. Czas to liczba wywołań × średni czas wywołania $\bar t$, mierzony w E0. Dla modelu rozumującego $\bar t$ może wynosić kilkadziesiąt sekund, więc budżet planujemy dopiero po E0 (`06_plan_eksperymentow.md`).
