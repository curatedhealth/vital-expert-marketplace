---
name: calculate-risk-adjusted-npv
description: "Use when a buyer (pharma business development or life-sciences investor) needs the RISK-ADJUSTED NPV of a development-stage drug asset as a RANGE, after the unrisked DCF inputs and the development risk and timeline ranges exist: development stages with costs and probabilities of success taken from the timeline register, the cumulative probability applied ONCE to the post-launch cash flows and the costs weighted by the probability of reaching each stage, discounted at a rate RANGE labelled a human choice, with the unrisked comparison alongside. Applies risk adjustment and discounting (owner ruling V4); chooses no rate, adopts no valuation, sets no final probability and gives no fairness or solvency view. Not for comparables or deal terms."
metadata:
  level: CF04
  register_code: CF-01.02.02.1.2
  register_id: b84fdf38-7947-44fe-ad5b-d4923e098f97
  version: 0.1.0
  verb: calculate
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.1 DCF & Risk-Adjusted NPV Modeling
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, compose-draft]
  feeds: [analyze-valuation-sensitivity, validate-valuation-assumptions, design-valuation-scenarios, communicate-valuation-scenarios]
  tools: [scripts/rnpv.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: [build-dcf-model, estimate-development-risk-and-timeline]
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Calculate risk-adjusted NPV

## What competent output looks like
- An rNPV register for one asset: development stages in order, each with years, cost range and probability range, every probability with the pointer of the timeline register row or benchmark stratum it came from.
- The cumulative probability of success by scenario and the reach probability of each stage; the probability applied exactly once (a series already risk-adjusted is refused).
- rNPV by scenario and discount rate as a range, with the unrisked NPV, the expected development cost and the launch value shown separately so a reader can see what the probability did.
- The statement that the rate is a human choice, with its documentation, and that the final probability of success is a person's to set.
- The adopted valuation shows HUMAN ONLY; no fairness or solvency view; absent inputs are GAPs with the consequence.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): stages, probabilities, costs, rate range, owners | none | agent asks; human supplies |
| 2 | Read probabilities, phase durations and the assumed route from the timeline register; read the unrisked DCF inputs (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Record stage costs and years (task 02) | extract-requirements-from-source | agent drafts; the deal team supplies the costs |
| 4 | Compute the cascade and the rNPV by scenario and rate (task 03) | scripts/rnpv.py | agent alone (script); human confirms the inputs |
| 5 | Compare the cumulative probability with the benchmark stratum (task 04) | compare-against-criteria | agent drafts; human reviews |
| 6 | Screen the failure modes and write the questions (task 05) | compare-against-criteria | agent drafts; human reviews every "triggered" |
| 7 | Validate and write the rNPV register (task 06) | scripts/validate_register.py; compose-draft with templates/rnpv-register.md | agent alone (script) |
| 8 | The choice of discount rate; the final probability of success; the adopted valuation | none | human only |

## Rules (general, apply to every case)
1. **Probability applied once.** Post-launch cash flows are multiplied by the cumulative probability and each stage cost by the probability of reaching the stage; the rate carries the cost of capital, not the drug's risk (VP-V-003, VP-V-004); a series already risk-adjusted is refused (E_DOUBLE).
2. **Every probability has a source.** The timeline register row, the benchmark stratum or a labelled team assumption; the script refuses one without it (E_SOURCE).
3. **Scenario pairing is stated.** Low = low probability and high cost; high = high probability and low cost (FV-SCENARIO-PAIRING). Ranges are not confidence intervals.
4. **No default rate.** The rate range is the team's input; the choice is a human decision (FV-RATE-CHOICE is [CHECK]).
5. **Revenue after the last stage only.** Revenue that starts before the last stage ends is refused (E_SEQUENCE).
6. **The final probability is a person's.** The skill shows the cascade and the benchmark comparison and stops.
7. **No fairness or solvency view; no adopted valuation.** Those are human only.

## Method anchoring
The rNPV structure (probabilities at each milestone, rate separate from probability) follows the registered WIPO guide (VP-V-001 to VP-V-005); the rate documentation duty comes from IVS 103 (VP-V-030, VP-V-031); the benchmark comparison reuses the due diligence register of success rates (VP-B-001, VP-B-004, VP-B-060). The stage layout and the pairing are this skill's own rules (FV-STAGE-LAYOUT, FV-SCENARIO-PAIRING). Name the rule id beside every figure.

## Connectors
- Timeline register (estimate-development-risk-and-timeline) and DCF register (build-dcf-model): read-only inputs.
- Navigator (methods_scenario, value_range): replay or store a human-supplied formula and range.
- mcps/real_options_valuation (compute_real_option_binomial_lattice): optional contrast with flexibility value (VP-V-022); not used by the script.
- VITAL Verify (qualify_source, check_claim, build_citation).

## Quality bar
- Every probability traced; the cascade and the reach probabilities shown; rNPV and unrisked NPV side by side.
- rnpv.py and validate_register.py exit 0; FV-RATE-CHOICE listed as [CHECK]; the rate range labelled a human choice.
- All screened failure modes resolved; at least one question; adopted valuation HUMAN ONLY; UNSIGNED until a reviewer signs.
