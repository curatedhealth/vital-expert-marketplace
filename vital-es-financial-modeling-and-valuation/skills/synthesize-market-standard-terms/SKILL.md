---
name: synthesize-market-standard-terms
description: "Use when a buyer (pharma business development or life-sciences investor) has the benchmark ranges of compare-deal-terms-to-benchmarks and the rNPV range of calculate-risk-adjusted-npv and needs them put side by side, term by term: n, range, the dispersion of the range, a thin-data flag, the span without each deal, and the overlap between the valuation range and the benchmark range, shown but never merged, averaged or reconciled. Caveats carry the sample's limits. The adopted valuation and any fairness or solvency view stay with people. Not for building either input or for deciding which terms are 'standard': the skill produces ranges and a cross-check, not a market standard."
metadata:
  level: CF04
  register_code: CF-01.02.02.3.3
  register_id: 3580146b-d8f8-4ee4-a898-6eb1e90045ea
  version: 0.1.0
  verb: synthesize
  capability: CF-01.02.02 Financial Modeling & Valuation
  mission: CF-01.02.02.3 Benchmarking & Comparable Analysis
  agent: npv_analyst (existing agent row, recommended; not written by the migration)
  atoms: [extract-requirements-from-source, compare-against-criteria, compose-draft]
  feeds: [val-summary]
  tools: [scripts/market_standard.py, scripts/validate_register.py]
  tier: "Standard (owner ruling of 8 November 2026; the Full tier of ruling V6 was provisional and is retired): this skill is validated with Standard-tier known-answer sets (arithmetic, rules and filing fidelity); not run"
  requires: [compare-deal-terms-to-benchmarks, calculate-risk-adjusted-npv]
  release_state: Draft (build complete; known-answer set built, not run; back-test or review pending)
---

# Synthesize market-standard terms

## What competent output looks like
- A market-terms register: per term n, low / median / high, dispersion (high over low), a thin-data flag and the leave-one-out span.
- A cross-check between the valuation range (with its register pointer) and a benchmark range, side by side with the overlap stated and an explicit 'merged: false'.
- Caveats on the sample: hand-picked, completed deals only, small n.
- The decisions that remain with people: whether the deals apply, which range informs the negotiation, any fairness or solvency view.
- Recommended valuation empty; adopted valuation HUMAN ONLY.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md) | none | agent asks; human supplies |
| 2 | Read the benchmark and rNPV registers with their pointers (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Choose the benchmark field for the cross-check and the caveats (task 02) | extract-requirements-from-source | agent drafts; the deal team chooses |
| 4 | Synthesize per term and cross-check the ranges (task 03) | scripts/market_standard.py | agent alone (script); human confirms the inputs |
| 5 | Screen the failure modes and write the questions (task 04) | compare-against-criteria | agent drafts; human reviews every "triggered" |
| 6 | Validate and write the market-terms register (task 05) | scripts/validate_register.py; compose-draft with templates/market-terms-register.md | agent alone (script) |
| 7 | Which range informs the negotiation; the adopted valuation; any fairness or solvency view | none | human only |

## Rules (general, apply to every case)
1. **Side by side, never merged.** The valuation range and the benchmark range answer different questions; the output says merged: false and does not average them.
2. **Thin data is flagged.** A range from few deals carries a thin-data flag and its dispersion.
3. **Caveats travel with the range** (hand-picked sample, completed deals only).
4. **No market standard is declared.** The script refuses fair, market and standard wording (E_FAIRNESS).
5. **Benchmarks come from the previous skill.** A missing or malformed benchmark block is refused (E_BENCH).
6. **Recommended valuation stays empty; adopted valuation is HUMAN ONLY.**
7. **Market data is scarce and comparability is a judgment** (VP-V-020, VP-V-035).

## Method anchoring
Deal data ground a valuation but are scarce (VP-V-020, WIPO guide); where market information is not the same asset a comparative analysis of similarities and differences is needed (VP-V-035, IVS 103). A fairness view belongs to an advisor with disclosures (VP-V-040) and a summary of procedures and bases (VP-V-051, VP-V-052); this skill reports ranges and refuses a verdict. The side-by-side layout, the dispersion measure and the thin-data flag are this skill's own.

## Connectors
- benchmark and rNPV registers: read-only.
- Navigator (value_range): optional store of the ranges, never merged.
- VITAL Verify (check_claim): check a sentence against its source.

## Quality bar
- Per-term n, range, dispersion and thin-data flag; the cross-check shows both ranges and merged: false.
- market_standard.py and validate_register.py exit 0; no verdict wording.
- Caveats present; recommended valuation empty; UNSIGNED until a reviewer signs.
