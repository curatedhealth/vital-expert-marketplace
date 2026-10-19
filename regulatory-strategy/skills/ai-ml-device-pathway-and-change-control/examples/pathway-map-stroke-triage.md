# Worked example: A1 for a stroke CT triage product

Live library calls on 19 October 2026. Trimmed outputs are in `live/`. The product ("StrokeSense") is the person's own, not yet authorized; its description is the person's.

**Request:** "We have a deep learning model that flags suspected large vessel occlusion on head CT and notifies the stroke team. We want the US first, then the EU and UK. What route, do we need a PCCP for quarterly retraining, and how does the AI Act hit us? Aidoc and Brainomix are the competitors."

**Calls made**

1. `regulatory-dh.list_jurisdictions` (free): US 1,226 records loaded 19 October 2026; EU 3,142 with no decision dates; UK and CH registrations not loaded. Saved as `live/list_jurisdictions_2026-10-19.json`.
2. `regulatory-dh.classify_product` `{name: "StrokeSense CT triage", intended_purpose: "..."}`: no stored record; codes not inferred. `live/classify_product_strokesense_2026-10-19.json`.
3. `regulatory-dh.search_devices` `{query: "Aidoc", jurisdiction: "all", limit: 10}`, `{query: "Brainomix", jurisdiction: "all", limit: 5}`, `{query: "Briefcase", jurisdiction: "EU", limit: 5}`. `live/search_devices_*.json`.
4. `regulatory-dh.get_pathway_precedents` `{product_code: "QAS", jurisdiction: "US"}`. `live/pathway_precedents_QAS_2026-10-19.json`.
5. `regulatory-dh.find_predicates` `{reference: "K261317"}`. `live/find_predicates_K261317_2026-10-19.json`.
6. `scripts/precedent_table.py live/search_devices_brainomix_2026-10-19.json --product-code QAS`.

## Answer (short mode)

**Answer.** In the US the competitors' records point to 510(k) under product code QAS: 87 of 88 stored QAS decisions are 510(k), with one De Novo (DEN170073, ContaCT, Viz.Al, Inc., granted 13 February 2018) that created the type. The regulatory owner decides between 510(k) and De Novo for StrokeSense. Quarterly retraining is the first change type FDA names for a PCCP, established in the 510(k) itself [AI US-07, US-09]. In the EU, if the owner's Rule 11 class is IIa or higher and the software is an AI system, the AI Act high-risk requirements apply from 2 August 2028, the date set by Regulation (EU) 2026/1744 [AI EU-19, EU-27].

| Jurisdiction | Candidate routes (owner decides) | Change plan mechanism | AI-specific obligations | Rows |
|---|---|---|---|---|
| US | 510(k) to a QAS predicate, or De Novo | PCCP: section 515C; final guidance of 18 August 2025 | AI lifecycle guidance is a draft of 7 January 2025 | AI US-01, US-09, US-15 to US-21 |
| EU | Notified body under MDR; class per Rule 11 | Pre-determined changes under AI Act Article 43(4); no EU PCCP guidance yet | High-risk from 2 August 2028 (Regulation (EU) 2026/1744); AI literacy since 2 February 2025 | AI EU-05, EU-19, EU-20, EU-31 |
| UK | CE accepted until 30 June 2030 for MDR devices | None in force; MHRA draft guidance announced 6 October 2026 | None specific in force | RP UK-03; AI UK-04 |

**Precedents, by their records.** Brainomix 360 Triage Stroke, 510(k) K251983, QAS, decided 26 August 2025, 60 days from stored submission. Aidoc BriefCase-Triage, 510(k) K261317, QAS, decided 14 May 2026; its predicate chain runs five levels back to DEN170073. Aidoc's Briefcase-Triage is also on EUDAMED, class IIa, Basic UDI-DI 7290018052BC.TRGSU. The records state no AI or PCCP status; FDA's AI-enabled device list (not comprehensive, list current 4 September 2026) is where to check.

**Gaps.**
1. Whether the omnibus also defers AI Act post-market monitoring (Article 72) for devices needs a legal read `[GAP]`.
2. UK device registrations are not loaded in the library; MHRA PCCP content is unpublished `[GAP]`.
3. Your EU class and AI-system status are for the regulatory owner; owner not named.

**Record:** Sourced references read 19 October 2026; library records retrieved 13 and 14 October 2026. Class and route are the regulatory owner's decision. Uncleared draft.

Full version (argument tables, AI Act date table, all precedents) on request.

## What this example shows

- The route is laid out as options with the precedent record behind each, not declared.
- The AI Act date is the amended one, with the amending act named.
- The library's same product under two spellings is matched on identifiers, and its AI status is not inferred.
- `get_market_status` was not used for the cross-jurisdiction view: its rows contradict each other (`live/market_status_briefcase_2026-10-19.json`, `references/tools.md`).
