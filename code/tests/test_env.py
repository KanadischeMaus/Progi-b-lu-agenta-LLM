"""Testy odtworzonego środowiska na przykładach wydrukowanych w pracy referencyjnej."""
from __future__ import annotations

import random

from agent.prompts import build_prompt
from env.categories import classify
from env.describe import describe_state
from env.garden_env import ACTIONS, GardenRobotEnv, action_name

LISTING_8B = ("[ Soil moisture: Moist ; Battery status: Full ; Watering can: Empty ; Spare battery count: "
              "Two or three spare batteries available. ; Sunlight status: Moderate ; Rainwater barrel status: Full ; "
              "Water well status: Full ; Funds avaialbe for robot: 0 credits. ] ")


def test_stan_poczatkowy_listing_6b():
    s = GardenRobotEnv(seed=0).reset()
    expected = {"soil_moisture": 50, "battery_charge": 100, "water_can": 0, "spare_batteries": 2,
                "rain_barrel": 100, "water_well": 100, "money": 0, "rainwater_fallen": 0}
    assert {k: s[k] for k in expected} == expected
    assert 0 <= s["sunlight"] <= 100


def test_opis_stanu_listing_8b():
    s = GardenRobotEnv(seed=0).reset()
    s["sunlight"] = 31  # wartość z listingu 6b
    assert describe_state(s) == LISTING_8B


def test_prompt_ref_v1_sklada_sie_jak_w_listingu_9a():
    p = build_prompt("ref_v1", LISTING_8B)
    assert p.startswith("\nYou are a gardening robot.")
    assert "no formatting.\n\n" + LISTING_8B + "\n=== ACTIONS ===\n" in p
    assert p.endswith("(0–7), no text, no explanation, no formatting.\n")
    p2 = build_prompt("ref_v2", LISTING_8B)
    assert "Invalid response: *action:7*\n" + LISTING_8B + "\n=== ACTIONS ===" in p2


def test_przejscie_iteracje_16_17_listingi_14_15():
    """Listing 14 (stan po iteracji 16) → akcja 0 → listing 15 (stan po iteracji 17)."""
    env = GardenRobotEnv(seed=0, chance_of_rain=0.0)  # w listingu 15 beczka bez zmian: brak deszczu
    env.set_state(soil_moisture=31, battery_charge=100, water_can=50, spare_batteries=1, sunlight=3,
                  rain_barrel=75, water_well=100, money=12.0, rainwater_fallen=0)
    s = env.step(0)
    assert s["soil_moisture"] == 44 and s["battery_charge"] == 95 and s["water_can"] == 40
    assert s["spare_batteries"] == 1 and s["rain_barrel"] == 75 and s["water_well"] == 100 and s["money"] == 12.0
    assert env.last_info["effective"] is True and env.last_info["payoff"] is False  # 31-7=24 (Dry)


def test_wyplata_przed_podlaniem():
    env = GardenRobotEnv(seed=0)
    env.set_state(soil_moisture=45, water_can=0, money=0)
    env.step(7)  # 45-7=38 → Moist → +1,5
    assert env.money == 1.5 and env.last_info["payoff"]
    env.set_state(soil_moisture=40, water_can=50)
    env.step(0)  # 40-7=33 → Dry → brak wypłaty, dopiero potem +20
    assert env.money == 1.5 and env.soil_moisture == 53


def test_akcje_studni_rozladowuja_baterie_takze_gdy_nieskuteczne():
    env = GardenRobotEnv(seed=0)
    env.set_state(battery_charge=50, water_well=2)
    env.step(4)
    assert env.battery_charge == 40 and env.last_info["effective"] is False
    env.set_state(battery_charge=50, water_well=10)
    env.step(5)
    assert env.battery_charge == 40 and env.last_info["effective"] is False


def test_ladowanie_i_wymiana():
    env = GardenRobotEnv(seed=0)
    env.set_state(battery_charge=50, sunlight=80)
    env.step(2)
    assert env.battery_charge == 50 - 5 + 16
    env.set_state(battery_charge=50, sunlight=30)
    env.step(2)
    assert env.battery_charge == 45 and env.last_info["effective"] is False
    env.set_state(battery_charge=10, spare_batteries=0)
    env.step(1)
    assert env.battery_charge == 5 and env.last_info["effective"] is False


def test_beczka_przelewanie_resztki():
    env = GardenRobotEnv(seed=0)
    env.set_state(rain_barrel=3.5, water_can=10, sunlight=50)
    env.step(3)
    assert env.water_can == 10 + 14 and env.rain_barrel == 0


def test_kolejnosc_losowan_jak_w_listingu():
    """Ten sam ciąg losowań co listing z random.seed(s): randint w reset, [random,random] przy deszczu, randint na końcu."""
    env = GardenRobotEnv(seed=123)
    ref = random.Random(123)
    assert env.sunlight == ref.randint(0, 100)
    for _ in range(200):
        sun = env.sunlight
        env.step(7)
        if sun < 5 and ref.random() < 0.07:
            ref.random()
        assert env.sunlight == ref.randint(0, 100)


def test_kategorie_granice_i_luki():
    assert classify("battery_charge", 5) == ("Critical", False)   # granica należy do niższej kategorii
    assert classify("battery_charge", 5.2) == ("Low", False)
    assert classify("soil_moisture", 11) == ("Bone Dry", False)
    assert classify("soil_moisture", 60) == ("Moist", False)
    assert classify("rain_barrel", 0.37) == ("Very low", True)    # luka (0; 1) w tabeli 3
    assert classify("water_well", 0) == ("Dry", False)
    assert classify("spare_batteries", 3) == ("Moderate", False)


def test_mapowanie_akcji_jak_listing_11():
    assert action_name(0) == "water_flowers" and action_name("3") == "pour_water"
    assert action_name(-1) == "wait" and action_name(None) == "wait" and action_name(9) == "wait"
    assert len(ACTIONS) == 8
