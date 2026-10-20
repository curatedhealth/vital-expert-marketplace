# Worked example: A2 price corridor evidence (live library data, 19 October 2026)

**Request (illustrative person):** "We are preparing a German launch for an insomnia app that will apply as a DiGA. What do registered comparators say about our corridor? Use somnio as the reference product. For a ceiling, run the anchor on our numbers: comparator cost 800 EUR per patient, 0.03 QALY gain, thresholds 20,000 and 30,000. Our pricing owner is the Head of Market Access."

The comparator cost, QALY gain and thresholds are illustrative numbers typed for this example, not anyone's product data. Library data is live.

## Calls made

1. `commercial-dh.list_commercial_dh_sources {}` (free): DE_DIGA 82 listings, loaded 15 October 2026, posture partial.
2. `commercial-dh.get_pricing_corridor {reference: "somnio"}`: 12 price rows; kept the one with somnio's source URL (`examples/live/pricing_corridor_somnio.json`).
3. `market-access-dh.find_scheme_precedents {scheme: "DE_DIGA", indication: "F51", limit: 10}`: 3 insomnia DiGA (`examples/live/precedents_DE_DIGA_F51.json`).
4. `analytics.vba-price-anchor {comparator_cost_per_patient: 800, incremental_qalys: 0.03, wtp_thresholds: [20000, 30000]}` (`examples/live/vba_price_anchor.json`).
5. `scripts/comparator_prices.py corridor` and `precedents` on the saved outputs.

## Answer (short mode)

**Answer.** Three permanently listed insomnia DiGA carry stored prices of 224.99 to 241.25 EUR in the library (retrieved 15 October 2026). The stored price has no unit or prescription period, so these are not yet comparable to a daily or quarterly figure. Your anchor on your own numbers gives ceilings of 1,400 and 1,700 EUR per patient, a hypothesis far above the registered range. The corridor and both ends are yours to set.

**Comparators (DE_DIGA, indication F51)**

| Product | Status | Listed on | Price as stored | Source, retrieved |
|---|---|---|---|---|
| somnio | permanent | 22 October 2020 | 224.99 EUR | diga.bfarm.de/de/verzeichnis/00508, 15 October 2026 |
| somnovia | permanent | 28 October 2024 | 236 EUR | diga.bfarm.de/de/verzeichnis/02097, 15 October 2026 |
| HelloBetter Schlafen | permanent | 18 December 2022 | 241.25 EUR | diga.bfarm.de/de/verzeichnis/01772, 15 October 2026 |

Low 224.99, high 241.25 EUR, three rows. Whether each is a manufacturer or a negotiated amount is not stored `[GAP]`; the directory publishes prescription periods and amounts (DE20). The corridor tool also returned ten prices of 490 to 795 EUR from DiGA in other indications, without names; they were set aside (register N4).

**Payer rules that bind (context; payer pricing is dh-access-and-value).** The manufacturer price applies for at least one year after listing, then the GKV-Spitzenverband amount (DE1, DE9). The group maximum for mental disorders, medical benefit, is EUR 6.66 per day, 80 percent of that for a trial listing, valid 1 October 2026 to 31 March 2027 (DE14, DE15); whether an insomnia DiGA falls in that group is `[GAP]` (DE11).

**Your anchor (hypothesis).** 800 + 0.03 x 20,000 = 1,400 EUR; at 30,000: 1,700 EUR. The tool applied a cost offset of 0 and one unit per patient.

**Reasons per end.** Floor: your unit cost `[GAP]`; lowest registered comparator 224.99 EUR. Ceiling: anchor 1,400 to 1,700 EUR on your assumptions; a group maximum, if the product falls in a group, caps the price once it applies (DE15). Ends: not set `[GAP]`.

**Gaps.** Price unit and period not stored; group assignment not sourced; your unit cost not given.

**Record.** Price positions stop for the Head of Market Access. Library records retrieved 15 October 2026; confirm on the directory. Uncleared draft, AI-assisted.

Word count of the answer above, excluding the calls list and the table's source column: 328 (counted by script).
