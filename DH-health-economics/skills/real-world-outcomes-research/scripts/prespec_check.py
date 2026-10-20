#!/usr/bin/env python3
"""Check a real-world study's execution log for prespecification order.

Usage: python3 prespec_check.py LOG.json [--md OUT.md]

The log is the person's own dated record (see examples/illustrative_study_log.json).
The script checks order and completeness only. It never decides whether a study is
acceptable; that is the person's rule (task B1).

Checks and the rows they apply (references/execution-and-reporting.md):
  1. Study type declared HETE or exploratory ............ HE-026
  2. Protocol final before first outcome access ......... CV94 (devices), CV75 (drugs)
  3. Analysis plan final before first outcome access .... CV94, CV75
  4. HETE only: public registration before analysis ..... HE-027
  5. Every revision dated and with a reason ............. CV75
  6. Revisions after first outcome access ............... reported as deviations (HE-028)
  7. Deviations carry a reason, for the conformance statement (HE-028)
  8. Linkage: planned yes or no; if yes, inconsistency rule given or [GAP] .. CV24

[PAPER] rows HE-025 to HE-030 print with their DOI (Berger et al. 2017, 10.1002/pds.4297).
"""
import json
import sys
from datetime import date

GAP = "[GAP]"


def d(value):
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return "bad"


def full(x):
    return f"{x.day} {x.strftime('%B %Y')}" if isinstance(x, date) else str(x)


def order_check(label, earlier, later, later_label, row):
    if earlier is None:
        return (label, f"Not dated {GAP}: order cannot be shown", row)
    if later is None:
        return (label, f"{later_label[:1].upper() + later_label[1:]} not dated {GAP}: order cannot be shown", row)
    if "bad" in (earlier, later):
        return (label, f"Date not in YYYY-MM-DD form {GAP}", row)
    if earlier < later:
        return (label, f"Order shown: {full(earlier)} is before {later_label} on {full(later)}", row)
    return (label, f"Order not shown: {full(earlier)} is on or after {later_label} on {full(later)}", row)


def run(log):
    rows = []
    stype = (log.get("study_type") or "").strip().lower()
    if stype in ("hete", "exploratory"):
        rows.append(("Study type declared", f"Declared {stype.upper() if stype == 'hete' else stype}"
                     f" on {full(d(log.get('study_type_declared_on')) or GAP)}", "HE-026"))
    else:
        rows.append(("Study type declared", f"Not declared {GAP}", "HE-026"))

    access = d((log.get("first_outcome_access") or {}).get("date"))
    docs = {doc.get("id"): doc for doc in log.get("documents", [])}
    for key, label in (("protocol", "Protocol final before first outcome access"),
                       ("analysis_plan", "Analysis plan final before first outcome access")):
        doc = docs.get(key)
        rows.append(order_check(label, d(doc.get("finalized_on")) if doc else None, access,
                                "first outcome access", "CV94, CV75"))

    analysis = d(log.get("analysis_started_on"))
    if stype == "hete":
        reg = log.get("registration") or {}
        r = order_check("Public registration before analysis", d(reg.get("submitted_on")), analysis,
                        "analysis start", "HE-027")
        if reg.get("registry"):
            r = (r[0], r[1] + f" ({reg.get('registry')} {reg.get('id') or 'id not given ' + GAP})", r[2])
        rows.append(r)

    late = []
    for rev in log.get("revisions", []):
        rd = d(rev.get("date"))
        problems = []
        if rd is None:
            problems.append("not dated")
        if not rev.get("reason"):
            problems.append("no reason")
        tag = f"{rev.get('doc', '?')} v{rev.get('version', '?')}"
        if problems:
            rows.append((f"Revision {tag}", f"{', '.join(problems)} {GAP}", "CV75"))
        else:
            after = isinstance(rd, date) and isinstance(access, date) and rd >= access
            if after:
                late.append(tag)
            unknown = not isinstance(access, date)
            rows.append((f"Revision {tag}", f"Dated {full(rd)}, reason given"
                         + ("; made after first outcome access: report as a deviation, not as prespecified" if after else "")
                         + (f"; position relative to first outcome access unknown {GAP}" if unknown else ""),
                         "CV75, HE-028" if after else "CV75"))

    devs = log.get("deviations", [])
    missing = [x for x in devs if not x.get("reason")]
    rows.append(("Deviations for the conformance statement",
                 f"{len(devs)} logged" + (f"; {len(missing)} without a reason {GAP}" if missing else "")
                 + (f"; plus {len(late)} revision(s) after outcome access" if late else ""), "HE-028"))

    link = log.get("linkage") or {}
    planned = link.get("planned")
    if planned is True:
        ok = link.get("in_protocol") and link.get("inconsistency_rule")
        rows.append(("Linkage", "Planned: yes; " + ("in protocol with an inconsistency rule" if ok
                     else f"inconsistency rule not given {GAP}"), "CV24"))
    elif planned is False:
        rows.append(("Linkage", "Planned: no", "CV24"))
    else:
        rows.append(("Linkage", f"Planned: not stated {GAP}", "CV24"))
    return [(a, b, with_doi(c)) for a, b, c in rows]


# [PAPER] rows: the DOI travels with the row id. HE-025 to HE-030 are Berger et al. 2017.
PAPER_DOI = {f"HE-0{n}": "10.1002/pds.4297" for n in range(25, 31)}


def with_doi(cell):
    parts = []
    for rid in [x.strip() for x in cell.split(",")]:
        parts.append(f"{rid} (DOI {PAPER_DOI[rid]})" if rid in PAPER_DOI else rid)
    return ", ".join(parts)


def to_md(log, rows):
    out = [f"Execution record check: {log.get('study', 'study not named')}",
           f"Log as supplied; checked {full(date.today())}. Order and completeness only; acceptability is your rule.",
           "", "| Check | Result | Row |", "|---|---|---|"]
    out += [f"| {a} | {b} | {c} |" for a, b, c in rows]
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as fh:
        log = json.load(fh)
    md = to_md(log, run(log))
    if "--md" in sys.argv:
        with open(sys.argv[sys.argv.index("--md") + 1], "w", encoding="utf-8") as fh:
            fh.write(md + "\n")
    print(md)
