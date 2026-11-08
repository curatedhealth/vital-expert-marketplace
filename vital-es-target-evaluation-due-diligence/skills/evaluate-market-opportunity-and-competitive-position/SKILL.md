---
name: evaluate-market-opportunity-and-competitive-position
description: "Use when a buyer (pharma business development or life-sciences investor) needs the market picture of a drug asset, or of each pipeline asset of a company, in the US and EU: patient population (incidence or prevalence with source, year and geography), diagnosed and treated shares where sourced, unmet need, current standard of care, competing marketed products and pipeline with dated sources, and the asset's differentiation against its target product profile, each claim tied to the clinical evidence register and the mechanism register. Produces a market register and its gaps. States no peak-sales, price, coverage or access figure (the viability skill builds a sales range from analogs; price, coverage and access come from the Market Access pack and are a gap until it is Released). Not for valuation or deal value, not for revenue and price ranges (use forecast-revenue-and-price-ranges), not for markets other than US and EU."
metadata:
  level: CF04
  register_code: CF-01.02.06.2.1
  register_id: 53b7ff7c-ff72-4f67-82d1-af0dffc3eacc
  version: 0.1.0
  verb: evaluate
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.2 Commercial & Market Assessment
  agent: bd-due-diligence-lead
  atoms: [extract-requirements-from-source, compare-against-criteria, compose-draft]
  feeds: [determine-commercial-viability]
  tools: [scripts/market_check.py, scripts/validate_register.py]
  tier: "Full (owner ruling 7 November 2026): the capability is Full; this skill is validated with a Standard-style known-answer set, built in a later lane"
  requires: []
  release_state: Draft (Q1-Q6 built; Q7 back-test pending; Q8 practitioner review pending)
---

# Evaluate market opportunity and competitive position

## What competent output looks like
- A market register per asset and market (company unit: one per pipeline asset, then a side-by-side roll-up):
  1. patient population: incidence or prevalence, each figure with source, year and geography; diagnosed and treated shares where sourced; addressable patients as a low, central, high arithmetic result (population times each sourced share);
  2. unmet need and current standard of care, each statement sourced;
  3. competing marketed products, each with a dated source;
  4. competing pipeline: phase, mechanism and expected timing, each entry with a dated source and the basis of the timing (company statement, registry, regulator, analyst); registry-only entries flagged;
  5. differentiation of the asset against its target product profile: a claim counts only if it points to a row of the clinical evidence register (skill A) or the mechanism register (skill F) and rests on a head-to-head or indirect comparison. Sponsor statements and cross-trial comparisons are listed as "not counted";
  6. every gap, with its consequence.
- No population figure from memory; a figure from another geography is a GAP, never a proxy.
- Orphan thresholds are shown as arithmetic on the supplied prevalence (US: less than 200,000 persons; EU: not more than 5 in 10,000). A designation is the regulator's act.
- Pricing, reimbursement and access assumptions come from the Market Access pack and are never built here. Until that pack is Released they are a GAP and the register says what that blocks.
- No peak-sales, revenue, price or market-share figure appears in the register.
- Absent evidence is a GAP with the consequence stated. Never "unknown".

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): buyer mode, unit, markets, target product profile, documents | none | agent asks; human supplies |
| 2 | Population and addressable patients (task 01) | extract-requirements-from-source; scripts/market_check.py | agent drafts; human reviews |
| 3 | Standard of care and unmet need (task 02) | extract-requirements-from-source | agent drafts; clinician reviews |
| 4 | Competing marketed products (task 03) | extract-requirements-from-source; connectors | agent drafts; human reviews |
| 5 | Competing pipeline with dated sources (task 04) | extract-requirements-from-source; scripts/market_check.py | agent drafts; human reviews registry-only entries |
| 6 | Differentiation against the target product profile (task 05) | compare-against-criteria (supported / not counted); scripts/market_check.py | agent drafts; human reviews every "supported" |
| 7 | Screen failure modes and write the questions (task 06) | compare-against-criteria (triggered / not triggered / cannot tell) | agent drafts; human reviews every "triggered" |
| 8 | Validate and write the register (task 07) | scripts/validate_register.py; compose-draft with templates/market-register.md | agent alone (script) |
| 9 | Which population definition and which market count for the decision; sign-off of the register | none | human only |

## Rules (general, apply to every case)
1. **Source, year, geography.** Every population or share figure carries all three; the script rejects a figure whose geography is not the market's own.
2. **Differentiation points at the registers.** A claim with no A or F row behind it is "not counted", however it is worded. A cross-trial comparison is "not counted".
3. **Pipeline carries dates.** Each entry has a source with a date on or before the reference date. A registry-only entry is flagged: registry status and dates are often outdated or wrong (BMJ Open 2017).
4. **No sales, price or access figure.** The validator rejects text that states one. Price, coverage and access inputs are a GAP naming the Market Access pack.
5. **Rule status.** Only VERIFIED-REOPENED rules compute; the context figures are never applied as a band (references/rules/market-rules.json).
6. **No standard exists.** No published standard exists for market sizing or competitive positioning; the arithmetic and the checks are engineering rules of this skill (references/method-standards.md).
7. **Markets.** US and EU as before; in addition the six revenue countries (US, DE, FR, IT, ES, UK) are read one by one: each country figure carries its own source, year and geography (a figure from another geography is a [GAP], not a proxy) and appears in a `country_patients` block (low / central / high) that the revenue skill reads as low / mid / high. A country with no sourced figure is a GAP with its consequence. Another market is a [GAP].

## Method anchoring
Name the rule id (for example ORPHAN-US-200K) and the source id from references/method-standards.md beside every flag. For judgements no listed standard covers (population definition, competitive positioning), say so and mark [CHECK]; the skill anchors on the sourced failure modes in references/failure-modes.md and on the statutory definitions it quotes.

## Connectors
- Literature (literature_search_literature, literature_grade_evidence): locate named epidemiology and standard-of-care publications. A lead for a person to check, not a population figure on its own.
- ClinicalTrials.gov (search_trials, get_trial_details): competing pipeline leads, with the record's last-update date as the source date. Live use only; in the back-test only arm C may use connectors, and only those that pass the leakage guard, as designed (evals/backtest/README.md). Registry status is never the only basis for a timing.
- Market Access pack (vital-pharma-market-access, read-only; draft 0.1.0): competitor-pipeline-and-launch-signals, competitor-access-tracking and market-pathway-mapping can supply dated competitor signals; price, coverage and access are not taken from it until it is Released.
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.
- Navigator (catalogue_get): the competency row and its siblings.

## Quality bar
- 100% of population, share, competitor and pipeline rows: source (with date where required) or [CHECK]; absent fields GAP with consequence.
- market_check exit 0 and validate_register exit 0; disabled rules listed.
- All four failure modes (MG-01 to MG-04) screened and resolved.
- At least one question for the named reviewer; status UNSIGNED until a named reviewer signs.
- Open [CHECK] and [GAP] items, decisions (with decider) and the hand-off (determine-commercial-viability) listed at the end.
