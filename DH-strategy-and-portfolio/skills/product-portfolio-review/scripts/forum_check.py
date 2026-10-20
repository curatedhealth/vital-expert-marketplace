#!/usr/bin/env python3
"""Forum review helpers for product-portfolio-review.

Every command reads the person's own records and rules. Nothing here judges a
person, decides, or sets a rule, threshold, owner or date.

  records   Check a forum decision log against the pass rule the person confirms
            (default, from the old method CF-12.01.03.3.2.1: a decision passes
            when it carries the rule, the rank, the decision and the person;
            a continue with no rule, or a stop with no record, fails; a decision
            that lives only in a slide fails). Also lists, as questions for the
            forum score, any lower-ranked item continued while a higher-ranked
            item was delayed or stopped, and the capacity the recorded continue
            items use.

              python3 forum_check.py records LOG.csv

  drift     Recompute each item's value from the scores in the log and the
            weights in the person's rule (EVIDEM weighted sum, value = 25 x sum
            of weight x 0-to-4 score), apply the person's decision rule, and mark
            each recorded decision "match" or "drift". Flags a recorded rank that
            differs from the recomputed rank, a rule dated after the forum, and
            continue items past the named capacity.

              python3 forum_check.py drift LOG.csv RULE.json

  benefits  Read a benefits plan (the person's register) and report, per
            benefit, the share of the planned change achieved
            ((actual - baseline) / (target - baseline)), with flags for missing
            register fields (owner, baseline, target, measure: the contents a
            benefits register lists, SP-104) and review dates not given. With
            --rule, applies the person's own threshold (a share between 0 and 1);
            without it, prints numbers only and no verdict.

              python3 forum_check.py benefits PLAN.csv [--rule 0.8] [--as-of 2026-10-20]

  words     Count a short-mode answer the way the cap counts it (body above the
            "Calls made" heading; Source and Rows columns left out), and check
            that the record line is last (no offer of a full version after it).

              python3 forum_check.py words ANSWER.md
"""
import argparse
import csv
import json
import re
from datetime import date

WORD_CAP = 450
CUT_ORDER = ("context paragraphs, repeated row ids in prose, secondary rules, "
             "rows not tied to the person's question (never a gap, a stop or the record line)")
SLIDE_WORDS = ("slide", "deck", "ppt")


def read_csv(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return [{k.strip(): (v or "").strip() for k, v in row.items()} for row in csv.DictReader(fh)]


def blank(v):
    return v is None or v == "" or v.lower() in ("none", "n/a", "not given")


# ---------- records ----------
def cmd_records(a):
    rows = read_csv(a.log)
    print("Pass rule applied (confirm it is yours): rule, rank, decision and decider recorded; "
          "a continue with no rule fails; a stop with no record fails; a decision only in a slide fails.\n")
    print("| Item | Decision | Rule | Rank | Decider | Date | Record | Result | Why |")
    print("|---|---|---|---|---|---|---|---|---|")
    n_pass = 0
    for r in rows:
        why = []
        dec = r.get("decision", "").lower()
        rec = r.get("record_location", "")
        if blank(r.get("rule_ref")):
            why.append("continue with no rule" if dec == "continue" else "no rule recorded")
        if blank(r.get("rank")):
            why.append("no rank")
        if blank(dec):
            why.append("no decision")
        if blank(r.get("decider")):
            why.append("no decider named")
        if blank(r.get("date")):
            why.append("date not given")
        if blank(rec):
            why.append("stop with no record" if dec == "stop" else "no record")
        elif any(w in rec.lower() for w in SLIDE_WORDS) and "minutes" not in rec.lower() and "record" not in rec.lower():
            why.append("lives only in a slide")
        res = "pass" if not why else "fail"
        n_pass += res == "pass"
        print("| {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            r.get("item"), r.get("decision") or "not given", r.get("rule_ref") or "none",
            r.get("rank") or "none", r.get("decider") or "not named", r.get("date") or "not given",
            rec or "none", res, "; ".join(why) or "all four present"))
    print("\n{} of {} decisions pass the rule as applied. Each decision is reported separately; no average.".format(n_pass, len(rows)))
    # Recorded rank against recorded decision: a lower-ranked item continued while a
    # higher-ranked item was delayed or stopped. A question for the forum score, not a fail.
    ranked = []
    for r in rows:
        try:
            ranked.append((int(float(r.get("rank"))), r.get("item"), (r.get("decision") or "").lower()))
        except (TypeError, ValueError):
            pass
    ranked.sort()
    pairs = []
    for hi in ranked:
        for lo in ranked:
            if hi[0] < lo[0] and hi[2] in ("delay", "stop") and lo[2] == "continue":
                pairs.append((hi, lo))
    if pairs:
        print("\nRank order and decision (as recorded):")
        for hi, lo in pairs:
            print("- {} (rank {}, {}) and {} (rank {}, continue): rank order and decision differ; reason not in the record. "
                  "A question for the forum score, not a pass or fail.".format(hi[1], hi[0], hi[2], lo[1], lo[0]))
    total = 0.0
    seen = False
    for r in rows:
        if (r.get("decision") or "").lower() == "continue" and not blank(r.get("capacity_use")):
            try:
                total += float(r["capacity_use"])
                seen = True
            except ValueError:
                pass
    if seen:
        print("\nRecorded continue items use {:g} in the log's capacity unit (compare with the named capacity in the forum score).".format(total))


# ---------- drift ----------
def cmd_drift(a):
    rows = read_csv(a.log)
    rule = json.load(open(a.rule, encoding="utf-8"))
    w = rule["weights"]
    dr = rule.get("decision_rule", {})
    if abs(sum(w.values()) - 1) > 1e-6:
        print("Flag: rule weights sum to {:.4f}, not 1.".format(sum(w.values())))
    vals, unscored = {}, []
    for r in rows:
        try:
            vals[r["item"]] = 25.0 * sum(w[c] * float(r["s_" + c]) for c in w)
        except (KeyError, ValueError):
            unscored.append(r["item"])
    order = sorted(vals, key=lambda k: -vals[k])
    implied, running, cap = {}, 0.0, dr.get("capacity")
    use = {r["item"]: (float(r["capacity_use"]) if not blank(r.get("capacity_use")) else None) for r in rows}
    for i, item in enumerate(order, 1):
        t = dr.get("type")
        if t == "capacity_in_rank_order":
            u = use.get(item)
            if u is None:
                implied[item] = "not measurable (capacity use not given)"
            elif running + u <= cap:
                running += u
                implied[item] = "continue"
            else:
                implied[item] = "not continue (rule does not say stop or delay)"
        elif t == "top_n":
            implied[item] = "continue" if i <= dr["n"] else "not continue (rule does not say stop or delay)"
        elif t == "min_value":
            implied[item] = "continue" if vals[item] >= dr["value"] else "not continue (rule does not say stop or delay)"
        else:
            implied[item] = "rule not machine-readable: read by hand"
    if rule.get("rule_date") and rows and rows[0].get("date"):
        if rule["rule_date"] > rows[0]["date"]:
            print("Flag: the rule is dated {} , after the forum of {}: a rule written after the decision cannot be used to score it (old method: do not rescore the rule to match what was decided).".format(rule["rule_date"], rows[0]["date"]))
    print("Rule: {} ; decision rule: {}\n".format(rule.get("rule_ref", "not named"), json.dumps(dr)))
    print("| Item | Recomputed value | Recomputed rank | Recorded rank | Implied by the rule | Recorded decision | Result |")
    print("|---|---|---|---|---|---|---|")
    cont_total, first_over = 0.0, None
    for i, item in enumerate(order, 1):
        r = next(x for x in rows if x["item"] == item)
        dec = r.get("decision", "").lower() or "not given"
        imp = implied[item]
        if imp.startswith("not measurable") or imp.startswith("rule not"):
            res = "not measurable"
        elif dec == "continue" and imp == "continue":
            res = "match"
        elif dec != "continue" and imp.startswith("not continue"):
            res = "match"
        elif dec == "continue":
            res = "drift: continue beyond the rule"
        else:
            res = "drift: held back against the rule"
        rr = r.get("rank") or "none"
        if rr not in ("none", str(i)):
            res += "; recorded rank differs from recomputed rank"
        if dec == "continue" and use.get(item) is not None:
            cont_total += use[item]
            if cap is not None and cont_total > cap and first_over is None:
                first_over = item
        print("| {} | {:.2f} | {} | {} | {} | {} | {} |".format(item, vals[item], i, rr, imp, dec, res))
    for item in unscored:
        print("| {} | not computed (scores missing) | | | | | not measurable |".format(item))
    if cap is not None:
        print("\nNamed capacity {} ; recorded continue items use {}.".format(cap, cont_total))
        if first_over:
            print("Recorded continue item that goes past the named capacity: {}.".format(first_over))
    print("\nMatch or drift is read against the person's rule as written; whether the rule or the decision is corrected is the person's call.")


# ---------- benefits ----------
def num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def cmd_benefits(a):
    rows = read_csv(a.plan)
    as_of = a.as_of
    print("| Benefit | Item | Owner | Baseline | Target | Actual (date) | Share of planned change | Your rule | Flags |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        flags = []
        for f in ("owner", "baseline", "target", "measure"):
            if blank(r.get(f)):
                flags.append(f + " not given")
        b, t, act = num(r.get("baseline")), num(r.get("target")), num(r.get("actual"))
        share, verdict = None, "no rule given"
        if act is None:
            flags.append("actual not measured")
        if None not in (b, t, act):
            if t == b:
                flags.append("target equals baseline")
            else:
                share = (act - b) / (t - b)
        if a.rule is not None:
            verdict = "not measurable" if share is None else ("met" if share >= a.rule else "not met")
        rd = r.get("review_date", "")
        if blank(rd):
            flags.append("review date not given")
        elif as_of and rd < as_of:
            flags.append("review date {} is before the read date {}".format(rd, as_of))
        print("| {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            r.get("benefit"), r.get("item"), r.get("owner") or "owner not named", r.get("baseline") or "not given",
            r.get("target") or "not given",
            "{} ({})".format(r.get("actual") or "not measured", r.get("actual_date") or "date not given"),
            "{:.0%}".format(share) if share is not None else "not measurable", verdict, "; ".join(flags) or "none"))
    print("\nBaselines, targets, owners and the rule are the person's. A share is arithmetic, not a judgment of the program or its people.")


# ---------- words ----------
def count_words(text):
    body = []
    for ln in text.splitlines():
        if re.match(r"^\s*#*\s*\**Calls made", ln, re.I):
            break
        body.append(ln)
    out, drop = [], None
    for ln in body:
        if ln.strip().startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if drop is None:
                drop = {i for i, c in enumerate(cells) if c.lower() in ("source", "rows", "row", "sources")}
            out.append(" ".join(c for i, c in enumerate(cells) if i not in drop))
        else:
            drop = None
            out.append(ln)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'.,%/()\-]*", "\n".join(out)))


def record_order(text):
    """The record line must be last in the answer body: no offer line after the
    "Record" block starts, and "Clears it" on the last body line."""
    body = []
    for ln in text.splitlines():
        if re.match(r"^\s*#*\s*\**Calls made", ln, re.I):
            break
        if ln.strip():
            body.append(ln.strip())
    rec = [i for i, ln in enumerate(body) if re.match(r"^(\d+\.\s*)?\**Record", ln) or "Clears it" in ln]
    if not rec:
        return "Flag: no record line found."
    if any(re.search(r"full version", ln, re.I) for ln in body[rec[0]:]):
        return "Flag: the offer of a full version sits after the record block; move it above \"Record\"."
    if "Clears it" not in body[-1] and "uncleared draft" not in body[-1]:
        return "Flag: the record line is not the last line of the answer body."
    return "Record line is last."


def cmd_words(a):
    text = open(a.answer, encoding="utf-8").read()
    n = count_words(text)
    if n <= WORD_CAP:
        print("{} words (cap {}): within the short-mode cap.".format(n, WORD_CAP))
    else:
        print("{} words (cap {}): over by {}. Cut in this order: {}.".format(n, WORD_CAP, n - WORD_CAP, CUT_ORDER))
    print(record_order(text))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("records"); s.add_argument("log"); s.set_defaults(fn=cmd_records)
    s = sub.add_parser("drift"); s.add_argument("log"); s.add_argument("rule"); s.set_defaults(fn=cmd_drift)
    s = sub.add_parser("benefits"); s.add_argument("plan"); s.add_argument("--rule", type=float)
    s.add_argument("--as-of", dest="as_of"); s.set_defaults(fn=cmd_benefits)
    s = sub.add_parser("words"); s.add_argument("answer"); s.set_defaults(fn=cmd_words)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
