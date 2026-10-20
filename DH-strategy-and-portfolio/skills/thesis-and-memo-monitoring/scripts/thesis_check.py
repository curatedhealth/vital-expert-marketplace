#!/usr/bin/env python3
"""Thesis check for thesis-and-memo-monitoring.

Reads the person's assumption register (CSV) and saved VITAL Digital Health Library
outputs, and prints per assumption: the value at the memo, the value now (with the
file and retrieval date), whether the person's own trigger rule is met, and flags.

    python3 thesis_check.py --register REGISTER.csv --as-of 2026-10-20 \
        [--deltas DELTAS.json] [--funding FUNDING.json] [--maturity MATURITY.json] \
        [--profile PROFILE.json]

Register columns: id, assumption, company, signal, value_at_memo, memo_date, trigger,
trigger_rule, rubric_at_memo, owner, reread_date.

Signals: deltas.change_count; funding.sec_count, funding.form_d_count,
funding.8k_count, funding.latest_filing_date; maturity.score, maturity.component.<name>;
profile.authorization_count, profile.latest_decision_date; none (no public signal).

Trigger rules (the person's, in machine form): ">N", ">=N", "<N", "<=N", "changes",
"after:YYYY-MM-DD", or blank (trigger not given). The script never sets a rule.

Flags (facts, never verdicts):
  T1 owner not named
  T2 reread date not given
  T3 not measurable from the public record (signal none)
  T4 evidence maturity compared without a stated rubric at the memo, or rubrics differ
  T5 the library change log began after the memo date (no change recorded is not
     conclusive for the period before the log)
  T6 reread date is earlier than the read date

Company status: when a funding file is given, the script lists the latest 8-K,
Form 25 and Form 15 rows to open and prints "Company status [GAP]: not read".
It never infers status from a filing date (DL-135 to DL-168).

Word count for the short-mode cap (450): drops the "Calls made" block (up to the
record line, which still counts) and the Source, Source of now and Rows columns.

    python3 thesis_check.py --words ANSWER.md
"""
import argparse
import csv
import json
import re
import sys
from datetime import date

LOG_NOTE = "log began {first}; last sweep {sweep}"


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def full_date(s):
    if not s:
        return "not given"
    try:
        d = date.fromisoformat(str(s)[:10])
    except ValueError:
        return str(s)
    return "{} {} {}".format(d.day, d.strftime("%B"), d.year)


def norm(s):
    return " ".join(str(s or "").lower().replace(",", " ").replace(".", " ").split())


def read_deltas(path):
    d = load(path)
    r = d.get("response", d)
    comps = {norm(c["company"]): c for c in r.get("companies", [])}
    log = r.get("log", {})
    return {"file": path, "companies": comps, "first": log.get("first_entry_at"),
            "sweep": log.get("last_sweep_at"), "since": (d.get("call", {}).get("args") or d.get("call", {}).get("arguments") or {}).get("since")}


def read_funding(path):
    d = load(path)
    r = d.get("response", d)
    sec = r.get("sources", {}).get("sec_edgar", {})
    bt = sec.get("by_type") or {}
    company = (d.get("call", {}).get("arguments") or {}).get("company")
    # A missing by_type stays missing (None), never 0.
    return {"file": path, "company": company, "rows": sec.get("rows") or [], "by_type": bt,
            "funding.sec_count": sec.get("count"),
            "funding.form_d_count": (bt.get("D", 0) + bt.get("D/A", 0)) if bt else None,
            "funding.8k_count": (bt.get("8-K", 0) + bt.get("8-K/A", 0)) if bt else None,
            "funding.latest_filing_date": (sec.get("date_range") or [None, None])[1]}


STATUS_FORMS = ("8-K", "25", "25-NSE", "15-12G", "15-12B", "15-15D")


def print_status(f):
    print("## Company status")
    print()
    print("Company status `[GAP]`: not read ({}). The library stores no status field and no 8-K item number; "
          "open the filings below for Items 1.03, 2.01, 3.01 and 5.01 (DL-136 to DL-141) and check for a "
          "Form 25 or Form 15 (DL-142 to DL-149). Form 25 or Form 15 is not dissolution (DL-144, DL-149). "
          "Nothing is inferred from the date filings stopped.".format(f["company"] or "the company in the funding file"))
    print()
    rows = sorted([x for x in f["rows"] if x.get("type") in STATUS_FORMS], key=lambda x: x.get("date") or "", reverse=True)
    for x in rows[:4]:
        print("- {} of {}: accession {}; {}".format(x.get("type"), full_date(x.get("date")), x.get("reference") or "not stored",
                                                   x.get("source_url") or "URL not stored"))
    if not rows:
        print("- No 8-K, Form 25 or Form 15 row in the saved copy; open the company's EDGAR filing list.")
    if f["by_type"]:
        stored = [t for t in f["by_type"] if t in STATUS_FORMS[1:]]
        print("- Form 25 or Form 15 among the stored types: {}; whether the library loads them needs a live check.".format(
            ", ".join(stored) if stored else "not in the stored types"))
    print("- Automated EDGAR reads need a declared User-Agent contact (DL-153): ask which contact the person's "
          "organization uses; never their name or email unasked, never an invented one.")
    print()


DROP_COLUMNS = {"source", "source of now", "rows", "rows or file"}


def count_words(text, drop=DROP_COLUMNS):
    body = []
    _skip_calls = False  # the calls list sits before the record block; skip it, then count the record
    for ln in text.splitlines():
        head = ln.strip().lower().lstrip("#* ").rstrip("*: ")
        if _skip_calls:
            if re.search(r"Clears it|^\W*(#+\s*)?(\*\*)?(\d+\.\s*)?(\*\*)?Record\b", ln.strip()):
                _skip_calls = False
            else:
                continue
        if head.startswith("calls made"):
            _skip_calls = True
            continue
        body.append(ln)
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


def read_maturity(path):
    d = load(path)
    out = []
    for c in d.get("calls", [d]):
        comps = {}
        for x in c.get("components", []) if isinstance(c.get("components"), list) else []:
            comps[x["component"]] = x.get("points")
        out.append({"resolution": c.get("resolution", ""), "score": c.get("score"),
                    "rubric": c.get("rubric_version"), "components": comps,
                    "retrieved": c.get("retrieved_at")})
    return {"file": path, "rows": out}


def read_profile(path):
    d = load(path)
    if "response" in d:
        prods = d["response"].get("products", [])
        name = (d.get("call", {}).get("arguments") or {}).get("company")
        retrieved = d["response"].get("provenance", {}).get("retrieved_at")
    else:
        prods = d.get("identity", {}).get("products", [])
        name = d.get("identity", {}).get("resolved", "")
        retrieved = d.get("retrieved")
    dates = sorted(p.get("decision_date") for p in prods if p.get("decision_date"))
    return {"file": path, "company": name, "retrieved": retrieved,
            "profile.authorization_count": len(prods),
            "profile.latest_decision_date": dates[-1] if dates else None}


def value_now(row, src):
    sig = row["signal"].strip()
    comp = norm(row["company"])
    if sig == "none" or not sig:
        return None, "no public signal", []
    if sig.startswith("deltas."):
        dl = src.get("deltas")
        if not dl:
            return None, "deltas file not given", []
        hit = None
        for k, v in dl["companies"].items():
            if comp and (comp in k or k in comp):
                hit = v
        if hit is None:
            return None, "company not in deltas file", []
        note = "{}; since {}; {}".format(dl["file"], full_date(dl["since"]),
                                          LOG_NOTE.format(first=full_date(dl["first"]), sweep=full_date(dl["sweep"])))
        return hit.get("change_count"), note, [dl["first"]]
    if sig.startswith("funding."):
        f = src.get("funding")
        if not f or (comp and norm(f["company"]) and comp not in norm(f["company"]) and norm(f["company"]) not in comp):
            return None, "funding file not given for this company", []
        return f.get(sig), f["file"], []
    if sig.startswith("maturity."):
        m = src.get("maturity")
        if not m:
            return None, "maturity file not given", []
        hit = None
        for r in m["rows"]:
            if comp and comp in norm(r["resolution"]):
                hit = r
        if hit is None:
            return None, "company not in maturity file", []
        note = "{}; rubric {}; retrieved {}".format(m["file"], hit["rubric"] or "not stated", full_date(hit["retrieved"]))
        if sig == "maturity.score":
            return hit["score"], note, [("rubric", hit["rubric"])]
        name = sig.split(".", 2)[2]
        return hit["components"].get(name), note, [("rubric", hit["rubric"])]
    if sig.startswith("profile."):
        p = src.get("profile")
        if not p:
            return None, "profile file not given", []
        return p.get(sig), "{}; retrieved {}".format(p["file"], full_date(p["retrieved"])), []
    return None, "signal not recognized", []


def as_number(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def trigger_met(rule, memo_val, now_val):
    rule = (rule or "").strip()
    if not rule:
        return "trigger rule not given"
    if now_val is None:
        return "not measurable"
    if rule == "changes":
        return "met" if str(now_val) != str(memo_val).strip() else "not met"
    if rule.startswith("after:"):
        return "met" if str(now_val)[:10] > rule[6:] else "not met"
    for op in (">=", "<=", ">", "<"):
        if rule.startswith(op):
            n, x = as_number(now_val), as_number(rule[len(op):])
            if n is None or x is None:
                return "not comparable"
            ok = {">=": n >= x, "<=": n <= x, ">": n > x, "<": n < x}[op]
            return "met" if ok else "not met"
    return "rule not recognized"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--register")
    ap.add_argument("--as-of")
    ap.add_argument("--words", metavar="ANSWER.md")
    ap.add_argument("--deltas")
    ap.add_argument("--funding")
    ap.add_argument("--maturity")
    ap.add_argument("--profile")
    a = ap.parse_args()
    if a.words:
        n = count_words(open(a.words, encoding="utf-8").read())
        if n <= 450:
            print("{} words (cap 450): within the short-mode cap.".format(n))
        else:
            print("{} words (cap 450): over by {}. Cut in this order: context paragraphs, repeated row ids in prose, "
                  "secondary rules, rows not tied to the person's question; never cut a gap, a stop, the company "
                  "status line or the record line.".format(n, n - 450))
        return
    if not a.register or not a.as_of:
        sys.exit("--register and --as-of are required unless --words is given")
    asof = date.fromisoformat(a.as_of)
    src = {}
    if a.deltas:
        src["deltas"] = read_deltas(a.deltas)
    if a.funding:
        src["funding"] = read_funding(a.funding)
    if a.maturity:
        src["maturity"] = read_maturity(a.maturity)
    if a.profile:
        src["profile"] = read_profile(a.profile)

    with open(a.register, encoding="utf-8") as fh:
        lines = [ln for ln in fh if not ln.startswith("#")]
    rows = list(csv.DictReader(lines))

    print("# Thesis check, read {}".format(full_date(a.as_of)))
    print()
    print("Register: `{}`. Values now come from saved library files as named. Trigger rules are the person's; "
          "'met' means the person's rule is met on the data, not a recommendation.".format(a.register))
    print()
    print("| Id | Assumption | Signal | At memo | Now | Source of now | Trigger (your words) | Rule met | Owner | Reread | Flags |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    counts = {"met": 0, "not met": 0, "other": 0}
    for r in rows:
        flags = []
        now, note, extra = value_now(r, src)
        if r["signal"].strip() in ("none", ""):
            flags.append("T3")
        if not r.get("owner", "").strip():
            flags.append("T1")
        rd = r.get("reread_date", "").strip()
        if not rd:
            flags.append("T2")
        elif date.fromisoformat(rd) < asof:
            flags.append("T6")
        for e in extra:
            if isinstance(e, tuple) and e[0] == "rubric":
                if not r.get("rubric_at_memo", "").strip() or r["rubric_at_memo"].strip() != (e[1] or ""):
                    flags.append("T4")
            elif isinstance(e, str) and r.get("memo_date") and e[:10] > r["memo_date"].strip():
                flags.append("T5")
        if "T3" in flags:
            met = "not measurable from the record"
        else:
            met = trigger_met(r.get("trigger_rule"), r.get("value_at_memo"), now)
        if "T4" in flags and met in ("met", "not met"):
            met = met + " (not comparable: T4)"
        counts["met" if met == "met" else ("not met" if met == "not met" else "other")] += 1
        print("| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} |".format(
            r["id"], r["assumption"], r["signal"] or "none", r.get("value_at_memo") or "not given",
            "not measurable" if now is None else now, note, r.get("trigger") or "not given", met,
            r.get("owner") or "owner not named", full_date(rd) if rd else "not given", ", ".join(flags) or "no flag"))
    print()
    print("Counts: rule met {met}; rule not met {notmet}; not measurable, not comparable or no rule {other}.".format(
        met=counts["met"], notmet=counts["not met"], other=counts["other"]))
    print()
    if "funding" in src:
        print_status(src["funding"])
    print("Flag key: T1 owner not named; T2 reread date not given; T3 not measurable from the public record; "
          "T4 rubric at memo not stated or different; T5 change log began after the memo date; "
          "T6 reread date earlier than the read date.")


if __name__ == "__main__":
    main()
