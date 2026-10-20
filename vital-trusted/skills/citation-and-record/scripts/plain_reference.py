#!/usr/bin/env python3
"""Build plain reference lines from supplied source details, for use without VERIFY.

Part of the VITAL TRUSTED skill citation-and-record (task TR-8.4.1).

  python plain_reference.py sources.json
  python plain_reference.py sources.json --json
  cat sources.json | python plain_reference.py -

Input: a JSON list of objects with any of these fields:
  authors (list or string), title, container, publisher, year, volume, issue,
  pages, doi, pmid, url, type ("article", "abstract", "web", "book", "report", ...)

Rules:
  - Only supplied values are used. A missing field is left out of the line and
    listed as missing. Nothing is filled, guessed or corrected.
  - Values are copied as given (whitespace trimmed). No capitalization or
    abbreviation is applied.
  - The lines follow no named style and are labeled "not tool-built".
"""
import argparse
import json
import sys

KNOWN = {"authors", "title", "container", "publisher", "year", "volume", "issue",
         "pages", "doi", "pmid", "url", "type"}
LABEL = "Reference lines built from the details you gave; not tool-built."


def clean(value):
    if value is None:
        return ""
    if isinstance(value, (int, float)):
        return str(value)
    if isinstance(value, str):
        return value.strip()
    return ""


def authors_text(value):
    if isinstance(value, list):
        names = [clean(a) for a in value if clean(a)]
        return ", ".join(names)
    return clean(value)


def build(src):
    a = authors_text(src.get("authors"))
    title = clean(src.get("title"))
    container = clean(src.get("container"))
    publisher = clean(src.get("publisher"))
    year = clean(src.get("year"))
    volume = clean(src.get("volume"))
    issue = clean(src.get("issue"))
    pages = clean(src.get("pages"))
    doi = clean(src.get("doi"))
    pmid = clean(src.get("pmid"))
    url = clean(src.get("url"))
    kind = clean(src.get("type")).lower() or "article"

    parts = []
    if a:
        parts.append(a.rstrip(".") + ".")
    if title:
        parts.append(title.rstrip(".") + ".")
    venue = container
    if publisher and publisher != container:
        venue = f"{venue}. {publisher}" if venue else publisher
    tail = ""
    if year:
        tail = year
    vol = volume
    if issue:
        vol = f"{vol}({issue})" if vol else f"({issue})"
    if vol:
        tail = f"{tail};{vol}" if tail else vol
    if pages:
        tail = f"{tail}:{pages}" if tail else pages
    if venue and tail:
        parts.append(f"{venue}. {tail}.")
    elif venue:
        parts.append(venue.rstrip(".") + ".")
    elif tail:
        parts.append(tail + ".")
    if doi:
        parts.append(f"doi:{doi}")
    if pmid:
        parts.append(f"PMID: {pmid}")
    if url and not doi:
        parts.append(url)
    line = " ".join(parts)

    missing = []
    for field, val in (("authors", a), ("title", title), ("year", year)):
        if not val:
            missing.append(field)
    if not (container or publisher):
        missing.append("journal, publisher or website")
    if kind == "article":
        if not volume:
            missing.append("volume")
        if not pages:
            missing.append("pages")
    if not (doi or pmid or url):
        missing.append("identifier (DOI, PMID or URL)")
    unknown = sorted(k for k in src.keys() if k not in KNOWN)
    return {"line": line, "missing": missing, "ignored_fields": unknown}


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", help="JSON file with a list of sources, or - for stdin")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    raw = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()
    try:
        data = json.loads(raw) if raw.strip() else []
    except json.JSONDecodeError as exc:
        print(f"Input is not valid JSON: {exc}", file=sys.stderr)
        return 2
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        print("Input must be a JSON list of sources.", file=sys.stderr)
        return 2
    results = [build(s) if isinstance(s, dict) else
               {"line": "", "missing": ["not a source object"], "ignored_fields": []}
               for s in data]
    if args.json:
        print(json.dumps({"label": LABEL, "sources": results}, indent=2, ensure_ascii=False))
        return 0
    if not results:
        print("No sources supplied. Nothing to build.")
        return 0
    for i, r in enumerate(results, 1):
        print(f"{i}. {r['line']}" if r["line"] else f"{i}. [no details supplied]")
    gaps = [(i, r) for i, r in enumerate(results, 1) if r["missing"] or r["ignored_fields"]]
    if gaps:
        print()
        print("Missing from what you gave me:")
        for i, r in gaps:
            if r["missing"]:
                print(f"  Source {i}: " + ", ".join(r["missing"]))
            if r["ignored_fields"]:
                print(f"  Source {i}: fields not used: " + ", ".join(r["ignored_fields"]))
    print()
    print(LABEL)
    return 0


if __name__ == "__main__":
    sys.exit(main())
