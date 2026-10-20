#!/usr/bin/env python3
"""Helpers for pipeline-and-market-monitoring.

deltas DELTAS.json
    Render a saved diligence-dh.get_deltas response (top level, or nested under
    "response") as a change table, with the log caveat: first entry, last sweep and the
    three limits as the library states them. Warns when the call's "since" date is
    earlier than the log's first entry. Prints any keys found on a change row, because
    no saved output yet shows a non-empty change (needs a live check).

screen-diff EARLIER.json LATER.json
    Compare two saved screen_market blocks (direct, or inside a screen_commercial_peers
    response, or nested under "response"). States whether the call arguments match; if
    not, it still lists differences but says no change can be inferred. Reports
    companies added or not returned (with total_matches and limit) and per-company
    changes in authorizations, studies, safety records, products and evidence maturity.

rules [--since YYYY-MM-DD] [--signals PATH]
    Print the rows of the dated rule and register change table in
    references/monitoring-signals.md (section 3) dated after --since.

mi-check MAP.csv --as-of YYYY-MM-DD [--max-age-days N] [--lanes "Buyers,Payers,Peers,Rules"] [--jurisdictions "US,DE"] [--readable-source]
    Check an ecosystem map (one row per entry; columns lane, jurisdiction, entry,
    source, date, gap) against the person's pass rule: source present, date present and,
    only if the person set --max-age-days, not older than that on --as-of; every lane and
    jurisdiction the person named has at least one non-gap entry. Prints pass, fail or
    not measurable per entry and element, and the coverage per lane. Sets no default
    age, lane list or blocking element: those are the person's. With
    --readable-source (a proposed element, only if the person confirms it) an entry
    whose source is only a row id or a library tool name fails "readable source".
    Always prints notes that are not fails: the readable source for each row id
    (name and URL from the research files in references/), whole-directory figures
    (DE33, DE34), the current FDA listing holder and filed status for peers covered by
    references/named-company-status.md, and a rules lane with no device or DiGA rule.

wordcount ANSWER.md [--limit 450]
    Count the words of a drafted short-mode answer the way the cap counts them: skips
    the calls list (the record line after it still counts) and leaves out table columns headed Source or Rows. Prints the
    count and, if over, the cut order.

Standard library only.
"""
import argparse
import json
import os
import re
import sys
from datetime import date

MONTHS = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July",
                                       "August", "September", "October", "November", "December"], 1)}


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def call_args(d):
    c = d.get("call") or {}
    return c.get("arguments") or c.get("args") or {}


def cmd_deltas(a):
    d = load(a.file)
    args = call_args(d)
    body = d.get("response", d)
    log = body.get("log", {})
    since = args.get("since", "not given")
    tool = (d.get("call") or {}).get("tool", "get_deltas")
    print(f"Call: {tool} {json.dumps(args)}; retrieved {d.get('retrieved') or d.get('_note') or 'not stated'}")
    print()
    print("| Company | Result | Changes |")
    print("|---|---|---|")
    for c in body.get("companies", []):
        ch = c.get("changes")
        if isinstance(ch, list):
            cells = []
            for e in ch:
                cells.append("; ".join(f"{k}: {v}" for k, v in e.items()))
            print(f"| {c.get('company')} | {len(ch)} change(s) | {' / '.join(cells)} |")
        else:
            print(f"| {c.get('company')} | {ch} | count {c.get('change_count', 'not given')} |")
    print()
    if not log:
        print("Log block missing: 'no change' cannot be read without it (use diligence-dh.get_deltas, not commercial-dh.get_deltas).")
        return
    first = (log.get("first_entry_at") or "")[:10]
    print(f"Log: first entry {first}; last entry {(log.get('last_entry_at') or '')[:10]}; last sweep {(log.get('last_sweep_at') or '')[:10]}.")
    for lim in log.get("limits", []):
        print(f"- Limit (as stated): {lim}")
    if since != "not given" and first and since < first:
        print(f"Warning: since {since} is earlier than the log's first entry {first}; changes dated before the log began may be missing.")
        print(f"Do not report 'no change' for {since} to {first}: offer the store's dated filings (diligence-dh.get_funding_signals) and authorization decision dates (diligence-dh.build_company_profile) for that window.")
    print("'No change recorded' is a statement about the library's log, not about the company. It says nothing about company status: read status from primary filings or write 'Status: [GAP]: not read'.")


def find_screen(d):
    if "response" in d and isinstance(d["response"], dict):
        inner = d["response"]
        return inner.get("screen_market", inner)
    return d.get("screen_market", d)


def rows_by_company(block):
    out = {}
    for r in block.get("results", []):
        sc = r.get("evidence_maturity_score")
        if sc is None and isinstance(r.get("evidence_maturity"), (dict, int)):
            sc = r["evidence_maturity"].get("score") if isinstance(r["evidence_maturity"], dict) else r["evidence_maturity"]
        out[r.get("company")] = {
            "authorizations": r.get("authorizations"),
            "studies": r.get("studies"),
            "safety_events": r.get("safety_events"),
            "products": tuple(r["products"]) if r.get("products") else None,
            "evidence_maturity": sc,
        }
    return out


def cmd_screen_diff(a):
    e, l = load(a.earlier), load(a.later)
    ea, la = call_args(e), call_args(l)
    same = ea == la
    eb, lb = find_screen(e), find_screen(l)
    print(f"Earlier arguments: {json.dumps(ea)}; later arguments: {json.dumps(la)}")
    print(f"Same arguments: {'yes' if same else 'no'}")
    print(f"total_matches earlier {eb.get('total_matches', 'not given')}, later {lb.get('total_matches', 'not given')}; shown earlier {len(eb.get('results', []))}, later {len(lb.get('results', []))}")
    if not same:
        print("Runs not comparable: arguments differ. Differences below are listed for reference only; no change can be inferred.")
    er, lr = rows_by_company(eb), rows_by_company(lb)
    added = [c for c in lr if c not in er]
    gone = [c for c in er if c not in lr]
    print()
    print("| Company | Change | Earlier | Later |")
    print("|---|---|---|---|")
    for c in added:
        print(f"| {c} | added in later run | not returned | returned |")
    for c in gone:
        print(f"| {c} | not returned in later run (check total_matches and limit) | returned | not returned |")
    n = 0
    for c in er:
        if c in lr:
            for k in er[c]:
                ev, lv = er[c][k], lr[c][k]
                if ev is None or lv is None:
                    continue
                if ev != lv:
                    n += 1
                    fmt = lambda v: "; ".join(v) if isinstance(v, tuple) else v
                    print(f"| {c} | {k} | {fmt(ev)} | {fmt(lv)} |")
    if not added and not gone and n == 0:
        print("| (none) | no difference in the fields both runs carry | | |")
    print()
    print("Fields missing from either saved run are not compared. The order is the library's sort; a position change is not a record change.")


def parse_date(s):
    m = re.match(r"\s*(\d{1,2}) ([A-Z][a-z]+) (\d{4})", s)
    if not m or m.group(2) not in MONTHS:
        return None
    return date(int(m.group(3)), MONTHS[m.group(2)], int(m.group(1)))


def cmd_rules(a):
    path = a.signals or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references", "monitoring-signals.md")
    text = open(path, encoding="utf-8").read()
    sec = text.split("## 3.", 1)[1].split("\n## ", 1)[0]
    lines = [ln for ln in sec.splitlines() if ln.startswith("| ") and not ln.startswith("| Date") and not ln.startswith("|---")]
    since = date.fromisoformat(a.since) if a.since else None
    print(f"Rule and register changes dated after {a.since or 'any date'} (from {os.path.relpath(path)}):")
    print("| Date | Change | Instrument | Rows | Status |")
    print("|---|---|---|---|---|")
    for ln in lines:
        d = parse_date(ln.split("|")[1])
        if since is None or (d and d > since):
            print(ln)
    print("For the owner the person names for legal questions; not applied to any deal here.")


CUT_ORDER = ("context paragraphs, repeated row ids in prose, secondary rules, rows not tied to "
             "the person's question. Never cut a gap, a stop or the record line.")


def answer_words(text):
    """Count words the way the 450-word cap counts them: skip the calls list (the record line after it still counts),
    drop table columns whose header names a source (Source, Rows), and skip pure
    punctuation tokens and table separator rows."""
    words = 0
    drop = set()
    in_table = False
    _skip_calls = False  # the calls list sits before the record block; skip it, then count the record
    for line in text.splitlines():
        s = line.strip()
        if _skip_calls:
            if re.search(r"Clears it|^\W*(#+\s*)?(\*\*)?(\d+\.\s*)?(\*\*)?Record\b", s.strip()):
                _skip_calls = False
            else:
                continue
        if re.match(r"^(#+\s*)?(\*\*)?(\d+\.\s*)?(\*\*)?calls made", s, re.I):
            _skip_calls = True
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not in_table:
                in_table = True
                drop = {i for i, c in enumerate(cells) if re.search(r"source|^rows?$", c, re.I)}
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            cells = [c for i, c in enumerate(cells) if i not in drop]
            s = " ".join(cells)
        else:
            in_table = False
            drop = set()
        words += sum(1 for tok in s.split() if re.search(r"[A-Za-z0-9]", tok))
    return words


def cmd_wordcount(a):
    with open(a.file, encoding="utf-8") as f:
        n = answer_words(f.read())
    print(f"Words (without the calls list and table source columns): {n} of {a.limit} allowed.")
    if n > a.limit:
        print(f"Over by {n - a.limit}. Cut in this order until under: {CUT_ORDER}")
    else:
        print("Within the short-mode cap.")


ROW_RE = re.compile(r"\b((?:SP|DL)-\d{3}|DE\d{2}|US\d{1,2})\b")


def research_urls():
    """Map row ids to (topic, first URL) from the research files in references/."""
    out = {}
    ref = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "references")
    for name in ("strategy-and-portfolio-research.md", "diligence-research.md", "hta-and-directory-research.md"):
        path = os.path.join(ref, name)
        if not os.path.exists(path):
            continue
        for line in open(path, encoding="utf-8"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4 and ROW_RE.fullmatch(cells[0] or ""):
                url = next((tok for c in cells[3:5] for tok in c.split() if tok.startswith("http")), "")
                out.setdefault(cells[0], (cells[1], url))
    return out


# Peers the research rows cover (references/named-company-status.md, read 20 October 2026).
PEER_NOTES = {
    "somryst": "Somryst: 510(k) applicant Pear Therapeutics, Inc. (SP-165); current FDA listing holder Nox Medical, listing created 18 December 2024 (SP-167)",
    "pear": "Pear Therapeutics: chapter 11 (Pear 8-K, 7 April 2023, SP-156 [WF]); Nasdaq delisting notice (Pear 8-K, 10 April 2023, SP-160 [WF]); Form 25-NSE 2 May 2023, not dissolution (SP-155, DL-144); reSET and reSET-O now listed by Harvest Bio (SP-169)",
    "akili": "Akili: merger completed, change in control to Virtual Therapeutics (Akili 8-K, 2 July 2024, SP-151 [WF]); Form 15, 12 July 2024, not dissolution (SP-154; DL-149 (inference)); EndeavorRx listed c/o Virtual Therapeutics (SP-168)",
    "big health": "Big Health: no SEC registrant found (SP-162 [WF]); active FDA registration; SleepioRx K233577 and DaylightRx K233872 listed (SP-163)",
    "aidoc": "Aidoc: no SEC registrant found (SP-162 [WF]); active FDA registration, 25 listings (SP-164)",
}
DEVICE_RULE = re.compile(r"MDR|510\(k\)|De Novo|FDA|DiGA|DiGAV|device|AI Act|SaMD", re.I)


def cmd_mi_check(a):
    import csv
    as_of = date.fromisoformat(a.as_of)
    rows = list(csv.DictReader(open(a.map, encoding="utf-8")))
    need = {"lane", "jurisdiction", "entry", "source", "date", "gap"}
    missing = need - set(rows[0].keys() if rows else [])
    if missing:
        sys.exit(f"Map is missing columns: {', '.join(sorted(missing))}")
    print(f"Market intelligence check on {len(rows)} entries, as of {a.as_of}.")
    print("Elements: source, date" + (f", age at most {a.max_age_days} days (your rule)" if a.max_age_days is not None else " (no maximum age given: age not checked)") + ".")
    print("| Lane | Jurisdiction | Entry | Source | Date | Age |")
    print("|---|---|---|---|---|---|")
    fails = 0
    for r in rows:
        if r["gap"].strip():
            print(f"| {r['lane']} | {r['jurisdiction']} | {r['entry'][:60]} | not measurable (gap: {r['gap']}) | not measurable | not measurable |")
            continue
        src = "pass" if r["source"].strip() else "FAIL: no source"
        if src == "pass" and a.readable_source:
            s0 = r["source"].strip()
            only_ids = not re.sub(r"(?:SP|DL)-\d{3}|DE\d{2}|US\d{1,2}|\bto\b|[,;\s]", "", s0)
            tool_only = bool(re.match(r"^[a-z\-]+\.[a-z_]+", s0))
            if only_ids or tool_only:
                src = "FAIL: not readable (row id or tool name only)"
        d = None
        try:
            d = date.fromisoformat(r["date"].strip())
        except ValueError:
            pass
        dt = "pass" if d else "FAIL: no date"
        if d is None:
            age = "not measurable"
        elif a.max_age_days is None:
            age = f"{(as_of - d).days} day(s) (no rule)"
        else:
            days = (as_of - d).days
            age = f"pass ({days} day(s))" if days <= a.max_age_days else f"FAIL ({days} day(s))"
        fails += sum(x.startswith("FAIL") for x in (src, dt, age))
        print(f"| {r['lane']} | {r['jurisdiction']} | {r['entry'][:60]} | {src} | {dt} | {age} |")
    print()
    lanes = [x.strip() for x in a.lanes.split(",")] if a.lanes else sorted({r["lane"] for r in rows})
    juris = [x.strip() for x in a.jurisdictions.split(",")] if a.jurisdictions else []
    print("Coverage (an entry counts only if it is not a gap):")
    for ln in lanes:
        sub = [r for r in rows if r["lane"].lower() == ln.lower()]
        filled = [r for r in sub if not r["gap"].strip()]
        line = f"- {ln}: {len(filled)} entries, {len(sub) - len(filled)} gaps"
        if juris:
            miss = [j for j in juris if not any(r["jurisdiction"].strip() in (j, "all") for r in filled)]
            if miss:
                line += f"; no entry for {', '.join(miss)}"
        if not filled:
            line += "; FAIL: lane has no record"
            fails += 1
        print(line)
    if not a.lanes:
        print("Lanes checked are those present in the map; give --lanes to check the lanes you said matter.")
    print(f"Failed elements: {fails}. Owner and recheck date for each are yours; none is set here.")
    urls = research_urls()
    notes = []
    for r in rows:
        if r["gap"].strip():
            continue
        ids = ROW_RE.findall(r["source"])
        if ids:
            named = "; ".join(f"{i} = {urls[i][0]} ({urls[i][1] or 'URL in the row'})" for i in dict.fromkeys(ids) if i in urls)
            if named:
                notes.append(f"Readable source for '{r['entry'][:40]}': {named}")
        if re.search(r"\bDE3[34]\b", r["source"]):
            notes.append(f"'{r['entry'][:40]}' rests on a whole-directory BfArM figure (DE33, DE34): not specific to your indication")
        if r["lane"].strip().lower() == "peers":
            low = r["entry"].lower()
            for key, note in PEER_NOTES.items():
                if key in low:
                    notes.append(f"Peer '{r['entry'][:40]}': holder as stored by the applicant. {note}")
    rules = [r for r in rows if r["lane"].strip().lower() == "rules" and not r["gap"].strip()]
    if rules and not any(DEVICE_RULE.search(r["entry"]) for r in rules):
        notes.append("Rules lane passes on count but holds no device or DiGA rule; route device rules to dh-regulatory-and-quality regulatory-pathway-and-classification (a note, not a fail, unless your rule says so)")
    if notes:
        print()
        print("Notes (not fails; facts from the research rows, read 20 October 2026):")
        for n in dict.fromkeys(notes):
            print(f"- {n}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    x = sub.add_parser("deltas"); x.add_argument("file")
    y = sub.add_parser("screen-diff"); y.add_argument("earlier"); y.add_argument("later")
    z = sub.add_parser("rules"); z.add_argument("--since"); z.add_argument("--signals")
    m = sub.add_parser("mi-check"); m.add_argument("map"); m.add_argument("--as-of", required=True); m.add_argument("--max-age-days", type=int); m.add_argument("--lanes"); m.add_argument("--jurisdictions"); m.add_argument("--readable-source", action="store_true")
    w = sub.add_parser("wordcount"); w.add_argument("file"); w.add_argument("--limit", type=int, default=450)
    a = p.parse_args()
    {"deltas": cmd_deltas, "screen-diff": cmd_screen_diff, "rules": cmd_rules, "mi-check": cmd_mi_check, "wordcount": cmd_wordcount}[a.cmd](a)


if __name__ == "__main__":
    main()
