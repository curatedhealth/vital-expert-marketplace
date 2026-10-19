#!/usr/bin/env python3
"""Precedent table: turn saved regulatory-dh.search_devices output into a dated table.

Input: a JSON file holding a search_devices (or get_authorization) response, or a list
of rows. Each row needs product, manufacturer, jurisdiction, pathway, decision_date;
submission_date, product_code, predicate_references, identifiers and source_url are
used when present.

Output: one line per row, newest decision first, with calendar days between the stored
submission and decision dates, plus a summary per jurisdiction and pathway. These are
days between two stored dates, not MDUFA "FDA days" (references/tools.md). EU rows have
no decision date in the library, so their days are not computable. The records carry no
AI or PCCP field; the table says so rather than guessing.

Usage: python3 precedent_table.py rows.json [--product-code QAS] [--json]
"""
import argparse
import datetime as dt
import json
import statistics
import sys


def load_rows(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    for key in ("results", "rows"):
        if isinstance(data.get(key), list):
            return data[key]
    sys.exit("No rows found: expected a list or a 'results' key.")


def parse(d):
    if not d:
        return None
    try:
        return dt.date.fromisoformat(str(d)[:10])
    except ValueError:
        return None


def ident(row):
    ids = row.get("identifiers") or {}
    for key in ("FDA_SUBMISSION", "BASIC_UDI_DI"):
        if ids.get(key):
            return ids[key][0]
    return ""


def build(rows, product_code=None):
    out = []
    for r in rows:
        if product_code and r.get("product_code") != product_code:
            continue
        sub, dec = parse(r.get("submission_date")), parse(r.get("decision_date"))
        days = (dec - sub).days if sub and dec else None
        out.append({
            "decision_date": dec.isoformat() if dec else "[GAP] not stored",
            "product": r.get("product", ""),
            "manufacturer": r.get("manufacturer", ""),
            "jurisdiction": r.get("jurisdiction", ""),
            "pathway": r.get("pathway", ""),
            "risk_class": r.get("risk_class", ""),
            "product_code": r.get("product_code", ""),
            "identifier": ident(r),
            "days_submission_to_decision": days,
            "predicates": ", ".join(r.get("predicate_references") or []) or "none stated",
            "source_url": r.get("source_url", ""),
        })
    out.sort(key=lambda x: x["decision_date"], reverse=True)
    return out


def summary(table):
    groups = {}
    for t in table:
        groups.setdefault((t["jurisdiction"], t["pathway"]), []).append(t)
    lines = []
    for (j, p), items in sorted(groups.items()):
        days = [t["days_submission_to_decision"] for t in items if t["days_submission_to_decision"] is not None]
        if days:
            lines.append(f"{j} {p}: {len(items)} rows; days between stored dates: median {statistics.median(days):g}, min {min(days)}, max {max(days)} (n {len(days)})")
        else:
            lines.append(f"{j} {p}: {len(items)} rows; days not computable (no stored dates)")
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--product-code")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    table = build(load_rows(a.file), a.product_code)
    if a.json:
        print(json.dumps({"rows": table, "summary": summary(table)}, indent=1))
        return
    print("| Decision date | Device | Manufacturer | Jur. | Route | Class | Code | Identifier | Days sub. to dec. | Predicates |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for t in table:
        d = t["days_submission_to_decision"]
        print(f"| {t['decision_date']} | {t['product'][:60]} | {t['manufacturer']} | {t['jurisdiction']} | {t['pathway']} | {t['risk_class']} | {t['product_code']} | {t['identifier']} | {d if d is not None else '[GAP]'} | {t['predicates']} |")
    print()
    for line in summary(table):
        print("- " + line)
    print("- Described by their records. The records state no AI or PCCP status; check FDA's AI-enabled device list or the decision summary.")
    print("- Days are calendar days between stored submission and decision dates, not MDUFA FDA days.")


if __name__ == "__main__":
    main()
