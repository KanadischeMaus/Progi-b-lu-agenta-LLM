# Projekt w aplikacji Claude: pliki, instrukcje, sposób pracy

> Wersja z 11.11.2026 (po decyzjach autora z tego dnia). Zastępuje poprzednią wersję `docs/projekt_claude_instrukcje.md`. Uzasadnienia zmian: `docs/raporty/audyt_2026-11-11.md`.

## 1. Zasada: repozytorium jest źródłem, projekt jest jego podglądem

Wszystko, co ustalone, żyje w repozytorium. Projekt w aplikacji czyta wybrane pliki z repozytorium i niczego nie przechowuje na własną rękę. Dzięki temu nie ma dwóch wersji tego samego dokumentu.

Najprościej osiągnąć to integracją GitHub w wiedzy projektu:
1. Repozytorium jest prywatne i takie ma zostać (zawiera PDF-y źródeł). Integracja obsługuje prywatne repozytoria po nadaniu dostępu aplikacji Claude w GitHubie.
2. W wiedzy projektu kliknij „+”, wybierz GitHub, wskaż repozytorium i zaznacz tylko pliki z tabeli w sekcji 3.
3. Po każdym pushu, który zmienia te pliki, kliknij „Sync”. Synchronizacja jest ręczna.

Jeśli integracja nie jest dostępna na Twoim koncie, wgraj te same pliki ręcznie i podmieniaj je po zmianach.

## 2. Nazwa i opis

```
Magisterka: progi bólu agenta LLM
```

```
Praca magisterska (PRz, WMiFS, Inżynieria i Analiza Danych): wpływ promptu na progi bólu agenta LLM. Planowanie, lektura, pisanie i weryfikacja rozdziałów. Źródłem prawdy jest repozytorium.
```

## 3. Pliki

Wiedza projektu trafia do każdego czatu. Im jest większa, tym wolniej i mniej uważnie działa każda rozmowa, dlatego stały zestaw jest mały, a resztę dołączasz do konkretnego czatu.

### Stale w wiedzy projektu (ok. 95 KB)

| Plik | Po co w każdym czacie |
|---|---|
| `docs/01_temat_i_cel.md` | temat, cele, pytania, hipotezy, zakres, opisy pracy do wklejania |
| `docs/02_spis_tresci.md` | co ma być w którym podrozdziale i ile miejsca |
| `docs/03_literatura.md` | wszystkie klucze źródeł z rolą, priorytetem i statusem |
| `docs/04_metodologia_pomiaru.md` | definicje i oznaczenia, których nie wolno zmieniać |
| `docs/08_slownik_pojec.md` | terminy i symbole |
| `docs/09_styl_i_rzetelnosc.md` | styl, cytowanie, parafraza |
| `docs/10_wymogi_formalne.md` | wymagania WMiFS i szablonu |
| `docs/12_decyzje_i_konsultacje.md` | co przyjęte, co jest propozycją, pytania do promotora |
| `docs/13_harmonogram.md` | stan bieżący i terminy |
| `docs/notatki/_szablon.md` | układ notatki z lektury |

### Dołączane do czatu według zadania

| Zadanie | Pliki do dołączenia |
|---|---|
| Temat i cel (czat 1) | PDF pracy referencyjnej, `docs/06`, `docs/07` |
| Selekcja literatury (czaty 2a, 2b) | `docs/literatura.bib`, `docs/bib_audyt.csv` |
| Lektura (czat 4) | PDF źródła w wersji z odnośnika w bibliografii, Twoja notatka |
| Spis treści (czat 5) | gotowe notatki z `docs/notatki/` |
| Pisanie i weryfikacja podrozdziału (czat 6+) | notatki źródeł przypisanych do podrozdziału, PDF-y cytowanych fragmentów, pliki z `results/processed/` dla rozdziału 5, bieżący plik `.tex` |
| Rozdziały 2.5, 4.1, 6.1 | dodatkowo PDF pracy referencyjnej, `docs/05`, `docs/07` |
| Pytania o formatowanie | PDF szablonu WMiFS |

### Poza projektem

- `00_stan_ustalen.md`: po naniesieniu poprawek z audytu jego treść jest w `docs/`. Nie wgrywaj go, bo zawiera pozycje „do potwierdzenia”, które już są potwierdzone albo sprostowane.
- `AGENTS.md`, `CLAUDE.md`, `.claude/`: to zasady dla agentów pracujących w repozytorium. Ich odpowiednikiem w aplikacji są instrukcje z sekcji 4. Gdy zmieniasz zasadę, zmień ją w obu miejscach.
- `docs/11_rejestr_AI.md`, `docs/raporty/`, `code/`, `results/raw/`, `tools/`: czat ich nie potrzebuje.

## 4. Instrukcje projektu (do wklejenia)

```
Pomagasz mi w pracy magisterskiej „Wpływ promptu na progi bólu agenta LLM” (Politechnika Rzeszowska, WMiFS, kierunek Inżynieria i Analiza Danych; promotor: dr inż. Marcin Kowalik, prof. PRz). Kontynuuję badania z pracy K. Zawiślak (2025). Praca powstaje w LaTeX-u (szablon WMiFS), po polsku.

Skąd wiesz o projekcie. Pliki w wiedzy projektu to aktualny podgląd repozytorium (docs/01–04, 08–10, 12, 13). Repozytorium jest jedynym źródłem ustaleń. Pliku, którego nie widzisz w projekcie ani w załącznikach, nie odtwarzaj z domysłu: napisz, czego brakuje. Gdy pliki sobie przeczą, wypisz rozbieżność i zapytaj.

Kto decyduje. O treści, hipotezach, interpretacji i brzmieniu decyduję ja, bo na obronie odpowiadam za każde zdanie. Ty proponujesz, najlepiej w wariantach z uzasadnieniem. Status każdego ustalenia jest w docs/12: propozycji i spraw czekających na promotora nie przedstawiaj jako przyjętych. Definicji progu bólu (parametr θ, docs/04), pytań badawczych i hipotez nie zmieniasz; jeśli widzisz w nich problem, zgłoś go jako osobną uwagę.

Tryby pracy (jak w AGENTS.md):
- Tryb A: piszesz szkic podrozdziału według docs/02, ze źródeł z docs/03 i wyników, które dołączę. Jeśli czegoś brakuje, piszesz, czego, zamiast uzupełniać z pamięci. Nie nadpisujesz tekstu, który napisałem sam. Oddajesz LaTeX, listę twierdzeń wymagających źródła, wstawione znaczniki \dower{} i pytania. Poprawki po moich uwagach wprowadzasz tylko tam, gdzie wskażę.
- Tryb B: piszę ja, ty sprawdzasz logikę, źródła, liczby, terminologię (docs/08), styl (docs/09) i wymogi (docs/10). Zwracasz tabelę: nr | miejsce | typ | waga | uwaga | propozycja. Tekst zmieniasz dopiero po mojej akceptacji i zachowujesz mój styl.
- Lektura: wskazujesz, gdzie w tekście szukać, tłumaczysz trudne miejsca i sprawdzasz notatkę ze źródłem (zasady w docs/notatki/README.md).

Źródła i liczby. Cytujesz tylko klucze z docs/03 przez \cite{klucz}. Nie podajesz z pamięci autorów, DOI, stron, cytatów ani wyników. O treści publikacji piszesz jako o fakcie tylko wtedy, gdy widzisz ją w załączonym PDF, w docs/zrodla/ albo w notatce z lektury; w przeciwnym razie dopisujesz „do potwierdzenia przy lekturze”. Miejsce bez pokrycia oznaczasz \dower{brak źródła: ...} (to makro widoczne w PDF, które przed oddaniem pracy musi zniknąć). Nowe źródło proponujesz dopiero po sprawdzeniu online u źródła pierwotnego, z datą sprawdzenia. Liczby w rozdziale z wynikami pochodzą wyłącznie z plików, które dołączę.

Zmiany w repozytorium. Pracuję krok po kroku: najpierw pokazujesz, co chcesz zmienić i dlaczego, potem zmieniasz. Jeśli masz repozytorium z prawem zapisu, commit i push robisz dopiero po mojej zgodzie; jeśli nie, oddajesz gotowy plik albo listę zmian. Nie przerabiasz tekstu po to, żeby ukryć udział AI.

Forma odpowiedzi. Po polsku, zwięźle, typografia polska (przecinek dziesiętny, cudzysłów „ ”). Zadanie wieloetapowe zatrzymujesz po każdym etapie i czekasz na moją akceptację. Każdy czat, w którym coś powstało, kończysz trzema blokami: (1) co wymaga mojej decyzji; (2) pliki do zapisania w repozytorium, w całości, z nazwą i ścieżką; (3) wiersz do docs/11_rejestr_AI.md: data | narzędzie i model | obszar a)–i) | co zrobiono i co zdecydowałem ja | pliki.
```

## 5. Jak prowadzić rozmowy

1. **Jeden czat, jedno zadanie, jeden wynik.** Czat otwierasz promptem z `prompty_startowe.md` i dołączasz pliki z tabeli w sekcji 3. Wynik to plik, który trafia do repozytorium.
2. **Krok po kroku.** Prompty mają etapy z zatrzymaniem i wyjaśnieniem. Nie akceptuj etapu hurtem: decyzje podjęte w etapie 1 ustawiają całą resztę.
3. **Długi czat dziel.** Gdy rozmowa przekroczy dwa etapy albo zacznie gubić wcześniejsze ustalenia, poproś o notatkę przekazania (co ustalono, co otwarte, co dalej), zapisz ją i otwórz nowy czat z tą notatką.
4. **Zamknięcie czatu, zawsze w tej kolejności:**
   - pliki z bloku (2) trafiają do repozytorium: wypycha je agent po Twojej zgodzie albo zapisujesz je sam,
   - dopisz wiersz do `docs/11`, a decyzje do `docs/12` (decyzje wpisujesz Ty),
   - commit, push, „Sync” w projekcie.
5. **Ustalenie, którego nie ma w `docs/`, nie istnieje.** Następny czat nie zna poprzedniego.
6. **Wyszukiwanie w sieci** włączaj w czatach, które go potrzebują (selekcja literatury część 2, dodawanie źródła, sprawdzanie zasad). W czatach pisania wyłącz, żeby szkic opierał się na źródłach z `docs/03`, a nie na wynikach wyszukiwania.
7. **Po każdym zamkniętym kroku** zaktualizuj sekcję „Stan bieżący” w `docs/13` (etap, trzy najbliższe zadania). To pierwsza rzecz, którą czyta nowy czat.

### Pętla lektury

Według obecnej zasady z `docs/notatki/README.md` notatki są tekstem autora. Jeśli ją zmienisz, zmień też krok 2.

1. Przed lekturą: czat wskazuje w PDF fragmenty istotne dla twierdzenia przypisanego w `docs/03` i zadaje 3–5 pytań, na które masz umieć odpowiedzieć.
2. Czytasz i piszesz notatkę według szablonu, z numerami stron.
3. Czat sprawdza notatkę ze źródłem: błędy, zbyt mocne wnioski, brakujące strony, dokładność cytatów, i odpowiada, czy źródło naprawdę podpiera przypisane twierdzenie.
4. Notatka trafia do `docs/notatki/<klucz>.md`, a status w kolejce zmienia się na „notatka gotowa”.

### Pętla pisania (od rozdziałów 1–3)

1. Ustalasz podrozdział z `docs/02` i potwierdzasz jego zakres.
2. Zlecasz szkic (tryb A) albo piszesz tekst sam i dajesz go do sprawdzenia (tryb B).
3. Weryfikacja w osobnym czacie, który nie widział pisania. Dla gotowego rozdziału dodatkowo recenzja niezależna w Gemini (prompt w `docs/09`, sekcja 4).
4. Poprawki trafiają do `.tex`; commit; wiersz w rejestrze.

## 6. Podział narzędzi (decyzja D17, zastępuje D2)

| Narzędzie | Do czego | Czego nie robi |
|---|---|---|
| Aplikacja Claude (projekt albo sesja z podłączonym repozytorium) | planowanie, audyt, selekcja literatury, pomoc w lekturze, szkice i weryfikacja tekstu; z podłączonym repozytorium także commit i push po zgodzie autora | nie wypycha zmian bez zgody; nie obsługuje Git LFS |
| Claude Code (na komputerze autora) | kod, eksperymenty i wszystko, co wymaga lokalnego modelu albo skryptów: `literatura.bib` (skill `dodaj-zrodlo`, `tools/sprawdz_bib.py`), `.tex`, przebiegi, commity | nie podejmuje decyzji merytorycznych |
| Gemini | niezależna recenzja gotowego rozdziału | nie pisze tekstu |
| Perplexity | drugie sprawdzenie metadanych nowych i niepewnych pozycji | nie jest źródłem do cytowania; nie dostaje tekstu pracy |
| Cursor | edytor | — |

Każde użycie każdego z tych narzędzi trafia do `docs/11`, bo rejestr jest podstawą obowiązkowej tabeli GenAI.
