"""Local FOCUSED session JSON IO.

SYNC: shape mirrors mcps/decision_companion/store.py _prepare_new + stage_schemas 0.3.x.
Engine: focused-local/0.5.0-pilot. No network.
"""

from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any
from uuid import uuid4

STAGES = (
    "how_to_decide",
    "widen_options",
    "gather_intelligence",
    "make_decision",
    "implement",
    "learning_loop",
)

ENGINE = "focused-local/0.5.0-pilot"
SCHEMA_VERSION = "0.3.1"


def _blank_stages() -> dict[str, Any]:
    return {
        stage: {
            "complete": False,
            "payload": {},
            "notes": [],
            "gaps": [],
            "history": [],
        }
        for stage in STAGES
    }


def blank_session(**seed: Any) -> dict[str, Any]:
    row: dict[str, Any] = {
        "session_id": str(uuid4()),
        "stages": _blank_stages(),
        "options": [],
        "ratings": [],
        "criteria": [],
        "premortem": [],
        "roles": {"decide": None, "advise": [], "inform": [], "implement": []},
        "daii": {},
        "skips": [],
        "choice": None,
        "usecase_id": None,
        "decision_type": None,
        "classification": None,
        "events": [],
        "verify_claims": [],
        "navigator_packet_prepared": False,
        "meta": {
            "engine": ENGINE,
            "schema_version": SCHEMA_VERSION,
            "stamp_mode": "FOCUSED-local",
        },
    }
    for key, value in seed.items():
        if key == "meta" and isinstance(value, dict):
            row["meta"].update(value)
        else:
            row[key] = value
    return row


def load_session(path: str | Path) -> dict[str, Any]:
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not data.get("session_id"):
        raise ValueError(f"Invalid FOCUSED session file: {p}")
    data.setdefault("stages", _blank_stages())
    data.setdefault("meta", {})
    data["meta"].setdefault("engine", ENGINE)
    data["meta"].setdefault("schema_version", SCHEMA_VERSION)
    return data


def save_session(row: dict[str, Any], path: str | Path) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    payload = deepcopy(row)
    p.write_text(json.dumps(payload, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    return p


def default_session_path(session_id: str, root: str | Path = "focused-sessions") -> Path:
    return Path(root) / f"{session_id}.focused.json"
