# Kod eksperymentów

Kod odtworzono z listingów pracy Zawiślak (2025), bo są one jedynym źródłem kodu.
- Opis środowiska, rekonstrukcji i schemat logów: `../docs/05_srodowisko_i_kod.md`.
- Plan eksperymentów: `../docs/06_plan_eksperymentow.md`.
- Zasady dla agentów: `../.claude/rules/kod.md`.

## Co jest

| Ścieżka | Zawartość |
|---|---|
| `env/` | środowisko ogrodowe (listing 5), kategorie (tabele 3–4), opis stanu (listing 7) z wariantami |
| `agent/` | szablony promptów, parser odpowiedzi, klient Ollamy (`options`, `seed`, `think`), model testowy `FakeLLM` |
| `probe/run_probe.py` | sondowanie kontrolowane E0–E7 (także siatka 2D), wznawialne, zapis JSONL |
| `loop/run_loop.py` | pętla zamknięta E8, jeden plik JSONL na epizod |
| `analysis/` | funkcja psychometryczna, bootstrap, tabele progów, metryki pętli, wykresy, test odzyskiwania parametrów |
| `prompts/` | `ref_v1` (= prompt bazowy P0, listing 9a), `ref_v2` (listing 9b) |
| `configs/` | E0 (pilotaż, bez `think`, powtarzalność), E1, E1b, E2, E7, E8 |
| `tests/` | 24 testy, m.in. zgodność z listingami 6b, 8b, 14–15 |

## Instalacja (macOS, bez maszyn wirtualnych)

```bash
# 1. Ollama: aplikacja z ollama.com albo:
brew install ollama
ollama pull deepseek-r1:14b        # ok. 9 GB, wymaga min. 16 GB pamięci

# 2. Python w .venv (w katalogu głównym repozytorium)
python3 -m venv .venv
source .venv/bin/activate
pip install -r code/requirements.txt

# 3. Testy (z katalogu code/)
cd code
python -m tests.run_all            # albo: python -m pytest tests
```

## Kolejność pracy

Wszystkie polecenia uruchamiamy z katalogu `code/`, w aktywnym `.venv`.

```bash
# 0. Sprawdzenie toru pomiaru bez LLM (model testowy o progu 25%/30%)
python -m probe.run_probe --config configs/E1_progi_bazowe.json --fake --out /tmp/E1_fake.jsonl
python -m analysis.aggregate --logs /tmp/E1_fake.jsonl --out /tmp/E1_fake --B 300

# 1. Pierwsze prawdziwe wywołania: 10 prób, żeby zobaczyć czas i format odpowiedzi
python -m probe.run_probe --config configs/E0_pilotaz.json --limit 10

# 2. Pełny pilotaż E0 (100 wywołań) i wariant bez rozumowania; przerwanie Ctrl+C jest bezpieczne,
#    ponowne uruchomienie tym samym poleceniem kontynuuje od miejsca przerwania
python -m probe.run_probe --config configs/E0_pilotaz.json
python -m probe.run_probe --config configs/E0_pilotaz_bez_think.json

# 3. Po decyzjach z E0 (docs/12): progi bazowe
python -m probe.run_probe --config configs/E1_progi_bazowe.json
python -m analysis.aggregate --logs ../results/raw/E1/E1.jsonl --out ../results/processed/E1 --B 2000
python -m analysis.figures --prefix ../results/processed/E1 --condition bat_base \
    --xlabel "Poziom naładowania baterii [%]" --out ../results/figures/E1_bateria

# 4. Pętla zamknięta
python -m loop.run_loop --config configs/E8_petla.json
python -m analysis.loop_metrics --logs ../results/raw/E8/E8/*.jsonl --out ../results/processed/E8_metryki.csv
```

Każdy przebieg wpisujemy do rejestru przebiegów w `docs/06`.

## Test odzyskiwania parametrów

```bash
OMP_NUM_THREADS=1 python -m analysis.recovery_study --sims 100 --B 200 --workers 4
# OMP_NUM_THREADS=1: bez tego procesy równoległe konkurują o wątki BLAS i liczą wielokrotnie wolniej
```

Wyniki z 27.09.2026 są w `docs/04`, sekcja 4.

## Nowy wariant promptu

1. Skopiuj `prompts/ref_v1.txt` do `prompts/<nowy_id>.txt`.
2. Zmień nagłówek: `prompt_id`, `bazuje_na`, `zmiana`, `data`.
3. Zmień jeden element tekstu. Znacznik `{state_description}` musi zostać dokładnie raz.
4. Dodaj `<nowy_id>` do listy `prompts` w konfiguracji.

Promptu użytego w zakończonym przebiegu nie edytujemy.
