#!/usr/bin/env python3
"""List wording that usually marks a label, promotion or comparison issue.

Finds words, not claims or uses. Makes no judgment. Part of the VITAL TRUSTED skill
claims-and-label.

Usage:
    python find_claim_cues.py draft.txt
    python find_claim_cues.py draft.txt --json
    cat draft.txt | python find_claim_cues.py -
"""
import json
import re
import sys

GROUPS = [
    ("comparison", [
        r"\bbetter\b", r"\bfaster\b", r"\bstronger\b", r"\bsafer\b",
        r"\bmore (?:effective|convenient|potent|tolerable)\b",
        r"\bbetter tolerated\b", r"\bsuperior(?:ity)?\b", r"\boutperform\w*",
        r"\bbeats?\b", r"\bversus\b", r"\bvs\.?(?=\s)", r"\bcompared (?:with|to)\b",
        r"\bhead[- ]to[- ]head\b",
    ]),
    ("absolute or superlative", [
        r"\bfirst\b(?![- ]line)", r"\bonly\b", r"\bleading\b", r"\bbest\b",
        r"\bnumber one\b", r"\bno\. ?1\b", r"\bunique\b", r"\bunmatched\b",
        r"\bunrivall?ed\b", r"\bgold standard\b",
    ]),
    ("safety absolute", [
        r"\bsafe(?:ly)?\b", r"\bno side[- ]effects?\b", r"\bside[- ]effect[- ]free\b",
        r"\bharmless\b", r"\brisk[- ]free\b", r"\bwell[- ]tolerated\b",
    ]),
    ("device function", [
        r"\bdiagnos\w*", r"\bdetects?\b", r"\bdetecting\b", r"\bpredicts?\b",
        r"\bprevents?\b", r"\bcures?\b", r"\brules? out\b", r"\bscreens? for\b",
        r"\breplaces? (?:a |your )?(?:visit|doctor|appointment)\w*",
    ]),
    ("population or line of therapy", [
        r"\bchildren\b", r"\badolescents?\b", r"\bteen(?:ager)?s?\b",
        r"\bp(?:a)?ediatric\b", r"\belderly\b", r"\bpregnan\w*",
        r"\bfirst[- ]line\b", r"\bsecond[- ]line\b", r"\bmonotherapy\b",
        r"\bin combination with\b", r"\bmild\b", r"\ball patients\b",
    ]),
    ("unapproved status", [
        r"\boff[- ]label\b", r"\bunlicen[cs]ed\b", r"\bunapproved\b",
        r"\bnot (?:yet )?approved\b", r"\binvestigational\b", r"\bcoming soon\b",
    ]),
    ("promotional tone", [
        r"\bgame[- ]chang\w*", r"\bbreakthrough\b", r"\brevolutionary\b",
        r"\bproven\b", r"\bguaranteed?\b", r"\bmiracle\b", r"\bswitch (?:to|your)\b",
        r"\bask your doctor about\b", r"\bdon'?t wait\b", r"!",
    ]),
]

COMPILED = [(g, [re.compile(p, re.IGNORECASE) for p in pats]) for g, pats in GROUPS]


def scan(text):
    """Return a list of dicts: line, group, match, text."""
    rows = []
    for n, line in enumerate(text.splitlines(), start=1):
        for group, pats in COMPILED:
            found = []
            for p in pats:
                for m in p.finditer(line):
                    found.append(m.group(0))
            if found:
                seen = []
                for f in found:
                    if f.lower() not in [s.lower() for s in seen]:
                        seen.append(f)
                rows.append({"line": n, "group": group, "match": ", ".join(seen),
                             "text": line.strip()})
    return rows


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    path = argv[1]
    text = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    rows = scan(text)
    if "--json" in argv:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0
    if not rows:
        print("No cue wording found. Read the draft against the label anyway.")
        return 0
    for r in rows:
        print(f"line {r['line']:>3} | {r['group']:<30} | {r['match']:<28} | {r['text']}")
    print(f"\n{len(rows)} cue rows. Cues are words, not findings.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
