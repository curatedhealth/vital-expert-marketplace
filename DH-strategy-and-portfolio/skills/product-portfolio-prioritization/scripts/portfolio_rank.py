#!/usr/bin/env python3
"""Ranking helpers for product-portfolio-prioritization.

Every command computes on the person's own numbers. Nothing here chooses,
scores, sets a weight or recommends a product, program or decision.

  mcda      Check and recompute an analytics.mcda ranking (EVIDEM weighted sum,
            value = 25 x sum of weight x 0-to-4 score). Reads a saved live call
            ({"call": {"arguments"|"args"}, "response"|"results"}) or a plain
            input file ({"alternatives": [...], "criteria_weights": {...}}).
            Flags weights that do not sum to 1, scores outside 0 to 4, missing
            scores (the tool returns 400, register C17), ties, and any
            difference from the tool's own values.

              python3 portfolio_rank.py mcda FILE.json

  swap      For each adjacent pair in the ranking and each criterion: the weight
            at which the pair would swap places if that one weight moved and the
            others kept their proportions (register C17: the tool gives no
            robustness view).

              python3 portfolio_rank.py swap FILE.json

            With --scores: for each adjacent pair, every single one-point change
            in one recorded score (the higher item down by 1, or the lower item
            up by 1, kept within 0 to 4) that ties or reverses the pair. One point
            on criterion c moves a value by 25 x weight(c). A test of the person's
            scores, never a proposed score.

              python3 portfolio_rank.py swap --scores FILE.json

  rice      Recompute an analytics.rice result as reach x impact x
            (confidence / 100) / effort, and flag a response whose confidence
            was read on the wrong scale (a fraction sent is divided by 100 again).

              python3 portfolio_rank.py rice FILE.json

  capacity  Sum the capacity the person's "continue" items use against the
            capacity the person named, in the person's ranking order, and name
            the first continue item that goes past it.

              python3 portfolio_rank.py capacity FILE.json

  words     Count a short-mode answer the way the cap counts it: everything from
            the "Calls made" heading on is dropped, and table columns headed
            Source or Rows are left out. Prints the count and, if over 450,
            the house cut order. Also checks that the record line is last: no
            offer of a full version after "Record", and "Clears it" on the last
            body line.

              python3 portfolio_rank.py words ANSWER.md
"""
import argparse
import json
import re
import sys

WORD_CAP = 450
CUT_ORDER = ("context paragraphs, repeated row ids in prose, secondary rules, "
             "rows not tied to the person's question (never a gap, a stop, the "
             "company status line or the record line)")
OFFER_RE = re.compile(r"full version", re.I)


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


# ---------- MCDA ----------
def mcda_inputs(data):
    """Return (alternatives, weights, tool_results or None, label)."""
    label = data.get("label") or data.get("_note") or data.get("inputs_are")
    if "alternatives" in data and "criteria_weights" in data:
        return data["alternatives"], data["criteria_weights"], data.get("results"), label
    call = data.get("call", {})
    args = call.get("arguments") or call.get("args") or {}
    resp = data.get("response")
    results = resp.get("results") if isinstance(resp, dict) else data.get("results")
    return args.get("alternatives", []), args.get("criteria_weights", {}), results, label


def mcda_value(scores, weights):
    return 25.0 * sum(weights[c] * scores[c] for c in weights)


def cmd_mcda(a):
    data = load(a.file)
    alts, weights, tool, label = mcda_inputs(data)
    if label:
        print("Input label: " + str(label))
    problems = []
    total = sum(weights.values())
    if abs(total - 1.0) > 1e-6:
        problems.append("weights sum to {:.4f}, not 1; ask the person to confirm their weights".format(total))
    ranked, not_ranked = [], []
    for alt in alts:
        sc = alt.get("scores", {})
        missing = [c for c in weights if c not in sc or sc[c] is None]
        out_of_range = [c for c in sc if sc[c] is not None and not (0 <= sc[c] <= 4)]
        if missing:
            not_ranked.append((alt["id"], "missing score: " + ", ".join(missing)))
            continue
        if out_of_range:
            problems.append("{}: score outside 0 to 4 on {}".format(alt["id"], ", ".join(out_of_range)))
        contrib = {c: 25.0 * weights[c] * sc[c] for c in weights}
        top = max(contrib, key=contrib.get)
        ranked.append((alt["id"], mcda_value(sc, weights), top, contrib))
    ranked.sort(key=lambda r: -r[1])
    print("\nRanking on the person's weights and scores (EVIDEM weighted sum, 0 to 100):\n")
    print("| Rank | Item | Value | Largest contribution |")
    print("|---|---|---|---|")
    for i, (name, val, top, contrib) in enumerate(ranked, 1):
        print("| {} | {} | {:.2f} | {} ({:.2f}) |".format(i, name, val, top, contrib[top]))
    for i in range(len(ranked) - 1):
        if abs(ranked[i][1] - ranked[i + 1][1]) < 1e-9:
            problems.append("tie: {} and {} both {:.2f} (the tool does not flag ties, register C17)".format(
                ranked[i][0], ranked[i + 1][0], ranked[i][1]))
    if not_ranked:
        print("\nNot ranked (send no call for these until the person gives the score):")
        for name, why in not_ranked:
            print("- {}: {}".format(name, why))
    if tool:
        print("\nCheck against the tool's own values:")
        mine = {r[0]: r[1] for r in ranked}
        for r in tool:
            tv = r.get("value_estimate")
            mv = mine.get(r.get("id"))
            if mv is None:
                print("- {}: tool {} ; not recomputed".format(r.get("id"), tv))
            else:
                ok = abs(mv - tv) < 0.01
                print("- {}: tool {} ; recomputed {:.2f} ; {}".format(r.get("id"), tv, mv, "same" if ok else "DIFFERENT"))
    if problems:
        print("\nFlags:")
        for p in problems:
            print("- " + p)
    print("\nThe ranking is arithmetic on the person's numbers, not a decision.")
    return ranked, weights, {a_["id"]: a_.get("scores", {}) for a_ in alts}


def swap_weight(sa, sb, weights, c):
    wc = weights[c]
    if wc >= 1:
        return None
    ra = sum(weights[k] * sa[k] for k in weights if k != c) / (1 - wc)
    rb = sum(weights[k] * sb[k] for k in weights if k != c) / (1 - wc)
    denom = (ra - rb) - (sa[c] - sb[c])
    if abs(denom) < 1e-12:
        return None
    x = (ra - rb) / denom
    if 0.001 < x < 0.999:
        return x
    return None


def score_swaps(scores, weights, ranked):
    print("\nOne-point score changes that tie or reverse each adjacent pair (one score moved by 1, within 0 to 4):\n")
    print("| Pair (higher first) | Values | Gap | Change | Effect of one point | Result |")
    print("|---|---|---|---|---|---|")
    for i in range(len(ranked) - 1):
        hi, lo = ranked[i], ranked[i + 1]
        vh, vl = mcda_value(scores[hi], weights), mcda_value(scores[lo], weights)
        gap = vh - vl
        found = False
        for c in sorted(weights, key=lambda k: -weights[k]):
            step = 25.0 * weights[c]
            for who, s, d in ((hi, scores[hi][c], -1), (lo, scores[lo][c], +1)):
                if not (0 <= s + d <= 4):
                    continue
                if step + 1e-9 >= gap:
                    res = "tie" if abs(step - gap) < 1e-9 else "reverses"
                    print("| {} over {} | {:.2f} / {:.2f} | {:.2f} | {} {} from {} to {} | {:.2f} | {} |".format(
                        hi, lo, vh, vl, gap, who, c, s, s + d, step, res))
                    found = True
        if not found:
            biggest = max(25.0 * weights[c] for c in weights)
            print("| {} over {} | {:.2f} / {:.2f} | {:.2f} | no single one-point change | largest {:.2f} | holds |".format(
                hi, lo, vh, vl, gap, biggest))
    print("\nScores are the person's; a one-point change is a test of their scores, not a proposed score.")


def cmd_swap(a):
    data = load(a.file)
    alts, weights, _tool, label = mcda_inputs(data)
    scores = {x["id"]: x.get("scores", {}) for x in alts if all(c in x.get("scores", {}) for c in weights)}
    ranked = sorted(scores, key=lambda k: -mcda_value(scores[k], weights))
    if label:
        print("Input label: " + str(label))
    if getattr(a, "scores", False):
        score_swaps(scores, weights, ranked)
        return
    print("\nWhere the ranking would flip (one weight moved, the others kept in proportion):\n")
    print("| Pair (higher first) | Criterion | Current weight | Swap at |")
    print("|---|---|---|---|")
    closest = None
    for i in range(len(ranked) - 1):
        hi, lo = ranked[i], ranked[i + 1]
        for c in weights:
            x = swap_weight(scores[hi], scores[lo], weights, c)
            if x is None:
                cell = "no swap between 0 and 1"
            else:
                cell = "{:.2f}".format(x)
                dist = abs(x - weights[c])
                if closest is None or dist < closest[0]:
                    closest = (dist, hi, lo, c, weights[c], x)
            print("| {} over {} | {} | {:.2f} | {} |".format(hi, lo, c, weights[c], cell))
    if closest:
        _d, hi, lo, c, w, x = closest
        print("\nClosest call: {} over {} swaps if {} moves from {:.2f} to {:.2f}.".format(hi, lo, c, w, x))
    print("Weights are the person's; a swap point is a test of their weights, not a proposal to change them.")


# ---------- RICE ----------
def cmd_rice(a):
    data = load(a.file)
    call = data.get("call", {})
    args = call.get("arguments") or call.get("args") or data
    items = args.get("initiatives", [])
    resp = data.get("response", {}) if isinstance(data.get("response"), dict) else {}
    tool = {r.get("id"): r for r in resp.get("results", [])}
    print("| Item | Reach | Impact | Confidence sent | Recomputed score (confidence as percent) | Tool score | Note |")
    print("|---|---|---|---|---|---|---|")
    for it in items:
        conf = it["confidence"]
        note = []
        if conf <= 1:
            note.append("confidence sent as a fraction; the tool reads percent and divides by 100 again (register N5): resend as a percent")
        score = it["reach"] * it["impact"] * (conf / 100.0) / it["effort"]
        t = tool.get(it["id"], {})
        ts = t.get("score")
        if ts is not None and abs(ts - score) > 0.01:
            note.append("tool differs")
        print("| {} | {} | {} | {} | {:.4f} | {} | {} |".format(
            it["id"], it["reach"], it["impact"], conf, score, ts if ts is not None else "not saved", "; ".join(note) or "same"))
    print("\nReach, impact, confidence and effort are the person's estimates; RICE ranks them, it does not decide.")


# ---------- capacity ----------
def cmd_capacity(a):
    data = load(a.file)
    cap = data.get("capacity_named")
    unit = data.get("capacity_unit", "units")
    items = data.get("items", [])
    order = data.get("order") or [x["id"] for x in items]
    by_id = {x["id"]: x for x in items}
    if cap is None:
        print("Capacity not given by the person: no comparison made. Ask for the capacity and its unit.")
    print("| Order | Item | Decision (the person's) | Capacity use ({}) | Running total of continue items |".format(unit))
    print("|---|---|---|---|---|")
    running, first_over = 0.0, None
    for n, iid in enumerate(order, 1):
        it = by_id.get(iid, {"id": iid})
        dec = it.get("decision", "not given")
        use = it.get("capacity_use")
        cell_use = "not given" if use is None else use
        if dec == "continue" and use is not None:
            running += use
            if cap is not None and running > cap and first_over is None:
                first_over = iid
        print("| {} | {} | {} | {} | {} |".format(n, iid, dec, cell_use, running if dec == "continue" else ""))
    missing = [x["id"] for x in items if x.get("decision") == "continue" and x.get("capacity_use") is None]
    if cap is not None:
        print("\nCapacity named: {} {}. Continue items use {} {}.".format(cap, unit, running, unit))
        if first_over:
            print("First continue item past the named capacity: {}.".format(first_over))
        else:
            print("Continue items stay within the named capacity.")
    if missing:
        print("Capacity use not given for continue items: " + ", ".join(missing) + " [GAP].")
    conts = [x for x in items if x.get("decision") == "continue"]
    if items and len(conts) == len(items):
        print("Every item is marked continue: the old method's 'do not continue every item' check applies; ask the person.")


# ---------- words ----------
def count_words(text):
    lines = text.splitlines()
    body = []
    for ln in lines:
        if re.match(r"^\s*#*\s*\**Calls made", ln, re.I):
            break
        body.append(ln)
    out = []
    drop_cols = None
    for ln in body:
        if ln.strip().startswith("|"):
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if drop_cols is None:
                drop_cols = {i for i, c in enumerate(cells) if c.lower() in ("source", "rows", "row", "sources")}
            cells = [c for i, c in enumerate(cells) if i not in drop_cols]
            out.append(" ".join(cells))
        else:
            drop_cols = None
            out.append(ln)
    words = re.findall(r"[A-Za-z0-9][A-Za-z0-9'.,%/()\-]*", "\n".join(out))
    return len(words)


def record_order(text):
    """The record line must be last in the answer body: no offer line after the
    "Record" block starts, and "Clears it" must be the last body line."""
    body = []
    for ln in text.splitlines():
        if re.match(r"^\s*#*\s*\**Calls made", ln, re.I):
            break
        if ln.strip():
            body.append(ln.strip())
    rec = [i for i, ln in enumerate(body) if re.match(r"^(\d+\.\s*)?\**Record", ln) or "Clears it" in ln]
    if not rec:
        return "Flag: no record line found."
    first = rec[0]
    if any(OFFER_RE.search(ln) for ln in body[first:]):
        return "Flag: the offer of a full version sits after the record block; move it above \"Record\"."
    if "Clears it" not in body[-1] and "uncleared draft" not in body[-1]:
        return "Flag: the record line is not the last line of the answer body."
    return "Record line is last."


def cmd_words(a):
    text = open(a.answer, encoding="utf-8").read()
    n = count_words(text)
    if n <= WORD_CAP:
        print("{} words (cap {}): within the short-mode cap.".format(n, WORD_CAP))
    else:
        print("{} words (cap {}): over by {}. Cut in this order: {}.".format(n, WORD_CAP, n - WORD_CAP, CUT_ORDER))
    print(record_order(text))


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn, arg in (("mcda", cmd_mcda, "file"), ("swap", cmd_swap, "file"), ("rice", cmd_rice, "file"),
                          ("capacity", cmd_capacity, "file"), ("words", cmd_words, "answer")):
        sp = sub.add_parser(name)
        sp.add_argument(arg)
        if name == "swap":
            sp.add_argument("--scores", action="store_true",
                            help="one-point score changes that tie or reverse each adjacent pair")
        sp.set_defaults(fn=fn)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
