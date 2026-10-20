#!/usr/bin/env python3
"""Classify each scheme's result for one product, using library output.

Usage:
  python classify_gaps.py SCHEMES.json STATUS.json

SCHEMES.json  the JSON returned by market-access-dh.list_schemes
STATUS.json   the JSON returned by market-access-dh.generate_report (format json
              or markdown; the "brief" object is read) or get_market_matrix

Prints a markdown table: scheme, class, wording, next step.
Classes follow references/gap-rules.md. Standard library only.
"""
import json
import sys

GAP = "[GAP]"


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def scheme_rows(schemes_json):
    return {r["code"]: r for r in schemes_json.get("results", [])}


def status_rows(status_json):
    """Return {scheme: row} from a generate_report brief or a market matrix."""
    rows = {}
    for result in status_json.get("results", []):
        brief = result.get("brief")
        if brief:
            for r in brief.get("current_status", []):
                rows[r["scheme"]] = r
        elif "scheme" in result:
            rows[result["scheme"]] = result
    return rows


def classify(scheme, meta, row):
    count = (meta or {}).get("listing_count", 0) or 0
    posture = (meta or {}).get("posture", "unknown")
    loaded = (meta or {}).get("last_load") or "never"
    status = (row or {}).get("status")
    if status and status != GAP:
        missing = [k for k in ("listed_on", "price") if (row or {}).get(k) in (None, GAP)]
        if missing:
            return ("field missing", f"Found ({status}); not stated: {', '.join(missing)}.",
                    "Check the authority's page for those fields.")
        return ("found", f"Found ({status}).", "None.")
    if count > 0:
        note = " The library's copy may be incomplete." if posture == "partial" else ""
        return ("covered, product absent",
                f"Not in the library's copy ({count} listings, loaded {loaded}, posture {posture}).{note}",
                "Check the authority directly before concluding.")
    reason = (meta or {}).get("posture_reason") or "no listings loaded"
    return ("not covered", f"The library holds no listings for this scheme: {reason[:160]}",
            "The library cannot answer here; check the authority.")


def main(argv):
    if len(argv) != 3:
        sys.exit(__doc__)
    schemes = scheme_rows(load(argv[1]))
    statuses = status_rows(load(argv[2]))
    print("| Scheme | Class | Wording | Next step |")
    print("|---|---|---|---|")
    for code in schemes:
        cls, wording, step = classify(code, schemes.get(code), statuses.get(code))
        print(f"| {code} | {cls} | {wording.replace('|', '/')} | {step} |")


if __name__ == "__main__":
    main(sys.argv)
