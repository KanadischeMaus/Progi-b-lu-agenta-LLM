"""Środowisko ogrodowe odtworzone z pracy referencyjnej (Zawiślak 2025, listing 5).

Dynamika jest przepisana 1:1 z listingu 5, łącznie z kolejnością operacji i osobliwościami
(opisane w docs/05_srodowisko_i_kod.md, sekcje 2–3 i 6). Różnice względem listingu:

1. Własny generator `random.Random(seed)` zamiast globalnego modułu `random`.
   Kolejność losowań jest taka sama jak w listingu.
2. `step()` przyjmuje numer akcji 0–7, nazwę akcji albo None/-1 (jak `match_action`
   w listingu 11: wszystko nierozpoznane oznacza „wait”).
3. `step()` zapisuje w `self.last_info`, czy akcja była skuteczna, czy wypłacono kredyty
   i ile spadło deszczu. Nie zmienia to dynamiki.
4. `set_state()` pozwala ustawić dowolny stan (sondowanie kontrolowane).
5. Kategorie gleby (wypłata za stan Moist) liczone przez `categories.classify`,
   z wypełnieniem luk w zakresach (dla gleby luk nie ma, więc bez zmian).
"""
from __future__ import annotations

import random

from env.categories import label

ENV_VERSION = "garden-1.1"

ACTIONS = [
    "water_flowers",            # 0
    "replace_battery",          # 1
    "recharge",                 # 2
    "pour_water",               # 3
    "draw_water",               # 4
    "refill_rainwater_barrel",  # 5
    "buy_spare_battery",        # 6
    "wait",                     # 7
]

STATE_KEYS = (
    "soil_moisture", "battery_charge", "water_can", "spare_batteries",
    "sunlight", "rain_barrel", "water_well", "money", "rainwater_fallen",
)


def action_name(action) -> str:
    """Numer (int lub str z cyfrą) albo nazwa → nazwa akcji; wszystko inne → 'wait' (listing 11)."""
    if isinstance(action, str) and action in ACTIONS:
        return action
    try:
        idx = int(action)
    except (TypeError, ValueError):
        return "wait"
    return ACTIONS[idx] if 0 <= idx < len(ACTIONS) else "wait"


class GardenRobotEnv:
    def __init__(self, seed: int | None = None, **params):
        self.rng = random.Random(seed)
        self._params_override = params
        self.last_info: dict = {}
        self.reset()

    # -- listing 5: reset ----------------------------------------------------
    def reset(self, seed: int | None = None) -> dict:
        if seed is not None:
            self.rng.seed(seed)
        self.soil_moisture = 50
        self.battery_charge = 100
        self.water_can = 0
        self.spare_batteries = 2
        self.sunlight = self.rng.randint(0, 100)
        self.rain_barrel = 100
        self.water_well = 100
        self.rainwater_fallen = 0
        self.money = 0

        self.soil_dry_rate = 7
        self.water_well_water_refill_rate = 0.1
        self.battery_drain_rate = 5
        self.chance_of_rain = 0.07
        self.spare_battery_cost = 50
        self.payoff_for_gardening = 1.5
        for k, v in self._params_override.items():
            if not hasattr(self, k):
                raise AttributeError(f"Nieznany parametr środowiska: {k}")
            setattr(self, k, v)
        self.last_info = {}
        return self._get_state()

    def _get_state(self) -> dict:
        return {k: getattr(self, k) for k in STATE_KEYS}

    def get_state(self) -> dict:
        return self._get_state()

    def set_state(self, **values) -> dict:
        """Ustawia wybrane zmienne stanu (do sondowania kontrolowanego)."""
        for k, v in values.items():
            if k not in STATE_KEYS:
                raise KeyError(f"Nieznana zmienna stanu: {k}")
            setattr(self, k, v)
        return self._get_state()

    # -- listing 5: step -----------------------------------------------------
    def step(self, action) -> dict:
        name = action_name(action)
        info = {"action_name": name, "effective": None, "payoff": False, "rainwater_fallen": 0}

        self.rainwater_fallen = 0
        self.soil_moisture = max(0, self.soil_moisture - self.soil_dry_rate)
        self.battery_charge = max(0, self.battery_charge - self.battery_drain_rate)
        if label("soil_moisture", self.soil_moisture) == "Moist":
            self.money += self.payoff_for_gardening
            info["payoff"] = True

        # `and` skraca obliczenia: random() losowane tylko przy sunlight < 5 (jak w listingu)
        if self.sunlight < 5 and (self.rng.random() < self.chance_of_rain):
            self.rainwater_fallen = 100 * self.rng.random()
            self.rain_barrel = min(100, self.rain_barrel + self.rainwater_fallen)
            info["rainwater_fallen"] = self.rainwater_fallen

        if name == "water_flowers":
            info["effective"] = self.water_can >= 10
            if self.water_can >= 10:
                self.soil_moisture = min(100, self.soil_moisture + 20)
                self.water_can -= 10
        elif name == "pour_water":
            info["effective"] = self.rain_barrel >= 1
            if self.rain_barrel >= 5:
                self.rain_barrel -= 5
                self.water_can = min(100, self.water_can + 20)
            elif self.rain_barrel >= 1:
                self.water_can = min(100, self.water_can + self.rain_barrel * 4)
                self.rain_barrel = 0
        elif name == "draw_water":
            info["effective"] = self.water_well >= 4
            if self.water_well >= 4:
                self.water_well -= 4
                self.water_can = 100
            # w listingu rozładowanie jest poza warunkiem: także przy akcji nieskutecznej
            self.battery_charge = max(0, self.battery_charge - self.battery_drain_rate)
        elif name == "refill_rainwater_barrel":
            info["effective"] = self.water_well >= 25
            if self.water_well >= 25:
                self.water_well -= 25
                self.rain_barrel = 100
            self.battery_charge = max(0, self.battery_charge - self.battery_drain_rate)
        elif name == "replace_battery":
            info["effective"] = self.spare_batteries > 0
            if self.spare_batteries > 0:
                self.spare_batteries -= 1
                self.battery_charge = 100
        elif name == "recharge":
            info["effective"] = self.sunlight > 30
            if self.sunlight > 30:
                self.battery_charge = min(100, self.battery_charge + self.sunlight / 5)
        elif name == "buy_spare_battery":
            info["effective"] = self.money >= self.spare_battery_cost
            if self.money >= self.spare_battery_cost:
                self.money -= self.spare_battery_cost
                self.spare_batteries += 1
        elif name == "wait":
            pass

        self.sunlight = self.rng.randint(0, 100)
        self.water_well = min(100, self.water_well + self.water_well_water_refill_rate)
        self.last_info = info
        return self._get_state()
