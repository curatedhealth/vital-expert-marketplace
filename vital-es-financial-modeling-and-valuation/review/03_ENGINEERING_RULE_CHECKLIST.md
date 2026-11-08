# Checklist of the authors' own rules (ENGINEERING RULE) and untraced items ([CHECK])

Generated 7 November 2026 from the nine grounding registers and the summary-tool rules. An ENGINEERING RULE has no published standard behind it; the reason and the gap are stated. A [CHECK] item is disabled in the scripts and never scored.

Total rows: 276 (every row is kept; 30 of them are also listed first).
**How to read it.** Start with the Top 30, ranked by consequence: rules that change a range, a status, a refusal or a human gate. Every row of the Top 30 also appears in its competency section.

## Top 30 (ranked by consequence)

| Rank | Row | Item | Status | Why it is load-bearing | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|
| 1 | V1-17 | rule FV-TERMINAL-SHARE | [CHECK] | a [CHECK] item: the terminal share is reported with no threshold; it can dominate the result |  |  |
| 2 | V1-19 | rule FV-UNRISKED | ENGINEERING RULE | keeps probability of success out of the DCF |  |  |
| 3 | V1-18 | rule FV-CASHFLOW-ARITHMETIC | ENGINEERING RULE | the arithmetic behind every present value |  |  |
| 4 | V1-20 | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | human gate: which valuation the team adopts |  |  |
| 5 | V1-21 | FORBIDDEN_RISK and FORBIDDEN_ADOPT key lists | ENGINEERING RULE | the keys that stop risk entering the DCF |  |  |
| 6 | V2-17 | rule FV-RATE-CHOICE | [CHECK] | a [CHECK] item: no default or range for the rate; the rate is a human choice |  |  |
| 7 | V2-20 | rule FV-DOUBLE-COUNT | ENGINEERING RULE | refuses risk counted twice |  |  |
| 8 | V2-19 | rule FV-SCENARIO-PAIRING | ENGINEERING RULE | defines low, mid and high in every rNPV range |  |  |
| 9 | V2-22 | LEVELS and COST_OF (low uses high cost) | ENGINEERING RULE | low scenario takes the high cost |  |  |
| 10 | V2-18 | rule FV-STAGE-LAYOUT | ENGINEERING RULE | reach probabilities and cost timing by stage |  |  |
| 11 | V3-16 | rule FV-NINE-CHECKS | ENGINEERING RULE | the nine checks of every assumption |  |  |
| 12 | V3-17 | rule FV-NO-VALIDATION-CLAIM | ENGINEERING RULE | the register never says "validated" |  |  |
| 13 | V3-15 | rule FV-TERMINAL-SHARE | [CHECK] | a [CHECK] item repeated in the validator |  |  |
| 14 | V4-15 | rule FV-SCENARIO-PAIRING | ENGINEERING RULE | the pairing rule behind the standard scenarios |  |  |
| 15 | V4-16 | rule FV-NO-INVENTED-PROBABILITY | ENGINEERING RULE | no scenario probability is invented |  |  |
| 16 | V5-18 | rule FV-SCALE-SUPPLIED | ENGINEERING RULE | the team supplies every scale; no default |  |  |
| 17 | V5-16 | rule FV-TORNADO-RANK | ENGINEERING RULE | how drivers are ranked |  |  |
| 18 | V5-17 | rule FV-SWITCHING | ENGINEERING RULE | the switching value definition |  |  |
| 19 | V5-21 | switching_upper = 10 and bisection tolerance 1e-9 | ENGINEERING RULE | the search range of the switching value |  |  |
| 20 | V6-16 | rule FV-REFUSAL-PATTERNS | ENGINEERING RULE | the phrase lists that refuse recommendation and fairness language |  |  |
| 21 | V6-15 | rule FV-POINTER-EVERY-LINE | ENGINEERING RULE | every line is auditable |  |  |
| 22 | V6-18 | RECOMMEND, FAIRNESS and POINT phrase patterns | ENGINEERING RULE | the phrase lists themselves |  |  |
| 23 | V7-17 | rule FV-SELECTION-FLAG | ENGINEERING RULE | completed-only deals can bias a range |  |  |
| 24 | V7-18 | rule FV-GAP-ALLOWANCE | ENGINEERING RULE | how many gaps a deal may carry |  |  |
| 25 | V7-15 | rule FV-CRITERIA-TEAM | ENGINEERING RULE | the criteria are the team's |  |  |
| 26 | V8-16 | rule FV-MIN-N | ENGINEERING RULE | fewer deals than the minimum gives no range |  |  |
| 27 | V8-18 | min_n default 3 when the team gives none | ENGINEERING RULE | the default minimum |  |  |
| 28 | V9-15 | rule FV-NO-MERGE | ENGINEERING RULE | the model range and the benchmark range are never merged |  |  |
| 29 | V9-16 | rule FV-THIN-DATA | ENGINEERING RULE | when a range is flagged thin |  |  |
| 30 | S-01 | S-STATUS: workstream status proposed from counts: yellow at 1 gap or 1 triggered or cannot-tell failure mode, red at 5 gaps or 3 such modes, | ENGINEERING RULE | sets the status colors the deal lead sees |  |  |

## V1 · build-dcf-model (34 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V1-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-06 |  | step | step 6 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V1-08 |  | step | step 8 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V1-09 |  | task card | 01-read-upstream-registers.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-10 |  | task card | 02-cost-and-capital-assumptions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-11 |  | task card | 03-discount-rate-range.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-12 |  | task card | 04-compute-present-values.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-13 |  | task card | 05-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-14 |  | task card | 06-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V1-15 |  | template | dcf-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V1-16 |  | template | dcf-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V1-17 | 1 | constant or list | rule FV-TERMINAL-SHARE | [CHECK] | disabled rule: no registered threshold for a terminal-value share; the script prints [CHECK] and does not compute it |  |  |
| V1-18 | 3 | constant or list | rule FV-CASHFLOW-ARITHMETIC | ENGINEERING RULE | operating cash flow = net revenue x (1 - cogs% - opex%) - fixed costs, less tax on the positive part, capex and working capital; no loss carry-forward Gap: no standard prescribes this cash-flow construction for a development-stage asset; WIPO describes sales growing from a low base, peaking and decl Context: VP-V-009, VP-V-010 |  |  |
| V1-19 | 2 | constant or list | rule FV-UNRISKED | ENGINEERING RULE | owner ruling V4 places risk adjustment in calculate-risk-adjusted-npv; this skill rejects probability keys (E_RISK) Gap: none: a house boundary |  |  |
| V1-20 | 4 | constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation and the discount-rate choice are human only Gap: none: an owner ruling Context: VP-V-006 |  |  |
| V1-21 | 5 | constant or list | FORBIDDEN_RISK and FORBIDDEN_ADOPT key lists | ENGINEERING RULE | owner rulings V4 and V5: probability keys and adopted-valuation keys are refused with E_RISK and E_ADOPT; house lists |  |  |
| V1-22 |  | constant or list | end-year and mid-year timing conventions | ENGINEERING RULE | calendar-year convention (t = year - valuation year, minus 0.5 for mid-year); house convention, stated in the script docstring |  |  |
| V1-23 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V1-24 |  | detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |  |  |
| V1-25 |  | detection question | FV-04 | [CHECK] | detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md |  |  |
| V1-26 |  | detection question | FV-05 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-C-001, VP-C-010, VP-C-061, VP-C-090 |  |  |
| V1-27 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V1-28 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V1-29 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V1-30 |  | eval fixture | good-dcf-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V1-31 |  | eval fixture | hand-check-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V1-32 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V1-33 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V1-34 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## V2 · calculate-risk-adjusted-npv (37 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V2-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-06 |  | step | step 6 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V2-08 |  | step | step 8 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V2-09 |  | task card | 01-read-probabilities-and-dcf.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-10 |  | task card | 02-stage-costs.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-11 |  | task card | 03-compute-rnpv.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-12 |  | task card | 04-benchmark-comparison.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-13 |  | task card | 05-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-14 |  | task card | 06-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V2-15 |  | template | rnpv-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V2-16 |  | template | rnpv-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V2-17 | 6 | constant or list | rule FV-RATE-CHOICE | [CHECK] | disabled rule: no registered default or range for a biotech discount rate (the one rate-magnitude source opened concerns capitalizing R&D outlays, VP-V-060, and is out of scope); the script prints [CHECK] and does not compute it |  |  |
| V2-18 | 10 | constant or list | rule FV-STAGE-LAYOUT | ENGINEERING RULE | stages are sequential, costs are spread evenly over a stage's years and weighted by the probability of reaching the stage; no standard prescribes the layout Gap: WIPO describes the principle (VP-V-001) but not a stage layout; the timeline skill's phase probabilities are the usual input Context: VP-V-001, VP-B-001, VP-B-004 |  |  |
| V2-19 | 8 | constant or list | rule FV-SCENARIO-PAIRING | ENGINEERING RULE | low scenario = low probability with high cost; high scenario = high probability with low cost; so the range is the conservative-to-favorable combination Gap: no source prescribes a pairing; ranges are not confidence intervals |  |  |
| V2-20 | 7 | constant or list | rule FV-DOUBLE-COUNT | ENGINEERING RULE | a series already risk-adjusted is refused so that risk is not counted twice (E_DOUBLE) Gap: none: follows the registered separation of rate and probability (VP-V-003) Context: VP-V-003, VP-V-005 |  |  |
| V2-21 |  | constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation, the discount-rate choice and the final probability of success are human only Gap: none: an owner ruling |  |  |
| V2-22 | 9 | constant or list | LEVELS and COST_OF (low uses high cost) | ENGINEERING RULE | pairing table of FV-SCENARIO-PAIRING; house rule |  |  |
| V2-23 |  | constant or list | error codes E_DOUBLE, E_SOURCE, E_SEQUENCE, E_STAGES, E_PROB, E_RANGE | ENGINEERING RULE | input checks of the calculator; house rules |  |  |
| V2-24 |  | detection question | FV-01 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-B-001, VP-B-004, VP-B-060 |  |  |
| V2-25 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V2-26 |  | detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |  |  |
| V2-27 |  | detection question | FV-04 | [CHECK] | detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md |  |  |
| V2-28 |  | detection question | FV-05 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-C-001, VP-C-010, VP-C-061, VP-C-090 |  |  |
| V2-29 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V2-30 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V2-31 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V2-32 |  | eval fixture | good-rnpv-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V2-33 |  | eval fixture | hand-check-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V2-34 |  | eval fixture | two-stage-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V2-35 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V2-36 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V2-37 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## V3 · validate-valuation-assumptions (30 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V3-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-06 |  | step | step 6 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V3-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V3-08 |  | task card | 01-collect-assumptions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-09 |  | task card | 02-trace-to-registers.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-10 |  | task card | 03-run-the-nine-checks.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-11 |  | task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-12 |  | task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V3-13 |  | template | assumption-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V3-14 |  | template | assumption-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V3-15 | 13 | constant or list | rule FV-TERMINAL-SHARE | [CHECK] | disabled rule: no registered threshold for a terminal-value share; the script prints [CHECK] and does not compute it |  |  |
| V3-16 | 11 | constant or list | rule FV-NINE-CHECKS | ENGINEERING RULE | the nine checks and their ok / flag / gap states are this skill's own set Gap: no published checklist for valuation assumptions of a development-stage asset was located |  |  |
| V3-17 | 12 | constant or list | rule FV-NO-VALIDATION-CLAIM | ENGINEERING RULE | the output states counts and that a named reviewer decides; it never calls a valuation validated (E_ADOPT on such a key) Gap: none: a house boundary |  |  |
| V3-18 |  | constant or list | KINDS and NEEDS_UPSTREAM lists | ENGINEERING RULE | house lists of assumption kinds and of kinds that need an upstream pointer |  |  |
| V3-19 |  | detection question | FV-01 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-B-001, VP-B-004, VP-B-060 |  |  |
| V3-20 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V3-21 |  | detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |  |  |
| V3-22 |  | detection question | FV-04 | [CHECK] | detection question written for this skill; no failure analysis was opened for this mode, so it stays [CHECK] in failure-modes.md |  |  |
| V3-23 |  | detection question | FV-05 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-C-001, VP-C-010, VP-C-061, VP-C-090 |  |  |
| V3-24 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V3-25 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V3-26 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V3-27 |  | eval fixture | good-assumptions-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V3-28 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V3-29 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V3-30 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## V4 · design-valuation-scenarios (28 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V4-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-06 |  | step | step 6 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V4-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V4-08 |  | task card | 01-collect-drivers.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-09 |  | task card | 02-named-scenarios-and-weights.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-10 |  | task card | 03-build-scenario-table.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-11 |  | task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-12 |  | task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V4-13 |  | template | scenario-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V4-14 |  | template | scenario-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V4-15 | 14 | constant or list | rule FV-SCENARIO-PAIRING | ENGINEERING RULE | low = adverse end of every driver, high = favorable end; directions are stated per driver Gap: no source prescribes a pairing; ranges are not confidence intervals |  |  |
| V4-16 | 15 | constant or list | rule FV-NO-INVENTED-PROBABILITY | ENGINEERING RULE | weights are the team's; none is invented; no expected value is computed by this skill Gap: none: a house boundary |  |  |
| V4-17 |  | constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation, the choice of rate and any fairness or solvency view are human only Gap: none: an owner ruling |  |  |
| V4-18 |  | constant or list | TOL = 1e-6 for the weight sum | ENGINEERING RULE | arithmetic tolerance; house |  |  |
| V4-19 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V4-20 |  | detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |  |  |
| V4-21 |  | detection question | FV-05 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-C-001, VP-C-010, VP-C-061, VP-C-090 |  |  |
| V4-22 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V4-23 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V4-24 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V4-25 |  | eval fixture | good-scenario-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V4-26 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V4-27 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V4-28 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## V5 · analyze-valuation-sensitivity (32 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V5-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-06 |  | step | step 6 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V5-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V5-08 |  | task card | 01-read-inputs.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-09 |  | task card | 02-scales-and-threshold.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-10 |  | task card | 03-run-sensitivity.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-11 |  | task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-12 |  | task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V5-13 |  | template | sensitivity-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V5-14 |  | template | sensitivity-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V5-15 |  | constant or list | rule FV-OAT | ENGINEERING RULE | one driver is moved at a time with the others at base (a tornado layout); the repo's risk_tornado calculator documents the same convention Gap: the cited tornado literature (Eschenbach 1992) is paywalled and was not opened; WIPO supports only that a single scenario limits the assessment (VP-V-011) Context: VP-V-011 |  |  |
| V5-16 | 17 | constant or list | rule FV-TORNADO-RANK | ENGINEERING RULE | drivers are ranked by absolute swing (rank-by-consequence) Gap: no source prescribes the ranking metric; a swing depends on the scales the team chose |  |  |
| V5-17 | 18 | constant or list | rule FV-SWITCHING | ENGINEERING RULE | the switching value is the scale of one driver at which the base rNPV equals a team-named threshold (bisection) Gap: a house construct; no standard |  |  |
| V5-18 | 16 | constant or list | rule FV-SCALE-SUPPLIED | ENGINEERING RULE | the scales are supplied by the team; the script ships no default percentage Gap: the repo calculator defaults to plus or minus 20 percent; no registered source supports that default, so none is used here |  |  |
| V5-19 |  | constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation and the choice of rate are human only Gap: none: an owner ruling |  |  |
| V5-20 |  | constant or list | DRIVERS (five) | ENGINEERING RULE | house list of drivers; each is a model input of calculate-risk-adjusted-npv |  |  |
| V5-21 | 19 | constant or list | switching_upper = 10 and bisection tolerance 1e-9 | ENGINEERING RULE | house search bounds; the result states when the switching value is not reached |  |  |
| V5-22 |  | detection question | FV-01 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-B-001, VP-B-004, VP-B-060 |  |  |
| V5-23 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V5-24 |  | detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |  |  |
| V5-25 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V5-26 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V5-27 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V5-28 |  | eval fixture | good-sensitivity-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V5-29 |  | eval fixture | hand-check-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V5-30 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V5-31 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V5-32 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## V6 · communicate-valuation-scenarios (28 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V6-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-06 |  | step | step 6 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V6-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V6-08 |  | task card | 01-read-registers.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-09 |  | task card | 02-draft-lines-decisions-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-10 |  | task card | 03-assemble-summary.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-11 |  | task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-12 |  | task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V6-13 |  | template | scenario-communication.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V6-14 |  | template | scenario-communication.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V6-15 | 21 | constant or list | rule FV-POINTER-EVERY-LINE | ENGINEERING RULE | every line points to a register row so a reader can audit it; same rule as the integrated report of the due diligence plugin Gap: none: a house rule |  |  |
| V6-16 | 20 | constant or list | rule FV-REFUSAL-PATTERNS | ENGINEERING RULE | recommendation, fairness / solvency and single-value phrase patterns are the plugin's own lists Gap: lists are not exhaustive; a person reviews every line |  |  |
| V6-17 |  | constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation, the choice of rate and any fairness or solvency view are human only Gap: none: an owner ruling |  |  |
| V6-18 | 22 | constant or list | RECOMMEND, FAIRNESS and POINT phrase patterns | ENGINEERING RULE | house lists; not exhaustive; a person reviews every line |  |  |
| V6-19 |  | constant or list | PTR pointer pattern | ENGINEERING RULE | house syntax of this plugin: <code>:<path> |  |  |
| V6-20 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V6-21 |  | detection question | FV-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-004, VP-V-005, VP-V-030, VP-V-031, VP-V-036 |  |  |
| V6-22 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V6-23 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V6-24 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V6-25 |  | eval fixture | good-summary-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V6-26 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V6-27 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V6-28 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## V7 · identify-comparable-transactions (29 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V7-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-06 |  | step | step 6 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V7-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V7-08 |  | task card | 01-collect-deals.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-09 |  | task card | 02-state-criteria.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-10 |  | task card | 03-screen-deals.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-11 |  | task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-12 |  | task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V7-13 |  | template | comparables-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V7-14 |  | template | comparables-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V7-15 | 25 | constant or list | rule FV-CRITERIA-TEAM | ENGINEERING RULE | the team states the criteria; no default set is shipped Gap: none: a house boundary |  |  |
| V7-16 |  | constant or list | rule FV-SOURCE-DATED | ENGINEERING RULE | every deal carries a source reference and date so a reader can audit it; nothing from memory Gap: none: a house rule |  |  |
| V7-17 | 23 | constant or list | rule FV-SELECTION-FLAG | ENGINEERING RULE | completed deals only can bias a range; the flag is raised when no terminated or withdrawn deal is present Gap: no source quantifies the bias |  |  |
| V7-18 | 24 | constant or list | rule FV-GAP-ALLOWANCE | ENGINEERING RULE | the maximum gaps a deal may carry is the team's input Gap: no source prescribes it |  |  |
| V7-19 |  | constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation, the choice of rate and any fairness or solvency view are human only Gap: none: an owner ruling |  |  |
| V7-20 |  | constant or list | selection flag text | ENGINEERING RULE | house wording; raised when every candidate is completed |  |  |
| V7-21 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V7-22 |  | detection question | FV-06 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-020, VP-V-021, VP-V-035 |  |  |
| V7-23 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V7-24 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V7-25 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V7-26 |  | eval fixture | good-comparables-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V7-27 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V7-28 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V7-29 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## V8 · compare-deal-terms-to-benchmarks (27 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V8-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-06 |  | step | step 6 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V8-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V8-08 |  | task card | 01-collect-terms.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-09 |  | task card | 02-record-subject.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-10 |  | task card | 03-compute-benchmarks.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-11 |  | task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-12 |  | task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V8-13 |  | template | benchmark-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V8-14 |  | template | benchmark-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V8-15 |  | constant or list | rule FV-TERMS-SOURCED | ENGINEERING RULE | every deal's terms carry a source reference and date Gap: none: a house rule |  |  |
| V8-16 | 26 | constant or list | rule FV-MIN-N | ENGINEERING RULE | a range needs at least the team's minimum number of deals; below it the result is 'no range' Gap: no source prescribes the minimum |  |  |
| V8-17 |  | constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation, the choice of rate and any fairness or solvency view are human only Gap: none: an owner ruling |  |  |
| V8-18 | 27 | constant or list | min_n default 3 when the team gives none | ENGINEERING RULE | house default, said in the output; the team may override |  |  |
| V8-19 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V8-20 |  | detection question | FV-06 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-020, VP-V-021, VP-V-035 |  |  |
| V8-21 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V8-22 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V8-23 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V8-24 |  | eval fixture | good-benchmarks-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V8-25 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V8-26 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V8-27 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## V9 · synthesize-market-standard-terms (27 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| V9-01 |  | step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-02 |  | step | step 2 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-03 |  | step | step 3 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-04 |  | step | step 4 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-05 |  | step | step 5 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-06 |  | step | step 6 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V9-07 |  | step | step 7 | ENGINEERING RULE | the human gate is an owner ruling for this capability (V5); not a published standard |  |  |
| V9-08 |  | task card | 01-read-registers.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-09 |  | task card | 02-choose-field-and-caveats.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-10 |  | task card | 03-synthesize.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-11 |  | task card | 04-failure-modes-and-questions.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-12 |  | task card | 05-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register |  |  |
| V9-13 |  | template | market-terms-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a valuation register; answer-first order is the plugin's decision-ready format |  |  |
| V9-14 |  | template | market-terms-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |  |  |
| V9-15 | 28 | constant or list | rule FV-NO-MERGE | ENGINEERING RULE | the valuation range and the benchmark range answer different questions; they are shown side by side, with merged false Gap: no source prescribes how to reconcile them; none is attempted |  |  |
| V9-16 | 29 | constant or list | rule FV-THIN-DATA | ENGINEERING RULE | a range from few deals is flagged and its dispersion shown Gap: no source gives a cut-off; the team's minimum n is used |  |  |
| V9-17 |  | constant or list | rule FV-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling V5: the adopted valuation, the choice of rate and any fairness or solvency view are human only Gap: none: an owner ruling |  |  |
| V9-18 |  | constant or list | cross-check overlap = max of lows to min of highs | ENGINEERING RULE | arithmetic definition of overlap; house |  |  |
| V9-19 |  | detection question | FV-02 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |  |  |
| V9-20 |  | detection question | FV-06 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-020, VP-V-021, VP-V-035 |  |  |
| V9-21 |  | detection question | FV-07 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-V-040, VP-V-041, VP-V-050, VP-V-051 |  |  |
| V9-22 |  | example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V9-23 |  | example | poor-recommendation.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to a registered passage or a rule in the example's own table |  |  |
| V9-24 |  | eval fixture | good-synthesis-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V9-25 |  | eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V9-26 |  | eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |  |  |
| V9-27 |  | eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |  |  |

## S · valuation summary command and tool (plugin level) (4 items)

| # | Top 30 | Type | Item | Status | Reason and stated gap | Confirm / change / reject | Note |
|---|---|---|---|---|---|---|---|
| S-01 | 30 | rule | S-STATUS: workstream status proposed from counts: yellow at 1 gap or 1 triggered or cannot-tell failure mode, red at 5 gaps or 3 such modes, red when the register is missing | ENGINEERING RULE | team-set default thresholds; a client may override with --thresholds; not a standard |  |  |
| S-02 |  | rule | S-CONFLICT: the model range and the benchmark range do not overlap: both are shown side by side, not reconciled, not merged | ENGINEERING RULE | engineering rule |  |  |
| S-03 |  | rule | S-POINTER: every line carries a register pointer; a recommending, fairness or single-value line fails | ENGINEERING RULE | engineering rule |  |  |
| S-04 |  | rule | S-HUMAN: the adopted valuation is HUMAN ONLY and the recommended valuation is empty in every register read | ENGINEERING RULE | owner ruling V5 |  |  |
