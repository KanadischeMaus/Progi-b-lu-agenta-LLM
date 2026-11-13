# Selekcja literatury, część 2, etap 2: preprinty

> Status: wynik etapu 2, przyjęty przez autora 13.11.2026 (decyzje w sekcji 4). Niczego nie zmieniono w `literatura.bib` ani w docs/03.
>
> Uzupełnienie z 13.11.2026: autor odczytał w całości strony arXiv czterech prac w innej sesji Claude 12.11.2026 (sekcja 0 i tabela 1).
>
> Narzędzie: aplikacja Claude (projekt, wątek „Uzupełnić luki w literaturze, część 2”), model claude-fable-5-2. Data sprawdzeń: 12.11.2026.

## 0. Zakres i sposób sprawdzenia

- Sprawdzono siedem preprintów, które zostają w wyborze (sekcja 8 raportu z części 1). Ośmiu preprintów z rezerwy nie sprawdzano, zgodnie z ustaleniem z części 1.
- Dla preprintu „wersja recenzowana” nie ma jeszcze wydawcy, u którego dałoby się ją potwierdzić. Wynik „brak” znaczy więc: nie znalazłem jej w trzech miejscach, czyli na stronie arXiv tej pracy (pola Comments, Journal reference, Related DOI), w rekordzie OpenAlex (typ i lista lokalizacji) oraz w wynikach wyszukiwarki dla pełnego tytułu.
- Czego nie dało się odczytać automatem:
  - DBLP (strona autora i wyszukiwarka) odmawia dostępu;
  - arXiv API odmawia dostępu (robots.txt);
  - dla czterech prac (`bianco2026beyond`, `masumori2025survival`, `tagliabue2025probing`, `schulhoff2024prompt`) strona arXiv wróciła w tej sesji w skróconej postaci, bez wierszy Comments, Journal reference i Related DOI. Autor odczytał te cztery strony w całości w innej sesji Claude 12.11.2026: wierszy Comments, Journal reference i Related DOI na nich nie ma (informacja autora z 13.11.2026, w tej sesji niesprawdzana);
  - Semantic Scholar odpowiedział tylko dla dwóch prac.
- Google Scholar nie był sprawdzany.

## 1. Tabela etapu 2

| Klucz | Wersja w .bib | Wersja recenzowana (miejsce, rok, DOI albo „brak, stan na …”) | Źródło sprawdzenia (12.11.2026) |
|---|---|---|---|
| `keeling2024can` | arXiv 2411.02432v1 | brak, stan na 12.11.2026 | arXiv, pełna strona: jedyna wersja v1 z 1.11.2024, wierszy Journal reference i Related DOI nie ma; OpenAlex W4404355701: typ „preprint”, jedyne źródło arXiv; wyszukiwarka: tylko arXiv i kopie |
| `bianco2026beyond` | arXiv 2602.19159v1 | brak, stan na 12.11.2026 | arXiv, widok skrócony: v1 z 22.02.2026, nowszej wersji strona nie pokazuje; pełna strona (odczyt autora, 12.11.2026): wierszy Comments, Journal reference i Related DOI nie ma; OpenAlex W7131426686: typ „preprint”, jedyne źródło arXiv; wyszukiwarka: arXiv i biblioteka Future Impact Group |
| `masumori2025survival` | arXiv 2508.12920v1 | brak, stan na 12.11.2026 | arXiv, widok skrócony: v1 z 18.08.2025; pełna strona (odczyt autora, 12.11.2026): wierszy Comments, Journal reference i Related DOI nie ma; OpenAlex W4414491860: typ „preprint”, jedyne źródło arXiv; strona publikacji laboratorium Ikegamiego: praca stoi w dziale „Pre Print” z odnośnikiem tylko do arXiv (przeczytana pierwsza połowa strony) |
| `tagliabue2025probing` | arXiv 2509.07961v2 | brak, stan na 12.11.2026 | arXiv, widok skrócony: zgłoszona 9.09.2025, bieżąca wersja v2 z 23.05.2026; pełna strona (odczyt autora, 12.11.2026): wierszy Comments, Journal reference i Related DOI nie ma; OpenAlex W4416068638: cztery lokalizacje, same repozytoria (arXiv, PhilPapers i PhilArchive), żadna z flagą „published” ani „accepted”; rekord PhilArchive TAGPTP bez nazwy czasopisma i bez DOI |
| `li2023large` | arXiv 2307.11760v7 | brak wersji w czasopiśmie ani w materiałach konferencji, stan na 12.11.2026. Krótka wersja (v1) została przyjęta na sympozjum LLM@IJCAI'23; czy miało ono recenzje i materiały: nie sprawdzono | arXiv, pełna strona: siedem wersji, ostatnia v7 z 12.11.2023, pole Comments: „Technical report; … short version (v1) was accepted by LLM@IJCAI'23; 32 pages; …”, wierszy Journal reference i Related DOI nie ma; OpenAlex W4385291101: typ „preprint”; Semantic Scholar: pole venue puste, brak DOI |
| `schulhoff2024prompt` | arXiv 2406.06608v6 | brak, stan na 12.11.2026 | arXiv, widok skrócony: zgłoszona 6.06.2024, bieżąca wersja v6 z 26.02.2025, 31 autorów, tytuł jak w .bib; pełna strona (odczyt autora, 12.11.2026): wierszy Comments, Journal reference i Related DOI nie ma; OpenAlex W4399597451: typ „preprint”, jedyne źródło arXiv; Semantic Scholar: pole venue puste, brak DOI |
| `qwen2024qwen25` | arXiv 2412.15115v2 | brak, stan na 12.11.2026 (raport techniczny) | arXiv, pełna strona: v1 z 19.12.2024, v2 z 3.01.2025, wierszy Comments, Journal reference i Related DOI nie ma; OpenAlex W4405655184: typ „preprint”, jedyne źródło arXiv |

Wniosek: żaden z siedmiu preprintów nie ma znalezionej wersji recenzowanej. Lista twierdzeń opartych wyłącznie na preprintach (sekcja 8 raportu z części 1) zostaje bez zmian.

## 2. Pozycje niepotwierdzone do końca: co i gdzie sprawdzić

Po uzupełnieniu autora z 13.11.2026 z listy wykreślono cztery strony arXiv (`bianco2026beyond`, `masumori2025survival`, `tagliabue2025probing`, `schulhoff2024prompt`). Zostają dwie sprawy; obie trafiają do pakietu dla Perplexity.

| Klucz | Czego nie potwierdziłem | Adres strony do sprawdzenia |
|---|---|---|
| `li2023large` | czy sympozjum LLM@IJCAI'23 miało recenzje i materiały (to rozstrzyga, czy krótką wersję można nazwać recenzowaną) | https://ijcai-23.org/workshops-symposia/ (adres z wyszukiwarki, strony nie czytałem) |
| wszystkie siedem | rekord DBLP: czy poza wpisem „CoRR” jest wpis konferencyjny albo czasopismowy | https://dblp.org (wyszukiwanie po tytule); dla `masumori2025survival` strona autora: https://dblp.org/pid/132/4368.html |

## 3. Poprawki do `literatura.bib` wynikające z etapu 2 (do części 3b)

| Klucz | Pole | Było | Powinno być | Źródło i data |
|---|---|---|---|---|
| `schulhoff2024prompt` | weryfikacja | „data v6 i ewentualna wersja recenzowana nieustalone” | „v6 z 2025-02-26 (strona arXiv, 2026-11-12); wersji recenzowanej nie znaleziono: OpenAlex i Semantic Scholar bez miejsca publikacji, 2026-11-12” (pełne brzmienie w `literatura_zmiany_bib.md`) | arXiv abs 2406.06608, OpenAlex W4399597451, Semantic Scholar; 12.11.2026 |
| `li2023large` | weryfikacja | „… (raport techniczny; krótka wersja: LLM@IJCAI'23) …” | dopisać: „pole Comments arXiv: krótka wersja (v1) przyjęta na LLM@IJCAI'23; wersji w czasopiśmie ani w materiałach konferencji nie znaleziono, 2026-11-12” | arXiv abs 2307.11760, OpenAlex W4385291101, Semantic Scholar; 12.11.2026 |
| pozostałe pięć | weryfikacja | bez daty sprawdzenia wersji recenzowanej | dopisać: „wersji recenzowanej nie znaleziono (arXiv, OpenAlex, wyszukiwarka), 2026-11-12” | jak w tabeli 1 |

Statusy, klucze, wersje w polu `eprint` i kategorie dostępu zostają bez zmian. Dla `tagliabue2025probing` i `bianco2026beyond` bieżąca wersja na arXiv jest ta sama co w .bib.

## 4. Decyzje autora (13.11.2026)

1. „Brak wersji recenzowanej” przyjęty dla wszystkich siedmiu pozycji, stan na 12.11.2026.
2. `li2023large` zostaje jako preprint; cytujemy wersję v7.
3. Sprawdzenie powtarzamy raz, na miesiąc przed oddaniem pracy.
4. `liu2024agentbench` i `kuss2005bayesian`: w docs/03 trafiają do „Rezerwowych i usuniętych”, docs/02 zostaje bez zmian. Z `literatura.bib` nie usuwamy ich teraz, bo są cytowane w docs/02 i w thesis/; wpisy znikną przy przeglądzie planu po lekturze rdzenia (zmiana odłożona).
5. Kolejka lektury jako sama tabela do wklejenia w docs/notatki/README.md.

## 5. Wiersz do docs/11_rejestr_AI.md

| Data | Narzędzie i model | Obszar | Co zrobiono i co zdecydował autor | Pliki |
|---|---|---|---|---|
| 12.11.2026 | aplikacja Claude (projekt), claude-fable-5-2 | b) | Etap 2 części 2 selekcji literatury: sprawdzenie, czy siedem preprintów z wyboru ma wersje recenzowane (arXiv, OpenAlex, Semantic Scholar, wyszukiwarka); wynik: brak dla wszystkich, lista stron do ręcznego sprawdzenia. Decyzje autora (13.11.2026): wynik przyjęty; li2023large zostaje preprintem (v7); powtórka sprawdzenia na miesiąc przed oddaniem pracy | raporty/literatura_selekcja_cz2_etap2.md |
