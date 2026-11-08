---
name: compare-deal-terms-to-benchmarks
description: "Use when a buyer (pharma business development or life-sciences investor) has deal terms for a screened set of comparable deals and for the subject deal, and needs the arithmetic placement: a low / median / high range per term (upfront, milestones, royalty and others the team names) from the supplied deals, the range with each deal left out to show how much one deal moves it, and the subject's position as below, within or above the range, or 'no range' when fewer than the minimum have the term. States positions, not verdicts: never fair, market or standard. Not for choosing the comparables (identify-comparable-transactions), synthesis across terms or the valuation."
metadata:
  level: CF04
  register_code: CF-01.02.02.3.2
  register_id: dbb7c50c-a244-4977-850f-df8e8efdcec9
  version: 0.1.0
  verb: compare
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.3 Benchmarking & Comparable Analysis
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, rank-by-consequence, compose-draft]
  feeds: [synthesize-market-standard-terms]
  tools: [scripts/benchmarks.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: [identify-comparable-transactions]
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Compare deal terms to benchmarks

## What competent output looks like
- A benchmark register: per term the deals that have it, n, low, median, high and the leave-one-out ranges.
- The subject's position per term as below, within or above the range of the supplied deals, or 'no range' with the consequence when n is below the minimum.
- Terms missing for a deal are null and counted, never filled.
- Every position carries the note that it is arithmetic and not a statement that the term is fair, market or standard.
- The adopted valuation and any fairness or solvency view show HUMAN ONLY.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md) | none | agent asks; human supplies |
| 2 | Take the included deals from the comparables register and their terms with sources (task 01) | extract-requirements-from-source | agent drafts; human supplies the terms |
| 3 | Record the subject's terms (task 02) | extract-requirements-from-source | agent drafts; the deal team supplies |
| 4 | Compute ranges, leave-one-out and positions (task 03) | scripts/benchmarks.py; rank-by-consequence orders the terms by how far the subject sits from the range | agent alone (script); human confirms the inputs |
| 5 | Screen the failure modes and write the questions (task 04) | compare-against-criteria | agent drafts; human reviews every "triggered" |
| 6 | Validate and write the benchmark register (task 05) | scripts/validate_register.py; compose-draft with templates/benchmark-register.md | agent alone (script) |
| 7 | Whether any term is acceptable; any fairness or solvency view | none | human only |

## Rules (general, apply to every case)
1. **Terms come from sources.** Each deal has a source reference and date (E_SOURCE); one currency (E_CURRENCY); numeric values only (E_VALUE).
2. **Minimum n.** A term with fewer than the minimum number of deals has 'no range' and a consequence; it is never extrapolated.
3. **Leave-one-out is shown.** It exposes how much one deal moves the range.
4. **Position, not verdict.** The script refuses fair, market and standard wording (E_FAIRNESS).
5. **Missing terms stay null.** They are counted as gaps and not filled.
6. **Market data scarcity is expected** (VP-V-020); the register states n beside every range.
7. **No fairness or solvency view** (VP-V-040, VP-V-051).

## Method anchoring
Deal comparison is a recognized way to ground a valuation but depends on scarce data (VP-V-020, VP-V-021, WIPO guide). Where an advisor gives a fairness opinion it must disclose its role and the basis (VP-V-040), and the filer summarizes procedures and bases (VP-V-051); this skill therefore reports positions and never a verdict. Range statistics and the minimum-n rule are this skill's own.

## Connectors
- comparables register (identify-comparable-transactions): read-only.
- Navigator (methods_scenario, value_range): optional store of a range.
- VITAL Verify (check_claim): check a term against its source passage.

## Quality bar
- Every deal has a source and one currency; n beside every range; leave-one-out present.
- benchmarks.py and validate_register.py exit 0; no verdict wording.
- Terms below the minimum n say 'no range' with the consequence; UNSIGNED until a reviewer signs.
