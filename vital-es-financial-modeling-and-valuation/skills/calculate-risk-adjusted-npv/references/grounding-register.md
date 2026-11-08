# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages), ENGINEERING RULE (no external source; the reason and the gap are stated) or [CHECK] (disabled until traced). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks that each item type has a row. Written 7 November 2026.

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 6 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |
| step | step 8 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |
| task card | 01-read-probabilities-and-dcf.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 02-stage-costs.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 03-compute-rnpv.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 04-benchmark-comparison.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 05-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 06-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| template | rnpv-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |
| template | rnpv-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |
| constant or list | rule FV-RNPV-STRUCTURE | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-001, VP-V-002 |
| constant or list | rule FV-RISK-ONCE | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-003, VP-V-004 |
| constant or list | rule FV-RATE-DOCUMENTED | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-030, VP-V-031 |
| constant or list | rule FV-RATE-CHOICE | [CHECK] | disabled rule: no registered default or range for a biotech discount rate (the one rate-magnitude source opened concerns capitalizing R&D outlays, VP-V-060, and is out of scope); the script prints [CHECK] and does not compute it |
| constant or list | rule FV-STAGE-LAYOUT | ENGINEERING RULE | stages are sequential, costs are spread evenly over a stage's years and weighted by the probability of reaching the stage; no standard prescribes the layout Gap: WIPO describes the principle (VP-V-001) but not a stage layout; the timeline skill's phase probabilities are the usual input Context: VP-V-001, VP-B-001, VP-B-004 |
| constant or list | rule FV-SCENARIO-PAIRING | ENGINEERING RULE | low scenario = low probability with high cost; high scenario = high probability with low cost; so the range is the conservative-to-favorable combination Gap: no source prescribes a pairing; ranges are not confidence intervals |
| constant or list | rule FV-DOUBLE-COUNT | ENGINEERING RULE | a series already risk-adjusted is refused so that risk is not counted twice (E_DOUBLE) Gap: none: follows the registered separation of rate and probability (VP-V-003) Context: VP-V-003, VP-V-005 |
| constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation, the discount-rate choice and the final probability of success are human only Gap: none: an owner ruling |
| constant or list | LEVELS and COST_OF (low uses high cost) | ENGINEERING RULE | pairing table of FV-SCENARIO-PAIRING; house rule |
| constant or list | error codes E_DOUBLE, E_SOURCE, E_SEQUENCE, E_STAGES, E_PROB, E_RANGE | ENGINEERING RULE | input checks of the calculator; house rules |
| detection question | FV-01 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-B-001, VP-B-004, VP-B-060 |
| detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |
| detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |
| detection question | FV-04 | [CHECK] | detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md |
| detection question | FV-05 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-C-001, VP-C-010, VP-C-061, VP-C-090 |
| detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |
| example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |
| example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |
| eval fixture | good-rnpv-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | hand-check-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | two-stage-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
