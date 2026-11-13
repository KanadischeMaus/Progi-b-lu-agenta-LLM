# Selekcja literatury, część 2, etap 1: luki

> Status: wynik etapu 1, przyjęty przez autora 12.11.2026. Decyzje autora: (1) `agresti2013categorical` dodana jako uzupełniająca, lektura trzech fragmentów; nazwę „przedział Wilsona” autor potwierdzi przy lekturze 1.4, a jeśli jej tam nie ma albo wydanie będzie niedostępne, wraca Agresti 2019; (2) `kleijnen2015design` dodana, lektura podrozdziału 3.5; Law 2024 w rezerwie; (3) „regresja wielomianowa” w L5.8 to regresja logistyczna dla odpowiedzi w trzech kategoriach; (4) zapasu dla L4.8 i L7.1 nie szukamy, `sharma2024towards` i `bonabeau1996quantitative` idą na początek pozycji uzupełniających w kolejce lektury; (5) rok w kluczu Agrestiego: 2013. Sekcja 5 poniżej to rekomendacje sprzed decyzji.
>
> Uzupełnienie z 13.11.2026: miejsce wydania książki Kleijnena to Cham (trzy katalogi biblioteczne: University of Patras, Santa Clara University, College of the Holy Cross: „Cham: Springer International Publishing: Imprint: Springer, 2015”); „New York” z portalu Tilburg University jest z nimi niezgodne.
>
> Narzędzie: aplikacja Claude (projekt, wątek „Uzupełnić luki w literaturze, część 2”), model claude-fable-5-2. Data sprawdzeń: 12.11.2026.

## 0. Czym sprawdzano

- Wyszukiwanie w sieci działa, ale zwraca tylko tytuły i adresy stron, bez treści. Treść stron czytało osobne narzędzie do pobierania.
- Pobieranie działa dla: wiley.com (strona produktu), mheducation.com, doi.org (strona Project Euclid pod DOI), arxiv.org, aclanthology.org, proceedings.mlr.press, katalogów bibliotecznych, RePEc, portalu Tilburg University.
- Pobieranie nie działa dla: link.springer.com (błąd plików cookie), projecteuclid.org (strona antybotowa), openreview.net (weryfikacja przeglądarki), plików PDF na media.wiley.com (zakaz w robots.txt; nie obchodziłem go).
- Zasada: w tabeli jest tylko to, co było na pobranej stronie. Wszystko, czego strona nie pokazała, ma dopisek „nie sprawdzono” albo „do potwierdzenia”.

## 1. Uwaga do brzmienia L5.8

Mapa z części 1 wymienia w L5.8 „regresję wielomianową dla siatki 2D”. W docs/04 §6 stoi „regresja logistyczna wielomianowa albo dwie binarne”, a odpowiedź ma tam trzy kategorie (naprawa baterii, naprawa gleby, inna). Przyjąłem więc, że chodzi o regresję logistyczną dla odpowiedzi wielokategorialnej (ang. *multinomial logistic regression*, *baseline-category logit*), a nie o regresję z wielomianem zmiennych objaśniających. Od tego zależy wybór źródła, dlatego proszę o potwierdzenie (decyzja 3).

## 2. Tabela etapu 1

| Luka | Kandydat (autorzy, tytuł, miejsce, rok) | Co podpiera | Gdzie i kiedy sprawdzono | Czy twierdzenie potwierdza streszczenie lub tekst | Rekomendacja |
|---|---|---|---|---|---|
| L5.8: przedział Wilsona, regresja logistyczna, regresja logistyczna wielomianowa | Agresti A., *Categorical Data Analysis*, wyd. 3, Wiley, Hoboken 2013, 752 s., ISBN 978-0-470-46363-5 (Wiley Series in Probability and Statistics) | trzy z czterech metod pomocniczych: przedział ufności dla proporcji (4.3), regresja logistyczna jako kontrola (4.3), model dla odpowiedzi w trzech kategoriach na siatce 2D (4.3 albo 4.5) | strona produktu wiley.com (tytuł, wydanie, 752 strony, ISBN, data „December 2012”); strona tytułowa i spis treści w próbce dystrybutora e-bookshelf.de („Copyright © 2013 by John Wiley & Sons”, Hoboken, dane Library of Congress z ISBN); katalog Texas A&M („Hoboken, N.J.: Wiley, [2013]”); strona autora (UF); 12.11.2026 | częściowo. Spis treści potwierdza: rozdz. 5 „Logistic Regression” (od s. 163), 8.1 „Nominal Responses: Baseline-Category Logit Models” (od s. 293), 1.4 „Statistical Inference for Binomial Parameters” (od s. 13). Nazwisko Wilsona w spisie treści nie pada; tekstu 1.4 nie widziałem, więc to, czy przedział jest tam nazwany i wyprowadzony, jest do potwierdzenia przy lekturze | **dodać** jako uzupełniającą, lektura trzech fragmentów; klucz `agresti2013categorical`, status Z, dostęp C |
| L5.8: wspólne liczby losowe | Kleijnen J. P. C., *Design and Analysis of Simulation Experiments*, wyd. 2, Springer, 2015, 322 s. (International Series in Operations Research & Management Science, t. 230), DOI 10.1007/978-3-319-18087-8, ISBN 978-3-319-18086-1 | wspólne ziarna środowiska dla wszystkich promptów, czyli porównania parami (4.5) | portal badawczy Tilburg University, czyli uczelni autora (tytuł, wydanie, rok, seria i tom, strony, oba ISBN, DOI); springerprofessional.de, serwis Springera (spis rozdziałów, streszczenia); RePEc (rozdz. 3, s. 83–133, DOI 10.1007/978-3-319-18087-8_3); 12.11.2026. Strona link.springer.com nie odpowiada automatowi | tak, na poziomie streszczenia rozdziału 3: „Section 3.5 discusses cross-correlated simulation outputs created through common random numbers (CRN); the use of CRN is popular in random simulation.” Czy podrozdział 3.5 mówi wprost o porównaniach parami: do potwierdzenia przy lekturze | **dodać** jako uzupełniającą, lektura podrozdziału 3.5; klucz `kleijnen2015design`, status Z z jednym polem do potwierdzenia (miejsce wydania: portal Tilburg podaje „New York”, serwis Springera wydawcę „Springer International Publishing”), dostęp C |
| L5.8: wspólne liczby losowe | Law A. M., *Simulation Modeling and Analysis*, wyd. 6, McGraw Hill, 2024, ISBN 978-1-264-26824-5 (e-book 978-1-264-26825-2) | to samo co Kleijnen | strona wydawcy mheducation.com (tytuł, wydanie, „© 2024”, „Published January 23, 2024”, oba ISBN); liczba stron tylko z księgarni i rozbieżna: 688 (Schweitzer, AbeBooks) i 656 (Books Express); 12.11.2026 | nie sprawdzono. Strona wydawcy nie pokazała automatowi spisu treści, więc nie wiem, w którym rozdziale 6. wydania są wspólne liczby losowe | **rezerwa**: wraca, jeśli wolisz klasyczny podręcznik symulacji i masz go w bibliotece; wtedy rozdział i strony trzeba odczytać z egzemplarza |
| L2.3 (część) | nie szukano | definicja temperatury i top_p | — | — | bez zmian: decyzja 13 z części 1 (cytujemy `ollama2026api`) |
| L3.6 | nie szukano | luka badawcza | — | — | bez zmian: twierdzenie z natury nie ma pojedynczego źródła |
| L4.8 (warunkowa) | nie szukano | alternatywne wyjaśnienie PB2 i PB5 | — | — | czekać na lekturę `sharma2024towards`; luka powstaje dopiero wtedy, gdy pojęcie sykofancji nie obejmie tego przypadku |
| L7.1 (warunkowa) | nie szukano | funkcja progowa z parametrem stromości | — | — | czekać na lekturę `bonabeau1996quantitative`; zamiennik (`ulrich2021response`) jest już w bazie |

## 3. Sprawdzone przy okazji, nie proponuję

| Pozycja | Co sprawdzono 12.11.2026 | Dlaczego nie jest kandydatem |
|---|---|---|
| Agresti A., *An Introduction to Categorical Data Analysis*, wyd. 3, Wiley, 2019 | fragment rozdziału 1 na serwerze wydawcy (catalogimages.wiley.com): podrozdział 1.3.5 „Better Confidence Intervals for a Binomial Proportion”, s. 9, opisuje „score confidence interval”, a przypis nazywa go „Wilson score”. Strona produktu się nie pobrała, więc ISBN i liczba stron są niepotwierdzone | krótszy podręcznik tego samego autora; byłby drugim źródłem do tych samych metod. Wraca tylko wtedy, gdy wolisz go zamiast wydania z 2013 r. |
| Brown L. D., Cai T. T., DasGupta A., „Interval Estimation for a Binomial Proportion”, *Statistical Science* 16(2), 2001, s. 101–133, DOI 10.1214/ss/1009213286 | strona pod DOI: autorzy, tytuł, tom, numer, strony, data (V 2001); streszczenie zaleca przedział Wilsona dla małych n. Czy tekst jest bezpłatny u wydawcy: nie sprawdzono (Project Euclid blokuje automat) | to artykuł, a decyzja 5 z części 1 mówi o źródłach podręcznikowych. Wraca, jeśli lektura 1.4 u Agrestiego pokaże, że przedział Wilsona nie jest tam nazwany |

## 4. Ocena: czy dobre źródło jest

- Dla przedziału Wilsona, regresji logistycznej i regresji logistycznej wielomianowej: tak, jeden podręcznik (Agresti 2013) z pełnymi danymi potwierdzonymi u wydawcy. Zastrzeżenie: nazwę „przedział Wilsona” potwierdzi dopiero lektura 1.4.
- Dla wspólnych liczb losowych: źródło jest (Kleijnen 2015), ale to monografia o planowaniu eksperymentów symulacyjnych, a nie podręcznik wprowadzający. Streszczenie potwierdza, że podrozdział 3.5 dotyczy CRN; nie potwierdza brzmienia, którego potrzebuje praca (porównania parami przy wspólnych ziarnach).
- Obie pozycje mają kategorię dostępu C (brak bezpłatnej kopii; na stronie Wileya są tylko fragmenty). Zgodnie z D16 cytujemy przez DOI albo stronę wydawcy.

## 5. Co wymaga decyzji autora

1. **Dodać `agresti2013categorical`?** Rekomendacja: tak, bo jedna pozycja pokrywa trzy z czterech metod pomocniczych, a jej dane są potwierdzone u wydawcy i na stronie tytułowej.
2. **Wspólne liczby losowe: Kleijnen, Law czy nazwana luka?** Rekomendacja: `kleijnen2015design`, bo tylko dla niego streszczenie u źródła potwierdza, gdzie jest CRN, a książka ma DOI.
3. **Czy „regresja wielomianowa” w L5.8 to regresja logistyczna dla odpowiedzi w trzech kategoriach (docs/04 §6)?** Rekomendacja: potwierdzić to odczytanie, bo docs/04 §6 definiuje odpowiedź w trzech kategoriach i mówi o regresji logistycznej.
4. **Luki warunkowe L4.8 i L7.1: szukać zapasu już teraz?** Rekomendacja: nie, ale w kolejce lektury (etap 3d) postawić `sharma2024towards` i `bonabeau1996quantitative` na początku pozycji uzupełniających, bo dopiero ich lektura rozstrzyga, czy luki w ogóle powstaną.
5. **Rok w kluczu Agrestiego.** Strona Wileya podaje datę wydania „December 2012”, strona tytułowa „Copyright © 2013”, katalog „[2013]”. Rekomendacja: 2013, bo tak datują książkę strona tytułowa, katalog i sam autor.

## 6. Wiersz do docs/11_rejestr_AI.md

| Data | Narzędzie i model | Obszar | Co zrobiono i co zdecydował autor | Pliki |
|---|---|---|---|---|
| 12.11.2026 | aplikacja Claude (projekt), claude-fable-5-2 | b) | Etap 1 części 2 selekcji literatury: wyszukanie i sprawdzenie online trzech kandydatów dla luki L5.8 (Agresti 2013, Kleijnen 2015, Law 2024), ocena pozostałych luk bez wyszukiwania. Decyzje autora (12.11.2026): dodane agresti2013categorical i kleijnen2015design, Law 2024 w rezerwie, zapasu dla L4.8 i L7.1 nie szukamy | raporty/literatura_selekcja_cz2_etap1.md |
