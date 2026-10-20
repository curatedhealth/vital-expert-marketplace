#!/usr/bin/env python3
"""Helper for analytics-products-and-decision-support (dh-technology).

Works only on the person's own files. It never sets a target, a threshold, a
certification rule, a priority rule, an owner or a decision.

  cards      python3 metric_check.py cards --file METRICS.csv
             Checks each metric card for the elements the sourced rows name
             (CMS measure specification structure, DA-132 to DA-137, used as a
             checklist for internal metrics) and the old task methods (owner,
             grain, certified source, filters, version). Columns:
             id, name, decision, owner, entity, entity_key, grain, period,
             initial_population, denominator, numerator, exclusions,
             scoring_direction, stratification, source_tables, allowed_filters,
             version, status, certified_on, certifier
  recompute  python3 metric_check.py recompute --data ROWS.csv
                 --denominator "col=val;col2>=1" --numerator "col=val"
                 [--reported 0.42] [--by col]
             Recomputes a rate from the person's row-level file with the
             denominator and numerator rules written on the card, and sets it
             beside the figure the dashboard shows. Operators: = != >= <= > <
             and "in" (col in a|b). The numerator is counted inside the
             denominator.
  driver     python3 metric_check.py driver --file BREAKDOWN.csv [--share 0.5]
             Columns: segment, prior, current (additive values or counts).
             Prints each segment's contribution to the total change. A segment
             "accounts for the move" only under the person's own --share rule;
             without it no driver is named.
  rank       python3 metric_check.py rank --input SCORES.json
             RICE ({"initiatives": [...]}) or weighted sum on 0 to 4
             ({"alternatives": [...], "criteria_weights": {...}}): recomputes
             what analytics.rice or analytics.mcda returns, flags proposed
             scores and fractional confidence, and prints, for each adjacent
             pair, the score on each criterion at which the lower option ties.
  words      python3 metric_check.py words ANSWER.md
             Counts a short answer without the "Calls made" block and the
             Source and Rows columns.

Flags are facts against the rows, never verdicts:
  K1 decision not given; K2 owner not named; K3 numerator or denominator not
  given (DA-134, DA-135); K4 initial population not given (DA-133); K5
  denominator written in codes only (DA-134); K6 scoring direction not given
  (DA-137); K7 stratification not stated (DA-136); K8 grain or period not
  given; K9 certified source not given; K10 status "certified" without
  certifier, date, owner, formula, grain or source; K11 same numerator and
  denominator as another card (recomputed beside it); K12 every column allowed
  as a filter, or filters not given; K13 version not given.
"""
import argparse
import csv
import json
import re
import sys

CAP = 450


def rows(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def g(r, k):
    return (r.get(k) or "").strip()


def cmd_cards(a):
    cards = rows(a.file)
    print("Checklist: CMS measure specification structure (CMS MMS Hub, read 20 October 2026, "
          "DA-132 to DA-137; CMS quality-measure guidance, used here as a checklist for internal metrics) "
          "and the old task methods. The certification rule itself is yours.")
    print("| Id | Metric | Owner | Status | Version | Flags |")
    print("|---|---|---|---|---|---|")
    seen = {}
    for r in cards:
        key = (g(r, "numerator").lower(), g(r, "denominator").lower())
        if all(key):
            seen.setdefault(key, []).append(g(r, "id"))
    counts = {}
    for r in cards:
        fl = []
        if not g(r, "decision"):
            fl.append("K1")
        if not g(r, "owner"):
            fl.append("K2")
        if not g(r, "numerator") or not g(r, "denominator"):
            fl.append("K3")
        if not g(r, "initial_population"):
            fl.append("K4")
        den = g(r, "denominator")
        if den and re.fullmatch(r"[A-Z0-9.,;:/\s-]+", den) and re.search(r"\d", den):
            fl.append("K5")
        if not g(r, "scoring_direction"):
            fl.append("K6")
        if not g(r, "stratification"):
            fl.append("K7")
        if not g(r, "grain") or not g(r, "period"):
            fl.append("K8")
        if not g(r, "source_tables"):
            fl.append("K9")
        if g(r, "status").lower() == "certified":
            need = ["certifier", "certified_on", "owner", "numerator", "denominator", "grain", "source_tables"]
            missing = [k for k in need if not g(r, k)]
            if missing:
                fl.append("K10 (" + ", ".join(missing) + ")")
        key = (g(r, "numerator").lower(), g(r, "denominator").lower())
        if all(key) and len(seen.get(key, [])) > 1:
            others = [x for x in seen[key] if x != g(r, "id")]
            fl.append("K11 (" + ", ".join(others) + ")")
        filt = g(r, "allowed_filters").lower()
        if not filt or filt in ("all", "any", "*", "every column"):
            fl.append("K12")
        if not g(r, "version"):
            fl.append("K13")
        for f in fl:
            counts[f.split()[0]] = counts.get(f.split()[0], 0) + 1
        print(f"| {g(r, 'id')} | {g(r, 'name')} | {g(r, 'owner') or 'owner not named'} | "
              f"{g(r, 'status') or 'not given'} | {g(r, 'version') or 'not given'} | {', '.join(fl) or 'none'} |")
    print("\nFlag counts: " + (", ".join(f"{k} {v}" for k, v in sorted(counts.items())) or "none") + ".")
    print("A flag is a missing element against the rows or the old task method; "
          "whether a metric is certified is the certifier's decision under your rule.")
    return 0


OPS = ("!=", ">=", "<=", "=", ">", "<")


def parse_rule(rule):
    out = []
    for part in [p.strip() for p in (rule or "").split(";") if p.strip()]:
        m = re.fullmatch(r"(\w+)\s+in\s+(.+)", part)
        if m:
            out.append((m.group(1), "in", [x.strip() for x in m.group(2).split("|")]))
            continue
        for op in OPS:
            if op in part:
                col, val = part.split(op, 1)
                out.append((col.strip(), op, val.strip()))
                break
        else:
            raise SystemExit(f"cannot read rule part: {part}")
    return out


def num(s):
    try:
        return float(str(s).replace(",", ""))
    except ValueError:
        return None


def match(r, conds):
    for col, op, val in conds:
        if col not in r:
            raise SystemExit(f"column not in the file: {col}")
        x = (r.get(col) or "").strip()
        if op == "in":
            ok = x in val
        elif op in ("=", "!="):
            ok = (x == val) if op == "=" else (x != val)
        else:
            xn, vn = num(x), num(val)
            if xn is None or vn is None:
                ok = False
            else:
                ok = {">=": xn >= vn, "<=": xn <= vn, ">": xn > vn, "<": xn < vn}[op]
        if not ok:
            return False
    return True


def cmd_recompute(a):
    data = rows(a.data)
    den_c, num_c = parse_rule(a.denominator), parse_rule(a.numerator)
    groups = {}
    for r in data:
        key = (r.get(a.by) or "not given").strip() if a.by else "all rows"
        d = groups.setdefault(key, [0, 0])
        if match(r, den_c):
            d[0] += 1
            if match(r, num_c):
                d[1] += 1
    tot_d = sum(v[0] for v in groups.values())
    tot_n = sum(v[1] for v in groups.values())
    print(f"Denominator rule: {a.denominator}. Numerator rule: {a.numerator} (counted inside the denominator).")
    print("| Group | Denominator | Numerator | Rate |")
    print("|---|---|---|---|")
    for k in sorted(groups):
        d, n = groups[k]
        print(f"| {k} | {d} | {n} | {(n / d):.4f} |" if d else f"| {k} | 0 | {n} | not computable (denominator 0) |")
    rate = tot_n / tot_d if tot_d else None
    print(f"\nRecomputed from your file: {tot_n} / {tot_d} = " + (f"{rate:.4f}" if rate is not None else "not computable"))
    if a.reported is not None and rate is not None:
        diff = rate - a.reported
        print(f"Figure shown on the dashboard: {a.reported:.4f}. Difference (recomputed minus shown): {diff:+.4f}.")
        print("Whether the difference matters is your rule; a difference means the dashboard formula, "
              "filters or refresh differ from the card until shown otherwise.")
    return 0


def cmd_driver(a):
    data = rows(a.file)
    segs = []
    for r in data:
        p, c = num(r.get("prior")), num(r.get("current"))
        if p is None or c is None:
            segs.append((g(r, "segment"), None, None, None))
        else:
            segs.append((g(r, "segment"), p, c, c - p))
    valid = [s for s in segs if s[3] is not None]
    tp = sum(s[1] for s in valid)
    tc = sum(s[2] for s in valid)
    total = tc - tp
    print(f"Total: prior {tp:g}, current {tc:g}, change {total:+g}.")
    print("| Segment | Prior | Current | Change | Share of total change |")
    print("|---|---|---|---|---|")
    for s, p, c, ch in segs:
        if ch is None:
            print(f"| {s} | not given | not given | not computable | not computable |")
            continue
        share = ch / total if total else None
        print(f"| {s} | {p:g} | {c:g} | {ch:+g} | " + (f"{share:.2f}" if share is not None else "not computable (no total change)") + " |")
    missing = [s[0] for s in segs if s[3] is None]
    if missing:
        print("Segments without both values: " + ", ".join(missing) + " (the total excludes them).")
    if total == 0:
        print("No total change: there is no move to explain.")
        return 0
    if a.share is None:
        print("Your rule for when a segment 'accounts for the move' is not given: no driver is named. "
              "Give a share (for example the share of the total change you require).")
        return 0
    hits = [s for s in valid if total and (s[3] / total) >= a.share]
    if hits:
        print(f"Under your rule (share >= {a.share:g}): " + ", ".join(f"{s[0]} ({s[3] / total:.2f})" for s in hits) + ".")
    else:
        print(f"Under your rule (share >= {a.share:g}) no segment in this breakdown accounts for the move: "
              "say so and do not name a driver.")
    opp = [s[0] for s in valid if total and s[3] * total < 0]
    if opp:
        print("Segments that moved against the total: " + ", ".join(opp) + ".")
    return 0


def cmd_rank(a):
    data = json.load(open(a.input, encoding="utf-8"))
    if "arguments" in data:
        data = data["arguments"]
    if "call" in data and isinstance(data["call"], dict):
        data = data["call"].get("args", data)
    if any(str(x.get("label", "")).lower() == "proposed" for x in data.get("initiatives", []) + data.get("alternatives", [])):
        print("Stop: scores labeled proposed are never ranked. Rank only the person's own scores.")
        return 1
    if "initiatives" in data:
        res = []
        for i in data["initiatives"]:
            conf = i["confidence"]
            note = ""
            if conf <= 1:
                note = "confidence given as a fraction: analytics.rice needs a whole percent (80, not 0.8)"
            score = i["reach"] * i["impact"] * (conf / 100) / i["effort"]
            res.append((i["id"], score, note))
        res.sort(key=lambda x: -x[1])
        print("| Initiative | RICE score = reach x impact x (confidence / 100) / effort | Note |")
        print("|---|---|---|")
        for idn, s, n in res:
            print(f"| {idn} | {s:.4f} | {n or 'none'} |")
        print("RICE is a calculator the person chose (vendor article, Intercom 2016), not a sourced rule. "
              "Arithmetic on your scores, not a decision.")
        return 0
    w = data["criteria_weights"]
    if abs(sum(w.values()) - 1) > 1e-6:
        print(f"Stop: weights sum to {sum(w.values()):g}, not 1.")
        return 1
    alts = []
    for alt in data["alternatives"]:
        sc = alt["scores"]
        if set(sc) != set(w):
            print(f"Not ranked: {alt['id']} is not scored on every criterion "
                  f"(missing {', '.join(sorted(set(w) - set(sc))) or 'none'}).")
            continue
        alts.append((alt["id"], sum(w[c] * sc[c] for c in w) / 4 * 100, sc))
    alts.sort(key=lambda x: -x[1])
    print("| Option | Value (weighted sum on 0 to 4, scaled to 100) |")
    print("|---|---|")
    for idn, v, _ in alts:
        print(f"| {idn} | {v:.2f} |")
    print("Every criterion is read as higher-is-better (register C17): name criteria so higher is better.")
    for (hi, vh, _), (lo, vl, sl) in zip(alts, alts[1:]):
        gap = vh - vl
        parts = []
        for c in w:
            need = sl[c] + gap / (w[c] * 25) if w[c] else None
            if need is not None and need <= 4:
                parts.append(f"{c} at {need:.2f}")
        print(f"Tie point: {lo} ties {hi} (gap {gap:.2f}) if one of its scores rises to "
              + ("; ".join(parts) if parts else "no single score within 0 to 4") + ".")
    print("Arithmetic on your scores, not a decision.")
    return 0


def count_words(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^#*\s*\**Calls made", text, flags=re.M | re.I)
    if m:
        rest = text[m.start():]
        r = re.search(r"^(#+\s*|\**)?Record\b|^.*Clears it:", rest, flags=re.M)
        text = text[:m.start()] + (rest[r.start():] if r else "")
    out, drop = [], set()
    names = ("source", "rows", "source and date", "source and rows", "source and rows (doi for [paper])")
    for line in text.splitlines():
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            low = [c.lower() for c in cells]
            if any(c in names for c in low):
                drop = {i for i, c in enumerate(low) if c in names}
            out.append(" ".join(c for i, c in enumerate(cells) if i not in drop))
        else:
            if not line.strip():
                drop = set()
            out.append(line)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9.,'%()/-]*", "\n".join(out)))


def cmd_words(a):
    n = count_words(a.answer)
    print(f"{n} words")
    if n <= CAP:
        print("within the short-mode cap")
        return 0
    print("over the cap: cut context paragraphs, repeated row ids in prose, secondary rules, "
          "rows not tied to the question; never a gap, a stop or the record line")
    return 1


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("cards")
    c.add_argument("--file", required=True)
    r = sub.add_parser("recompute")
    r.add_argument("--data", required=True)
    r.add_argument("--denominator", required=True)
    r.add_argument("--numerator", required=True)
    r.add_argument("--reported", type=float)
    r.add_argument("--by")
    d = sub.add_parser("driver")
    d.add_argument("--file", required=True)
    d.add_argument("--share", type=float)
    k = sub.add_parser("rank")
    k.add_argument("--input", required=True)
    w = sub.add_parser("words")
    w.add_argument("answer")
    a = ap.parse_args()
    return {"cards": cmd_cards, "recompute": cmd_recompute, "driver": cmd_driver,
            "rank": cmd_rank, "words": cmd_words}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
