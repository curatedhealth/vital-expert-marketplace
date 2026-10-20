#!/usr/bin/env python3
"""Responsible-AI release evidence check, run on the person's own evidence index.

Commands
  read     reads the evidence index for one release as of a read date and prints each item as
           present, missing, not yet applicable or not assessable, with flags G1 to G8.
  review   applies the person's pass rule ("all applicable" or "listed:ID,ID,...") and prints,
           for every item that fails it, the owner, the date it will be present and whether
           release waits, all as the person recorded them ("owner not named" / "not given"
           otherwise), plus the computed count of items that would have to become present.
  words    counts a short answer against the 450-word cap (calls list and Source/Rows columns
           left out).

Completeness, not quality: "present" means the index points to evidence of the required type for
this release; whether the evidence is good enough is the person's judgment. Nothing here sets a
rule, an owner or a date.

Evidence index CSV columns:
  item_id, requirement, rows, applies, required_type, evidence_ref, evidence_type, evidence_date,
  model_version, dataset_version, groups_not_seen, owner, present_by, release_waits
  applies: "yes", "no", "from YYYY-MM-DD" or empty (not given)
  required_type / evidence_type: test, document, control, policy (evidence_type empty = none)
  dates ISO (YYYY-MM-DD); groups_not_seen separated by ";"
"""
import argparse
import csv
import datetime as dt
import re
import sys

CAP = 450
FLAGS = {
    "G1": "no evidence recorded",
    "G2": "policy statement given in place of a test",
    "G3": "evidence is for a different model version than this release",
    "G4": "evidence dated after the read date",
    "G5": "groups not seen at test time, still not tested",
    "G6": "owner not named for a missing item",
    "G7": "date the item will be present: not given, or earlier than the read date",
    "G8": "whether release waits: not given",
}


def d(s):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return dt.date.fromisoformat(s)
    except ValueError:
        return "bad"


def full(x):
    if x is None:
        return "not given"
    if x == "bad":
        return "unreadable date"
    return f"{x.day} {x.strftime('%B')} {x.year}"


def load(path):
    rows = list(csv.DictReader(open(path, newline="", encoding="utf-8")))
    if not rows:
        sys.exit("empty index")
    return rows


def assess(r, release, as_of):
    flags, note = [], ""
    applies = (r.get("applies") or "").strip().lower()
    if applies == "no":
        return "not applicable", flags, "you marked it not applicable"
    if not applies:
        return "not assessable", flags, "applicability not given"
    if applies.startswith("from"):
        start = d(applies[4:].strip())
        if start in (None, "bad"):
            return "not assessable", flags, "applicability date unreadable"
        if start > as_of:
            return "not yet applicable", flags, f"applies from {full(start)}"
    ref = (r.get("evidence_ref") or "").strip()
    etype = (r.get("evidence_type") or "").strip().lower()
    rtype = (r.get("required_type") or "").strip().lower()
    status = "present"
    if not ref:
        flags.append("G1")
        status = "missing"
    elif rtype == "test" and etype == "policy":
        flags.append("G2")
        status = "missing"
    mv = (r.get("model_version") or "").strip()
    if status == "present" and rtype == "test":
        if not mv:
            status, note = "not assessable", "model version of the evidence not given"
        elif mv != release:
            flags.append("G3")
            status, note = "not assessable", f"evidence on {mv}, release is {release}"
    ed = d(r.get("evidence_date"))
    if ed not in (None, "bad") and ed > as_of:
        flags.append("G4")
    if (r.get("groups_not_seen") or "").strip():
        flags.append("G5")
    if status in ("missing", "not assessable"):
        if not (r.get("owner") or "").strip():
            flags.append("G6")
        pb = d(r.get("present_by"))
        if pb in (None, "bad") or pb < as_of:
            flags.append("G7")
        if not (r.get("release_waits") or "").strip():
            flags.append("G8")
    return status, flags, note


def cmd_read(a):
    as_of = d(a.as_of)
    if as_of in (None, "bad"):
        sys.exit("--as-of must be the person's read date, YYYY-MM-DD")
    rows = load(a.index)
    print(f"Release: {a.release} | Read date: {full(as_of)} | Index: {a.index}")
    print("| Item | Requirement | Rows | Status | Evidence | Evidence date | Flags | Note |")
    print("|---|---|---|---|---|---|---|---|")
    counts = {}
    unseen = []
    for r in rows:
        st, fl, note = assess(r, a.release, as_of)
        counts[st] = counts.get(st, 0) + 1
        if "G5" in fl:
            unseen.append((r["item_id"], r["groups_not_seen"]))
        print(f"| {r['item_id']} | {r['requirement']} | {r.get('rows','')} | {st} | "
              f"{r.get('evidence_ref') or 'none'} | {full(d(r.get('evidence_date')))} | "
              f"{', '.join(fl) or ''} | {note} |")
    print()
    print("Counts: " + "; ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    for item, groups in unseen:
        print(f"G5 {item}: not seen at test time and not tested: {groups.replace(';', ', ')}")
    used = sorted({f for r in rows for f in assess(r, a.release, as_of)[1]})
    for f in used:
        print(f"{f}: {FLAGS[f]}")
    print("Completeness only: whether present evidence is good enough is yours.")
    return 0


def cmd_review(a):
    as_of = d(a.as_of)
    if as_of in (None, "bad"):
        sys.exit("--as-of must be the person's read date, YYYY-MM-DD")
    rows = load(a.index)
    if not a.pass_rule:
        print("Pass rule: not given [GAP]. Values are reported; nothing is marked met or failed.")
        return 1
    rule = a.pass_rule.strip()
    if rule == "all applicable":
        scope = None
    elif rule.startswith("listed:"):
        scope = {x.strip() for x in rule[7:].split(",") if x.strip()}
    else:
        sys.exit('pass rule must be "all applicable" or "listed:ID,ID"')
    print(f"Release: {a.release} | Read date: {full(as_of)} | Your pass rule: {rule} "
          f"(written on {a.rule_date or 'not given'})")
    failed = []
    for r in rows:
        if scope is not None and r["item_id"] not in scope:
            continue
        st, fl, note = assess(r, a.release, as_of)
        if st in ("missing", "not assessable"):
            failed.append((r, st, fl, note))
    if scope:
        missing_ids = scope - {r["item_id"] for r in rows}
        for m in sorted(missing_ids):
            print(f"Item {m} named in your rule is not in the index: not assessable.")
    print("| Item | Requirement | Status | Why | Owner | Present by | Release waits |")
    print("|---|---|---|---|---|---|---|")
    for r, st, fl, note in failed:
        why = "; ".join([FLAGS[f] for f in fl if f in ("G1", "G2", "G3")] + ([note] if note else []))
        pb = d(r.get("present_by"))
        pbs = full(pb)
        if pb not in (None, "bad") and pb < as_of:
            pbs += " (earlier than the read date)"
        print(f"| {r['item_id']} | {r['requirement']} | {st} | {why} | "
              f"{(r.get('owner') or '').strip() or 'owner not named'} | {pbs} | "
              f"{(r.get('release_waits') or '').strip() or 'not given'} |")
    n = len(failed)
    print()
    if n == 0:
        print("Every item in your rule's scope is present or not yet applicable as of the read date.")
    else:
        print(f"Your rule is not met: {n} item(s) are missing or not assessable; all {n} would have to become present "
              "and assessable for this release to meet it (computed from the index).")
    print("Release go or no-go is yours; a failed item stays open until you close it with evidence.")
    return 0


def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out, drop = [], set()
    names = ("source", "rows", "source and date", "source and rows", "source and rows (doi for [paper])")
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
    print(f"{n} words")
    if n <= CAP:
        print("within the short-mode cap")
        return 0
    print("over the cap: cut context paragraphs, repeated row ids in prose, secondary rules, rows not tied "
          "to the question; never a gap, a stop or the record line")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("read")
    r.add_argument("--index", required=True)
    r.add_argument("--release", required=True, help="model version of the release")
    r.add_argument("--as-of", required=True, help="the person's read date, YYYY-MM-DD")
    v = sub.add_parser("review")
    v.add_argument("--index", required=True)
    v.add_argument("--release", required=True)
    v.add_argument("--as-of", required=True)
    v.add_argument("--pass-rule", help='the person\'s rule: "all applicable" or "listed:ID,ID"')
    v.add_argument("--rule-date", help="date the person wrote the rule")
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"read": cmd_read, "review": cmd_review, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
