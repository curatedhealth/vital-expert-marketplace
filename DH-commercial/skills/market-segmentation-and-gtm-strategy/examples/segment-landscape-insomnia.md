# Worked example: A1 segment landscape for an insomnia digital therapeutic

Live library calls on 19 October 2026. Trimmed outputs are in `examples/live/`. The product is hypothetical; every peer, route and coverage fact below comes from the live calls or the CP rows.

**Request:** "We have a CBT-I app for chronic insomnia, FDA 510(k) cleared under 21 CFR 882.5801, CE marked. We are deciding between Germany and the US. Who buys and pays in each, and who is already there?"

**Calls made**

1. `commercial-dh.list_commercial_dh_sources` `{}` (free): US 1,226 and EU 3,142 device authorizations; UK and CH 0; DE_DIGA 82 listings loaded 15 October 2026; no funding source, no UK company register.
2. `commercial-dh.screen_commercial_peers` `{segment: "dtx", limit: 10}`: 10 of 18 matches, all US companies. Run through `scripts/gtm_helpers.py peers` (`peer_table_dtx_2026-10-19.md`): 9 of 10 per-peer device lookups missed because the lookup uses company names.
3. `commercial-dh.screen_commercial_peers` `{segment: "dtx", name: "Somryst", limit: 3}`: Somryst, 510(k) K191716, 23 March 2020, product code QVO, regulation 882.5801.
4. `market-access-dh.find_scheme_precedents` `{scheme: "DE_DIGA", indication: "F51", limit: 10}`: three permanent insomnia DiGA (two earlier attempts returned 503, not counted).
5. `market-access-dh.get_status_history` `{reference, scheme: "DE_DIGA"}` for each of the three (added 19 October 2026 after grading): only HelloBetter Schlafen has a BfArM notice stored.
6. `market-access-dh.find_scheme_precedents` `{scheme: "US_CMS_DMHT", limit: 5}`: G0552 to G0554, conditions naming 21 CFR 882.5801 and 882.5803.
7. `regulatory-dh.search_devices` `{query: "Big Health", jurisdiction: "US"}` (added 19 October 2026 after grading): Sleepio K233577, QVO, 882.5801, 5 August 2024; Daylight K233872, SCP, 882.5801, 30 August 2024.

## Answer (short mode)

**Answer.** Both candidate segments have a payer route on record; they put different people in the buyer seat. In Germany the prescriber or the sickness fund decides and three insomnia DiGA are already permanently listed. In the US Medicare route, the practitioner buys the device and bills the codes, so the practitioner, not the patient, is your buyer. Whether your product qualifies for either route is a Market Access question.

| Segment (proposed) | Buyer | User | Payer and route | Binding channel rule | Peers on record |
|---|---|---|---|---|---|
| Germany, statutory insured adults with insomnia | Treating physician or psychotherapist (prescription), or the fund (approval with proof of indication) | Patient | Sickness funds, DiGA listing (CP-DE-01, CP-DE-02) | No deals with prescribers on allocating prescriptions (CP-DE-06); DiGA must be ad-free (PC-DE-15) | somnio (listed 22 October 2020), HelloBetter Schlafen (listed 18 December 2022, permanent from 17 December 2024, BfArM notice 18), somnovia (listed 28 October 2024), all "dauerhaft aufgenommen" today, retrieved 15 October 2026; date status began not stored for somnio and somnovia `[GAP]` |
| US Medicare behavioral health practices | Billing practitioner, who must bear the device cost (CP-US-59) | Patient under a behavioral health plan of care (CP-US-60) | Medicare DMHT codes G0552 to G0554, device at 882.5801 (CP-US-58) | Anti-Kickback Statute where Medicare pays (CP-US-01); patient engagement cap $623 for 2026 (CP-US-27) | Somryst, 510(k) K191716, 23 March 2020, QVO; Sleepio, 510(k) K233577, 5 August 2024, QVO; both regulation 882.5801. Other makers: lookup missed |
| US self-insured employers | Employer | Employee | Employer budget; channel rules not sourced `[GAP]` | Not sourced `[GAP]` | Not screened |

**Coverage.** The peer screen holds only the companies the store holds: in the `dtx` segment, ten US companies were returned and one EU company exists (Novasight). German DiGA makers are visible only through the DE_DIGA listing mirror. No UK device authorizations are loaded.

**Gaps that matter.**
1. Lookup missed for 9 of 10 screened peers (for example Akili, 3 authorizations, no device row by company name). Look up products by name before calling them absent.
2. Whether your device qualifies for G0552 and what the codes pay: Market Access pack.
3. Employer channel rules: not in this skill's sources.

**Record.** Fact draft. Segments proposed. Uncleared.

## What this example shows

- Roles are kept apart: in the US Medicare route the buyer is the practitioner, which changes the motion in B1.
- Peers are described by their record only, with dates and the retrieval date.
- The connector's lookup miss is shown to the person, not turned into "no competitor".
