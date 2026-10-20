#!/usr/bin/env python3
"""Cue scan of a draft for market statements and personal details in the output.

Part of the VITAL TRUSTED skill market-rules-and-data (tasks TR-2.2.2 and TR-2.2.3).

  python scan_output.py draft.txt --statements --market UK
  python scan_output.py draft.txt --data
  python scan_output.py draft.txt --statements --data --market CH --json
  cat draft.txt | python scan_output.py - --data --small-count 10

--statements lists the elements usually expected for the market (UK, EU, CH, US,
unknown) and the lines where a cue word was found. --data lists formats that can point
to a person, masked, and small counts next to words such as "patients" or "cases".

It finds words, not meaning. A cue found does not show an element is there or correct;
"no cue found" is a place to look, not a finding. A clean data scan does not make a
text anonymous. The review process and the privacy function decide.
"""
import argparse
import json
import re
import sys

# Cue words per element. Elements per market follow references/rules.md.
CUES = {
    "prescribing information or where to find it": re.compile(
        r"prescribing information|summary of product characteristics|\bSmPC\b|\bPI\b"
        r"|brief summary|Fachinformation|Arzneimittelinformation|information professionnelle"
        r"|swissmedicinfo|product information", re.I),
    "date of preparation or last revision": re.compile(
        r"date of preparation|prepared(?: on)?\s*:|date (?:created|of revision)|last revised"
        r"|revised\s*:|Stand\s*:|date de pr[ée]paration", re.I),
    "side-effect reporting statement": re.compile(
        r"adverse events? should be reported|report(?:ing)? (?:of )?(?:suspected )?(?:side effects|adverse)"
        r"|yellow card|medwatch|FDA-1088|Nebenwirkungen (?:melden|meldung)|pharmacovigilance", re.I),
    "audience statement": re.compile(
        r"for (?:uk |us |swiss )?(?:healthcare|health care|medical) professionals(?: only)?"
        r"|intended for (?:healthcare|health care|medical) professionals|nur f[üu]r fachpersonen"
        r"|r[ée]serv[ée] aux professionnels", re.I),
    "job code or reference": re.compile(
        r"job (?:code|number|bag)|material (?:code|number)|reference (?:no\.?|number)|\bref\.?\s*:", re.I),
    "supply or dispensing classification": re.compile(
        r"\bPOM\b|prescription only|\bRx only\b|Abgabekategorie|cat[ée]gorie de remise|supply classification"
        r"|legal classification|dispensing category", re.I),
    "authorisation holder name and address": re.compile(
        r"marketing authori[sz]ation holder|Zulassungsinhaberin|titulaire de l'autorisation", re.I),
    "black triangle": re.compile(r"▼|black triangle|additional monitoring", re.I),
    "non-proprietary name": re.compile(r"\((?:[a-z]+(?:mab|nib|stat|pril|sartan|vir|tide|cept|ase|ide|ine|ol))\)", re.I),
}

MARKETS = {
    "UK": ["prescribing information or where to find it", "non-proprietary name",
           "date of preparation or last revision", "side-effect reporting statement",
           "black triangle", "audience statement", "job code or reference"],
    "EU": ["prescribing information or where to find it", "date of preparation or last revision",
           "supply or dispensing classification", "audience statement", "job code or reference"],
    "CH": ["prescribing information or where to find it", "authorisation holder name and address",
           "supply or dispensing classification", "audience statement", "job code or reference"],
    "US": ["prescribing information or where to find it", "audience statement", "job code or reference"],
    "unknown": ["job code or reference", "date of preparation or last revision"],
}

NOTES = {
    "UK": "UK list from the ABPI Code 2024 as read; black triangle only when required.",
    "EU": "EU list from Directive 2001/83/EC and the EFPIA Code as read; national codes add more.",
    "CH": "Swiss list from the advertising ordinance (AWV) Article 6 as read; the full item list is in references/rules.md.",
    "US": "US list is partial: advertisement rules as read; emails and brochures not read.",
    "unknown": "Market not given: only company-system elements listed. Ask the market.",
}

# Formats that can point to a person in an output.
DATA = {
    "title followed by a name": re.compile(
        r"\b(?:Mr|Mrs|Ms|Miss|Mx|Dr|Prof|Herr|Frau|Mme)\.?\s+[A-Z][a-zA-Z'-]+(?:\s+[A-Z][a-zA-Z'-]+)?"),
    "email address": re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b"),
    "phone number": re.compile(r"(?<![\w.])\+?\d{1,3}[\s.-]\d{2,4}[\s.-]\d{2,4}[\s.-]\d{2,4}(?![\w.])"),
    "date": re.compile(
        r"\b(?:\d{1,2}[./-]\d{1,2}[./-]\d{2,4}|\d{4}-\d{2}-\d{2}"
        r"|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{4})\b", re.I),
    "age": re.compile(r"\b(?:aged?\s+\d{1,3}|\d{1,3}[- ]?(?:year[s]?[- ]old|y/?o|yrs?\b))", re.I),
    "record-like number": re.compile(r"\b(?:MRN|patient|subject|pt|record|case)\s*(?:no\.?|#|id)?\s*[:#]?\s*[A-Z]*\d[A-Z0-9-]{2,}\b", re.I),
}
PEOPLE = r"(?:patients?|cases?|people|persons?|respondents?|participants?|women|men|children|subjects?)"
SMALL = re.compile(
    rf"\b(\d{{1,3}})\s+(?:of\s+(?:the\s+)?\d{{1,6}}\s+)?(?:\w+\s+)?{PEOPLE}\b|\bn\s*=\s*(\d{{1,3}})\b", re.I)

DATA_NOTE = ("Format scan only. Names without a title, villages, jobs and patient stories "
             "are not found. A clean scan does not make a text anonymous; the data privacy "
             "function decides.")
SMALL_NOTE = ("Small-count cutoff {n} is a listing cutoff for reading, not a privacy "
              "threshold. Your data privacy function sets that.")


def mask(s):
    """Keep the first character of each run of letters or digits; mask the rest."""
    return re.sub(r"(?<=[A-Za-z0-9])[A-Za-z0-9]", "*", s)


def scan_statements(text, market):
    lines = text.splitlines()
    out = []
    for element in MARKETS[market]:
        rx = CUES[element]
        hits = [n for n, line in enumerate(lines, start=1) if rx.search(line)]
        out.append({"element": element, "cue_lines": hits})
    return out


def scan_data(text, small_count):
    hits = []
    for n, line in enumerate(text.splitlines(), start=1):
        taken = []
        for kind, rx in DATA.items():
            for m in rx.finditer(line):
                a, b = m.span()
                if any(x < b and a < y for x, y in taken):
                    continue
                taken.append((a, b))
                hits.append({"line": n, "kind": kind, "snippet": mask(m.group(0).strip())})
        for m in SMALL.finditer(line):
            val = int(m.group(1) or m.group(2))
            if 0 < val <= small_count:
                hits.append({"line": n, "kind": "small count", "snippet": m.group(0).strip()})
    return hits


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", help="text file, or - for standard input")
    ap.add_argument("--statements", action="store_true")
    ap.add_argument("--data", action="store_true")
    ap.add_argument("--market", default="unknown", choices=sorted(MARKETS))
    ap.add_argument("--small-count", type=int, default=10)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    if not (args.statements or args.data):
        ap.error("choose --statements, --data or both")
    if args.path == "-":
        text = sys.stdin.read()
    else:
        with open(args.path, encoding="utf-8") as f:
            text = f.read()

    result = {}
    if args.statements:
        result["statements"] = {"market": args.market, "elements": scan_statements(text, args.market),
                                "note": NOTES[args.market]}
    if args.data:
        result["data"] = {"hits": scan_data(text, args.small_count), "note": DATA_NOTE,
                          "small_count_note": SMALL_NOTE.format(n=args.small_count)}

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0

    if "statements" in result:
        s = result["statements"]
        print(f"Elements usually expected, market {s['market']} (cue words only)")
        for e in s["elements"]:
            where = ("cue on line " + ", ".join(map(str, e["cue_lines"]))) if e["cue_lines"] else "no cue found"
            print(f"  {e['element']:<45} {where}")
        print("  " + s["note"])
        print("  A cue is not the element; 'no cue found' is a place to look.\n")
    if "data" in result:
        d = result["data"]
        print("Details that could point to a person (masked)")
        if not d["hits"]:
            print("  none of the scanned formats found")
        for h in d["hits"]:
            print(f"  line {h['line']:>4}  {h['kind']:<26} {h['snippet']}")
        print("  " + d["note"])
        print("  " + d["small_count_note"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
