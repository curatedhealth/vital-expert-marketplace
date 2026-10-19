#!/usr/bin/env python3
"""Portfolio review checks. Checks only; never decides stop, keep or fix, never changes a score.

Activities: decision is stop, keep or fix with a reason; traces to an outcome or is flagged
"traces to none" (restate or retire); a scale note only on keep (as the connector enforces).
Scaling plans: only for keep, with what, owner and order; and (owner ruling 8) only when the
activity's outcome was measured as achieved, otherwise "keep and watch".
Re-score candidates (outcomes loop): a named steward, evidence from recorded results, a reason
per outcome; no bulk. Direction changes need two named people.
Readiness re-run: named factors, whole numbers 1 to 10, no index.

Input (JSON):
  {"activities": [{"id": "a1", "name": "...", "decision": "keep", "reason": "...",
                   "outcome": "...", "outcome_status": "achieved" | "not achieved" | "not measured",
                   "realized_place": "inside"}],
   "scaling_plans": [{"activity": "a1", "what": "...", "owner": "...", "order": ["...", "..."]}],
   "rescore": {"steward": "...", "candidates": [{"outcome": "...", "evidence": "...", "reason": "...",
               "decided": "approve" | "reject" | "edit" | null}]},
   "direction_change": {"proposed": "...", "approvers": ["...", "..."]},
   "readiness_factors": [{"name": "...", "score": 6}]}

Usage:  python3 review_check.py input.json
"""

from __future__ import annotations

import json
import re
import sys



ROLE_WORDS = {
    "the", "our", "a", "of", "and", "for", "&", "head", "director", "vp", "svp", "evp", "chief", "lead",
    "leader", "manager", "officer", "executive", "president", "facilitator", "owner", "steward", "sponsor",
    "cmo", "cco", "ceo", "cfo", "coo", "cio", "cto", "cdo", "cso", "gm", "medical", "compliance", "sales",
    "ops", "operations", "affairs", "commercial", "marketing", "field", "writing", "legal", "finance",
    "regulatory", "quality", "data", "digital", "it", "hr", "strategy", "information", "technology",
    "global", "regional", "country", "brand", "market", "access", "safety", "clinical", "science",
    "scientific", "team", "function", "business", "unit", "insights", "analytics", "content", "review",
    "senior", "deputy", "associate", "group", "department", "excellence", "customer", "engagement",
}


def _role_only(s):
    """[CHECK] heuristic: True when the text names a role but no person.
    A person is assumed when a title like Dr./Prof. appears, or a word outside the role vocabulary."""
    s = str(s or "").strip()
    if not s:
        return False
    if re.search(r"\b(dr|prof|mr|ms|mrs)\.?\s+[A-Z]", s):
        return False
    words = [w for w in re.split(r"[\s,/()\-]+", s.lower()) if w]
    return all(w.strip(".") in ROLE_WORDS for w in words)


def evaluate(p):
    flags, rows = [], []
    acts = {a.get("id"): a for a in p.get("activities") or []}
    for a in p.get("activities") or []:
        f = []
        if a.get("decision") not in ("stop", "keep", "fix"):
            f.append("decision must be stop, keep or fix (the person's)")
        if not str(a.get("reason") or "").strip():
            f.append("no reason")
        if not str(a.get("outcome") or "").strip():
            f.append("traces to no outcome: restate against one or retire")
        if a.get("decision") == "keep" and a.get("outcome_status") != "achieved":
            f.append("kept, but its outcome is not measured as achieved: keep and watch; no scaling yet")
        rows.append({"activity": a.get("name", a.get("id")), "decision": a.get("decision"),
                     "outcome": a.get("outcome") or "traces to none", "outcome_status": a.get("outcome_status"),
                     "realized_place": a.get("realized_place"), "flags": f})
    plans = []
    for s in p.get("scaling_plans") or []:
        f = []
        a = acts.get(s.get("activity"))
        if not a or a.get("decision") != "keep":
            f.append("a scaling plan attaches only to an activity marked keep")
        elif a.get("outcome_status") != "achieved":
            f.append("the activity's outcome is not measured as achieved: scale only after it is (owner ruling 8)")
        for k in ("what", "owner"):
            if not str(s.get(k) or "").strip():
                f.append(f"no {k}: the person writes the plan")
        if not isinstance(s.get("order"), list) or not s.get("order"):
            f.append("no order of steps")
        plans.append({"activity": s.get("activity"), "flags": f})
    rs = p.get("rescore") or {}
    rescore = None
    if rs:
        f = []
        st = str(rs.get("steward") or "").strip()
        if not st:
            f.append("no named steward: nothing changes")
        elif rs.get("steward_is_role") or _role_only(st):
            f.append("steward given as a role only: a gap until a person is named")
        for c in rs.get("candidates") or []:
            if not str(c.get("evidence") or "").strip():
                f.append(f"{c.get('outcome')}: no evidence from recorded results")
            if c.get("decided") and not str(c.get("reason") or "").strip():
                f.append(f"{c.get('outcome')}: decided without a reason")
            if not c.get("decided"):
                f.append(f"{c.get('outcome')}: awaiting the steward's decision (lapses if not reviewed in time)")
        rescore = {"steward": rs.get("steward"), "flags": f, "scores_changed": False}
    dc = p.get("direction_change")
    direction = None
    if dc:
        names = [n for n in dc.get("approvers") or [] if str(n).strip()]
        direction = {"proposed": dc.get("proposed"),
                     "flags": [] if len(set(names)) >= 2 else ["a change to direction needs two named people; route to Decision Framing"]}
    factors = []
    for x in p.get("readiness_factors") or []:
        s = x.get("score")
        ok = str(x.get("name") or "").strip() and isinstance(s, int) and not isinstance(s, bool) and 1 <= s <= 10
        factors.append({"name": x.get("name"), "score": s, "flag": None if ok else "needs a name and a whole number 1 to 10"})
    return {"activities": rows, "scaling_plans": plans, "rescore": rescore, "direction_change": direction,
            "readiness_factors": factors, "readiness_index": None,
            "rule": "Checks only. People decide stop, keep or fix; a named steward decides each re-score with evidence and a reason; no index is computed."}


def main(argv):
    files = [a for a in argv[1:] if not a.startswith("--")]
    try:
        raw = open(files[0], encoding="utf-8").read() if files else sys.stdin.read()
        r = evaluate(json.loads(raw))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"Not checked: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(r, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
