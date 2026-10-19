#!/usr/bin/env python3
"""Decision record checks before sign-off. Checks only; never fills a section, never chooses
the result, never signs.

Checks:
  - the eight canon sections are present (missing ones are gaps, never filled);
  - section 2 holds a range (low, likely, high, unit, basis; low differs from high) and the
    cost of a wrong decision;
  - section 3 states where scores came from (room or field) and the Gate 2 attestation;
  - section 5 includes doing nothing and doing it internally;
  - section 6 result is exactly Proceed, Investigate first or Handle it internally, chosen by a
    named owner (never the assistant);
  - section 8 dissent: text with holders' names, or "none" attested by a named person; empty
    differs from absent;
  - score release: every scored stage released by a named person, after all scorers submitted;
  - Gate 3: two different named signers, one of them the decision owner; not AI;
  - roles or titles alone (the CMO, Head of X, the facilitator) are gaps for owner, Gate 2,
    result, dissent, release and signers; for route lead and assumption owners they are
    annex gaps that do not block preparing the signature ([CHECK] heuristic);
  - missing submission counts for a released stage are an annex gap; no release shown is a gap.

Input (JSON):
  {"owner": "Dr. Lena Brandt",
   "sections": {"1": {...}, "2": {"range": {"low", "mid", "high", "unit", "basis"}, "cost_of_wrong": "..."},
                "3": {"provenance": "room" | "field", "gate2_attested_by": "..."},
                "4": {...}, "5": {"options": ["Do nothing", "Do it internally", "..."]},
                "6": {"result": "Investigate first", "chosen_by": "...", "route": "...", "route_lead": "..."},
                "7": {"assumptions": [{"text": "...", "owner": "..."}]}, "8": {"dissent": [{"text": "...", "by": "..."}] | null, "none_attested_by": "..." | null}},
   "score_stages": [{"stage": "outcomes", "scorers_expected": 4, "scorers_submitted": 4, "released_by": "..."}],
   "signers": ["Dr. Lena Brandt", "Head of Sales Ops"]}

Usage:  python3 record_check.py record.json
"""

from __future__ import annotations

import json
import re
import sys

AI = {"ai", "model", "assistant", "claude"}
RESULTS = ("Proceed", "Investigate first", "Handle it internally")
NAMES = {"1": "Decision", "2": "Value at stake", "3": "Outcome priorities", "4": "Capability and gap register",
         "5": "Options considered", "6": "Recommendation and route", "7": "Assumptions and risks", "8": "Dissent"}



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


def _person(x):
    s = str(x or "").strip()
    return s if s and s.lower() not in AI else None


def _same(a, b):
    """Same person: exact match, or the same last word (surname) in both."""
    if not a or not b:
        return False
    a, b = str(a).strip().lower(), str(b).strip().lower()
    return a == b or re.sub(r"[^a-z ]", "", a).split()[-1:] == re.sub(r"[^a-z ]", "", b).split()[-1:]


def evaluate(p):
    owner = _person(p.get("owner"))
    secs = p.get("sections") or {}
    gaps, blocks, annex = [], [], []

    def role_gap(label, value, into=None):
        if _person(value) and _role_only(value):
            (gaps if into is None else into).append(f"{label} '{value}' is a role only: name the person")

    if not owner:
        blocks.append("no named decision owner")
    role_gap("decision owner", owner)
    for k, n in NAMES.items():
        if not secs.get(k) and k != "8":
            gaps.append(f"section {k} ({n}) missing: [GAP], not filled")
    s2 = secs.get("2") or {}
    r = s2.get("range") or {}
    if s2:
        if any(r.get(x) in (None, "") for x in ("low", "mid", "high", "unit", "basis")):
            gaps.append("value at stake: range incomplete (low, likely, high, unit, basis)")
        elif r["low"] == r["high"]:
            blocks.append("value at stake is a point; a range is required")
        if not str(s2.get("cost_of_wrong") or "").strip():
            gaps.append("value at stake: cost of a wrong decision missing")
    s3 = secs.get("3") or {}
    if s3:
        if s3.get("provenance") not in ("room", "field"):
            gaps.append("outcome priorities: where the scores came from is not stated")
        if not _person(s3.get("gate2_attested_by")):
            gaps.append("outcome priorities: Gate 2 not attested by a named person")
        role_gap("Gate 2 attested by", s3.get("gate2_attested_by"))
    s5 = secs.get("5") or {}
    if s5:
        low = [str(o).lower() for o in s5.get("options") or []]
        for b in ("do nothing", "do it internally"):
            if not any(b in o for o in low):
                gaps.append(f"options considered: '{b}' missing")
    s6 = secs.get("6") or {}
    result_ok = False
    if s6:
        if s6.get("result") not in RESULTS:
            gaps.append("result pending or not one of Proceed, Investigate first, Handle it internally")
        elif not _person(s6.get("chosen_by")):
            blocks.append("result not chosen by a named person")
        else:
            result_ok = True
            role_gap("result chosen by", s6.get("chosen_by"))
            if owner and not _same(s6.get("chosen_by"), owner):
                gaps.append("result chosen by someone other than the named owner: confirm the owner's decision")
        if not str(s6.get("route") or "").strip():
            gaps.append("route (next step and who leads) missing")
        if "route_lead" in s6:
            if not _person(s6.get("route_lead")):
                annex.append("route: no named lead")
            role_gap("route lead", s6.get("route_lead"), annex)
    for a in (secs.get("7") or {}).get("assumptions") or []:
        if not _person(a.get("owner")):
            annex.append(f"assumption '{a.get('text', '')[:40]}': no owner")
        role_gap("assumption owner", a.get("owner"), annex)
    s8 = secs.get("8")
    if s8 is None or s8 == {}:
        gaps.append("section 8 (Dissent) absent: record dissent text, or 'none' attested by a named person")
    else:
        d, none_by = s8.get("dissent"), s8.get("none_attested_by")
        if d and none_by:
            blocks.append("dissent has both text and a 'none' attestation")
        elif d:
            for x in d:
                if not _person(x.get("by")):
                    gaps.append("a dissent entry has no named holder")
                role_gap("dissent holder", x.get("by"))
        elif not _person(none_by):
            gaps.append("dissent empty without a named 'none' attestation (empty must differ from absent)")
        else:
            role_gap("'no dissent' attested by", none_by)
    if not p.get("score_stages"):
        gaps.append("score release not shown: for each scored stage, who released it and whether all scorers submitted")
    for st in p.get("score_stages") or []:
        if st.get("scorers_expected") is None or st.get("scorers_submitted") is None:
            annex.append(f"{st.get('stage')}: submission counts not shown; confirm every scorer submitted before release")
        elif st["scorers_submitted"] < st["scorers_expected"]:
            gaps.append(f"{st.get('stage')}: not every scorer has submitted; do not release yet")
        if not _person(st.get("released_by")):
            gaps.append(f"{st.get('stage')}: scores unreleased (release needs a named person)")
        elif _role_only(st.get("released_by")):
            gaps.append(f"{st.get('stage')}: released by '{st.get('released_by')}', a role only: name the person")
    signers = [s for s in (p.get("signers") or []) if _person(s)]
    for s in signers:
        if _role_only(s):
            gaps.append(f"signer '{s}' is a role only: Gate 3 needs a named person")
    if len(set(signers)) < 2:
        gaps.append("Gate 3 needs two different named signers")
    if owner and not any(_same(owner, s) for s in signers):
        gaps.append("Gate 3: the decision owner is not among the signers")
    ready = not blocks and not gaps and result_ok
    return {"ready_to_prepare_signature": ready, "blocks": blocks, "gaps": gaps,
            "annex_gaps": annex,
            "signers": signers, "signed": False,
            "rule": "Checks only. Missing sections stay gaps. The owner chooses the result. Signing happens in the Navigator app; this never signs."}


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
