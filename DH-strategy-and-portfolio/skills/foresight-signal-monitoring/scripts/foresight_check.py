#!/usr/bin/env python3
"""Foresight log check for foresight-signal-monitoring (dh-strategy-and-portfolio).

Reads the person's foresight log (signals, foresight calls and technology selections) and
prints, per row, the quality and resolution flags, then counts by the person's own outcomes
and applies the person's pass rule if one is given. It never resolves a call itself: the
outcome column is the person's (or a proposed outcome the person confirms).

Usage:
  python3 foresight_check.py --log LOG.csv --as-of YYYY-MM-DD [--pass-rule "hit_share >= 0.6"]
                             [--log-start 2026-10-12] [--owners "call=M. Keller;selection=J. Osei"]
                             [--if-confirmed "F5=miss;F7=miss"]
  python3 foresight_check.py --words ANSWER.md

  --owners       the owners the person names by kind of row, in their words. A row whose log
                 owner differs gets O4 and both names are printed; the checker never chooses.
  --if-confirmed proposed outcomes awaiting the person's confirmation. The recorded counts stay
                 as they are; a second count and pass-rule result show what would change if the
                 person confirmed them (computed, never estimated).
  --words        the whole answer except the "Calls made" block (which sits before the
                 record line), leaving out the Source, Rows, Retrieved and Evidence columns.

LOG.csv columns (header row; empty cells allowed):
  id, kind (signal | call | selection), statement, made_on, source_type
  (register | filing | publication | registry | regulator | legal_act | press | vendor | other),
  source_url, event_date, horizon_date, resolution_rule, outcome (hit | miss | open | void),
  resolved_on, evidence_url, evidence_type (record | change_log | person_data), owner, reread

Flags:
  Q1 source is press, vendor, other or blank: a lead, not a signal
  Q2 event date missing (signal) or made_on missing (call, selection)
  Q3 source URL missing
  R1 resolution rule not given (call, selection)
  R2 horizon date passed and no outcome recorded: due for resolution by your rule
  R3 outcome recorded without evidence URL
  R4 resolved before it was made (data error)
  R5 outcome rests on the library change log for a period before the log began
  O1 owner not named   O2 reread date not given   O3 reread date earlier than the as-of date
  O4 the log's owner differs from the owner the person names for that kind of row (--owners)
Pass-rule metrics: hits, misses, open, void, resolved, hit_share, leads, flagged_rows, rows.
"""
import argparse
import csv
import re
import sys

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]
RECORD_TYPES = {"register", "filing", "publication", "registry", "regulator", "legal_act"}
DROP_COLUMNS = {"source", "rows", "retrieved", "source url", "evidence"}


def full_date(s):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s or "")
    if not m:
        return s or "not given"
    y, mo, d = m.groups()
    return "{} {} {}".format(int(d), MONTHS[int(mo) - 1], y)


def is_date(s):
    return bool(re.match(r"\d{4}-\d{2}-\d{2}$", (s or "").strip()))


def parse_pairs(s):
    out = {}
    for part in (s or "").split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip().lower() if k.strip().lower() in ("signal", "call", "selection") else k.strip()] = v.strip()
    return out


def flags_for(r, as_of, log_start, owners=None):
    f = []
    kind = (r.get("kind") or "").strip().lower()
    st = (r.get("source_type") or "").strip().lower()
    if kind == "signal":
        if st not in RECORD_TYPES:
            f.append("Q1")
        if not is_date(r.get("event_date")):
            f.append("Q2")
    else:
        if not is_date(r.get("made_on")):
            f.append("Q2")
        if not (r.get("resolution_rule") or "").strip():
            f.append("R1")
    if not (r.get("source_url") or "").strip():
        f.append("Q3")
    outcome = (r.get("outcome") or "").strip().lower()
    hz = r.get("horizon_date")
    if kind != "signal" and is_date(hz) and hz < as_of and outcome in ("", "open"):
        f.append("R2")
    if outcome in ("hit", "miss") and not (r.get("evidence_url") or "").strip():
        f.append("R3")
    if is_date(r.get("resolved_on")) and is_date(r.get("made_on")) and r["resolved_on"] < r["made_on"]:
        f.append("R4")
    if ((r.get("evidence_type") or "").strip().lower() == "change_log" and is_date(r.get("made_on"))
            and r["made_on"] < log_start):
        f.append("R5")
    if not (r.get("owner") or "").strip():
        f.append("O1")
    elif owners and kind in owners and owners[kind] != (r.get("owner") or "").strip():
        f.append("O4")
    if not is_date(r.get("reread")):
        f.append("O2")
    elif r["reread"] < as_of:
        f.append("O3")
    return f


def safe_eval(rule, metrics):
    if not re.fullmatch(r"[\w\s\.<>=!()andornot+\-*/]+", rule):
        raise ValueError("pass rule uses characters this checker does not read")
    names = set(re.findall(r"[A-Za-z_]+", rule)) - {"and", "or", "not"}
    unknown = names - set(metrics)
    if unknown:
        raise ValueError("pass rule names unknown metrics: {}".format(", ".join(sorted(unknown))))
    return bool(eval(rule, {"__builtins__": {}}, dict(metrics)))


def tally(rows, override=None):
    counts = {"hits": 0, "misses": 0, "open": 0, "void": 0}
    for r in rows:
        kind = (r.get("kind") or "").strip().lower()
        if kind not in ("call", "selection"):
            continue
        outcome = (r.get("outcome") or "").strip().lower()
        if override and r.get("id") in override:
            outcome = override[r.get("id")].lower()
        key = {"hit": "hits", "miss": "misses", "void": "void"}.get(outcome, "open")
        counts[key] += 1
    counts["resolved"] = counts["hits"] + counts["misses"]
    counts["hit_share"] = (counts["hits"] / counts["resolved"]) if counts["resolved"] else 0.0
    return counts


def check(log, as_of, pass_rule, log_start, owners=None, if_confirmed=None):
    with open(log, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    print("Read as of {}; {} rows from {}.\n".format(full_date(as_of), len(rows), log))
    print("| Id | Kind | Statement | Made or dated | Horizon | Outcome (yours) | Owner | Reread | Flags |")
    print("|---|---|---|---|---|---|---|---|---|")
    counts = {"hits": 0, "misses": 0, "open": 0, "void": 0, "leads": 0, "flagged_rows": 0, "rows": len(rows)}
    by_kind = {}
    for r in rows:
        f = flags_for(r, as_of, log_start, owners)
        kind = (r.get("kind") or "").strip().lower()
        outcome = (r.get("outcome") or "").strip().lower()
        if kind == "signal" and "Q1" in f:
            counts["leads"] += 1
        if f:
            counts["flagged_rows"] += 1
        if kind in ("call", "selection"):
            k = by_kind.setdefault(kind, {"hit": 0, "miss": 0, "open": 0, "void": 0, "not recorded": 0})
            key = outcome if outcome in ("hit", "miss", "open", "void") else "not recorded"
            k[key] += 1
            if outcome == "hit":
                counts["hits"] += 1
            elif outcome == "miss":
                counts["misses"] += 1
            elif outcome == "void":
                counts["void"] += 1
            else:
                counts["open"] += 1
        dated = r.get("event_date") if kind == "signal" else r.get("made_on")
        print("| {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            r.get("id"), kind or "not given", (r.get("statement") or "")[:90], full_date(dated),
            full_date(r.get("horizon_date")) if r.get("horizon_date") else "",
            outcome or "not recorded", (r.get("owner") or "").strip() or "owner not named",
            full_date(r.get("reread")) if r.get("reread") else "not given", " ".join(f) or "none"))
    resolved = counts["hits"] + counts["misses"]
    counts["resolved"] = resolved
    counts["hit_share"] = (counts["hits"] / resolved) if resolved else 0.0
    print("\nCounts by your recorded outcomes (open includes 'not recorded'):\n")
    print("| Kind | Hit | Miss | Open | Void | Not recorded |")
    print("|---|---|---|---|---|---|")
    for kind, k in sorted(by_kind.items()):
        print("| {} | {} | {} | {} | {} | {} |".format(kind, k["hit"], k["miss"], k["open"], k["void"], k["not recorded"]))
    if resolved:
        print("\nHit share: {} of {} resolved calls and selections ({:.0%}); open and void rows are outside "
              "the denominator. This is your log counted by your outcomes, not an accuracy benchmark; no "
              "source sets one.".format(counts["hits"], resolved, counts["hit_share"]))
    else:
        print("\nNo resolved calls or selections: no hit share can be computed.")
    print("Leads logged as signals (Q1): {}. Rows with any flag: {} of {}.".format(
        counts["leads"], counts["flagged_rows"], counts["rows"]))
    no_owner = [r.get("id") for r in rows if not (r.get("owner") or "").strip()]
    print("Rows with owner not named in the log (O1), misses or not: {}. Ask who owns each.".format(
        ", ".join(no_owner) if no_owner else "none"))
    if owners:
        for r in rows:
            kind = (r.get("kind") or "").strip().lower()
            lo = (r.get("owner") or "").strip()
            if lo and kind in owners and owners[kind] != lo:
                print("O4 {}: the log names {}; you named {} for {}s. Both shown; ask which applies.".format(
                    r.get("id"), lo, owners[kind], kind))
    if pass_rule:
        try:
            met = safe_eval(pass_rule, counts)
            print("\nYour pass rule '{}': {} on this log.".format(pass_rule, "met" if met else "not met"))
        except ValueError as e:
            print("\nYour pass rule '{}' could not be applied: {}. Ask the person to restate it.".format(pass_rule, e))
    else:
        print("\nPass rule not given: nothing is marked passed or failed.")
    if if_confirmed:
        alt = tally(rows, if_confirmed)
        alt["leads"], alt["flagged_rows"], alt["rows"] = counts["leads"], counts["flagged_rows"], counts["rows"]
        print("\nIf you confirm the proposed outcomes ({}): hit share {} of {} ({:.0%}).".format(
            "; ".join("{} {}".format(k, v) for k, v in if_confirmed.items()), alt["hits"], alt["resolved"],
            alt["hit_share"]) if alt["resolved"] else "\nIf you confirm the proposed outcomes: no resolved rows.")
        if pass_rule:
            try:
                print("Your pass rule would then be {}. Not applied until you confirm.".format(
                    "met" if safe_eval(pass_rule, alt) else "not met"))
            except ValueError as e:
                print("Pass rule could not be applied to the confirmed set: {}.".format(e))
    print("\nFlag key: Q1 lead not signal; Q2 date missing; Q3 source URL missing; R1 resolution rule not given; "
          "R2 horizon passed, outcome not recorded; R3 outcome without evidence; R4 resolved before made; "
          "R5 rests on the change log before it began ({}); O1 owner not named; O2 reread not given; "
          "O3 reread earlier than the as-of date; O4 log owner differs from the owner you named for that kind.".format(full_date(log_start)))


def strip_calls(text):
    """Drop the "Calls made" block wherever it sits (it comes before the record line):
    its lead-in line, the rest of that paragraph and any bullet or indented lines under it.
    Counting resumes at the first ordinary line after a blank line."""
    body, skipping, prev_blank = [], False, False
    for ln in text.splitlines():
        st = ln.strip()
        head = st.lower().lstrip("#*0123456789. ").rstrip("*: ")
        if head.startswith("calls made"):
            skipping, prev_blank = True, False
            continue
        if skipping:
            if not st:
                prev_blank = True
                continue
            is_list = st.startswith(("-", "*", "+")) or ln[:1] in (" ", "\t")
            if prev_blank and not is_list:
                skipping = False
            else:
                prev_blank = False
                continue
        body.append(ln)
    return body


def count_words(text, drop=DROP_COLUMNS):
    body = strip_calls(text)
    out, drop_idx = [], None
    for ln in body:
        st = ln.strip()
        if st.startswith("|"):
            cells = [c.strip() for c in st.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if drop_idx is None:
                drop_idx = {i for i, c in enumerate(cells) if c.lower().strip("* ") in drop}
            out.append(" ".join(c for i, c in enumerate(cells) if i not in drop_idx))
        else:
            drop_idx = None
            out.append(ln)
    return len([t for t in re.findall(r"\S+", " ".join(out)) if re.search(r"[A-Za-z0-9]", t)])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--log")
    ap.add_argument("--as-of")
    ap.add_argument("--pass-rule")
    ap.add_argument("--log-start", default="2026-10-12")
    ap.add_argument("--words", metavar="ANSWER.md")
    ap.add_argument("--owners")
    ap.add_argument("--if-confirmed")
    a = ap.parse_args()
    if a.words:
        n = count_words(open(a.words, encoding="utf-8").read())
        if n <= 450:
            print("{} words (cap 450): within the short-mode cap.".format(n))
        else:
            print("{} words (cap 450): over by {}. Cut in this order: context paragraphs, repeated row ids in "
                  "prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the "
                  "company status line or the record line.".format(n, n - 450))
        return 0
    if not (a.log and a.as_of):
        sys.exit("--log and --as-of are required unless --words is given")
    if not is_date(a.as_of):
        sys.exit("--as-of must be YYYY-MM-DD")
    check(a.log, a.as_of, a.pass_rule, a.log_start, parse_pairs(a.owners), parse_pairs(a.if_confirmed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
