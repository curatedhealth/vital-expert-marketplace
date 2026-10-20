#!/usr/bin/env python3
"""Screen a draft evidence statement or narrative against the passages and ratings behind it.

A first pass for a person to judge. It finds wording and numbers, not meaning.

Usage:
  python3 statement_check.py --draft draft.txt --evidence evidence.json [--market US|EU|DE|UK]

evidence.json:
  {"outcomes": [{"outcome": "depressive symptoms",
                 "certainty": "low" | "moderate" | "high" | "very low" | null,
                 "rated_by": "who rated it, in the person's words" | null,
                 "passages": ["verbatim results passage", ...]}]}

Checks:
  1. Numbers in the draft that appear in no supplied passage (a number the reader cannot trace).
  2. Certainty words in the draft that are higher than every rating supplied, or any certainty
     word when no outcome has a rating (ratings are the person's; ES-94, ES-96).
  3. Certainty verbs stronger than Cochrane Handbook Table 15.6.b allows for the highest rating
     supplied: "likely"/"probably" needs moderate or high (ES-204); an unhedged "reduces",
     "increases" or "results in" needs high (ES-203); low takes "may" or "the evidence suggests"
     (ES-205); very low takes "the evidence is very uncertain" (ES-206). Wide-interval "no effect"
     wording is flagged for the owner to check against the interval (ES-207).
  4. Wording tied to sourced rows (row ids as in the skill's research files), filtered by market.
Rows are listed for the owner the person names for regulatory or legal review, or owner not named; a hit is a candidate, never a finding.
"""
import argparse
import json
import re
import sys

LEVELS = {"very low": 1, "low": 2, "moderate": 3, "high": 4}

# (pattern, note, {market: rows}); "ALL" applies to every market.
WORDING = [
    (r"\bprov(e|es|en|ing)\b", "proof language: the evidence is never more than its sources",
     {"ALL": ["skill rule (governance.md)"], "UK": ["PC-UK-04"]}),
    (r"\bclinically proven\b", "device-indicating wording in Great Britain",
     {"UK": ["PC-UK-04"]}),
    (r"\bcur(e|es|ed|ing)\b", "cure claim",
     {"EU": ["PC-EU-10"], "DE": ["PC-EU-10", "PC-DE-03"], "UK": ["PC-UK-07", "PC-UK-13 [INDUSTRY]"]}),
    (r"\bguarantee(d|s)?\b", "certain success",
     {"DE": ["PC-DE-04"], "UK": ["PC-UK-13 [INDUSTRY]"]}),
    (r"\bno side[- ]effects?\b|\bno harmful effects?\b", "no-harm claim",
     {"DE": ["PC-DE-04"], "UK": ["PC-UK-13 [INDUSTRY]"]}),
    (r"\bsafe and effective\b|\bfound (to be )?(safe|effective)\b", "safety or effectiveness conclusion",
     {"US": ["PC-US-09 (before clearance)", "PC-US-44"], "ALL": ["skill rule (governance.md)"]}),
    (r"\bcost[- ]effective(ness)?\b|\bsaves? money\b", "economic conclusion: the person's or the HTA body's, and HCEI rules for US payors",
     {"US": ["PC-US-04", "PC-US-06", "PC-US-35"], "ALL": ["skill rule (governance.md)"]}),
    (r"\b(approved|certified|cleared|endorsed)\b", "approval wording: check it is true and complied with",
     {"EU": ["PC-EU-11"], "DE": ["PC-EU-11"], "UK": ["PC-UK-08"]}),
    (r"\ball (patients|patient groups|people)\b|\beveryone\b|\bany patient\b", "population wider than studied",
     {"US": ["PC-US-23", "PC-US-27"], "EU": ["PC-EU-02"], "DE": ["PC-EU-02"], "UK": ["PC-UK-06"]}),
    (r"\bthe evidence shows\b|\bstudies show\b", "single study presented as a body of evidence",
     {"ALL": ["certainty-wording.md rule 6"]}),
]

CERT_RE = re.compile(r"\b(very low|low|moderate|high)\b[^.\n]{0,40}\bcertainty\b|\bcertainty\b[^.\n]{0,40}\b(very low|low|moderate|high)\b", re.I)
EFFECT_VERB_RE = re.compile(r"\b(reduces|reduced|increases|increased|results? in|resulted in|improves|improved|lowers|lowered|fell|falls|dropped|drops|treats)\b", re.I)
HEDGE_MOD_RE = re.compile(r"\b(likely|probably)\b", re.I)
HEDGE_LOW_RE = re.compile(r"\b(may|might|evidence suggests|very uncertain)\b", re.I)
NO_EFFECT_RE = re.compile(r"\bno (effect|difference)\b|\bno different\b|\bdoes not (reduce|increase|improve)\b", re.I)
NUM_RE = re.compile(r"(?<![\w.])[-+]?\d+(?:[.,]\d+)?(?![\w])")


def norm_num(s):
    return s.replace(",", ".").lstrip("+")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--draft", required=True)
    ap.add_argument("--evidence", required=True)
    ap.add_argument("--market", default="ALL", choices=["ALL", "US", "EU", "DE", "UK"])
    a = ap.parse_args()
    draft = open(a.draft, encoding="utf-8").read().strip()
    try:
        ev = json.load(open(a.evidence, encoding="utf-8"))
    except (OSError, ValueError) as e:
        sys.exit(f"Refused: the evidence file could not be read as JSON ({e}).")
    outcomes = ev.get("outcomes") or []
    if not draft or not outcomes:
        sys.exit("Refused: an empty draft or no outcomes. Supply the draft and at least one outcome with its passage.")
    passages = " ".join(p for o in outcomes for p in (o.get("passages") or []))
    if not passages.strip():
        sys.exit("Refused: no passages supplied. A statement with no passage is [GAP], not checkable.")

    print("# Statement check (first pass for a person to judge)\n")
    # 1. numbers
    pnums = {norm_num(n) for n in NUM_RE.findall(passages)}
    pnums |= {n.lstrip("-") for n in pnums}
    print("## Numbers not found in any supplied passage")
    missing = []
    for m in NUM_RE.finditer(draft):
        n = norm_num(m.group())
        if n not in pnums and n.lstrip("-") not in pnums:
            ctx = draft[max(0, m.start() - 30): m.end() + 30].replace("\n", " ")
            missing.append(f"- {m.group()} in \"...{ctx}...\"")
    print("\n".join(missing) if missing else "- none")

    # 2. certainty
    print("\n## Certainty wording against the person's ratings")
    rated = [(o.get("outcome"), (o.get("certainty") or "").lower(), o.get("rated_by")) for o in outcomes]
    rated_levels = [LEVELS[c] for _, c, _ in rated if c in LEVELS]
    hits = []
    for m in CERT_RE.finditer(draft):
        word = (m.group(1) or m.group(2)).lower()
        if not rated_levels:
            hits.append(f"- \"{m.group()}\": no outcome has a rating from a person or body [GAP]")
        elif LEVELS[word] > max(rated_levels):
            hits.append(f"- \"{m.group()}\": higher than every supplied rating ({', '.join(f'{o}: {c or 'not rated'}' for o, c, _ in rated)})")
    print("\n".join(hits) if hits else "- none")
    for o, c, r in rated:
        if c in LEVELS and not r:
            print(f"- rating for '{o}' has no rater named: say who rated it")

    # 3. certainty verbs (Table 15.6.b)
    print("\n## Certainty verbs against Table 15.6.b for the highest rating supplied")
    top = max(rated_levels) if rated_levels else 0
    vhits = []
    for sent in re.split(r"(?<=[.;])\s+|\n+", draft):
        if not sent.strip():
            continue
        if HEDGE_MOD_RE.search(sent) and top < LEVELS["moderate"] and not HEDGE_LOW_RE.search(sent):
            vhits.append(f"- \"{sent.strip()[:120]}\": \"likely\"/\"probably\" is moderate-certainty wording (ES-204); highest rating supplied: {('not rated' if not top else [k for k, v in LEVELS.items() if v == top][0])}")
        m = EFFECT_VERB_RE.search(sent)
        if m and top < LEVELS["high"] and not HEDGE_MOD_RE.search(sent) and not HEDGE_LOW_RE.search(sent) \
                and not re.search(r"\b(authors?|report(s|ed)?|as reported|showed|found)\b", sent, re.I):
            vhits.append(f"- \"{sent.strip()[:120]}\": unhedged \"{m.group()}\" is high-certainty wording (ES-203); hedge to the rating given (ES-204 to ES-206) or attribute it to the source")
        if NO_EFFECT_RE.search(sent):
            vhits.append(f"- \"{sent.strip()[:120]}\": check the interval; a wide interval including no effect is not \"no effect\" (ES-207)")
    print("\n".join(vhits) if vhits else "- none")

    # 4. wording
    print(f"\n## Wording tied to sourced rows (market: {a.market})")
    found = 0
    for pat, note, rows in WORDING:
        for m in re.finditer(pat, draft, re.I):
            sel = rows.get("ALL", []) + ([r for k, v in rows.items() if k != "ALL" for r in v] if a.market == "ALL" else rows.get(a.market, []))
            if not sel:
                continue
            found += 1
            ctx = draft[max(0, m.start() - 25): m.end() + 25].replace("\n", " ")
            print(f"- \"{m.group()}\" ({note}): {', '.join(dict.fromkeys(sel))}. Context: \"...{ctx}...\"")
    if not found:
        print("- none (no flag means no listed pattern matched; it is not a clearance)")
    print("\nEvery hit is a candidate for the owner the person names for regulatory or legal review, or owner not named. The script clears nothing.")


if __name__ == "__main__":
    main()
