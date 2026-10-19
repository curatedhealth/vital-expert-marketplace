# Worked example: B1 on live connector calls

Live library calls on 19 October 2026. The scores, weights and RICE inputs below were typed for the measurement and are presented as the example person's numbers; they are illustrative, not anyone's real scores. Saved outputs are in `examples/live/`.

**Request:** "We have an FDA-cleared ADHD digital therapy (we say it is classified under 21 CFR 882.5803). Three partner options for the US: a behavioral health group practice network, a regional health-system reseller, an EHR marketplace listing. My scores and weights are below. Rank them, tell me how solid the order is, and what we have to sort out first. Our partnerships committee decides."

| Option | Buyer access | Compliance fit | Implementation capacity | Strategic alignment |
|---|---|---|---|---|
| Behavioral health group practice network | 4 | 2 | 2 | 4 |
| Regional health-system reseller | 3 | 2 | 3 | 2 |
| EHR marketplace listing | 2 | 4 | 1 | 3 |
| Weight | 0.35 | 0.25 | 0.20 | 0.20 |

**Calls made**

1. `analytics.mcda` with the three options and the weights above. The first two attempts returned HTTP 503 ("Nothing was counted"); the retry after a pause answered. Saved as `mcda_partner_options.json`.
2. `python3 scripts/rank_check.py examples/live/mcda_partner_options.json`: values match the connector; swap points computed.
3. `diligence-dh.build_company_profile {company: "Akili Interactive Labs, Inc."}`, to show what a peer record states for the same classification (`partner_profile_akili.json`).

## Answer (short mode)

**Your order.** On your scores and weights: practice network 77.5, health-system reseller 63.75, EHR marketplace 62.5 (analytics.mcda, EVIDEM weighted sum). The ranking reflects your scores; it is not a recommendation.

**How solid.** The top place holds unless implementation capacity carried a weight of about 0.48 instead of 0.20. Second and third are nearly tied: moving implementation capacity from 0.20 to about 0.18, or strategic alignment from 0.20 to about 0.24, swaps them. Treat second place as open.

**Facts that bear on the choice.**
- The practice network route runs through DMHT billing. G0552 is payable only for 510(k) or De Novo devices classified at 882.5801 or, for CY 2026, 882.5803 (CP-US-58, CP-US-62), and only if the billing practitioner incurs the device cost (CP-US-59). The practice is the buyer of the device; your product's classification is as you stated it.
- A reseller or EHR partner that touches PHI is a subcontractor business associate and needs a BAA with the required clauses (CP-US-44 to CP-US-48).
- For context, the library's record for a product in the same regulation (EndeavorRx, K231337, 882.5803, cleared 13 December 2023) is a public record, not a comparison with your product.

**What to settle first.** How each partner is paid. If any option pays per referral, per patient or on outcomes, that is a stop for your compliance owner before any agreement (CP-US-01, CP-US-08; outcomes-based payments by device makers are excluded from the safe harbor, CP-US-13). Then data terms before any data flows (CP-US-46).

**Stops.** The partner choice is your partnerships committee's. Compensation design goes to your compliance or legal owner (owner not named: who is it?).

**Gaps.** Whether a DMHT-billing practitioner network will buy at the device cost you set: not in the sources `[GAP]`; that is your commercial judgment and Market Access's payment question.

**Record:** Prioritization draft. Scores, weights and the choice are yours. AI-assisted. Uncleared.

Full version available with the facts-per-option table and the dependency sequence.

## What this example shows

- The model ranks only the person's scores and checks the connector's arithmetic.
- The near-tie is shown as fragile instead of hidden behind a single order.
- Channel facts come from rows, the peer record is described only by what it states, and compensation goes to the compliance owner before anything is signed.
