# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages in `verbatim-passages.json`) or ENGINEERING RULE (no external source; the reason and the gap are stated). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks the rows. A "practitioner" mark means a practitioner article that is not a standard. Written 7 November 2026 (upgrade lane C, D, E, G, H).

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 2 | ENGINEERING RULE | population step; the reporting questions (measure, extrapolation, sensitivity, sources, uncertainty) come from VP-G-001 to VP-G-003 and VP-G-010 to VP-G-013 (orphan scope by analogy; GATHER is a reporting standard, not a method); the orphan arithmetic is VP-G-020, VP-G-021; step order is the plugin's; gap stated: no market-sizing standard |
| step | step 3 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 4 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 5 | ENGINEERING RULE | pipeline step; the registry cross-check is VP-G-050, VP-G-051, VP-G-052; the dated-source requirement is the plugin's; gap stated: no open competitive-intelligence practice source (G13) |
| step | step 6 | ENGINEERING RULE | differentiation step; cross-trial exclusion rests on VP-G-040 + ISPOR ITC VP-G-080..082 (G10) + NICE DSU TSD 18 VP-G-070/071 (G9 VERIFIED); the TPP is read as the seller supplies it (draft, VP-G-030, VP-G-031) |
| step | step 7 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 8 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 9 | ENGINEERING RULE | the choice of population definition and the sign-off are human only (owner ruling) |
| task card | 01-population.md | ENGINEERING RULE | population questions VP-G-001 to VP-G-003, VP-G-010 to VP-G-013 (orphan scope by analogy); orphan arithmetic VP-G-020, VP-G-021; gap stated: no market-sizing standard |
| task card | 02-standard-of-care-and-unmet-need.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 03-competing-marketed-products.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 04-competing-pipeline.md | ENGINEERING RULE | registry cross-check VP-G-050, VP-G-051, VP-G-052; gap stated: no open competitive-intelligence source |
| task card | 05-differentiation.md | ENGINEERING RULE | cross-trial exclusion VP-G-040 + VP-G-070/071 + VP-G-080..082; TPP draft VP-G-030, VP-G-031 |
| task card | 06-failure-modes-and-questions.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 07-write-register.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| template | market-register.md | ENGINEERING RULE | section structure is the decision-ready order of anatomy 3.6 with this skill's register fields; a house format, gap stated: no published reporting standard exists for a diligence register |
| constant or list | ORPHAN-US-200K | VERIFIED-REOPENED | VP-G-020; unit test matches the number |
| constant or list | ORPHAN-EU-5PER10K | VERIFIED-REOPENED | VP-G-021; unit test matches the number (prevalence limb only) |
| constant or list | PREVALENCE-REPORTING (measure, extrapolation, textbook flags) | VERIFIED-REOPENED | VP-G-010, VP-G-011, VP-G-013 and GATHER VP-G-001 to VP-G-003; the field names are the plugin's |
| constant or list | REG-STATUS-CONTEXT and REG-CROSSCHECK | VERIFIED-REOPENED | VP-G-050, VP-G-051, VP-G-052; unit test |
| constant or list | MKT-OVERESTIMATE-CONTEXT | VERIFIED-REOPENED | VP-G-060; context only |
| constant or list | basis kinds, comparison types (head_to_head, indirect, cross_trial, none) | ENGINEERING RULE | closed sets; cross-trial exclusion motivated by VP-G-040 + VP-G-070/071 + VP-G-080..082 |
| constant or list | forbidden price keys and forecast phrase patterns | ENGINEERING RULE | keep price, coverage, access and sales figures out of this register (owner ruling: Market Access pack owns them) |
| constant or list | max_figure_age_years (buyer-set) | ENGINEERING RULE | not a constant: the buyer sets the age limit; no source sets one |
| detection question | MG-01 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | MG-02 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | MG-03 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | MG-04 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| example | poor-sales-claim.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| eval fixture | good-market-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
| constant or list | country markets DE, FR, IT, ES, UK and `country_patients` block | ENGINEERING RULE | added 7 November 2026 so the revenue skill reads patients per country; the geography rule (one geography per figure) is the skill's own; no published standard sets a country-level sizing method; gap stated |
| constant or list | no single-country orphan check | ENGINEERING RULE | the orphan definitions registered for this skill are the US and EU statutory ones (ORPHAN-US-200K, ORPHAN-EU-5PER10K); applying them to one member state is not sourced, so the script says not computed |
| eval fixture | good-country-input.json | ENGINEERING RULE | fictional input built to test country patients; not tied to a real case |
