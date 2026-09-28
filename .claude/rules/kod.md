---
paths:
  - "code/**/*.py"
  - "code/**/*.ipynb"
  - "tools/**/*.py"
---

# Zasady dla kodu eksperymentów

Pełny opis środowiska i schemat logów: `docs/05_srodowisko_i_kod.md`. Plan eksperymentów i rejestr przebiegów: `docs/06_plan_eksperymentow.md`.

## Środowisko pracy

- Python 3.11+ w `.venv` w katalogu głównym repozytorium, zależności w `code/requirements.txt`. Bez maszyn wirtualnych i Dockera.
- Model lokalny przez natywną aplikację Ollama na macOS. Przed każdym dłuższym przebiegiem zapisz w logu:
  - wersję Ollamy,
  - nazwę i skrót (digest) modelu z `ollama list`,
  - sprzęt (model Maca, RAM).

## Zgodność z pracą referencyjną

- `code/env/` odwzorowuje listing 5 i tabele 3–4 pracy Zawiślak (jedyne źródło kodu). Testy w `tests/test_env.py` sprawdzają zgodność z przykładami wydrukowanymi w pracy (listingi 6b, 8b, 14, 15). Nie zmieniaj ich bez decyzji w `docs/12`.
- Elementy zrekonstruowane są oznaczone komentarzem „rekonstrukcja” i opisane w `docs/05`, sekcja 10.
- Testy uruchamiasz poleceniem `python -m tests.run_all` (z `code/`), także bez pytest.

## Losowość i powtarzalność

- Żadnego globalnego `random.*`. Środowisko dostaje własną instancję `random.Random(seed)`, analiza `numpy.random.default_rng(seed)`.
- Parametry modelu przekazujemy tylko w `options`:
  `ollama.chat(model=..., messages=[...], options={"temperature": T, "seed": s, "top_p": p})`.
- Parametr `think` ustawiamy jawnie i zapisujemy w logu.
- Ziarno wywołania wyznaczamy deterministycznie z identyfikatorów (np. hash z `exp_id`, `prompt_id`, `poziom`, `proba`), żeby dało się powtórzyć pojedynczą próbę.
- Zmiana dynamiki środowiska wymaga:
  - podniesienia `ENV_VERSION`,
  - wpisu w `docs/12_decyzje_i_konsultacje.md`.

## Prompty

- Każdy prompt to osobny plik `code/prompts/<prompt_id>.txt` z nagłówkiem (ID, wersja, data, cel).
- Promptu użytego w zakończonym przebiegu nie edytujemy. Zmiana to nowy `prompt_id`.
- Prompt składa się z szablonu i danych stanu. Składanie odbywa się w jednej funkcji, a log zawiera wynikowy, pełny tekst.

## Parsowanie odpowiedzi

- Status parsowania ma jedną z kategorii: `ok`, `brak_liczby`, `wiele_liczb`, `poza_zakresem`, `timeout`.
- Nieudane parsowanie nigdy nie zamienia się po cichu w akcję „nic nie rób”. Pętla zamknięta może wtedy wykonać akcję domyślną, ale log musi to jawnie odnotować.
- Treść rozumowania (`message.thinking` albo blok `<think>`) zapisujemy osobno. Nie parsujemy jej jako odpowiedzi.

## Logi i wyniki

- Surowe logi to `results/raw/<exp_id>/<run_id>.jsonl`, jedna linia na wywołanie modelu. Nigdy ich nie nadpisujemy ani nie edytujemy.
- Długie przebiegi muszą dać się wznowić: skrypt pomija klucze już obecne w logu.
- Przy błędach połączenia robimy najwyżej 2 ponowienia, a każde jest zapisane w logu.
- Dane przetworzone trafiają do `results/processed/`, wykresy do `results/figures/` (PDF do pracy, PNG do podglądu). Każdy plik powstaje ze skryptu.

## Testy

`pytest` dla:
- funkcji kroku środowiska: deterministycznej przy danym ziarnie, z testem każdej akcji,
- parsera odpowiedzi: przypadki z `docs/07_analiza_pracy_referencyjnej.md`, m.in. `**Answer: 0**`, `<think>...</think>7`, dwie liczby,
- dopasowania funkcji psychometrycznej: na danych syntetycznych ze znanymi θ, k, γ, λ estymacja musi odzyskać parametry w granicach błędu.

## Styl

- Nazwy zmiennych i funkcji po angielsku, komentarze i docstringi po polsku albo po angielsku, ale spójnie w pliku.
- Krótkie funkcje, bez logiki ukrytej w notebookach. Notebook służy tylko do podglądu i wywołuje funkcje z modułów.
