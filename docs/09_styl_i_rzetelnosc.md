# Styl i rzetelność

Plik dla każdego, kto pisze albo poprawia tekst pracy: autora i agentów. Celem jest tekst jasny, konkretny, dobrze udokumentowany i spójny. Taki tekst łatwo obronić.

## 1. Styl naukowy po polsku

**Forma i czas**
- Forma bezosobowa („przeprowadzono”, „przyjęto”) albo 1. osoba liczby mnogiej („przyjmujemy”). Wybieramy jedną i trzymamy się jej. Decyzję zapisujemy w `12`.
- Metody i wyniki opisujemy w czasie przeszłym („zmierzono”, „agent wybierał”). Twierdzenia ogólne i definicje w teraźniejszym („funkcja psychometryczna opisuje...”).

**Zdania i akapity**
- Jedno zdanie, jedna myśl. Zdanie wielokrotnie złożone dzielimy.
- Czasowniki zamiast łańcuchów rzeczowników: „przeanalizowano”, a nie „dokonano przeprowadzenia analizy”.
- Pierwsze zdanie akapitu mówi, o czym jest akapit. Nie kończymy akapitu zdaniem, które tylko powtarza jego treść.

**Konkret zamiast ogólnika**

| Zamiast | Piszemy |
|---|---|
| „agent reagował szybciej” | „agent rozpoczynał ładowanie przy średnio 31% baterii (PU 95%: 27–35%) wobec 18% w wariancie bazowym” |
| „prompt ma istotny wpływ” | „istotny” tylko przy teście statystycznym, z wartością i testem |
| „wiele badań pokazuje” | konkretne badania z odwołaniami |

**Zbędne frazy (usuwamy albo zastępujemy treścią)**
- „W dzisiejszych czasach...”, „W ostatnich latach obserwujemy dynamiczny rozwój...”
- „Warto zauważyć, że...”, „Należy podkreślić, że...”, „Nie ulega wątpliwości, że...”, „Jak wiadomo...”
- „odgrywa kluczową rolę”, „stanowi istotny element”, „szeroko pojęty”, „kompleksowy”, „innowacyjny”
- kalki z angielskiego:
  - „adresować problem” → „rozwiązywać”, „zajmować się”,
  - „bazować na” → „opierać się na”,
  - „w oparciu o” → „na podstawie”.

**Listy**
- Tylko gdy elementy są równorzędne i jest ich co najmniej trzy. W pozostałych przypadkach piszemy akapit.
- Nie dzielimy wszystkiego na trójki z przyzwyczajenia. Liczba punktów wynika z treści.

**Terminy, liczby, rysunki**
- Terminy wyłącznie według `08_slownik_pojec.md`. Nie wymieniamy synonimów dla ozdoby, bo w tekście technicznym zmiana słowa sugeruje zmianę pojęcia.
- Liczby z przecinkiem dziesiętnym, z jednostką i niepewnością. Zaokrąglamy do precyzji, na jaką pozwala pomiar (zwykle 2 cyfry znaczące dla $\theta$ w %).
- Rysunek i tabela opisane w tekście: co pokazują i jaki jest wniosek. Nie tylko „przedstawiono na rys. 5”.

## 2. Cytowanie i parafraza

- **Cytat dosłowny:** w cudzysłowie „...”, z odwołaniem i numerem strony `\cite[s.~5]{klucz}`. Używamy rzadko, głównie przy definicjach.
- **Parafraza:** oddajemy myśl własną strukturą zdania i odwołujemy się do źródła. Zamiana słów na synonimy przy zachowaniu składni oryginału to nadal zapożyczenie.
- **Synteza zamiast streszczenia:** akapit przeglądowy zestawia 2–3 źródła i mówi, co z nich wynika dla tej pracy. Nie streszczamy jednego źródła zdanie po zdaniu.
- **Tłumaczenie z angielskiego:** tłumaczenie fragmentu to też cytat albo parafraza. Zawsze z odwołaniem.
- **Własne wcześniejsze teksty i praca referencyjna:** nie kopiujemy; cytujemy.
- **Kod i listingi** z pracy referencyjnej: jeśli pokazujemy, to z odwołaniem („na podstawie listingu 5 w~\cite{zawislak2025budowa}”).
- **Rysunki** przerysowane z innych prac: w podpisie „na podstawie~\cite{...}”.

## 3. Jak działa kontrola pracy w JSA i co z tego wynika

Pracę sprawdza Jednolity System Antyplagiatowy (JSA) prowadzony przez OPI~\cite{opi2023jsa}. Student wgrywa ją przez APD. System ma dwa niezależne moduły.

**Moduł podobieństw**
- Porównuje tekst z bazami: repozytorium prac dyplomowych, publikacje, zasoby internetowe.
- Wskazuje fragmenty zbieżne. Raport interpretuje promotor.
- Na WMiFS w ramach jednego badania można wykonać najwyżej trzy próby sprawdzenia pliku. Promotor decyduje o dopuszczeniu pracy do obrony.
- **Co z tego wynika:** rzetelne cytowanie (sekcja 2) i własne ujęcie tematu. Fragmenty cytowane z odwołaniem są dopuszczalne. Problemem są zapożyczenia bez odwołania i parafrazy zbyt bliskie oryginałowi.

**Moduł analizy użycia sztucznej inteligencji (od 2024)**
- Jest opcjonalny: promotor włącza go przy zakładaniu badania.
- Według opisu OPI ocenia regularność i przewidywalność tekstu za pomocą modelu językowego. Nie porównuje tekstu z żadną bazą.
- OPI zaznacza, że wynik obarczony jest błędami w obie strony: tekst ludzki może zostać oznaczony, a wygenerowany przeoczony.

**Nasze podejście**
- Użycie AI jest dopuszczalne i jawne. Od roku 2025/2026 WMiFS wymaga tabeli z wykazem obszarów i narzędzi GenAI (`10`, `11`).
- Nie „uczłowieczamy” tekstu pod detektor i nie korzystamy z narzędzi, które to robią. Celem jest dobry tekst, za którego treść autor odpowiada, a nie wynik detektora.
- Udział autora dokumentujemy:
  - historią wersji w git (kto, kiedy, co zmienił),
  - rejestrem AI (`11`),
  - ustaleniami z promotorem (`12`).
  Przy ewentualnym oznaczeniu fragmentu przez moduł SI to są dowody procesu powstawania pracy.
- Sposób pracy z AI warto uzgodnić z promotorem na początku, a nie przy raporcie z JSA.

## 4. Recenzja niezależna rozdziału

Model, który nie pisał tekstu, łatwiej zauważy luki. Dwie możliwości:
- subagent w Claude Code bez kontekstu pisania (instrukcja w `CLAUDE.md`),
- czat Gemini (albo inny model), do którego wklejamy rozdział i poniższy prompt.

Każde użycie wpisujemy do rejestru AI.

**Prompt dla recenzenta (do wklejenia):**

```
Jesteś recenzentem pracy magisterskiej z inżynierii i analizy danych
(Politechnika Rzeszowska). Temat: „Wpływ promptu na progi bólu agenta LLM”.
Poniżej fragment pracy (LaTeX). Oceń go krytycznie i konkretnie:
1. Czy wywód jest logiczny i kompletny? Wskaż przeskoki i nieuzasadnione wnioski.
2. Które twierdzenia wymagają źródła, a go nie mają?
3. Czy definicje i oznaczenia są spójne?
4. Czy liczby i wnioski z wyników są sformułowane ostrożnie (niepewność, n)?
5. Język: niejasne zdania, powtórzenia, puste frazy, błędy.
Zwróć tabelę: nr | fragment (cytat do 10 słów) | problem | propozycja.
Nie przepisuj całego tekstu. Nie oceniaj formatowania LaTeX.
[WKLEJ ROZDZIAŁ]
```

## 5. Lista kontrolna przed oddaniem rozdziału promotorowi

- [ ] Każde twierdzenie merytoryczne ma odwołanie albo wynik z `results/`.
- [ ] Brak `\dower{}` i `TODO` (albo świadomie zostawione z pytaniem do promotora).
- [ ] Terminy zgodne ze słownikiem, symbole zgodne z `04`.
- [ ] Rysunki i tabele mają odwołania w tekście i podpisy bez kropki.
- [ ] Liczby z niepewnością; przecinek dziesiętny.
- [ ] Rozdział przeczytany na głos (albo przez recenzenta niezależnego). Zdania do poprawy poprawione.
- [ ] Wpis w rejestrze AI, commit w git.
