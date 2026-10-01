---
paths:
  - "thesis/**/*.tex"
  - "thesis/**/*.bib"
---

# Zasady redakcji tekstu w LaTeX-u (szablon WMiFS PRz)

Preambuła szablonu ustawia już marginesy, interlinię, czcionki i styl nagłówków. Nie zmieniaj jej bez zgody autora.

## Struktura

- Rozdział to `\chapter{}`, podrozdział `\section{}`, niższy poziom `\subsection{}`. Głębiej nie schodzimy.
- Tytuły rozdziałów i podpisy rysunków oraz tabel piszemy bez kropki na końcu.
- Przed zasadniczymi częściami (wstęp, rozdziały, podsumowanie, bibliografia, dodatki) stosuj `\cleardoublepage`, zgodnie z instrukcją szablonu.
- Tytuł podrozdziału nie może zostać sam na dole strony. Przy składaniu końcowym sprawdź to w PDF.

## Rysunki, tabele, wzory

- Podpis rysunku stoi pod rysunkiem: `\caption` po `\includegraphics`. Podpis tabeli stoi nad tabelą: `\caption` przed `tabular`.
- Każdy rysunek i każda tabela musi mieć odwołanie w tekście: `rys.~\ref{fig:...}`, `tab.~\ref{tab:...}`. Etykieta stoi zaraz po `\caption`.
- Wykresy wstawiamy jako wektorowe PDF-y wygenerowane skryptem z `code/analysis/`. Nie robimy zrzutów ekranu.
  - Opisy osi po polsku, z jednostkami.
  - Separator dziesiętny to przecinek.
- Wzory numerowane w `equation`, wyśrodkowane. Odwołanie: `wzór~\eqref{eq:...}`.
- Zmienne we wzorach i w tekście zapisujemy tak samo, np. $\theta$, $k$, $\gamma$, $\lambda$ (patrz `docs/08_slownik_pojec.md`).

## Typografia polska

- Po jednoliterowych wyrazach (a, i, o, u, w, z, A, I, O, U, W, Z) stawiaj twardą spację: `w~prompcie`, `z~baterią`.
- Twarda spacja stoi też:
  - między liczbą a jednostką: `20~iteracji`, `14~mld`,
  - między skrótem a numerem: `rys.~3`, `tab.~2`, `s.~45--56`.
- Bez odstępu przed znakiem procentu: `40\%`.
- Cudzysłów polski: „tekst” (znaki „ i ” w UTF-8). Nie używaj prostego `"`.
- Separator dziesiętny w tekście to przecinek: `0,82`. W trybie matematycznym pisz `0{,}82`, żeby nie powstał odstęp.
- Myślnik w zdaniu to półpauza ze spacjami: ` -- `, używana oszczędnie (zob. `docs/09`, nawyk 1). Długiej pauzy `---` nie stosujemy. Zakresy liczb bez spacji: `10--20`.
- Skróty łacińskie i angielskie (np. LLM, RL) rozwijamy przy pierwszym użyciu:
  `duży model językowy (ang.~\textit{large language model}, LLM)`.
- Terminy obcojęzyczne piszemy kursywą przy pierwszym użyciu, później w wersji polskiej, jeśli jest przyjęta w słowniku.

## Kod i prompty w tekście

- W tekście głównym pokazujemy tylko krótkie fragmenty, do ok. 15 linii. Pełne prompty i kod trafiają do dodatków.
- Pełne prompty wstawiamy z plików w `code/prompts/` (np. `\lstinputlisting` albo `verbatim`), żeby praca pokazywała dokładnie to, co dostał model.

## Cytowanie i bibliografia

- Cytuj przez `\cite{klucz}`, z kluczami z `docs/literatura.bib`. Nie wymyślaj kluczy.
- Pliku z `\bibitem` nie edytuj ręcznie. Generuje go `tools/bib2bibitem.py` (instrukcja w `CLAUDE.md` i `thesis/README.md`).
- Odwołanie stawiaj przed kropką: `... progu bólu~\cite{starzyk2017needs}.`

## Znaczniki robocze

- `\dower{treść}` to widoczny w PDF znacznik miejsca do weryfikacji. Makro dodaje autor do preambuły (patrz `thesis/README.md`).
- `% TODO:` to notatka niewidoczna w PDF.
- Przed oddaniem pracy oba wyszukiwania (`\dower`, `TODO`) muszą dać zero wyników.
