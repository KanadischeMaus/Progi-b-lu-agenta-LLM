# Temat i cel pracy

> Status: wersja robocza. Pytania badawcze i hipotezy wymagają akceptacji promotora. Po akceptacji wpisz datę w `12_decyzje_i_konsultacje.md`.

## Metryczka

| | |
|---|---|
| Tytuł | Wpływ promptu na progi bólu agenta LLM |
| Tytuł angielski (propozycja) | The Influence of Prompt Wording on the Pain Thresholds of an LLM Agent |
| Autor | [Imię Nazwisko], [nr albumu] |
| Promotor | dr inż. Marcin Kowalik, prof. PRz |
| Jednostka | Politechnika Rzeszowska, Wydział Matematyki i Fizyki Stosowanej |
| Kierunek | Inżynieria i Analiza Danych, studia II stopnia |
| Rok akademicki | 2026/2027 |
| Język pracy | polski (streszczenie PL i EN) |

## Opis tematu (od promotora, dosłownie)

> Celem pracy jest zbadanie wpływu sposobu formułowania promptu na mechanizmy motywacyjne warunkujące zachowanie agenta opartego na dużym modelu językowym (LLM) w wybranym środowisku decyzyjnym. W szczególności analiza ma wykazać, w jakim stopniu treść i konstrukcja promptu zmienia wartości progów bólu, którymi agent LLM kieruje się podczas podejmowania decyzji w stanach środowiska uznawanych za niepożądane z punktu widzenia realizowanego celu. W przyjętym modelu ból agenta jest związany z jego stanem wewnętrznym oraz dostępnością zasobów środowiska niezbędnych do osiągnięcia zamierzonego celu.

Dodatkowe wskazanie promotora: środowisko i pętla agenta są gotowe. Do dopracowania jest sposób mierzenia „zachowania” agenta. Na tej podstawie badamy prompty. Kod istnieje wyłącznie jako listingi w pracy referencyjnej. Odtworzono go w `code/` (`05_srodowisko_i_kod.md`).

## Kontekst

- **Praca referencyjna (Zawiślak 2025):**
  - Agent ogrodowy sterowany przez `deepseek-r1:14b`, 8 akcji, 2 potrzeby prymitywne (bateria, wilgotność gleby).
  - Dwa warianty promptu, po jednym przebiegu po 1000 iteracji.
  - Wniosek jakościowy: agent reaguje na stany krytyczne „zgodnie z mechanizmem progu bólu”.
  - Progu nie wyznaczono liczbowo. Szczegóły i znalezione problemy: `07_analiza_pracy_referencyjnej.md`.
- **Praca Kingi (2026/2027):** kontynuacja badań. Zakres i rozgraniczenie z tą pracą: `\dower{do ustalenia z promotorem}`.
- **Ta praca:** przechodzi od obserwacji jakościowej do pomiaru. Próg bólu staje się parametrem estymowanym z danych, z niepewnością, a prompt jest zmienną niezależną.

## Problem badawczy

Agent LLM nie ma jawnie zaprogramowanego progu bólu, w przeciwieństwie do agenta motywowanego Starzyka~\cite{starzyk2017needs}. Próg ujawnia się dopiero w zachowaniu: przy jakim poziomie zasobu agent zaczyna reagować działaniem naprawczym. Nie wiadomo:
- czy ten próg jest ostry (przełączenie skokowe) czy rozmyty,
- jak bardzo zależy od sformułowania promptu,
- czy prompt przesuwa próg, zmienia jego ostrość, czy tylko zwiększa szum decyzji.

Literatura pokazuje dużą wrażliwość LLM na drobne zmiany promptu~\cite{sclar2024quantifying, salinas2024butterfly}, ale brakuje pomiarów tej wrażliwości w kategoriach progów motywacyjnych.

## Cel główny

Opracować metodę pomiaru progów bólu agenta LLM i zastosować ją do ilościowej oceny, jak treść i konstrukcja promptu zmieniają te progi w środowisku ogrodowym.

## Cele szczegółowe

- **C1. Operacjonalizacja.** Zdefiniować ból, akcję naprawczą i próg bólu tak, żeby dało się je mierzyć w zachowaniu agenta LLM (`04_metodologia_pomiaru.md`).
- **C2. Narzędzie pomiarowe.** Zbudować moduł sondowania kontrolowanego i logowania oraz procedurę dopasowania funkcji psychometrycznej z przedziałami ufności.
- **C3. Poprawa środowiska.** Usunąć błędy wpływające na powtarzalność (temperatura, ziarno, parsowanie) i udokumentować wersję środowiska.
- **C4. Eksperymenty z promptem.** Zmierzyć wpływ wybranych czynników promptu na parametry progu ($\theta$, $k$, $\gamma$, $\lambda$).
- **C5. Walidacja.** Sprawdzić, czy progi z sondowania przewidują zachowanie w pełnej pętli symulacji.
- **C6. Interpretacja.** Odnieść wyniki do modelu uczenia motywowanego (ból prymitywny i abstrakcyjny, rywalizacja bólów) i do literatury o wrażliwości LLM na prompt.

## Pytania badawcze i hipotezy robocze

| | Pytanie | Hipoteza robocza | Eksperyment |
|---|---|---|---|
| PB1 | Czy agent LLM przełącza się na akcję naprawczą progowo? | H1: prawdopodobieństwo akcji naprawczej maleje sigmoidalnie wraz z poziomem zasobu; nachylenie $k$ istotnie > 0 | E1 |
| PB2 | Czy próg zadany w prompcie przesuwa próg zmierzony? | H2: $\theta$ rośnie monotonicznie z zadanym progiem $X$; zależność nie musi być 1:1 | E3 |
| PB3 | Czy ramowanie promptu (neutralne, ból, zagrożenie, nagroda) zmienia próg i ostrość? | H3: ramowanie zagrożeniem przesuwa $\theta$ w górę (wcześniejsza reakcja) i zwiększa $\gamma$ (reakcje bez potrzeby) | E4 |
| PB4 | Czy sposób przedstawienia stanu (etykiety, liczby, oba) zmienia próg? | H4: przy samych etykietach przełączenie skupia się na granicach kategorii; liczby dają gładszą krzywą | E2 |
| PB5 | Czy wskazówki zachowania w prompcie (pole `behavior`) zmieniają próg? | H5: wskazówki zmniejszają rozrzut i przesuwają $\theta$ w stronę progów zapisanych we wskazówkach | E5 |
| PB6 | Jak prompt zmienia hierarchię bólów przy jednoczesnym niedoborze dwóch zasobów? | H6: granica decyzyjna bateria–gleba przesuwa się zgodnie z celem akcentowanym w prompcie | E7 |
| PB7 | Czy progi z sondowania przewidują zachowanie w pętli zamkniętej? | H7: $\theta$ z sondowania koreluje z poziomem zasobu na początku epizodów naprawczych | E8 |

Plan eksperymentów E0–E9: `06_plan_eksperymentow.md`.

## Zakres

**W zakresie:**
- środowisko ogrodowe z pracy referencyjnej (poprawione, wersjonowane),
- jeden model główny (`deepseek-r1:14b` przez Ollamę), opcjonalnie drugi model do porównania,
- ból prymitywny (bateria, wilgotność gleby), ból abstrakcyjny w wersji ograniczonej (woda w konewce, zapasowe baterie),
- analiza statystyczna z przedziałami ufności.

**Poza zakresem:**
- trenowanie i dostrajanie modeli,
- porównanie wielu modeli komercyjnych,
- rozważania o tym, czy model „odczuwa” ból. Ból traktujemy funkcjonalnie, jako sygnał niedoboru zasobu. Zaznaczamy to w pracy, żeby uniknąć antropomorfizacji (por.~\cite{sharkey2025could, shanahan2023role, butlin2026identifying, keeling2024can}).

## Wkład własny (do sformułowania we wstępie)

1. Operacjonalizacja progu bólu agenta LLM jako parametru funkcji psychometrycznej.
2. Narzędzie sondowania i logowania, które pozwala mierzyć próg z niepewnością.
3. Odtworzenie środowiska referencyjnego z listingów, jego korekta i wersjonowanie, w tym udokumentowanie błędów wpływających na powtarzalność.
4. Wyniki eksperymentów pokazujące, które elementy promptu przesuwają próg, a które zmieniają jego ostrość.

## Pytania do promotora

1. Czy akceptuje Pan definicję progu jako punktu środkowego funkcji psychometrycznej (`04`)?
2. Jaki jest podział zakresu z pracą Kingi (środowisko, metryki, prompty)?
3. Czy limit objętości WMiFS (15–50 stron znormalizowanych, bez załączników) obowiązuje ściśle? Praca referencyjna ma ponad 80 stron.
4. Czy wymagany jest drugi model do porównania, czy wystarczy jeden?
5. Na jakim sprzęcie liczymy (własny Mac, serwer uczelni, Colab)? Od tego zależy budżet eksperymentów.
6. Kolejność bibliografii: alfabetyczna (poradnik Biblioteki PRz, do którego odsyła szablon) czy według pierwszego cytowania? Szablon tego nie określa.
