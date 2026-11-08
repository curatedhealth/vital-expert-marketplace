# Market register: FICTIONAL FX-801, chronic dermal fibrosis (bd, asset, markets US and EU; reference date 7 November 2026)

Reviewer: UNSIGNED    Status: Draft    Access inputs (price, coverage, access): GAP until the Market Access pack is Released
(Every name, figure and source here is FICTIONAL.)

## Answer first
- Addressable patients, US: 24,000 / 36,000 / 53,200 (low / central / high) = prevalence 120,000 / 150,000 / 190,000 (FICTIONAL registry report, 2021, United States) x diagnosed 0.5 / 0.6 / 0.7 x treated 0.4 (FICTIONAL claims study, 2022, United States). EU: 18,900 is the prevalent population (4.2 per 100,000 x a sourced 450 million denominator, 2020), not the addressable one: no EU shares were supplied.
- Orphan arithmetic: US prevalence of 150,000 persons is below the 200,000 line (ORPHAN-US-200K); EU 0.42 per 10,000 is not more than 5 (ORPHAN-EU-5PER10K). Designation is the regulator's act.
- Competitors: one marketed infusion product; two pipeline entries. C1 (Phase 3, company statement of 4 August 2026) reads out in 2027. C2 (Phase 2) rests on a registry record of 10 February 2025 alone, 635 days old, over the buyer's 365-day limit: flagged.
- Differentiation: 1 of 3 claims supported. Once-daily oral versus infusion points to row A-R2 on a head-to-head comparison. "Fewer infusion reactions than C1" is a cross-trial comparison: not counted. "Best-in-class efficacy" is a sponsor statement: not counted.

## Access inputs
GAP: price, coverage and access assumptions come from the Market Access pack (vital-pharma-market-access, draft 0.1.0, not Released); not used here; the viability skill cannot adjust for them.

## Failure-mode screen
| Mode | State | Register ref or reason | Gap |
|---|---|---|---|
| MG-01 | triggered | population[0] | |
| MG-02 | triggered | pipeline[1] | |
| MG-03 | triggered | differentiation[1] | |
| MG-04 | not triggered | both populations carry source, year and the market's own geography; the EU figure is per 100,000 with a sourced denominator | |

## Questions
1. Seller: provide the head-to-head study report behind the dosing claim.
2. Reviewer: is a registry-only completion date for C2 enough, or should the sponsor be asked?

## Open items
[GAP]: EU diagnosed and treated shares; the seller's target product profile.  Decisions needed (owner): which case definition counts (deal lead).  Hand-off: determine-commercial-viability.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| population figures carry source, year, geography and measure; extrapolation justified | prevalence reporting points to consider; GATHER | VP-G-010, VP-G-011, VP-G-001 to VP-G-003 |
| orphan arithmetic uses each market's own threshold; designation is the regulator's act | statutory thresholds | VP-G-020, VP-G-021 |
| a competitor status from one registry is flagged and cross-checked | registry completion status is commonly inaccurate | VP-G-050, VP-G-051, VP-G-052 |
| a differentiation claim on two side-by-side trials is not counted | trial rates cannot be directly compared | VP-G-040 |
| the seller's TPP is read as supplied; the FDA guidance is a draft | FDA TPP notices | VP-G-030, VP-G-031 |
| overestimation context | consensus forecast outliers | VP-G-060 |
