#!/usr/bin/env python3
"""Change log check: find changes without an assessment, assessments without a rationale,
changes implemented before approval or assessment, missing approvers, missing risk reviews,
and items changed several times without an aggregate assessment.

Input: the person's change log as CSV. Column names are matched case-insensitively; map
others with --map old=new. Recognized columns:
  change_id          required
  item               configuration item or document (used for the aggregate check)
  description
  assessment_ref     id of the impact assessment (blank = none)
  assessment_date
  decision           for example "no submission", "510(k)", "notify NB", "not significant"
  rationale          text of the basis for the decision
  approved_by
  approval_date
  implemented_date   date released or put into use
  touches_hazard     yes/no: does the change touch a hazard in the risk file
  risk_review_ref    reference to the risk file review
  aggregate_ref      reference to an assessment covering several changes to the same item
Dates: YYYY-MM-DD, DD.MM.YYYY or DD/MM/YYYY. Unreadable dates are reported as MISSING_DATE.

Output: one line per finding (change, check code, detail, source row), counts and rates per
check, and, with --rules, the person's own thresholds marked met or not met. The script sets
no threshold, judges no conclusion and names no owner. See references/change-control-checks.md.

Usage: python3 change_log_check.py log.csv [--rules rules.json] [--map col=field ...] [--json]
       rules.json: {"NO_ASSESSMENT": {"max_rate": 0.0, "owner": "name the person gave"}}
"""
import argparse
import csv
import datetime as dt
import json
import sys
from collections import defaultdict

ROW = {
    "NO_ASSESSMENT": "QS34",
    "NO_RATIONALE": "QX14, QX22",
    "DECISION_WITHOUT_BASIS": "QX14, QX22",
    "IMPL_BEFORE_APPROVAL": "QS34",
    "IMPL_BEFORE_ASSESSMENT": "QS34",
    "NO_APPROVER": "pack method (O)",
    "NO_RISK_REVIEW": "QS22, QS31",
    "NOT_ASSESSED_IN_AGGREGATE": "QX12, QX13",
    "MISSING_DATE": "[GAP]",
}
NEG_DECISIONS = ("no submission", "not significant", "document only", "no 510", "no notification", "letter to file")


def pdate(s):
    s = (s or "").strip()
    if not s:
        return None
    for f in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"):
        try:
            return dt.datetime.strptime(s, f).date()
        except ValueError:
            pass
    return "bad"


def load(path, mapping):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    out = []
    for r in rows:
        n = {}
        for k, v in r.items():
            key = (k or "").strip().lower()
            key = mapping.get(key, key)
            n[key] = (v or "").strip()
        out.append(n)
    return out


def check(rows):
    f = []
    add = lambda cid, code, detail: f.append({"change_id": cid, "check": code, "detail": detail, "row": ROW[code]})
    by_item = defaultdict(list)
    for r in rows:
        cid = r.get("change_id") or "[no id]"
        by_item[r.get("item", "")].append(r)
        a_ref, rat, dec = r.get("assessment_ref", ""), r.get("rationale", ""), r.get("decision", "").lower()
        if not a_ref:
            add(cid, "NO_ASSESSMENT", "no assessment reference")
        elif not rat:
            add(cid, "NO_RATIONALE", f"assessment {a_ref} has no rationale")
        if dec and any(d in dec for d in NEG_DECISIONS) and not rat:
            add(cid, "DECISION_WITHOUT_BASIS", f"decision '{r.get('decision')}' with no rationale")
        appr_by, appr_d = r.get("approved_by", ""), pdate(r.get("approval_date"))
        if bool(appr_by) != bool(appr_d):
            add(cid, "NO_APPROVER", "approver name without approval date" if appr_by else "approval date without approver name")
        impl, ass_d = pdate(r.get("implemented_date")), pdate(r.get("assessment_date"))
        for label, d in (("implemented_date", impl), ("approval_date", appr_d), ("assessment_date", ass_d)):
            if d == "bad":
                add(cid, "MISSING_DATE", f"{label} unreadable: '{r.get(label)}'")
        if impl and impl != "bad":
            if appr_d and appr_d != "bad" and impl < appr_d:
                add(cid, "IMPL_BEFORE_APPROVAL", f"implemented {impl}, approved {appr_d} ({(appr_d - impl).days} day(s) later)")
            elif not appr_d and r.get("approval_date", "") == "":
                add(cid, "IMPL_BEFORE_APPROVAL", f"implemented {impl}, no approval recorded")
            if ass_d and ass_d != "bad" and impl < ass_d:
                add(cid, "IMPL_BEFORE_ASSESSMENT", f"implemented {impl}, assessed {ass_d}")
        if r.get("touches_hazard", "").lower() in ("yes", "y", "true", "1") and not r.get("risk_review_ref"):
            add(cid, "NO_RISK_REVIEW", "touches a hazard; no risk file review reference")
    for item, rs in by_item.items():
        if item and len(rs) > 1 and not any(x.get("aggregate_ref") for x in rs):
            ids = ", ".join(x.get("change_id", "?") for x in rs)
            for x in rs:
                add(x.get("change_id", "?"), "NOT_ASSESSED_IN_AGGREGATE",
                    f"item '{item}' changed {len(rs)} times ({ids}); no aggregate assessment reference")
    return f


def summarize(rows, findings, rules):
    n = len(rows)
    per = defaultdict(set)
    for x in findings:
        per[x["check"]].add(x["change_id"])
    out = []
    for code in ROW:
        k = len(per.get(code, ()))
        rate = k / n if n else 0
        line = {"check": code, "changes": k, "of": n, "rate": round(rate, 4), "row": ROW[code]}
        if rules and code in rules:
            r = rules[code]
            line["rule"] = r
            if "max_rate" in r:
                line["rule_result"] = "met" if rate <= r["max_rate"] else "not met"
            line["owner"] = r.get("owner", "owner not named")
        out.append(line)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("log")
    ap.add_argument("--rules")
    ap.add_argument("--map", nargs="*", default=[])
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    mapping = dict(m.lower().split("=", 1) for m in a.map)
    rows = load(a.log, mapping)
    if not rows or "change_id" not in rows[0]:
        sys.exit("change_id column not found; use --map yourcolumn=change_id")
    rules = json.load(open(a.rules)) if a.rules else None
    findings = check(rows)
    summ = summarize(rows, findings, rules)
    if a.json:
        print(json.dumps({"changes": len(rows), "findings": findings, "summary": summ}, indent=1))
        return
    print(f"Change log check: {len(rows)} changes, {len(findings)} findings\n")
    print("| Change | Check | Detail | Row |\n|---|---|---|---|")
    for x in findings:
        print(f"| {x['change_id']} | {x['check']} | {x['detail']} | {x['row']} |")
    print("\n| Check | Changes | Rate | Your rule | Result | Owner you named | Row |\n|---|---|---|---|---|---|---|")
    for s in summ:
        rule = s.get("rule", {})
        rt = f"max {rule['max_rate']:.0%}" if "max_rate" in rule else "no rule set"
        print(f"| {s['check']} | {s['changes']} of {s['of']} | {s['rate']:.1%} | {rt} | {s.get('rule_result', '')} | {s.get('owner', '')} | {s['row']} |")
    print("\nCounts and rates only. Thresholds and owners are the person's; no rule set means no verdict.")


if __name__ == "__main__":
    main()
