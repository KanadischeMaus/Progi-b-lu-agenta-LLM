# Tekst pracy (LaTeX, szablon WMiFS)

Ten katalog ma zawierać projekt z Overleaf: plik główny, rozdziały, preambułę, obrazy. Agenci edytują tu pliki `.tex`, a Overleaf służy do kompilacji i podglądu.

## Połączenie z Overleaf: trzy sposoby

**Stan (11.11.2026):** instancja Overleaf PRz nie ma integracji Git ani GitHub, więc obowiązuje sposób 3. Pliki edytujemy w repozytorium, a do Overleaf wgrywamy całość przy kamieniach milowych (np. gotowy rozdział), nie po każdej zmianie.

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
| plik główny | `thesis/Praca_magisterska.tex` |
| rozdziały | `thesis/rozdzialy/00_wstep.tex` … `07_podsumowanie.tex`, `dodatki.tex` |
| bibliografia (generowana) | `thesis/bibliografia.tex` |
| rysunki | `thesis/rysunki/` (powstanie przy pierwszym wykresie) |
| makra robocze | `thesis/makra.tex` (`\dower`, blok `planroboczy`) |
| strona tytułowa, streszczenie, tabela GenAI | `thesis/strona_tytulowa-1.tex`, `thesis/Streszczenie.tex`, `thesis/tabela_genai.tex` |

Szkielet rozdziałów wygenerowano 11.11.2026 z `docs/02_spis_tresci.md` (plan v1). Pod każdym tytułem jest blok `planroboczy` z opisem treści i planowanymi źródłami; usuwamy go, gdy podrozdział jest napisany. Oryginalny szablon: `docs/zrodla/szablon_overleaf.zip`.

## Bibliografia

Szablon używa `thebibliography`. Pozycji nie wpisujemy ręcznie:

```bash
python tools/bib2bibitem.py --bib docs/literatura.bib --main thesis/Praca_magisterska.tex --out thesis/bibliografia.tex
```

- W pliku głównym, w miejscu bibliografii z szablonu, wstaw `\input{bibliografia}`. Jeśli szablon ma własne `\begin{thebibliography}`, użyj opcji `--items-only` i wstaw wynik do środka.
- Kolejność pozycji domyślnie alfabetyczna (D13). Wariant według pierwszego cytowania: `--kolejnosc cytowania` (pytanie 6 do promotora).
- Skrypt ostrzega o kluczach, których nie ma w `.bib`, o pozycjach ze statusem `?` i o pozycjach bez kategorii dostępu.
- Format zgodny z przykładami z szablonu: autorzy z inicjałami, tytuł artykułu w „ ”, czasopismo kursywą, t./nr/s., rok. Powyżej 3 autorów: pierwszy autor i „i in.” (D13).
- Odnośniki według kategorii dostępu (D12 złagodzone przez D16, `docs/03`): A – „Dostępne online: …” do DOI (bez DOI: `url` albo arXiv), B – DOI i adres bezpłatnej kopii, C – „DOI: …”, a bez DOI sam adres z pola `url` (np. stały adres JSTOR), bez daty dostępu. Data dostępu z pola `urldate`, a gdy go brak, z opcji `--dostep`.
- Testy generatora: `python -m unittest tools/test_bib2bibitem.py`.
- Preambuła musi ładować pakiet `url` albo `hyperref`, bo skrypt używa `\url{}`.

## Makro znacznika weryfikacji

Makro jest w `thesis/makra.tex`, ładowanym linią `\input{makra}` przed `\begin{document}` (jedyna zmiana w preambule szablonu; usunąć przed oddaniem pracy):

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
