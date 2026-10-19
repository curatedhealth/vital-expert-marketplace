# Worked example: requirement map with a comparable (A1)

Request: "We are building CT stroke-scoring software similar to Brainomix 360 e-ASPECTS. Map what we face in the US, EU, Great Britain, Switzerland, Canada and Australia, and show where e-ASPECTS stands."

Real library data, retrieved on 19 October 2026. Shown so the model sees the shape of a good answer, not to be reused as current fact.

## Calls made

| Call | Arguments | Saved output |
|---|---|---|
| `regulatory-dh.list_jurisdictions` (free) | none | `live/list_jurisdictions_2026-10-19.json` |
| `regulatory-dh.search_devices` | `query` "Brainomix", `software_only` "false", `limit` 25 | `live/search_devices_brainomix_2026-10-19.json` |
| `regulatory-dh.compare_authorizations` | `references` ["K243294", "++B720EASPECTSCEGK", "K221564"] | `live/compare_authorizations_e-aspects_2026-10-19.json` |
| `regulatory-dh.get_market_status` | `name` "Brainomix 360 e-ASPECTS" | `live/get_market_status_brainomix_e-aspects_2026-10-19.json` |
| `scripts/market_matrix.py` | the three files above, `--product e-ASPECTS` | `market_matrix_e-aspects_2026-10-19.md` |

## What the tools returned (abridged)

- US: two e-ASPECTS 510(k) records, class 2, product code POK, regulation 892.2060: K243294 (decision 14 February 2025, eight predicates listed) and K221564 (decision 23 February 2023, predicate K200760); retrieved 13 October 2026.
- EU: one EU_MDR record, Class IIb, "On the EU market", Basic UDI-DI ++B720EASPECTSCEGK, EMDN Z11030592; and three EU_MDD records named "e-ASPECTS", Class IIa, "On the EU market"; no decision dates; retrieved 14 October 2026.
- `get_market_status` returned three rows that disagree (two say US true, EU false; one says US false, EU true). Merged: records found in both.
- GB, CH, AU: register not loaded. CA: loaded (227 MDALL rows) but not searchable by product.

## The answer the skill should give (short mode)

**Answer.** Three differences shape your plan. First, the EU and Switzerland apply MDR Rule 11, under which decision software is IIa, IIb or III by the impact of the decision (EU-02, EU-03, CH-01), while Great Britain still uses MDD-era rules that can give a lower class (UK-14). Second, an EU MDR certificate opens Great Britain until 30 June 2030 and is a basis in Switzerland and Australia (MR-23, MR-20, MR-07); an FDA decision opens Australia (MR-09) but not yet Great Britain or Switzerland, where those routes are drafts (MR-26, MR-21). Third, Canada needs a license with an MDSAP certificate for Class II to IV (MR-02, MR-05). Your class in each region is your regulatory owner's call.

| Region | Class rule and argument (owner decides) | Route | Reliance in (status) | e-ASPECTS in the library |
|---|---|---|---|---|
| US | Class from product code; e-ASPECTS records sit under POK, class 2 | 510(k) if a predicate fits (US-06) | none needed | K243294, class 2, 510(k), 14 February 2025 |
| EU | Rule 11 by decision impact (EU-02, EU-03) | Notified body for IIa and above (EU-09, EU-10) | none | MDR record Class IIb (++B720EASPECTSCEGK); three MDD records Class IIa; no dates stored |
| GB | MDD-era rules (UK-14) | CE accepted until 30 June 2030 (UK-03) | FDA reliance: draft (MR-26) | Register not loaded |
| CH | EU Annex VIII (CH-01) | Swiss or EU declaration (MR-19) | EU certificate: in force (MR-20); FDA: draft (MR-21) | Register not loaded |
| CA | Classes I to IV; software rule [GAP] (MR-01) | License for II to IV (MR-02) | MDSAP certificate (MR-05) | Loaded, not searchable |
| AU | Rule 4.5, diagnosis or screening (MR-14) | ARTG with overseas evidence | FDA, EU NB, Health Canada, MDSAP: in force, same device, audit possible (MR-07, MR-10, MR-11) | Register not loaded |

**Registration after authorization.** US annual registration 1 October to 31 December (JX-29); Canada statement before 1 November (JX-33); EU device registration before the first unit is placed (JX-40); Swiss registration from July 2026 (JX-42); MHRA registration (UK-01).

**Check with the regulator.** The e-ASPECTS records show Class IIa (MDD) and Class IIb (MDR) in the EU; the library does not say why, and neither should we. Canada and Australia status for e-ASPECTS: check MDALL and the ARTG.

**Record.** Uncleared draft for your regulatory owner. AI-assisted. Want the full version with MDSAP use per region?

## Why this is a good answer

It answers first with the differences that matter. It describes e-ASPECTS only by its records and does not explain the IIa versus IIb difference. It merges the contradicting market-status rows instead of repeating "EU: false". It labels every reliance route with its legal status and keeps the drafts out of the plan. It never says what class the person's product is.
