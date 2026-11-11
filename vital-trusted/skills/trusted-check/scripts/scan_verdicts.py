#!/usr/bin/env python3
"""Scan a TRUSTED summary for verdict words and leaked codes before it is shown.

Usage:
    python scan_verdicts.py summary.txt
    python scan_verdicts.py summary.txt --json
    cat summary.txt | python scan_verdicts.py -

Exit code 0 when nothing is found, 1 when there are hits, 2 on a usage error.

It finds words, not meaning. A clean scan is not a clean summary.

Verdict words inside quotation marks, and lines starting with ">", are skipped: they
repeat the person's request or the supplied material, not the summary's own voice.
The closing statement must be the last line; the only text allowed after it is a
"Detail for reviewers" section.

Counts must add up: "fix these <n> things", "supply <k> missing" and "answer <q>
questions" in the header must equal the sums of the "to fix", "missing" and "question"
counts in the letter rows, and a light "<n> thing(s) to fix" must equal the number of
notes ("- ") under it. One is singular: "fix this 1 thing", "supply 1 missing item",
"answer 1 question"; never "fix these 1 things".

After a safety flag, the summary never says "Nothing flagged in what was checked" as its
overall line; it says "Nothing else flagged in what was checked". Letter rows may still
read "nothing flagged in what was checked" for their own letter.
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
    (r"\ball\s+set\b", re.I, "says the draft can go", False),
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

# An approval the person reported is attribution, not a verdict (TR-H3). The word is
# allowed on a line that says the person told us.
ATTRIBUTION = re.compile(r"\b(?:as you told me|you told me|you said|you stated|as you stated|as you said|per you)\b", re.I)

# Quoted spans: the person's words or the supplied material, repeated. Masked before the
# verdict scan. Straight single quotes count only when they are not apostrophes.
QUOTED = re.compile(
    r'"[^"\n]*"'
    r"|\u201c[^\u201d\n]*\u201d"
    r"|\u2018[^\u2019\n]*\u2019"
    r"|(?<![A-Za-z0-9])'[^'\n]+?'(?![A-Za-z0-9])"
)
BLOCKQUOTE = re.compile(r"^\s*>")


def mask_quotes(line):
    """Blank out quoted spans so their words are not read as the summary's verdicts."""
    return QUOTED.sub(lambda m: " " * len(m.group(0)), line)


# Header totals and row counts (every header count equals the sum of the rows).
HEADER_COUNTS = {
    "to fix": re.compile(r"\bfix\s+(?:these|this)\s+(\d+)\s+things?\b", re.I),
    "missing": re.compile(r"\bsupply\s+(\d+)\s+missing\b", re.I),
    "questions": re.compile(r"\banswer\s+(\d+)\s+questions?\b", re.I),
}
ROW_COUNTS = {
    "to fix": re.compile(r"\b(\d+)\s+to\s+fix\b", re.I),
    "missing": re.compile(r"\b(\d+)\s+missing\b", re.I),
    "questions": re.compile(r"\b(\d+)\s+questions?\s+for\b", re.I),
}
ROW_START = re.compile(r"^\s*" + LETTERS + r"(?=\s{2,}|\s*$|\s+\d)")
LIGHT_HEADER = re.compile(r"^\s*Quick check\b.*?\b(\d+)\s+things?\s+to\s+fix\b", re.I)


def check_counts(lines):
    """Compare header totals with the sums of the row counts, and light counts with notes."""
    hits = []
    header_line, header = None, {}
    sums = {key: 0 for key in ROW_COUNTS}
    rows = 0
    for number, line in enumerate(lines, start=1):
        if DETAIL_HEADING.match(line):
            break
        own = mask_quotes(line)
        if header_line is None and HEADER_COUNTS["to fix"].search(own):
            header_line = number
            for key, pattern in HEADER_COUNTS.items():
                found = pattern.search(own)
                header[key] = int(found.group(1)) if found else 0
            continue
        if ROW_START.match(own):
            rows += 1
            for key, pattern in ROW_COUNTS.items():
                sums[key] += sum(int(m.group(1)) for m in pattern.finditer(own))
        light = LIGHT_HEADER.match(own)
        if light:
            notes = 0
            for following in lines[number:]:
                if following.lstrip().startswith("- "):
                    notes += 1
                elif following.startswith((" ", "\t")) and following.strip():
                    continue
                else:
                    break
            if notes and notes != int(light.group(1)):
                hits.append({"line": number, "found": light.group(0).strip()[:60],
                             "why": f"says {light.group(1)} to fix but lists {notes} notes", "kind": "count"})
    if header_line is not None and rows:
        for key in HEADER_COUNTS:
            if header[key] != sums[key]:
                hits.append({"line": header_line, "found": f"{header[key]} {key}",
                             "why": f"header says {header[key]} {key}; the rows add up to {sums[key]}",
                             "kind": "count"})
    return hits


# One is singular, more than one is plural.
NUMBER_FORM = [
    (re.compile(r"\bfix\s+these\s+1\s+things?\b", re.I), "one thing: write 'fix this 1 thing'"),
    (re.compile(r"\bfix\s+this\s+(?:[02-9]|\d{2,})\s+things?\b", re.I), "more than one: write 'fix these <n> things'"),
    (re.compile(r"\bfix\s+this\s+1\s+things\b", re.I), "one thing: write 'fix this 1 thing'"),
    (re.compile(r"\bsupply\s+1\s+missing\s+items\b", re.I), "one item: write 'supply 1 missing item'"),
    (re.compile(r"\banswer\s+1\s+questions\b", re.I), "one question: write 'answer 1 question'"),
]

# The flag's heading, at any depth; and an overall "nothing flagged" line after it.
FLAG_HEADING = re.compile(r"something to pass to your safety reporting procedure", re.I)
NOTHING_FLAGGED = re.compile(r"(?:^\s*|[.;:]\s+)Nothing flagged in what was checked\b")


def check_after_flag(lines):
    """After a safety flag, the overall line says 'Nothing else flagged', never 'Nothing flagged'."""
    hits, flagged = [], False
    for number, line in enumerate(lines, start=1):
        if DETAIL_HEADING.match(line):
            break
        if FLAG_HEADING.search(line):
            flagged = True
            continue
        own = mask_quotes(line)
        if flagged and not ROW_START.match(own) and NOTHING_FLAGGED.search(own):
            hits.append({"line": number, "found": "Nothing flagged in what was checked",
                         "why": "a safety flag was given above: write 'Nothing else flagged in what was checked'",
                         "kind": "count"})
    return hits


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
        own_voice = "" if BLOCKQUOTE.match(line) else mask_quotes(line)
        for pattern, flags, reason, negation_allowed in VERDICTS:
            for match in re.finditer(pattern, own_voice, flags):
                if negation_allowed and NEGATION.search(own_voice[: match.start()]):
                    continue
                if reason == "reads as approval" and ATTRIBUTION.search(line):
                    continue
                hits.append({"line": number, "found": match.group(0), "why": reason, "kind": "verdict"})
        if in_detail:
            continue
        for pattern, reason in CODES:
            for match in re.finditer(pattern, line):
                hits.append({"line": number, "found": match.group(0).strip(), "why": reason, "kind": "code"})

    hits.extend(check_counts(lines))
    hits.extend(check_after_flag(lines))
    for number, line in enumerate(lines, start=1):
        own = mask_quotes(line)
        for pattern, reason in NUMBER_FORM:
            for match in pattern.finditer(own):
                hits.append({"line": number, "found": match.group(0), "why": reason, "kind": "count"})

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
