#!/usr/bin/env python3
"""First-pass claim screen for task A2 (claims audit).

Reads marketing text (a file or stdin), splits it into sentences, and lists
wording that matches a claim type in references/claim-rules.md, with the row ids
that claim type can engage. It finds words, not meaning: every hit is a candidate
for a person to judge, and a sentence with no hit is NOT cleared. The skill's
audit (intended use, audience, evidence passage) decides the flag level.

Usage:
  python3 claim_screen.py ../evals/files/sleepwell_ad_illustrative.txt
  python3 claim_screen.py --market DE --audience consumer ad.txt
  python3 claim_screen.py --json ad.txt
"""
import argparse
import json
import re
import sys

# (claim type number in claim-rules.md, label, regex, rows, markets the rows apply to or None for all)
PATTERNS = [
    (1, "Cure, treat or prevent", r"\b(cures?|cured|curing|heal(s|ed)?|heilt|heilung|eliminates?|prevents?|beseitigt)\b",
     ["PC-EU-10", "PC-UK-07", "PC-DE-03", "PC-UK-13 [INDUSTRY]", "PC-US-63 (if sold as wellness)"], None),
    (2, "Certain success or no harm", r"\b(guarantee[ds]?|garantiert|100\s?%|no side[- ]effects?|ohne nebenwirkungen|risk[- ]free|completely safe)\b",
     ["PC-DE-04", "PC-UK-13 [INDUSTRY]", "PC-US-03"], None),
    (3, "Efficacy or 'clinically proven'", r"\b(clinically (proven|validated|tested)|klinisch (bewiesen|belegt|getestet)|proven to|scientifically proven)\b",
     ["PC-US-28 to PC-US-31", "PC-US-72, PC-US-73 [WF]", "PC-DE-05", "PC-UK-04", "PC-UK-10 [INDUSTRY]"], None),
    (4, "Approval, certification or endorsement", r"\b(fda[- ](cleared|approved|authori[sz]ed)|ce[- ](certified|marked|zertifiziert)|diga[- ]listed|approved by|doctor[- ]recommended|arztempfohlen|clinical[- ]grade|medical[- ]grade)\b",
     ["PC-EU-11", "PC-UK-08", "PC-US-63", "PC-UK-03", "PC-DE-11"], None),
    (5, "Comparative", r"\b(better than|unlike|outperforms?|beats?|superior to|besser als|more effective than)\b",
     ["PC-US-26", "PC-US-27", "PC-EU-02", "PC-DE-03", "PC-US-72 [WF]"], None),
    (7, "Diagnosis or self-test implied", r"\b(diagnos\w*|take the test|find out if you have|detects?|screen(s|ing)? for|what'?s your \w+ type)\b",
     ["PC-UK-12 [INDUSTRY]", "PC-UK-14 [INDUSTRY]", "PC-UK-16 [INDUSTRY]", "PC-US-63", "EU: PC-EU-02"], None),
    (8, "Coverage or price", r"\b(covered by|reimbursed|erstattet|free with|kostenlos|on prescription|auf rezept|krankenkasse|insurance pays|zero cost)\b",
     ["PC-EU-07", "PC-EU-08", "PC-US-03", "CP-DE-01", "CP-DE-03"], None),
    (9, "Number or percentage", r"(\b\d+([.,]\d+)?\s?(%|percent|prozent|minutes?|minuten|hours?|stunden|weeks?|wochen|days?|tage)\b)",
     ["US: PC-US-31", "US: PC-US-40 (payor material)", "DE: PC-DE-05", "EU: PC-EU-07", "cite only the audited market's rows"], None),
    (10, "Disclaimer used as a fix", r"\b(not a medical device|kein medizinprodukt|for information only|for entertainment only|nur zur information)\b",
     ["PC-UK-02", "PC-US-74 [WF]", "PC-US-30", "EU: PC-EU-07"], None),
    (11, "German public advertising: health improved or impaired", r"\b(improves? your health|verbessert (ihre|deine) gesundheit|without (it|this) your|ohne .* gefährdet)\b",
     ["PC-DE-10", "PC-DE-09"], {"DE"}),
    (12, "DiGA offer or advertising", r"\b(auto[- ]?renew\w*|abo\w*|subscription|limited[- ]time offer|sonderangebot|in-app ad\w*)\b",
     ["PC-DE-15", "PC-DE-17"], {"DE"}),
]


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


def screen(text, market=None):
    out = []
    for i, s in enumerate(sentences(text), 1):
        hits = []
        for num, label, rx, rows, markets in PATTERNS:
            if markets and market and market not in markets:
                continue
            found = []
            for m in re.finditer(rx, s, flags=re.IGNORECASE):
                if m.group(0) not in found:
                    found.append(m.group(0))
            if found:
                hits.append({"claim_type": num, "label": label, "matched": "; ".join(found), "rows": rows})
        out.append({"n": i, "sentence": s, "candidates": hits})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?", help="text file; stdin if omitted")
    ap.add_argument("--market", help="US, EU, DE or UK; market-specific patterns run only for their market")
    ap.add_argument("--audience", default="unknown", help="consumer, clinician, payor, fachkreise (recorded, not used to drop rows)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read()
    if not text.strip():
        print("No text given.")
        return 2
    res = screen(text, a.market.upper() if a.market else None)
    if a.json:
        print(json.dumps({"market": a.market, "audience": a.audience, "sentences": res}, indent=1, ensure_ascii=False))
        return 0
    print(f"Market: {a.market or 'not given'}; audience: {a.audience}. Candidates for a person to judge; no hit does not mean cleared.\n")
    print("| # | Sentence | Claim type (claim-rules.md) | Matched | Rows it can engage |")
    print("|---|---|---|---|---|")
    total = 0
    for r in res:
        if not r["candidates"]:
            print(f"| {r['n']} | {r['sentence']} | no wording match | | |")
        for h in r["candidates"]:
            total += 1
            print(f"| {r['n']} | {r['sentence']} | {h['claim_type']} {h['label']} | {h['matched']} | {', '.join(h['rows'])} |")
    print(f"\n{len(res)} sentences, {total} candidate matches. Intended use, audience and evidence passages decide the flag level (claims-audit.md, step 5).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
