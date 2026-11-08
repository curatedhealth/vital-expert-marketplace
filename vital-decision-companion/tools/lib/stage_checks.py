"""Structural decision checks for a local FOCUSED session. No network."""

from __future__ import annotations

from typing import Any

REQUIRED_HOW = ("statement", "goal", "decider", "deadline")


def structural_gaps(row: dict[str, Any]) -> list[dict[str, str]]:
    gaps: list[dict[str, str]] = []
    stages = row.get("stages") or {}
    how = ((stages.get("how_to_decide") or {}).get("payload")) or {}
    for field in REQUIRED_HOW:
        if not str(how.get(field) or "").strip():
            # also allow top-level mirrors
            if not str(row.get(field) or "").strip():
                gaps.append({"code": f"missing_{field}", "message": f"missing {field}", "field": field})

    options = row.get("options") or []
    if len(options) < 2:
        gaps.append({"code": "too_few_options", "message": "need at least two options (include doing nothing if relevant)", "field": "options"})

    criteria = row.get("criteria") or []
    if not criteria:
        gaps.append({"code": "criteria_missing", "message": "no criteria yet", "field": "criteria"})
    else:
        for c in criteria:
            if not isinstance(c, dict) or c.get("weight") is None:
                gaps.append({"code": "weights_missing", "message": "criterion missing numeric weight", "field": "criteria.weight"})
                break

    ratings = row.get("ratings") or []
    if criteria and options and not ratings:
        gaps.append({"code": "ratings_missing", "message": "no ratings yet", "field": "ratings"})

    return gaps
