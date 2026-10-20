# Worked example: A1 decision evidence tracking, digital CBT at NICE

Live library calls and guidance pages read on 19 October 2026. Trimmed library outputs in `examples/live/`; the guidance text as read is in `examples/live/nice_pages/`; the quotes used are in `examples/live/decision_notes_nice_2026-10-19.json` and were machine-checked against the page text (10 of 10 matched). The decisions are real NICE guidance used as comparables; nothing here predicts a decision on any other product.

**Request:** "We're preparing a digital CBT-I app for adults and a guided digital CBT for depression. What did NICE say about the economic evidence for comparable products, and what evidence did it ask for?"

**Calls made**

1. `market-access-dh.list_schemes` (free): UK_NICE_EVA 15 rows, UK_NICE_HTG 2, UK_NICE_NHAP 0; NICE posture partial ("NICE_API_KEY is empty").
2. `market-access-dh.find_scheme_precedents {scheme: "UK_NICE_EVA", limit: 25}`: 15 rows, including HTG675 and HTE8 (the same guidance) and HTG660. Saved: `live/nice_eva_precedents_2026-10-19.json`.
3. `market-access-dh.find_scheme_precedents {scheme: "UK_NICE_HTG", limit: 10}`: HTG624 (Sleepio) and HTG778 (stored as permanent although titled "early-use assessment"). Saved: `live/nice_htg_precedents_2026-10-19.json`.
4. `market-access-dh.get_status_history {reference: "HTG660", scheme: "UK_NICE_EVA"}`: one day-zero snapshot; the page says last updated 7 September 2026. Saved: `live/status_history_htg660_2026-10-19.json`.
5. Guidance pages read at nice.org.uk: HTG624 recommendations and committee discussion; HTG675 recommendations and further evidence; HTG660 recommendations and evidence generation.
6. `scripts/decision_evidence_log.py --rows live/nice_eva_precedents_2026-10-19.json live/nice_htg_precedents_2026-10-19.json --notes live/decision_notes_nice_2026-10-19.json --only HTG624 HTG675 HTG660 HTG778`. Output: `live/decision_log_output.txt`.

## Answer (short mode)

**NICE accepted economic cases for these products, each with stated limits, and asked for named outcomes.** The library listed the decisions; their content comes from the guidance pages, read 19 October 2026.

| Ref | Category as read | Published | Flags |
|---|---|---|---|
| HTG624 Sleepio | Routine use: "recommended as a cost saving option ... for people who would otherwise be offered sleep hygiene or sleeping pills" (1.1) | 20 May 2022 | |
| HTG675 depression | Early use: Space from Depression "can be used ... while further evidence is generated on its clinical and cost effectiveness" (1.1); three others research only (1.3) | 16 May 2023 | Also stored as HTE8 |
| HTG660 children and young people | Early use: four technologies "while evidence is being generated" (1.1) | 8 February 2023 | Last updated 7 September 2026; history holds only a day-zero snapshot |
| HTG778 asthma | `[GAP]`: not read | 5 May 2026 | Early-use title stored as permanent |

**What NICE said about the economics.**
- HTG624: "At a price of £45 per person, Sleepio is cost saving compared with usual treatment in primary care", based on resource use "before and after Sleepio was introduced in 9 GP practices". On the earlier £66.11 tiered price: "The committee did not agree that there was enough evidence to extrapolate the data to 3 years" (4.14). At £45 the limits were "dependence on the Sampson et al. (2021) study and the lack of remission outcomes" (4.15), and for all prices the model "assumes that Sleepio is clinically equivalent to face-to-face CBT-I but more evidence is needed" (4.16).
- HTG675: the early analysis suggests the technologies "could be cost effective based on current prices and evidence".
- HTG660: "Early results from the economic modelling show that the technologies could be cost effective."

**What NICE asked for.** HTG675 lists 11 outcomes, among them recovery, relapse, health-related quality of life and resource use (1.2). HTG660 lists 5, among them health-related quality of life and engagement (4.1). HTG624 asks for research in people eligible for face-to-face CBT-I (1.3).

**Windows.** Both early-use pages say "reviewed within 4 years", which governs over the PMG48 default of 3 years (`HE-072`, `EN-6`). Counted from publication: HTG675 to 16 May 2027, HTG660 to 8 February 2027, as of 19 October 2026. No re-evaluation outcome is published for HTG675 (`EN-6`).

**What it means for you, as facts.** Committees accepted one-year resource-use evidence and early models, and named extrapolation and assumed equivalence as limits. Your own case is checked with `reimbursement-evidence-support` (A2).

**Record:** Clears it: owner not named. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. AI-assisted.

## What this example shows

- The library row says a decision exists; only the guidance text says how the evidence was treated.
- Renumbered guidance and an early-use title stored as permanent are caught before counting.
- The guidance's own review period is used, and the counting date is stated.
