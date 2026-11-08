---
name: design-valuation-scenarios
description: "Use when a buyer (pharma business development or life-sciences investor) has a valuation model and needs the SCENARIOS designed before they are run: the drivers with low, mid and high ranges, each with a source or a labelled team assumption and an owner, the standard low / mid / high set built by one stated pairing rule (adverse ends in the low scenario, favorable ends in the high one), named scenarios the team defines on top, a coverage check of the required drivers and a weights check. Invents no scenario probability and computes no expected value; chooses no rate; adopts no valuation. Not for running the model (calculate-risk-adjusted-npv) or sensitivity (analyze-valuation-sensitivity)."
metadata:
  level: CF04
  register_code: CF-01.02.02.2.1
  register_id: a2970c37-4a5c-4f89-b688-fca808249707
  version: 0.1.0
  verb: design
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.2 Scenario & Sensitivity Analysis
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, compose-draft]
  feeds: [analyze-valuation-sensitivity, communicate-valuation-scenarios]
  tools: [scripts/scenarios.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: [calculate-risk-adjusted-npv]
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Design valuation scenarios

## What competent output looks like
- A scenario register: the drivers with unit, direction (higher or lower is better), low / mid / high, source or labelled owner.
- The standard three-scenario table by the stated pairing rule, every cell showing which end of the driver it took.
- Named scenarios defined by the team (settings per driver); drivers a named scenario leaves unset are listed.
- Coverage: required drivers without a range are gaps with the consequence. Weights, when the team gives them, all present and summing to 1; no probability is invented and no expected value is computed.
- The adopted valuation shows HUMAN ONLY.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md) | none | agent asks; human supplies |
| 2 | Collect the drivers and their ranges with sources or owners (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Define the named scenarios the team wants and any weights (task 02) | extract-requirements-from-source | agent drafts; the deal team defines |
| 4 | Build the scenario table and the checks (task 03) | scripts/scenarios.py | agent alone (script); human confirms the inputs |
| 5 | Screen the failure modes and write the questions (task 04) | compare-against-criteria | agent drafts; human reviews every "triggered" |
| 6 | Validate and write the scenario register (task 05) | scripts/validate_register.py; compose-draft with templates/scenario-register.md | agent alone (script) |
| 7 | The scenario set; the weights; the adopted valuation | none | human only |

## Rules (general, apply to every case)
1. **One pairing rule, stated.** The low scenario takes the adverse end of every driver, the high the favorable end (FV-SCENARIO-PAIRING); the range is not a confidence interval.
2. **Every driver has a source or a labelled owner.** A driver needs a source_ref, or the label TEAM ASSUMPTION with a named owner; an owner alone is refused (E_SOURCE).
3. **No invented probabilities.** Weights are the team's, all or none, summing to 1; no expected value is computed here (E_WEIGHT).
4. **Gaps stay gaps.** A required driver with no range is listed with its consequence and not filled.
5. **Relying on one scenario limits the assessment** (VP-V-011); the table gives the standard set and the team's named ones.
6. **No adopted valuation, no fairness view.**

## Method anchoring
A single scenario limits the assessment to one set of outcomes (VP-V-011), and costs may need simulated scenarios for higher costs and delays (VP-V-012); both are registered WIPO statements (a guide, not a standard). The pairing rule, the weights rule and the coverage check are this skill's own rules.

## Connectors
- Risk-adjusted NPV register (calculate-risk-adjusted-npv): read-only.
- mcps/scenario_modeler (compute_scenario): optional cross-check of a team formula.
- Navigator (methods_scenario): replay a human-supplied formula.

## Quality bar
- Every driver sourced or owned; the pairing table complete; coverage gaps listed.
- scenarios.py and validate_register.py exit 0; weights absent or complete.
- At least one question; adopted valuation HUMAN ONLY; UNSIGNED until a reviewer signs.
