#!/usr/bin/env python3
"""Decision sizing from people's scores, when the Navigator connector is unavailable.

Applies the same rule as the Navigator template nav.sizing (version 1): four criteria, whole
numbers 1 to 10, equal weights, weighted mean, reversibility counted as a cost (11 - score).
It never creates, changes or fills a score. It refuses incomplete score sets, as the engine does.

Input (JSON file or stdin):
{
  "decision": "Owner decides ...",            optional, echoed in the output
  "owner_scorer_id": "Anna Keller",           optional, must be one of the scorers
  "scores": [
    {"scorer_id": "Anna Keller", "criterion_key": "stakes", "value": 8},
    ...
  ]
}

Usage:
  python3 sizing_check.py scores.json            markdown table
  python3 sizing_check.py scores.json --json     machine-readable result
"""

from __future__ import annotations

import json
import sys
from statistics import mean

CRITERIA = [
    ("stakes", "Stakes", "benefit"),
    ("reversibility", "Reversibility (10 = easy to reverse)", "cost"),
    ("commitment_horizon", "Commitment horizon", "benefit"),
    ("functions_involved", "Functions involved", "benefit"),
]
KEYS = [c[0] for c in CRITERIA]


class SizingError(ValueError):
    pass


def _counted(key: str, value: float) -> float:
    direction = dict((c[0], c[2]) for c in CRITERIA)[key]
    return 11 - value if direction == "cost" else value


def load_scores(payload: dict) -> dict[str, dict[str, int]]:
    cells = payload.get("scores")
    if not isinstance(cells, list) or not cells:
        raise SizingError("scores must be a non-empty list of cells")
    grid: dict[str, dict[str, int]] = {}
    for i, cell in enumerate(cells):
        scorer = cell.get("scorer_id")
        key = cell.get("criterion_key")
        value = cell.get("value")
        if not scorer or not isinstance(scorer, str):
            raise SizingError(f"scores[{i}]: scorer_id must name a person")
        if key not in KEYS:
            raise SizingError(f"scores[{i}]: unknown criterion '{key}'; expected one of {KEYS}")
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 10:
            raise SizingError(f"scores[{i}]: value must be a whole number 1 to 10, got {value!r}")
        if key in grid.setdefault(scorer, {}):
            raise SizingError(f"scores[{i}]: {scorer} scored '{key}' twice")
        grid[scorer][key] = value
    missing = {s: [k for k in KEYS if k not in row] for s, row in grid.items()}
    missing = {s: ks for s, ks in missing.items() if ks}
    if missing:
        detail = "; ".join(f"{s}: {', '.join(ks)}" for s, ks in missing.items())
        raise SizingError(
            "every scorer must score every criterion; no score is filled in. Missing: " + detail
        )
    return grid


def size(payload: dict) -> dict:
    grid = load_scores(payload)
    owner = payload.get("owner_scorer_id")
    if owner is not None and owner not in grid:
        raise SizingError(f"owner_scorer_id '{owner}' is not one of the scorers")

    rows = []
    for key, label, direction in CRITERIA:
        values = [grid[s][key] for s in grid]
        rows.append(
            {
                "criterion": key,
                "label": label,
                "direction": direction,
                "group_view": round(mean(values), 1),
                "lowest": min(values),
                "highest": max(values),
                "range": max(values) - min(values),
                "owner_view": grid[owner][key] if owner else None,
            }
        )

    composite = mean(_counted(r["criterion"], r["group_view"]) for r in rows)
    owner_composite = (
        mean(_counted(k, grid[owner][k]) for k in KEYS) if owner else None
    )
    widest = max(rows, key=lambda r: r["range"])

    return {
        "decision": payload.get("decision"),
        "scorers": sorted(grid),
        "indicative": len(grid) < 3,
        "criteria": rows,
        "composite": round(composite, 1),
        "owner_composite": round(owner_composite, 1) if owner_composite is not None else None,
        "widest_disagreement": {"criterion": widest["label"], "range": widest["range"]},
        "field_test_inputs": {
            "a_reversibility_scores": [grid[s]["reversibility"] for s in sorted(grid)],
            "b_commitment_horizon_scores": [grid[s]["commitment_horizon"] for s in sorted(grid)],
            "b_functions_involved_scores": [grid[s]["functions_involved"] for s in sorted(grid)],
            "note": "The method sets no score threshold. Ask the owner (a) is it hard to reverse, "
            "(b) does it commit money or people beyond one planning cycle or across functions.",
        },
        "rule": "Template nav.sizing v1 rule: equal weights, weighted mean, reversibility counted "
        "as 11 minus the score. Computed, not scored: every number above comes from named people.",
    }


def to_markdown(r: dict) -> str:
    lines = []
    if r.get("decision"):
        lines.append(f"**Decision:** {r['decision']}\n")
    lines.append("| Criterion | Group view | Range | Owner's view |")
    lines.append("|---|---|---|---|")
    for c in r["criteria"]:
        owner = "" if c["owner_view"] is None else str(c["owner_view"])
        lines.append(f"| {c['label']} | {c['group_view']} | {c['lowest']} to {c['highest']} | {owner} |")
    owner_comp = "" if r["owner_composite"] is None else str(r["owner_composite"])
    lines.append(f"| **Composite (1 to 10)** | **{r['composite']}** | | {owner_comp} |")
    lines.append("")
    lines.append(f"Scorers: {', '.join(r['scorers'])}.")
    if r["indicative"]:
        lines.append("Fewer than three scorers: the size is indicative.")
    w = r["widest_disagreement"]
    if w["range"] > 0:
        lines.append(f"Widest disagreement: {w['criterion']} (scores {w['range']} points apart). Discuss it; do not average it away.")
    lines.append("")
    lines.append(r["field_test_inputs"]["note"])
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    args = [a for a in argv[1:] if not a.startswith("--")]
    as_json = "--json" in argv
    try:
        raw = open(args[0], encoding="utf-8").read() if args else sys.stdin.read()
        result = size(json.loads(raw))
    except (SizingError, json.JSONDecodeError, OSError) as exc:
        print(f"Not computed: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2) if as_json else to_markdown(result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
