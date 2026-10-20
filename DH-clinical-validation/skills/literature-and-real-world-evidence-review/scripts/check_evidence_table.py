#!/usr/bin/env python3
"""Check an evidence table for missing fields, duplicate studies and appraisal mismatches.

Usage:
  python3 check_evidence_table.py TABLE.csv [--jca] [--json]

One row per study result (a study, an outcome, a time point). Columns (case-insensitive):

  study_id, report_ids (DOI or PMID of each report, separated by ';'), title,
  design, design_basis (publication type, methods section, registry, or "library label"),
  population, intervention, comparator, outcome, timepoint, n_participants,
  effect, effect_measure, ci, rob_tool, rob_judgement, retraction_status,
  publication_type, source_locator (section, table or page the numbers came from),
  in_synthesis (Y or N)

Why each field is required (rows in references/EVIDENCE_SYNTHESIS_METHODS.md and
references/CLINICAL_STUDY_AND_RWE.md):
  study_id, report_ids   the study, not the report, is the unit (ES-22, ES-56)
  PICO fields            review and synthesis PICO (ES-36, ES-37)
  timepoint              outcome specification includes the time point (CV113 [PAPER] doi 10.1136/bmj-2024-081123)
  n_participants, effect, effect_measure, ci
                         numbers of participants and relative or absolute effects (ES-19, ES-98)
  rob_tool, rob_judgement
                         tool and judgment per result (ES-10, ES-70, ES-163, ES-164)
  retraction_status      retraction notices must be examined (ES-119)
  design_basis, source_locator
                         house rule: library design labels are checked against the paper
                         (register N8) and every number keeps its passage (register N3)

The script reports; it does not fill a field, judge risk of bias or decide inclusion.
"""
import csv
import json
import re
import sys
from collections import defaultdict

REQUIRED = ["study_id", "report_ids", "design", "design_basis", "population", "intervention",
            "comparator", "outcome", "timepoint", "n_participants", "effect", "effect_measure",
            "ci", "rob_tool", "rob_judgement", "retraction_status", "source_locator"]
RANDOMIZED = {"rct", "randomized", "randomised", "randomized controlled trial", "cluster rct", "crossover rct"}
ROB2_LEVELS = {"low", "some concerns", "high"}                      # ES-73
ROBINS_LEVELS = {"low", "moderate", "serious", "critical", "no information"}  # ES-76


def norm(row):
    return {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}


def blank(v):
    return (not v) or v.upper() in ("[GAP]", "GAP", "NA", "N/A", "-", "?")


def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def check(rows, jca=False):
    problems, notes = [], []
    missing_by_field = defaultdict(list)
    for i, r in enumerate(rows, start=2):
        label = f"row {i} ({r.get('study_id') or 'no study_id'})"
        for f in REQUIRED:
            if blank(r.get(f, "")):
                missing_by_field[f].append(label)

    # Duplicate reports across different study ids, and the same result counted twice.
    seen_id = {}
    seen_title = {}
    for i, r in enumerate(rows, start=2):
        sid = r.get("study_id", "")
        for rid in [x.strip().lower() for x in r.get("report_ids", "").split(";") if x.strip()]:
            if rid in seen_id and seen_id[rid][1] != sid:
                problems.append(f"Report {rid} appears under two study ids ({seen_id[rid][1]} at row {seen_id[rid][0]}, {sid} at row {i}): one study entered twice (ES-22, ES-56).")
            seen_id.setdefault(rid, (i, sid))
        t = norm_title(r.get("title", ""))
        if t:
            if t in seen_title and seen_title[t][1] != sid:
                problems.append(f"Same title under two study ids (rows {seen_title[t][0]} and {i}): check whether it is one study.")
            seen_title.setdefault(t, (i, sid))
    by_result = defaultdict(list)
    for i, r in enumerate(rows, start=2):
        key = (r.get("study_id", "").lower(), r.get("outcome", "").lower(), r.get("timepoint", "").lower())
        by_result[key].append(i)
    for (sid, out, tp), idx in by_result.items():
        if sid and len(idx) > 1:
            problems.append(f"Study {sid}, outcome '{out or '?'}', time point '{tp or '?'}' appears in rows {idx}: the same result would be counted more than once (ES-56).")
    reports_per_study = defaultdict(set)
    for r in rows:
        for rid in r.get("report_ids", "").split(";"):
            if rid.strip():
                reports_per_study[r.get("study_id", "")].add(rid.strip().lower())
    for sid, reps in reports_per_study.items():
        if sid and len(reps) > 1:
            notes.append(f"Study {sid} has {len(reps)} reports ({', '.join(sorted(reps))}); keep them under one study (ES-56).")

    for i, r in enumerate(rows, start=2):
        label = f"row {i} ({r.get('study_id') or 'no study_id'})"
        design = r.get("design", "").lower()
        basis = r.get("design_basis", "").lower()
        if "library" in basis or "label" in basis:
            problems.append(f"{label}: design '{design}' rests on a library label; check it against the paper's methods (register N8).")
        ptype = r.get("publication_type", "").lower()
        if "conference" in ptype or "abstract" in ptype:
            notes.append(f"{label}: conference abstract; not a full report.")
        if "preprint" in ptype or design == "preprint":
            notes.append(f"{label}: preprint; not peer reviewed (ES-53 allows preprints as a source; say so in the table).")
        tool = r.get("rob_tool", "").lower().replace(" ", "")
        judg = r.get("rob_judgement", "").lower()
        randomized = design in RANDOMIZED
        if randomized:
            if "robins" in tool:
                problems.append(f"{label}: randomized design assessed with ROBINS-I; ROBINS-I is for non-randomized studies (ES-75 [PAPER] doi 10.1136/bmj.i4919, ES-164).")
            if jca and tool and "rob1" not in tool and "rob 1" not in r.get("rob_tool", "").lower():
                problems.append(f"{label}: EU JCA validity guidance asks for Cochrane RoB 1 for RCT outcomes (ES-163); table shows '{r.get('rob_tool')}'.")
            if not jca and "rob1" in tool:
                notes.append(f"{label}: RoB 1 used; the Cochrane Handbook uses RoB 2, the EU JCA asks for RoB 1 (ES-163, conflict noted in the research file).")
            if "rob2" in tool and not blank(judg) and judg not in ROB2_LEVELS:
                problems.append(f"{label}: RoB 2 judgment '{r.get('rob_judgement')}' is not one of Low, Some concerns, High (ES-73).")
        elif design and design not in ("systematic_review", "meta_analysis", "other", "preprint"):
            if "rob2" in tool or "rob1" in tool:
                problems.append(f"{label}: non-randomized design '{design}' assessed with a randomized-trial tool; ROBINS-I applies to comparative non-randomized studies (ES-75 [PAPER] doi 10.1136/bmj.i4919, ES-164).")
        if "robins" in tool:
            if not blank(judg) and judg not in ROBINS_LEVELS:
                problems.append(f"{label}: ROBINS-I judgment '{r.get('rob_judgement')}' is not one of Low, Moderate, Serious, Critical, No information (ES-76).")
            if judg == "critical" and r.get("in_synthesis", "").lower() in ("y", "yes"):
                problems.append(f"{label}: critical risk of bias and marked for synthesis; ROBINS-I says such a study should not be included in any synthesis (ES-77).")
        if design in ("systematic_review", "meta_analysis"):
            notes.append(f"{label}: a review in a table of primary studies; check its included studies against your own to avoid double counting.")
        rs = r.get("retraction_status", "").lower()
        if rs in ("retracted", "expression_of_concern", "expression of concern"):
            problems.append(f"{label}: retraction status '{rs}'; examine the notice before use (ES-119, ES-125).")
        elif rs == "corrected":
            notes.append(f"{label}: corrected; read the erratum (ES-121).")
        if not blank(r.get("effect", "")) and blank(r.get("source_locator", "")):
            problems.append(f"{label}: an effect is entered without the section, table or page it came from.")

    return dict(missing_by_field), problems, notes


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    with open(argv[1], newline="", encoding="utf-8-sig") as f:
        rows = [norm(r) for r in csv.DictReader(f)]
    jca = "--jca" in argv
    missing, problems, notes = check(rows, jca)
    if "--json" in argv:
        print(json.dumps({"rows": len(rows), "missing_by_field": missing, "problems": problems, "notes": notes}, indent=1))
        return 0 if not (missing or problems) else 1
    print(f"Evidence table check: {argv[1]} ({len(rows)} rows){' with EU JCA rules' if jca else ''}")
    print("\nMissing fields ([GAP] or blank)")
    if not missing:
        print("  none")
    for f in REQUIRED:
        if f in missing:
            print(f"  {f}: {len(missing[f])} row(s): {', '.join(missing[f])}")
    print("\nProblems" if problems else "\nProblems: none found")
    for p in problems:
        print("  - " + p)
    if notes:
        print("\nNotes")
        for n in notes:
            print("  - " + n)
    return 0 if not (missing or problems) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
