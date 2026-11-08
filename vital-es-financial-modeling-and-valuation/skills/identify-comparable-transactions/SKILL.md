---
name: identify-comparable-transactions
description: "Use when a buyer (pharma business development or life-sciences investor) has candidate licensing or acquisition deals that a person supplied, each with a dated source, and needs them screened against the team's own criteria: therapeutic area, stage, modality, date window, with match, mismatch or gap recorded per criterion, the excluded deals with the reason, the number included and a selection flag when only completed deals are present. The criteria are the team's; the script ships none and fetches no deal. Says nothing on whether any deal is fair or a price is right. Not for extracting terms (compare-deal-terms-to-benchmarks) or for the valuation itself."
metadata:
  level: CF04
  register_code: CF-01.02.02.3.1
  register_id: 4792c430-970e-4982-8e5a-628b8de9d21d
  version: 0.1.0
  verb: identify
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.3 Benchmarking & Comparable Analysis
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, classify-text-labels, compose-draft]
  feeds: [compare-deal-terms-to-benchmarks]
  tools: [scripts/comparables.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: []
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Identify comparable transactions

## What competent output looks like
- A comparables register: the criteria the team stated, the candidate deals, and per deal a match / mismatch / gap on each criterion with the source reference and date.
- The deals included and the deals excluded with the reason, the count of each, and the minimum the team asked for.
- The selection flag: when every candidate is a completed deal, terminated and withdrawn deals are absent and the range can be biased (FV-06).
- The statement that comparability is the team's judgment and that nothing here says a deal is fair.
- A candidate with no dated source is refused; nothing is taken from memory.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md) | none | agent asks; human supplies |
| 2 | Collect the candidate deals with a dated source each (task 01) | extract-requirements-from-source | agent drafts; human supplies the sources |
| 3 | Record the criteria and the window (task 02) | extract-requirements-from-source | agent drafts; the deal team states them |
| 4 | Screen each deal against the criteria (task 03) | scripts/comparables.py; compare-against-criteria for the gap cases; classify-text-labels for the stage and modality labels | agent alone (script); human confirms every exclusion |
| 5 | Screen the failure modes and write the questions (task 04) | compare-against-criteria | agent drafts; human reviews every "triggered" |
| 6 | Validate and write the comparables register (task 05) | scripts/validate_register.py; compose-draft with templates/comparables-register.md | agent alone (script) |
| 7 | Whether the included deals are comparable to the subject | none | human only |

## Rules (general, apply to every case)
1. **Criteria are the team's.** The script ships none (E_CRITERIA) and the window is validated (E_WINDOW).
2. **Every deal has a dated source.** No deal enters without a reference and a date, and a source dated after the reference date is refused (E_SOURCE, E_SOURCE_DATE).
3. **Match, mismatch or gap per criterion.** A deal with more gaps than the team allows is excluded and the reason is stated.
4. **Selection flag.** When every candidate is a completed deal the register says so (FV-06).
5. **Guideline transactions are the market approach for intangibles** (VP-V-034), and unlike assets need a comparative analysis of similarities and differences (VP-V-035); the register records the comparison but does not perform it for the team.
6. **Scarce comparables are normal for early-stage assets** (VP-V-020); fewer than the minimum is a stated gap, not a fill.
7. **No fairness statement.**

## Method anchoring
The WIPO guide states that comparing recent relevant deals is essential and that the usefulness of the market approach is limited by scarce comparable deals, especially early stage (VP-V-020, VP-V-021); IVS 210 states the guideline transactions method is generally the only market approach method for intangibles (VP-V-034) and IVS 103 requires a comparative analysis where the market information is not the same asset (VP-V-035). The screening layout, the gap allowance and the selection flag are this skill's own rules.

## Connectors
- Navigator (catalogue_search, services_get): optional pointers for ontology labels of stage and modality.
- VITAL Verify (qualify_source, check_claim): admit and check each deal source the person supplies.
- No deal database is connected; deals are supplied by a person with their sources.

## Quality bar
- Every deal has a dated source; criteria stated by the team; each criterion has match, mismatch or gap.
- comparables.py and validate_register.py exit 0; the included and excluded counts add to the candidate count.
- Selection flag present when only completed deals are supplied; UNSIGNED until a reviewer signs.
