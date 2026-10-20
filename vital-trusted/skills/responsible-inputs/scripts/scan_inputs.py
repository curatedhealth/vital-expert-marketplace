#!/usr/bin/env python3
"""Pattern scan of a text before it is used with an AI assistant.

Part of the VITAL TRUSTED skill responsible-inputs (tasks TR-6.1.1 and TR-6.1.2).

  python scan_inputs.py extract.txt
  python scan_inputs.py extract.txt --json
  cat extract.txt | python scan_inputs.py -

Finds identifier formats (emails, phones, dates, ages over 89, URLs, IP addresses,
ID-like numbers, titles followed by a name), confidentiality markers and copyright or
license markers. Prints counts and masked snippets; never prints a full identifier.

It finds formats, not meaning. A clean scan does not mean the text is anonymous,
de-identified or cleared to share. That decision belongs to the company's policy.
"""
import argparse
import json
import re
import sys

IDENTIFIERS = {
    "email address": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
    "URL": re.compile(r"\b(?:https?://|www\.)\S+", re.IGNORECASE),
    "IP address": re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b"),
    "phone number": re.compile(
        r"(?<![\w.])(?:\+\d{1,3}[\s.-]?)?(?:\(\d{1,4}\)[\s.-]?)?\d{2,4}[\s.-]\d{2,4}[\s.-]\d{2,4}(?:[\s.-]\d{2,4})?(?![\w.])"
    ),
    "date": re.compile(
        r"\b(?:\d{1,2}[./-]\d{1,2}[./-]\d{2,4}|\d{4}-\d{2}-\d{2}"
        r"|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{4}"
        r"|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2},?\s+\d{4})\b",
        re.IGNORECASE,
    ),
    "age over 89": re.compile(
        r"\b(?:9\d|1[01]\d)\s*(?:-?\s*year[s]?[- ]old|y/?o|yrs?\b|years of age)|\baged?\s+(?:9\d|1[01]\d)\b",
        re.IGNORECASE,
    ),
    "ID-like number or subject code": re.compile(
        r"\b(?:(?:MRN|patient|subject|pt|record|case|ID|no\.?)\s*[:#]?\s*[A-Z0-9-]*\d[A-Z0-9-]{2,}"
        r"|\d{3,4}-\d{3,4}(?:-\d{2,4})?|\d{7,})\b",
        re.IGNORECASE,
    ),
    "title followed by a name": re.compile(
        r"\b(?:Mr|Mrs|Ms|Miss|Mx|Dr|Prof|Herr|Frau|Mme|M)\.?\s+[A-Z][a-zA-Z'-]+(?:\s+[A-Z][a-zA-Z'-]+)?"
    ),
}

CONFIDENTIALITY = re.compile(
    r"\b(?:strictly\s+)?confidential\b|\bunpublished\b|\bdraft\b|\binternal use only\b"
    r"|\bnot for (?:distribution|circulation)\b|\bembargo(?:ed)?\b|\btop-?line\b"
    r"|\bclinical study report\b|\bCSR\b|\bproprietary\b|\bunder NDA\b|\bprivileged\b",
    re.IGNORECASE,
)

COPYRIGHT = re.compile(
    r"©|\(c\)\s*\d{4}|\bcopyright\b|\ball rights reserved\b|\blicen[cs]ed to\b"
    r"|\breprinted with permission\b|\bdoi:\s*10\.\d{4,}|\b10\.\d{4,9}/\S+",
    re.IGNORECASE,
)

NOTE = ("Pattern scan only. It finds formats, not meaning: names without a title, rare "
        "conditions, a patient's story or a small place are not found. A clean scan does "
        "not make a text anonymous or cleared to share.")


def mask(s):
    """Keep the first character of each run of letters or digits; mask the rest."""
    return re.sub(r"(?<=[A-Za-z0-9])[A-Za-z0-9]", "*", s)


def scan(text):
    hits = []
    for n, line in enumerate(text.splitlines(), start=1):
        taken = []
        for label, rx in IDENTIFIERS.items():
            for m in rx.finditer(line):
                span = m.span()
                if any(a < span[1] and span[0] < b for a, b in taken):
                    continue  # do not count the same characters twice
                taken.append(span)
                hits.append({"line": n, "category": "identifier", "kind": label,
                             "snippet": mask(m.group(0).strip())})
        for m in CONFIDENTIALITY.finditer(line):
            hits.append({"line": n, "category": "confidentiality marker",
                         "kind": m.group(0).lower(), "snippet": m.group(0)})
        for m in COPYRIGHT.finditer(line):
            hits.append({"line": n, "category": "copyright or license marker",
                         "kind": m.group(0).lower(), "snippet": m.group(0)})
    return hits


def summarize(hits):
    counts = {}
    for h in hits:
        key = (h["category"], h["kind"] if h["category"] == "identifier" else "")
        counts[key] = counts.get(key, 0) + 1
    return counts


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", help="text file, or - for standard input")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    hits = scan(text)
    counts = summarize(hits)
    if args.json:
        out = {"hits": hits,
               "counts": [{"category": c, "kind": k, "n": n} for (c, k), n in counts.items()],
               "note": NOTE}
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return
    if not hits:
        print("No identifier formats or markers found.")
    else:
        print("Counts")
        for (c, k), n in sorted(counts.items()):
            print(f"  {c}{' · ' + k if k else ''}: {n}")
        print("\nHits (masked)")
        for h in hits:
            print(f"  line {h['line']:>4}  {h['category']:<28} {h['kind']:<32} {h['snippet']}")
    print("\n" + NOTE)


if __name__ == "__main__":
    main()
