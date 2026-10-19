#!/usr/bin/env python3
"""Delivery plan checks. Computes and checks; never assigns people, never chooses a tier.

Steps are jobs (each ends at a review gate). For each step:
  - dependencies: every one must exist and the plan must have no cycle; reports a valid order;
  - capacity: must be stated by people (never assumed);
  - capability first: a step that names a performer must also name the capability it needs;
  - the tier proposal from the engine's delegability rule, when the four risk factors are scored:
    consequence (high = costly if wrong), reversibility (low = irreversible, counted 11 - x),
    checkability (low = cannot be checked, counted 11 - x), regulatory (high = regulated).
    Any factor at 8 or more -> people only; all at 3 or less -> agent; otherwise agent with review;
  - regulated work: anything but people only needs an exception in the person's words;
  - AI at a critical point needs a context-of-use statement;
  - every delegated step needs an oversight owner; review point defaults to the step's gate.
Tier mapping (owner ruling 3): people only = assist; agent with review = augment, or automate
with a human approving; agent = automate.

Input (JSON):
  {"steps": [{"id": "j1", "name": "...", "capability": "...", "performer": "role or agent type",
              "depends_on": ["j0"], "capacity": "0.5 FTE medical writer",
              "risk": {"consequence": 7, "reversibility": 6, "checkability": 8, "regulatory": 5},
              "choice": "people_only" | "agent_with_review" | "agent" | null,
              "regulated": false, "exception": "...", "critical_point": false,
              "context_of_use": "...", "oversight_owner": "role",
              "review_on": "...", "review_question": "..."}]}

Usage:  python3 delivery_check.py plan.json [--json]
"""

from __future__ import annotations

import json
import sys

TIERS = {"people_only": "People only", "agent_with_review": "Agent with review", "agent": "Agent"}
LEVELS = {"people_only": "assist", "agent_with_review": "augment, or automate with a human approving", "agent": "automate"}
RISK_KEYS = ("consequence", "reversibility", "checkability", "regulatory")
INVERT = {"reversibility", "checkability"}


class CheckError(ValueError):
    pass


def propose_tier(risk):
    vals = {}
    for k in RISK_KEYS:
        v = risk.get(k)
        if isinstance(v, bool) or not isinstance(v, int) or not 1 <= v <= 10:
            return None, f"risk factor '{k}' must be a whole number 1 to 10 scored by people"
        vals[k] = 11 - v if k in INVERT else v
    if any(v >= 8 for v in vals.values()):
        return "people_only", "a risk factor is 8 or more: " + ", ".join(k for k, v in vals.items() if v >= 8)
    if all(v <= 3 for v in vals.values()):
        return "agent", "every risk factor is 3 or less"
    return "agent_with_review", "risk factors are mixed"


def evaluate(payload):
    steps = payload.get("steps")
    if not isinstance(steps, list) or not steps:
        raise CheckError("a plan needs at least one step")
    ids = [s.get("id") for s in steps]
    if not all(ids) or len(set(ids)) != len(ids):
        raise CheckError("every step needs a unique id")
    by_id = {s["id"]: s for s in steps}
    issues, rows = [], []
    for s in steps:
        deps = s.get("depends_on") or []
        if isinstance(deps, str):
            deps = [deps]
        s["_deps"] = deps
        for d in deps:
            if d not in by_id:
                issues.append(f"{s['id']}: depends on '{d}', which is not in the plan")
    # topological order
    order, state = [], {}

    def visit(n, path):
        if state.get(n) == 2:
            return
        if state.get(n) == 1:
            issues.append("cycle: " + " -> ".join(path + [n]))
            return
        state[n] = 1
        for d in by_id[n]["_deps"]:
            if d in by_id:
                visit(d, path + [n])
        state[n] = 2
        order.append(n)

    for s in steps:
        visit(s["id"], [])
    for s in steps:
        r = {"id": s["id"], "name": s.get("name", s["id"]), "flags": []}
        if s.get("capacity") in (None, ""):
            r["flags"].append("no capacity stated; cannot be sequenced")
        if s.get("performer") and not s.get("capability"):
            r["flags"].append("names a performer but no capability: resolve the capability first")
        prop, why = (None, None)
        if isinstance(s.get("risk"), dict):
            prop, why = propose_tier(s["risk"])
            if prop is None:
                r["flags"].append(why)
        r["proposed_tier"] = TIERS.get(prop) if prop else None
        r["proposal_reason"] = why if prop else None
        choice = s.get("choice")
        if choice and choice not in TIERS:
            r["flags"].append(f"choice '{choice}' is not one of people only, agent with review, agent")
            choice = None
        r["chosen_tier"] = TIERS.get(choice) if choice else None
        r["intervention_level"] = LEVELS.get(choice) if choice else None
        if choice and prop and choice != prop:
            r["flags"].append(f"chosen tier differs from the computed proposal ({TIERS[prop]}); record the person's reason")
        if s.get("regulated") and choice and choice != "people_only" and not (s.get("exception") or "").strip():
            r["flags"].append("regulated work is people only unless an exception is recorded in the person's words")
        if choice in ("agent", "agent_with_review"):
            if s.get("critical_point") and not (s.get("context_of_use") or "").strip():
                r["flags"].append("AI at a critical decision point needs a context-of-use statement first; a qualified person decides there")
            if not s.get("oversight_owner"):
                r["flags"].append("no oversight owner: cannot be placed")
            r["review_on"] = s.get("review_on") or "at the step's gate (default)"
            if not (s.get("review_question") or "").strip():
                r["flags"].append("review question missing")
        if not choice:
            r["flags"].append("tier not chosen by the person yet")
        cap = str(s.get("capacity") or "").lower()
        if choice == "agent" and cap and not any(w in cap for w in ("run", "agent", "call", "job")):
            r["flags"].append("tier is agent but capacity is stated only as people's time: check which does the work")
        rows.append(r)
    return {"order": order if not any(i.startswith("cycle") for i in issues) else None,
            "plan_issues": issues, "steps": rows,
            "tool_note": "The connector's sequence check takes one dependency per step; list the step after all its predecessors.",
            "rule": "Checks only. People state capacity, choose the tier and name the oversight owner. A step is a job that ends at a review gate."}


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        r = evaluate(json.loads(raw))
    except (CheckError, json.JSONDecodeError, OSError) as exc:
        print(f"Not checked: {exc}", file=sys.stderr)
        return 2
    if "--json" in argv:
        print(json.dumps(r, indent=2))
        return 0
    print("Order: " + (" -> ".join(r["order"]) if r["order"] else "none (fix the plan issues)"))
    for i in r["plan_issues"]:
        print("Plan issue: " + i)
    print("| Step | Proposed tier (why) | Chosen tier | Intervention level | Review | Flags |\n|---|---|---|---|---|---|")
    for s in r["steps"]:
        prop = f"{s['proposed_tier']} ({s['proposal_reason']})" if s["proposed_tier"] else ""
        print(f"| {s['name']} | {prop} | {s['chosen_tier'] or ''} | {s['intervention_level'] or ''} | {s.get('review_on', '')} | {'; '.join(s['flags'])} |")
    print(r["rule"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
