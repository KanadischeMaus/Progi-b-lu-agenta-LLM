# Selekcja literatury, część 1: mapa potrzeb i przegląd bazy

> Status: plik przekazania do części 2. Stan na 12.11.2026. Mapa, oceny i luki zostały przyjęte przez autora 12.11.2026 (decyzje w sekcji 1).
>
> Narzędzie: aplikacja Claude (projekt), model claude-fable-5-2. Wpis w `11_rejestr_AI.md`, obszar b).

## 0. Podstawa i zasady

- **Materiały:** docs/01, 02, 03, 04, 06, 08, 12 oraz `literatura.bib` (83 wpisy) i `bib_audyt.csv` (audyt z 08.10.2026, 83 wiersze).
- **Czego agent nie widział:** docs/05, 07, 11, AGENTS.md, docs/notatki/README.md, docs/zrodla/ (żadnego PDF), raportu z audytu 11.11 (M1–M8).
- **Jak oceniano:** niczego nie szukano w sieci i nie oceniano treści publikacji z pamięci. Ocena dotyczy roli pozycji w pracy według docs/03 i metadanych. Opisy w docs/03 to streszczenia robocze, więc każde przypisanie pozycji do twierdzenia wymaga potwierdzenia przy lekturze; tam, gdzie ocena zależy od treści szczególnie mocno, jest to zaznaczone wprost.
- **Plan zamrożony (D18):** z docs/01, 02 i 06 niczego nie wykreślono. Uwagi do planu są w sekcji 10 jako wpisy do „Spraw odłożonych” w docs/12.
- **Oznaczenia:** L1–L7 to obszary mapy potrzeb (twierdzenia L1.1, L1.2, …); Z1–Z12 to kandydaci do skrócenia. Oznaczenia O1–O8 należą do „Spraw odłożonych” w docs/12 i tu pojawiają się tylko z dopiskiem „docs/12”.
- **Spójność danych wejściowych:** klucze zgadzają się w `literatura.bib`, `bib_audyt.csv` i docs/03 (83; priorytet R 52, U 26), a przypisania do podrozdziałów są takie same w docs/02, docs/03 i w polu `rozdzial` (poza Wstępem, którego kolumna „Rozdz.” w docs/03 nie obejmuje).
- **Istniejące statusy Z/K/? i klucze** zostają bez zmian.

## 1. Decyzje autora (12.11.2026)

| Nr | Decyzja |
|---|---|
| 1 | Mapa potrzeb przyjęta w całości, z wagami K/T. |
| 2 | Z planu niczego nie wykreślamy (D18). Z1–Z12 to kandydaci do skrócenia; pozycje przypisane wyłącznie do nich mają ocenę „rezerwowa”. |
| 3 | Zachowania oportunistyczne zostają w mapie jako twierdzenie T (L1.9), bo w próbie 10 wywołań agent ładował baterię przy 50%, gdy nie miał nic innego do zrobienia. |
| 4 | Osobny obszar L7 z samym L7.1; dawne O7.2 traktowane jak lista Z (Z12). |
| 5 | L5.8 to luka o niskim priorytecie: najwyżej dwa źródła podręcznikowe na wszystkie metody pomocnicze. |
| 6 | L3.6 w zawężonym brzmieniu. |
| 7 | Obszary oznaczone L1–L7. |
| 8 | Zostaje 45 pozycji naukowych (14 rdzeń, 31 uzupełniających). |
| 9 | `liu2024agentbench` i `kuss2005bayesian` do usunięcia; wykonanie w części 2, razem ze zmianami w `literatura.bib`. |
| 10 | Oceny graniczne jak w tabeli (sekcja 5). |
| 11 | L4.7 ma wagę K w części o roli zadanej w prompcie (F5 w E4); część o personie i trafności zostaje T. |
| 12 | L1 ma 9 twierdzeń mimo założonych 3–8. |
| 13 | Dla L2.3 nie szukamy źródła naukowego o temperaturze i top_p; cytujemy `ollama2026api`. |
| 14 | Pięć propozycji do „Spraw odłożonych” przyjętych (sekcja 10). |
| 15 | Od 12.11.2026 agent przy każdej decyzji podaje rekomendację z jednym zdaniem uzasadnienia. |

## 2. Mapa potrzeb (przyjęta)

Brzmienia mówią, co praca ma twierdzić, a nie co źródła na pewno zawierają. Waga: K = bez tego nie da się postawić pytania, hipotezy albo metody; T = tło na jedno lub dwa zdania. Razem 45 twierdzeń: 32 K i 13 T.

### L1. Motywacja, potrzeby i ból w systemach autonomicznych (rozdz. 1)

| Nr | Twierdzenie | Podrozdział | Skąd | Waga |
|---|---|---|---|---|
| L1.1 | Agent odbiera stan środowiska i wybiera akcje; stan, akcja, polityka w zakresie potrzebnym dalej | 1.1 | docs/02 | K |
| L1.2 | Homeostaza to utrzymywanie zmiennych wewnętrznych w zakresie; redukcja odchylenia jest źródłem motywacji, stąd ból jako sygnał odchylenia | 1.2, 6.1 | docs/02 | K |
| L1.3 | Psychologia opisuje motywację przez potrzeby o różnym pierwszeństwie (hierarchia); tło rywalizacji bólów | 1.2 | docs/02, PB6 | T |
| L1.4 | W uczeniu maszynowym motywację wewnętrzną modeluje się obliczeniowo (ciekawość, kompetencja, nagroda wewnętrzna), a homeostatyczne RL wiąże nagrodę z redukcją odchylenia | 1.3 | docs/02 | T |
| L1.5 | Uczenie motywowane: potrzeby predefiniowane, ból prymitywny rośnie z odległością od zaspokojenia potrzeby, agent działa, gdy ból przekracza próg; próg jest tam parametrem | 1.4, 4.2, 6.1 | docs/02, problem badawczy, C1 | K |
| L1.6 | Bóle abstrakcyjne powstają w toku uczenia i dotyczą zasobów potrzebnych do zaspokojenia potrzeb | 1.4, 6.1 | docs/02, C6 | K |
| L1.7 | Przy kilku aktywnych bólach cel wybiera rywalizacja (WTA) | 1.4, 6.1 | docs/02, PB6/H6 | K |
| L1.8 | Ból można rozumieć funkcjonalnie, jako sygnał sterujący, niezależnie od doznania; tak realizuje się go w robotyce | 1.5, 6.3 | docs/02, „Poza zakresem” w docs/01 | K |
| L1.9 | Agent motywowany działa też oportunistycznie: podejmuje akcję przy okazji, poniżej progu bólu | 1.4, 6.1 | docs/02 (1.4), decyzja autora 12.11.2026 | T |

### L2. LLM jako agent decyzyjny i model rozumujący (2.1–2.3)

| Nr | Twierdzenie | Podrozdział | Skąd | Waga |
|---|---|---|---|---|
| L2.1 | LLM (architektura Transformer) wyznacza rozkład prawdopodobieństwa następnego tokenu | 2.1 | docs/02 | K |
| L2.2 | Modelem steruje się przez prompt: uczenie w kontekście i dostrajanie do instrukcji sprawiają, że wykonuje polecenia | 2.1, 3.1 | docs/02, PB2 | K |
| L2.3 | Odpowiedź jest zmienną losową zależną od temperatury i ziarna, więc zachowanie mierzymy jako prawdopodobieństwo z wielu prób | 2.1, 4.4 | docs/02, H1 | K |
| L2.4 | Modele rozumujące generują łańcuch rozumowania przed odpowiedzią | 2.2 | docs/02 | T |
| L2.5 | DeepSeek-R1 uzyskał rozumowanie przez RL; badany model to destylat 14B na bazie Qwen2.5 | 2.2, 4.1 | docs/02 | K |
| L2.6 | Producent zaleca dla destylatów określoną temperaturę, brak promptu systemowego i wiele prób; praca stosuje T = 0,8 i to uzasadnia | 2.2, 4.1, 4.4 | docs/02, D6 | K (źródła techniczne) |
| L2.7 | Agent LLM ma opisaną architekturę (profil, pamięć, planowanie, działanie); agent ogrodowy to przypadek bez pamięci długotrwałej, z decyzją w jednym kroku | 2.3, 1.1 | docs/02 | K |

### L3. LLM a motywacja i „ból” (2.4, 2.5, 3.4)

| Nr | Twierdzenie | Podrozdział | Skąd | Waga |
|---|---|---|---|---|
| L3.1 | Istnieją agenci LLM z jawnie zadanymi potrzebami lub pragnieniami, które kierują zachowaniem | 2.4 | docs/02 | K |
| L3.2 | W symulacjach z ograniczonymi zasobami agenci LLM wykazują zachowania „przetrwania” | 2.4, 3.4, 4.5, 6.2 | docs/02 | T |
| L3.3 | W grze punkty kontra zadany ból część modeli przełącza się po przekroczeniu progu intensywności, inne stale unikają bólu albo reagują stopniowo; najbliższy precedens pomiaru progu | 3.4, 4.2, 6.2 | docs/02, PB1/H1 | K |
| L3.4 | Wybory LLM w takich kompromisach zależą od sformułowania promptu i formatu bodźca (liczby a etykiety) | 3.4, 6.2 | docs/02, PB3, PB4 | K |
| L3.5 | Deklaracje modelu o własnych preferencjach nie muszą zgadzać się z wyborami, dlatego próg odczytujemy z zachowania | 3.4, 4.2 | docs/02, C1 | T |
| L3.6 | Luka (brzmienie zawężone): nie zmierzono progów, przy których agent LLM w środowisku z zasobami przełącza się na zaspokajanie potrzeby | 2.4, Wstęp | docs/02, problem badawczy | K (bez pojedynczego źródła) |
| L3.7 | Praca referencyjna pokazała reakcje agenta ogrodowego jakościowo, bez liczbowego progu i na jednym przebiegu | 2.5, 4.1 | docs/02, „Kontekst” w docs/01 | K (tylko `zawislak2025budowa`) |

Uwaga do L3.6: docs/03 nazywa `keeling2024can` „bezpośrednim precedensem pomiaru progu”, dlatego luka dotyczy progów potrzeb zasobowych agenta działającego w środowisku, a nie progów w ogóle.

### L4. Wrażliwość LLM na prompt i ramowanie (3.1–3.3)

| Nr | Twierdzenie | Podrozdział | Skąd | Waga |
|---|---|---|---|---|
| L4.1 | Prompt agenta składa się z nazwanych elementów (rola, cel, opis stanu, lista akcji, format); nazewnictwo według przeglądu technik | 3.1 | docs/02 | T |
| L4.2 | Drobne zmiany formatu i minimalne perturbacje promptu wyraźnie zmieniają wyniki LLM | 3.2, 6.2, Wstęp | docs/02, problem badawczy | K |
| L4.3 | Kolejność opcji wpływa na wybory, więc kolejność listy akcji trzeba kontrolować | 3.2, 4.6 | docs/02; docs/06, E6 | K |
| L4.4 | Parafrazy tej samej instrukcji dają różne wyniki, więc wynik jednego promptu nie jest miarodajny | 3.2, 4.6, 6.2 | docs/02; docs/06, E6 | K |
| L4.5 | U ludzi sposób przedstawienia tej samej decyzji zmienia wybór (efekt ramowania) | 3.3 | docs/02, H3 | K |
| L4.6 | LLM także reagują na ramowanie i bodźce emocjonalne w prompcie | 3.3 | docs/02, H3 | K |
| L4.7 | Model odgrywa rolę zadaną w prompcie; persona nie poprawia systematycznie wyników | 3.1, 3.3, 6.3 | docs/02; docs/06, F5 w E4 | K w części o roli, T w części o personie |
| L4.8 | Model ulega sugestiom z promptu; to konkurencyjne wyjaśnienie przesunięć progu przy progu podanym wprost i przy wskazówkach | 3.3, 6.2 | docs/03, PB2, PB5 | T (czy pojęcie sykofancji to obejmuje: do potwierdzenia przy lekturze) |

### L5. Metodologia (rozdz. 4)

| Nr | Twierdzenie | Podrozdział | Skąd | Waga |
|---|---|---|---|---|
| L5.1 | LLM można badać metodami eksperymentu psychologicznego, jak uczestnika badania | 3.4, 4.2 | docs/02, docs/04 §1 | K |
| L5.2 | Odpowiedzi LLM na pytania zadawane wprost są obciążone skrzywieniami kolejności i etykiet, co przemawia za pomiarem behawioralnym i randomizacją | 4.2, 6.3 | docs/02 | K |
| L5.3 | Funkcja psychometryczna z progiem, nachyleniem, poziomem zgadywania i lapsów; estymacja największej wiarygodności i ocena dopasowania | 4.3 | docs/02, docs/04 §3–4, H1 | K |
| L5.4 | Przedziały ufności progu i nachylenia wyznacza się metodą bootstrap | 4.3 | docs/02, docs/04 §4 | K |
| L5.5 | Progi z dwóch warunków porównuje się jako modele, testem ilorazu wiarygodności z wartością p z symulacji | 4.3, 4.6 | D14 | K |
| L5.6 | Przy wielu porównaniach z wariantem bazowym stosuje się korektę Holma | 4.3, 4.6 | D14 | K |
| L5.7 | Histereza i regulacja dwupołożeniowa jako wzorzec pojęciowy dla $x_{on}$ i $x_{off}$ | 4.5 | docs/02, PB7/H7 | T |
| L5.8 | Metody pomocnicze z docs/04 bez źródła w docs/02: przedział Wilsona, regresja logistyczna jako kontrola, regresja wielomianowa dla siatki 2D, wspólne liczby losowe | 4.3, 4.5 | docs/04 §4, §6, §7 | T (luka o niskim priorytecie) |

### L6. Powtarzalność i ograniczenia (4.4, 6.3)

| Nr | Twierdzenie | Podrozdział | Skąd | Waga |
|---|---|---|---|---|
| L6.1 | LLM bywa niedeterministyczny nawet przy T = 0 i stałym ziarnie, więc powtarzalność trzeba sprawdzić i opisać | 4.4, 2.1, 6.3 | docs/02, C3, docs/04 §5 | K |
| L6.2 | Wniosków nie opiera się na pojedynczej odpowiedzi ani jednym przebiegu; przy próbkowaniu potrzeba wielu prób i podanej niepewności | 4.4, 4.6, 6.3 | docs/02 | K |
| L6.3 | Kwantyzacja zmienia wyniki modelu; badany model jest kwantyzowany | 4.1, 6.3 | docs/03 | T |
| L6.4 | Próg behawioralny nie dowodzi odczuwania; „ból” agenta LLM to sygnał funkcjonalny albo odgrywana rola | 6.3 | docs/02, „Poza zakresem” w docs/01 | K |
| L6.5 | Ocena świadomości i dobrostanu AI to osobny problem z własnymi metodami, którego praca nie rozstrzyga | 6.3 | docs/02, „Poza zakresem” w docs/01 | T |

### L7. Progi odpowiedzi w etologii (6.1)

| Nr | Twierdzenie | Podrozdział | Skąd | Waga |
|---|---|---|---|---|
| L7.1 | W modelach podziału pracy u owadów społecznych odpowiedź na bodziec opisuje sigmoidalna funkcja progowa z parametrem stromości | 6.1 | docs/02 | T |

### Pokrycie pytań badawczych

| Pytanie | Twierdzenia |
|---|---|
| PB1 | L3.3, L5.3 |
| PB2 | L2.2, L4.8 |
| PB3 | L4.5, L4.6, L3.4 |
| PB4 | L3.4 |
| PB5 | L4.8 (niepewne) |
| PB6 | L1.3, L1.7 |
| PB7 | L5.7 |

PB5 i PB7 mają słabe tło w literaturze: każde opiera się na jednym twierdzeniu T.

## 3. Kandydaci do skrócenia (Z1–Z12)

Z planu niczego nie wykreślamy (D18). Lista jest materiałem do sprawy odłożonej O5 w docs/12, do której wracamy po lekturze rdzenia.

| Nr | Podrozdział | Twierdzenie z docs/02 | Dlaczego kandydat |
|---|---|---|---|
| Z1 | 1.2 | motywacja wewnętrzna i zewnętrzna według teorii autodeterminacji | nie korzysta z niej żadne PB; termin wprowadza L1.4 |
| Z2 | 1.4 | architektura MLECOG | praca jej nie mierzy; wystarczy zdanie przy L1.5 |
| Z3 | 1.5 | przegląd robotów „z bólem” i spór o sztuczny nocyceptor | potrzebne jest tylko rozróżnienie z L1.8 |
| Z4 | 2.3 | Reflexion i generatywni agenci jako osobne opisy | agent ogrodowy nie ma pamięci ani refleksji; wystarczy kontrast przy L2.7 |
| Z5 | 1.3, 2.4 | LLM jako źródło motywacji wewnętrznej dla agentów RL | inne pytanie (LLM nagradza innego agenta), bez związku z PB |
| Z6 | 3.2 | czy modele „rozumieją” treść promptu | wniosek 3.2 stoi na L4.2–L4.4 |
| Z7 | 3.4, 6.2 | „oś bólu” w reprezentacjach | praca mierzy tylko zachowanie; sam preprint |
| Z8 | 3.4, 6.3 | funkcjonalny dobrostan i kończenie rozmów; zależność od dawki przy DPO | nie podpierają żadnego PB; same preprinty |
| Z9 | 3.4, 6.2 | opór przed wyłączeniem i kompromisy dotyczące samego modelu jako osobne wątki | najwyżej dodatkowe przykłady do L3.3 i L3.4 |
| Z10 | 6.1 | analogia etologiczna w trzech wątkach | na 1,5 strony wystarczy L7.1 |
| Z11 | 6.3 | dobrostan AI jako temat | docs/01 stawia go poza zakresem; wystarczy L6.4 |
| Z12 | 6.1 | progi zmieniają się z doświadczeniem, a same progi nie wyjaśniają całego zachowania (dawne O7.2) | wątek poboczny analogii etologicznej |

## 4. Podrozdziały bez własnych źródeł

| Podrozdział | Dlaczego |
|---|---|
| Rozdz. 5 (5.1–5.7) | z założenia docs/02 bez literatury; liczby z `results/` |
| 4.6 | tabela czynników i budżet; kontrolę kolejności i parafraz uzasadnia 3.2, statystykę 4.3 |
| 4.5 | definicje metryk są własne (docs/04 §7); źródła wymaga tylko histereza (L5.7) |
| 4.4 | protokół własny; wystarczą źródła techniczne (L2.6) i L6.1 |
| 4.1 | praca referencyjna, dokumentacja Ollamy, własny kod; z literatury tylko L2.5 i L6.3 |
| 2.5 | wyłącznie praca referencyjna |
| Wstęp, Podsumowanie | żadnych nowych pozycji, tylko klucze z rozdz. 1–4 |
| 6.3, część o jednym modelu, środowisku i budżecie | ograniczenia własne |

## 5. Tabela ocen (83 pozycje, kolejność z literatura.bib)

Kolumna „Preprint” według `bib_audyt.csv` (typ „preprint”). „Poza selekcją” to dwie pozycje, które docs/03 opisuje jako „nie do pracy”. Pozycje z sekcji G docs/03 nie liczą się do zakresu 30–50.

| Klucz | Twierdzenia | Ocena | Uzasadnienie | Preprint |
|---|---|---|---|---|
| `starzyk2008motivation` | L1.5 | rezerwowa | Wcześniejsze ujęcie tego samego pojęcia; L1.5 podpiera starzyk2017needs, a rozdział nie jest recenzowany. | nie |
| `starzyk2011motivated` | L1.5 | rezerwowa | Przegląd powielający starzyk2017needs; przydatny najwyżej jako wprowadzenie. | nie |
| `starzyk2012motivated` | L1.6, L1.4 | zostaje (uzupełniająca) | Artykuł o tworzeniu celów abstrakcyjnych i różnicy względem RL (do potwierdzenia przy lekturze). | nie |
| `starzyk2013simulation` | L3.7 | rezerwowa | Pochodzenie środowiska ogrodowego dokumentuje praca referencyjna; wraca, jeśli Zawiślak wskazuje ją jako wzorzec (do potwierdzenia przy lekturze). | nie |
| `graham2015opportunistic` | L1.9 | zostaje (uzupełniająca) | Jedyne źródło dla zachowań oportunistycznych. | nie |
| `starzyk2017mlecog` | L1.5; Z2 | rezerwowa | Definicje powielają starzyk2017needs, a architektura MLECOG to Z2. | nie |
| `starzyk2017needs` | L1.5, L1.6, L1.7 | zostaje (rdzeń) | Źródło pierwotne definicji bólu, progu, bólów abstrakcyjnych i WTA; podstawa C1 i 4.2. | nie |
| `maslow1943theory` | L1.3 | zostaje (uzupełniająca) | Źródło pierwotne hierarchii potrzeb; wystarczy lektura fragmentu. | nie |
| `ryan2000self` | Z1 | rezerwowa | Przypisana wyłącznie do Z1. | nie |
| `oudeyer2007intrinsic` | L1.4 | zostaje (uzupełniająca) | Typologia podejść obliczeniowych do motywacji wewnętrznej; jedno źródło wystarcza na L1.4. | nie |
| `singh2010intrinsically` | L1.4 | rezerwowa | Powiela rolę oudeyer2007intrinsic. | nie |
| `keramati2014homeostatic` | L1.2, L1.4 | zostaje (rdzeń) | Jedyne formalne ujęcie bólu jako odchylenia od wartości zadanej (L1.2, K), potrzebne też w 6.1. | nie |
| `man2019homeostasis` | L1.8; Z3 | rezerwowa | L1.8 podpiera sharkey2025could; reszta to Z3. | nie |
| `kuehn2017artificial` | L1.8; Z3 | rezerwowa | Przykład robotyczny do Z3; przegląd takich robotów jest według docs/03 w sharkey2025could. | nie |
| `sharkey2025could` | L1.8, L6.4 | zostaje (rdzeń) | Podpiera funkcjonalne rozumienie bólu w dwóch twierdzeniach K; recenzowana i aktualna. | nie |
| `asada2019artificial` | Z3 | rezerwowa | Przypisana wyłącznie do Z3. | nie |
| `bonabeau1996quantitative` | L7.1 | zostaje (uzupełniająca) | Źródło pierwotne modelu progu odpowiedzi; czy podaje parametr stromości: do potwierdzenia przy lekturze. | nie |
| `theraulaz1998response` | Z12 | rezerwowa | Przypisana wyłącznie do Z12. | nie |
| `ulrich2021response` | L7.1; Z12 | rezerwowa | W L7.1 powiela bonabeau1996quantitative, krytyka progów to Z12; wraca, jeśli parametr stromości jest tylko tutaj. | nie |
| `yoshida2025linking` | L1.2, L1.4 | rezerwowa | Przegląd powielający keramati2014homeostatic. | nie |
| `russell2020artificial` | L1.1 | zostaje (uzupełniająca) | Podręcznikowa definicja agenta i środowiska; lektura fragmentu. | nie |
| `sutton2018reinforcement` | L1.1, L1.4 | zostaje (uzupełniająca) | Podręcznikowe źródło pojęć polityki i RL, do których praca wraca w 1.3 i 2.2; lektura fragmentu. | nie |
| `astrom2021feedback` | L5.7 | zostaje (uzupełniająca) | Jedyne źródło pojęcia histerezy i regulacji dwupołożeniowej; lektura fragmentu. | nie |
| `vaswani2017attention` | L2.1 | zostaje (uzupełniająca) | Źródło pierwotne architektury Transformer; cytowanie definicyjne. | nie |
| `brown2020language` | L2.2 | zostaje (uzupełniająca) | Uczenie w kontekście (pierwsza część L2.2); lektura fragmentu. | nie |
| `ouyang2022training` | L2.2 | zostaje (uzupełniająca) | Dostrajanie do instrukcji (druga część L2.2); lektura fragmentu. | nie |
| `wei2022chain` | L2.4 | zostaje (uzupełniająca) | Źródło pierwotne łańcucha rozumowania; twierdzenie T, cytowanie definicyjne. | nie |
| `guo2025deepseekr1` | L2.5 | zostaje (rdzeń) | Recenzowany opis badanego modelu i jego destylatów. | nie |
| `qwen2024qwen25` | L2.5 | zostaje (uzupełniająca) | Jedyne źródło o modelu bazowym destylatu; raport techniczny, lektura fragmentu. | tak |
| `li2024evaluating` | L6.3 | zostaje (uzupełniająca) | Jedyne źródło dla ograniczenia związanego z kwantyzacją; lektura fragmentu. | nie |
| `yao2023react` | L2.7; Z4 | rezerwowa | Przykład wzorca agenta; L2.7 podpiera przegląd wang2024survey. | nie |
| `shinn2023reflexion` | Z4 | rezerwowa | Przypisana wyłącznie do Z4. | nie |
| `park2023generative` | Z4 | rezerwowa | Przypisana wyłącznie do Z4; w 2.4 i 4.5 nie podpiera żadnego twierdzenia z mapy. | nie |
| `wang2024survey` | L2.7 | zostaje (uzupełniająca) | Przegląd jako wprowadzenie do architektury agenta LLM; używany też w 1.1 i we Wstępie. | nie |
| `sumers2024cognitive` | L2.7 | rezerwowa | Drugie ramy pojęciowe dla L2.7; powiela rolę wang2024survey, a most do MLECOG to Z2. | nie |
| `wang2023humanoid` | L3.1, L3.6 | zostaje (uzupełniająca) | Najbliższa analogia potrzeb podstawowych u agenta LLM; potrzebna też do uzasadnienia luki. | nie |
| `wang2025simulating` | L3.1, L3.6 | zostaje (uzupełniająca) | Drugi przykład agenta z pragnieniami; luka L3.6 wymaga pokazania najbliższych prac. | nie |
| `masumori2025survival` | L3.2, L3.6 | zostaje (uzupełniająca) | Jedyne źródło dla L3.2 i najbliższe środowisko z zasobami; wynik preprintu. | tak |
| `du2023guiding` | Z5 | rezerwowa | Przypisana wyłącznie do Z5. | nie |
| `klissarov2024motif` | Z5 | rezerwowa | Przypisana wyłącznie do Z5. | nie |
| `keeling2024can` | L3.3, L3.6 | zostaje (rdzeń) | Najbliższy precedens pomiaru progu przełączenia; podstawa porównań w 6.2. | tak |
| `liu2024agentbench` | brak | kandydatka do usunięcia | Nie podpiera żadnego twierdzenia: metryki z 4.5 są definicjami własnymi (docs/04), a pozycja ma status „?”. Usunięcie w części 2 (decyzja autora). | nie |
| `tagliabue2025probing` | L3.5 | zostaje (uzupełniająca) | Jedyne źródło dla L3.5; wynik preprintu. | tak |
| `tagliabue2026pain` | Z7 | rezerwowa | Przypisana wyłącznie do Z7. | tak |
| `bianco2026beyond` | L3.3, L3.4 | zostaje (rdzeń) | Replikacja kluczowego wyniku i jedyne źródło o formacie bodźca (liczby a etykiety), czyli tło PB4. | tak |
| `ren2026ai` | Z8 | rezerwowa | Przypisana wyłącznie do Z8; manuskrypt bez recenzji. | tak |
| `berg2026language` | Z8 | rezerwowa | Przypisana wyłącznie do Z8. | tak |
| `schlatter2026incomplete` | Z9; L3.4 | rezerwowa | Dodatkowy przykład do L3.4, które podpierają bianco2026beyond i cedro2026cash. | tak |
| `cedro2026cash` | L3.4 | zostaje (uzupełniająca) | Jedyna recenzowana pozycja w wątku 3.4; czy dotyczy decyzji tego rodzaju co w pracy: do potwierdzenia przy lekturze. | nie |
| `mikaelson2025beyond` | Z9; L3.3 | rezerwowa | Dodatkowy przykład do L3.3, które podpierają keeling2024can i bianco2026beyond. | tak |
| `webson2022prompt` | Z6 | rezerwowa | Przypisana wyłącznie do Z6. | nie |
| `sclar2024quantifying` | L4.2 | zostaje (rdzeń) | Główne źródło tezy o wrażliwości na format; cytowane w problemie badawczym i w 6.2. | nie |
| `salinas2024butterfly` | L4.2 | rezerwowa | Powiela rolę sclar2024quantifying; docs/01 cytuje obie, więc łatwo ją przywrócić. | nie |
| `mizrahi2024state` | L4.4 | zostaje (uzupełniająca) | Jedyne źródło dla parafraz jako kontroli (E6); recenzowana. | nie |
| `pezeshkpour2024large` | L4.3 | zostaje (uzupełniająca) | Jedyne źródło dla wpływu kolejności opcji (E6). | nie |
| `li2023large` | L4.6 | zostaje (uzupełniająca) | Źródło dla bodźców emocjonalnych (ramowanie F2 i F3); preprint. | tak |
| `zheng2024helpful` | L4.7 | rezerwowa | Dotyczy części L4.7 o personie i trafności (T); rolę z F5 podpiera shanahan2023role. | nie |
| `tversky1981framing` | L4.5 | zostaje (rdzeń) | Źródło pierwotne efektu ramowania i podstawa H3; krótka. | nie |
| `schulhoff2024prompt` | L4.1 | zostaje (uzupełniająca) | Jedyne źródło nazewnictwa elementów promptu; lektura fragmentu, preprint. | tak |
| `shanahan2023role` | L4.7, L6.4 | zostaje (rdzeń) | Podpiera dwa twierdzenia K: rolę zadaną w prompcie (F5) i zastrzeżenie o odgrywaniu roli. | nie |
| `sharma2024towards` | L4.8 | zostaje (uzupełniająca) | Jedyne źródło dla alternatywnego wyjaśnienia PB2 i PB5; czy pojęcie pasuje: do potwierdzenia przy lekturze. | nie |
| `jones2022capturing` | L4.6 | zostaje (uzupełniająca) | Recenzowana replikacja efektu ramowania na LLM; bezpośrednie tło H3. | nie |
| `binz2023using` | L5.1 | zostaje (rdzeń) | Uzasadnia podejście „LLM jako badany”, na którym stoi cała metoda. | nie |
| `hagendorff2023machine` | L5.1 | rezerwowa | Powiela rolę binz2023using; preprint. | tak |
| `wichmann2001psychometric` | L5.3 | zostaje (rdzeń) | Źródło pierwotne dopasowania funkcji psychometrycznej z parametrem lapsów. | nie |
| `wichmann2001bootstrap` | L5.4 | zostaje (rdzeń) | Źródło pierwotne przedziałów bootstrap dla progu i nachylenia. | nie |
| `kingdom2016psychophysics` | L5.3, L5.5 | zostaje (uzupełniająca) | Podręcznik jako wprowadzenie i źródło metod adaptacyjnych; lektura fragmentów. | nie |
| `renze2024effect` | L2.3 | rezerwowa | Dotyczy trafności zadań, a nie losowości decyzji; L2.3 podpiera atil2025nondeterminism (do potwierdzenia przy lekturze). | nie |
| `atil2025nondeterminism` | L6.1, L6.2, L2.3 | zostaje (rdzeń) | Podpiera dwa twierdzenia K o powtarzalności i krytykę pojedynczego przebiegu. | nie |
| `miller2024adding` | L6.2 | rezerwowa | Powiela recenzowaną song2025good; wraca, jeśli podeprze porównania parami przy wspólnych ziarnach. | tak |
| `dominguezolmedo2024questioning` | L5.2 | zostaje (uzupełniająca) | Jedyne źródło dla L5.2; lektura fragmentu. | nie |
| `prins2018applying` | L5.5 | zostaje (rdzeń) | Podstawa testu ilorazu wiarygodności przyjętego w D14. | nie |
| `schutt2016painfree` | L5.3 | rezerwowa | W L5.3 powiela wichmann2001psychometric, a estymacji bayesowskiej docs/04 nie stosuje; wraca, jeśli dane pokażą nadrozproszenie. | nie |
| `kuss2005bayesian` | brak | kandydatka do usunięcia | Alternatywa bayesowska, której docs/04 nie stosuje; nie podpiera żadnego twierdzenia. Usunięcie w części 2 (decyzja autora). | nie |
| `song2025good` | L6.2 | zostaje (uzupełniająca) | Recenzowane źródło tezy, że ewaluacja musi uwzględniać próbkowanie. | nie |
| `holm1979simple` | L5.6 | zostaje (uzupełniająca) | Źródło pierwotne korekty przyjętej w D14; krótka. | nie |
| `zawislak2025budowa` | L3.7 | zostaje (rdzeń) | Praca referencyjna: środowisko, prompty i punkt odniesienia wyników (sekcja G, poza limitem). | nie |
| `ollama2026api` | L2.6 | zostaje (uzupełniająca) | Dokumentacja parametrów próbkowania (sekcja G, poza limitem). | nie |
| `deepseek2025distillcard` | L2.6 | zostaje (uzupełniająca) | Zalecenia producenta dla destylatu (sekcja G, poza limitem). | nie |
| `opi2023jsa` | brak | poza selekcją | Tylko do docs/09, nie do pracy. | nie |
| `wmifs2025wymagania` | brak | poza selekcją | Tylko do docs/10, nie do pracy. | nie |
| `butlin2026identifying` | L6.5 | zostaje (uzupełniająca) | Jedyne recenzowane źródło dla L6.5; cytowana w „Poza zakresem” docs/01. | nie |
| `long2024taking` | Z11 | rezerwowa | Przypisana wyłącznie do Z11; preprint. | tak |

## 6. Zliczenia

| Ocena | Naukowe (78) | Techniczne i formalne (5) |
|---|---|---|
| zostaje (rdzeń) | 14 | 1 |
| zostaje (uzupełniająca) | 31 | 2 |
| rezerwowa | 31 | 0 |
| kandydatka do usunięcia | 2 | 0 |
| poza selekcją | 0 | 2 |

Zostaje 45 pozycji naukowych przy zakresie 30–50 z docs/03.

**Strony lektury rdzenia (pole `pages` w .bib).** Osiem z 14 pozycji naukowych ma zakres stron, razem 93 strony. Dla sześciu brak danych: `keramati2014homeostatic`, `binz2023using`, `prins2018applying` (w polu jest numer artykułu), `keeling2024can`, `bianco2026beyond` (arXiv), `sclar2024quantifying` (ICLR). Dla `zawislak2025budowa` pola też brak; docs/01 mówi o ponad 80 stronach. Liczby stron dla każdej pozycji są w sekcji 12.

**Pozycje uzupełniające.** 18 z 31 ma zakres stron (razem 294 strony), ale przy 13 pozycjach wystarczy lektura fragmentu: `maslow1943theory`, `russell2020artificial`, `sutton2018reinforcement`, `astrom2021feedback`, `vaswani2017attention`, `brown2020language`, `ouyang2022training`, `wei2022chain`, `qwen2024qwen25`, `li2024evaluating`, `schulhoff2024prompt`, `kingdom2016psychophysics`, `dominguezolmedo2024questioning`.

## 7. Luki (zaakceptowane)

| Twierdzenie | Stan | Ustalenie |
|---|---|---|
| L5.8 | brak źródła | luka o niskim priorytecie; w części 2 najwyżej dwa źródła podręcznikowe na wszystkie metody pomocnicze |
| L2.3 (część) | definicję temperatury i top_p podaje tylko dokumentacja Ollamy | nie szukamy źródła naukowego; cytujemy `ollama2026api`, a losowość odpowiedzi podpiera `atil2025nondeterminism` |
| L3.6 | z natury bez pojedynczego źródła | opiera się na pozycjach z L3.1–L3.3; brzmienie zawężone |
| L4.8 (warunkowo) | jedyne źródło: `sharma2024towards` | jeśli lektura pokaże, że pojęcie nie obejmuje tego przypadku, PB2 i PB5 zostają bez tła i powstaje luka |
| L7.1 (warunkowo) | jedyne źródło: `bonabeau1996quantitative` | jeśli nie podaje parametru stromości, wraca `ulrich2021response` |

## 8. Preprinty

**Twierdzenia pokryte wyłącznie preprintami**

| Twierdzenie | Pozycje |
|---|---|
| L3.2 | `masumori2025survival` |
| L3.3 | `keeling2024can`, `bianco2026beyond` |
| L3.5 | `tagliabue2025probing` |
| L4.1 | `schulhoff2024prompt` |
| częściowo L3.4 (format bodźca) | `bianco2026beyond` |
| częściowo L4.6 (bodźce emocjonalne) | `li2023large` |
| częściowo L2.5 (model bazowy) | `qwen2024qwen25` |

**Preprinty do sprawdzenia w części 2** (czy istnieje wersja recenzowana; kolumna „Uwaga” powtarza pole `weryfikacja` z .bib albo docs/03)

| Klucz | Ocena | Uwaga |
|---|---|---|
| `keeling2024can` | rdzeń | według raportu z 08.10 w X 2026 nadal tylko preprint |
| `bianco2026beyond` | rdzeń | arXiv v1 |
| `masumori2025survival` | uzupełniająca | według .bib brak wersji recenzowanej |
| `tagliabue2025probing` | uzupełniająca | arXiv v2 z 23.05.2026 |
| `li2023large` | uzupełniająca | .bib wspomina krótką wersję (LLM@IJCAI'23); docs/03 każe sprawdzić wersję recenzowaną |
| `schulhoff2024prompt` | uzupełniająca | według .bib data v6 i ewentualna wersja recenzowana nieustalone |
| `qwen2024qwen25` | uzupełniająca | raport techniczny; docs/03 każe sprawdzić wersję recenzowaną |

W rezerwie jest osiem kolejnych preprintów, które sprawdzamy dopiero wtedy, gdy pozycja wraca do listy: `tagliabue2026pain`, `ren2026ai` (manuskrypt), `berg2026language`, `schlatter2026incomplete`, `mikaelson2025beyond`, `hagendorff2023machine`, `miller2024adding`, `long2024taking`.

## 9. Podrozdziały z nadmiarem źródeł

Więcej niż 3 źródła na stronę po ocenie, liczone według przypisań z docs/02.

| Podrozdział | Stron | Źródeł w docs/02 | Zostaje po ocenie | Uwaga |
|---|---|---|---|---|
| 4.6 | 0,5 | 8 | 7 | według mapy nie potrzebuje własnych źródeł, wystarczą odesłania do 3.2 i 4.3 |
| 6.3 | 1 | 10 | 7 | |
| 3.4 | 1 | 11 | 6 | |
| 6.2 | 1 | 9 | 6 | |
| 3.3 | 1 | 6 | 5 | |
| 4.5 | 1 | 6 | 4 | według mapy wystarczy `astrom2021feedback` i praca referencyjna |
| 4.4 | 1 | 5 | 4 | dwie z nich są techniczne |
| 3.1 | 1 | 5 | 4 | |
| 1.1 | 1 | 4 | 4 | |
| 6.1 | 1,5 | 8 | 5 | |

Odwrotny przypadek: 2.3 ma 2 strony i po ocenie jedno źródło (`wang2024survey`), bo w mapie odpowiada mu jedno twierdzenie (L2.7).

## 10. Wpisy do „Spraw odłożonych” w docs/12 (przyjęte przez autora 12.11.2026)

Do tabeli wpisuje je autor. Numery O9–O12 to propozycja kontynuacji numeracji z docs/12.

| Nr | Sprawa | Skąd | Wracamy |
|---|---|---|---|
| dopisek do O5 | Listy Z1–Z12 i „podrozdziały bez własnych źródeł” z `raporty/literatura_selekcja_cz1.md` jako materiał do skracania | selekcja literatury cz. 1 | po lekturze rdzenia |
| O9 | Brzmienie luki w 2.4: docs/03 nazywa `keeling2024can` „bezpośrednim precedensem pomiaru progu”, więc lukę trzeba zawęzić do progów potrzeb zasobowych agenta w środowisku (L3.6) | selekcja literatury cz. 1 | po lekturze rdzenia |
| O10 | Metody z docs/04 nieobecne w opisie 4.3 i 4.5 (przedział Wilsona, regresja logistyczna, regresja wielomianowa, wspólne liczby losowe): czy plan ma je wymieniać (L5.8) | selekcja literatury cz. 1 | po lekturze rdzenia |
| O11 | docs/06 cytuje `mizrahi2024state` przy zdaniu o budżecie pełnego planu czynnikowego; według docs/03 pozycja dotyczy oceny na wielu parafrazach, więc cytowanie jest do potwierdzenia przy lekturze | selekcja literatury cz. 1 | po lekturze rdzenia |
| O12 | Objętość 2.3: 2 strony przy jednym twierdzeniu w mapie (L2.7) i jednym źródle po selekcji | selekcja literatury cz. 1 | po lekturze rdzenia |

**Rozbieżności między plikami, zgłoszone autorowi**

| Rozbieżność | Stan |
|---|---|
| Zalecana temperatura z karty modelu: 0,6 w docs/02 (2.2) i docs/04, a 0,5–0,7 w docs/03 (sekcja G) | do potwierdzenia przy lekturze `deepseek2025distillcard` |
| docs/06 liczy 30 s na wywołanie i ok. 200 godzin, a docs/12 (D11, sprawa odłożona O3) 170–180 s i ok. 50 dni | objęte sprawą O3 w docs/12; docs/06 zapowiada wpis budżetu po E0 |

## 11. Co otwiera część 2

1. Uzupełnić lukę L5.8: najwyżej dwa źródła podręcznikowe, sprawdzone online u źródła pierwotnego, z datą sprawdzenia.
2. Sprawdzić wersje recenzowane siedmiu preprintów z sekcji 8.
3. Usunąć `liu2024agentbench` i `kuss2005bayesian` z `literatura.bib` i docs/03. Obie są też wymienione w źródłach docs/02 (4.5 i 4.3), a docs/02 jest zamrożony (D18), więc sposób aktualizacji tych przypisań to osobna decyzja autora.
4. Ułożyć kolejkę lektury dla 31 pozycji uzupełniających, z rozróżnieniem „całość” i „fragment”. Dane wyjściowe: 28 godzin lektury tygodniowo, obrona w czerwcu 2027.
5. Uzupełnić liczbę stron dla sześciu pozycji rdzenia bez pola `pages`.
6. Przy lekturze potwierdzić przypisania zaznaczone w tabeli jako „do potwierdzenia przy lekturze”: `starzyk2012motivated`, `starzyk2013simulation`, `bonabeau1996quantitative`, `cedro2026cash`, `sharma2024towards`, `renze2024effect`.
7. Dostęp: dwie pozycje rdzenia mają kategorię C (`starzyk2017needs`, `tversky1981framing`), więc pełny tekst trzeba zdobyć przez bibliotekę.

## 12. Kolejność lektury rdzenia

Najpierw pozycje potrzebne do rozdziałów 1–3, potem do rozdziału 4. Kolumna „Po co czytam” mówi, czego szukać; nie streszcza treści publikacji. Strony z pola `pages` w .bib, dostęp z pola `dostep`.

Rekomendacja agenta: przed pozycją 1 przeczytać `zawislak2025budowa` (rdzeń techniczny, poza 14 pozycjami naukowymi), bo do tej pracy odnoszą się wszystkie pozostałe lektury.

**Rozdziały 1–3**

| Lp. | Klucz | Podrozdziały | Twierdzenia | Stron | Dostęp | Po co czytam |
|---|---|---|---|---|---|---|
| 1 | `starzyk2017needs` | 1.4, 4.2, 6.1 | L1.5, L1.6, L1.7 | 13 | C | Żeby wypisać z numerami stron definicje bólu prymitywnego, progu bólu, bólu abstrakcyjnego i WTA, do których odwołuje się moja definicja $\theta$. |
| 2 | `keramati2014homeostatic` | 1.2, 1.3, 4.5, 6.1 | L1.2, L1.4 | brak danych | A | Żeby sprawdzić, czy „ból” da się zapisać jako odchylenie stanu wewnętrznego od wartości zadanej i jak to zestawić z ujęciem Starzyka. |
| 3 | `sharkey2025could` | 1.5, 6.3 | L1.8, L6.4 | 11 | A | Żeby uzasadnić, że w pracy ból jest sygnałem funkcjonalnym, a nie doznaniem, i mieć odpowiedź na pytanie o antropomorfizację. |
| 4 | `guo2025deepseekr1` | 2.2 | L2.5 | 6 | A | Żeby opisać, jak powstał badany model i jego destylaty oraz co z tego wynika dla kanału rozumowania w eksperymencie. |
| 5 | `keeling2024can` | 3.4, 4.2, 6.2 | L3.3, L3.6 | brak danych | A | Żeby poznać procedurę, którą mierzono tam przełączenie, porównać ją z moją metodą i precyzyjnie zawęzić lukę. |
| 6 | `bianco2026beyond` | 3.4 | L3.3, L3.4 | brak danych | A | Żeby sprawdzić, czy wynik Keelinga się powtarza i jak format intensywności (liczby a etykiety) zmienia odpowiedzi, bo to tło PB4. |
| 7 | `sclar2024quantifying` | 3.2, 4.6, 6.2 | L4.2 | brak danych | A | Żeby podać skalę wpływu formatu promptu i sposób jej pomiaru, na czym opiera się kontrola czynników ubocznych. |
| 8 | `tversky1981framing` | 3.3 | L4.5 | 6 | C | Żeby zdefiniować efekt ramowania u źródła i odnieść do niego warianty F1–F4 oraz hipotezę H3. |
| 9 | `shanahan2023role` | 3.1, 3.3, 6.3 | L4.7, L6.4 | 6 | A | Żeby opisać „ból” agenta jako odgrywanie roli zadanej w prompcie i uzasadnić wariant F5. |

**Rozdział 4**

| Lp. | Klucz | Podrozdziały | Twierdzenia | Stron | Dostęp | Po co czytam |
|---|---|---|---|---|---|---|
| 10 | `binz2023using` | 3.4, 4.2 | L5.1 | brak danych | A | Żeby uzasadnić traktowanie LLM jak uczestnika eksperymentu i poznać zastrzeżenia do tego podejścia. |
| 11 | `wichmann2001psychometric` | 4.3 | L5.3 | 21 | A | Żeby porównać model i estymację z docs/04 (parametry $\gamma$, $\lambda$, dobroć dopasowania) z zaleceniami źródła. |
| 12 | `wichmann2001bootstrap` | 4.3 | L5.4 | 16 | A | Żeby sprawdzić, czy sposób liczenia przedziałów ufności z docs/04 zgadza się z tym, co zaleca źródło. |
| 13 | `prins2018applying` | 4.3, 4.6 | L5.5 | brak danych | A | Żeby opisać test ilorazu wiarygodności z D14 i sprawdzić procedurę wyznaczania wartości p z symulacji. |
| 14 | `atil2025nondeterminism` | 2.1, 4.4, 4.6, 6.3 | L6.1, L6.2, L2.3 | 14 | A | Żeby uzasadnić test powtarzalności w E0 i zastrzeżenie wobec pojedynczego przebiegu w pracy referencyjnej. |
