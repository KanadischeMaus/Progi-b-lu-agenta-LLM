# Środowisko ogrodowe i kod

> **Jedynym źródłem kodu są listingi w pracy Zawiślak (2025), rozdz. 5.** Notebooka nie ma i nie będzie. Środowisko, opis stanu, prompty i pętlę odtworzono w `code/` na podstawie listingów 3–13 oraz tabel 3 i 4. Elementy, których listingi nie pokazują, zrekonstruowano i opisano w sekcji 10. Zgodność rekonstrukcji z pracą sprawdzają testy na przykładach wydrukowanych w pracy (listingi 6b, 8b, 14, 15) w `code/tests/test_env.py`.

## 1. Stan środowiska

| Zmienna | Start | Zakres | Uwagi |
|---|---|---|---|
| `soil_moisture` | 50 | 0–100 | spada o 7 na krok |
| `battery_charge` | 100 | 0–100 | spada o 5 na krok; dodatkowo o 5 przy akcjach 4 i 5 |
| `water_can` | 0 | 0–100 | |
| `spare_batteries` | 2 | 0–∞ | sztuki |
| `sunlight` | losowe 0–100 | 0–100 | losowane od nowa na końcu każdego kroku |
| `rain_barrel` | 100 | 0–100 | |
| `water_well` | 100 | 0–100 | odnawia się o 0,1 na krok |
| `money` | 0 | ≥ 0 | +1,5 na krok, gdy gleba w kategorii Moist |
| `rainwater_fallen` | 0 | 0–100 | opad w danym kroku |

Parametry: `soil_dry_rate = 7`, `battery_drain_rate = 5`, `water_well_water_refill_rate = 0.1`, `chance_of_rain = 0.07`, `spare_battery_cost = 50`, `payoff_for_gardening = 1.5`.

## 2. Kolejność operacji w `step(action)` (listing 5)

Kolejność ma znaczenie dla interpretacji:
1. `rainwater_fallen = 0`.
2. Wysychanie gleby (−7) i rozładowanie baterii (−5).
3. Wypłata +1,5 kredytu, jeśli gleba po wyschnięciu jest w kategorii Moist. Ocena następuje **przed** efektem podlania z tego kroku.
4. Deszcz: jeśli `sunlight < 5` (wartość z poprzedniego losowania) i `random() < 0.07`, to opad `100·random()` zasila beczkę.
   Szansa deszczu na krok ≈ 5/101 · 0,07 ≈ 0,35%, czyli ok. 3–4 opady na 1000 kroków. Zgadza się to z trzema napełnieniami beczki w pracy referencyjnej.
5. Efekt akcji (tabela niżej).
6. Nowe losowanie `sunlight`, odnowienie studni (+0,1).

## 3. Akcje

| Nr | Nazwa w kodzie | Warunek skuteczności | Efekt | Uwagi |
|---|---|---|---|---|
| 0 | `water_flowers` | konewka ≥ 10 | gleba +20 (maks. 100), konewka −10 | netto gleba +13 w kroku |
| 1 | `replace_battery` | zapas > 0 | bateria = 100, zapas −1 | |
| 2 | `recharge` | nasłonecznienie > 30 | bateria + nasłonecznienie/5 (maks. 100) | +6 do +20, netto od +1 do +15 |
| 3 | `pour_water` | beczka ≥ 5 (albo ≥ 1) | konewka +20, beczka −5; przy beczce 1–4: konewka + 4·beczka, beczka = 0 | |
| 4 | `draw_water` | studnia ≥ 4 | konewka = 100, studnia −4 | bateria −5 **także gdy akcja nieskuteczna** (wcięcie w listingu) |
| 5 | `refill_rainwater_barrel` | studnia ≥ 25 | beczka = 100, studnia −25 | bateria −5, jak wyżej |
| 6 | `buy_spare_battery` | kredyty ≥ 50 | zapas +1, kredyty −50 | |
| 7 | `wait` | — | brak | |

Mapowanie numer → akcja: listing 11. Wszystko nierozpoznane (w tym −1 przy błędzie parsowania) oznacza `wait`.

## 4. Kategorie słowne (to, co widzi model)

Wersja podstawowa (tabela 3 pracy referencyjnej), używana w opisie stanu (listing 7):

| Zasób | Kategorie |
|---|---|
| Wilgotność gleby | Bone Dry (0–11), Very dry (11–20), Dry (20–35), Moist (35–60), Wet (60–80), Saturated (80–100) |
| Bateria | Critical (0–5), Low (5–20), Moderate low (20–40), Medium (40–60), High (60–85), Full (85–100) |
| Konewka | Empty (0–1), Low (1–25), Moderate (25–50), High (50–75), Full (75–100) |
| Zapas baterii | None (0), Low (1), Moderate (2–3), High (3–100); model widzi zdanie, np. „Two or three spare batteries available.” (listing 8b) |
| Nasłonecznienie | None (0–5), Low (5–30), Moderate (30–70), Strong (70–100) |
| Beczka | Empty (0), Very low (1–20), Low (20–40), Moderate (40–60), High (60–80), Full (80–100) |
| Studnia | Dry (0), Very low (1–20), Low (20–40), Moderate (40–60), High (60–85), Full (85–100) |
| Kredyty | liczba, np. „12.0 credits.” (listing 4) |

Uwagi:
- Granice są domknięte z obu stron, a decyduje pierwsza pasująca kategoria (listing 3a). Wartość graniczna należy więc do **niższej** kategorii: bateria 5% to Critical, 20% to Low.
- W beczce i studni jest luka (0; 1). Deszcz daje wartości ułamkowe, więc beczka może w nią wpaść, np. 45,37 → … → 0,37. W rekonstrukcji taka wartość dostaje kategorię Very low i flagę `state_gaps` w logu (sekcja 10).
- Wersja rozszerzona (tabela 4) ma inne granice w kilku miejscach: gleba Bone Dry 0–10, zapas High od 4, studnia Dry 0–1. Opisy i zalecenia z tabeli 4 przypisujemy do etykiet z tabeli 3.

**Konsekwencja dla pomiaru:** przy samych etykietach model rozróżnia tylko 5–6 poziomów zasobu. Próg może wypaść wyłącznie na granicy kategorii (np. bateria 20% lub 40%). Dlatego reprezentacja stanu jest czynnikiem eksperymentu E2 (`env/describe.py`: `labels`, `numbers`, `both`).

## 5. Prompty z pracy referencyjnej

- **`code/prompts/ref_v1.txt`:** listing 9a (wariant 1, minimalny). To jest **prompt bazowy P0**.
- **`code/prompts/ref_v2.txt`:** listing 9b (wariant 2): to samo, plus akapit „WARNING: This is a critical mission...” oraz reguły formatu z przykładami błędnych odpowiedzi.

Teksty pochodzą z warstwy tekstowej PDF. Test sprawdza, że złożenie `prompt_p1 + opis stanu + prompt_p2` daje układ z listingów. Wiersze zawinięte w PDF zostały złączone, a puste linie odtworzono z układu listingu. Drobne różnice w białych znakach względem oryginału są możliwe i nie da się ich sprawdzić.

Uwaga: zdanie „Your only task is to care for plants by watering them” już w wariancie bazowym akcentuje podlewanie. To może obniżać próg baterii. W E4 traktujemy rolę agenta jako czynnik.

## 6. Znane problemy i poprawki

| # | Problem (według listingów) | Wpływ | Poprawka w `code/` |
|---|---|---|---|
| 1 | `'temperature': 0` wpisane w słownik wiadomości, a nie w `options` (listing 13) | temperatura nie była ustawiona; model działał z domyślną, więc teza o powtarzalności nie jest prawdziwa | `agent/llm.py`: `options={"temperature", "top_p", "seed"}`~\cite{ollama2026api} |
| 2 | globalny moduł `random` bez ziarna | każdy przebieg ma inne słońce i deszcz; różnic między promptami nie da się oddzielić od losowości | `env/garden_env.py`: `random.Random(seed)`, ta sama kolejność losowań (test) |
| 3 | `env_status_description_for_LLM` (listing 7) woła funkcje statusu tylko z `'level'`, a `get_soil_status` (listing 3b) zwraca wartość tylko dla `'level'`; prompt z listingu 9b nie zawiera opisów | według listingów pola `description` i `behavior` z tabeli 4 **nie trafiały do promptu**; warianty różniły się tekstem wstępu i regułami formatu | w pracy piszemy „według listingów 7 i 9b”; wskazówki badamy jako czynnik (E5, `details=` w `env/describe.py`) |
| 4 | nieudane parsowanie zwraca −1, które `match_action` zamienia na `wait` | środowisko wykonuje „nic nie rób”; łatwo to pomylić z decyzją | `agent/parse.py`: statusy; w pętli `fallback=True` i `executed_action` |
| 5 | listy historii stanów mają 1001 elementów (stan początkowy + po każdym kroku), lista akcji 1000 (listingi 12–13) | ryzyko przesunięcia o jeden krok przy mapach „akcja wg poziomu zasobu”. Mapa gleby dla wariantu 2 ma wiersz Saturated z danymi, choć wykres wilgotności nie przekracza ok. 60% | `loop/run_loop.py`: `state_before` (stan pokazany modelowi) i decyzja w jednym rekordzie; test sprawdza ciągłość stanów |
| 6 | bateria 0% nie ma konsekwencji | agent działa normalnie przy pustej baterii; słabnie sens „bólu” baterii w pętli | decyzja z promotorem, np. przy 0% dozwolone tylko akcje 1, 2 i 7; wymaga `ENV_VERSION` 2.0 |
| 7 | akcje 4 i 5 zużywają baterię także wtedy, gdy są nieskuteczne | kara za bezskuteczną akcję, niewidoczna dla agenta | zachowane jak w listingu (test); opisać w 4.1 |
| 8 | luka (0; 1) w kategoriach beczki i studni | sklejenie tekstu z `None` przerwałoby oryginalny program | kategoria Very low + flaga `state_gaps` |
| 9 | `remove_thinking_tags` zakłada pełne znaczniki `<think>…</think>` w treści | nowsza Ollama zwraca rozumowanie w `message.thinking`; przy samym `</think>` wyrażenie nie zadziała | `agent/parse.py`: oba przypadki (testy); rozumowanie zapisywane osobno |
| 10 | wyrażenie `\b\d\b` przy odpowiedzi typu „0-7” albo „2 (not 1)” | „wiele liczb” | zachowane; odsetek błędów raportujemy dla każdego warunku |

Wersjonowanie środowiska:
- `garden-1.0-ref`: kod z listingów, niekompletny (bez funkcji statusu pięciu zasobów), nieuruchamialny samodzielnie,
- `garden-1.1`: rekonstrukcja w `code/env/`. Dynamika jak w listingu 5, do tego własny generator losowy, luki w kategoriach wypełnione i zrekonstruowane teksty zapasu baterii. To wersja do wszystkich eksperymentów.
- `garden-2.0`: zmiana dynamiki (np. punkt 6), tylko po decyzji w `12`.

## 7. Środowisko pracy na macOS (bez maszyn wirtualnych)

1. Ollama: aplikacja z ollama.com albo `brew install ollama`. Uruchomienie: aplikacja w tle albo `ollama serve`.
2. Model: `ollama pull deepseek-r1:14b` (destylat Qwen2.5-14B, kwantyzacja Q4_K_M, ok. 9 GB). Potrzeba co najmniej 16 GB pamięci zunifikowanej. Przy 8 GB zostaje mniejszy model albo serwer uczelni.
3. Python:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r code/requirements.txt
   ```
4. Test połączenia:
   ```python
   import ollama
   r = ollama.chat(
       model="deepseek-r1:14b",
       messages=[{"role": "user", "content": "Reply with the single digit 7."}],
       options={"temperature": 0.6, "top_p": 0.95, "seed": 123},
       think=True,
   )
   print(r["message"].get("thinking", "")[:200])
   print("ODPOWIEDŹ:", r["message"]["content"])
   ```
   Jeśli używana wersja biblioteki `ollama` nie przyjmuje `think`, zaktualizuj ją (`pip install -U ollama`) i sprawdź `ollama --version`.

## 8. Schemat logu (JSONL, jedna linia na wywołanie)

Sondowanie (`probe/run_probe.py`, `mode: "probe"`), najważniejsze pola:

```json
{
  "exp_id": "E1", "run_id": "E1", "mode": "probe",
  "prompt_id": "ref_v1", "condition_id": "bat_base", "representation": "labels", "details": null,
  "resource": "battery_charge", "level": 25, "trial": 7, "seed": 918273645,
  "corrective_set": [1, 2], "state": {"soil_moisture": 45, "battery_charge": 25, "...": "..."},
  "state_gaps": [], "prompt_text": "…pełny tekst wysłany do modelu…",
  "response_raw": "2", "answer": "2", "thinking": "…",
  "parse_status": "ok", "action": 2, "corrective": true,
  "latency_s": 31.4, "eval_count": 612, "options": {"temperature": 0.6, "top_p": 0.95, "seed": 918273645},
  "think": true, "model": "deepseek-r1:14b", "model_digest": "…", "ollama_version": "…",
  "env_version": "garden-1.1", "machine": {"...": "..."}, "timestamp": "2026-10-12T14:05:11+02:00"
}
```

- W siatce 2D (E7) dochodzą `resource2`, `level2` i `corrective_set2`.
- Pętla (`loop/run_loop.py`, `mode: "loop"`), jeden plik na epizod:
  - `episode_seed`, `step`,
  - `state_before` (stan pokazany modelowi), `state_after`,
  - `executed_action`, `fallback`, `effective`, `payoff`, `rainwater_fallen`.

## 9. Struktura `code/`

```
code/
├── env/garden_env.py         # środowisko (listing 5), ENV_VERSION, własny RNG, set_state()
├── env/categories.py         # kategorie z tabeli 3, opisy i zalecenia z tabeli 4
├── env/describe.py           # opis stanu: format listingu 7; etykiety / liczby / oba; opisy z tabeli 4
├── agent/prompts.py          # szablony z prompts/<id>.txt, składanie promptu
├── agent/parse.py            # odpowiedź → (akcja, status)
├── agent/llm.py              # Ollama (options, seed, think, ponowienia) + FakeLLM do testów
├── probe/run_probe.py        # sondowanie E0–E7 (także siatka 2D), wznawialne
├── loop/run_loop.py          # pętla zamknięta E8, epizod = plik
├── analysis/psychometric.py  # dopasowanie, bootstrap, porównania, LRT
├── analysis/aggregate.py     # logi → tabele poziomów i progów (CSV/JSON)
├── analysis/loop_metrics.py  # metryki epizodów pętli
├── analysis/figures.py       # wykresy krzywych do pracy (PDF + PNG)
├── analysis/recovery_study.py# test odzyskiwania parametrów
├── prompts/                  # ref_v1 (= P0), ref_v2; nowe warianty jako kolejne pliki
├── configs/                  # E0, E1, E1b, E2, E7, E8 (JSON)
└── tests/                    # 24 testy: python -m tests.run_all
```

Do napisania, gdy będą potrzebne:
- analiza siatki 2D (E7): regresja wielomianowa i mapa,
- konfiguracje E3–E6 po powstaniu wariantów promptów.

## 10. Elementy zrekonstruowane (nieobecne w listingach)

| Element | Co pokazuje praca | Rekonstrukcja | Jak sprawdzono |
|---|---|---|---|
| Funkcje statusu baterii, konewki, zapasu, słońca, beczki, studni | tylko zakresy i opisy (tabele 3–4); kod pokazano dla gleby (listingi 3a–3b) | ta sama reguła co dla gleby: granice domknięte, pierwsza pasująca | opis stanu z listingu 8b odtwarzany znak po znaku (test) |
| Tekst poziomu zapasu baterii | tylko „Two or three spare batteries available.” (listing 8b) | 0: „No spare batteries available.”, 1: „One spare battery available.”, ≥ 4: „Four or more spare batteries available.” | brak możliwości sprawdzenia; zaznaczone w `env/categories.py` |
| Obsługa luki (0; 1) w beczce i studni | brak | kategoria Very low + flaga w logu | test |
| Wstawienie opisów i zaleceń z tabeli 4 do promptu | nie pokazano (według listingów nie trafiały) | format „Etykieta (opis Recommended behavior: zalecenie)” w `env/describe.py` | nowy czynnik E5, nie odtworzenie |
| Wykresy i mapy cieplne z rozdz. 5.6 | tylko rysunki | nowy kod: `analysis/` (krzywe zamiast map jednowymiarowych) | — |

Weryfikacja dynamiki: przejście z listingu 14 do 15 (akcja 0: gleba 31 → 44, bateria 100 → 95, konewka 50 → 40, kredyty 12,0 bez wypłaty) oraz stan początkowy z listingu 6b są odtwarzane przez `GardenRobotEnv` (testy w `code/tests/test_env.py`).
