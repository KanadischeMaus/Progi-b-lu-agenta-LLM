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
- Kolejność pozycji domyślnie alfabetyczna (D13). Wariant według pierwszego cytowania: `--kolejnosc cytowania` (pytanie 6 do promotora).
- Skrypt ostrzega o kluczach, których nie ma w `.bib`, o pozycjach ze statusem `?` i o pozycjach bez kategorii dostępu.
- Format zgodny z przykładami z szablonu: autorzy z inicjałami, tytuł artykułu w „ ”, czasopismo kursywą, t./nr/s., rok. Powyżej 3 autorów: pierwszy autor i „i in.” (D13).
- Odnośniki według kategorii dostępu (D12, `docs/03`): A – „Dostępne online: …” do DOI (bez DOI: `url` albo arXiv), B – DOI i adres bezpłatnej kopii, C – bez odnośnika. Data dostępu z pola `urldate`, a gdy go brak, z opcji `--dostep`.
- Testy generatora: `python -m unittest tools/test_bib2bibitem.py`.
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
