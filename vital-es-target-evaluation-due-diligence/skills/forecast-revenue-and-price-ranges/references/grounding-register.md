# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages in `verbatim-passages.json`), ENGINEERING RULE (no external source; the reason and the gap are stated) or [CHECK] (disabled until traced). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks that each item type has a row. Written 7 November 2026.

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a deal revenue forecast |
| step | step 2 | ENGINEERING RULE | reads upstream registers; the dependency is the plugin's own chain (market, timeline, exclusivity); no external standard |
| step | step 3 | ENGINEERING RULE | list prices come from dated public pages (context VP-R-030, VP-R-033, VP-R-035, VP-R-036, VP-R-038, VP-R-039); no standard prescribes which price to take as list; gap stated in source-register.md |
| step | step 4 | ENGINEERING RULE | net price is a team assumption because net is not public (VP-R-021, VP-R-023); the assumption itself is a house rule (FC-NET-ASSUMPTION); no source gives a net-to-list ratio |
| step | step 5 | ENGINEERING RULE | uptake and erosion parameters come from the team with sources; no default curve exists (FC-UPTAKE-DEFAULT, FC-LOE-DEFAULT-CURVE are [CHECK]); context VP-R-053, VP-R-060 |
| step | step 6 | ENGINEERING RULE | scripted arithmetic and sensitivity are a house method; the funnel structure follows the payer-side method as context only (VP-R-050, VP-R-051); no standard prescribes seller-side arithmetic |
| step | step 7 | ENGINEERING RULE | the failure-mode screen uses detection questions written for this skill; no published detection checklist exists |
| step | step 8 | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a deal revenue forecast |
| step | step 9 | ENGINEERING RULE | the human gate is the owner's ruling for this skill (the team sets net and uptake; the skill prepares); not a published standard |
| step | step 10 | ENGINEERING RULE | the human gate on the adopted forecast is owner ruling R5; not a published standard |
| task card | 01-patients-launch-exclusivity-probability.md | ENGINEERING RULE | reads fields from upstream registers; house rule that upstream gaps stay gaps |
| task card | 02-list-prices.md | ENGINEERING RULE | list price needs a dated public source (FC-LIST-DATED); source pages and their limits VP-R-030 to VP-R-039 are described in source-register.md; house rule on dating |
| task card | 03-net-price-assumptions.md | ENGINEERING RULE | net price is an assumption because net is not public (VP-R-021, VP-R-022, VP-R-023, VP-R-024); FC-NET-ASSUMPTION is a house rule |
| task card | 04-uptake-and-erosion.md | ENGINEERING RULE | analog selection and erosion parameters are the team's decisions; no default exists; context VP-R-053, VP-R-060, VP-R-001, VP-R-010 |
| task card | 05-compute-ranges-and-sensitivity.md | ENGINEERING RULE | scripted house arithmetic; funnel structure context VP-R-050, VP-R-051; sensitivity as scenarios follows the idea in VP-R-052 but the table is a house method |
| task card | 06-failure-modes-and-questions.md | ENGINEERING RULE | detection questions written for this skill; no published detection checklist |
| task card | 07-write-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a deal revenue forecast |
| template | revenue-register.md | ENGINEERING RULE | house format of this plugin (anatomy 3.2); no published standard prescribes the intake, task-card or register format for a deal revenue forecast; answer-first order is the plugin's decision-ready format |
| template | revenue-register.schema.json | ENGINEERING RULE | schema of the register fields of this skill; house format |
| constant or list | rule FC-FUNNEL | ENGINEERING RULE | revenue = patients x share x adherence x price per patient-year; the eligible-population by treatment-share structure follows the payer-side budget-impact method (context VP-R-050, VP-R-051) but no published standard prescribes th Context: VP-R-050, VP-R-051 |
| constant or list | rule FC-LIST-DATED | ENGINEERING RULE | list price must carry a reference and a date on or before the reference date, or be marked a team assumption; public list sources and their limits are described in references/source-register.md Context: VP-R-030, VP-R-031, VP-R-032, VP-R-033, VP-R-035, VP-R-036, VP-R-039 |
| constant or list | rule FC-NET-NOT-PUBLIC | VERIFIED-REOPENED | restates the registered wording; passage ids VP-R-021, VP-R-022, VP-R-040, VP-R-023, VP-R-024 |
| constant or list | rule FC-NET-ASSUMPTION | ENGINEERING RULE | because net is not public (FC-NET-NOT-PUBLIC) it is an assumption range set by a named deal-team member and labelled so (owner ruling R2) Context: VP-R-020, VP-R-021 |
| constant or list | rule FC-NET-DEFAULT-RATIO | [CHECK] | disabled rule: no default net-to-list ratio is registered; the calculator prints [CHECK] and does not compute it |
| constant or list | rule FC-UPTAKE-DEFAULT | [CHECK] | disabled rule: no default uptake curve or time to peak is registered; the calculator prints [CHECK] and does not compute it |
| constant or list | rule FC-LOE-DEFAULT-CURVE | [CHECK] | disabled rule: no default erosion curve (price or volume) is registered for either small molecules or biologics; the calculator prints [CHECK] and does not compute it |
| constant or list | rule FC-LOE-RAMP | ENGINEERING RULE | linear ramp over years_to_floor from the year after the exclusivity end, applied to price and volume separately; parameters are the team's, with a source reference Context: VP-R-001, VP-R-002, VP-R-004, VP-R-010, VP-R-011, VP-R-012, VP-R-013 |
| constant or list | rule FC-NO-RISK-ADJUSTMENT | ENGINEERING RULE | owner ruling R4: unrisked revenue; probability of success is displayed alongside and never applied; risk-adjusting belongs to the future deal valuation capability |
| constant or list | rule FC-NO-DISCOUNTING | ENGINEERING RULE | owner ruling R4: undiscounted revenue; discounting belongs to the future deal valuation capability |
| constant or list | rule FC-COUNTRY-ONLY | ENGINEERING RULE | owner ruling R3: US, DE, FR, IT, ES, UK country by country; there is no EU price; other markets are a GAP |
| constant or list | rule FC-CURRENCY | ENGINEERING RULE | each country in its own currency; a conversion needs a dated, sourced rate supplied by the team; nothing is converted or inflated |
| constant or list | rule FC-FORECAST-ERROR-CONTEXT | VERIFIED-REOPENED | restates the registered wording; passage ids VP-H-001, VP-H-002, VP-H-003, VP-H-004, VP-H-005, VP-H-010 |
| constant or list | rule FC-MA-CROSSCHECK | ENGINEERING RULE | owner ruling R1: Market Access outputs appear only as side-by-side cross-check columns, never merged, and count only when the pack is Released |
| constant or list | rule FC-ADOPTION-HUMAN | ENGINEERING RULE | owner ruling R5: the forecast the deal team adopts is HUMAN ONLY; ranges only, never a point |
| constant or list | COUNTRIES (US, DE, FR, IT, ES, UK) and currencies | ENGINEERING RULE | owner ruling R3; the six markets and their own currencies; house scope, not a standard |
| constant or list | DRIVERS (seven sensitivity drivers) | ENGINEERING RULE | house list of the inputs of the arithmetic; each is swept low to high with the others at mid |
| constant or list | forbidden keys (discount_rate, wacc, npv, rnpv, risk_adjust, probability_weighted) | ENGINEERING RULE | owner ruling R4; the calculator refuses them with E_DISCOUNT and E_RISK_ADJUST |
| constant or list | scenario pairing (low drivers with latest launch and highest erosion) | ENGINEERING RULE | house rule that the low case is the conservative combination; ranges are not confidence intervals |
| constant or list | loss-of-exclusivity ramp clamp(0,1) | ENGINEERING RULE | house arithmetic so the factor stays between 0 and 1; see FC-LOE-RAMP |
| constant or list | error codes E_MARKET, E_CURRENCY, E_RANGE, E_DATE, E_PRICE_SOURCE, E_NET, E_UPTAKE, E_LOE, E_ASSET | ENGINEERING RULE | input checks of the calculator; house rules |
| detection question | FR-01 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-H-001, VP-H-002, VP-H-010 |
| detection question | FR-02 | [CHECK] | detection question written for this skill; no failure analysis was opened for this mode, so the mode stays [CHECK] in failure-modes.md |
| detection question | FR-03 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-R-021, VP-R-023, VP-R-024 |
| detection question | FR-04 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-R-001, VP-R-002, VP-R-010 |
| detection question | FR-05 | [CHECK] | detection question written for this skill; no failure analysis was opened for this mode, so the mode stays [CHECK] in failure-modes.md |
| detection question | FR-06 | ENGINEERING RULE | detection question written for this skill (gap stated: no published detection checklist exists); the documented finding is in failure-modes.md, passage ids VP-R-020, VP-R-021 |
| example | good-fictional-forecast.md | ENGINEERING RULE | fictional asset RX-640; each fact pattern is mapped to a registered passage in the example's own table |
| example | poor-point-forecast.md | ENGINEERING RULE | fictional asset; the poor example shows the errors the validator rejects; each pattern maps to a registered passage or a rule |
| eval fixture | good-forecast-input.json | ENGINEERING RULE | fictional input built to test the arithmetic; not tied to a real case |
| eval fixture | good-register.json | ENGINEERING RULE | fictional register that passes the validator; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional register built to fail the validator in 17 named ways; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
