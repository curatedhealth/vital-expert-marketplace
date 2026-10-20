#!/usr/bin/env python3
"""Build PRISMA 2020 flow counts from a screening log and check that they reconcile.

Usage:
  python3 prisma_flow.py LOG.csv [--rule cochrane|nice|iqwig|rapid|none] [--jca] [--json]

The log has one row per record (a title or abstract from one source). Columns
(header names are case-insensitive; extra columns are ignored):

  record_id        unique id of the record in the log (required)
  source           where it came from, as the person names it (PubMed, Embase via Ovid, ClinicalTrials.gov ...)
  source_type      database | register | website | organization | citation | other
  duplicate_of     record_id of the kept record if this one was removed as a duplicate, else blank
  auto_excluded    Y if an automation tool removed it before human screening, else blank
  removed_other    reason text if removed before screening for another reason, else blank
  ta_decision      include | exclude  (title and abstract screening)
  ta_reviewers     number of people who screened this record at title/abstract
  report_sought    Y if the full report was sought
  report_retrieved Y | N
  ft_decision      include | exclude  (full-text eligibility)
  ft_reason        reason for a full-text exclusion
  ft_reviewers     number of people who made the full-text decision independently
  study_id         the study this report belongs to (several reports may share one study)
  ai_assisted      steps where AI helped, separated by ';' (e.g. screening;extraction), else blank

Counting rules come from the sourced rows cited in references/review-rules-by-body.md:
PRISMA 2020 flow elements (ES-20 [PAPER] doi 10.1136/bmj.n160), human versus automation exclusions (ES-21), records
versus reports versus studies (ES-22, ES-56), excluded reports with reasons (ES-13),
records per source (ES-31). Reviewer rules: Cochrane (ES-57, ES-58), NICE (ES-129),
IQWiG (ES-139), Cochrane rapid reviews 2021 (ES-112). --jca adds the EU JCA checks:
exclusion list with reasons (ES-162) and disclosure of every AI-assisted step (ES-170).

The script counts and checks. It does not decide eligibility, and it never changes a
reviewer's decision.
"""
import csv
import json
import sys
from collections import Counter, OrderedDict

RULES = {
    "cochrane": {"ta_min": 1, "ft_min": 2,
                 "text": "Cochrane MECIR C39: title/abstract by one person is acceptable; full-text decisions by two people independently (ES-57, ES-58)"},
    "nice": {"ta_min": 2, "ft_min": 2,
             "text": "NICE PMG36: more than one reviewer should assess all records (ES-129)"},
    "iqwig": {"ta_min": 2, "ft_min": 2,
              "text": "IQWiG General Methods 8.0: all selection steps by two persons independently (ES-139)"},
    "rapid": {"ta_min": 1, "ft_min": 1, "ta_dual_share": 0.20,
              "text": "Cochrane rapid review interim guidance 2021: dual screening of at least 20% of abstracts; second reviewer checks all full-text excludes (ES-112)"},
    "none": None,
}


def norm(row):
    return {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}


def yes(v):
    return v.strip().lower() in ("y", "yes", "true", "1")


def to_int(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def build(rows, rule_name="none", jca=False):
    problems, notes = [], []
    ids = Counter(r.get("record_id", "") for r in rows)
    for rid, n in ids.items():
        if not rid:
            problems.append("A row has no record_id.")
        elif n > 1:
            problems.append(f"record_id {rid} appears {n} times in the log.")
    known = set(ids)

    by_source = Counter()
    by_source_type = Counter()
    for r in rows:
        by_source[r.get("source") or "[source not given]"] += 1
        by_source_type[r.get("source_type") or "[type not given]"] += 1

    dup = [r for r in rows if r.get("duplicate_of")]
    for r in dup:
        if r["duplicate_of"] not in known:
            problems.append(f"{r['record_id']}: duplicate_of {r['duplicate_of']} is not a record in the log.")
        if r.get("ta_decision"):
            problems.append(f"{r['record_id']}: removed as a duplicate but also has a title/abstract decision.")
    auto = [r for r in rows if not r.get("duplicate_of") and yes(r.get("auto_excluded", ""))]
    other = [r for r in rows if not r.get("duplicate_of") and not yes(r.get("auto_excluded", "")) and r.get("removed_other")]
    removed_ids = {r["record_id"] for r in dup + auto + other}
    screened = [r for r in rows if r["record_id"] not in removed_ids]

    ta_excl = [r for r in screened if r.get("ta_decision", "").lower() == "exclude"]
    ta_incl = [r for r in screened if r.get("ta_decision", "").lower() == "include"]
    no_ta = [r for r in screened if r.get("ta_decision", "").lower() not in ("include", "exclude")]
    for r in no_ta:
        problems.append(f"{r['record_id']}: screened but no title/abstract decision (include or exclude).")
    for r in ta_excl:
        if r.get("ft_decision") or yes(r.get("report_sought", "")):
            problems.append(f"{r['record_id']}: excluded at title/abstract but has a full-text entry.")

    sought = [r for r in ta_incl if yes(r.get("report_sought", "")) or r.get("ft_decision") or r.get("report_retrieved")]
    not_sought = [r for r in ta_incl if r not in sought]
    for r in not_sought:
        problems.append(f"{r['record_id']}: included at title/abstract but no report was sought.")
    not_retrieved = [r for r in sought if r.get("report_retrieved", "").lower() in ("n", "no")]
    assessed = [r for r in sought if r not in not_retrieved]
    for r in not_retrieved:
        if r.get("ft_decision"):
            problems.append(f"{r['record_id']}: report marked not retrieved but has a full-text decision.")
    ft_excl = [r for r in assessed if r.get("ft_decision", "").lower() == "exclude"]
    ft_incl = [r for r in assessed if r.get("ft_decision", "").lower() == "include"]
    ft_none = [r for r in assessed if r.get("ft_decision", "").lower() not in ("include", "exclude")]
    for r in ft_none:
        problems.append(f"{r['record_id']}: report assessed but no full-text decision.")
    reasons = Counter()
    for r in ft_excl:
        if not r.get("ft_reason"):
            problems.append(f"{r['record_id']}: full-text exclusion without a reason (PRISMA item 16b, ES-13).")
            reasons["[reason missing]"] += 1
        else:
            reasons[r["ft_reason"]] += 1

    studies = OrderedDict()
    for r in ft_incl:
        sid = r.get("study_id") or f"[no study_id: {r['record_id']}]"
        if not r.get("study_id"):
            problems.append(f"{r['record_id']}: included report has no study_id; studies cannot be counted (ES-22, ES-56).")
        studies.setdefault(sid, []).append(r["record_id"])

    counts = OrderedDict([
        ("records_identified", len(rows)),
        ("records_identified_by_source", dict(by_source)),
        ("records_identified_by_source_type", dict(by_source_type)),
        ("duplicates_removed", len(dup)),
        ("records_marked_ineligible_by_automation", len(auto)),
        ("records_removed_other_reasons", len(other)),
        ("records_screened", len(screened)),
        ("records_excluded", len(ta_excl)),
        ("reports_sought_for_retrieval", len(sought)),
        ("reports_not_retrieved", len(not_retrieved)),
        ("reports_assessed_for_eligibility", len(assessed)),
        ("reports_excluded", len(ft_excl)),
        ("reports_excluded_reasons", dict(reasons)),
        ("new_studies_included", len(studies)),
        ("reports_of_included_studies", len(ft_incl)),
    ])

    # Reconciliation (each line must hold).
    checks = [
        ("identified = duplicates + automation + other removed + screened",
         len(rows) == len(dup) + len(auto) + len(other) + len(screened)),
        ("screened = excluded + included at title/abstract + undecided",
         len(screened) == len(ta_excl) + len(ta_incl) + len(no_ta)),
        ("sought = not retrieved + assessed", len(sought) == len(not_retrieved) + len(assessed)),
        ("assessed = excluded + included + undecided", len(assessed) == len(ft_excl) + len(ft_incl) + len(ft_none)),
        ("excluded reports = sum of reasons", len(ft_excl) == sum(reasons.values())),
        ("studies <= reports of included studies", len(studies) <= len(ft_incl)),
        ("sum of records by source = records identified", sum(by_source.values()) == len(rows)),
    ]
    for label, ok in checks:
        if not ok:
            problems.append(f"Counts do not reconcile: {label}.")
    if not_sought:
        problems.append(f"{len(not_sought)} record(s) included at title/abstract are missing from the full-text stage.")

    # Reviewer rule
    rule = RULES.get(rule_name)
    if rule:
        notes.append("Reviewer rule applied: " + rule["text"] + ".")
        ta_counts = [to_int(r.get("ta_reviewers")) for r in screened]
        if any(c is None for c in ta_counts):
            problems.append("ta_reviewers is blank for some screened records; the reviewer rule cannot be checked for them [GAP].")
        if "ta_dual_share" in rule:
            known_c = [c for c in ta_counts if c is not None]
            share = (sum(1 for c in known_c if c >= 2) / len(known_c)) if known_c else 0
            notes.append(f"Share of screened records with two reviewers: {share:.0%}.")
            if share < rule["ta_dual_share"]:
                problems.append(f"Dual title/abstract screening covers {share:.0%} of records, below the 20% the rule names (ES-112).")
            for r in ft_excl:
                c = to_int(r.get("ft_reviewers"))
                if c is None or c < 2:
                    problems.append(f"{r['record_id']}: full-text exclude not checked by a second reviewer (ES-112).")
        else:
            for r in screened:
                c = to_int(r.get("ta_reviewers"))
                if c is not None and c < rule["ta_min"]:
                    problems.append(f"{r['record_id']}: {c} title/abstract reviewer(s); the rule asks for {rule['ta_min']}.")
            for r in assessed:
                c = to_int(r.get("ft_reviewers"))
                if c is None:
                    problems.append(f"{r['record_id']}: ft_reviewers blank [GAP].")
                elif c < rule["ft_min"]:
                    problems.append(f"{r['record_id']}: {c} full-text reviewer(s); the rule asks for {rule['ft_min']}.")

    # AI-assisted steps and the human versus automation split
    ai_steps = Counter()
    for r in rows:
        for s in (r.get("ai_assisted") or "").split(";"):
            s = s.strip().lower()
            if s:
                ai_steps[s] += 1
    if auto:
        notes.append(f"{len(auto)} record(s) removed by automation tools; report them separately from human exclusions in the flow diagram (ES-21).")
    if jca:
        notes.append("EU JCA: full-text exclusions with reasons go in Appendix D.2.2 and all results as RIS files (ES-162).")
        if ai_steps or auto:
            notes.append("EU JCA: AI-assisted steps found (" + ", ".join(f"{k}: {v} rows" for k, v in ai_steps.items()) +
                         (f"; automation removals: {len(auto)}" if auto else "") +
                         "). Each must be documented in the dossier, with a named human responsible (ES-169, ES-170).")
    counts["ai_assisted_steps"] = dict(ai_steps)
    return counts, checks, problems, notes


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = argv[1]
    rule = "none"
    if "--rule" in argv:
        rule = argv[argv.index("--rule") + 1].lower()
        if rule not in RULES:
            print(f"Unknown rule {rule}. Use one of: {', '.join(RULES)}")
            return 2
    jca = "--jca" in argv
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = [norm(r) for r in csv.DictReader(f)]
    counts, checks, problems, notes = build(rows, rule, jca)
    if "--json" in argv:
        print(json.dumps({"counts": counts, "reconciles": all(ok for _, ok in checks) and not problems,
                          "problems": problems, "notes": notes}, indent=1))
        return 0 if not problems else 1
    print(f"PRISMA 2020 flow counts from {path}")
    for k, v in counts.items():
        if isinstance(v, dict):
            print(f"  {k}:")
            for kk, vv in v.items():
                print(f"      {kk}: {vv}")
        else:
            print(f"  {k}: {v}")
    print("\nReconciliation")
    for label, ok in checks:
        print(f"  [{'ok' if ok else 'FAIL'}] {label}")
    if notes:
        print("\nNotes")
        for n in notes:
            print("  - " + n)
    print("\nProblems" if problems else "\nProblems: none found")
    for p in problems:
        print("  - " + p)
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
