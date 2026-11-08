---
name: build-dcf-model
description: "Use when a buyer (pharma business development or life-sciences investor) needs the UNRISKED discounted cash flow of a drug asset as a RANGE: net revenue by scenario and year taken from the signed revenue register of forecast-revenue-and-price-ranges, a cost structure, tax, capital and working-capital assumptions supplied by the deal team, a discount-rate RANGE that is labelled a human choice, and an explicit treatment of the terminal value, giving present values by scenario and rate with the share that comes from the terminal value. Applies no probability of success (that is calculate-risk-adjusted-npv), picks no discount rate, adopts no valuation and gives no fairness or solvency view. Not for comparables (identify-comparable-transactions) or deal terms."
metadata:
  level: CF04
  register_code: CF-01.02.02.1.1
  register_id: 9472e27b-1386-4c48-826a-b3dd28e1fee9
  version: 0.1.0
  verb: build
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.1 DCF & Risk-Adjusted NPV Modeling
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, compose-draft]
  feeds: [calculate-risk-adjusted-npv, validate-valuation-assumptions, design-valuation-scenarios]
  tools: [scripts/dcf.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: [forecast-revenue-and-price-ranges, assess-ip-portfolio-and-freedom-to-operate]
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Build DCF model

## What competent output looks like
- A DCF register for one asset (company mode: one per pipeline asset, then a side-by-side roll-up): net revenue by scenario and year, each with the pointer of the revenue register row it came from.
- The cost structure (cost of goods, operating expense, fixed costs, tax rate, capital expenditure, working capital) with a source or a labelled team assumption and a named owner for every line.
- The discount-rate range, labelled HUMAN CHOICE, with the method and evidence the team documents for it (VP-V-030, VP-V-031); no default rate is supplied.
- Present values by scenario and rate, unrisked, with the terminal value stated (or its absence stated) and the share of the value that comes from it. Every figure is a range or a table of a range; never a point.
- The statement that no probability of success is applied here, with the pointer to the skill that applies it.
- The adopted valuation shows HUMAN ONLY and the recommended valuation is empty. Absent evidence is a GAP with the consequence, never a number.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): buyer mode, unit, currency, valuation date, who chooses the rate | none | agent asks; human supplies |
| 2 | Read revenue ranges, launch years and exclusivity end dates from the due diligence registers (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Record cost, tax, capital and working-capital assumptions with owner and source (task 02) | extract-requirements-from-source | agent drafts; the deal team supplies the values |
| 4 | Record the discount-rate range and its documentation (task 03) | extract-requirements-from-source; compare-against-criteria (against the IVS documentation duty) | agent drafts; human only chooses the rate |
| 5 | Compute present values by scenario and rate with the terminal treatment (task 04) | scripts/dcf.py | agent alone (script); human confirms the inputs |
| 6 | Screen the failure modes and write the questions (task 05) | compare-against-criteria (triggered / not triggered / cannot tell) | agent drafts; human reviews every "triggered" |
| 7 | Validate and write the DCF register (task 06) | scripts/validate_register.py; compose-draft with templates/dcf-register.md | agent alone (script) |
| 8 | The choice of discount rate; the terminal assumption; the adopted valuation | none | human only |

## Rules (general, apply to every case)
1. **Unrisked only.** The script rejects probability keys (E_RISK); the probability of success is applied once, in calculate-risk-adjusted-npv.
2. **No default rate, no default cost structure.** Each is the team's input with a source reference or the label HUMAN CHOICE / TEAM ASSUMPTION and an owner.
3. **Rate and cash flow consistent.** A nominal rate goes with nominal cash flows (VP-V-032); the currency is one and nothing is converted.
4. **Terminal value is explicit.** It exists only when the team supplies the annual change with a source; it is discounted with the same rate (VP-V-033); the share is reported and no threshold is applied (rule FV-TERMINAL-SHARE is [CHECK]).
5. **Revenue is read, not rebuilt.** Net revenue comes from the signed revenue register; a missing series is a GAP and the revenue skill is named.
6. **Missing costs are a stated upper bound.** With no cost structure the value is revenue-only and is labelled as such, never read as a valuation.
7. **Ranges and tables of ranges.** No single present value is presented as the value (E_POINT in the validator).
8. **No fairness or solvency view.** Those are an advisor's regulated act (VP-V-040 to 043, VP-V-050 to 052).

## Method anchoring
The rNPV and DCF structure follows the registered WIPO guide (VP-V-001, VP-V-002; a guide, not a standard); the discount rate must be documented and consistent with the cash flow (IVS 103, VP-V-030 to VP-V-033). The cash-flow construction (margins, tax on positive results, capital and working capital) is this skill's own rule (FV-CASHFLOW-ARITHMETIC): no standard prescribes it. Name the rule id beside every figure.

## Connectors
- Revenue register (forecast-revenue-and-price-ranges), exclusivity register (assess-ip-portfolio-and-freedom-to-operate): read-only inputs.
- Navigator (methods_scenario, value_range): replay a human-supplied formula or store the signed low / mid / high; never to choose inputs.
- mcps/scenario_modeler (compute_scenario): optional cross-check of the arithmetic on a formula the team supplies.
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.

## Quality bar
- Revenue series traced to the revenue register or a named GAP; cost structure, tax and rate each with source or owner.
- dcf.py and validate_register.py exit 0; the terminal share is reported; FV-TERMINAL-SHARE listed as [CHECK].
- All of the screened failure modes resolved; at least one question for the named reviewer; adopted valuation HUMAN ONLY; status UNSIGNED until a reviewer signs.
- Open [CHECK] and [GAP] items and the decisions with their owners listed at the end.
