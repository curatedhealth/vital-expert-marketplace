#!/usr/bin/env python3
"""Two fidelity helpers that work on the person's own files.

1. claims: set each shipped claim beside its source passage and quote the words that differ.
   python3 fidelity_sample.py claims SAMPLE.csv [--shipped N]
   CSV columns: claim_id, version, product_text, source_passage, source_ref
   Optional column: population_product, population_source
   Output per claim: words in the source passage missing from the product text (possible
   dropped caveat, hedge or population limit), words in the product text absent from the
   passage (possible stronger verb or wider population), and numbers that differ.
   --shipped N states how many claims shipped in the version, so the output reports
   sample coverage (the old DH-01.01.4.2.2 rule: never sample only the claims that match).
   The script never marks match or fail. The person marks each row against their own rule.

2. adherence: delivered dose against the prescribed regimen, per user (Carroll adherence:
   content, frequency, duration, coverage, TM102, DOI 10.1186/1748-5908-2-40).
   python3 fidelity_sample.py adherence LOG.csv --sessions-per-week S --weeks W
          [--min-minutes M] [--enrolled N]
   CSV columns: user_id, week, sessions, minutes
   Output per user: sessions delivered of expected, sessions meeting the minimum minutes,
   weeks with any use; coverage = users with any session over enrolled users.
   The regimen and any threshold are the person's. The script computes; it never sets a bar.
"""
import argparse
import csv
import re
import statistics
import sys

STOP = set("""a an the and or of to in on for with by at as is are was were be been being that this these
those it its from into than then there their they them which who whom whose while""".split())

WORD = re.compile(r"[A-Za-z][A-Za-z0-9'\-]*")
NUM = re.compile(r"(?<![A-Za-z0-9])\d+(?:[.,·]\d+)?")


def words(text):
    return [w.lower() for w in WORD.findall(text or "")]


def content_words(text):
    return [w for w in words(text) if w not in STOP]


def nums(text):
    return set(n.replace("·", ".").replace(",", ".") for n in NUM.findall(text or ""))


def diff_claim(product, source):
    p, s = content_words(product), content_words(source)
    ps, ss = set(p), set(s)
    dropped = [w for w in dict.fromkeys(s) if w not in ps]
    added = [w for w in dict.fromkeys(p) if w not in ss]
    n_added = sorted(nums(product) - nums(source))
    n_dropped = sorted(nums(source) - nums(product))
    return dropped, added, n_added, n_dropped


def run_claims(path, shipped):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print("Fidelity sample: product text beside source passage. Differences are quoted for the person to mark;")
    print("the script marks nothing as match or fail. Check_claim overlap is not used here (register N3).")
    if shipped:
        print(f"Sample coverage: {len(rows)} of {shipped} shipped claims ({100 * len(rows) / shipped:.0f} percent).")
    else:
        print(f"Sample coverage: {len(rows)} claims; number shipped not given [GAP].")
    no_source = 0
    for r in rows:
        cid, ver = r.get("claim_id", "?"), r.get("version", "?")
        prod, src = r.get("product_text", ""), r.get("source_passage", "")
        print()
        print(f"{cid} (version {ver}) source: {r.get('source_ref') or '[GAP]'}")
        print(f"  product: \"{prod}\"")
        if not src.strip() or "[GAP]" in src:
            no_source += 1
            print("  source passage: none. A claim with no source is a fail under the old DH-01.01.4.2.2 rule, if the person adopts it.")
            continue
        print(f"  source:  \"{src}\"")
        dropped, added, n_add, n_drop = diff_claim(prod, src)
        print(f"  in source, not in product: {', '.join(dropped) if dropped else 'none'}")
        print(f"  in product, not in source: {', '.join(added) if added else 'none'}")
        if n_add or n_drop:
            print(f"  numbers: product only {n_add or 'none'}; source only {n_drop or 'none'}")
        pp, psrc = r.get("population_product"), r.get("population_source")
        if pp or psrc:
            print(f"  population: product \"{pp or '[GAP]'}\" vs source \"{psrc or '[GAP]'}\"")
    print()
    print(f"Claims with no source passage: {no_source} of {len(rows)}.")


def run_adherence(path, spw, weeks, min_minutes, enrolled):
    expected = spw * weeks
    users = {}
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            u = users.setdefault(r["user_id"], {"sessions": 0, "weeks_used": 0, "minutes": 0.0, "weeks_seen": set(), "long": 0})
            s = int(r.get("sessions") or 0)
            m = float(r.get("minutes") or 0)
            if int(r["week"]) > weeks:
                continue
            u["sessions"] += s
            u["minutes"] += m
            if s > 0:
                u["weeks_used"] += 1
                if min_minutes and s and (m / s) >= min_minutes:
                    u["long"] += s
    print(f"Delivered dose against the regimen the person gave: {spw} sessions per week for {weeks} weeks = {expected} expected sessions.")
    if min_minutes:
        print(f"Minimum minutes per session (person's): {min_minutes}. Counted from weekly averages, not single sessions.")
    print("Adherence in Carroll's sense: frequency and duration delivered against the plan (TM102, DOI 10.1186/1748-5908-2-40).")
    print()
    print("user_id | sessions | percent of expected | weeks with use | mean minutes per session" + (" | sessions at minimum minutes" if min_minutes else ""))
    pcts = []
    for uid, u in sorted(users.items()):
        pct = 100 * u["sessions"] / expected if expected else 0
        pcts.append(pct)
        mean_min = u["minutes"] / u["sessions"] if u["sessions"] else 0
        line = f"{uid} | {u['sessions']} | {pct:.0f} | {u['weeks_used']} of {weeks} | {mean_min:.1f}"
        if min_minutes:
            line += f" | {u['long']}"
        print(line)
    active = sum(1 for u in users.values() if u["sessions"] > 0)
    print()
    if pcts:
        print(f"Users in log: {len(users)}; with any session: {active}.")
        print(f"Percent of expected sessions: mean {statistics.mean(pcts):.0f}, median {statistics.median(pcts):.0f}, min {min(pcts):.0f}, max {max(pcts):.0f}.")
    if enrolled:
        print(f"Coverage: {active} of {enrolled} enrolled users had any session ({100 * active / enrolled:.0f} percent).")
    else:
        print("Coverage: enrolled count not given [GAP].")
    print("Whether any figure passes is the person's rule. No threshold is applied here.")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("claims")
    c.add_argument("csv")
    c.add_argument("--shipped", type=int)
    a = sub.add_parser("adherence")
    a.add_argument("csv")
    a.add_argument("--sessions-per-week", type=int, required=True)
    a.add_argument("--weeks", type=int, required=True)
    a.add_argument("--min-minutes", type=float)
    a.add_argument("--enrolled", type=int)
    args = ap.parse_args()
    if args.cmd == "claims":
        run_claims(args.csv, args.shipped)
    else:
        run_adherence(args.csv, args.sessions_per_week, args.weeks, args.min_minutes, args.enrolled)


if __name__ == "__main__":
    sys.exit(main())
