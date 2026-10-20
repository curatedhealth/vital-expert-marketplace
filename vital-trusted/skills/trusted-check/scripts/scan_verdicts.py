#!/usr/bin/env python3
"""Scan a TRUSTED summary for verdict words and leaked codes before it is shown.

Usage:
    python scan_verdicts.py summary.txt
    python scan_verdicts.py summary.txt --json
    cat summary.txt | python scan_verdicts.py -

Exit code 0 when nothing is found, 1 when there are hits, 2 on a usage error.

It finds words, not meaning. A clean scan is not a clean summary.
"""

import argparse
import json
import re
import sys

CLOSING = "This check flags issues. It is not medical, legal, regulatory or ethics review."

LETTERS = r"(?:Tangible|Rule-compliant|Unbiased|Safe|True|Ethical|Defensible)"

SKILL_NAMES = [
    "trusted-capability-map", "trusted-intake", "trusted-check",
    "substance-and-usefulness", "fit-for-reader", "claims-and-label",
    "market-rules-and-data", "balanced-evidence", "honest-framing", "patient-safety",
    "grounded-statements", "sourced-claims", "responsible-inputs", "responsible-use",
    "work-record", "claim-assessment", "source-assessment", "confidence-scoring",
    "citation-and-record",
]

# (regex, flags, reason, negation_allowed)
# negation_allowed: a "not" or "never" shortly before the match makes it acceptable,
# for words that are verdicts only when asserted ("not proof the statements are true").
VERDICTS = [
    (r"\bpass(?:es|ed|ing)?\b(?!\s+(?:it|them|this|these|that|to|on|along)\b)", re.I,
     "reads as a pass/fail verdict", False),
    (r"(?<![Rr]ule-)\bcompliant\b", re.I, "reads as a compliance verdict", False),
    (r"\bnon-compliant\b", re.I, "reads as a compliance verdict", False),
    (r"\bapprov(?:ed|able)\b(?!\s+(?:label|labeling|labelling|product information|indication|indications|use|uses)\b)",
     re.I, "reads as approval", False),
    (r"\bvalidated\b", re.I, "reads as validation", False),
    (r"\bsafe\b(?!\s+reporting)", 0, "lowercase 'safe' reads as a safety verdict", True),
    (r"\bSafe\s+to\b", 0, "'Safe to ...' reads as a safety verdict", False),
    (r"\b(?:is|are|looks|seems)\s+(?:all\s+)?(?:safe|accurate|correct|true|ethical|fine|good|clean|balanced)\b",
     re.I, "states a verdict about the draft", True),
    (r"\baccurate\b", re.I, "reads as an accuracy verdict", True),
    (r"\bethical\b(?!\s+review)", 0, "lowercase 'ethical' reads as an ethics verdict", True),
    (r"\b(?:good|ready|okay|ok|fine|safe|clear)\s+to\s+(?:go|send|use|publish|share|submit)\b", re.I,
     "says the draft can go", False),
    (r"\bready\s+for\s+(?:approval|sign-off|signoff|submission|review|release)\b", re.I,
     "says the draft is ready", False),
    (r"\b(?:all\s+clear|no\s+issues|looks\s+good|green\s+light|signed\s+off|almost\s+there|nearly\s+there)\b",
     re.I, "reads as a verdict", False),
    (r"\b(?:TRUSTED|overall|quality|total)\s+score\b", re.I, "a score for the draft is a verdict", False),
    (r"\b\d{1,3}\s*/\s*100\b", 0, "a score for the draft is a verdict", False),
    (r"\bgrade\s+[A-F]\b", 0, "a grade for the draft is a verdict", False),
    (r"\b(?:yes|no)[,.]?\s+(?:it\s+)?(?:can|is\s+ok|is\s+okay)\s+(?:be\s+)?sen[dt]\b", re.I,
     "answers 'is it OK to send' with yes or no", False),
]

CODES = [
    (r"\bTR-(?:H\d+|\d+(?:\.\d+){1,2})\b", "rule or framework code shown to the person"),
    (r"\[GAP:", "raw gap syntax shown to the person"),
    (r"\[CHECK\b", "internal [CHECK] marker shown to the person"),
    (r"\bpattern\s+[A-Z]\d{1,2}\b", "pattern id shown to the person"),
    (r"^\s*[TRUSED]\s{1,3}" + LETTERS + r"\b", "letter code shown beside the letter word"),
    (r"^\s*" + LETTERS + r"\s+·\s", "raw check line shown to the person"),
    (r"\b(?:" + "|".join(re.escape(s) for s in SKILL_NAMES) + r")\b", "skill name shown to the person"),
]

NEGATION = re.compile(r"\b(?:not|never|no|cannot|can't|isn't|aren't|nor)\b[^.;:]{0,40}$", re.I)
DETAIL_HEADING = re.compile(r"^\s*Detail for reviewers\b", re.I)


def scan(text):
    hits = []
    lines = text.splitlines()
    in_detail = False
    for number, line in enumerate(lines, start=1):
        if DETAIL_HEADING.match(line):
            in_detail = True
        if line.strip() == CLOSING:
            continue
        for pattern, flags, reason, negation_allowed in VERDICTS:
            for match in re.finditer(pattern, line, flags):
                if negation_allowed and NEGATION.search(line[: match.start()]):
                    continue
                hits.append({"line": number, "found": match.group(0), "why": reason, "kind": "verdict"})
        if in_detail:
            continue
        for pattern, reason in CODES:
            for match in re.finditer(pattern, line):
                hits.append({"line": number, "found": match.group(0).strip(), "why": reason, "kind": "code"})

    nonblank = [line.strip() for line in lines if line.strip()]
    if not nonblank or CLOSING not in nonblank:
        hits.append({"line": len(lines), "found": "", "why": "closing statement missing or altered", "kind": "closing"})
    elif not in_detail and nonblank[-1] != CLOSING:
        hits.append({"line": len(lines), "found": nonblank[-1][:60],
                     "why": "closing statement is not the last line", "kind": "closing"})
    return hits


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", help="summary text file, or - for standard input")
    parser.add_argument("--json", action="store_true", help="print hits as JSON")
    args = parser.parse_args(argv)
    try:
        text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    except OSError as error:
        print(f"Cannot read {args.path}: {error}", file=sys.stderr)
        return 2
    hits = scan(text)
    if args.json:
        print(json.dumps({"hits": hits, "count": len(hits)}, indent=2))
    elif hits:
        for hit in hits:
            found = f' "{hit["found"]}"' if hit["found"] else ""
            print(f'line {hit["line"]}:{found} ({hit["why"]})')
        print(f"{len(hits)} to fix before showing the summary.")
    else:
        print("No verdict words or codes found. Read the summary once anyway.")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
