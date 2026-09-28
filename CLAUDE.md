@AGENTS.md

## Ustawienia specyficzne dla Claude Code

- **Skille:**
  - `/napisz-podrozdzial` (tryb A),
  - `/zweryfikuj-tekst` (tryb B),
  - `/dodaj-zrodlo` (nowa pozycja literatury).
- **Reguły ładowane według ścieżek:**
  - `.claude/rules/latex.md` przy plikach w `thesis/`,
  - `.claude/rules/kod.md` przy plikach w `code/`.
- Przed większą zmianą w kodzie (nowy moduł, zmiana logiki środowiska) użyj trybu planowania i pokaż plan autorowi.
- Do niezależnej recenzji gotowego rozdziału uruchom subagenta, który nie widział procesu pisania. Przekaż mu tylko:
  - plik rozdziału,
  - `docs/09_styl_i_rzetelnosc.md`,
  - `docs/08_slownik_pojec.md`,
  - `docs/literatura.bib`.
- W rejestrze AI (`docs/11_rejestr_AI.md`) wpisuj narzędzie jako „Claude Code” i model, który faktycznie działał w sesji (sprawdź `/status` albo `/model`).
- Bibliografię do LaTeX-a generuj skryptem, nie ręcznie:
  `python tools/bib2bibitem.py --bib docs/literatura.bib --main thesis/main.tex --out thesis/bibliografia.tex`
  (nazwy plików `main.tex` i `bibliografia.tex` dopasuj do projektu z Overleaf, patrz `thesis/README.md`).
