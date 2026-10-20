#!/usr/bin/env python3
"""Lifecycle checks on the person's own files (medical-software-lifecycle-and-delivery).

Subcommands
  items     --inventory FILE.csv --as-of YYYY-MM-DD
            Software item and SOUP inventory. Columns: id, item, origin (own | ots | open-source),
            manufacturer, version, release_date, patch, support_level, end_of_support,
            safety_class, hazard_ref. Checks the FDA OTS identity fields (EN-026) and the SBOM
            support fields (EN-054). Prints the class as the person wrote it; never assigns one.
  docs      --register FILE.csv --level basic|enhanced --product NAME
            Premarket software document register. Columns: element, document, version, status
            (present | draft | missing), product. Checks the ten FDA documentation elements (PL15)
            with the level notes of PL17 to PL19. The level is the person's.
  problems  --log FILE.csv
            Problem resolution records. Columns: id, item, version_found, effect,
            hazardous_function (yes | no | not given), change_ref, status (open | closed),
            accepted_rationale, accepted_by. Checks the record elements of the old task
            DH-04.03.4.1.3.
  words     ANSWER.md
            Counts a short answer against the 450-word cap, without the calls list and without
            Source or Rows table columns.

Flags
  I1 class not given; I2 class given, hazard not given; I3 identity field not given (OTS or
  open-source); I4 support level or end-of-support date not given (OTS or open-source);
  I5 support level outside the three FDA values; I6 end-of-support date earlier than the read date.
  D1 element missing; D2 element in draft; D3 document names another product.
  P1 item or version not given; P2 effect not given; P3 closed with no change and no accepted
  rationale; P4 rationale with no named acceptor; P5 open on a hazardous function.
Every flag is a fact about the person's file, not a verdict.
"""
import argparse
import csv
import re
import sys
from datetime import date

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
SUPPORT = {"maintained", "no longer maintained", "abandoned"}
ELEMENTS = [
    "Documentation Level Evaluation",
    "Software Description",
    "Risk Management File",
    "Software Requirements Specification",
    "System and Software Architecture Diagram",
    "Software Design Specification",
    "Software Development, Configuration Management, and Maintenance Practices",
    "Software Testing as part of Verification and Validation",
    "Software Version History",
    "Unresolved Software Anomalies",
]
LEVEL_NOTES = {
    ("Software Design Specification", "basic"): "Basic: kept in the design file, not submitted (PL17)",
    ("Software Design Specification", "enhanced"): "Enhanced: submitted with trace to the SRS (PL17)",
    ("Software Development, Configuration Management, and Maintenance Practices", "basic"):
        "Basic: summary of the lifecycle plan and of configuration management and maintenance, or an IEC 62304 declaration (PL18)",
    ("Software Development, Configuration Management, and Maintenance Practices", "enhanced"):
        "Enhanced: adds complete configuration management and maintenance plan documents (PL18)",
    ("Software Testing as part of Verification and Validation", "basic"):
        "Basic: summary of unit, integration and system testing plus system-level protocol and report (PL19)",
    ("Software Testing as part of Verification and Validation", "enhanced"):
        "Enhanced: adds unit and integration protocols and reports (PL19)",
    ("Unresolved Software Anomalies", "basic"): "Each with its impact on safety and effectiveness (PL20)",
    ("Unresolved Software Anomalies", "enhanced"): "Each with its impact on safety and effectiveness (PL20)",
}


def blank(v):
    return v is None or str(v).strip() == "" or str(v).strip().lower() in {"not given", "n/a", "na"}


def show(v):
    return "not given" if blank(v) else str(v).strip()


def pdate(v):
    if blank(v):
        return None
    try:
        y, m, d = [int(x) for x in str(v).strip().split("-")]
        return date(y, m, d)
    except ValueError:
        return None


def full(d):
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def fdate(v):
    d = pdate(v)
    return full(d) if d else show(v)


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return [{(k or "").strip().lower(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(f)]


def cmd_items(a):
    rows = read(a.inventory)
    asof = pdate(a.as_of)
    if not asof:
        print("Read date not given: pass --as-of YYYY-MM-DD (the person's read date). Nothing checked.")
        return 2
    print(f"Read date: {full(asof)}. Fields checked: FDA OTS identity (EN-026) and SBOM support fields (EN-054). "
          "Class is shown as you wrote it.")
    print("| Id | Item | Origin | Version | Release date | Support level | End of support | Class (yours) | Hazard ref | Flags |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    counts = {}
    for r in rows:
        flags = []
        origin = r.get("origin", "").lower()
        third = origin in {"ots", "open-source", "open source", "soup"}
        if blank(r.get("safety_class")):
            flags.append("I1")
        elif blank(r.get("hazard_ref")):
            flags.append("I2")
        if third:
            missing = [k for k in ("manufacturer", "version", "release_date", "patch") if blank(r.get(k))]
            if missing:
                flags.append("I3 (" + ", ".join(m.replace("_", " ") for m in missing) + ")")
            if blank(r.get("support_level")) or blank(r.get("end_of_support")):
                flags.append("I4")
            if not blank(r.get("support_level")) and r["support_level"].lower() not in SUPPORT:
                flags.append("I5")
            eos = pdate(r.get("end_of_support"))
            if eos and eos < asof:
                flags.append("I6")
        for f in flags:
            counts[f[:2]] = counts.get(f[:2], 0) + 1
        print(f"| {show(r.get('id'))} | {show(r.get('item'))} | {show(r.get('origin'))} | {show(r.get('version'))} | "
              f"{fdate(r.get('release_date'))} | {show(r.get('support_level'))} | {fdate(r.get('end_of_support'))} | "
              f"{show(r.get('safety_class'))} | {show(r.get('hazard_ref'))} | {', '.join(flags) or 'none'} |")
    print()
    print(f"Items: {len(rows)}. Flag counts: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none") + ".")
    print("I6 is a date fact against your read date, not urgency. The class, and what follows from an "
          "end-of-support date, are yours; vulnerability handling routes to cybersecurity-and-privacy-by-design.")
    return 0


def norm(s):
    return re.sub(r"[^a-z]", "", s.lower())


def cmd_docs(a):
    rows = read(a.register)
    level = a.level.lower()
    by = {}
    for r in rows:
        by[norm(r.get("element", ""))] = r
    print(f"Documentation level: {level} (yours; the criteria for the level are not in this skill's sources). "
          "Elements: FDA premarket software guidance (PL15).")
    print("| # | Element | Document | Version | Status | Product named | Level note | Flags |")
    print("|---|---|---|---|---|---|---|---|")
    counts = {}
    for i, e in enumerate(ELEMENTS, 1):
        r = by.get(norm(e))
        flags = []
        if not r or blank(r.get("status")) or r.get("status", "").lower() == "missing":
            flags.append("D1")
        elif r.get("status", "").lower() == "draft":
            flags.append("D2")
        if r and not blank(r.get("product")) and norm(r["product"]) != norm(a.product):
            flags.append("D3")
        for f in flags:
            counts[f] = counts.get(f, 0) + 1
        r = r or {}
        print(f"| {i} | {e} | {show(r.get('document'))} | {show(r.get('version'))} | {show(r.get('status')) if r else 'missing'} | "
              f"{show(r.get('product'))} | {LEVEL_NOTES.get((e, level), '')} | {', '.join(flags) or 'none'} |")
    extra = [r.get("element") for r in rows if norm(r.get("element", "")) not in {norm(e) for e in ELEMENTS}]
    print()
    print("Flag counts: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none") + ".")
    if extra:
        print("Rows not matched to an FDA element (shown, not judged): " + "; ".join(extra) + ".")
    print("A register check reads titles and statuses only; it does not open the documents. Whether the set is "
          "ready to file is the regulatory owner's (dh-regulatory-and-quality regulatory-submission-and-dossier).")
    return 0


def cmd_problems(a):
    rows = read(a.log)
    print("Problem resolution records (old task DH-04.03.4.1.3). Hazardous function as you marked it.")
    print("| Id | Item | Version found | Effect | Hazardous function | Change | Status | Accepted by | Flags |")
    print("|---|---|---|---|---|---|---|---|---|")
    counts = {}
    for r in rows:
        flags = []
        if blank(r.get("item")) or blank(r.get("version_found")):
            flags.append("P1")
        if blank(r.get("effect")):
            flags.append("P2")
        st = r.get("status", "").lower()
        if st == "closed" and blank(r.get("change_ref")) and blank(r.get("accepted_rationale")):
            flags.append("P3")
        if not blank(r.get("accepted_rationale")) and blank(r.get("accepted_by")):
            flags.append("P4")
        if st == "open" and r.get("hazardous_function", "").lower() == "yes":
            flags.append("P5")
        for f in flags:
            counts[f] = counts.get(f, 0) + 1
        print(f"| {show(r.get('id'))} | {show(r.get('item'))} | {show(r.get('version_found'))} | {show(r.get('effect'))} | "
              f"{show(r.get('hazardous_function'))} | {show(r.get('change_ref'))} | {show(r.get('status'))} | "
              f"{show(r.get('accepted_by'))} | {', '.join(flags) or 'none'} |")
    print()
    print(f"Records: {len(rows)}. Flag counts: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none") + ".")
    print("Whether an open problem blocks release, and who accepts it, are the person's.")
    return 0


def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out, drop = [], set()
    names = ("source", "rows", "source and date", "source and rows", "source (row)")
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            low = [c.lower() for c in cells]
            if any(c in names for c in low):
                drop = {i for i, c in enumerate(low) if c in names}
            out.append(" ".join(c for i, c in enumerate(cells) if i not in drop))
        else:
            if not line.strip():
                drop = set()
            out.append(line)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9.,'%()/-]*", "\n".join(out)))


def cmd_words(a):
    n = count_words(a.answer)
    print(f"{n} words (calls list and Source or Rows columns excluded); cap 450")
    if n <= 450:
        print("within the short-mode cap")
        return 0
    print("over the cap: cut context paragraphs, repeated row ids in prose, secondary rules, "
          "rows not tied to the question; never a gap, a stop or the record line")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("items")
    i.add_argument("--inventory", required=True)
    i.add_argument("--as-of", required=True)
    d = sub.add_parser("docs")
    d.add_argument("--register", required=True)
    d.add_argument("--level", required=True, choices=["basic", "enhanced", "Basic", "Enhanced"])
    d.add_argument("--product", required=True)
    p = sub.add_parser("problems")
    p.add_argument("--log", required=True)
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"items": cmd_items, "docs": cmd_docs, "problems": cmd_problems, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
