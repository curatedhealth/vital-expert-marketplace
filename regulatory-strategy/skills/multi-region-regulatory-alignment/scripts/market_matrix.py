#!/usr/bin/env python3
"""Market matrix: one row per jurisdiction from saved library output.

Why this exists: regulatory-dh.get_market_status returns one row per stored
record, and each row says "false" for every jurisdiction that record is not
in. A product with a US record and an EU record therefore comes back as two
rows that contradict each other (US true / EU false, then US false / EU
true), and the exhibit shows only the first. "false" also means "no record in
the library's copy", never "not authorized". This script merges the rows,
adds what search_devices stores per jurisdiction (class, regime, pathway,
identifiers, latest decision date), and classifies every jurisdiction with
the gap classes in references/gap-rules.md.

Inputs (any combination, JSON as saved from the library):
  --search FILE        search_devices output (results[] rows)
  --status FILE        get_market_status output (results[] rows)
  --jurisdictions FILE list_jurisdictions output (to tell "store holds no
                       data for this register" from "record not found")
  --product TEXT       keep rows whose product name contains TEXT (case-insensitive)
  --markets LIST       comma list of the person's markets, e.g. US,EU,UK,CH,CA,AU,BR,JP
  --json               print JSON instead of a Markdown table

Usage:
  python3 market_matrix.py --search s.json --status m.json --jurisdictions j.json \
      --product "e-ASPECTS" --markets US,EU,UK,CH,CA,AU
"""
import argparse
import json
import sys

# Market code used by the person -> code used by the library.
ALIASES = {"GB": "UK", "UK": "UK", "EU": "EU", "US": "US", "CH": "CH", "CA": "CA",
           "AU": "AU", "BR": "BR", "JP": "JP", "TW": "TW", "SG": "SG", "KR": "KR", "CN": "CN"}


def load(path):
    if not path:
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def rows(obj):
    if obj is None:
        return []
    if isinstance(obj, list):
        return obj
    return obj.get("results", []) or []


def store_state(jur_obj):
    """Map jurisdiction -> ('loaded', count) | ('not loaded', reason)."""
    state = {}
    if not jur_obj:
        return state
    for r in jur_obj.get("results", []):
        code = r.get("jurisdiction")
        n = r.get("authorizations") or 0
        if n > 0:
            state[code] = ("loaded", n, r.get("last_load"), r.get("scope", ""))
        else:
            state[code] = ("not loaded", 0, r.get("last_load"), r.get("scope", ""))
    for r in jur_obj.get("closed", []):
        for code in str(r.get("code", "")).split("/"):
            state.setdefault(code, ("not loaded", 0, None, r.get("reason", "")))
    return state


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--search")
    ap.add_argument("--status")
    ap.add_argument("--jurisdictions")
    ap.add_argument("--product", default="")
    ap.add_argument("--markets", default="US,EU,UK,CH")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    needle = a.product.lower()
    search = [r for r in rows(load(a.search))
              if needle in str(r.get("product", "")).lower()]
    status = [r for r in rows(load(a.status))
              if needle in str(r.get("product", "")).lower()]
    state = store_state(load(a.jurisdictions))

    # Merge get_market_status rows: any true wins; "false" is "not found in the store".
    merged = {}
    for r in status:
        for jur, val in (r.get("authorized") or {}).items():
            prev = merged.get(jur)
            if val is True or prev is True:
                merged[jur] = True
            elif val == "[GAP]":
                merged.setdefault(jur, "[GAP]")
            else:
                merged.setdefault(jur, False)
    contradictions = []
    if len(status) > 1:
        for jur in merged:
            vals = {json.dumps((r.get("authorized") or {}).get(jur)) for r in status}
            if len(vals) > 1:
                contradictions.append(jur)

    out = []
    for m in [x.strip().upper() for x in a.markets.split(",") if x.strip()]:
        jur = ALIASES.get(m, m)
        recs = [r for r in search if r.get("jurisdiction") == jur]
        st = state.get(jur)
        row = {"market": m, "library_code": jur}
        if recs:
            classes = sorted({str(r.get("risk_class")) for r in recs})
            regimes = sorted({str(r.get("regime")) for r in recs})
            pathways = sorted({str(r.get("pathway")) for r in recs})
            dates = sorted(d for d in (r.get("decision_date") for r in recs) if d)
            ids = []
            for r in recs:
                for k, v in (r.get("identifiers") or {}).items():
                    if k != "EMDN":
                        ids.extend(v)
            row.update({
                "gap_class": "Found",
                "records": len(recs),
                "class_as_recorded": classes,
                "regime": regimes,
                "pathway": pathways,
                "latest_decision_date": dates[-1] if dates else "[GAP] not stored",
                "identifiers": ids,
                "source": sorted({r.get("source_url") for r in recs}),
                "retrieved": sorted({str(r.get("retrieved_at"))[:10] for r in recs}),
            })
            if len(classes) > 1:
                row["note"] = ("More than one class recorded in this jurisdiction: "
                               "read each record (regime, identifier) before comparing.")
        elif merged.get(jur) is True:
            row.update({"gap_class": "Found (status only)",
                        "note": "get_market_status says a record exists; search_devices row not in this file."})
        elif jur == "CA" and st and st[0] == "loaded":
            row.update({"gap_class": "Register loaded, not searchable by product",
                        "note": f"The library holds {st[1]} Health Canada MDALL rows (last load {st[2]}), "
                                "but search_devices cannot reach them (no CA in its jurisdiction list; "
                                "is_software is null). Check MDALL directly."})
        elif st and st[0] == "loaded":
            row.update({"gap_class": "Register loaded, product not found",
                        "note": f"Not in the library's copy ({st[1]} records, last load {st[2]}). "
                                "Not a statement that it is unauthorized; check the regulator."})
        elif st:
            row.update({"gap_class": "Register not loaded",
                        "note": f"The library holds no records for this register: {st[3]}".strip()})
        else:
            row.update({"gap_class": "Register not served",
                        "note": "The library does not serve this jurisdiction; check the regulator."})
        out.append(row)

    result = {"product_filter": a.product, "matrix": out,
              "get_market_status_rows": len(status),
              "get_market_status_contradictions": contradictions}

    if a.json:
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        print()
        return

    print(f"Market matrix for '{a.product or 'all rows'}'")
    print()
    print("| Market | Library result | Class as recorded | Regime / pathway | Latest decision | Identifiers | Source, retrieved |")
    print("|---|---|---|---|---|---|---|")
    for r in out:
        if r["gap_class"] == "Found":
            print(f"| {r['market']} | Found ({r['records']} records) | {', '.join(r['class_as_recorded'])} | "
                  f"{', '.join(r['regime'])} / {', '.join(r['pathway'])} | {r['latest_decision_date']} | "
                  f"{', '.join(r['identifiers'][:4])}{' ...' if len(r['identifiers']) > 4 else ''} | "
                  f"{'; '.join(r['source'][:2])} ({', '.join(r['retrieved'])}) |")
        else:
            print(f"| {r['market']} | {r['gap_class']} | | | | | {r.get('note', '')} |")
    for r in out:
        if r.get("note") and r["gap_class"] == "Found":
            print(f"\nNote ({r['market']}): {r['note']}")
    if contradictions:
        print(f"\nget_market_status returned {len(status)} rows that disagree on: "
              f"{', '.join(contradictions)}. Merged as 'any record found'; "
              "a 'false' means no record in the library's copy, not 'not authorized'.")


if __name__ == "__main__":
    main()
