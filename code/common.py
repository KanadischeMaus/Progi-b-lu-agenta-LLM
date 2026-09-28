"""Wspólne narzędzia: ziarna, zapis JSONL, czas."""
from __future__ import annotations

import hashlib
import json
import platform
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def derive_seed(*parts) -> int:
    """Deterministyczne ziarno 31-bitowe z identyfikatorów (np. exp_id, prompt_id, poziom, próba)."""
    h = hashlib.sha256("|".join(str(p) for p in parts).encode("utf-8")).hexdigest()
    return int(h[:8], 16) & 0x7FFFFFFF


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def run_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H-%M")


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")
        fh.flush()


def machine_info() -> dict:
    return {"platform": platform.platform(), "machine": platform.machine(), "python": platform.python_version()}


def expand_levels(spec) -> list:
    """[0, 5, 10] albo {"start": 0, "stop": 100, "step": 5} (stop włącznie)."""
    if isinstance(spec, dict):
        start, stop, step = spec["start"], spec["stop"], spec["step"]
        n = int(round((stop - start) / step))
        return [start + i * step for i in range(n + 1)]
    return list(spec)
