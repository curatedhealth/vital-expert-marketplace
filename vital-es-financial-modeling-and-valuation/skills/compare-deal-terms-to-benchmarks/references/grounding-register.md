# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages), ENGINEERING RULE (no external source; the reason and the gap are stated) or [CHECK] (disabled until traced). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks that each item type has a row. Written 7 November 2026.

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 6 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |
| step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |
| task card | 01-collect-terms.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 02-record-subject.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 03-compute-benchmarks.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| template | benchmark-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |
| template | benchmark-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |
| constant or list | rule FV-TERMS-SOURCED | ENGINEERING RULE | every deal's terms carry a source reference and date Gap: none: a house rule |
| constant or list | rule FV-MIN-N | ENGINEERING RULE | a range needs at least the team's minimum number of deals; below it the result is 'no range' Gap: no source prescribes the minimum |
| constant or list | rule FV-POSITION-NOT-VERDICT | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-040, VP-V-051 |
| constant or list | rule FV-MARKET-DATA-SCARCE | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-020, VP-V-021 |
| constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation, the choice of rate and any fairness or solvency view are human only Gap: none: an owner ruling |
| constant or list | min_n default 3 when the team gives none | ENGINEERING RULE | house default, said in the output; the team may override |
| detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |
| detection question | FV-06 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-020, VP-V-021, VP-V-035 |
| detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |
| example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |
| example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |
| eval fixture | good-benchmarks-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
