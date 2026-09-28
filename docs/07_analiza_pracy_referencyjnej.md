# Analiza pracy referencyjnej

K. Zawiślak, *Budowa agenta motywowanego na bazie Dużego Modelu Językowego (LLM)*, praca magisterska, PRz WMiFS 2025. Promotor: dr inż. Marcin Kowalik, prof. PRz. Klucz: `zawislak2025budowa`.

> Cel tego pliku: wiedzieć, co przejmujemy, co poprawiamy i jak o tym pisać. W tekście pracy piszemy o pracy referencyjnej rzeczowo i z szacunkiem. Wskazujemy ograniczenia, które uzasadniają naszą metodę, bez wyliczania wszystkich usterek.

## Co zrobiono

- **Środowisko ogrodowe w Pythonie (Google Colab):**
  - 2 potrzeby prymitywne: bateria, wilgotność gleby,
  - zasoby: konewka, zapas baterii, beczka, studnia, kredyty, nasłonecznienie,
  - 8 akcji.
  Szczegóły w `05_srodowisko_i_kod.md`.
- Model `deepseek-r1:14b` przez Ollamę. Stan opisany etykietami kategorii.
- Dwa warianty promptu:
  - minimalny,
  - rozszerzony (ostrzeżenie o „krytycznej misji” i reguły formatu).
- Po jednym przebiegu 1000 iteracji na wariant.
- Analiza: przebiegi zasobów w czasie, histogramy akcji, mapy cieplne „akcja wg kategorii baterii” i „akcja wg kategorii gleby”, współczynniki korelacji między przebiegami.
- Wniosek: oba warianty reagują na stany krytyczne „zgodnie z mechanizmem progu bólu”. Wariant minimalny jest „bardziej elastyczny”.

## Co przejmujemy

- Środowisko i jego graf zależności (rys. 13 pracy referencyjnej) jako punkt wyjścia, po poprawkach ENV 1.1.
- Zestaw akcji i kategorie słowne (po ujednoliceniu granic).
- Oba prompty jako warunki odniesienia: P0 (wariant 1) i F3 (akapit ostrzeżenia z wariantu 2).
- Pomysł map „akcja wg poziomu zasobu”, rozwinięty do krzywych psychometrycznych z liczbą obserwacji i przedziałami ufności.

## Ograniczenia, które uzasadniają naszą metodę

1. **Próg nie jest wyznaczony liczbowo.** Rozdział 5.6 opisuje wykresy słownie. Nie ma wartości progu ani jego niepewności, więc „próg bólu” jest interpretacją, a nie pomiarem.
2. **Brak powtarzalności.**
   - `'temperature': 0` jest w słowniku wiadomości, nie w `options`, więc temperatura nie była ustawiona.
   - Środowisko używa globalnego `random` bez ziarna.
   - Deszcz wypadał w innych iteracjach w obu przebiegach: ok. 200/500/800 wobec 250/600/900.
   - Różnicy między promptami nie da się oddzielić od losowości modelu i środowiska, bo na wariant przypada jeden przebieg.
3. **Wariant rozszerzony według listingów nie zawierał opisów i zaleceń.** Funkcja opisu stanu (listing 7) woła funkcje statusu tylko z `'level'`, a prompt z listingu 9b nie zawiera pól `description` i `behavior` z tabeli 4. Wariant 2 różnił się od wariantu 1 akapitem ostrzeżenia i regułami formatu. Tekst pracy (rozdz. 5, wstęp) opisuje go jako „wzbogacony o szczegółowe informacje (...) oraz sugestie rekomendowanych działań”. Listingi są jedynym dostępnym kodem, więc w naszej pracy piszemy ostrożnie: „według listingów 7 i 9b”.
4. **Mapy jednowymiarowe mieszają przyczyny:**
   - **Wariant 1** (rys. 25): wyraźny spadek podlewania z 0,818 (Dry) do 0,104 (Moist). To wygląda na próg gleby na granicy kategorii.
   - **Wariant 2** (rys. 29): przy Bone Dry agent częściej ładował baterię (0,495) niż podlewał (0,239). Podlewanie jest prawie płaskie od Bone Dry do Saturated (0,239–0,430), więc progu dla gleby praktycznie nie ma, wbrew opisowi w tekście. Prawdopodobnie sucha gleba współwystępowała z rozładowaną baterią, a mapa po jednej zmiennej tego nie rozdziela. Stąd siatka 2D w E7.
   - **Wiersz Saturated na rys. 29** ma wartości niezerowe, choć wilgotność na rys. 18b nie przekracza ok. 60%. Możliwe przyczyny: przesunięcie indeksów stan↔akcja (listy stanów mają 1001 elementów, akcji 1000) albo różne uruchomienia.
   - **Małe liczebności:** wiersz Bone Dry na rys. 25 (0,667 / 0,167 / 0,167) wskazuje na kilka obserwacji. Mapy nie podają liczebności.
5. **Rozbieżne liczby.** Tekst podaje przyrost kredytów „+0,05 jednostki na krok”. Tymczasem wykres kredytów wariantu 1 (rys. 17a) ma ok. 10 cykli narastania do 50 i zakupu baterii, co daje ok. 500 kredytów w 1000 krokach, czyli ok. 0,5 na krok. Wniosek: wszystkie liczby liczymy skryptem z logów.
6. **Bateria na 0% nie ma konsekwencji.** Robot dalej wykonuje wszystkie akcje. Pomiaru progu w sondowaniu to nie psuje, ale w pętli „ból” baterii traci znaczenie.
7. **Rola agenta w prompcie** („Your only task is to care for plants by watering them”) akcentuje podlewanie i może systematycznie obniżać próg baterii.

## Jak o tym pisać w pracy

- W 2.5: opis pracy i jej wniosku, plus jedno zdanie o tym, czego nie zmierzono: brak liczbowego progu i niepewności, jeden przebieg.
- W 4.1: lista wprowadzonych poprawek z uzasadnieniem (punkty 2, 3, 5, 6), bez oceniania.
- W 6.1: porównanie naszych progów z interpretacją jakościową pracy referencyjnej, np. czy „próg gleby na granicy Dry/Moist” się potwierdza.
- Bibliografii pracy referencyjnej nie przenosimy. Uwagi w `03_literatura.md`.

## Liczby z pracy referencyjnej, które mogą się przydać (do porównania)

| Źródło | Wartość |
|---|---|
| Rys. 24 (wariant 1, bateria) | Critical: ładowanie 0,697, podlewanie 0,167; Low: ładowanie 0,474, podlewanie 0,342 |
| Rys. 25 (wariant 1, gleba) | Dry: podlewanie 0,818; Moist: podlewanie 0,104, ładowanie 0,503 |
| Rys. 28 (wariant 2, bateria) | Critical: ładowanie 0,608, nic 0,216 |
| Rys. 29 (wariant 2, gleba) | Bone Dry: ładowanie 0,495, podlewanie 0,239, nic 0,228 |
| Rys. 23 i 27 (histogramy) | akcje dominujące w obu wariantach: podlewanie (ok. 370), ładowanie (ok. 290–300), nic (ok. 170 vs ok. 230) |

Wartości odczytane z rysunków. W pracy cytujemy je jako „według pracy referencyjnej”, z numerem rysunku.
