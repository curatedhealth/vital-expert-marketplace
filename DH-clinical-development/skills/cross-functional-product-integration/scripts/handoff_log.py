#!/usr/bin/env python3
"""Handoff log helper for the VITAL Clinical Product Development pack.

Works only on the person's own handoff log (CSV). It never invents a value:
a missing field prints as [GAP]. Rules about what counts as "received",
"late" or "critical" are the person's; the script applies the rule the
person confirmed (receipt = received_on plus a named received_by that matches
receiver_named) and says so in its output. A handoff with no named receiver is
not measurable and the script asks for the receiver (measurement-rules.md
section 3); it never guesses one.

Columns (header row required; extra columns are ignored):
  id, work_product, category, ctq, sender_function, receiver_function,
  receiver_named, owner_owes, asked_on, due_on, received_on, received_by,
  blocked_decision, depends_on, late_path, look_again_on
Dates are YYYY-MM-DD. depends_on lists ids separated by ";".

Subcommands:
  check  FILE --as-of DATE            completeness of each handoff record and
                                      days open (cross-functional integration A1/A2)
  score  FILE --from DATE --to DATE   received / late / open / not measurable for
                                      handoffs due in the period (monitoring A2)
  repair FILE --as-of DATE            open and late handoffs with owner, blocked
                                      decision and look-again date, in dependency
                                      order (monitoring B1)
"""
import argparse
import csv
import sys
from datetime import date

REQUIRED_MAP = ["work_product", "sender_function", "receiver_function", "receiver_named",
                "blocked_decision"]
REQUIRED_DEP = ["owner_owes", "asked_on", "late_path"]
GAP = "[GAP]"


def d(value):
    value = (value or "").strip()
    if not value:
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        return "bad"


def load(path):
    with open(path, newline="", encoding="utf-8") as fh:
        rows = [{k.strip(): (v or "").strip() for k, v in r.items() if k}
                for r in csv.DictReader(fh)]
    if not rows:
        sys.exit("No rows in " + path)
    ids = [r.get("id", "") for r in rows]
    if len(set(ids)) != len(ids) or "" in ids:
        sys.exit("Every row needs a unique id.")
    return rows


def show(value):
    return value if value else GAP


def deps(row):
    return [x.strip() for x in row.get("depends_on", "").split(";") if x.strip()]


def dependency_order(rows, keep):
    """Order the kept ids so that an item comes after the open items it waits on.
    Returns (ordered ids, cycle ids)."""
    kept = {r["id"]: r for r in rows if r["id"] in keep}
    order, state = [], {}
    cycle = set()

    def visit(i, stack):
        if state.get(i) == 2:
            return
        if state.get(i) == 1:
            cycle.update(stack[stack.index(i):])
            return
        state[i] = 1
        for j in deps(kept[i]):
            if j in kept:
                visit(j, stack + [j])
        state[i] = 2
        order.append(i)

    for i in kept:
        visit(i, [i])
    return order, sorted(cycle)


def status(row, start, end):
    """Apply the person's confirmed rule. Returns one of received, late, open,
    not measurable, with the reason."""
    due = d(row.get("due_on"))
    got = d(row.get("received_on"))
    by = row.get("received_by", "")
    named = row.get("receiver_named", "")
    if due in (None, "bad"):
        return "not measurable", "no due date " + GAP + "; ask the person for it"
    if not named:
        # measurement-rules.md section 3: a handoff without a named receiver is
        # not measurable, whether or not it has arrived. The script does not
        # guess a receiver; it asks.
        return "not measurable", "receiver not named " + GAP + "; ask the person who receives it"
    if got == "bad":
        return "not measurable", "received_on not a date " + GAP + "; ask the person for it"
    if got is None or got > end:
        return "open", "not received by " + end.isoformat()
    if not by:
        return "not measurable", "received_on given but no received_by " + GAP + "; ask who received it"
    if by.lower() != named.lower():
        return "not measurable", "received_by (%s) is not the named receiver (%s); ask whether the person's rule counts it" % (by, named)
    if got > due:
        return "late", "received %s, due %s (%d days after)" % (got, due, (got - due).days)
    return "received", "received %s, due %s" % (got, due)


def cmd_check(rows, as_of):
    print("# Handoff log check as of %s\n" % as_of)
    print("Rule applied: a field left blank is printed as %s. The log is the person's; nothing is filled in.\n" % GAP)
    print("| id | Work product | Sender to receiver | Blocked decision | Owner owes | Asked on | Days open | Late path | Missing |")
    print("|---|---|---|---|---|---|---|---|---|")
    missing_total = 0
    for r in rows:
        miss = [f for f in REQUIRED_MAP + REQUIRED_DEP if not r.get(f)]
        missing_total += len(miss)
        asked, got = d(r.get("asked_on")), d(r.get("received_on"))
        if asked in (None, "bad"):
            days = GAP
        elif got not in (None, "bad"):
            days = "received"
        else:
            days = str((as_of - asked).days)
        print("| %s | %s | %s to %s | %s | %s | %s | %s | %s | %s |" % (
            r["id"], show(r.get("work_product")), show(r.get("sender_function")),
            show(r.get("receiver_function")), show(r.get("blocked_decision")),
            show(r.get("owner_owes")), show(r.get("asked_on")), days,
            show(r.get("late_path")), ", ".join(miss) if miss else "none"))
    open_ids = {r["id"] for r in rows if d(r.get("received_on")) in (None, "bad")}
    order, cycle = dependency_order(rows, open_ids)
    print("\nRecords: %d. Fields missing across the log: %d." % (len(rows), missing_total))
    print("Open handoffs in dependency order (each after the open items it waits on): " + (", ".join(order) or "none"))
    unknown = sorted({j for r in rows for j in deps(r) if j not in {x["id"] for x in rows}})
    if unknown:
        print("depends_on names ids not in the log: %s %s" % (", ".join(unknown), GAP))
    if cycle:
        print("Circular wait between: %s. The person decides which goes first." % ", ".join(cycle))


def cmd_score(rows, start, end):
    print("# Handoff score, period %s to %s\n" % (start, end))
    print("Rule applied (the person's, as confirmed): a handoff is received when received_on is on or before the period end and received_by matches receiver_named. A message sent is not a receipt. Rows due in the period, and rows due earlier still open at its start, are scored; none is dropped.\n")
    scored, excluded = [], []
    for r in rows:
        due, got = d(r.get("due_on")), d(r.get("received_on"))
        in_period = due not in (None, "bad") and start <= due <= end
        carried = due not in (None, "bad") and due < start and (got in (None, "bad") or got >= start)
        if in_period or carried or due in (None, "bad"):
            s, why = status(r, start, end)
            scored.append((r, s, why, "carried in" if carried else ""))
        else:
            excluded.append(r["id"])
    counts = {}
    for _, s, _, _ in scored:
        counts[s] = counts.get(s, 0) + 1
    print("| id | Work product | Category | CTQ | Status | Fact | Note |")
    print("|---|---|---|---|---|---|---|")
    for r, s, why, note in scored:
        print("| %s | %s | %s | %s | %s | %s | %s |" % (r["id"], show(r.get("work_product")),
              show(r.get("category")), show(r.get("ctq")), s, why, note))
    print("\nScored: %d (%s). Outside the period: %d (%s)." % (
        len(scored), ", ".join("%s %d" % (k, v) for k, v in sorted(counts.items())),
        len(excluded), ", ".join(excluded) or "none"))
    asks = [(r["id"], why) for r, s, why, _ in scored if s == "not measurable"]
    if asks:
        print("\nTo ask the person (not measurable until answered; nothing is filled in):")
        for i, why in asks:
            print("- %s: %s" % (i, why))
    measurable = sum(v for k, v in counts.items() if k != "not measurable")
    if measurable:
        print("\nReceived on time over measurable handoffs: %d of %d. Not measurable kept out of this denominator and listed above." % (counts.get("received", 0), measurable))
    print("\nBy the person's category (each category counted separately, never merged):")
    cats = {}
    for r, s, _, _ in scored:
        key = (r.get("category") or GAP, (r.get("ctq") or GAP))
        cats.setdefault(key, {}).setdefault(s, 0)
        cats[key][s] += 1
    for (cat, ctq), c in sorted(cats.items()):
        print("- %s (CTQ marked by the person: %s): %s" % (cat, ctq, ", ".join("%s %d" % kv for kv in sorted(c.items()))))


def cmd_repair(rows, as_of):
    print("# Handoffs not received as of %s\n" % as_of)
    print("Owners, blocked decisions and look-again dates are the person's; blanks print %s. Order follows dependency, not urgency.\n" % GAP)
    open_rows = {}
    for r in rows:
        got = d(r.get("received_on"))
        if got in (None, "bad") or got > as_of:
            open_rows[r["id"]] = r
    order, cycle = dependency_order(rows, set(open_rows))
    print("| Step | id | Work product | Owner owes | Blocked decision | Waits on (open) | Look again on |")
    print("|---|---|---|---|---|---|---|")
    for n, i in enumerate(order, 1):
        r = open_rows[i]
        waits = [j for j in deps(r) if j in open_rows]
        print("| %d | %s | %s | %s | %s | %s | %s |" % (n, i, show(r.get("work_product")),
              show(r.get("owner_owes")), show(r.get("blocked_decision")),
              ", ".join(waits) or "none", show(r.get("look_again_on"))))
    if cycle:
        print("\nCircular wait between: %s. The person decides which goes first." % ", ".join(cycle))
    unnamed = [i for i in order if not open_rows[i].get("receiver_named")]
    if unnamed:
        print("\nReceiver not named %s for: %s. Ask the person who receives each; until then the handoff is not measurable and cannot be shown as received." % (GAP, ", ".join(unnamed)))
    print("\nNot received: %d. A decision stays blocked until its work product is received by the named receiver; a meeting does not unblock it." % len(order))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check"); c.add_argument("file"); c.add_argument("--as-of", required=True)
    s = sub.add_parser("score"); s.add_argument("file"); s.add_argument("--from", dest="start", required=True); s.add_argument("--to", dest="end", required=True)
    r = sub.add_parser("repair"); r.add_argument("file"); r.add_argument("--as-of", required=True)
    a = p.parse_args()
    rows = load(a.file)
    if a.cmd == "check":
        cmd_check(rows, date.fromisoformat(a.as_of))
    elif a.cmd == "score":
        cmd_score(rows, date.fromisoformat(a.start), date.fromisoformat(a.end))
    else:
        cmd_repair(rows, date.fromisoformat(a.as_of))


if __name__ == "__main__":
    main()
