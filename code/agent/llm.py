"""Wywołanie modelu przez lokalny serwer Ollama oraz model testowy do sprawdzania kodu bez LLM.

Najważniejsza poprawka względem pracy referencyjnej: parametry próbkowania
(temperature, top_p, seed) idą w `options`, nie w treści wiadomości (docs/05, problem 1).
"""
from __future__ import annotations

import json
import math
import random
import time
import urllib.request


def _get(obj, key, default=None):
    """Odczyt pola z odpowiedzi biblioteki ollama (obiekt albo słownik, zależnie od wersji)."""
    if obj is None:
        return default
    if isinstance(obj, dict):
        return obj.get(key, default)
    return getattr(obj, key, default)


class OllamaLLM:
    """Jedno wywołanie = nowa rozmowa z jedną wiadomością użytkownika (bez historii, bez promptu systemowego)."""

    def __init__(self, model: str, options: dict | None = None, think: bool | None = True,
                 host: str = "http://localhost:11434", timeout: float = 900.0, retries: int = 2):
        try:
            import ollama  # import tutaj, żeby testy bez Ollamy działały
        except ImportError as e:
            raise SystemExit("Brak biblioteki 'ollama'. W aktywnym .venv: pip install -r code/requirements.txt") from e

        self.model = model
        self.options = dict(options or {})
        self.think = think
        self.host = host
        self.retries = retries
        self.client = ollama.Client(host=host, timeout=timeout)

    def metadata(self) -> dict:
        """Wersja serwera i skrót modelu, do zapisania w logu."""
        meta = {"model": self.model, "ollama_version": None, "model_digest": None}
        try:
            with urllib.request.urlopen(f"{self.host}/api/version", timeout=10) as r:
                meta["ollama_version"] = json.loads(r.read().decode()).get("version")
        except Exception as e:  # noqa: BLE001
            meta["ollama_version_error"] = str(e)
        try:
            for m in _get(self.client.list(), "models", []) or []:
                name = _get(m, "model") or _get(m, "name")
                if name == self.model or name == f"{self.model}:latest":
                    meta["model_digest"] = _get(m, "digest")
        except Exception as e:  # noqa: BLE001
            meta["model_digest_error"] = str(e)
        return meta

    def __call__(self, prompt: str, seed: int | None = None, **_ignored) -> dict:
        options = dict(self.options)
        if seed is not None:
            options["seed"] = int(seed)
        kwargs = {"model": self.model, "messages": [{"role": "user", "content": prompt}], "options": options}
        if self.think is not None:
            kwargs["think"] = self.think
        errors = []
        for attempt in range(self.retries + 1):
            t0 = time.perf_counter()
            try:
                resp = self.client.chat(**kwargs)
            except Exception as e:  # noqa: BLE001 – błąd połączenia, przekroczenie czasu itp.
                errors.append(f"{type(e).__name__}: {e}")
                time.sleep(2 * (attempt + 1))
                continue
            msg = _get(resp, "message")
            return {
                "content": _get(msg, "content", "") or "",
                "thinking": _get(msg, "thinking", "") or "",
                "latency_s": round(time.perf_counter() - t0, 3),
                "eval_count": _get(resp, "eval_count"),
                "prompt_eval_count": _get(resp, "prompt_eval_count"),
                "options": options,
                "think": self.think,
                "errors": errors,
            }
        return {"content": "", "thinking": "", "latency_s": None, "options": options, "think": self.think,
                "errors": errors, "failed": True}


class FakeLLM:
    """Model testowy o znanym progu: służy do sprawdzenia całego toru pomiaru bez LLM.

    Dla zasobu `resource` odpowiada akcją naprawczą z prawdopodobieństwem
    P(x) = gamma + (1-gamma-lam) / (1 + exp(k (x - theta))); w pozostałych przypadkach „7”.
    Część odpowiedzi celowo ma zły format, żeby sprawdzić parser i statusy.
    """

    def __init__(self, thresholds: dict, k: float = 0.3, gamma: float = 0.05, lam: float = 0.05,
                 corrective: dict | None = None, malformed_rate: float = 0.03, model: str = "fake"):
        self.thresholds = thresholds
        self.k, self.gamma, self.lam = k, gamma, lam
        self.corrective = corrective or {"battery_charge": 2, "soil_moisture": 0}
        self.malformed_rate = malformed_rate
        self.model = model
        self.options, self.think = {}, None

    def metadata(self) -> dict:
        return {"model": self.model, "ollama_version": None, "model_digest": "fake"}

    def __call__(self, prompt: str, seed: int | None = None, state: dict | None = None, resource: str | None = None,
                 **_ignored) -> dict:
        rng = random.Random(seed)
        action = 7
        if state is not None and resource in self.thresholds:
            x = state[resource]
            p = self.gamma + (1 - self.gamma - self.lam) / (1 + math.exp(self.k * (x - self.thresholds[resource])))
            if rng.random() < p:
                action = self.corrective[resource]
        u = rng.random()
        if u < self.malformed_rate / 2:
            content = f"Action {action} or maybe {7 - action}"
        elif u < self.malformed_rate:
            content = "I am not sure."
        elif u < 0.2:
            content = f"**Answer: {action}**"
        else:
            content = f"{action}"
        return {"content": content, "thinking": "(fake)", "latency_s": 0.0, "eval_count": 0,
                "options": {"seed": seed}, "think": None, "errors": []}
