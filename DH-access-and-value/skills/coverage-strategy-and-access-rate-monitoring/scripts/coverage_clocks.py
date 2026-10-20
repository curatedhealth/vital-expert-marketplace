#!/usr/bin/env python3
"""Coverage clocks: turn library listing rows into a dated clock table.

Input: a JSON file holding a library tool response (search_listings,
find_scheme_precedents, get_reimbursement_status, get_market_matrix) or a
list of rows. Each row needs at least scheme, status, listed_on; delisted
DiGA rows may carry the deletion date in evidence_passage.

Output: one line per row with the clock that applies, the elapsed time, and
a flag. The flags restate official clocks (see references/lapse-signals.md);
they are prompts to check, never verdicts. Expiry of a German trial is not
deletion: the DiGA stays listed until BfArM decides.

Usage: python3 coverage_clocks.py rows.json [--as-of YYYY-MM-DD] [--json]
"""
import argparse
import datetime as dt
import json
import re
import sys

# Official clocks, in months, with the reference row that sources them.
CLOCKS = {
    ("DE_DIGA", "provisional"): {
        "clock": "DiGA trial listing: 12 months, one extension up to 12 more",
        "limits": [(12, "past the 12-month trial: extension or decision pending"),
                   (24, "past the 24-month legal maximum: check BfArM decision or court route")],
        "source": "lapse-signals.md L-1, L-2",
    },
    ("FR_PECAN", "covered"): {
        "clock": "PECAN: one year, not renewable; LPPR file within 6 months, LATM within 9",
        "limits": [(6, "LPPR filing deadline reached (DTx)"),
                   (9, "LATM filing deadline reached (remote monitoring)"),
                   (12, "PECAN year ended: listing, refusal or continuity period applies")],
        "source": "lapse-signals.md L-5",
    },
    ("FR_PECAN", "provisional"): None,  # filled below, same as covered
    ("UK_NICE_EVA", "conditional"): {
        "clock": "NICE early use: evidence generation about 3 years, annual reporting from 12 months",
        "limits": [(12, "annual evidence report to NICE due"),
                   (36, "evidence period ended: re-evaluation for routine use expected")],
        "source": "lapse-signals.md L-7",
    },
}
CLOCKS[("FR_PECAN", "provisional")] = CLOCKS[("FR_PECAN", "covered")]
CLOCKS[("UK_NICE_EVA", "provisional")] = CLOCKS[("UK_NICE_EVA", "conditional")]
CLOCKS[("UK_NICE_EVA", "covered")] = CLOCKS[("UK_NICE_EVA", "conditional")]

DELETED = re.compile(r"Gestrichen am (\d{2})\.(\d{2})\.(\d{4})")
LISTED = re.compile(r"Aufgenommen am (\d{2})\.(\d{2})\.(\d{4})")


def months_between(a, b):
    return (b.year - a.year) * 12 + (b.month - a.month) - (1 if b.day < a.day else 0)


def parse_date(value):
    if not value:
        return None
    return dt.date.fromisoformat(str(value)[:10])


def german_date(match):
    if not match:
        return None
    d, m, y = match.groups()
    return dt.date(int(y), int(m), int(d))


def rows_from(payload):
    if isinstance(payload, list):
        return payload
    rows = payload.get("results", [])
    out = []
    for r in rows:
        # get_market_matrix nests schemes; flatten when present
        if isinstance(r, dict) and "schemes" in r and isinstance(r["schemes"], list):
            out.extend(r["schemes"])
        else:
            out.append(r)
    return out


def assess(row, as_of):
    scheme = row.get("scheme")
    status = row.get("status")
    listed = parse_date(row.get("listed_on"))
    passage = row.get("evidence_passage") or ""
    result = {
        "product": row.get("product"),
        "scheme": scheme,
        "status": status,
        "listed_on": row.get("listed_on"),
        "clock": None,
        "months_elapsed": None,
        "flag": None,
        "source": None,
        "check": [],
    }
    if status == "delisted":
        deleted = german_date(DELETED.search(passage))
        listed_p = german_date(LISTED.search(passage)) or listed
        result["clock"] = "deleted"
        if deleted and listed_p:
            result["months_elapsed"] = months_between(listed_p, deleted)
            result["flag"] = f"deleted {deleted.isoformat()} after {result['months_elapsed']} months listed"
        else:
            result["flag"] = "deleted; deletion date not stated [GAP]"
        result["source"] = "lapse-signals.md L-3"
        return result
    spec = CLOCKS.get((scheme, status))
    if not spec:
        result["clock"] = "no official clock for this scheme and status"
        return result
    result["clock"] = spec["clock"]
    result["source"] = spec["source"]
    if not listed:
        result["flag"] = "start date not stated [GAP]"
        return result
    elapsed = months_between(listed, as_of)
    result["months_elapsed"] = elapsed
    passed = [text for limit, text in spec["limits"] if elapsed >= limit]
    result["flag"] = passed[-1] if passed else "within the first clock period"
    if row.get("ends_on") in (None, ""):
        result["check"].append("end date not stored; clock counted from listed_on")
    return result


def consistency_checks(row):
    notes = []
    passage = (row.get("evidence_passage") or "").lower()
    if row.get("scheme") == "DE_DIGA" and row.get("status") == "permanent":
        notes.append("listed_on may be the first listing date, not the date it became permanent")
    if row.get("status") == "permanent" and "vorläufig aufgenommen" in passage:
        notes.append("status says permanent but the stored passage says provisional: check the register")
    return notes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--as-of", default=dt.date.today().isoformat())
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    as_of = dt.date.fromisoformat(args.as_of)
    with open(args.path, encoding="utf-8") as fh:
        payload = json.load(fh)
    out = []
    for row in rows_from(payload):
        res = assess(row, as_of)
        res["check"].extend(consistency_checks(row))
        out.append(res)
    if args.json:
        json.dump({"as_of": as_of.isoformat(), "rows": out}, sys.stdout, ensure_ascii=False, indent=2)
        print()
        return
    print(f"As of {as_of.isoformat()}")
    print("| Product | Scheme | Status | Listed | Months | Flag | Check |")
    print("|---|---|---|---|---|---|---|")
    for r in out:
        name = (r['product'] or '').replace('|', '/')
        print(f"| {name} | {r['scheme']} | {r['status']} | {r['listed_on'] or '[GAP]'} | "
              f"{'' if r['months_elapsed'] is None else r['months_elapsed']} | {r['flag'] or ''} | "
              f"{'; '.join(r['check'])} |")


if __name__ == "__main__":
    main()
