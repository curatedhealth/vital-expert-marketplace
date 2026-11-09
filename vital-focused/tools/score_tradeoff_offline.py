#!/usr/bin/env python3
"""Add up the person's own weights and ratings, with a ±10-point robustness check.

Two ways to call it (run by full path from the person's working folder):

  python3 <plugin root>/tools/score_tradeoff_offline.py --session focused-sessions/<id>.focused.json
  python3 <plugin root>/tools/score_tradeoff_offline.py --grid '<json>'     (or --grid grid.json, or --grid - for stdin)

Grid JSON (no saved session needed):
  {"criteria": [{"name": "Cost", "weight": 40}, ...],          # optional "direction": "lower_better"
   "options":  ["A", "B", "C"],                               # or [{"id": "A", "name": "Build in-house"}]
   "ratings":  {"A": {"Cost": 2, "Speed": 2}, ...},           # or a list of {"option","criterion","value","rater"}
   "scale":    {"min": 1, "max": 5},                          # optional, default 1 to 5
   "rater":    "Thomas Weber"}                                # optional; defaults to "as given by the person"

Output: totals on a 0 to 100 scale and as a weighted average on the rating scale, the gap
between options, and whether the top-ranked option stays first when any one weight moves by
up to 10 points. It never names a winner.
"""

from __future__ import annotations

import argparse
import json
import sys
sys.dont_write_bytecode = True  # read-only hosts: never write __pycache__
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.score_core import score_session  # noqa: E402
from lib.session_io import load_session  # noqa: E402

DEFAULT_RATER = "as given by the person"


def row_from_grid(grid: dict) -> dict:
    rater = str(grid.get("rater") or DEFAULT_RATER)
    options = []
    for o in grid.get("options") or []:
        options.append(o if isinstance(o, dict) else {"id": str(o), "name": str(o)})
    ratings = grid.get("ratings") or grid.get("scores") or grid.get("cells") or grid.get("matrix") or []
    # ratings nested inside options: [{"name": "A", "ratings": {"Cost": 2}}]
    if not ratings and any(isinstance(o, dict) and isinstance(o.get("ratings") or o.get("scores"), dict) for o in options):
        ratings = {str(o.get("id") or o.get("name")): (o.get("ratings") or o.get("scores")) for o in options if isinstance(o, dict)}
    if isinstance(ratings, dict):
        cells = []
        for opt, per in ratings.items():
            for crit, val in (per or {}).items():
                cells.append({"option": str(opt), "criterion": str(crit), "value": val, "rater": rater})
        ratings = cells
    else:
        norm = []
        for c in ratings:
            if not isinstance(c, dict):
                continue
            val = c.get("value", c.get("score", c.get("rating")))
            norm.append({"option": str(c.get("option") or c.get("option_id") or c.get("name")),
                         "criterion": str(c.get("criterion") or c.get("criteria")),
                         "value": val, "rater": c.get("rater") or rater})
        ratings = norm
    if not options:
        seen = []
        for c in ratings:
            if c["option"] not in seen:
                seen.append(c["option"])
        options = [{"id": s, "name": s} for s in seen]
    crit = grid.get("criteria") or grid.get("weights") or []
    if isinstance(crit, dict):
        crit = [{"name": k, "weight": v} for k, v in crit.items()]
    lower = set(grid.get("lower_better") or [])
    crit = [{**c, "direction": "lower_better"} if c.get("name") in lower and not c.get("direction") else c for c in crit]
    row = {"criteria": crit, "options": options, "ratings": ratings}
    if isinstance(grid.get("scale"), dict):
        row["scale"] = grid["scale"]
    return row


def add_rating_scale_view(out: dict, row: dict) -> dict:
    scale = out.get("method", {}).get("scale") or {"min": 1.0, "max": 5.0}
    lo, hi = float(scale["min"]), float(scale["max"])
    for r in out.get("raters", []):
        for item in r.get("ranked", []):
            item["weighted_average_on_rating_scale"] = round(lo + (hi - lo) * item["total"] / 100.0, 2)
        ranked = r.get("ranked", [])
        r["gaps_between_options"] = [
            {"between": [a["option"], b["option"]], "points_out_of_100": round(a["total"] - b["total"], 2)}
            for a, b in zip(ranked, ranked[1:])
        ]
    return out


def load_grid(arg: str) -> dict:
    if arg == "-":
        return json.load(sys.stdin)
    if arg.lstrip().startswith("{"):
        return json.loads(arg)
    p = Path(arg)
    if p.exists():
        return json.loads(p.read_text())
    return json.loads(arg)


def main() -> int:
    p = argparse.ArgumentParser(description="Add up the person's own weights and ratings (never names a winner).")
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--session", help="path to a saved .focused.json session")
    src.add_argument("--grid", help="grid as JSON text, a JSON file path, or - for stdin")
    args = p.parse_args()
    try:
        row = load_session(args.session) if args.session else row_from_grid(load_grid(args.grid))
    except (OSError, ValueError) as exc:
        print(json.dumps({"scored": False, "gaps": [{"code": "unreadable_input", "message": str(exc)}]}, indent=2))
        return 1
    out = add_rating_scale_view(score_session(row), row)
    print(json.dumps(out, indent=2))
    return 0 if out.get("scored") or out.get("gaps") else 1


if __name__ == "__main__":
    raise SystemExit(main())
