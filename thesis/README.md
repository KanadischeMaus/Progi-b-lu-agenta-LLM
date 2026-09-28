# Tekst pracy (LaTeX, szablon WMiFS)

Ten katalog ma zawierać projekt z Overleaf: plik główny, rozdziały, preambułę, obrazy. Agenci edytują tu pliki `.tex`, a Overleaf służy do kompilacji i podglądu.

## Połączenie z Overleaf: trzy sposoby

Integracja Git i synchronizacja z GitHubem to w Overleaf funkcje płatne (plan premium albo licencja instytucjonalna; warto sprawdzić, czy PRz ją ma).

1. **Overleaf Git (premium).** Menu projektu → Integrations → Git daje adres repozytorium.
   ```bash
   git clone https://git.overleaf.com/<id-projektu> thesis-overleaf
   ```
   Najprościej trzymać ten klon **obok** repozytorium magisterki albo w `thesis/` jako osobne repozytorium. W drugim przypadku dopisz `thesis/*` i `!thesis/README.md` do `.gitignore`. Zmiany wysyła się poleceniem `git push` w katalogu klonu, a Overleaf je od razu widzi.
2. **Synchronizacja z GitHubem (premium).** Overleaf łączy projekt z osobnym repozytorium GitHub (projekt = katalog główny repozytorium). Pracuje się jak w punkcie 1, tylko przez GitHub.
3. **Bez premium (ręcznie).**
   - Overleaf → Menu → Download → Source (ZIP), rozpakować do `thesis/`, commit.
   - Po sesji z agentem wgrać zmienione pliki do Overleaf (Upload, zastąpić).
   - Zasada: jedna strona edytuje naraz. Przed pracą z agentem zawsze pobierz aktualną wersję z Overleaf.

Alternatywa: lokalna kompilacja na Macu (MacTeX + VS Code z rozszerzeniem LaTeX Workshop). Wtedy Overleaf jest potrzebny tylko do podglądu dla promotora.

## Co uzupełnić po skopiowaniu projektu

W tej tabeli agenci szukają ścieżek. Wpisz faktyczne nazwy:

| Element | Ścieżka w projekcie |
|---|---|
| plik główny | `thesis/main.tex` ← `\dower{uzupełnić}` |
| rozdziały | `thesis/rozdzialy/*.tex` ← `\dower{uzupełnić}` |
| bibliografia (generowana) | `thesis/bibliografia.tex` ← `\dower{uzupełnić}` |
| rysunki | `thesis/rysunki/` ← `\dower{uzupełnić}` |

## Bibliografia

Szablon używa `thebibliography`. Pozycji nie wpisujemy ręcznie:

```bash
python tools/bib2bibitem.py --bib docs/literatura.bib --main thesis/main.tex --out thesis/bibliografia.tex
```

- W pliku głównym, w miejscu bibliografii z szablonu, wstaw `\input{bibliografia}`. Jeśli szablon ma własne `\begin{thebibliography}`, użyj opcji `--items-only` i wstaw wynik do środka.
- Kolejność pozycji odpowiada pierwszemu cytowaniu.
- Skrypt ostrzega o kluczach, których nie ma w `.bib`, i o pozycjach ze statusem `?`.
- Format zgodny z przykładami z szablonu: autorzy z inicjałami, tytuł artykułu w „ ”, czasopismo kursywą, t./nr/s., rok. Do tego DOI, jeśli jest (wymóg DOI do potwierdzenia z promotorem; da się łatwo wyłączyć w skrypcie).
- Preambuła musi ładować pakiet `url` albo `hyperref`, bo skrypt używa `\url{}`.

## Makro znacznika weryfikacji

Za zgodą autora dodajemy do preambuły (usunąć przed oddaniem pracy):

```latex
% --- robocze: usunąć przed oddaniem ---
\newcommand{\dower}[1]{\textcolor{red}{[DO WERYFIKACJI: #1]}}
```

Wymaga pakietu `xcolor`; szablon go używa, bo ma przykład „Kolorowy tekst”.

Kontrola przed oddaniem:

```bash
grep -rn "\\\\dower\|TODO" thesis/
```

Wynik musi być pusty.
