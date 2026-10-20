#!/usr/bin/env python3
"""List framing words in a draft for a person to review.

Part of the VITAL TRUSTED skill honest-framing (tasks TR-3.2.1 and TR-3.2.3).

Groups:
  certainty     words that close the question ("proves", "dramatic", "clearly")
  hedging       hedge words, with a count per sentence so stacked hedges show
  minimizing    qualifiers that shrink a rate ("only 2%", "just", "as few as")
  interest      independence labels and sponsor or company-data words

Usage:
  python find_framing_cues.py draft.txt
  python find_framing_cues.py draft.txt --json
  cat draft.txt | python find_framing_cues.py -

It finds words, not meaning. Read every hit against the material.
Exit code 0 always (hits are not errors), 2 on a usage error.
"""
import argparse
import json
import re
import sys

CERTAINTY = [
    r"prov(?:e|es|ed|en|ing)\b", r"proof\b", r"definitive(?:ly)?\b", r"conclusive(?:ly)?\b",
    r"dramatic(?:ally)?\b", r"breakthrough\b", r"remarkabl[ey]\b", r"game[- ]chang\w*",
    r"unprecedented\b", r"revolutionar\w*", r"clearly\b", r"undeniabl[ey]\b",
    r"unquestionabl[ey]\b", r"established\b", r"robust(?:ly)?\b", r"striking(?:ly)?\b",
    r"transformative\b", r"highly significant\b", r"(?<!statistically )significant(?:ly)?\b(?! *\(?p)",
    r"superior(?:ity)?\b", r"long[- ]term\b", r"durable\b", r"life[- ]changing\b",
]
HEDGES = [
    r"may\b", r"might\b", r"could\b", r"possibl[ey]\b", r"potential(?:ly)?\b",
    r"appears? to\b", r"seems? to\b", r"suggest(?:s|ed|ing)?\b", r"perhaps\b",
    r"preliminary\b", r"further research\b", r"interpreted with caution\b",
    r"cannot be ruled out\b", r"to some extent\b", r"in some patients\b",
]
MINIMIZING = [
    r"only\s+(?:\d[\d.,]*\s*%|\d[\d.,]*\s+(?:in|of|out of)\s+\d)", r"just\s+\d[\d.,]*",
    r"as (?:few|little|low) as\b", r"merely\b", r"negligible\b", r"rare(?:ly)?\b",
    r"minimal\b", r"mild\b",
]
INTEREST = [
    r"independent(?:ly)?\b", r"unbiased\b", r"objective(?:ly)?\b", r"neutral\b",
    r"experts? agree\b", r"physicians? prefer\b", r"doctors? prefer\b",
    r"real[- ]world (?:evidence|data|doctors)\b", r"data on file\b", r"internal analysis\b",
    r"funded by\b", r"sponsored by\b", r"commissioned by\b", r"on behalf of\b",
    r"employee(?:s)? of\b", r"honorari(?:a|um)\b", r"consult(?:ant|ing|ancy)\b",
    r"advisory board\b", r"no conflicts?\b", r"no role\b",
]

GROUPS = {
    "certainty": [re.compile(r"\b" + p, re.I) for p in CERTAINTY],
    "hedging": [re.compile(r"\b" + p, re.I) for p in HEDGES],
    "minimizing": [re.compile(r"\b" + p, re.I) for p in MINIMIZING],
    "interest": [re.compile(r"\b" + p, re.I) for p in INTEREST],
}

SENTENCE = re.compile(r"[^.!?\n]+[.!?]?")


def scan(text):
    hits = []
    stacked = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for group, pats in GROUPS.items():
            seen = set()
            for pat in pats:
                for m in pat.finditer(line):
                    if (m.start(), m.end()) in seen:
                        continue
                    seen.add((m.start(), m.end()))
                    lo, hi = max(0, m.start() - 40), min(len(line), m.end() + 40)
                    hits.append({"line": lineno, "group": group, "match": m.group(0),
                                 "context": line[lo:hi].strip()})
        for s in SENTENCE.finditer(line):
            sent = s.group(0)
            n = sum(len(p.findall(sent)) for p in GROUPS["hedging"])
            if n >= 2:
                stacked.append({"line": lineno, "hedges": n, "sentence": sent.strip()})
    hits.sort(key=lambda h: (h["line"], h["group"]))
    counts = {g: sum(1 for h in hits if h["group"] == g) for g in GROUPS}
    return {"counts": counts, "stacked_hedges": stacked, "hits": hits,
            "note": "words to look at, not findings; read each against the material"}


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("path", help="text file, or - for standard input")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    try:
        text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    except OSError as e:
        print(f"cannot read {a.path}: {e}", file=sys.stderr)
        sys.exit(2)
    res = scan(text)
    if a.json:
        print(json.dumps(res, indent=2))
        return
    c = res["counts"]
    print("Words to look at (not findings)")
    print(f"  certainty {c['certainty']}, hedging {c['hedging']}, "
          f"minimizing {c['minimizing']}, interest {c['interest']}")
    for h in res["hits"]:
        print(f"  line {h['line']:>3}  {h['group']:<10}  '{h['match']}'  ... {h['context']} ...")
    for s in res["stacked_hedges"]:
        print(f"  line {s['line']:>3}  stacked    {s['hedges']} hedges in: {s['sentence']}")


if __name__ == "__main__":
    main()
