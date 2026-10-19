# Worked example: A1 coding pathway map, US, digital CBT app for depression

Live library calls on 19 October 2026. Shown so the model sees the shape of a good answer, not to be reused as current fact.

**Request:** "Our CBT app for depression has FDA De Novo authorization under 21 CFR 882.5801. We sell to patients directly today. Which Medicare codes could pay for it, and what is changing for 2027? Quick version."

**Calls made**

1. `market-access-dh.list_schemes` (free): US_CMS_RPM 4 listings, US_CMS_DMHT 3 listings, both loaded 15 October 2026, posture partial.
2. `market-access-dh.find_scheme_precedents {scheme: "US_CMS_DMHT", limit: 25}`: G0552, G0553, G0554.
3. `market-access-dh.find_scheme_precedents {scheme: "US_CMS_RPM", limit: 25}`: 99453, 99454, 99457, 99458.
4. `scripts/price_facts.py examples/library_codes_and_prices_2026-10-19.json --as-of 2026-10-19`: output in `price_facts_2026-10-19.txt`. Every stated amount equals RVU x 33.4009; four rows have an empty `price` field although the passage states the amount.

## Answer (short mode)

**Answer.** The route that fits is the digital mental health treatment codes G0552 to G0554. Your classification (882.5801, as you state it) meets the device condition (US17). The deciding condition is commercial, not clinical: the billing practitioner must incur the cost of the device, and supply must be incident to their services under a behavioral health plan of care (US17). A direct-to-consumer sale does not fit that; CMS itself says the cost-bearing condition may not fit direct-to-consumer models and that claims volume has stayed low (US20).

**Routes.**

| Route | Codes | What is paid | Who bills | Fits? | Source |
|---|---|---|---|---|---|
| DMHT | G0552 device supply and onboarding; G0553 first 20 min; G0554 each further 20 min | Practitioner's service plus device supply | Practitioner who bought the device | Fits on device class; unclear on the sales model | US16, US17; library rows, retrieved 15 October 2026 |
| RPM | 99453, 99454, 99457, 99458 (stored); 99445, 99470 (not stored) | Physiologic monitoring service | E/M-eligible practitioner | Unclear: a CBT app does not obviously collect physiologic data `[GAP]` | US2, US15 |
| RTM | 98975 to 98986, incl. 98986 (CBT device supply, 2 to 15 days) | Therapeutic monitoring service | Same as RPM | Possibly, as an alternative to DMHT; not stored in the library | US3, US4, US7 |
| ACCESS (BH track) | G0674, G0675 | Outcome-aligned monthly payment to a participant | A Part B enrolled organization, not you | Only as a vendor to a participant | US29, US35 |

**Stored amounts** (national, before geographic adjustment; not a payment your product will receive): G0553 54.11 USD non-facility, 26.05 facility; G0554 41.42 and 25.38; G0552 contractor priced, no national amount, each MAC sets it (US19). Source: library rows citing CMS PFS indicators for 2026, retrieved 15 October 2026.

**Conflicts.** RPM and RTM cannot be billed together (US12). G0552/G0553 and RTM set-up 98975 billed by another provider count as substitute spend against an ACCESS behavioral health participant (US34).

**Pending for 2027 (proposed 16 July 2026; final rule not published as of 19 October 2026).** RTM limited to established patients (US23); RPM/RTM to start in a face-to-face visit (US24); a possible collapse of 17 monitoring codes into four G-codes, one naming digital therapeutic interventions (US27). DMHT changes were not among the proposals read.

**Check.** 1. Your classification against the FDA record (the regulatory owner confirms it). 2. Your MAC's G0552 rate. 3. The CY 2027 final rule when published.

**Record.** Uncleared draft. Coding and sales-model decisions stop for the accountable owner.

## Why this is a good answer

It names the condition that decides (who buys the device), not just the codes. It keeps proposed rules separate from law. It reports stored amounts with their setting and limits, and flags G0552 as contractor priced instead of inventing a figure. It does not assert the product's classification; it repeats the person's statement and routes confirmation to the owner.
