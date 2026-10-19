#!/usr/bin/env python3
"""Value-at-stake helpers. Computes and checks; never creates, changes or fills a score or a figure.

Two commands.

  drivers  People's scores on value drivers (template nav.value_drivers criteria), per driver:
           group view, range, owner's view, and an equal-weight composite with time to value
           counted as a cost (11 - score). Refuses incomplete score sets.

           {"owner_scorer_id": "...",                      optional
            "scores": [{"scorer_id": "...", "driver": "...", "criterion_key":
                        "size_of_prize" | "confidence" | "time_to_value" | "breadth",
                        "value": 1-10}, ...]}

  range    Checks a value range against the Navigator rule (low, mid, high present; low != high;
           unit and basis present) and two consistency checks (low <= mid <= high). Lists figures
           with no stated source class and external figures with no primary source.

           {"low": 1.2, "mid": 2.0, "high": 3.1, "unit": "EUR million per year",
            "basis": "...",
            "figures": [{"name": "rep hours", "value": 6, "class": "M" | "O" | "V" | "H",
                         "source": "2025 time-and-motion study", "external": false}],
            "confidence_group_view": 4.0}                   optional, from the drivers command

Usage:
  python3 value_check.py drivers scores.json [--json]
  python3 value_check.py range range.json [--json]
"""

from __future__ import annotations

import json
import sys
from statistics import mean

CRITERIA = [
    ("size_of_prize", "Size of the prize", "benefit"),
    ("confidence", "Confidence in the estimate", "benefit"),
    ("time_to_value", "Time to value (10 = slow)", "cost"),
    ("breadth", "Breadth", "benefit"),
]
KEYS = [c[0] for c in CRITERIA]
COST = {c[0] for c in CRITERIA if c[2] == "cost"}


class CheckError(ValueError):
    pass


def drivers(payload: dict) -> dict:
    cells = payload.get("scores")
    if not isinstance(cells, list) or not cells:
        raise CheckError("scores must be a non-empty list")
    grid: dict[str, dict[str, dict[str, int]]] = {}
    for i, c in enumerate(cells):
        s, d, k, v = c.get("scorer_id"), c.get("driver"), c.get("criterion_key"), c.get("value")
        if not s or not d:
            raise CheckError(f"scores[{i}]: scorer_id and driver are required")
        if k not in KEYS:
            raise CheckError(f"scores[{i}]: unknown criterion '{k}'; expected one of {KEYS}")
        if isinstance(v, bool) or not isinstance(v, int) or not 1 <= v <= 10:
            raise CheckError(f"scores[{i}]: value must be a whole number 1 to 10, got {v!r}")
        cell = grid.setdefault(d, {}).setdefault(s, {})
        if k in cell:
            raise CheckError(f"scores[{i}]: {s} scored '{k}' for '{d}' twice")
        cell[k] = v
    scorers = sorted({s for d in grid.values() for s in d})
    missing = []
    for d, by_s in grid.items():
        for s in scorers:
            gaps = [k for k in KEYS if k not in by_s.get(s, {})]
            if gaps:
                missing.append(f"{s} on {d}: {', '.join(gaps)}")
    if missing:
        raise CheckError("every scorer must score every criterion for every driver; nothing is filled in. Missing: " + "; ".join(missing))
    owner = payload.get("owner_scorer_id")
    if owner is not None and owner not in scorers:
        raise CheckError(f"owner_scorer_id '{owner}' is not one of the scorers")

    out = []
    for d, by_s in grid.items():
        rows = []
        for k, label, _ in CRITERIA:
            vals = [by_s[s][k] for s in scorers]
            rows.append({"criterion": k, "label": label, "group_view": round(mean(vals), 1),
                         "lowest": min(vals), "highest": max(vals),
                         "owner_view": by_s[owner][k] if owner else None})
        comp = mean((11 - r["group_view"]) if r["criterion"] in COST else r["group_view"] for r in rows)
        widest = max(rows, key=lambda r: r["highest"] - r["lowest"])
        out.append({"driver": d, "criteria": rows, "composite": round(comp, 1),
                    "widest_disagreement": widest["label"],
                    "widest_range": widest["highest"] - widest["lowest"]})
    return {"scorers": scorers, "indicative": len(scorers) < 3, "drivers": out,
            "rule": "Computed, equal weights, time to value counted as 11 minus the score. "
                    "Every number comes from named people. Not a ranking of options."}


def check_range(r: dict) -> dict:
    problems, notes = [], []
    low, mid, high = r.get("low"), r.get("mid"), r.get("high")
    if low is None or mid is None or high is None:
        problems.append("Provide low, likely (mid) and high.")
    else:
        if low == high:
            problems.append("A point estimate is refused: low and high must differ.")
        if not (low <= mid <= high):
            problems.append("Low should not be above likely, and likely should not be above high.")
    if not r.get("unit"):
        problems.append("Provide the unit.")
    if not r.get("basis"):
        problems.append("Provide the basis: how the figures were reached.")
    for f in r.get("figures") or []:
        name = f.get("name", "a figure")
        cls = f.get("class")
        if cls not in ("M", "O", "V", "H"):
            problems.append(f"'{name}' has no evidence class (M, O, V or H).")
        if cls in ("M", "V") and not f.get("source"):
            problems.append(f"'{name}' is marked {cls} but names no source.")
        if f.get("external") and not f.get("source"):
            problems.append(f"'{name}' comes from outside the organization with no primary source: remove it or name the source.")
    conf = r.get("confidence_group_view")
    if conf is not None and low not in (None, 0) and high is not None and mid:
        width = (high - low) / abs(mid) if mid else None
        if width is not None:
            notes.append(f"Range width is {width:.0%} of the likely figure; group confidence was {conf} of 10. "
                         "Ask whether the width matches the confidence; do not change it yourself.")
    return {"ok": not problems, "problems": problems, "notes": notes,
            "wording": "Estimated value at stake; not realized until the outcomes are measured as achieved."}


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] not in ("drivers", "range"):
        print(__doc__)
        return 2
    cmd = argv[1]
    files = [a for a in argv[2:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        payload = json.loads(raw)
        result = drivers(payload) if cmd == "drivers" else check_range(payload)
    except (CheckError, json.JSONDecodeError, OSError) as exc:
        print(f"Not computed: {exc}", file=sys.stderr)
        return 2
    if "--json" in argv or cmd == "range":
        print(json.dumps(result, indent=2))
    else:
        for d in result["drivers"]:
            print(f"\n**{d['driver']}** (composite {d['composite']}, computed)")
            print("| Criterion | Group view | Range | Owner's view |\n|---|---|---|---|")
            for c in d["criteria"]:
                ov = "" if c["owner_view"] is None else c["owner_view"]
                print(f"| {c['label']} | {c['group_view']} | {c['lowest']} to {c['highest']} | {ov} |")
            if d["widest_range"] > 0:
                print(f"Widest disagreement: {d['widest_disagreement']} ({d['widest_range']} points). Discuss; do not average it away.")
        print(f"\nScorers: {', '.join(result['scorers'])}." + (" Fewer than three: indicative." if result["indicative"] else ""))
        print(result["rule"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
