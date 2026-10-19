#!/usr/bin/env python3
"""Price facts: turn saved library rows into a sourced price-fact table.

What it does
  US codes (US_CMS_RPM, US_CMS_DMHT): reads the stated national amount, relative value
  units (RVU) and conversion factor from each row's evidence_passage, recomputes
  RVU x conversion factor, and flags where the stated amount does not match, where the
  price field is empty although the passage states an amount, and where a code is
  contractor priced (no national amount).
  DiGA rows (any DE_DIGA list): lists each comparator's stored price with its status and
  months since listing, and says which price rule applies by time since listing
  (manufacturer price in year one, references/price-rules.md rows DE7 and DE9; negotiated
  or arbitrated amount after that, DE1 and DE5). The library does not say which kind of
  price the stored figure is, nor its prescription period: both stay [GAP].
  Summary statistics (count, minimum, median, maximum) are of the comparators' stored
  prices only.

What it never does
  It never computes, proposes or ranks a price for the person's product.

Input
  A JSON file shaped like examples/library_codes_and_prices_2026-10-19.json: top-level keys
  are lists of rows with identifier, status, listed_on, price, currency, evidence_passage.
  Keys starting with "_" and non-list values are skipped.

Usage
  python3 price_facts.py FILE.json [--as-of YYYY-MM-DD] [--json]
"""
import argparse
import datetime as dt
import json
import re
import statistics

AMOUNT_CF_RVU = re.compile(
    r"\$(?P<amount>[0-9]+\.[0-9]{2}) at the non-QP conversion factor \$(?P<cf>[0-9.]+) \(total RVU (?P<rvu>[0-9.]+)\)")
NONFAC = re.compile(
    r"Non-facility \$(?P<nf>[0-9.]+) and facility \$(?P<f>[0-9.]+) at the non-QP conversion factor \$(?P<cf>[0-9.]+) "
    r"\(non-facility RVU (?P<nfr>[0-9.]+), facility RVU (?P<fr>[0-9.]+)\)")


def months_between(start, end):
    return (end.year - start.year) * 12 + (end.month - start.month) - (1 if end.day < start.day else 0)


def us_row(row):
    passage = row.get("evidence_passage") or ""
    out = {"code": row.get("identifier"), "price_field": row.get("price"), "flags": []}
    if "Contractor-priced" in passage or "contractor pricing" in passage:
        out["stated"] = "contractor priced; no national amount"
        out["flags"].append("contractor priced: each MAC sets the amount (US19)")
        return out
    m = AMOUNT_CF_RVU.search(passage)
    if m:
        amount, cf, rvu = float(m["amount"]), float(m["cf"]), float(m["rvu"])
        out.update(stated=f"{amount:.2f} USD (all settings)", recomputed=f"{rvu} x {cf} = {rvu * cf:.2f}")
        if abs(rvu * cf - amount) > 0.01:
            out["flags"].append("stated amount does not equal RVU x conversion factor")
    else:
        m = NONFAC.search(passage)
        if m:
            nf, f, cf = float(m["nf"]), float(m["f"]), float(m["cf"])
            nfr, fr = float(m["nfr"]), float(m["fr"])
            out.update(stated=f"non-facility {nf:.2f} USD; facility {f:.2f} USD",
                       recomputed=f"{nfr} x {cf} = {nfr * cf:.2f}; {fr} x {cf} = {fr * cf:.2f}")
            if abs(nfr * cf - nf) > 0.01 or abs(fr * cf - f) > 0.01:
                out["flags"].append("stated amount does not equal RVU x conversion factor")
        else:
            out["stated"] = "[GAP] no amount in passage"
    if row.get("price") is None and "stated" in out and not out["stated"].startswith("[GAP]"):
        out["flags"].append("price field empty although the passage states an amount (register item C10)")
    out["flags"].append("national amount before geographic adjustment (US8, US9)")
    return out


def diga_row(row, as_of):
    listed = row.get("listed_on")
    months = None
    rule = "[GAP] no listing date"
    if listed:
        months = months_between(dt.date.fromisoformat(listed), as_of)
        if months < 12:
            rule = "year one: manufacturer's actual price applies (DE7, DE9)"
        else:
            rule = ("past year one: a negotiated or arbitrated amount applies (DE1, DE5); "
                    "whether the stored figure is that amount is [GAP]")
    return {"id": row.get("identifier"), "product": row.get("product"), "status": row.get("status"),
            "listed_on": listed, "months_listed": months, "stored_price": row.get("price"),
            "currency": row.get("currency"), "rule": rule}


def summarize(prices):
    prices = [p for p in prices if isinstance(p, (int, float))]
    if not prices:
        return None
    return {"n": len(prices), "min": min(prices), "median": round(statistics.median(prices), 2), "max": max(prices)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--as-of", default=dt.date.today().isoformat())
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    as_of = dt.date.fromisoformat(a.as_of)
    with open(a.file, encoding="utf-8") as fh:
        data = json.load(fh)
    report = {"as_of": a.as_of, "us": [], "de": {}}
    for key, rows in data.items():
        if key.startswith("_") or not isinstance(rows, list):
            continue
        if key.startswith("US_"):
            report["us"].extend(us_row(r) for r in rows)
        elif key.startswith("DE_DIGA"):
            de_rows = [diga_row(r, as_of) for r in rows]
            report["de"][key] = {
                "rows": de_rows,
                "all": summarize([r["stored_price"] for r in de_rows]),
                "permanent": summarize([r["stored_price"] for r in de_rows if r["status"] == "permanent"]),
                "provisional": summarize([r["stored_price"] for r in de_rows if r["status"] == "provisional"]),
            }
    if a.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return
    print(f"Price facts as of {a.as_of}. Comparator and code facts only; no price for the person's product.\n")
    if report["us"]:
        print("US codes | stated | recomputed | flags")
        for r in report["us"]:
            print(f"{r['code']} | {r.get('stated')} | {r.get('recomputed', '')} | {'; '.join(r['flags'])}")
        print()
    for key, block in report["de"].items():
        print(f"{key}: stored DiGA prices (unit and prescription period [GAP])")
        print("id | product | status | listed | months | stored price | rule")
        for r in block["rows"]:
            print(f"{r['id']} | {r['product']} | {r['status']} | {r['listed_on']} | {r['months_listed']} | "
                  f"{r['stored_price']} {r['currency']} | {r['rule']}")
        for label in ("all", "permanent", "provisional"):
            if block[label]:
                s = block[label]
                print(f"  {label}: n={s['n']}, min={s['min']}, median={s['median']}, max={s['max']}")
        print()


if __name__ == "__main__":
    main()
