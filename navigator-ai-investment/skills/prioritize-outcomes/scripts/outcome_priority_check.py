#!/usr/bin/env python3
"""Outcome priorities: computes and checks; never creates, changes or fills a score.

Follows the Navigator template nav.outcomes and the canon (GOV-06 6.1.4 to 6.1.7, Annex B.2;
Decision R4): whole numbers 1 to 10 from named people; equal weight; group importance and
satisfaction are the means across scorers; Opportunity = I + max(0, I - S); bands extreme >= 15,
strong 12 to < 15, moderate 10 to < 12, low < 10 (describe, never decide); dissent flag when the
spread on either criterion is 3 or more, strong disagreement at 4 or more; fewer than three scorers is indicative; the owner's view
is computed separately and shown after the group's; sensitivity drops each scorer in turn and
reports whether the leader and the top set change. Then reads the field-test rule (GOV-06 6.1.7).

Input (JSON):
  {"items": [{"id": "o1", "label": "Reduce the time ...", "dimension": "OV"}, ...],
   "scores": [{"scorer_id": "CMO", "item_id": "o1", "criterion_key": "importance" | "satisfaction",
               "value": 1-10}, ...],
   "owner_scorer_id": "CMO",                                   optional
   "top_n": 3,                                                  optional, 3 to 5
   "decision": {"hard_to_reverse": true | false | null,        optional, from the frame
                "beyond_one_cycle_or_cross_function": true | false | null},
   "field_verified": ["o2"]}                                    optional, outcomes field-verified

Usage:  python3 outcome_priority_check.py scores.json [--json]
"""

from __future__ import annotations

import json
import sys
from statistics import mean, median

KEYS = ("importance", "satisfaction")
DISAGREEMENT_SPREAD = 3          # dissent flag (owner ruling 18 Oct 2026)
STRONG_DISAGREEMENT_SPREAD = 4   # field-test trigger on a top-five outcome (owner ruling 18 Oct 2026)


class CheckError(ValueError):
    pass


def opportunity(i: float, s: float) -> float:
    return i + max(0.0, i - s)


def band(o: float) -> str:
    if o >= 15:
        return "extreme"
    if o >= 12:
        return "strong"
    if o >= 10:
        return "moderate"
    return "low"


def build_grid(payload: dict):
    items = payload.get("items")
    if not isinstance(items, list) or not items:
        raise CheckError("items must be a non-empty list")
    labels = {}
    for i, it in enumerate(items):
        iid = it.get("id") if isinstance(it, dict) else None
        if not iid:
            raise CheckError(f"items[{i}]: id is required")
        labels[iid] = it
    cells = payload.get("scores")
    if not isinstance(cells, list) or not cells:
        raise CheckError("scores must be a non-empty list")
    grid: dict[str, dict[str, dict[str, int]]] = {}
    for n, c in enumerate(cells):
        s, it, k, v = c.get("scorer_id"), c.get("item_id"), c.get("criterion_key"), c.get("value")
        if not s:
            raise CheckError(f"scores[{n}]: scorer_id is required")
        if it not in labels:
            raise CheckError(f"scores[{n}]: unknown item '{it}'")
        if k not in KEYS:
            raise CheckError(f"scores[{n}]: criterion must be importance or satisfaction, got {k!r}")
        if isinstance(v, bool) or not isinstance(v, int) or not 1 <= v <= 10:
            raise CheckError(f"scores[{n}]: value must be a whole number 1 to 10, got {v!r}")
        cell = grid.setdefault(s, {}).setdefault(it, {})
        if k in cell:
            raise CheckError(f"scores[{n}]: {s} scored {k} on {it} twice")
        cell[k] = v
    missing = [f"{s} on {it}: {k}" for s in grid for it in labels for k in KEYS
               if k not in grid[s].get(it, {})]
    if missing:
        raise CheckError("every scorer must score importance and satisfaction for every outcome; "
                         "nothing is filled in. Missing: " + "; ".join(missing))
    return labels, grid


def rank(labels: dict, grid: dict, scorers: list[str]) -> list[dict]:
    rows = []
    for it in labels:
        imp = [grid[s][it]["importance"] for s in scorers]
        sat = [grid[s][it]["satisfaction"] for s in scorers]
        gi, gs = mean(imp), mean(sat)
        opp = opportunity(gi, gs)
        med = median(opportunity(a, b) for a, b in zip(imp, sat))
        rows.append({"_opp": opp, "_med": med,
            "id": it, "label": labels[it].get("label", it), "dimension": labels[it].get("dimension"),
            "importance": round(gi, 2), "satisfaction": round(gs, 2),
            "opportunity": round(opp, 2), "band": band(round(opp, 4)),
            "median_of_scorer_opportunities": round(median(opportunity(a, b) for a, b in zip(imp, sat)), 2),
            "importance_range": [min(imp), max(imp)], "satisfaction_range": [min(sat), max(sat)],
            "disagreement": (max(imp) - min(imp) >= DISAGREEMENT_SPREAD) or (max(sat) - min(sat) >= DISAGREEMENT_SPREAD),
            "strong_disagreement": (max(imp) - min(imp) >= STRONG_DISAGREEMENT_SPREAD) or (max(sat) - min(sat) >= STRONG_DISAGREEMENT_SPREAD),
        })
    # Same order as the Navigator engine: opportunity, then median of scorers' own, then id.
    rows.sort(key=lambda r: (-round(r["_opp"], 4), -round(r["_med"], 4), r["id"]))
    for n, r in enumerate(rows, 1):
        r["rank"] = n
    for a, b in zip(rows, rows[1:]):
        if round(a["_opp"], 4) == round(b["_opp"], 4):
            a["tied_with_next"] = True
    for r in rows:
        del r["_opp"], r["_med"]
    return rows


def evaluate(payload: dict) -> dict:
    labels, grid = build_grid(payload)
    scorers = sorted(grid)
    top_n = int(payload.get("top_n") or 5)
    if not 3 <= top_n <= 5:
        raise CheckError("top_n must be 3 to 5 (GOV-06 6.1.7: the top three to five outcomes; owner default five)")
    top_n = min(top_n, len(labels))
    group = rank(labels, grid, scorers)
    top_ids = [r["id"] for r in group[:top_n]]

    owner = payload.get("owner_scorer_id")
    owner_view = None
    if owner is not None:
        if owner not in grid:
            raise CheckError(f"owner '{owner}' has no scores; omit owner_scorer_id to skip the owner view")
        ov = rank(labels, grid, [owner])
        owner_view = {"scorer_id": owner, "ranking": [{"id": r["id"], "opportunity": r["opportunity"],
                                                        "rank": r["rank"]} for r in ov],
                      "differs_on_top": sorted(set(r["id"] for r in ov[:top_n]) ^ set(top_ids))}

    flips = []
    if len(scorers) >= 2:
        for s in scorers:
            sub = rank(labels, grid, [x for x in scorers if x != s])
            sub_top = [r["id"] for r in sub[:top_n]]
            change = {}
            base_order = [r["id"] for r in group]
            sub_order = [r["id"] for r in sub]
            if sub_order != base_order:
                change["order_becomes"] = [labels[i].get("label", i) for i in sub_order]
            if sub[0]["id"] != group[0]["id"]:
                change["new_leader"] = sub[0]["id"]
                if sub[0].get("tied_with_next"):
                    change["by_tie"] = True
                    change["tied_at"] = sub[0]["opportunity"]
            if sub_top != top_ids and set(sub_top) == set(top_ids):
                change["top_order_changes"] = True
            if set(sub_top) != set(top_ids):
                change["top_set_in"] = sorted(set(sub_top) - set(top_ids))
                change["top_set_out"] = sorted(set(top_ids) - set(sub_top))
            if change:
                name = lambda ids: [labels[i].get("label", i) for i in ids]
                for k in ("top_set_in", "top_set_out"):
                    if k in change:
                        change[k] = name(change[k])
                if "new_leader" in change:
                    change["new_leader"] = labels[change["new_leader"]].get("label", change["new_leader"])
                flips.append({"without": s, **change})
    leader_flip = any("new_leader" in f for f in flips)
    top_flip = any("top_set_in" in f or f.get("top_order_changes") for f in flips)  # reported, not a trigger
    order_flip = any("order_becomes" in f for f in flips)
    sensitivity = {"status": "close_call" if leader_flip else ("stable" if len(scorers) >= 2 else "not_run"),
                   "leader_changes": leader_flip, "top_set_changes": top_flip,
                   "full_order_changes": order_flip, "variants": flips,
                   "tested": "each scorer left out in turn; leader, top set and full order compared"}

    field_verified = set(payload.get("field_verified") or [])
    room_only_top = [i for i in top_ids if i not in field_verified]
    disagreement_top = [r["id"] for r in group[:top_n] if r["strong_disagreement"]]
    d = payload.get("decision") or {}
    htr, big = d.get("hard_to_reverse"), d.get("beyond_one_cycle_or_cross_function")
    reasons, unknown = [], []
    if htr is True and big is True and room_only_top:
        reasons.append("hard to reverse, commits beyond one planning cycle or across functions, "
                       "and the top outcomes were scored only in the room")
    elif room_only_top and (htr is None or big is None):
        unknown.append("ask the owner whether the decision is hard to reverse and whether it commits "
                       "money or people beyond the client's own budget cycle or across functions")
    if disagreement_top:
        reasons.append("scorers strongly disagreed (spread of 4 or more) on a top-five outcome: " + "; ".join(labels[i].get("label", i) for i in disagreement_top))
    if leader_flip:
        reasons.append("the first-ranked outcome changes under the sensitivity check")
    field_test = {
        "required": bool(reasons), "reasons": reasons, "still_to_ask": unknown,
        "outcomes_to_test": top_ids if reasons else [],
        "provenance": {i: ("field-verified" if i in field_verified else "scored in the room") for i in labels},
        "rule": "A field test of the top three to five outcomes with the people they are for, or a "
                "waiver by the decision owner with a reason recorded (GOV-06 6.1.7). Where field and "
                "room disagree, record it as dissent.",
    }
    return {"scorers": scorers, "indicative": len(scorers) < 3, "group": group, "top": top_ids,
            "owner_view": owner_view, "sensitivity": sensitivity, "field_test": field_test,
            "rule": "Computed from people's scores, equal weight. Opportunity = importance + max(0, "
                    "importance - satisfaction), on group means. Bands describe; people decide."}


def print_table(r: dict) -> None:
    print("| Rank | Outcome | Importance | Satisfaction | Opportunity | Band | Disagreement |")
    print("|---|---|---|---|---|---|---|")
    for g in r["group"]:
        dis = "yes (I {}-{}, S {}-{})".format(*g["importance_range"], *g["satisfaction_range"]) if g["disagreement"] else ""
        tie = " (tied)" if g.get("tied_with_next") else ""
        print(f"| {g['rank']} | {g['label']} | {g['importance']} | {g['satisfaction']} | {g['opportunity']}{tie} | {g['band']} | {dis} |")
    print(f"\nScorers: {', '.join(r['scorers'])}." + (" Fewer than three: indicative." if r["indicative"] else ""))
    s = r["sensitivity"]
    held = "first-ranked outcome holds" if s["status"] == "stable" else ("not run (one scorer)" if s["status"] == "not_run" else "close call: the first-ranked outcome changes")
    lower = (" Top set or order below the leader changes in some variant (reported; not a field-test trigger)."
             if (s["top_set_changes"] or s["full_order_changes"]) and s["status"] == "stable" else "")
    print(f"Sensitivity ({s['tested']}): {held}.{lower}" + (f" Variants: {s['variants']}" if s["variants"] else ""))
    if r["owner_view"]:
        print(f"Owner's view (show after the group's): {r['owner_view']['ranking']}")
    f = r["field_test"]
    print(f"Field test required: {f['required']}. {'; '.join(f['reasons'])} {'; '.join(f['still_to_ask'])}")
    print(r["rule"])


def main(argv: list[str]) -> int:
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        result = evaluate(json.loads(raw))
    except (CheckError, json.JSONDecodeError, OSError, ValueError) as exc:
        print(f"Not computed: {exc}", file=sys.stderr)
        return 2
    if "--json" in argv:
        print(json.dumps(result, indent=2))
    else:
        print_table(result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
