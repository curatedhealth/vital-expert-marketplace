#!/usr/bin/env python3
"""Helpers for gtm-positioning-monitoring.

sample CHECKSET.csv
    Score the in-market artifacts the person supplied against the positioning line.
    CHECKSET.csv columns: artifact, file, segment, line, in_market (yes/no), sampler.
    `file` is a plain-text copy of the artifact, path relative to the CSV.
    For each artifact: line present (exact, case and spacing ignored), altered (best
    matching sentence at or above the similarity cut, default 0.6), or absent; plus the
    sentences that hold flag words. Flags are signals for the owner, never verdicts.

peers-diff EARLIER.json LATER.json
    Compare two saved commercial-dh.screen_commercial_peers outputs (full or trimmed):
    companies added or dropped, and changes in authorization count or products.

Flag words come from the sourced rows only:
  - device-indicating words listed on the MHRA borderline page behind PC-UK-04
  - approval wording (CP-US-74, PC-EU-11, PC-UK-08)
  - certainty and no-side-effect wording (PC-DE-04, PC-UK-13 [INDUSTRY])
  - wellness exit wording: "clinical grade", "clinically accurate", "medical grade" (PC-US-63)
Standard library only.
"""
import csv
import difflib
import json
import os
import re
import sys

MHRA_WORDS = [  # PC-UK-04 (list read on the same MHRA page, raw file uk_borderline.txt)
    "aids", "alleviates", "avoids", "can benefit those who suffer from", "clears infestations",
    "clinically proven", "combats", "compensates for", "counteracts", "cure", "cures",
    "diagnoses", "assists diagnosis", "eases symptoms", "eliminates", "heals", "help with",
    "investigation", "monitors", "pain relief", "relief from pain", "prevents",
    "protects against", "repairs", "stops", "traditionally used for", "treats", "treatments",
]
APPROVAL = ["fda approved", "fda-approved", "fda cleared", "fda-cleared", "approved by", "certified",
            "ce certified", "ce-certified", "bfarm-approved", "bfarm approved", "diga-listed",
            "nhs approved", "nhs-approved", "endorsed by", "registered with the fda"]
CERTAINTY = ["guaranteed", "guarantee", "no side effects", "without side effects"]
WELLNESS_EXIT = ["clinical grade", "clinical-grade", "clinically accurate", "medical grade", "medical-grade"]

GROUPS = [("device-indicating word (PC-UK-04)", MHRA_WORDS),
          ("approval wording (CP-US-74, PC-EU-11, PC-UK-08)", APPROVAL),
          ("certainty wording (PC-DE-04; PC-UK-13 [INDUSTRY])", CERTAINTY),
          ("wellness exit wording (PC-US-63)", WELLNESS_EXIT)]


def norm(s):
    return re.sub(r"\s+", " ", s.lower()).strip()


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


def flags(text):
    out = []
    for sent in sentences(text):
        low = " " + norm(sent) + " "
        for label, words in GROUPS:
            for w in words:
                if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
                    out.append((w, label, sent))
    return out


def sample(csv_path, cut=0.6):
    base = os.path.dirname(os.path.abspath(csv_path))
    rows = list(csv.DictReader(open(csv_path, encoding="utf-8")))
    print("| Artifact | Segment | In market | Line | Best match | Similarity | Sampler |")
    print("|---|---|---|---|---|---|---|")
    all_flags = []
    for r in rows:
        path = os.path.join(base, r["file"])
        if not os.path.exists(path):
            print(f"| {r['artifact']} | {r['segment']} | {r['in_market']} | not measurable [GAP] (no copy supplied) | - | - | {r.get('sampler') or 'not named'} |")
            continue
        text = open(path, encoding="utf-8").read()
        line = norm(r["line"])
        if line in norm(text):
            status, best, score = "present", r["line"], 1.0
        else:
            n = max(1, len(sentences(r["line"])))
            sents = sentences(text)
            cands = [" ".join(sents[i:i + n]) for i in range(max(1, len(sents) - n + 1))]
            scored = [(difflib.SequenceMatcher(None, line, norm(c)).ratio(), c) for c in cands] or [(0.0, "")]
            score, best = max(scored)
            status = "altered" if score >= cut else "absent"
        if r["in_market"].strip().lower() != "yes":
            status += " (not the in-market copy: do not score)"
        print(f"| {r['artifact']} | {r['segment']} | {r['in_market']} | {status} | {best[:90]} | {score:.2f} | {r.get('sampler') or 'not named'} |")
        for w, label, sent in flags(text):
            all_flags.append((r["artifact"], w, label, sent))
    print()
    print("Flags (signals for the owner, not verdicts):")
    print()
    print("| Artifact | Word | Group and row | Sentence |")
    print("|---|---|---|---|")
    for a, w, label, sent in all_flags:
        print(f"| {a} | {w} | {label} | {sent[:120]} |")
    print()
    print(f"Artifacts: {len(rows)}. Similarity cut for 'altered': {cut} (a tool setting, not a rule; the person's pass rule decides).")


def peer_index(d):
    sm = d.get("screen_market", {})
    return {r["company"]: r for r in sm.get("results", [])}


def peers_diff(a_path, b_path):
    a, b = json.load(open(a_path, encoding="utf-8")), json.load(open(b_path, encoding="utf-8"))
    ia, ib = peer_index(a), peer_index(b)
    print(f"Earlier: {len(ia)} companies returned ({a.get('call', {}).get('args', '')}). Later: {len(ib)} ({b.get('call', {}).get('args', '')}).")
    if a.get("call", {}).get("args") != b.get("call", {}).get("args"):
        print("The two runs used different arguments; differences may come from the query, not the market.")
    print()
    print("| Company | Change | Earlier | Later |")
    print("|---|---|---|---|")
    for c in sorted(set(ia) | set(ib)):
        if c not in ia:
            print(f"| {c} | added | - | {ib[c].get('products')} |")
        elif c not in ib:
            print(f"| {c} | not returned | {ia[c].get('products')} | - |")
        else:
            for k in ("authorizations", "products", "studies", "safety_events"):
                if ia[c].get(k) is None or ib[c].get(k) is None:
                    continue  # field not in one of the saved runs: not a change
                if ia[c].get(k) != ib[c].get(k):
                    print(f"| {c} | {k} | {ia[c].get(k)} | {ib[c].get(k)} |")
    print()
    print("'Not returned' can be a limit or ranking effect; it is not evidence that a company left the market.")


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "sample":
        sample(sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 0.6)
    elif len(sys.argv) == 4 and sys.argv[1] == "peers-diff":
        peers_diff(sys.argv[2], sys.argv[3])
    else:
        print(__doc__)
        sys.exit(2)
