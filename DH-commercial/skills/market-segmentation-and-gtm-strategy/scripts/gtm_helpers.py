#!/usr/bin/env python3
"""Helpers for market-segmentation-and-gtm-strategy.

peers  FILE         Turn a saved commercial-dh.screen_commercial_peers output (full or
                    trimmed JSON) into a markdown peer table with match status per feed.
swap   FILE         Read an analytics.mcda input (alternatives + criteria_weights, the
                    person's scores) and report, for each adjacent pair in the ranking and
                    each criterion, the weight at which the pair would swap, with the other
                    weights kept in proportion. Recomputes the EVIDEM weighted sum
                    (value = 25 x sum(weight x score) on the 0 to 4 scale) and checks it
                    against the tool output when that is in the same file under "results".

Standard library only. No scores are invented: the script reads only what the file holds.
"""
import json
import sys


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def peers(path):
    d = load(path)
    sm = d.get("screen_market", {})
    by_company = {r.get("company"): r for r in sm.get("results", [])}
    print(f"Peer screen: {sm.get('result_count', '?')} returned of {sm.get('total_matches', '?')} matches. "
          f"{sm.get('perimeter_statement') or sm.get('perimeter', {}).get('statement', '')}")
    print("Coverage: " + "; ".join(d.get("coverage", [])))
    print()
    print("| Peer | Products (screen) | Authorizations (screen) | Device rows found | Listing rows found | Status |")
    print("|---|---|---|---|---|---|")
    missed = 0
    for p in d.get("peers", []):
        name = p.get("name")
        sd = p.get("search_devices_results")
        if sd is None:
            sd = p.get("search_devices", {}).get("results", [])
        sl = p.get("search_listings_results")
        if sl is None:
            sl = p.get("search_listings", {}).get("results", [])
        scr = by_company.get(name, {})
        products = ", ".join(scr.get("products", [])) or "-"
        auths = scr.get("authorizations", "-")
        dev = "; ".join(f"{x.get('product')} {x.get('pathway')} {x.get('decision_date')}" for x in sd) or "none"
        lst = "; ".join(f"{x.get('product')} {x.get('scheme')} {x.get('status')}" for x in sl) or "none"
        if not sd and isinstance(auths, int) and auths > 0:
            status = "lookup missed: screen counts authorizations, device search by company name returned none"
            missed += 1
        elif not sd and not scr:
            status = "named product; no device row"
        else:
            status = "found"
        print(f"| {name} | {products} | {auths} | {dev} | {lst} | {status} |")
    print()
    print(f"Lookups missed: {missed} of {len(d.get('peers', []))}. Absence from the store is not absence from the market.")


def value(scores, weights):
    return 25.0 * sum(weights[c] * scores.get(c, 0) for c in weights)


def swap(path):
    d = load(path)
    args = d.get("call", {}).get("args", d)
    alts = args["alternatives"]
    w = args["criteria_weights"]
    total = sum(w.values())
    if abs(total - 1) > 1e-6:
        print(f"Weights sum to {total:.3f}, not 1. Ask the person to confirm before ranking.")
    ranked = sorted(alts, key=lambda a: value(a["scores"], w), reverse=True)
    print("| Rank | Option | Value (recomputed) |")
    print("|---|---|---|")
    for i, a in enumerate(ranked, 1):
        print(f"| {i} | {a['id']} | {value(a['scores'], w):.2f} |")
    tool = {r["id"]: r.get("value_estimate") for r in d.get("results", [])}
    if tool:
        bad = [a["id"] for a in alts if abs(tool.get(a["id"], -1) - value(a["scores"], w)) > 0.01]
        print("\nCheck against analytics.mcda: " + ("all values match." if not bad else f"MISMATCH for {bad}"))
    ties = [(x["id"], y["id"]) for x, y in zip(ranked, ranked[1:])
            if abs(value(x["scores"], w) - value(y["scores"], w)) < 1e-9]
    for t in ties:
        print(f"Tie: {t[0]} and {t[1]} have the same value.")
    print("\nWhere adjacent options would swap (one weight moved, the others kept in proportion):\n")
    print("| Pair | Criterion | Current weight | Swap at weight | Direction |")
    print("|---|---|---|---|---|")
    for hi, lo in zip(ranked, ranked[1:]):
        for k in w:
            a = hi["scores"].get(k, 0) - lo["scores"].get(k, 0)
            rest = sum(w[c] * (hi["scores"].get(c, 0) - lo["scores"].get(c, 0)) for c in w if c != k)
            if w[k] >= 1:
                continue
            B = rest / (1 - w[k])
            if abs(B - a) < 1e-12:
                continue
            t = B / (B - a)
            if 1e-6 < t < 1 - 1e-6 and abs(t - w[k]) > 1e-9:
                direction = "if raised above" if t > w[k] else "if lowered below"
                print(f"| {hi['id']} over {lo['id']} | {k} | {w[k]:.2f} | {t:.2f} | {direction} |")
    print("\nCriteria not listed for a pair cannot swap that pair at any weight strictly between 0 and 1 (at most a tie at an end point).")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("peers", "swap"):
        print(__doc__)
        sys.exit(2)
    {"peers": peers, "swap": swap}[sys.argv[1]](sys.argv[2])
