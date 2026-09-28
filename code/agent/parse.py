"""Parsowanie odpowiedzi modelu na numer akcji.

Zasada jak w pracy referencyjnej (listing 13): po usunięciu rozumowania szukamy
pojedynczych cyfr wyrażeniem \\b\\d\\b; poprawna odpowiedź zawiera dokładnie jedną.
Różnica: nieudane parsowanie dostaje status, a nie ciche „nic nie rób”.

Statusy: ok | brak_liczby | wiele_liczb | poza_zakresem | pusta
"""
from __future__ import annotations

import re

THINK_BLOCK = re.compile(r"<think>.*?</think>", flags=re.DOTALL)
SINGLE_DIGIT = re.compile(r"\b\d\b")
N_ACTIONS = 8


def strip_thinking(text: str) -> tuple[str, str]:
    """Rozdziela (odpowiedź, rozumowanie). Obsługuje też samo zamknięcie </think>
    (gdy serwer ucina znacznik otwierający)."""
    thinking_parts = THINK_BLOCK.findall(text)
    answer = THINK_BLOCK.sub("", text)
    if "</think>" in answer:
        before, _, after = answer.rpartition("</think>")
        thinking_parts.append(before)
        answer = after
    return answer.strip(), "\n".join(thinking_parts).strip()


def parse_action(content: str) -> tuple[int | None, str]:
    answer, _ = strip_thinking(content or "")
    if not answer:
        return None, "pusta"
    digits = SINGLE_DIGIT.findall(answer)
    if len(digits) == 0:
        return None, "brak_liczby"
    if len(digits) > 1:
        # ta sama cyfra powtórzona (np. „7 ... 7”) też jest niejednoznaczna – jak w listingu 13
        return None, "wiele_liczb"
    value = int(digits[0])
    if not 0 <= value < N_ACTIONS:
        return None, "poza_zakresem"
    return value, "ok"
