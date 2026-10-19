# Price evidence: what is fact, what is hypothesis

Interpretive reference for task A2. Rows cited from `payer-price-facts.md` (copied from the Market Access pack) and `promotion-and-claims-research.md`. Live behavior from calls on 19 October 2026 (`examples/live/`). Not owner-reviewed.

## Three kinds of number, never mixed

| Kind | Examples | How it is labeled |
|---|---|---|
| Rule | A threshold, a group maximum, a conversion factor | Fact, with row id and validity window |
| Registered price | A comparator's stored DiGA price, a CMS national amount | Fact about that product or code, with source URL and retrieval date |
| Model output | `vba-price-anchor` ceiling, budget impact on the person's inputs | Hypothesis on the person's inputs; never a price for the product |

The skill never outputs a price for the person's product. A corridor end is the person's; the model gives the reason each end could rest on, labeled "proposed" until the person adopts it.

## The corridor, end by end

The old method holds: name the floor and the ceiling with currency; tie the floor to cost or to the smallest comparators the person will name; tie the ceiling to the outcome or the budget the person will cite, or mark it `[GAP]`. Do not publish a single price with no corridor when buyer sets differ.

| End | Evidence that can support it | Where it comes from |
|---|---|---|
| Floor | The person's unit cost; the lowest registered comparator price in the same indication and scheme | The person; `find_scheme_precedents` |
| Ceiling | A value-based anchor on the person's comparator cost, QALY gain and threshold; a payer cap where one exists | `analytics.vba-price-anchor`; payer rows below |
| Context only | National averages, negotiated-versus-manufacturer gaps | DE-9, DE-10 |

## Payer rules that cap or shape a commercial price (context, owned by dh-market-access)

| Market | Rule | Row |
|---|---|---|
| Germany | Manufacturer price applies from listing, in any case for at least one year; then the GKV-Spitzenverband amount | DE1, DE7, DE9 |
| Germany | Threshold EUR 0.84 per calendar day incl. VAT; group maximums for two groups only (urogenital, medical benefit EUR 7.56 per day; mental disorders, medical benefit EUR 6.66 per day), valid 1 October 2026 to 31 March 2027 | DE14 |
| Germany | Maximums not applied in year one up to 2,000 redeemed codes; trial listings get 80 percent of the group maximum; above 10,000 codes 75 percent (permanent) or 60 percent (trial) | DE15 |
| Germany | Negotiated price reflects the extent of proven medical benefit and/or patient-relevant structural and procedural improvements | DE12 |
| Germany | Negotiated prices for 40 DiGA average 227 EUR per quarter, 325 EUR (59 percent) below the 552 EUR manufacturer prices they replaced | DE-9 |
| United States | Payment = RVUs x conversion factor x geographic adjustment; CY 2026 conversion factors 33.5675 and 33.4009 USD | US8 |
| United States | G0552 contractor priced, no national rate | US19 |
| France | LPP price may exceed the reimbursed tariff; rate set after CEPS negotiation, no predefined range | FR5 |
| England | MedTech Funding Mandate: cost saving within 3 years and budget impact not above GBP 20 million in any of the first 3 years [WF] | EN1 |

Anything a payer sets, codes, negotiates or reimburses is answered by dh-market-access (coding-pricing-and-payer-contracting). Use these rows to say where a commercial price would meet a payer rule, then point there.

## Comparators

- Comparators come from `market-access-dh.find_scheme_precedents` with the product's indication, in the register's language or code (for DE_DIGA an ICD-10-GM code such as "F51" or a German term). Each comparator carries its source URL and retrieval date.
- A comparator shows that a price was registered for that product, not that the person's product would get it.
- DE_DIGA `price` carries no unit, no prescription period and no flag for manufacturer versus negotiated amount. Say so with each German comparator.
- `commercial-dh.get_pricing_corridor` is not a comparator corridor (register N4). For somnio on 19 October 2026 it returned somnio's own price twice (224.99 EUR, once with no source URL) and ten prices between 490 and 795 EUR from the ten most recent DE_DIGA listings in any indication, without product names, while the three insomnia DiGA in the same store carry 224.99, 236 and 241.25 EUR. Use only the row for the named product; `scripts/comparator_prices.py` separates the rows.

## Value-based anchor

- `analytics.vba-price-anchor` returns, per threshold, `value_based_budget_per_patient` = comparator cost per patient + incremental QALYs x threshold + `non_drug_cost_offset_per_patient` (returned as 0 by default), divided by `units_per_patient` (returned as 1). Live check: comparator 800, 0.03 QALY, thresholds 20,000 and 30,000 returned 1,400 and 1,700, which matches that arithmetic.
- The tool cites Neumann, Cohen and Weinstein (2014) and the NICE manual (2022) as method sources. Those citations are the tool's; this skill does not source any threshold value. The threshold is the person's, and the output is a ceiling on the person's assumptions, labeled hypothesis.
- Pass thresholds as a plain list of numbers; objects return HTTP 422 (register N5).

## Budget impact

`analytics.budget-impact-model` returned HTTP 422 on 19 October 2026 again (register N5; earlier builds tried four other shapes). Until fixed, run the arithmetic in the conversation on the person's numbers, show every step, and label it a hypothesis: for each year, eligible population x uptake share x (new annual cost per patient minus the weighted current annual cost per patient).

## Payor communication of price evidence

A budget-impact model or a value-based price analysis shown to a payor is health care economic information in the United States (PC-US-06, PC-US-36). That moves it into task B1 and its stops.
