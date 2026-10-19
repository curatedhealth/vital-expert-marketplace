# Worked example: A2 scorecard and B1 action on illustrative data

The handoff log and measure sheet are ILLUSTRATIVE files written to test the skill (`examples/handoff_log_illustrative.csv`, `examples/measures_illustrative.json`); the partners "Reseller A" and "Implementer B" are invented. The public-signal call is live, 19 October 2026 (`examples/live/diligence_deltas.json`).

**Request:** "Q3 partner review. Here is our handoff log and the measure sheet we agreed. Reseller A says they sent us 9 leads in August alone. Also one of their webinar slides said 'FDA-registered, so you know it is approved'. Score both partners and tell me what our rules say we do. Our VP Partnerships owns partner actions; Legal owns claims."

**Calls made**

1. `python3 scripts/partner_scorecard.py examples/handoff_log_illustrative.csv examples/measures_illustrative.json`: output in `examples/scorecard_illustrative_output.md`.
2. `diligence-dh.get_deltas {companies: ["Akili Interactive Labs, Inc.", "Pear Therapeutics, Inc."], since: "2026-01-01"}` was run on public names to measure the tool; it is not about these partners. Reseller A and Implementer B are not regulated companies, so no public-signal call applies to them.

## Answer (short mode)

**Reseller A: hold, by your rule.** One claim breach in Q3 against your rule of zero, and you set claim breaches to force a hold. Qualified buyers handed off: 4 against your threshold of 6 (missed). Implementations started: 2 against 2 (met).

**Implementer B: continue, by your rules.** Implementations started: 3 against 3 (met). Claim breaches: 0 (met).

**Not counted.** Reseller A's report of 9 August leads carries no buyer ids; one further reported lead (HS-190, 12 September 2026) is not in your record. Neither counts. One reported lead (HS-101) matches your record and is already counted. Implementer B shows an implementation for HS-104, a buyer Reseller A handed off: not counted for Implementer B.

**Claim breach, for Legal.** Reseller A webinar, 18 September 2026, slide 7: "FDA-registered, so you know it is approved". Registration does not denote approval, and a representation creating that impression is misbranding (CP-US-74). Whether and how to correct it is Legal's decision; the register rule you confirmed says the partner is not continued while the breach is open.

**The decision needed.** Your VP Partnerships decides the hold on Reseller A and the date it is told (date not set). Any notice to the partner is a draft for that owner.

**Hypotheses for the handoff miss (to test, not findings).** The partner may count leads before your handoff event: compare its August list with your record. Buyers may be reaching you directly after partner contact: check source fields for HS-190.

**Duty checks.** Breach-notice terms and sub-processor terms were not in the data given: not shown.

**Record:** Scorecard and action review draft on your data and rules. AI-assisted. Uncleared.

## What this example shows

- Counts come from the person's record; the partner's own number is shown and not counted.
- The hold follows the person's rule, the owner is the one they named, and the date stays theirs.
- The claim breach is quoted and routed to Legal with its row, not judged.
- Missing evidence of a duty is "not shown", never "breached".
