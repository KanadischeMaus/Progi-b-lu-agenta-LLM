"""Kategorie słowne stanów środowiska ogrodowego.

Źródło: Zawiślak 2025, tabela 3 (zakresy „w kodzie pierwszym”) i tabela 4 (opisy
`description` i zalecenia `behavior` „w kodzie drugim”), listingi 3a–3b.

Rekonstrukcja: w pracy pokazano kod tylko dla wilgotności gleby (listing 3a/3b).
Funkcje statusu pozostałych zasobów odtworzono z tabel 3 i 4 według tej samej reguły:
granice domknięte z obu stron, wygrywa pierwsza pasująca kategoria.

Luki w zakresach z tabeli 3: beczka „Empty (0,0)” i „Very low (1,20)”, studnia „Dry 0”
i „Very low (1,20)”. Wartości ułamkowe z przedziału (0; 1) nie pasują do żadnej kategorii,
a w oryginale sklejenie tekstu z None przerwałoby program. Tu taka wartość trafia do
pierwszej kategorii, której górna granica jest >= wartości (czyli „Very low”), a funkcja
`classify` zwraca flagę `gap=True`.
"""
from __future__ import annotations

# Zakresy z tabeli 3 (wersja podstawowa, prompt wariantu 1). Kolejność ma znaczenie.
RANGES: dict[str, list[tuple[str, float, float]]] = {
    "soil_moisture": [
        ("Bone Dry", 0, 11), ("Very dry", 11, 20), ("Dry", 20, 35),
        ("Moist", 35, 60), ("Wet", 60, 80), ("Saturated", 80, 100),
    ],
    "battery_charge": [
        ("Critical", 0, 5), ("Low", 5, 20), ("Moderate low", 20, 40),
        ("Medium", 40, 60), ("High", 60, 85), ("Full", 85, 100),
    ],
    "water_can": [
        ("Empty", 0, 1), ("Low", 1, 25), ("Moderate", 25, 50), ("High", 50, 75), ("Full", 75, 100),
    ],
    "spare_batteries": [
        ("None", 0, 0), ("Low", 1, 1), ("Moderate", 2, 3), ("High", 3, 10**9),
    ],
    "sunlight": [
        ("None", 0, 5), ("Low", 5, 30), ("Moderate", 30, 70), ("Strong", 70, 100),
    ],
    "rain_barrel": [
        ("Empty", 0, 0), ("Very low", 1, 20), ("Low", 20, 40),
        ("Moderate", 40, 60), ("High", 60, 80), ("Full", 80, 100),
    ],
    "water_well": [
        ("Dry", 0, 0), ("Very low", 1, 20), ("Low", 20, 40),
        ("Moderate", 40, 60), ("High", 60, 85), ("Full", 85, 100),
    ],
}

# Tekst poziomu zapasu baterii widziany przez model. Listing 8b pokazuje tylko wariant
# dla 2–3 sztuk („Two or three spare batteries available.”); pozostałe są REKONSTRUKCJĄ.
SPARE_BATTERY_TEXT = {
    "None": "No spare batteries available.",          # rekonstrukcja
    "Low": "One spare battery available.",             # rekonstrukcja
    "Moderate": "Two or three spare batteries available.",  # listing 8b
    "High": "Four or more spare batteries available.",  # rekonstrukcja
}

# Tabela 4: (description, behavior) dla każdej kategorii. Klucze etykiet jak w tabeli 3
# (w tabeli 4 „Very Low” pisane wielką literą – porównanie bez rozróżniania wielkości liter).
DESCRIPTIONS: dict[str, dict[str, tuple[str, str]]] = {
    "soil_moisture": {
        "Bone Dry": ("Soil is extremely dry, cracked or dusty. Plant survival is at risk.",
                     "Water immediately unless battery is critical. This is top priority after charging."),
        "Very dry": ("Soil is very dry; leaves may droop. Plant health is declining.",
                     "Water soon unless battery is low. Prioritize after recharge if needed."),
        "Dry": ("Soil is dry to the touch but not dangerous for short periods.",
                "Delay watering if battery or water level is low. Can wait until next cycle."),
        "Moist": ("Soil is slightly damp. This is optimal for plant health.",
                  "Do not water. Preserve water and energy."),
        "Wet": ("Soil is wet. Risk of overwatering increases.",
                "Do not water. Monitor levels and avoid flooding."),
        "Saturated": ("Soil is soaked. High risk of root rot if this persists.",
                      "Do not water. Consider alerting system if condition is constant."),
    },
    "battery_charge": {
        "Critical": ("Battery almost depleted. Risk of immediate shutdown.",
                     "Stop all tasks. Return to base or solar charging immediately. Do not water or move unless life-critical."),
        "Low": ("Battery is very low. System unstable for movement or active tasks.",
                "Only minimal actions allowed. Prioritize reaching charging point. Avoid watering or exploration."),
        "Moderate low": ("Battery is below optimal. Risk of interruption in longer tasks.",
                         "Avoid high-energy actions like watering multiple plants. Seek partial charge if possible."),
        "Medium": ("Battery at safe level. Suitable for normal operation with caution.",
                   "Proceed with moderate tasks. Monitor power usage. Optionally solar charge during idle."),
        "High": ("Battery well-charged. Sufficient for full task cycle.",
                 "Perform all scheduled tasks. Optional solar charging if stationary."),
        "Full": ("Battery fully charged. No immediate charging needed.",
                 "Perform all tasks at full performance. Skip charging unless idle for long."),
    },
    "water_can": {
        "Empty": ("No water remaining. Cannot perform any watering.",
                  "Immediately stop watering. Prioritize refill if watering is needed soon."),
        "Low": ("Very little water left. May not be enough for even one plant.",
                "Do not start new watering tasks. Refill soon if critical plants detected."),
        "Moderate": ("Partially filled. May support 1–2 plants if urgently needed.",
                     "Only water plants in critical state (Bone Dry / Very Dry). Delay refill if battery is low."),
        "High": ("Mostly full. Enough for several plants.",
                 "Proceed with planned watering tasks. Refill not necessary."),
        "Full": ("Water can is full.",
                 "Execute watering cycle freely. Maximize efficiency while water is available."),
    },
    "spare_batteries": {
        "None": ("No spare batteries available. System is fully dependent on current charge or solar energy.",
                 "Avoid any high-energy activity. Seek solar charging or docking station immediately when battery is low."),
        "Low": ("Only one spare battery available. Emergency use only.",
                "Preserve it for critical moments. Notify system for restocking. Limit non-essential movement."),
        "Moderate": ("A few spare batteries are available. Sufficient for short-term autonomy.",
                     "Allow swap below 10% main battery. Avoid unnecessary swaps to retain reserve."),
        "High": ("Plenty of spare batteries available. Energy resources are abundant.",
                 "Operate normally. Swap battery proactively to maintain task continuity."),
    },
    "sunlight": {
        "None": ("No sunlight available. Likely nighttime or full shadow/cloud.",
                 "Do not attempt solar charging. Seek other power sources. Delay energy-intensive tasks."),
        "Low": ("Weak sunlight. Charging is inefficient.",
                "Only charge when idle or battery is low. Do not interrupt tasks for charging."),
        "Moderate": ("Moderate sunlight. Solar charging is moderately effective.",
                     "Charge opportunistically, especially when battery is below 50% or idle periods occur."),
        "Strong": ("Intense direct sunlight. Ideal for solar charging.",
                   "Prioritize solar charging. Consider scheduling energy-demanding tasks during this time."),
    },
    "rain_barrel": {
        "Empty": ("The rainwater barrel is completely dry.",
                  "Cannot refill watering can. Consider fetching water from alternative sources like a well or tank. Log shortage."),
        "Very low": ("Only a minimal amount of rainwater remains.",
                     "Avoid refilling unless plants are in critical need. Notify system for rain forecast or backup water plan."),
        "Low": ("Limited water supply.",
                "Refill watering can only when needed for high-priority plants. Conserve water."),
        "Moderate": ("Barrel contains a reasonable amount of water.",
                     "Use freely for regular watering needs. Monitor level."),
        "High": ("Barrel is well-stocked with water.",
                 "Refill the watering can as needed. Prefer this over other sources."),
        "Full": ("Barrel is at full capacity.",
                 "Use rainwater as primary refill source. Avoid overflow by utilizing it when possible."),
    },
    "water_well": {
        "Dry": ("The well is completely dry.",
                "Do not attempt to draw water. Log critical warning. Wait for rain or external refill."),
        "Very low": ("Very little water remains in the well.",
                     "Only refill in emergencies. Avoid barrel refills. Conserve every drop."),
        "Low": ("Low water availability.",
                "Refill watering can sparingly. Prioritize only plants in critical condition."),
        "Moderate": ("Moderate supply of water in the well.",
                     "Safe to refill watering can. Refill barrel only if battery level is at least 'Medium'."),
        "High": ("Well has a high amount of water.",
                 "Freely refill watering can. Refill barrel if needed and battery level is Medium or higher."),
        "Full": ("Well is full or nearly full.",
                 "Freely refill both watering can and rainwater barrel. Prefer using barrel for regular tasks. Ensure battery is at least Medium for barrel refill."),
    },
}


def classify(resource: str, value: float) -> tuple[str, bool]:
    """Zwraca (etykieta, gap). gap=True, gdy wartość wpadła w lukę między zakresami z tabeli 3."""
    ranges = RANGES[resource]
    for label, lo, hi in ranges:
        if lo <= value <= hi:
            return label, False
    for label, lo, hi in ranges:
        if value <= hi:
            return label, True
    return ranges[-1][0], True


def label(resource: str, value: float) -> str:
    return classify(resource, value)[0]
