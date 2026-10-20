#!/usr/bin/env python3
"""Say which identifier a string holds and which VERIFY argument it belongs in.

Part of the VITAL TRUSTED skill source-assessment (task TR-8.2.1).

  python identify_source_id.py "https://doi.org/10.1000/xyz123"
  python identify_source_id.py "PMID: 12345678" --json
  echo "PMC1234567" | python identify_source_id.py -

It recognizes DOI, PMCID, PMID and http(s) URL by their shape only. It does not resolve,
fetch or check any identifier, and a match does not mean the identifier exists.
A DOI inside a doi.org link is reported as a DOI (the stable identifier), with the link
kept as a second candidate.
"""
import argparse
import json
import re
import sys

DOI = re.compile(r"\b(10\.\d{4,9}/[^\s\"<>]+)", re.IGNORECASE)
PMCID = re.compile(r"\b(PMC\d{4,10})\b", re.IGNORECASE)
PMID_LABELED = re.compile(r"\bPMID\s*[:#]?\s*(\d{1,9})\b", re.IGNORECASE)
PUBMED_URL = re.compile(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d{1,9})", re.IGNORECASE)
BARE_DIGITS = re.compile(r"^\s*(\d{1,9})\s*$")
URL = re.compile(r"\bhttps?://[^\s\"<>]+", re.IGNORECASE)


def clean_doi(doi):
    return doi.rstrip(".,;)]}")


def identify(text):
    found = []
    m = DOI.search(text)
    if m:
        found.append({"kind": "DOI", "argument": "doi", "value": clean_doi(m.group(1))})
    m = PMCID.search(text)
    if m:
        found.append({"kind": "PMCID", "argument": "pmcid", "value": m.group(1).upper()})
    m = PMID_LABELED.search(text) or PUBMED_URL.search(text) or BARE_DIGITS.match(text)
    if m:
        found.append({"kind": "PMID", "argument": "pmid", "value": m.group(1)})
    m = URL.search(text)
    if m:
        found.append({"kind": "URL", "argument": "url", "value": m.group(0).rstrip(".,;)]}")})
    notes = []
    if not found:
        notes.append("No DOI, PMID, PMCID or link found. Ask for one; a title alone cannot be qualified.")
    elif found[0]["kind"] == "URL":
        notes.append("Link only: check_currency will return \"not checked\" for it. Ask whether a DOI or PMID exists.")
    if any(f["kind"] == "PMID" for f in found) and BARE_DIGITS.match(text):
        notes.append("Bare digits read as a PMID by shape only; confirm with the person.")
    return {"input": text.strip(), "candidates": found, "use_first": found[0] if found else None, "notes": notes}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("text", help="identifier text, or - to read stdin")
    ap.add_argument("--json", action="store_true", help="print JSON")
    a = ap.parse_args()
    text = sys.stdin.read() if a.text == "-" else a.text
    r = identify(text)
    if a.json:
        print(json.dumps(r, indent=2))
        return
    if r["use_first"]:
        u = r["use_first"]
        print(f"{u['kind']}: {u['value']}  -> VERIFY argument \"{u['argument']}\"")
        for c in r["candidates"][1:]:
            print(f"  also found {c['kind']}: {c['value']} (\"{c['argument']}\")")
    for n in r["notes"]:
        print("Note: " + n)
    print("Shape only: not resolved or checked.")


if __name__ == "__main__":
    main()
