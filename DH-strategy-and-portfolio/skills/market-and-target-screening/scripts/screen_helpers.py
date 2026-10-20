#!/usr/bin/env python3
"""Helpers for market-and-target-screening.

table SCREEN.json [--min-authorizations N] [--min-score N]
    Turn a saved diligence-dh.screen_market response into a Markdown long list with
    the perimeter line. Accepts the three saved shapes: a direct screen_market response
    ({"results": [...], "perimeter": {...}}), a commercial-dh.screen_commercial_peers
    response with a "screen_market" block, or either nested under "response".
    --min-authorizations and --min-score apply the person's own pass rules only; the
    output labels them "your rule". Without them nothing is filtered. The order is the
    library's sort and is printed as such, never as a ranking.

swap MCDA.json
    Recompute an analytics.mcda result (value = 25 x sum of weight x score) and, for
    each adjacent pair in the ranking, the weight at which the two would swap when one
    criterion's weight moves and the others are rescaled in proportion. Accepts a file
    with "arguments" and "results" at top level, or the saved partnership-screen job
    file (key "step_2_mcda"). Ranks only what the person scored; it never adds scores.

wordcount ANSWER.md [--limit 450]
    Count the words of a drafted short-mode answer the way the cap counts them: stops
    at the calls list and leaves out table columns headed Source or Rows. Prints the
    count and, if over, the cut order.

Standard library only.
"""
import argparse
import json
import re
import sys


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def find_screen(d):
    """Return (block, call_args) for the screen_market block in any saved shape."""
    if "response" in d and isinstance(d["response"], dict):
        inner = d["response"]
        args = (d.get("call") or {}).get("arguments") or (d.get("call") or {}).get("args") or {}
        if "screen_market" in inner:
            return inner["screen_market"], args
        return inner, args
    args = (d.get("call") or {}).get("args") or (d.get("call") or {}).get("arguments") or {}
    if "screen_market" in d:
        return d["screen_market"], args
    return d, args


def score_of(row):
    em = row.get("evidence_maturity_score")
    if em is None:
        em = row.get("evidence_maturity")
        if isinstance(em, dict):
            em = em.get("score")
    return em


def cmd_table(a):
    d = load(a.file)
    block, args = find_screen(d)
    rows = block.get("results", [])
    retrieved = block.get("retrieved_at") or d.get("retrieved") or "not stated"
    perim = block.get("perimeter") or {}
    statement = perim.get("statement") or block.get("perimeter_statement") or "not stated in the saved output"
    print(f"Call: screen arguments {json.dumps(args)}; retrieved {retrieved}")
    total = block.get("total_matches", d.get("total_matches", "not stated"))
    print(f"Shown: {len(rows)} of {total} matches. Perimeter statement: \"{statement}\"")
    if perim:
        print(f"Store: {perim.get('companies_in_store', 'not stated')} companies; segments loaded {perim.get('segments_loaded')}; jurisdictions loaded {perim.get('jurisdictions_loaded')}")
    elif block.get("jurisdictions_loaded"):
        print(f"Jurisdictions loaded: {block.get('jurisdictions_loaded')}")
    if block.get("ranking"):
        print(f"Order: the library's sort ({block['ranking']}); not a ranking of targets.")
    if d.get("contradiction"):
        print(f"Coverage note from the response: {d['contradiction']}")
    rules = []
    if a.min_authorizations is not None:
        rules.append(f"authorizations >= {a.min_authorizations} (your rule)")
    if a.min_score is not None:
        rules.append(f"evidence maturity score >= {a.min_score} (your rule)")
    print("Rules applied: " + ("; ".join(rules) if rules else "none (no filter given)"))
    print()
    print("| Company | Country (as stored) | Jurisdictions | Products | Authorizations | Studies | Safety records | Evidence maturity (rubric v1) | Your rules |")
    print("|---|---|---|---|---|---|---|---|---|")
    kept = 0
    for r in rows:
        auth = r.get("authorizations")
        sc = score_of(r)
        res = []
        if a.min_authorizations is not None:
            res.append("not measurable [GAP]" if auth is None else ("pass" if auth >= a.min_authorizations else "fail"))
        if a.min_score is not None:
            res.append("not measurable [GAP]" if sc is None else ("pass" if sc >= a.min_score else "fail"))
        verdict = ", ".join(res) if res else "none"
        if "fail" not in res:
            kept += 1

        def cell(v):
            if v is None:
                return "not in saved output"
            if isinstance(v, list):
                return "; ".join(str(x) for x in v)
            return str(v)
        print(f"| {cell(r.get('company'))} | {cell(r.get('country'))} | {cell(r.get('jurisdictions'))} | {cell(r.get('products'))} | {cell(auth)} | {cell(r.get('studies'))} | {cell(r.get('safety_events'))} | {cell(sc)} | {verdict} |")
    print()
    print(f"Passing or not measurable under your rules: {kept} of {len(rows)} shown. Not-measurable rows stay on the list.")


def mcda_parts(d):
    if "step_2_mcda" in d:
        d = d["step_2_mcda"]
    args = d.get("arguments") or d.get("args") or {}
    return args.get("alternatives", []), args.get("criteria_weights", {}), d.get("results", [])


def value(scores, w):
    return 25.0 * sum(w[c] * scores.get(c, 0) for c in w)


def cmd_swap(a):
    alts, w, results = mcda_parts(load(a.file))
    if not alts or not w:
        sys.exit("No alternatives or weights found.")
    missing = [x["id"] for x in alts if set(w) - set(x.get("scores", {}))]
    if missing:
        print("Not ranked (score missing; the tool refuses the whole call): " + ", ".join(missing))
        alts = [x for x in alts if x["id"] not in missing]
    total_w = sum(w.values())
    if abs(total_w - 1) > 1e-6:
        print(f"Warning: weights sum to {total_w}, not 1.")
    vals = {x["id"]: value(x["scores"], w) for x in alts}
    returned = {r.get("id"): r.get("value_estimate") for r in results}
    order = sorted(alts, key=lambda x: -vals[x["id"]])
    print("| Rank | Candidate | Value (recomputed) | Value (tool) | Largest contributor |")
    print("|---|---|---|---|---|")
    for i, x in enumerate(order, 1):
        contrib = {c: 25.0 * w[c] * x["scores"][c] for c in w}
        top = max(contrib, key=contrib.get)
        print(f"| {i} | {x['id']} | {vals[x['id']]:.2f} | {returned.get(x['id'], 'not given')} | {top} ({contrib[top]:.2f}) |")
    print()
    for i in range(len(order) - 1):
        A, B = order[i], order[i + 1]
        d = {c: A["scores"][c] - B["scores"][c] for c in w}
        lines = []
        for k in w:
            rest = sum(w[c] * d[c] for c in w if c != k)
            wk = w[k]
            # diff(x) = x*d_k + (1-x)/(1-wk)*rest ; solve diff = 0
            denom = d[k] - rest / (1 - wk) if wk < 1 else None
            if denom in (None, 0):
                continue
            x = -(rest / (1 - wk)) / denom
            if 1e-9 < x < 1 - 1e-9 and abs(x - wk) > 1e-9:
                lines.append(f"{k} from {wk:.2f} to {x:.3f}")
        tie = " (tied now)" if abs(vals[A['id']] - vals[B['id']]) < 1e-9 else ""
        print(f"{A['id']} over {B['id']}{tie}: swap if " + ("; or ".join(lines) if lines else "no single-weight move swaps them") + " (other weights rescaled in proportion).")
    print()
    print("These are the person's scores and weights, ranked. Not a recommendation.")


CUT_ORDER = ("context paragraphs, repeated row ids in prose, secondary rules, rows not tied to "
             "the person's question. Never cut a gap, a stop or the record line.")


def answer_words(text):
    """Count words the way the 450-word cap counts them: skip the calls list (the record line after it still counts),
    drop table columns whose header names a source (Source, Rows), and skip pure
    punctuation tokens and table separator rows."""
    words = 0
    drop = set()
    in_table = False
    _skip_calls = False  # the calls list sits before the record block; skip it, then count the record
    for line in text.splitlines():
        s = line.strip()
        if _skip_calls:
            if re.search(r"Clears it|^\W*(#+\s*)?(\*\*)?(\d+\.\s*)?(\*\*)?Record\b", s.strip()):
                _skip_calls = False
            else:
                continue
        if re.match(r"^(#+\s*)?(\*\*)?(\d+\.\s*)?(\*\*)?calls made", s, re.I):
            _skip_calls = True
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not in_table:
                in_table = True
                drop = {i for i, c in enumerate(cells) if re.search(r"source|^rows?$", c, re.I)}
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            cells = [c for i, c in enumerate(cells) if i not in drop]
            s = " ".join(cells)
        else:
            in_table = False
            drop = set()
        words += sum(1 for tok in s.split() if re.search(r"[A-Za-z0-9]", tok))
    return words


def cmd_wordcount(a):
    with open(a.file, encoding="utf-8") as f:
        n = answer_words(f.read())
    print(f"Words (without the calls list and table source columns): {n} of {a.limit} allowed.")
    if n > a.limit:
        print(f"Over by {n - a.limit}. Cut in this order until under: {CUT_ORDER}")
    else:
        print("Within the short-mode cap.")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("table")
    t.add_argument("file")
    t.add_argument("--min-authorizations", type=int)
    t.add_argument("--min-score", type=int)
    s = sub.add_parser("swap")
    s.add_argument("file")
    w = sub.add_parser("wordcount")
    w.add_argument("file")
    w.add_argument("--limit", type=int, default=450)
    a = p.parse_args()
    {"table": cmd_table, "swap": cmd_swap, "wordcount": cmd_wordcount}[a.cmd](a)


if __name__ == "__main__":
    main()
