#!/usr/bin/env python3
"""Price evidence helper for task A2 (price corridor evidence).

Three subcommands, all on saved library output or the person's own numbers:

  corridor   Keep only the named product's own price row from a saved
             commercial-dh.get_pricing_corridor response and count the rows set
             aside (register N4: the tool mixes in recent listings in any
             indication, without product names).
  precedents Build the comparator table from a saved
             market-access-dh.find_scheme_precedents response: product, status,
             listed on, price as stored, source, retrieved; low, high, count.
  vba        Recompute the value-based anchor the way analytics.vba-price-anchor
             does (comparator cost + QALY gain x threshold + offset) / units,
             to check a returned figure or to show the arithmetic.

Outputs are evidence tables. They never produce a price for the person's product.

Examples:
  python3 comparator_prices.py precedents ../examples/live/precedents_DE_DIGA_F51.json
  python3 comparator_prices.py corridor ../examples/live/pricing_corridor_somnio.json \
      --product-url https://diga.bfarm.de/de/verzeichnis/00508 \
      --precedents ../examples/live/precedents_DE_DIGA_F51.json
  python3 comparator_prices.py vba --comparator-cost 800 --qalys 0.03 --thresholds 20000 30000
"""
import argparse
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def day(ts):
    return (ts or "")[:10] or "[GAP]"


def cmd_precedents(args):
    data = load(args.file)
    rows = data.get("results", [])
    if not rows:
        print("No precedent rows in the file. A missing row is a gap in the library, not evidence of no price.")
        return 1
    print("| Product | Manufacturer | Status | Listed on | Price as stored | Unit stated? | Source | Retrieved |")
    print("|---|---|---|---|---|---|---|---|")
    priced = []
    for r in rows:
        price = r.get("price")
        cur = r.get("currency") or ""
        shown = f"{price} {cur}".strip() if price is not None else "[GAP]"
        if price is not None:
            priced.append((float(price), cur, r.get("product")))
        print(f"| {r.get('product')} | {r.get('manufacturer')} | {r.get('status')} ({r.get('status_raw')}) | "
              f"{r.get('listed_on') or '[GAP]'} | {shown} | no [GAP] | {r.get('source_url')} | {day(r.get('retrieved_at'))} |")
    if priced:
        currencies = {c for _, c, _ in priced}
        if len(currencies) > 1:
            print(f"\nMixed currencies {sorted(currencies)}: no low or high computed.")
        else:
            lo = min(priced)
            hi = max(priced)
            print(f"\nRegistered prices: {len(priced)} of {len(rows)} rows. Low {lo[0]:g} {lo[1]} ({lo[2]}); "
                  f"high {hi[0]:g} {hi[1]} ({hi[2]}). Context for the person's corridor, not a target.")
    print("Unit and prescription period are not stored on these rows; for DE_DIGA the directory publishes them (DE20).")
    return 0


def cmd_corridor(args):
    data = load(args.file)
    prices = data.get("prices", [])
    url = args.product_url
    if not url and args.precedents and args.product:
        for r in load(args.precedents).get("results", []):
            if (r.get("product") or "").lower() == args.product.lower():
                url = r.get("source_url")
    if not url:
        print("Give --product-url, or --precedents with --product, to identify the product's own record.")
        return 2
    own = [p for p in prices if p.get("source_url") == url]
    no_url = [p for p in prices if not p.get("source_url")]
    other = [p for p in prices if p.get("source_url") and p.get("source_url") != url]
    print(f"Product record: {url}")
    if own:
        p = own[0]
        print(f"Registered price: {p.get('amount')} {p.get('currency')} ({p.get('scheme')}), retrieved {day(p.get('retrieved_at'))}, via {p.get('upstream_tool')}.")
    else:
        print("No price row carries the product's own source URL: registered price [GAP].")
    same_amount = [p for p in no_url if own and p.get("amount") == own[0].get("amount")]
    print(f"Rows with no source URL: {len(no_url)} ({len(same_amount)} repeat the product's own amount).")
    print(f"Rows from other records set aside: {len(other)} (no product name or indication on the row; not comparators).")
    if args.precedents:
        comp_urls = {r.get("source_url") for r in load(args.precedents).get("results", [])}
        overlap = [p for p in other if p.get("source_url") in comp_urls]
        print(f"Of those, rows that are also same-indication precedents: {len(overlap)}.")
        if other:
            amounts = sorted(float(p["amount"]) for p in other if p.get("amount") is not None)
            if amounts:
                print(f"Set-aside amounts ranged {amounts[0]:g} to {amounts[-1]:g}; do not read them as a corridor.")
    return 0


def cmd_vba(args):
    if args.qalys is None or args.comparator_cost is None or not args.thresholds:
        print("All inputs are the person's: --comparator-cost, --qalys and --thresholds are required.")
        return 2
    print("| Threshold per QALY | Value-based budget per patient | Ceiling per unit |")
    print("|---|---|---|")
    for t in args.thresholds:
        budget = args.comparator_cost + args.qalys * t + args.offset
        print(f"| {t:g} | {budget:g} | {budget / args.units:g} |")
    print(f"Defaults applied: offset {args.offset:g}, units per patient {args.units:g}. Hypothesis on the person's inputs; not a price.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("precedents")
    p.add_argument("file")
    c = sub.add_parser("corridor")
    c.add_argument("file")
    c.add_argument("--product-url")
    c.add_argument("--product")
    c.add_argument("--precedents")
    v = sub.add_parser("vba")
    v.add_argument("--comparator-cost", type=float)
    v.add_argument("--qalys", type=float)
    v.add_argument("--thresholds", type=float, nargs="+")
    v.add_argument("--offset", type=float, default=0.0)
    v.add_argument("--units", type=float, default=1.0)
    args = ap.parse_args()
    return {"precedents": cmd_precedents, "corridor": cmd_corridor, "vba": cmd_vba}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
