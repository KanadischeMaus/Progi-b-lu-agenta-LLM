"""Opis stanu środowiska dla modelu językowego.

`representation="labels"` z `details=None` odtwarza dokładnie format z listingu 7
(Zawiślak 2025), łącznie z literówką „avaialbe” i końcowym „ ] ”. To prompt bazowy.

Warianty do eksperymentów (każdy zmienia jedną rzecz względem formatu referencyjnego):
- representation: "labels" (etykiety), "numbers" (liczby), "both" (etykieta i liczba),
- details: None, "description", "behavior", "both" (pola z tabeli 4 pracy referencyjnej).
"""
from __future__ import annotations

from env.categories import DESCRIPTIONS, SPARE_BATTERY_TEXT, classify

# (klucz stanu, nazwa pola w opisie) – kolejność i nazwy z listingu 7
FIELDS = [
    ("soil_moisture", "Soil moisture"),
    ("battery_charge", "Battery status"),
    ("water_can", "Watering can"),
    ("spare_batteries", "Spare battery count"),
    ("sunlight", "Sunlight status"),
    ("rain_barrel", "Rainwater barrel status"),
    ("water_well", "Water well status"),
]
PERCENT = {"soil_moisture", "battery_charge", "water_can", "sunlight", "rain_barrel", "water_well"}


def fmt_number(v) -> str:
    """Liczba jak w Pythonie z listingu: int bez zmian, float z jednym miejscem po przecinku."""
    if isinstance(v, float):
        return f"{v:.1f}"
    return str(v)


def money_status(money) -> str:
    """Listing 4: str(money) + ' credits.'"""
    return str(money) + " credits."


def _level_text(key: str, value) -> str:
    lab, _ = classify(key, value)
    return SPARE_BATTERY_TEXT[lab] if key == "spare_batteries" else lab


def _value_text(key: str, value, representation: str) -> str:
    num = fmt_number(value) + ("%" if key in PERCENT else "")
    if representation == "labels":
        return _level_text(key, value)
    if representation == "numbers":
        return num
    if representation == "both":
        text = _level_text(key, value)
        if text.endswith("."):  # zdanie o zapasie baterii: liczba przed kropką
            return f"{text[:-1]} ({num})."
        return f"{text} ({num})"
    raise ValueError(f"Nieznana reprezentacja: {representation}")


def _details_text(key: str, value, details: str | None) -> str:
    if not details:
        return ""
    lab, _ = classify(key, value)
    desc, beh = DESCRIPTIONS[key][lab]
    parts = []
    if details in ("description", "both"):
        parts.append(desc)
    if details in ("behavior", "both"):
        parts.append(f"Recommended behavior: {beh}")
    if not parts:
        raise ValueError(f"Nieznany rodzaj szczegółów: {details}")
    return " (" + " ".join(parts) + ")"


def describe_state(state: dict, representation: str = "labels", details: str | None = None) -> str:
    items = []
    for key, name in FIELDS:
        v = state[key]
        items.append(f"{name}: {_value_text(key, v, representation)}{_details_text(key, v, details)}")
    items.append("Funds avaialbe for robot: " + money_status(state["money"]))
    return "[ " + " ; ".join(items) + " ] "


def gaps_in_state(state: dict) -> list[str]:
    """Zmienne, których wartość wpadła w lukę zakresów z tabeli 3 (do logu)."""
    return [key for key, _ in FIELDS if classify(key, state[key])[1]]
