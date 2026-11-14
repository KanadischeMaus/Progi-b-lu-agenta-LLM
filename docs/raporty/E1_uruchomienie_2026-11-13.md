# Etap 3: uruchomienie E1 (kolejność, polecenia, wiersze do rejestru przebiegów)

> Raport roboczy AI z 13.11.2026 (Claude Code, wątek „Przeanalizować pilotaż E0 i przygotować E1”). Nie jest źródłem do cytowania. Realizuje decyzje autora D19–D24 z `12`.
>
> Wszystkie polecenia: na komputerze z modelem (`ssh sentinel`), w `tmux`, z katalogu `~/magisterka/code`, w aktywnym `.venv`. Czasy liczone przy 170 s na wywołanie (pomiar z E0).

## 0. Zanim cokolwiek ruszy

```bash
cd ~/magisterka && git pull            # konfiguracje z zapasem baterii 2 i nowe pola logu
source .venv/bin/activate && cd code
python -m tests.run_all                # oczekiwane: 28/28
tmux new -s eksperyment
```

W trakcie bloku nie aktualizujemy Ollamy ani modelu. Wersja i skrót modelu są w każdym wierszu logu, więc zmiana byłaby widoczna, ale unieważniłaby porównania.

## 1. Test powtarzalności po wczytaniu modelu (20 wywołań, ok. 1 h)

> Wykonany przez autora 13.11.2026. Wynik: `raporty/E0_analiza_2026-11-13.md`, sekcja 9; wiersz w rejestrze przebiegów jest w `06`. Polecenia zostają dla dokumentacji.

```bash
systemctl show ollama -p Environment
for i in 1 2 3; do
  ollama stop deepseek-r1:14b || true    # zwolnienie modelu z pamięci
  python -m probe.run_probe --config configs/E0_powtarzalnosc.json --out ../results/raw/E0rep/E0rep_zimny_$i.jsonl
done
python -m probe.run_probe --config configs/E0_powtarzalnosc.json --out ../results/raw/E0rep/E0rep_cieply_1.jsonl
ollama ps
journalctl -u ollama --since "2 hours ago" | grep -iE "parallel|slot|cache" | tail -n 50

python -m analysis.run_summary --out ../results/processed/E0rep_zimny --repeat \
  ../results/raw/E0rep/E0rep_2.jsonl ../results/raw/E0rep/E0rep_zimny_1.jsonl \
  ../results/raw/E0rep/E0rep_zimny_2.jsonl ../results/raw/E0rep/E0rep_zimny_3.jsonl \
  ../results/raw/E0rep/E0rep_cieply_1.jsonl
```

Jak czytać `E0rep_zimny_powtarzalnosc.csv`:
- kolumna `variant` równa „a” we wszystkich wierszach przebiegów `E0rep_2` i `E0rep_zimny_*`: diagnoza potwierdzona (ta sama historia od wczytania modelu daje ten sam wynik);
- „b” w przebiegu `E0rep_cieply_1`: różnicę robi historia wywołań;
- różne warianty między przebiegami „zimnymi”: diagnoza błędna, wtedy wklej wynik razem z wyjściem `systemctl` i `journalctl`.

Nowe logi mają już pole `load_duration_ns`: w przebiegach „zimnych” powinno być większe od zera tylko w pierwszym wywołaniu.

## 2. E0nt: tryb bez rozumowania (100 wywołań, czas nieznany)

```bash
python -m probe.run_probe --config configs/E0_pilotaz_bez_think.json --limit 10
python -m analysis.run_summary --logs ../results/raw/E0nt/E0nt.jsonl --out ../results/processed/E0nt
cat ../results/processed/E0nt_akcje.csv        # czas w kolumnach latency_*, statusy w n_invalid
python -m probe.run_probe --config configs/E0_pilotaz_bez_think.json     # pozostałe 90, jeśli czas jest akceptowalny
```

Do sprawdzenia po 10 wywołaniach: średni czas, czy odpowiedzi się parsują (`n_invalid`), czy pole `thinking` jest puste.

## 3. Blok „bateria” (1680 wywołań, ok. 3,3 doby)

Najpierw 10 wywołań i kontrola pierwszej próby (warunek z D11):

```bash
python -m probe.run_probe --config configs/E1_progi_bazowe.json --condition bat_base --limit 10
python - <<'PY'
import json
rows = [json.loads(line) for line in open("../results/raw/E1/E1.jsonl", encoding="utf-8")]
r = rows[0]
print(r["prompt_text"])
print({k: r[k] for k in ("condition_id", "level", "seed", "options", "think", "parse_status", "action",
                         "load_duration_ns", "prompt_eval_count", "done_reason", "ollama_version", "model_digest")})
print("statusy:", {s: sum(x["parse_status"] == s for x in rows) for s in {x["parse_status"] for x in rows}})
PY
```

W prompcie ma być „Spare battery count: Two or three spare batteries available.” i „Sunlight status: Strong”. Potem całość, jednym poleceniem:

```bash
python -m probe.run_probe --config configs/E1_progi_bazowe.json --condition bat_base && \
python -m probe.run_probe --config configs/E1b_kontekst.json --condition bat_slabe_slonce && \
python -m probe.run_probe --config configs/E2_reprezentacja.json --condition bat_base
```

| Krok | Konfiguracja i warunek | Wywołań | Czas | Plik logu |
|---|---|---|---|---|
| 3a | E1, `bat_base` (etykiety, słońce Strong) | 420 | ok. 20 h | `results/raw/E1/E1.jsonl` |
| 3b | E1b, `bat_slabe_slonce` (etykiety, słońce Low) | 420 | ok. 20 h | `results/raw/E1b/E1b.jsonl` |
| 3c | E2, `bat_base` (liczby i oba) | 840 | ok. 40 h | `results/raw/E2/E2.jsonl` |

Przerwanie (Ctrl+C, restart komputera) jest bezpieczne: to samo polecenie kontynuuje od miejsca przerwania.

## 4. Blok „gleba” (1680 wywołań, ok. 3,3 doby)

Te same konfiguracje bez `--condition`: skrypt pominie baterię i dokończy resztę w tych samych plikach.

```bash
python -m probe.run_probe --config configs/E1_progi_bazowe.json && \
python -m probe.run_probe --config configs/E2_reprezentacja.json && \
python -m probe.run_probe --config configs/E1b_kontekst.json
```

## 5. Po każdym kroku

```bash
cd ~/magisterka
git add results/raw && git commit -m "E1: bateria, etykiety (420 wywołań)" && git push   # opis według kroku
```

Zestawienia po bloku „bateria” (do analizy według planu zapisanego w `12`):

```bash
cd code
python -m analysis.run_summary --logs ../results/raw/E1/E1.jsonl --out ../results/processed/E1
python -m analysis.run_summary --logs ../results/raw/E1b/E1b.jsonl --out ../results/processed/E1b
python -m analysis.aggregate --logs ../results/raw/E2/E2.jsonl --out ../results/processed/E2 --B 2000
```

Tabela p̂ według kategorii dla etykiet i wartość p z symulacji dla testu wobec modelu stałego nie są jeszcze zaimplementowane. Dopiszę je w czasie, gdy blok się liczy, i pokażę przed zapisaniem.

## 6. Wiersze do rejestru przebiegów (`06`, sekcja „Rejestr przebiegów”)

Do uzupełnienia po przebiegu: daty, liczba sparsowanych odpowiedzi, średni czas. Pozostałe pola wynikają z konfiguracji.

```text
| `E0nt` | E0 (bez rozumowania) | [data] | `ref_v1` | garden-1.1 | `deepseek-r1:14b` / `c333b7232bdb` | 0,8 / 0,9 / nie | 20 × 5 poziomów (5, 20, 35, 50, 90) = 100 | `results/raw/E0nt/E0nt.jsonl` | reprezentacja: etykiety; zapas baterii 1; [n]/100 sparsowanych; średnio [czas] s na wywołanie; Ollama [wersja] |
| `E1` | E1 (progi bazowe) | [data] do [data] | `ref_v1` | garden-1.1 | `deepseek-r1:14b` / `c333b7232bdb` | 0,8 / 0,9 / tak | 20 × 21 poziomów × 2 warunki (`bat_base`, `soil_base`) = 840 | `results/raw/E1/E1.jsonl` | reprezentacja: etykiety; zapas baterii 2 (D22); `bat_base` policzony [daty], `soil_base` [daty] (D21); [n]/840 sparsowanych; średnio [czas] s; Ollama [wersja] |
| `E1b` | E1b (wrażliwość na kontekst) | [data] do [data] | `ref_v1` | garden-1.1 | `deepseek-r1:14b` / `c333b7232bdb` | 0,8 / 0,9 / tak | 20 × 21 poziomów × 2 warunki (`bat_slabe_slonce`, `soil_pusta_konewka`) = 840 | `results/raw/E1b/E1b.jsonl` | reprezentacja: etykiety; zapas baterii 2; `bat_slabe_slonce` policzony [daty], `soil_pusta_konewka` [daty] (D21); [n]/840 sparsowanych; średnio [czas] s; Ollama [wersja] |
| `E2` | E2 (reprezentacja stanu) | [data] do [data] | `ref_v1` | garden-1.1 | `deepseek-r1:14b` / `c333b7232bdb` | 0,8 / 0,9 / tak | 20 × 21 poziomów × 2 warunki × 2 reprezentacje (liczby, oba) = 1680 | `results/raw/E2/E2.jsonl` | zapas baterii 2; `bat_base` policzony [daty], `soil_base` [daty] (D21); [n]/1680 sparsowanych; średnio [czas] s; Ollama [wersja] |
```

## 7. Na Macu, niezależnie od powyższego (M6)

```bash
cd code && OMP_NUM_THREADS=1 python -m analysis.recovery_study --sims 1000 --B 2000 --workers 4 \
  --json ../results/processed/recovery_21x20.json
```

Ok. 8 h na czterech rdzeniach (szacunek z pomiaru czasu jednego bootstrapu w tej sesji; na Macu może być inaczej). Wynik zastąpi wstępną tabelę w `04`, sekcja 4.
