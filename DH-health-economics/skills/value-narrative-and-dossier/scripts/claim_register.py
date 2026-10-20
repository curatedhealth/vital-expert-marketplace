#!/usr/bin/env python3
"""Build a claim register from verify.check_claim results plus a reader's fields.

Usage:
    python3 claim_register.py CHECKS.json [--format md|json]

CHECKS.json is either a list of claim objects or an object with a
"check_claim_calls" list (as in examples/live/verify_dcbti_pregnancy.json).
Each claim object holds:
    id, claim (text), status (from check_claim), rationale (from check_claim),
    passage, locator,
    same_direction  (true / false / missing: the reader's own reading)
    mismatch        (text, empty if none: e.g. "population widened")
    certainty       (the person's GRADE rating for that outcome, or null)
    certainty_by    (who rated it, or null)

A claim may enter the narrative only when check_claim returned "supported",
the reader marked same_direction true, no mismatch is recorded and a passage
exists. Certainty never comes from a tool: an empty rating stays [GAP].
The script also screens claim wording for terms the sourced rows bind
(references/certainty-and-wording.md), including certainty verbs stronger than
Table 15.6.b allows for the rating given (ES-203 to ES-206). It decides nothing for the person.
"""
import json
import re
import sys

OVERREACH = [
    (r"\bprove[sdn]?\b|\bproof\b", "states proof; conclusions are the person's or the HTA body's (PC-US-01, PC-US-03)"),
    (r"\bcure[sd]?\b", "cure claim (PC-EU-10, PC-DE-03)"),
    (r"\bguarantee[sd]?\b", "guaranteed success (PC-DE-04)"),
    (r"\bno side effects?\b|\bno harm", "no harmful effects (PC-DE-04)"),
    (r"\bcost[- ]effective\b", "cost-effectiveness stated as fact; HCEI for US payors (PC-US-04, PC-US-06, PC-US-40)"),
    (r"\bsave[sd]? money\b|\bcost[- ]saving\b", "savings stated as fact; HCEI for US payors (PC-US-06)"),
    (r"\ball patients\b|\bevery\b|\balways\b", "universal wording; check population against the passage (PC-US-27, PC-EU-02)"),
]


# Certainty verbs, Cochrane Handbook 6.5 Table 15.6.b (ES-203 to ES-206): an unhedged effect verb
# is high-certainty wording, "likely"/"probably" moderate, "may"/"the evidence suggests" low,
# "the evidence is very uncertain" very low. The rating is the person's; the script only compares.
LEVELS = {"very low": 1, "low": 2, "moderate": 3, "high": 4}
EFFECT_VERB = re.compile(r"\b(reduce[sd]?|increase[sd]?|improve[sd]?|lower(s|ed)?|results? in|resulted in|fell|dropped)\b", re.I)
HEDGE_MOD = re.compile(r"\b(likely|probably)\b", re.I)
HEDGE_LOW = re.compile(r"\b(may|might|evidence suggests|very uncertain)\b", re.I)


def verb_flag(text, cert):
    level = LEVELS.get((cert or "").strip().lower(), 0)
    if HEDGE_LOW.search(text):
        return None
    if HEDGE_MOD.search(text):
        if level < LEVELS["moderate"]:
            return "wording: 'likely'/'probably' is moderate-certainty wording (ES-204); rating is " + (cert or "not given")
        return None
    if EFFECT_VERB.search(text) and level < LEVELS["high"]:
        return "wording: unhedged effect verb is high-certainty wording (ES-203); word it to the rating (ES-204 to ES-206) or attribute it to the source; rating is " + (cert or "not given")
    return None


def load(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    items = data.get("check_claim_calls") if isinstance(data, dict) else data
    if not isinstance(items, list) or not items:
        raise SystemExit("No claims found: give a list or an object with 'check_claim_calls'.")
    return items


def overlap(rationale):
    m = re.search(r"(\d+)%", rationale or "")
    return int(m.group(1)) if m else None


def decide(c):
    reasons = []
    text = (c.get("claim") or "").strip()
    if not text:
        raise SystemExit(f"Claim {c.get('id')} has no text.")
    status = (c.get("status") or "not checked").lower()
    passage = (c.get("passage") or "").strip()
    sd = c.get("same_direction")
    mismatch = (c.get("mismatch") or "").strip()
    if not passage:
        reasons.append("no passage [GAP]")
    if status != "supported":
        reasons.append(f"check_claim returned {status}")
    if sd is None:
        reasons.append("passage not yet read by a person: hold until read")
    elif sd is False:
        reasons.append("passage does not state the claim in the same direction")
    if mismatch:
        reasons.append(mismatch)
    flags = []
    if status == "supported" and (sd is False or mismatch):
        flags.append("tool said supported; the reading disagrees (register N3)")
    if status in ("unsupported", "partial") and sd is False and "opposite" in mismatch:
        flags.append("passage states the opposite; tool did not return contradicted (register N3)")
    for pat, why in OVERREACH:
        if re.search(pat, text, re.I):
            flags.append("wording: " + why)
    cert = c.get("certainty")
    vf = verb_flag(text, cert)
    if vf:
        flags.append(vf)
    cert_txt = f"{cert} ({c.get('certainty_by') or 'rater not named'})" if cert else "[GAP] not yet rated by a person"
    return {
        "id": c.get("id"),
        "claim": text,
        "status": status,
        "overlap_pct": overlap(c.get("rationale")),
        "locator": c.get("locator") or "[GAP]",
        "may_enter": not reasons,
        "held_because": reasons,
        "flags": flags,
        "certainty": cert_txt,
    }


def to_md(rows):
    out = ["| # | Claim | Verify status (overlap) | Locator | May enter? | Held because | Flags | Certainty |",
           "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        ov = f"{r['overlap_pct']}%" if r["overlap_pct"] is not None else "n/a"
        out.append("| {} | {} | {} ({}) | {} | {} | {} | {} | {} |".format(
            r["id"], r["claim"], r["status"], ov, r["locator"],
            "yes" if r["may_enter"] else "no",
            "; ".join(r["held_because"]) or "",
            "; ".join(r["flags"]) or "",
            r["certainty"]))
    n = sum(r["may_enter"] for r in rows)
    out.append("")
    out.append(f"{n} of {len(rows)} claims may enter. Certainty ratings are the person's; the script never fills them.")
    return "\n".join(out)


def main(argv):
    if len(argv) < 2:
        raise SystemExit(__doc__)
    rows = [decide(c) for c in load(argv[1])]
    fmt = argv[argv.index("--format") + 1] if "--format" in argv else "md"
    print(json.dumps(rows, indent=2, ensure_ascii=False) if fmt == "json" else to_md(rows))


if __name__ == "__main__":
    main(sys.argv)
