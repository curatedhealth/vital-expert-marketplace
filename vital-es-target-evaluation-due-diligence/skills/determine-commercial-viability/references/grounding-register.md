# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages in `verbatim-passages.json`) or ENGINEERING RULE (no external source; the reason and the gap are stated). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks the rows. A "practitioner" mark means a practitioner article that is not a standard. Written 7 November 2026 (upgrade lane C, D, E, G, H).

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 2 | ENGINEERING RULE | analog collection step; the selection criteria (comparability of properties, order of entry, unmet need, launch environment) are practitioner statements VP-H-030 to VP-H-032 (not a standard); the dated-source and stated-basis requirements are the plugin's; gap stated: no source gives a number of analogs |
| step | step 3 | ENGINEERING RULE | range and leave-one-out arithmetic of the plugin; ANALOG-MIN-3 is an engineering rule (gap stated: no source sets three); forecast error is context VP-H-001 to VP-H-005 |
| step | step 4 | ENGINEERING RULE | conditions read from upstream registers are the plugin's design; the exclusivity statutes are in skill C's register |
| step | step 5 | ENGINEERING RULE | price and revenue come from the signed register of forecast-revenue-and-price-ranges (owner ruling R7, 7 November 2026), coverage and access only from the Market Access pack (owner ruling); access-failure evidence VP-H-020 to VP-H-022 is context with its scope |
| step | step 6 | ENGINEERING RULE | option set GO, CONDITIONAL GO, NO-GO with conditions; the option dimensions parallel practitioner frameworks VP-H-040, VP-H-041 and a practitioner three-option recommendation VP-A-143 (not standards); no thresholds come from a source; the decision is human only |
| step | step 7 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 8 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 9 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 10 | ENGINEERING RULE | the commercial decision is human only (owner ruling) |
| task card | 01-analogs.md | ENGINEERING RULE | analog criteria are practitioner rows VP-H-030 to VP-H-032 (not a standard); gap stated: no number of analogs |
| task card | 02-analog-range.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 03-conditions-from-upstream.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 04-market-access-handoff.md | ENGINEERING RULE | owner ruling: coverage and access only from the Market Access pack, price and revenue from the revenue register (R7), pack price figures only as a cross-check; access-failure context VP-H-020 to VP-H-022 |
| task card | 05-option-set.md | ENGINEERING RULE | option dimensions parallel practitioner frameworks VP-H-040, VP-H-041; gap stated: no thresholds; the decision is human only |
| task card | 06-failure-modes-and-questions.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 07-write-register.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| template | viability-register.md | ENGINEERING RULE | section structure is the decision-ready order of anatomy 3.6 with this skill's register fields; a house format, gap stated: no published reporting standard exists for a diligence register |
| constant or list | KOSSMEIER-CONTEXT | VERIFIED-REOPENED | VP-H-001 to VP-H-005; unit test matches the figures; context only, no band |
| constant or list | MKT-OVERESTIMATE-CONTEXT | VERIFIED-REOPENED | VP-H-010; unit test matches the count |
| constant or list | CHA-ERROR-BAND (disabled) | ENGINEERING RULE | rule disabled; gap stated: the article body is paywalled (H1a); no band is applied |
| constant or list | ANALOG-MIN-3 | ENGINEERING RULE | floor of three included analogs; gap stated: no source sets the number (practitioner guidance gives criteria and no count, VP-H-030 to VP-H-032) |
| constant or list | option-set conditions (11) and states (met / not met / straddles / gap) | ENGINEERING RULE | the conditions and states are the plugin's design; thresholds are the buyer's; gap stated: no source for go or no-go thresholds |
| constant or list | recommendation and point-estimate phrase patterns | ENGINEERING RULE | keep a recommendation and a single peak-sales figure out of the register (owner ruling: the decision is human only) |
| detection question | MH-01 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | MH-02 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | MH-03 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | MH-04 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| eval fixture | good-analog-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-option-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
| constant or list | condition C-RV (price and revenue from a signed revenue register) | ENGINEERING RULE | owner ruling R7 of 7 November 2026; evaluated only when the input carries a revenue_inputs block; an unsigned or missing register is a gap, never not met; no published standard sets a commercial go/no-go test |
