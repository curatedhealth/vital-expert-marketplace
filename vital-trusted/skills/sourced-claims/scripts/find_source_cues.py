#!/usr/bin/env python3
"""List wording that usually marks a claim needing a source, or a citation needing work.

Part of the VITAL TRUSTED skill sourced-claims (tasks TR-5.2.1 to TR-5.2.3).

  python find_source_cues.py draft.txt
  python find_source_cues.py draft.txt --json
  cat draft.txt | python find_source_cues.py -

It finds wording, not claims, and makes no judgment. A line with no cue can still hold
a claim that needs a source; read the whole draft.
"""
import argparse
import json
import re
import sys

YEAR = re.compile(r"\b(19|20)\d{2}\b")
ID = re.compile(r"\b(doi|pmid|pubmed|nct\d|isbn)\b|10\.\d{4,}/", re.IGNORECASE)
BRACKET_SOURCE = re.compile(r"\([^)]*[A-Za-z]{3,}[^)]*\)|\[[^\]]*(source|ref|gap)[^\]]*\]", re.IGNORECASE)


def rx(words):
    return re.compile(r"\b(" + "|".join(words) + r")\b", re.IGNORECASE)


CUES = [
    ("vague authority", rx([
        r"studies (?:show|suggest|have shown|demonstrate)",
        r"research (?:shows|suggests|has shown)",
        r"evidence (?:shows|suggests)",
        r"data (?:show|suggest)",
        r"experts? (?:agree|say|recommend|believe)",
        r"(?:it is|it's) (?:well )?(?:known|established|accepted)",
        r"guidelines? recommends?",
        r"clinicians (?:agree|prefer)",
        r"physicians (?:agree|prefer)",
    ])),
    ("unnamed regulator or guidance", rx([
        r"(?:per|according to|under|in line with) (?:the )?(?:FDA|EMA|MHRA|Swissmedic|NICE|HAS|G-BA|IQWiG|WHO|ICH)(?: guidance| guidelines?| rules?)?",
        r"(?:FDA|EMA|MHRA|Swissmedic|NICE|ICH) (?:guidance|guidelines?|says|requires|recommends)",
        r"regulators? (?:require|expect|say)",
    ])),
    ("superlative or first", rx([
        r"leading", r"first", r"only", r"best", r"most (?:prescribed|effective|trusted|used)",
        r"gold standard", r"number one", r"no\. ?1", r"unrivall?ed", r"unique(?:ly)?",
        r"market leader", r"best-in-class", r"first-in-class",
    ])),
    ("undated current", rx([r"current(?:ly)?", r"latest", r"now", r"recent(?:ly)?", r"new", r"to date", r"up-to-date"])),
    ("weak source type", rx([
        r"press release", r"blog", r"news(?:letter)?", r"preprint", r"abstract", r"poster",
        r"data on file", r"internal (?:analysis|data|deck|document)", r"tweet", r"linkedin post",
        r"personal communication",
    ])),
]

AUTHOR_YEAR = re.compile(r"\b[A-Z][a-z]+(?: et al\.?)?,? (?:19|20)\d{2}\b|\b[A-Z][a-z]+ et al\.?")
BARE_DOF = re.compile(r"\bdata on file\b\s*[.)\]]?\s*$|\bdata on file\b(?![^.;]*\b(?:19|20)\d{2}\b)", re.IGNORECASE)
FIGURE = re.compile(r"\b\d+(?:\.\d+)?\s?%|\b\d+ (?:in|out of) \d+\b|\b\d+(?:\.\d+)?-fold\b", re.IGNORECASE)


def scan_line(line):
    hits = []
    for group, pattern in CUES:
        for m in pattern.finditer(line):
            if group == "undated current" and YEAR.search(line):
                continue
            hits.append((group, m.group(0)))
    for m in AUTHOR_YEAR.finditer(line):
        if not ID.search(line):
            hits.append(("incomplete citation", m.group(0)))
    if BARE_DOF.search(line):
        hits.append(("incomplete citation", "data on file (no name or date)"))
    for m in FIGURE.finditer(line):
        if not BRACKET_SOURCE.search(line):
            hits.append(("figure", m.group(0)))
    # de-duplicate, keep order
    seen, out = set(), []
    for h in hits:
        key = (h[0], h[1].lower())
        if key not in seen:
            seen.add(key)
            out.append(h)
    return out


def scan(text):
    rows = []
    for i, line in enumerate(text.splitlines(), start=1):
        for group, words in scan_line(line):
            rows.append({"line": i, "group": group, "match": words, "text": line.strip()})
    return rows


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("path", help="text file, or - for stdin")
    p.add_argument("--json", action="store_true", help="print JSON")
    a = p.parse_args(argv)
    text = sys.stdin.read() if a.path == "-" else open(a.path, encoding="utf-8").read()
    rows = scan(text)
    if a.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0
    if not rows:
        print("No cues found. Read the draft anyway: claims can need a source without any cue word.")
        return 0
    for r in rows:
        print(f"line {r['line']:>3}  {r['group']:<30} {r['match']!r:<28} | {r['text'][:90]}")
    counts = {}
    for r in rows:
        counts[r["group"]] = counts.get(r["group"], 0) + 1
    print()
    print("Counts: " + ", ".join(f"{g} {n}" for g, n in counts.items()))
    print("This lists wording only. It does not decide whether a claim is sourced.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
