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
| task card | 01-collect-assumptions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 02-trace-to-registers.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 03-run-the-nine-checks.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |
| template | assumption-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |
| template | assumption-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |
| constant or list | rule FV-PROB-ABOVE-BENCHMARK | VERIFIED-REOPENED | restates the registered wording; passage ids VP-B-001, VP-B-004, VP-B-060 |
| constant or list | rule FV-PEAK-ABOVE-ANALOG | VERIFIED-REOPENED | restates the registered wording; passage ids VP-H-001, VP-H-002, VP-H-010 |
| constant or list | rule FV-RATE-DOCUMENTED | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-030, VP-V-031 |
| constant or list | rule FV-RISK-TWICE | VERIFIED-REOPENED | restates the registered wording; passage ids VP-V-004, VP-V-005 |
| constant or list | rule FV-TERMINAL-SHARE | [CHECK] | disabled rule: no registered threshold for a terminal-value share; the script prints [CHECK] and does not compute it |
| constant or list | rule FV-NINE-CHECKS | ENGINEERING RULE | the nine checks and their ok / flag / gap states are this skill's own set Gap: no published checklist for valuation assumptions of a development-stage asset was located |
| constant or list | rule FV-NO-VALIDATION-CLAIM | ENGINEERING RULE | the output states counts and that a named reviewer decides; it never calls a valuation validated (E_ADOPT on such a key) Gap: none: a house boundary |
| constant or list | KINDS and NEEDS_UPSTREAM lists | ENGINEERING RULE | house lists of assumption kinds and of kinds that need an upstream pointer |
| detection question | FV-01 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-B-001, VP-B-004, VP-B-060 |
| detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |
| detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |
| detection question | FV-04 | [CHECK] | detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md |
| detection question | FV-05 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-C-001, VP-C-010, VP-C-061, VP-C-090 |
| detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |
| example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |
| example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |
| eval fixture | good-assumptions-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
