# Wyniki

```
results/
├── raw/<exp_id>/<run_id>.jsonl   # surowe logi: jedna linia = jedno wywołanie modelu (schemat w docs/05, sekcja 8)
├── processed/                    # tabele pośrednie (CSV/Parquet) generowane skryptami z code/analysis/
└── figures/                      # wykresy do pracy (PDF) i podglądu (PNG), generowane skryptami
```

Zasady:
- Plików w `raw/` nie edytujemy i nie nadpisujemy. Nowy przebieg to nowy `run_id` i wpis w rejestrze przebiegów (`docs/06`).
- Wszystko w `processed/` i `figures/` da się odtworzyć poleceniem z `code/`. W nagłówku pliku albo w nazwie zapisujemy skrypt i `run_id`.
- Liczby w pracy pochodzą z tych plików. W tekście LaTeX komentarz `% źródło: ...` wskazuje plik.
- Duże pliki (> 50 MB): rozważyć Git LFS albo archiwum poza repozytorium z sumą kontrolną w rejestrze przebiegów.
