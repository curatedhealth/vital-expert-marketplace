#!/usr/bin/env python3
"""List phrases in a text that may stigmatize, blame or define people by a condition.

Part of the VITAL TRUSTED skill `responsible-use` (task: equity and inclusion).

The scan finds wording, not meaning. Every hit is a phrase to look at, never a finding:
quotes, a community's own preferred terms, product names and medical terminology can all
match. Each term carries the source it comes from in references/rules.md; terms marked
CHECK are good practice that has not been confirmed against a primary document.

Usage:
    python scan_language.py draft.txt
    python scan_language.py draft.txt --json
    cat draft.txt | python scan_language.py -
"""
import argparse
import json
import re
import sys

# (pattern, category, suggestion, source id in references/rules.md)
TERMS = [
    (r"\baddicts?\b", "blame or stigma", "person with a substance use disorder", "U9"),
    (r"\bjunkies?\b", "blame or stigma", "person with a substance use disorder", "U9"),
    (r"\b(?:substance|drug)\s+abusers?\b", "blame or stigma", "person with a substance use disorder", "U9"),
    (r"\babusers?\b", "blame or stigma", "person with a substance use disorder (if about substance use)", "U9"),
    (r"\bsuffer(?:s|ing|ed)?\s+from\b", "suffering framing", "has, lives with, people with", "U13 CHECK"),
    (r"\bsufferers?\b", "suffering framing", "people with <condition>", "U13 CHECK"),
    (r"\bafflicted\s+(?:with|by)\b", "suffering framing", "has, lives with", "U13 CHECK"),
    (r"\bvictims?\s+of\b", "suffering framing", "people who have, people living with", "U13 CHECK"),
    (r"\b(?:wheelchair[- ]bound|confined\s+to\s+a\s+wheelchair)\b", "suffering framing", "uses a wheelchair", "U13 CHECK"),
    (r"\bnon-?compliant\b", "blame or stigma", "did not take the treatment as planned; stopped treatment", "U13 CHECK"),
    (r"\bnon-?adherent\s+patients?\b", "blame or stigma", "people who stopped or changed treatment", "U13 CHECK"),
    (r"\bcommitted\s+suicide\b", "blame or stigma", "died by suicide", "U13 CHECK"),
    (r"\b(?:the\s+)?(?:diabetics|epileptics|asthmatics|schizophrenics|hemophiliacs|haemophiliacs)\b",
     "condition as the person", "people with <condition>, unless the community prefers otherwise", "U10, U13 CHECK"),
    (r"\bthe\s+mentally\s+ill\b", "group label", "people with mental illness", "U10, U13 CHECK"),
    (r"\bthe\s+disabled\b", "group label", "disabled people or people with disabilities (follow the group's preference)", "U10"),
    (r"\bhandicapped\b", "group label", "disabled people or people with disabilities (follow the group's preference)", "U10, U13 CHECK"),
    (r"\bthe\s+elderly\b", "group label", "older people, or adults aged <n> and over as the source defines them", "U11, U13 CHECK"),
    (r"\bnormal\s+(?:people|patients|subjects|controls|volunteers)\b",
     "group label", "healthy volunteers; people without <condition>", "U11 CHECK"),
]

COMPILED = [(re.compile(p, re.IGNORECASE), c, s, src) for p, c, s, src in TERMS]


def scan(text):
    hits = []
    for lineno, line in enumerate(text.splitlines(), start=1):
        for rx, cat, sugg, src in COMPILED:
            for m in rx.finditer(line):
                start = max(0, m.start() - 40)
                end = min(len(line), m.end() + 40)
                hits.append({
                    "line": lineno,
                    "phrase": m.group(0),
                    "category": cat,
                    "consider": sugg,
                    "source": src,
                    "context": line[start:end].strip(),
                    "in_quotes": _inside_quotes(line, m.start()),
                })
    # Drop "abusers" hits already covered by a longer substance/drug abuser hit.
    longer = {(h["line"], h["context"]) for h in hits if re.match(r"(?i)(substance|drug)\s+abuser", h["phrase"])}
    hits = [h for h in hits if not (h["phrase"].lower().startswith("abuser") and (h["line"], h["context"]) in longer)]
    hits.sort(key=lambda h: (h["line"], h["context"]))
    return hits


def _inside_quotes(line, pos):
    before = line[:pos]
    return (before.count('"') % 2 == 1) or (before.count("“") > before.count("”"))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", help="text file, or - for stdin")
    ap.add_argument("--json", action="store_true", help="print JSON")
    args = ap.parse_args(argv)
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    hits = scan(text)
    counts = {}
    for h in hits:
        counts[h["category"]] = counts.get(h["category"], 0) + 1
    if args.json:
        print(json.dumps({"phrases_to_look_at": len(hits), "by_category": counts, "hits": hits}, indent=2))
        return 0
    print(f"Phrases to look at: {len(hits)} (wording matches, not findings)")
    for cat, n in sorted(counts.items()):
        print(f"  {cat}: {n}")
    for h in hits:
        q = " [inside quotation marks: keep a quote exact]" if h["in_quotes"] else ""
        print(f"line {h['line']}: \"{h['phrase']}\" ({h['category']}; source {h['source']}){q}")
        print(f"    context: ...{h['context']}...")
        print(f"    consider: {h['consider']}")
    if not hits:
        print("No listed phrases found. This does not mean the text is free of stigma or stereotypes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
