# Price rules and registered prices: what is fact, what is hypothesis

Interpretive reference for task A2. Rows cited from `coding-pricing-sources.md`, `access-monitoring-sources.md` (DE-9, DE-10), `outcomes-contracting-sources.md` and `france-pecan-lppr-latm.md`. Read on 19 October 2026; not owner-reviewed.

## Three kinds of number, never mixed

| Kind | Examples | How it is labeled |
|---|---|---|
| Rule | A threshold, a group maximum, a conversion factor, a mandatory share | Fact, with row id and validity window |
| Registered price | A comparator's stored DiGA price, a CMS national amount, a French fee in an arrêté | Fact about that product or code, with source and retrieval date |
| Model output | `get_pricing_corridor` spread, `vba-price-anchor` ceiling, `budget-impact-model` result | Hypothesis, on the person's inputs; never a price for the product |

The skill never outputs a price for the person's product. A pricing position stops for its owner.

## Germany

| Rule | Value | Row |
|---|---|---|
| Who sets the price after year one | GKV-Spitzenverband with the manufacturer, binding on all funds | DE1 |
| Year-one price | The manufacturer's actual price, in any case for at least one year after listing | DE7, DE9 |
| Arbitration | No agreement within nine months of listing: arbitration board sets the amount within three months; a lawsuit does not suspend it | DE5, DE6 |
| Price criteria | Extent of proven medical benefit and/or patient-relevant structural and procedural improvements | DE12 |
| Outcome-linked share | At least 20 percent of the amount from 1 January 2026 | DE2 |
| Volume discount | From 1 January 2027: at least 2 percent above 3,000 units a year, at least 30 percent above 100,000 | DE3 |
| Threshold | No negotiation needed below it. Definition: daily price at 25 percent of the average of all listed DiGA, plus rolling annual GKV revenue of EUR 750,000 incl. VAT | DE10 (framework) |
| Current threshold | EUR 0.84 per calendar day incl. VAT, valid 1 October 2026 to 31 March 2027 | DE14 |
| Group maximums | Groups by indication and kind of care effect; set only where at least two DiGA fall in a group | DE11 |
| Current group maximums | Urogenital, medical benefit: EUR 7.56 per day (5.67 above 10,000 codes; 6.05 trial; 4.54 trial above 10,000). Mental disorders, medical benefit: EUR 6.66 per day (5.00; 5.33; 4.00). Only these two groups published | DE14 |
| Maximum mechanics | Not applied in year one up to 2,000 redeemed codes; above 10,000 codes falls to 75 percent (permanent) or 60 percent (trial); trial listings get 80 percent | DE15 |
| Update cycle | Half-yearly, 1 April and 1 October; manufacturer notifies at 2,001 and 10,001 codes | DE16 |
| Directory publishes amounts | Prescription periods and amount per period | DE20 |

Unresolved: the 2024 framework says outcome components "can" be agreed; the statute makes 20 percent mandatory; no implementing agreement found (coding file Changes and conflicts 6, Not sourced 9). How the 2027 volume discount interacts with the maximum reductions is not sourced (Changes and conflicts 8).

National price context (payer's statutory report, GKV25; context, never a target):

| Figure | Value | Row |
|---|---|---|
| Negotiated vs manufacturer | Negotiated prices for 40 DiGA average 227 EUR per quarter, 325 EUR (59 percent) below the 552 EUR manufacturer prices they replaced; average manufacturer price 566 EUR at 31 December 2025; range 119 to 2,077.40 EUR | DE-9 |
| Cut on permanent listing | Permanent from the start: average cut 57 percent. Trial then permanent: average cut 51 percent | DE-10 |

Library caveat: the DE_DIGA `price` field does not say whether it is a manufacturer or negotiated amount, nor its prescription period. State both as `[GAP]` and point to the directory page (DE20).

## United States

| Rule | Value | Row |
|---|---|---|
| Payment formula | RVUs x conversion factor x geographic adjustment | US8 |
| CY 2026 conversion factors | 33.5675 USD (qualifying APM); 33.4009 USD (non-qualifying APM) | US8 |
| No national floor | Geographic practice cost indices are required by statute | US9 |
| Work RVU decisions 2026 | 99470: 0.31; 99457: 0.61 | US5 |
| Device-supply method | OPPS geometric mean cost divided by the conversion factor; 99445 and 99454 get the same value | US6 |
| DMHT G0552 | Contractor priced; no national amount; commenters report inconsistent MAC rates | US19 |
| ACCESS annual allowed amounts | eCKM 360/180; CKM 420/210; MSK 180/none; BH 180/90 USD (initial/follow-on), rural add-on 15 USD; 5 July 2026 to 31 December 2027 | US31 |
| ACCESS mechanics | 50 percent of the Medicare portion withheld; the Medicare portion is 80 percent of the allowed amount and both downward adjustments apply to it, never to the allowed amount (BH initial: $180 allowed, $144 Medicare portion, $72 withheld; outcomes file, "ACCESS: Medicare portion and payment basis"); outcome attainment threshold 50 percent; substitute spend threshold 90 percent; 5 percent multi-track discount | US32, US33 |

National amounts per code are not in the research file (Not sourced 1). The library stores them for seven codes, each passage citing "CMS PFS Indicators for 2026, updated 1 October 2026" (live call 19 October 2026): 99453 21.71; 99454 52.11; 99457 51.77 non-facility, 26.39 facility; 99458 41.42 / 26.39; G0553 54.11 / 26.05; G0554 41.42 / 25.38 USD, all at the non-qualifying conversion factor. `scripts/price_facts.py` recomputes each from its RVU. Quote them as "library row, national, before geographic adjustment".

## France

| Rule | Value | Source |
|---|---|---|
| Price setter for LPP | CEPS, after HAS evaluation (official agency explainer, class V) | FR1, FR3 |
| Criteria | Article L.165-2 CSS, text not read | FR2 |
| Price vs tariff | LPP price may exceed the reimbursed tariff; no predefined range | FR5 |
| PECAN therapeutic | Maximum 780 EUR incl. tax per patient per year; 435 EUR first quarter, 38.3 EUR per month from month 4 | France file, PECAN payment rows |
| PECAN telemonitoring | "from 50 € TTC" monthly, degressive | France file, PECAN payment: telemonitoring |
| LATM fees | Set by the arrêté of 16 May 2023; amounts not read | France file, LATM evaluation: tariffs; Not sourced 5 |

## England

MedTech Funding Mandate price test: cost saving within 3 years and budget impact not above GBP 20 million in any of the first 3 years (EN1, [WF]). No national price exists for a digital therapy in the pages read.

## Tools that produce numbers (hypotheses)

- `commercial-dh.get_pricing_corridor`: returns stored prices, but for a DiGA it mixes the product's own price with the ten most recent DiGA listings in any indication (live call 19 October 2026). Use only the row for the named product; take comparators from `find_scheme_precedents` with an indication.
- `analytics.vba-price-anchor`: inverts a willingness-to-pay threshold on the person's comparator cost and QALY gain. Output is a ceiling on the person's assumptions, labeled hypothesis.
- `analytics.budget-impact-model`: multi-year impact on the person's population, mix, cost and uptake. Returned HTTP 422 on every argument shape tried on 19 October 2026; see `tools.md`.
