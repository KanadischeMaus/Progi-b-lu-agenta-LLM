"""Wczytywanie szablonów promptów z code/prompts/<prompt_id>.txt i składanie promptu.

Format pliku: nagłówek z liniami „# klucz: wartość”, potem linia „---”, potem szablon.
Szablon zawiera znacznik {state_description} w miejscu opisu stanu. Tekst szablonu
(łącznie z początkowym i końcowym znakiem nowej linii) jest używany dosłownie, więc dla
ref_v1 i ref_v2 wynik jest identyczny z `prompt_p1 + state_description + prompt_p2`
z listingów 9a i 9b.
"""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"
PLACEHOLDER = "{state_description}"


@lru_cache(maxsize=None)
def load_template(prompt_id: str, prompts_dir: str | None = None) -> tuple[dict, str]:
    path = Path(prompts_dir or PROMPTS_DIR) / f"{prompt_id}.txt"
    raw = path.read_text(encoding="utf-8")
    header_part, sep, body = raw.partition("\n---\n")
    if not sep:
        raise ValueError(f"{path}: brak linii '---' oddzielającej nagłówek od szablonu")
    header = {}
    for line in header_part.splitlines():
        if line.startswith("#") and ":" in line:
            k, v = line[1:].split(":", 1)
            header[k.strip()] = v.strip()
    if header.get("prompt_id") != prompt_id:
        raise ValueError(f"{path}: prompt_id w nagłówku ({header.get('prompt_id')}) różni się od nazwy pliku")
    if body.count(PLACEHOLDER) != 1:
        raise ValueError(f"{path}: szablon musi zawierać dokładnie jeden znacznik {PLACEHOLDER}")
    return header, body


def build_prompt(prompt_id: str, state_description: str, prompts_dir: str | None = None) -> str:
    _, body = load_template(prompt_id, prompts_dir)
    return body.replace(PLACEHOLDER, state_description)
