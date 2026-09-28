# Słownik pojęć i oznaczeń

Zasada: jedno pojęcie = jedna nazwa w całej pracy. Odpowiednik angielski podajemy kursywą przy pierwszym użyciu w tekście. Nowe pojęcie dopisujemy tu, zanim pojawi się w rozdziale.

## Pojęcia podstawowe

| Termin w pracy | Angielski | Definicja robocza / uwagi |
|---|---|---|
| agent | agent | system, który odbiera stan środowiska i wybiera akcje~\cite{russell2020artificial} |
| środowisko | environment | tu: środowisko ogrodowe (symulacja) |
| stan | state | wektor poziomów zasobów i nasłonecznienia |
| akcja | action | jedna z 8 akcji (0–7), `05_srodowisko_i_kod.md` |
| krok (iteracja) | step | jedno wywołanie modelu i jedna akcja w pętli; w pracy używamy słowa „krok” |
| duży model językowy (LLM) | large language model | skrót LLM jest nieodmienny: „agenta LLM”, „modelu LLM” |
| agent LLM | LLM agent / LLM-based agent | agent, którego decyzje generuje LLM |
| prompt | prompt | tekst wejściowy modelu (instrukcja + opis stanu + lista akcji); odmiana: promptu, promptem, prompty |
| wariant promptu | prompt variant | prompt różniący się od bazowego jednym elementem; identyfikator `prompt_id` |
| prompt bazowy (P0) | baseline prompt | wariant 1 z pracy referencyjnej po poprawkach technicznych |
| ramowanie | framing | sposób przedstawienia sytuacji (neutralny, ból, zagrożenie, nagroda) przy tej samej treści decyzyjnej~\cite{tversky1981framing} |
| rozumowanie | reasoning | tekst generowany przez model przed odpowiedzią (DeepSeek-R1: blok `think`) |
| temperatura | temperature | parametr próbkowania; T = 0 oznacza (w przybliżeniu) wybór najbardziej prawdopodobnego tokenu |
| ziarno | seed | wartość inicjująca generator losowy; osobne dla modelu i środowiska |

## Motywacja i ból

| Termin w pracy | Angielski | Definicja robocza / uwagi |
|---|---|---|
| uczenie motywowane | motivated learning | podejście J. A. Starzyka~\cite{starzyk2017needs} |
| agent motywowany | motivated agent | agent działający w celu redukcji bólu |
| potrzeba | need | predefiniowana wielkość, którą agent ma utrzymywać (tu: energia, wilgotność gleby) |
| ból prymitywny | primitive pain | sygnał związany z potrzebą predefiniowaną; rośnie wraz z odległością od jej zaspokojenia |
| ból abstrakcyjny | abstract pain | ból związany z zasobem potrzebnym do zaspokojenia innej potrzeby (np. pusta konewka) |
| próg bólu | pain threshold | u Starzyka: parametr („agent działa, gdy ból przekracza próg”); **u nas:** $\theta$, estymowany z zachowania |
| rywalizacja bólów | pain competition | wybór bólu do redukcji, gdy aktywnych jest kilka; u Starzyka mechanizm WTA |
| WTA | winner-take-all | „zwycięzca bierze wszystko”: wygrywa najsilniejszy sygnał |
| motywacja wewnętrzna | intrinsic motivation | ~\cite{oudeyer2007intrinsic, ryan2000self} |
| homeostaza | homeostasis | utrzymywanie zmiennych wewnętrznych w zakresie~\cite{keramati2014homeostatic} |
| ból funkcjonalny | functional pain | ból jako sygnał sterujący, bez założeń o odczuwaniu; tak rozumiemy „ból” w całej pracy |

## Pomiar

| Termin w pracy | Angielski | Symbol | Uwagi |
|---|---|---|---|
| poziom zasobu | resource level | $x_r$ | 0–100% (zapas baterii: sztuki) |
| akcja naprawcza | corrective action | $A_r$ | zbiór akcji redukujących ból zasobu $r$ (`04`, sekcja 2) |
| reakcja naprawcza | corrective response | $y$ | $y=1$, gdy wybrana akcja należy do $A_r$ |
| funkcja psychometryczna | psychometric function | $P_r(x)$ | prawdopodobieństwo reakcji naprawczej w funkcji poziomu zasobu |
| próg bólu (zmierzony) | (measured) pain threshold | $\theta$ | punkt środkowy przejścia |
| próg 50% | 50% threshold | $\theta_{0,5}$ | poziom, przy którym $P = 0{,}5$ (miara pomocnicza) |
| ostrość przejścia | slope / steepness | $k$ | razem z szerokością przejścia $w = 2\ln 3/k$ |
| poziom reakcji bez potrzeby | guess / false-alarm rate | $\gamma$ | reakcje naprawcze przy pełnym zasobie |
| poziom zaniedbania | lapse rate | $\lambda$ | brak reakcji przy krytycznym stanie |
| sondowanie kontrolowane | controlled probing | — | pytania o decyzję w sztucznie ustawionych stanach |
| pętla zamknięta | closed-loop simulation | — | pełna symulacja: decyzja zmienia stan |
| epizod naprawczy | corrective episode | — | ciąg kroków z akcjami z $A_r$ |
| poziom rozpoczęcia / zakończenia epizodu | onset / offset level | $x_{on}$, $x_{off}$ | |
| histereza | hysteresis | $x_{off}-x_{on}$ | |
| odpowiedź nieczytelna | unparseable response | — | status parsowania ≠ `ok`; nie jest akcją „nic nie rób” |
| przedział ufności (95%) | confidence interval | PU | bootstrap percentylowy |

## Zasoby i akcje środowiska (polskie nazwy do tekstu)

| W kodzie | W tekście |
|---|---|
| `battery_charge` | poziom naładowania baterii (bateria) |
| `soil_moisture` | wilgotność gleby |
| `water_can` | woda w konewce (konewka) |
| `spare_batteries` | zapasowe baterie (zapas baterii) |
| `sunlight` | nasłonecznienie |
| `rain_barrel` | beczka na deszczówkę (beczka) |
| `water_well` | studnia |
| `money` | kredyty |
| 0 `water_flowers` | podlanie roślin |
| 1 `replace_battery` | wymiana baterii |
| 2 `recharge` | ładowanie słoneczne |
| 3 `pour_water` | napełnienie konewki z beczki |
| 4 `draw_water` | napełnienie konewki ze studni |
| 5 `refill_rainwater_barrel` | napełnienie beczki ze studni |
| 6 `buy_spare_battery` | zakup zapasowej baterii |
| 7 `wait` | brak działania („nic nie rób”) |

Nazwy kategorii stanu (Bone Dry, Critical itd.) zostawiamy w oryginale, bo tak widzi je model. W tekście piszemy je kursywą: *Critical*.
