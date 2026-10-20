# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `market-access-dh_find_scheme_precedents`). Counted calls draw on the library key's monthly allowance; free calls do not.

Behavior below was observed in live calls on 19 October 2026. Saved output: `examples/library_codes_and_prices_2026-10-19.json` and `examples/tool_test_calls_2026-10-19.json`.

## market-access-dh.list_schemes (free)

- No arguments. 16 schemes with authority, pathway kind, clock rule, listing count, last load, posture.
- On 19 October 2026: US_CMS_RPM 4 listings, US_CMS_DMHT 3, DE_DIGA 82, FR_PECAN 2, FR_LATM 2, FR_LPPR 0. The DE_DIGA clock rule now names the GKV-Spitzenverband as the negotiating party.
- No scheme exists for RTM, ACCESS, EBM physician fees or England procurement. Those routes come from the research file only.

## market-access-dh.find_scheme_precedents (counted)

- Required `scheme`. Optional `indication`, `product_category`, `limit` 1 to 25 (most recent listings first).
- `{scheme: "US_CMS_RPM", limit: 25}` returns 99453, 99454, 99457, 99458. Not stored: 99445, 99470, 99091 and every RTM code. `search_listings` for "99445" returns nothing.
- `{scheme: "US_CMS_DMHT", limit: 25}` returns G0552, G0553, G0554 with the FDA classification (882.5801, 882.5803) in `indications`.
- Pitfall: for 99457, 99458, G0553 and G0554 the `price` field is empty while the passage states non-facility and facility amounts. Read the passage; `scripts/price_facts.py` parses it and recomputes RVU x conversion factor.
- Pitfall: the passages cite "CMS PFS Indicators for 2026, updated 1 October 2026", while `source_url` points to an MLN booklet. Cite both and say the amount comes from the PFS indicators per the library.
- `{scheme: "DE_DIGA", indication: "F33"}` returns depression DiGA with price and listing date. Search by ICD code or German term; English terms miss rows. The price carries no unit, prescription period, or manufacturer-versus-negotiated flag.
- `{scheme: "FR_PECAN"}`: ODYSIGHT carries 50 EUR (monthly per patient, stated in the passage only). `{scheme: "FR_LATM"}`: prices empty; the passage states fee ranges.

## market-access-dh.search_listings (counted)

- Required `query` (2+ characters). Use it to see whether the person's product is already listed. A code number not in the store returns an empty result with a gap line.

## market-access-dh.get_status_history (counted)

- For CMS codes, one day-zero snapshot dated 15 October 2026 only. The library cannot show when a code or its amount changed.

## market-access-dh.retrieve_guidance (counted)

- "DiGA Höchstbetrag Schwellenwert Vergütungsbetrag" returned no passage. Price rules come from `references/price-rules.md`.

## commercial-dh.get_pricing_corridor (counted)

- Required `reference`. Fans out to seven Market Access tools and returned 69,520 characters for "deprexis".
- Defect: the `prices` array held deprexis's own price twice (once with no source URL) and ten prices from the ten most recent DiGA listings in any indication (period pain, incontinence, menopause, hypertension, dementia). Rows carry no product name or indication. It is not a comparator corridor.
- Use: only the row for the named product, as its registered price. Build comparators from `find_scheme_precedents` with an indication instead.

## commercial-dh.map_money_flow (counted)

- `reference` plus caller-supplied `user`, `buyer`, `payer`, `note`. Echoes the three roles, sets `conflated` if two are the same string, and attaches the product's market matrix. It adds no fact the caller did not give, apart from the listing block.
- Use it in A2 to state who pays whom on the person's own description, labeled as the person's input.

## analytics.vba-price-anchor (counted)

- `comparator_cost_per_patient`, `incremental_qalys`, `wtp_thresholds`. The schema says the thresholds are objects; only a plain list of numbers works (`[20000, 30000]`); objects return HTTP 422.
- Returns `value_based_budget_per_patient` and `price_per_unit_ceiling` per threshold, plus hidden defaults `non_drug_cost_offset_per_patient: 0` and `units_per_patient: 1`. Test call: 1,000 comparator cost, 0.02 QALY: 1,400 at 20,000 and 1,600 at 30,000.
- Every input is the person's, including the threshold. The output is a hypothesis, never the product's price. No threshold is supplied by the model.

## analytics.budget-impact-model (counted)

- Returned HTTP 422 on four argument shapes (uptake as numbers; as objects with `share`, `uptake`, `market_share`). The schema does not say what an uptake item holds. Until fixed, run the arithmetic in the conversation on the person's numbers, show it, and label it a hypothesis.

## verify.build_record (counted)

- Needs a named human in `cleared_by`. Use only when an output leaves the conversation. Do not send register facts to `verify_text` or `check_claim`: register pages rate "no provenance".

## Not used here

- `watch_*` tools. Change tracking is the monitoring skill's job.
