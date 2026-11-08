---
name: analyze-valuation-sensitivity
description: "Use when a buyer (pharma business development or life-sciences investor) has an rNPV model and needs to see what moves the result: one-at-a-time swings for revenue, probability of success, development cost, launch delay and discount rate, a tornado ranking by absolute swing, and switching values (the scale of revenue or of probability at which the base rNPV reaches a threshold the team names). The scales and the threshold are the team's. Describes the model, not the asset; chooses no rate, adopts no valuation, gives no fairness or solvency view. Not for building the model or the narrative (communicate-valuation-scenarios)."
metadata:
  level: CF04
  register_code: CF-01.02.02.2.2
  register_id: 4863908b-1081-413b-9234-c4c6320ead14
  version: 0.1.0
  verb: analyze
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.2 Scenario & Sensitivity Analysis
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, rank-by-consequence, compose-draft]
  feeds: [communicate-valuation-scenarios]
  tools: [scripts/sensitivity.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: [calculate-risk-adjusted-npv, design-valuation-scenarios]
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Analyze valuation sensitivity

## What competent output looks like
- A sensitivity register: the base case (mid scenario, one rate) and, per driver, the value at the low and high end with the scales the team supplied.
- The tornado ranking by absolute swing with ranks, so the reader sees the drivers in order of effect.
- Switching values for revenue and probability: the scale at which the base rNPV equals the team's threshold, or the statement that it is not reached in the range.
- The statement that the ranking describes the model and depends on the chosen scales; the adopted valuation shows HUMAN ONLY.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md) | none | agent asks; human supplies |
| 2 | Read the rNPV inputs and the scenario table (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Record the scales, the delay, the threshold and the rate (task 02) | extract-requirements-from-source | agent drafts; the deal team supplies |
| 4 | Run the swings, the ranking and the switching values (task 03) | scripts/sensitivity.py; rank-by-consequence orders the drivers | agent alone (script); human confirms the inputs |
| 5 | Screen the failure modes and write the questions (task 04) | compare-against-criteria | agent drafts; human reviews every "triggered" |
| 6 | Validate and write the sensitivity register (task 05) | scripts/validate_register.py; compose-draft | agent alone (script) |
| 7 | The scales, the threshold, the rate and the adopted valuation | none | human only |

## Rules (general, apply to every case)
1. **Scales are supplied.** No default percentage (E_SCALE); the repo tornado defaults to plus or minus 20 percent and that default is not used here.
2. **One driver at a time, others at base** (FV-OAT); the base is the mid scenario at the chosen rate.
3. **Rank by absolute swing** (FV-TORNADO-RANK, rank-by-consequence).
4. **Switching value by bisection** to a stated tolerance; reported as not reached in range when the sign does not change.
5. **The model is imported, not copied.** The arithmetic is calculate-risk-adjusted-npv's; the probability is applied once there.
6. **The ranking is not a finding about the asset.** It depends on the scales.
7. **No adopted valuation, no fairness view.**

## Method anchoring
A single scenario limits the assessment (VP-V-011, WIPO guide, not a standard). The one-at-a-time layout, the ranking metric and the switching value are this skill's own rules; the tornado literature the repo calculator cites (Eschenbach 1992; Saltelli et al. 2008) is paywalled and was not opened.

## Connectors
- mcps/risk_tornado (compute_tornado) and mcps/scenario_modeler (compute_scenario): optional cross-check on a formula the team supplies.
- Navigator (methods_risk_tornado, value_range): replay a human-supplied formula and store a range.
- rNPV and scenario registers: read-only.

## Quality bar
- Scales and threshold supplied by the team; every driver's low and high case shown; ranks consecutive.
- sensitivity.py and validate_register.py exit 0; switching values stated or 'not reached'.
- At least one question; adopted valuation HUMAN ONLY; UNSIGNED until a reviewer signs.
