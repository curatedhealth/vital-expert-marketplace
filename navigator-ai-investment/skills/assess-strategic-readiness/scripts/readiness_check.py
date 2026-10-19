#!/usr/bin/env python3
"""Strategic readiness: the outcome-weighted capability gap. Computes and checks; never scores.

Mirrors the Navigator engine's `weighted_gap` (template nav.capabilities): whole numbers 1 to 10
on Current ("Does not exist today" to "Fully in place today") and Required ("Not needed" to
"Essential"), equal weight per scorer; gap = max(0, mean required - mean current); criticality =
a direct value if given, else the link-weighted mean of the scores of the outcomes the capability
serves, else 1 (default); weighted gap = gap x criticality; ranked by weighted gap, then gap, then
id. Adds: spread of 3 or more flagged; fewer than three scorers indicative; the owner's view
computed separately; capabilities that serve no scored outcome flagged (demand before supply).

Input (JSON):
  {"capabilities": [{"id": "c1", "label": "Medical content review at scale"}, ...],
   "scores": [{"scorer_id": "CMO", "item_id": "c1", "criterion_key": "current" | "required",
               "value": 1-10}, ...],
   "outcome_scores": {"o1": 13.0, "o2": 11.25},          attested opportunity scores
   "outcome_labels": {"o1": "Reduce time to accurate answer"},   optional
   "outcome_links": [{"capability_id": "c1", "outcome_id": "o1", "weight": 1}, ...],
   "criticality": {"c3": 5},                              optional, direct, with a reason elsewhere
   "owner_scorer_id": "CMO"}                              optional

Usage:  python3 readiness_check.py input.json [--json]
"""

from __future__ import annotations

import json
import sys
from statistics import mean

KEYS = ("current", "required")
SPREAD = 3


class CheckError(ValueError):
    pass


def _grid(payload):
    caps = payload.get("capabilities")
    if not isinstance(caps, list) or not caps:
        raise CheckError("capabilities must be a non-empty list")
    labels = {}
    for i, c in enumerate(caps):
        if not isinstance(c, dict) or not c.get("id"):
            raise CheckError(f"capabilities[{i}]: id is required")
        if c["id"] in labels:
            raise CheckError(f"capabilities[{i}]: duplicate id {c['id']}")
        labels[c["id"]] = c.get("label", c["id"])
    grid = {}
    for n, s in enumerate(payload.get("scores") or []):
        sid, it, k, v = s.get("scorer_id"), s.get("item_id"), s.get("criterion_key"), s.get("value")
        if not sid:
            raise CheckError(f"scores[{n}]: scorer_id is required")
        if it not in labels:
            raise CheckError(f"scores[{n}]: unknown capability {it!r}")
        if k not in KEYS:
            raise CheckError(f"scores[{n}]: criterion must be current or required, got {k!r}")
        if isinstance(v, bool) or not isinstance(v, int) or not 1 <= v <= 10:
            raise CheckError(f"scores[{n}]: value must be a whole number 1 to 10, got {v!r}")
        cell = grid.setdefault(sid, {}).setdefault(it, {})
        if k in cell:
            raise CheckError(f"scores[{n}]: {sid} scored {k} on {it} twice")
        cell[k] = v
    if not grid:
        raise CheckError("scores must be a non-empty list")
    missing = [f"{s} on {c}: {k}" for s in grid for c in labels for k in KEYS if k not in grid[s].get(c, {})]
    if missing:
        raise CheckError("every scorer must score current and required for every capability; nothing is filled in. Missing: " + "; ".join(missing))
    return labels, grid


def _criticality(labels, payload):
    direct = payload.get("criticality") or {}
    scores = payload.get("outcome_scores") or {}
    for k, v in list(direct.items()) + list(scores.items()):
        if isinstance(v, bool) or not isinstance(v, (int, float)) or v < 0:
            raise CheckError(f"criticality and outcome scores must be numbers >= 0, got {k}: {v!r}")
    by_cap = {}
    for i, link in enumerate(payload.get("outcome_links") or []):
        cap, out = link.get("capability_id"), link.get("outcome_id")
        if cap not in labels:
            raise CheckError(f"outcome_links[{i}]: unknown capability {cap!r}")
        if out not in scores:
            raise CheckError(f"outcome_links[{i}]: no outcome score for {out!r}")
        w = link.get("weight", 1)
        if isinstance(w, bool) or not isinstance(w, (int, float)) or w < 0:
            raise CheckError(f"outcome_links[{i}]: weight must be a number >= 0")
        by_cap.setdefault(cap, []).append((w, scores[out], out))
    out = {}
    for c in labels:
        if c in direct:
            out[c] = (float(direct[c]), "set directly", [])
        elif c in by_cap and sum(w for w, _, _ in by_cap[c]) > 0:
            tot = sum(w for w, _, _ in by_cap[c])
            out[c] = (sum(w * s for w, s, _ in by_cap[c]) / tot, "from the outcomes it serves", [o for _, _, o in by_cap[c]])
        else:
            out[c] = (1.0, "default (serves no scored outcome)", [])
    return out


def _rank(labels, grid, scorers, crit):
    rows = []
    for c in labels:
        cur = [grid[s][c]["current"] for s in scorers]
        req = [grid[s][c]["required"] for s in scorers]
        gap = max(0.0, mean(req) - mean(cur))
        k, src, outs = crit[c]
        rows.append({"id": c, "label": labels[c], "current": round(mean(cur), 2), "required": round(mean(req), 2),
                     "gap": round(gap, 4), "criticality": round(k, 4), "criticality_source": src, "serves": outs,
                     "weighted_gap": round(gap * k, 4),
                     "current_range": [min(cur), max(cur)], "required_range": [min(req), max(req)],
                     "disagreement": max(cur) - min(cur) >= SPREAD or max(req) - min(req) >= SPREAD})
    rows.sort(key=lambda r: (-r["weighted_gap"], -r["gap"], r["id"]))
    for n, r in enumerate(rows, 1):
        r["rank"] = n
        r["tie_on_weighted_gap"] = sum(1 for x in rows if x["weighted_gap"] == r["weighted_gap"]) > 1
    return rows


def evaluate(payload):
    labels, grid = _grid(payload)
    scorers = sorted(grid)
    crit = _criticality(labels, payload)
    group = _rank(labels, grid, scorers, crit)
    owner = payload.get("owner_scorer_id")
    owner_view = None
    if owner is not None:
        if owner not in grid:
            raise CheckError(f"owner {owner!r} has no scores")
        owner_view = [{"id": r["id"], "weighted_gap": r["weighted_gap"], "rank": r["rank"]}
                      for r in _rank(labels, grid, [owner], crit)]
    return {"scorers": scorers, "indicative": len(scorers) < 3, "group": group, "owner_view": owner_view,
            "serves_no_outcome": [r["label"] for r in group if r["criticality_source"].startswith("default")],
            "rule": "Computed from people's scores, equal weight. Gap = required minus current (never below 0), "
                    "weighted by the scores of the outcomes each capability serves. Not a maturity level and "
                    "not a decision."}


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        r = evaluate(json.loads(raw))
    except (CheckError, json.JSONDecodeError, OSError) as exc:
        print(f"Not computed: {exc}", file=sys.stderr)
        return 2
    if "--json" in argv:
        print(json.dumps(r, indent=2))
        return 0
    print("| Rank | Capability | Current | Required | Gap | Weight from outcomes | Weighted gap | Disagreement |")
    print("|---|---|---|---|---|---|---|---|")
    for g in r["group"]:
        parts = []
        if g["current_range"][1] - g["current_range"][0] >= SPREAD:
            parts.append("current {}-{}".format(*g["current_range"]))
        if g["required_range"][1] - g["required_range"][0] >= SPREAD:
            parts.append("required {}-{}".format(*g["required_range"]))
        dis = "yes (" + ", ".join(parts) + ")" if parts else ""
        print(f"| {g['rank']} | {g['label']} | {g['current']} | {g['required']} | {round(g['gap'], 2)} | "
              f"{round(g['criticality'], 2)} ({g['criticality_source']}) | {round(g['weighted_gap'], 2)}"
              f"{' (tied)' if g['tie_on_weighted_gap'] else ''} | {dis} |")
    print(f"\nScorers: {', '.join(r['scorers'])}." + (" Fewer than three: indicative." if r["indicative"] else ""))
    if r["serves_no_outcome"]:
        print("Serves no scored outcome (flag for restating or retirement): " + "; ".join(r["serves_no_outcome"]))
    if r["owner_view"]:
        print(f"Owner's view (show after the group's): {r['owner_view']}")
    print(r["rule"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
