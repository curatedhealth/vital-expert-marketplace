#!/usr/bin/env python3
"""Portfolio placement: computes and checks; never scores, never decides.

The investment grid (Navigator engine `opportunity_governance_grid`) with the owner's ruling of
19 October 2026: the second axis is fit to capacity, and value is the option's Outcome fit (the
group's average score from the option comparison, 1 to 10), not its composite, so cost and
burden are not counted twice. Baseline options (do nothing, do it internally, when marked as the
baseline) are reference lines and are never placed. Oversight needed = the option's Governance burden score (1 light to
10 heavy). Oversight the organization can carry today = scored by named people, 1 to 10; the
group view is the mean. An option is above capacity when needed > capacity (the engine computes
this when capacity is passed as its burden split). Value is high when >= the value split (median
of the options by default, or a split the owner states).

  high value, fits capacity    -> Invest now              (invest_now)
  high value, above capacity   -> Build the basis first   (codify_first)
  low value,  fits capacity    -> Later, in batches       (harvest_later)
  low value,  above capacity   -> Not now                 (not_now)
  consequence of error too high to delegate (owner says yes) -> Support, do not automate
  (augment_dont_automate); the underlying bucket is kept.

Lenses re-group the same options by the tags and scores people gave; they never change the bucket
or the ranking.

Input (JSON):
  {"options": [{"id": "a", "label": "...", "outcome_fit": 7.0, "oversight_needed": 7.0,
                "is_baseline": false,
                "consequence_high": false,
                "tags": {"play": "augmentation", "aim": "productivity", "source": "internal"},
                "cost": 6.0}, ...],
   "capacity_scores": [{"scorer_id": "CMO", "value": 5}, ...],
   "value_split": 6.0}                                                     optional

Usage:  python3 placement_check.py input.json [--json]
"""

from __future__ import annotations

import json
import sys
from statistics import mean, median

NAMES = {"invest_now": "Invest now", "codify_first": "Build the basis first", "harvest_later": "Later, in batches",
         "not_now": "Not now", "augment_dont_automate": "Support, do not automate"}
LENSES = {"play": ("Capability against capacity", {"augmentation": "Augmentation (capability play)",
                                                    "automation": "Automation (capacity play)"}),
          "aim": ("Productivity against differentiation", {"productivity": "Productivity", "differentiation": "Differentiation"}),
          "source": ("Internal against external", {"internal": "Internal", "external": "External"})}


class CheckError(ValueError):
    pass


def _num(v, where):
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not 1 <= v <= 10:
        raise CheckError(f"{where} must be a number from 1 to 10, got {v!r}")
    return float(v)


def evaluate(payload):
    opts = payload.get("options")
    if not isinstance(opts, list) or not opts:
        raise CheckError("options must be a non-empty list")
    caps = payload.get("capacity_scores")
    if not isinstance(caps, list) or not caps:
        raise CheckError("capacity_scores must list the oversight capacity scores of named people; it is never assumed")
    seen, cap_vals = set(), []
    for i, c in enumerate(caps):
        sid, v = c.get("scorer_id"), c.get("value")
        if not sid or sid in seen:
            raise CheckError(f"capacity_scores[{i}]: one score per named scorer")
        if isinstance(v, bool) or not isinstance(v, int) or not 1 <= v <= 10:
            raise CheckError(f"capacity_scores[{i}]: value must be a whole number 1 to 10")
        seen.add(sid)
        cap_vals.append(v)
    capacity = mean(cap_vals)
    rows, reference = [], []
    for i, o in enumerate(opts):
        if not o.get("id"):
            raise CheckError(f"options[{i}]: id is required")
        if o.get("is_baseline") is True:
            reference.append(o.get("label", o["id"]))
            continue
        flag = o.get("consequence_high", False)
        if not isinstance(flag, bool):
            raise CheckError(f"options[{i}]: consequence_high must be true or false")
        rows.append({"id": o["id"], "label": o.get("label", o["id"]), "value": _num(o.get("outcome_fit"), f"options[{i}].outcome_fit"),
                     "oversight_needed": _num(o.get("oversight_needed"), f"options[{i}].oversight_needed"),
                     "consequence_high": flag, "tags": o.get("tags") or {},
                     "cost": o.get("cost"), "outcome_fit": o.get("outcome_fit")})
    if not rows:
        raise CheckError("no option to place besides the baseline")
    v_split = _num(payload["value_split"], "value_split") if payload.get("value_split") is not None else median(r["value"] for r in rows)
    for r in rows:
        high, above = r["value"] >= v_split, r["oversight_needed"] > capacity
        code = {(True, False): "invest_now", (True, True): "codify_first",
                (False, False): "harvest_later", (False, True): "not_now"}[(high, above)]
        r["grid_bucket"] = NAMES[code]
        r["bucket"] = NAMES["augment_dont_automate"] if r["consequence_high"] else NAMES[code]
        r["fit"] = round(capacity - r["oversight_needed"], 2)
    lenses = {}
    for key, (title, names) in LENSES.items():
        groups = {}
        for r in rows:
            tag = r["tags"].get(key)
            groups.setdefault(names.get(tag, "Not tagged" if tag is None else f"Unknown tag '{tag}'"), []).append(r["label"])
        lenses[title] = groups
    cb = [{"option": r["label"], "cost": r["cost"], "outcome_fit": r["outcome_fit"]} for r in rows
          if r["cost"] is not None and r["outcome_fit"] is not None]
    lenses["Cost against benefit"] = cb or "Not available: needs each option's cost and outcome fit scores"
    caps_spread = max(cap_vals) - min(cap_vals)
    return {"capacity": round(capacity, 2), "capacity_range": [min(cap_vals), max(cap_vals)],
            "capacity_disagreement": caps_spread >= 3, "capacity_scorers": len(cap_vals),
            "value_split": round(v_split, 2), "value_split_source": "stated by the owner" if payload.get("value_split") is not None else "median of the options",
            "split_warning": ("Fewer than four options: a median split puts half of them low by definition. Ask the owner for a value split."
                              if payload.get("value_split") is None and len(rows) < 4 else None),
            "options": rows, "not_placed_baselines": reference, "counts": {n: sum(1 for r in rows if r["bucket"] == n) for n in NAMES.values()},
            "lenses": lenses,
            "rule": "A decision aid, not a measurement: placement on each axis is a scored judgment by named "
                    "people and the boundaries are a convention. Lenses change the view, never the bucket or the ranking."}


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        r = evaluate(json.loads(raw))
    except (CheckError, json.JSONDecodeError, OSError, KeyError) as exc:
        print(f"Not computed: {exc}", file=sys.stderr)
        return 2
    if "--json" in argv:
        print(json.dumps(r, indent=2))
        return 0
    print(f"Oversight the organization can carry today: {r['capacity']} (range {r['capacity_range'][0]} to {r['capacity_range'][1]}, "
          f"{r['capacity_scorers']} scorers{'; disagreement' if r['capacity_disagreement'] else ''}). Value split: {r['value_split']} ({r['value_split_source']}).")
    if r["split_warning"]:
        print(r["split_warning"])
    print("| Option | Value (outcome fit) | Oversight needed | Fit (capacity minus needed) | Bucket | Grid bucket if overridden |")
    print("|---|---|---|---|---|---|")
    for o in r["options"]:
        print(f"| {o['label']} | {o['value']} | {o['oversight_needed']} | {o['fit']:+} | {o['bucket']} | {o['grid_bucket'] if o['consequence_high'] else ''} |")
    if r["not_placed_baselines"]:
        print("Not placed (reference lines): " + "; ".join(r["not_placed_baselines"]))
    for t, g in r["lenses"].items():
        print(f"\n{t}: {g}")
    print("\n" + r["rule"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
