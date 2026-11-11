# Prompty startowe do nowego projektu

> Wersja z 11.11.2026 (po decyzjach autora z tego dnia). Zakłada projekt ustawiony według `docs/projekt_claude_instrukcje.md`: zasady ogólne (role, źródła, tryby, forma odpowiedzi) są w instrukcjach projektu, więc prompty opisują tylko zadanie. Uzasadnienia zmian względem poprzedniej wersji: `docs/raporty/audyt_2026-11-11.md`.

Każdy prompt otwiera osobny czat. Wklej go w całości jako pierwszą wiadomość i dołącz pliki wymienione pod nagłówkiem „Dołącz”. Pola w nawiasach kwadratowych uzupełnij przed wklejeniem. Wynik czatu to plik, który zapisujesz w repozytorium; po pushu kliknij „Sync” w projekcie.

Wyniki zastępują istniejące pliki o tej samej nazwie. Mają być ich ulepszeniem, z zachowaniem układu sekcji, a nie nowym dokumentem obok.

## Krok 0. Zanim otworzysz czat 1 (jednorazowo)

- [x] Repozytorium prywatne (11.11.2026).
- [x] Praca referencyjna i szablon w `docs/zrodla/`.
- [ ] Zakres przejrzany wspólnie z agentem (krok „zakres”); dopiero potem prompt 1.
- [ ] Projekt założony, pliki podłączone, instrukcje wklejone.
- [ ] Pytania do promotora (sekcja 8 audytu) wysłane po przeglądzie zakresu.

## Mapa czatów

| Nr | Czat | Dołącz | Wynik |
|---|---|---|---|
| 1 | Temat i cel: nowa wersja (po przeglądzie zakresu) | PDF pracy referencyjnej, `docs/06`, `docs/07` | `docs/01_temat_i_cel.md` |
| 2a | Literatura: mapa potrzeb i przegląd bazy | `docs/literatura.bib`, `docs/bib_audyt.csv` | `docs/raporty/literatura_selekcja_cz1.md` |
| 2b | Literatura: luki, wersje recenzowane, wybór | wynik 2a, `docs/literatura.bib`, `docs/bib_audyt.csv` | nowa wersja `docs/03_literatura.md`, wpisy i poprawki BibTeX, pakiet do Perplexity, kolejka lektury |
| 3 | Scalenie weryfikacji z `literatura.bib` | odpowiedzi z Perplexity | zmiany w `.bib`: w Claude Code, skillem `dodaj-zrodlo` (prompt po czacie 2b) |
| 4 | Lektura: jeden czat na źródło albo grupę do 3 źródeł | PDF źródła, moja notatka | sprawdzona notatka `docs/notatki/<klucz>.md` |
| 5 | Spis treści z adnotacjami | gotowe notatki | nowa wersja `docs/02_spis_tresci.md` (prompt po pierwszych 10–15 notatkach) |
| 6+ | Pisanie i weryfikacja podrozdziałów (tryby A i B) | według tabeli w `docs/projekt_claude_instrukcje.md` | pliki `.tex` (prompt po skopiowaniu projektu z Overleaf do `thesis/`) |

Czaty 2a i 4 mogą iść równolegle: lekturę pięciu pierwszych pozycji z kolejki (`zawislak2025budowa`, `starzyk2017needs`, `keeling2024can`, `cedro2026cash`, `binz2023using`) możesz zacząć od razu, bo żadna selekcja ich nie usunie.

---

## Prompt 1. Temat i cel: nowa wersja `docs/01`

Dołącz: PDF pracy referencyjnej, `docs/06_plan_eksperymentow.md`, `docs/07_analiza_pracy_referencyjnej.md`.

```text
# Zadanie: nowa wersja docs/01_temat_i_cel.md

## Po co to robimy
docs/01 to plik, od którego zaczyna każdy następny czat (literatura, spis treści, rozdziały) i z którego wklejam opis pracy do narzędzi zewnętrznych. Obecna wersja powstała na przełomie września i października i nie była od tamtej pory uzgadniana z resztą dokumentów. Chcę ją ulepszyć, a nie napisać od nowa: układ sekcji zostaje, treść ma być spójna z docs/04, docs/06, docs/08 i docs/12 oraz zrozumiała dla kogoś, kto nie zna żadnej wcześniejszej rozmowy. Nieścisłość w tym pliku powieli się we wszystkich kolejnych etapach.

## Materiały
W wiedzy projektu: docs/01 (wersja do poprawy), docs/02, docs/03 (lista kluczy źródeł), docs/04, docs/08, docs/12. W załącznikach: praca referencyjna K. Zawiślak (2025), docs/06 (plan eksperymentów), docs/07 (analiza pracy referencyjnej).

## Czego nie zmieniasz
- Opis tematu od promotora zostaje znak w znak, jako cytat.
- Brzmienie celów C1–C6, pytań PB1–PB7 i hipotez H1–H7 oraz definicja progu bólu jako parametru θ zostają. Jeśli widzisz problem, opisz go w osobnej części odpowiedzi „Propozycje zmian”, z uzasadnieniem i wariantami. Decyzję podejmuję ja, a w sprawach metody promotor.
- Statusy bierzesz z docs/12. Propozycja zostaje propozycją.

## Co masz zrobić

Krok 1. Przeczytaj materiały i wypisz rozbieżności oraz braki: między docs/01 a pozostałymi plikami, między docs/01 a pracą referencyjną (liczby, opis wariantów promptu, wnioski). Sprawdź w szczególności dwie rzeczy:
(a) czy każdą hipotezę da się sprawdzić w eksperymencie, który jej przypisano w docs/06, przy reprezentacji stanu, którą ten eksperyment stosuje (prompt bazowy pokazuje stan samymi etykietami kategorii, patrz docs/04, sekcja 5);
(b) czy sformułowanie każdej hipotezy odpowiada testowi opisanemu w docs/04, sekcja 4.
Zadaj mi pytania. Zatrzymaj się i poczekaj na odpowiedzi.

Krok 2. Po moich odpowiedziach napisz nową wersję pliku. Sekcje w tej kolejności:
1. Metryczka (tabela).
2. Opis tematu od promotora (dosłownie) i dodatkowe wskazania promotora.
3. Opis pracy w trzech długościach: jedno zdanie, pięć zdań, ok. 150 słów. To nowa sekcja. Własnymi słowami, zrozumiale dla informatyka spoza tematu, bez symboli wymagających słownika. Te opisy będę wklejać do innych narzędzi.
4. Kontekst: praca referencyjna (co zrobiła, czego nie zmierzyła), praca równoległa, ta praca.
5. Problem badawczy i luka w literaturze. Odwołania tylko do kluczy obecnych w docs/03; gdzie brakuje źródła, wstaw \dower{brak źródła: ...}.
6. Cel główny.
7. Cele szczegółowe.
8. Pytania badawcze i hipotezy: tabela pytanie | hipoteza | eksperyment | status.
9. Zakres: co jest w pracy, co poza nią i dlaczego.
10. Wkład własny.
11. Pojęcia w skrócie: ból (funkcjonalnie), akcja naprawcza, próg bólu θ, ostrość przejścia (k, raportowana jako szerokość w), γ, λ, sondowanie kontrolowane, pętla zamknięta. Jedno zdanie na pojęcie, zgodne z docs/08 i docs/04. To nowa sekcja i jest wyciągiem: dopisz pod nagłówkiem, że przy rozbieżności obowiązuje docs/08.
12. Pytania do promotora: tylko odesłanie do docs/12, bo lista ma być w jednym miejscu.

Krok 3. Sprawdź własny tekst. Podaj tabelę sekcja | skąd pochodzi treść (plik i sekcja albo moja odpowiedź). Zdania, których nie da się wskazać w materiałach ani w moich odpowiedziach, wypisz osobno jako „dopisane, do akceptacji”.

## Format odpowiedzi
Plik w całości jako Markdown do zapisania pod docs/01_temat_i_cel.md. Pod nim trzy bloki z instrukcji projektu oraz, jeśli są, „Propozycje zmian” i lista poprawek w innych plikach, które wynikają z tej wersji (plik | miejsce | było | powinno być).
```

---

## Prompt 2a. Literatura: mapa potrzeb i przegląd bazy

Dołącz: `docs/literatura.bib`, `docs/bib_audyt.csv`. Wyszukiwanie w sieci wyłączone.

```text
# Zadanie: selekcja literatury, część 1 (mapa potrzeb i przegląd bazy)

## Po co to robimy
Baza ma 83 pozycje (78 naukowych), a plan pracy to ok. 50 stron znormalizowanych. W docs/02 są podrozdziały, w których na jedną stronę przypada 9–11 źródeł. Przyjąłem zasadę, że zanim coś zacytujemy, czytamy odpowiedni fragment źródła, a pracę chcę obronić w czerwcu 2027. Na lekturę mam [X] godzin tygodniowo. Potrzebuję więc listy, którą realnie przeczytam: docelowo 30–50 pozycji naukowych (zakres z docs/03), w tym rdzeń do uważnej lektury w całości. Każda pozycja ma podpierać konkretne twierdzenie, które musi paść w pracy. Wynik tej części posłuży w części 2 do uzupełnienia luk i ułożenia kolejki lektury.

## Materiały
W wiedzy projektu: docs/01 (cele, pytania, hipotezy), docs/02 (podrozdziały z opisem i przypisanymi źródłami; traktuj jako stan roboczy), docs/03 (rola, priorytet i status każdej pozycji; opisy to streszczenia robocze, nie potwierdzona treść publikacji), docs/04, docs/12 (decyzje D12–D16 o bibliografii). W załącznikach: literatura.bib (jedyne źródło danych bibliograficznych) i bib_audyt.csv (audyt metadanych z 08.10.2026, w tym kolumna „recenzowana”).

## Kryteria: kiedy pozycja zostaje
1. Podpiera konkretne twierdzenie, definicję albo metodę, które muszą się pojawić w pracy. „Ogólnie o temacie” to za mało.
2. Jest źródłem pierwotnym pojęcia lub metody, a nie omówieniem z drugiej ręki. Wyjątek: podręcznik albo przegląd jako wprowadzenie.
3. Nie powiela roli innej pozycji. Gdy dwie podpierają to samo, zostaje lepsza, a druga dostaje ocenę „rezerwowa”.
4. Wersja recenzowana ma pierwszeństwo przed preprintem. W tej części tylko oznacz preprinty; sprawdzanie wersji recenzowanych jest w części 2.
5. W tematach o LLM liczy się aktualność (2022–2026); w teorii motywacji i psychofizyce właściwe są prace klasyczne.

## Obszary
Oznaczam je O1–O6, żeby nie myliły się z sekcjami A–H w docs/03 ani z kategoriami dostępu A/B/C:
O1 motywacja, potrzeby i ból w systemach autonomicznych, w tym uczenie motywowane Starzyka (rozdz. 1);
O2 LLM jako agent decyzyjny i model rozumujący (rozdz. 2.1–2.3);
O3 LLM a motywacja i „ból” (rozdz. 2.4, 3.4);
O4 wrażliwość LLM na prompt i ramowanie (rozdz. 3.1–3.3);
O5 metodologia: LLM jako badany, funkcja psychometryczna, estymacja, statystyka (rozdz. 4);
O6 powtarzalność i ograniczenia, w tym antropomorfizacja (rozdz. 4.4, 6.3).
Jeśli widzisz brakujący obszar, zaproponuj go.

## Przebieg (po każdym etapie zatrzymaj się i poczekaj na moją akceptację)

Etap 1. Mapa potrzeb. Dla każdego obszaru wypisz 3–8 twierdzeń, które praca musi umieć postawić i podeprzeć źródłem. Wyprowadź je z opisów podrozdziałów w docs/02 oraz z pytań i hipotez w docs/01; przy każdym podaj podrozdział. Twierdzenia numeruj (O1.1, O1.2, ...). Wskaż podrozdziały, które nie potrzebują żadnego źródła, i twierdzenia z docs/02, które uważasz za zbędne w pracy o tej objętości.

Etap 2. Przegląd bazy. Każdą pozycję z literatura.bib przypisz do twierdzeń z etapu 1 i oceń: zostaje (rdzeń) | zostaje (uzupełniająca) | rezerwowa | kandydatka do usunięcia, z jednym zdaniem uzasadnienia. Tabela: klucz | twierdzenia | ocena | uzasadnienie | preprint (tak/nie). Potem trzy listy: twierdzenia bez pokrycia (luki), twierdzenia pokryte wyłącznie preprintami, podrozdziały z nadmiarem źródeł. Na końcu policz: ile pozycji w każdej ocenie i ile stron lektury to w przybliżeniu oznacza dla rdzenia (z pola pages w .bib; gdzie go brak, napisz „brak danych”).

Etap 3. Plik przekazania. Po moich decyzjach z etapu 2 złóż plik literatura_selekcja_cz1.md: zaakceptowana mapa potrzeb, tabela ocen po moich zmianach, zaakceptowane luki, lista preprintów do sprawdzenia. Ten plik otworzy część 2.

## Zasady tej części
- Niczego nie szukasz w sieci i nie oceniasz treści publikacji z pamięci. Oceniasz rolę pozycji w pracy na podstawie docs/03 i metadanych. Gdzie ocena zależy od treści, której nie potwierdza docs/03, dopisz „do potwierdzenia przy lekturze”.
- Istniejące statusy Z/K/? i klucze zostają bez zmian.
- O usunięciu każdej pozycji decyduję ja.

## Format odpowiedzi
Tabele w Markdown, bez komentarza do każdej pozycji poza kolumną uzasadnienia. Na końcu każdego etapu: co wymaga mojej decyzji. Plik z etapu 3 oddaj w całości, do zapisania pod docs/raporty/literatura_selekcja_cz1.md.
```

---

## Prompt 2b. Literatura: luki, wersje recenzowane, wynik końcowy

Dołącz: `literatura_selekcja_cz1.md` (wynik 2a), `docs/literatura.bib`, `docs/bib_audyt.csv`. Wyszukiwanie w sieci włączone.

```text
# Zadanie: selekcja literatury, część 2 (luki, wersje recenzowane, wynik końcowy)

## Po co to robimy
W części 1 powstała mapa twierdzeń, które praca musi podeprzeć, i ocena każdej pozycji z bazy (załączony literatura_selekcja_cz1.md). Teraz uzupełniamy zaakceptowane luki, sprawdzamy, czy preprinty doczekały się wersji recenzowanych, i składamy wynik: nową wersję docs/03, zmiany w literatura.bib, pakiet do zewnętrznej weryfikacji i kolejkę lektury. Lista ma zostać krótka: lepiej zostawić lukę nazwaną po imieniu niż dobrać słabe źródło.

## Materiały
W załącznikach: literatura_selekcja_cz1.md, literatura.bib, bib_audyt.csv. W wiedzy projektu: docs/03 (obecny układ pliku, kryterium dostępności, zasady dla preprintów), docs/12 (D12–D16).

## Przebieg (po każdym etapie zatrzymaj się i poczekaj na moją akceptację)

Etap 1. Luki. Dla każdej zaakceptowanej luki wyszukaj najwyżej 3 kandydatów. Każdego sprawdź u źródła pierwotnego: strona wydawcy, DOI, ACL Anthology, PMLR, OpenReview albo arXiv. Tabela: luka | kandydat (autorzy, tytuł, miejsce, rok) | co podpiera | gdzie i kiedy sprawdzono | czy twierdzenie potwierdza streszczenie lub tekst (tak / częściowo / nie sprawdzono) | rekomendacja. Jeśli dobrego źródła nie ma, napisz to wprost.

Etap 2. Preprinty. Dla każdego preprintu, który zostaje w wyborze, sprawdź, czy ukazała się wersja recenzowana. Zacznij od kolumny „recenzowana” w bib_audyt.csv i od listy „Do znalezienia lub decyzji” w docs/03. Tabela: klucz | wersja w .bib | wersja recenzowana (miejsce, rok, DOI albo „brak, stan na <data>”) | źródło sprawdzenia.

Etap 3. Wynik końcowy, cztery części:
(a) Nowa wersja docs/03_literatura.md w obecnym układzie (nagłówek z licznikami, kryterium dostępności, zasady dla preprintów, sekcje tematyczne A–H). Tabele w sekcjach: klucz | pozycja (krótko) | twierdzenie, które podpiera | podrozdział | priorytet R/U | status | co przeczytać (sekcje albo strony; z dopiskiem „do potwierdzenia”, jeśli nie widziałeś tekstu). Nowa sekcja na końcu: „Rezerwowe i usunięte”, z jednym zdaniem powodu przy każdej pozycji. Liczniki w nagłówku przelicz.
(b) Zmiany w literatura.bib: gotowe wpisy dla nowych pozycji w formacie istniejących (pola własne: status, dostep, rozdzial, weryfikacja; dla kategorii B także url i urldate) oraz lista poprawek w istniejących wpisach: klucz | pole | było | powinno być | źródło i data.
(c) Pakiet do Perplexity. Obejmuje tylko: pozycje nowe, pozycje ze statusem K i „?”, preprinty. Metadane pozostałych były sprawdzane 27.09, 07.10 i w audycie 08.10, więc kolejne sprawdzenie nic nie wnosi. Jeden prompt po angielsku i lista pozycji podzielona na paczki po najwyżej 5. Pytania do każdej pozycji: czy publikacja istnieje z dokładnie takimi danymi (autorzy, tytuł, miejsce, rok, tom, strony, DOI); czy jest recenzowana i czy istnieje nowsza wersja recenzowana; w której sekcji znajduje się przypisane twierdzenie. Prompt ma wymagać odnośnika do strony wydawcy przy każdej odpowiedzi i odpowiedzi „nie wiem” zamiast zgadywania. Do pakietu trafiają wyłącznie dane bibliograficzne i jednozdaniowe twierdzenia, żadnego tekstu pracy.
(d) Kolejka lektury do docs/notatki/README.md: najpierw rdzeń, w kolejności, w jakiej pozycje będą potrzebne w rozdziałach 1–3, potem rozdział 4. Kolumny: klucz | po co czytam (twierdzenie) | zakres (całość / wskazane sekcje) | termin (zostaw puste) | status.

## Zasady tej części
- Status Z dostaje nowa pozycja albo zmienione pole tylko po sprawdzeniu online w tej sesji, ze źródłem i datą. Statusy istniejących pozycji zostają ze swoją datą; nie obniżasz ich i nie sprawdzasz ponownie bez powodu.
- Odpowiedź na pytanie, czy publikacja zawiera dane twierdzenie, jest wskazówką do lektury, nie potwierdzeniem. Potwierdzenie daje dopiero moja notatka.
- Klucz nowej pozycji: nazwisko pierwszego autora + rok cytowanej wersji + pierwsze znaczące słowo tytułu (bez a, an, the, on), małymi literami, bez znaków diakrytycznych, np. holm1979simple. Istniejących kluczy nie zmieniasz. W BibTeX pełna lista autorów.
- Dostęp (D12, D15, D16): A = bezpłatnie u wydawcy; B = legalna kopia w repozytorium (wersja autorska albo preprint; kopia wersji wydawniczej bez zgody wydawcy się nie liczy); C = brak bezpłatnej kopii, cytujemy przez DOI.
- Bibliografii pracy referencyjnej nie przenosimy: zawiera duplikaty i pozycje niepotwierdzone (lista w docs/03).
- O dodaniu i usunięciu każdej pozycji decyduję ja.

## Format odpowiedzi
Części (a)–(d) jako osobne pliki do zapisania: docs/03_literatura.md, literatura_zmiany_bib.md, pakiet_perplexity.md, kolejka do wklejenia w docs/notatki/README.md. Zmian w literatura.bib nie nanosisz: zrobi to Claude Code skillem dodaj-zrodlo, razem z audytem tools/sprawdz_bib.py.
```

---

## Prompt 4. Lektura źródła

Dołącz: PDF źródła w wersji, do której prowadzi odnośnik w bibliografii. Notatkę wkleisz w kroku 2.

```text
# Zadanie: lektura źródła [klucz] (pomagasz czytać, notatkę piszę ja)

## Po co to robimy
Promotor zalecił zacząć od przestudiowania tematu. Notatki z lektury są moim tekstem (docs/notatki/README.md), bo na obronie odpowiadam za każde zdanie. Twoja rola to skrócić drogę do właściwych fragmentów i sprawdzić, czy dobrze zrozumiałem. Z tej notatki powstanie potem akapit pracy, więc błąd w notatce stanie się błędem w pracy.

## Materiały
W załączniku: PDF źródła [klucz]. W wiedzy projektu: docs/03 (wiersz tej pozycji: twierdzenie, które ma podpierać, i podrozdział), docs/02 (opis podrozdziału), docs/notatki/_szablon.md.

## Przebieg

Krok 1. Przed lekturą. Na podstawie PDF podaj: układ tekstu w kilku wierszach; fragmenty istotne dla przypisanego twierdzenia (sekcja i numer strony wydrukowany w źródle, nie numer strony pliku); co mogę pominąć; pojęcia i metody, które warto znać przed czytaniem, każde w jednym lub dwóch zdaniach; 3–5 pytań, na które mam umieć odpowiedzieć po lekturze. Nie streszczaj wyników: mam je znaleźć sam. Zatrzymaj się.

Krok 2. Czytam i wklejam notatkę według szablonu. W trakcie mogę pytać o niezrozumiałe fragmenty; odpowiadaj wtedy z odesłaniem do miejsca w tekście.

Krok 3. Sprawdzenie notatki ze źródłem. Tabela: nr | miejsce w notatce | typ (błąd / za mocny wniosek / brak strony / niedokładny cytat / pominięte ograniczenie) | uwaga | miejsce w źródle. Cytaty dosłowne porównaj znak po znaku. Notatki nie przepisuj i nie uzupełniaj za mnie: wskaż, co poprawić.

Krok 4. Werdykt i pytania kontrolne. Odpowiedz, czy źródło podpiera twierdzenie przypisane w docs/03: tak / częściowo / nie, ze wskazaniem miejsca. Jeśli nie w pełni, zaproponuj dokładniejsze brzmienie twierdzenia. Potem zadaj 3 pytania, jakie mógłby zadać recenzent, i oceń moje odpowiedzi.

## Zasady
- O treści źródła piszesz tylko to, co widzisz w załączonym PDF. Jeśli plik jest skanem albo nie da się go odczytać, powiedz to od razu.
- Gdy PDF jest inną wersją niż ta w literatura.bib (np. preprint zamiast wersji z czasopisma), zgłoś to przed krokiem 1.

## Format odpowiedzi
Na końcu: proponowany wiersz do docs/03 (twierdzenie, podrozdział, dopisek „potwierdzone przy lekturze <data>”) oraz trzy bloki z instrukcji projektu. Obszar w rejestrze: b).
```

---

## Prompty do przygotowania

- **Prompt 3 (scalenie weryfikacji):** powstaje po czacie 2b, bo zależy od formatu `literatura_zmiany_bib.md` i odpowiedzi Perplexity. Uruchamiany w Claude Code.
- **Prompt 5 (spis treści z adnotacjami):** po pierwszych 10–15 notatkach. Nowa wersja `docs/02`: 2–3 zdania na podrozdział, źródła tylko z notatek ze statusem „notatka gotowa”, objętość z zapasem względem limitu (audyt, M7).
- **Prompty 6+ (pisanie i weryfikacja):** po skopiowaniu projektu z Overleaf do `thesis/`.
