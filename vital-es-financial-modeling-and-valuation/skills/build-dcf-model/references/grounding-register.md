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
| task card | 01-read-upstream-registers.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 02-cost-and-capital-assumptions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 03-discount-rate-range.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 04-compute-present-values.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 05-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 06-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| template | dcf-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |
| template | dcf-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |
| constant or list | rule FV-RATE-SUPPLIED | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-030 |
| constant or list | rule FV-RATE-CONSISTENT | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-032 |
| constant or list | rule FV-TERMINAL-RATE | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-033 |
| constant or list | rule FV-TERMINAL-SHARE | [CHECK] | disabled rule: no registered threshold for a terminal-value share; the script prints [CHECK] and does not compute it |
| constant or list | rule FV-CASHFLOW-ARITHMETIC | ENGINEERING RULE | operating cash flow = net revenue x (1 - cogs% - opex%) - fixed costs, less tax on the positive part, capex and working capital; no loss carry-forward Gap: no standard prescribes this cash-flow construction for a development-stage asset; WIPO describes sales growing from a low base, peaking and decl Context: VP-V-009, VP-V-010 |
| constant or list | rule FV-UNRISKED | ENGINEERING RULE | owner ruling V4 places risk adjustment in calculate-risk-adjusted-npv; this skill rejects probability keys (E_RISK) Gap: none: a house boundary |
| constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation and the discount-rate choice are human only Gap: none: an owner ruling Context: VP-V-006 |
| constant or list | FORBIDDEN_RISK and FORBIDDEN_ADOPT key lists | ENGINEERING RULE | owner rulings V4 and V5: probability keys and adopted-valuation keys are refused with E_RISK and E_ADOPT; house lists |
| constant or list | end-year and mid-year timing conventions | ENGINEERING RULE | calendar-year convention (t = year - valuation year, minus 0.5 for mid-year); house convention, stated in the script docstring |
| detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |
| detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |
| detection question | FV-04 | [CHECK] | detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md |
| detection question | FV-05 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-C-001, VP-C-010, VP-C-061, VP-C-090 |
| detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |
| example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |
| example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |
| eval fixture | good-dcf-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | hand-check-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
