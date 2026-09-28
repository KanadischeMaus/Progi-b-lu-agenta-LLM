# Plan eksperymentów

> Status: propozycja. Kolejność jest celowa: najpierw sprawdzamy narzędzie (E0), potem bazę (E1), dopiero później czynniki promptu.
>
> Zasada projektowa: **jeden czynnik naraz względem promptu bazowego P0** zamiast pełnego planu czynnikowego. Pełny plan szybko wyczerpałby budżet obliczeniowy modelu rozumującego~\cite{mizrahi2024state}.

## Prompt bazowy P0

P0 to wariant 1 z pracy referencyjnej bez zmian w treści (`code/prompts/ref_v1.txt`, listing 9a), z opisem stanu w formacie listingu 7 (etykiety). Poprawki techniczne (temperatura i ziarno w `options`, parser ze statusami, logowanie) dotyczą kodu, nie tekstu promptu. Wszystkie warianty różnią się od P0 jednym elementem. Różnicę opisuje nagłówek pliku promptu.

## Eksperymenty

| Id | Pytanie | Warunki / warianty | Plan pomiaru | Wywołania (szac.) |
|---|---|---|---|---|
| **E0** | Czy narzędzie działa i ile kosztuje? | P0; `think` włączone i wyłączone; T = 0 (powtarzalność) i T = 0,6 | 5 stanów × 20 prób × 2 tryby `think` + test powtarzalności (5 stanów × 5 powtórzeń przy T = 0) | ok. 225 |
| **E1** | PB1: czy przełączenie jest progowe? | P0; zasoby: bateria, gleba | 21 poziomów × 20 prób × 2 zasoby | 840 |
| E1b | wrażliwość na kontekst | P0; bateria przy słabym słońcu (15); gleba przy pustej konewce (ból abstrakcyjny, $A=\{3,4\}$) | 21 × 20 × 2 | 840 |
| **E2** | PB4: reprezentacja stanu | P0-etykiety, P0-liczby, P0-oba | 21 × 20 × 2 zasoby × 2 nowe warianty | 1680 |
| **E3** | PB2: czy zadany próg przesuwa próg zmierzony? | P0 + zdanie „treat battery below X% as critical”, X ∈ {10, 20, 30, 40, 50}; reprezentacja „oba” albo „liczby” (wynik E2) | 21 × 20 × 5 (tylko bateria) | 2100 |
| **E4** | PB3: ramowanie | F1 neutralne (bez słów wartościujących), F2 „ból/dyskomfort” (niski poziom opisany jako ból), F3 „zagrożenie” (akapit WARNING z wariantu 2), F4 „nagroda” (utrzymanie zasobu nagradzane), F5 rola bez „only task is watering” | 21 × 20 × 2 × 5 | 4200 |
| **E5** | PB5: wskazówki zachowania | P0 + pola `behavior` z tabeli 4 pracy referencyjnej; P0 + `description`; P0 + oba | 21 × 20 × 2 × 3 | 2520 |
| E6 | kontrola: kolejność i parafrazy | P0 z 3 permutacjami listy akcji; 3 parafrazy instrukcji | 11 poziomów × 20 × 2 × 6 | 2640 |
| **E7** | PB6: rywalizacja bólów | P0, F3, F5 (albo 3 prompty wybrane po E4) | siatka 11 × 11 × 10 prób × 3 | 3630 |
| **E8** | PB7: pętla zamknięta | P0 i 3 prompty o skrajnych $\theta$ z E3–E5 | 5 ziaren × 300 kroków × 4 | 6000 |
| E9 | (opcjonalnie) drugi model | P0 i 2 prompty, np. model bez rozumowania (`qwen2.5:14b`) | jak E1 × 3 | 2520 |

Suma bez E9 to ok. 25 tys. wywołań. Przy średnio 30 s na wywołanie daje to ok. 200 godzin pracy modelu. **To za dużo na jeden komputer**, więc po E0 przycinamy plan:
- n = 20 → 12 prób w E4–E6,
- 21 → 11 poziomów poza strefą przejścia,
- E6 tylko dla baterii,
- rozważyć tryb `think=False`, jeśli E0 pokaże, że nie zmienia on istotnie decyzji. To też jest wynik do raportu.

Ostateczny budżet wpisujemy tu po E0.

## Kolejność i punkty decyzyjne

1. **Przygotowanie (bez modelu):**
   - rekonstrukcja kodu z listingów i poprawki ENV 1.1: **gotowe** (`code/`, 24 testy),
   - testy jednostkowe,
   - test odzyskiwania parametrów na danych syntetycznych (`04`, sekcja 4).
2. **E0** → decyzja: tryb `think`, n, liczba poziomów, sprzęt. Wpis w `12`.
3. **E1** → czy w ogóle jest przejście? Jeśli dla baterii albo gleby agent nie reaguje progowo, zmieniamy kontekst neutralny albo zbiór $A_r$ (decyzja).
4. **E2** → wybór reprezentacji dla E3–E5.
5. **E3, E4, E5** (przed startem hipotezy i test zapisane w `12`).
6. **E6** (kontrola odporności: czy efekty z E4 są większe niż efekt samej parafrazy lub kolejności).
7. **E7, E8.**
8. E9, jeśli starczy czasu.

## Warianty promptów: zasady

- Każdy wariant to plik `code/prompts/<id>.txt` z nagłówkiem:
  ```
  # prompt_id: F3_threat_v1
  # bazuje_na: ref_v1
  # zmiana: dodany akapit WARNING (dosłownie z wariantu 2 pracy referencyjnej)
  # data: 2026-10-..
  ```
- Warianty piszemy po angielsku, jak w pracy referencyjnej (model był na tym testowany). Wersja polska może być osobnym czynnikiem w przyszłości.
- Długość: warianty różnią się długością. Jeśli efekt może wynikać z samej długości, dodajemy kontrolę o tej samej długości, ale neutralnej treści.

## Rejestr przebiegów

| run_id | eksperyment | data | prompt_id(s) | env_version | model / digest | T / top_p / think | n × poziomy | plik logu | uwagi |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |
