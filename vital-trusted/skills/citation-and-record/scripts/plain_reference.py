#!/usr/bin/env python3
"""Build plain reference lines from supplied source details.

Part of the VITAL TRUSTED skill citation-and-record (task TR-8.4.1).

  python plain_reference.py sources.json
  python plain_reference.py sources.json --json
  cat sources.json | python plain_reference.py -

Input: a JSON list of objects with any of these fields:
  authors (list or string), title, container, publisher, year, date, volume,
  issue, pages, version (or revision), published_online, doi, pmid, url,
  presenter (or presented_by),
  type ("article", "abstract", "poster", "guideline", "web", "book", "report",
  "label", "smpc", ...)

  version: a label's revision or a document's version, as given ("revision April
  2026", "version 3.0"). published_online: the online publication date, as given
  ("3 March 2026"); the line reads "Published online <date>.". date: a full date
  as given, used where no year was given.

Rules:
  - Only supplied values are used. A missing field is left out of the line and
    listed as missing. Nothing is filled, guessed or corrected.
  - Values are copied as given (whitespace trimmed). No abbreviation is applied;
    only the first letter of a kind or version that opens a sentence is capitalized.
  - A year that was supplied in any form (year, date, version or published_online)
    is never listed as missing.
  - The source kind (type) is kept in the line when it is not a journal article,
    a web page or a book, for example "Poster", "Fact sheet", "Label", "Press
    release". It is copied as given, with only its first letter capitalized, and
    left out when the venue or title already names it.
  - Labels, fact sheets, press releases and similar company documents have a
    corporate author or none, so missing authors are not listed for them.
  - A guideline, position or consensus statement from a society or agency names
    its issuer as author, so no journal, publisher or website is asked for when an
    author is given. Labels, SmPCs and similar documents are not asked for one either.
  - Labels, SmPCs, prescribing information and leaflets carry no DOI or PMID, so
    no identifier is listed as missing for them.
  - A presenter (a poster or talk) is shown as "Presented by <name>." and never as
    the author. Missing authors are still listed: the presenter is not always one.
  - The lines follow no named style and are labeled "not tool-checked".
"""
import argparse
import json
import re
import sys

KNOWN = {"authors", "title", "container", "publisher", "year", "date", "volume", "issue",
         "pages", "version", "revision", "published_online", "doi", "pmid", "url", "type",
         "presenter", "presented_by"}
YEAR_IN_TEXT = re.compile(r"\b(?:19|20)\d{2}\b")
LABEL = "Reference lines built from the details you gave; not tool-checked."
# Kinds whose name is not added to the line.
KIND_NOT_SHOWN = {"article", "journal article", "web", "website", "web page", "book"}
# Company or authority documents: corporate author or none, so authors are not asked for.
CORPORATE_KINDS = {"label", "approved label", "fact sheet", "press release", "smpc",
                   "summary of product characteristics", "prescribing information",
                   "instructions for use", "ifu", "brochure", "data on file",
                   "package leaflet", "patient leaflet"}
# Documents issued by a society, agency or company: the issuer is the author, no venue asked for.
ISSUED_KINDS = {"guideline", "treatment guideline", "clinical guideline", "guidance",
                "position statement", "consensus statement", "recommendation",
                "recommendations", "statement"}
# Documents that carry no DOI or PMID: no identifier is asked for.
NO_ID_KINDS = {"label", "approved label", "smpc", "summary of product characteristics",
               "prescribing information", "package leaflet", "patient leaflet",
               "instructions for use", "ifu", "data on file"}


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


def authors_unreadable(value):
    """True when authors were supplied in a form other than text or a list of text."""
    if value is None or isinstance(value, str):
        return False
    if isinstance(value, list):
        return any(not isinstance(item, str) for item in value)
    return True


def sentence(value):
    """Copy a value as given, first letter capitalized, ending with one full stop."""
    value = value.rstrip(".")
    return value[0].upper() + value[1:] + "." if value else ""


def build(src):
    bad_authors = authors_unreadable(src.get("authors"))
    a = "" if bad_authors else authors_text(src.get("authors"))
    title = clean(src.get("title"))
    container = clean(src.get("container"))
    publisher = clean(src.get("publisher"))
    year = clean(src.get("year"))
    date = clean(src.get("date"))
    version = clean(src.get("version")) or clean(src.get("revision"))
    online = clean(src.get("published_online"))
    volume = clean(src.get("volume"))
    issue = clean(src.get("issue"))
    pages = clean(src.get("pages"))
    doi = clean(src.get("doi"))
    pmid = clean(src.get("pmid"))
    url = clean(src.get("url"))
    kind_given = clean(src.get("type"))
    presenter = clean(src.get("presenter")) or clean(src.get("presented_by"))
    kind = kind_given.lower() or "article"

    parts = []
    if a:
        parts.append(a.rstrip(".") + ".")
    if title:
        parts.append(title.rstrip(".") + ".")
    venue = container
    if publisher and publisher != container:
        venue = f"{venue}. {publisher}" if venue else publisher
    tail = ""
    if year or date:
        tail = year or date
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
    if (kind_given and kind not in KIND_NOT_SHOWN
            and kind not in f"{title} {container} {publisher}".lower()):
        parts.append(sentence(kind_given))
    if presenter:
        parts.append("Presented by " + presenter.rstrip(".") + ".")
    if version:
        parts.append(sentence(version))
    if online:
        parts.append(sentence("published online " + online))
    if doi:
        parts.append(f"doi:{doi}")
    if pmid:
        parts.append(f"PMID: {pmid}")
    if url and not doi:
        parts.append(url)
    line = " ".join(parts)

    missing = []
    if bad_authors:
        missing.append("authors not read: they were not given as plain text, so none are "
                       "shown; give each name as text")
    year_given = year or date or YEAR_IN_TEXT.search(f"{version} {online}")
    for field, val in (("authors", a), ("title", title), ("year", year_given)):
        if field == "authors" and kind in CORPORATE_KINDS:
            continue
        if not val and not (field == "authors" and bad_authors):
            missing.append(field)
    issued = kind in ISSUED_KINDS and a
    if not (container or publisher or issued or kind in CORPORATE_KINDS):
        missing.append("journal, publisher or website")
    if kind == "article":
        if not volume:
            missing.append("volume")
        if not pages:
            missing.append("pages")
    if not (doi or pmid or url or kind in NO_ID_KINDS):
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
