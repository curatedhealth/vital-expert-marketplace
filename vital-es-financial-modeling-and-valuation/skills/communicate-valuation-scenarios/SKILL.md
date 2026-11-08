---
name: communicate-valuation-scenarios
description: "Use when a buyer (pharma business development or life-sciences investor) needs the valuation scenarios put in front of a decision owner: a summary that starts from the rNPV range with its register pointer, shows what would change the call (switching values and the top-ranked drivers copied from the sensitivity register), lists the decisions needed with the person who decides and the options, and the questions. Every line points to a register row; a line that recommends, states a fairness or solvency view, calls a price fair or states one number as the value is refused. Assembles and checks; adds no finding of its own; adopts nothing. Not for building the model, the sensitivity or the comparables."
metadata:
  level: CF04
  register_code: CF-01.02.02.2.3
  register_id: 272b2085-7ae6-492c-a869-07457b901fb7
  version: 0.1.0
  verb: communicate
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.2 Scenario & Sensitivity Analysis
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, compose-draft]
  feeds: [synthesize-market-standard-terms]
  tools: [scripts/scenario_summary.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: [analyze-valuation-sensitivity]
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Communicate valuation scenarios

## What competent output looks like
- A scenario communication register: the rNPV range with its pointer, then what would change the call (switching values and top drivers with pointers), then the decisions needed (item, owner, options), then the questions.
- Every added line carries a register pointer; lines that recommend, give a fairness or solvency view, or state one number as the value are refused.
- The comparables cross-check appears only as a pointer to the side-by-side, never merged. The human-only list is shown: the rate choice, the adopted valuation, the final probability, any fairness or solvency view, deal terms.
- Status UNSIGNED; adopted valuation HUMAN ONLY.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md) | none | agent asks; human supplies |
| 2 | Read the rNPV range, the sensitivity register and the scenario table with their pointers (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Draft the lines, decisions and questions (task 02) | compose-draft; compare-against-criteria (refusal patterns) | agent drafts; human reviews every line |
| 4 | Assemble and check the summary (task 03) | scripts/scenario_summary.py | agent alone (script); human reviews the output |
| 5 | Screen the failure modes and write the questions (task 04) | compare-against-criteria | agent drafts; human reviews every "triggered" |
| 6 | Validate and write the register (task 05) | scripts/validate_register.py; compose-draft with templates/scenario-communication.md | agent alone (script) |
| 7 | Which decision is taken, and whether anything is adopted | none | human only |

## Rules (general, apply to every case)
1. **Pointers on every line.** A line without a register pointer is refused (E_POINTER).
2. **No recommendation, no fairness or solvency view, no single value.** The scripts refuse them (E_RECOMMEND, E_FAIRNESS, E_POINT); they are an advisor's regulated acts or a person's (VP-V-040 to 043, VP-V-050 to 052).
3. **Start from the range.** A summary without a range, or with low equal to high, is refused (E_RANGE).
4. **Copy, do not compute.** The switching values and the ranks come from the sensitivity register; this skill adds no number.
5. **Decisions have owners.** Each decision names the person who decides and the options (E_DECISIONS).
6. **Comparables are side by side.** Never merged.

## Method anchoring
The refusals follow the registered texts on fairness opinions: what an advisor must disclose about its role, compensation and verification (FINRA Rule 5150, VP-V-040 to 043) and the summary of procedures, findings and bases that Item 1015 requires of an outside report (VP-V-050 to 052). This skill produces neither; it keeps a decision memo from drifting into either. The structure of the summary is the plugin's own.

## Connectors
- rNPV, scenario, sensitivity and comparables registers: read-only.
- VITAL Verify (check_claim, build_citation): check a sentence against its source before it is added.

## Quality bar
- Range with pointer first; what would change the call from the sensitivity register; decisions with owners; questions.
- scenario_summary.py and validate_register.py exit 0.
- No recommendation, fairness or solvency view, or single value anywhere; UNSIGNED until a reviewer signs.
