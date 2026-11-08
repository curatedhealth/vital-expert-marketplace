---
name: estimate-development-risk-and-timeline
description: Use when a signed-off clinical evidence register exists for a drug asset and the buyer (pharma business development or life-sciences investor) needs the probability of technical and regulatory success as a range, a timeline range, the three to five drivers that move them most, and the implications for the buyer's decision. US and EU only. Needs the register from review-clinical-data-quality. Not for revenue, price or deal value, and not for setting the final number (a person owns it).
metadata:
  level: CF04
  register_code: CF-01.02.06.1.3
  register_id: eddd38ad-fc9b-469f-8ace-d8d9e16e28b4
  version: 0.1.0
  verb: estimate
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.1 Scientific & Clinical Due Diligence
  agent: bd-due-diligence-lead
  atoms: [compare-against-criteria, rank-by-consequence, compose-draft]
  requires: [review-clinical-data-quality]
  feeds: [evaluate-regulatory-pathway-and-legal-risk, determine-commercial-viability]
  tools: [scripts/pos_chain.py, scripts/timeline_range.py, scripts/tornado_inputs.py, scripts/bio_pinned_rows.json]
  tier: "Full (owner ruling 7 November 2026): the Full proof is the chain F -> A -> B; back-test set designed, not frozen"
  release_state: Draft (Q1-Q6 built; Q7 back-test pending; Q8 practitioner review pending)
---

# Estimate development risk and timeline

## What competent output looks like
- The probability of technical success and of regulatory success as ranges, with the benchmark stated
  first and each adjustment tied to a stated reason and to a register row or failure mode.
- A timeline range from the benchmark phase durations, with adjustments stated the same way.
- The assumed regulatory route and review months per market (US, EU) as a labelled deal-team assumption, and the approval years early, mid and late from the start date; these are the launch inputs read by the revenue and price skill (forecast-revenue-and-price-ranges). The review months sit inside the benchmark's last phase and are never added to the total.
- The three to five drivers that move probability and timing most, from the sensitivity result.
- Decision implications by buyer mode (BD: fit and deal-term implications such as milestones and
  contingent-value terms; investor: the next value inflection and the capital needed to reach it).
- The final number is marked UNSIGNED until a named person records it. No point estimate stands alone.
- EU approval probability is a stated [GAP]: the references hold no EU approval benchmark.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md); confirm the register is signed off | none | agent asks; human supplies |
| 2 | Choose ONE benchmark stratum (phase, indication, modality, biomarker selection as patient preselection) (task 01) | references/benchmarks/ | agent drafts; human confirms the stratum |
| 3 | Chain the benchmark (task 02) | scripts/pos_chain.py | agent alone (script) |
| 4 | Propose adjustments, each with reason and reference (task 03) | compare-against-criteria (criteria = register findings and failure modes) | agent drafts; human reviews every adjustment |
| 5 | Run ranges and sensitivity; build the timeline (task 04) | scripts/pos_chain.py, scripts/timeline_range.py, scripts/tornado_inputs.py; Navigator methods_risk_tornado cross-check | agent alone (script) |
| 6 | Rank drivers and state decision implications by buyer mode (task 05) | rank-by-consequence; compose-draft | agent drafts; human reviews |
| 7 | Write the estimate (task 06) | compose-draft (templates/estimate.md) | agent alone |
| 8 | Final number | none | human only |

## Rules (general, apply to every case)
1. **Benchmark first.** The estimate starts from one published stratum. Strata are not combinable (the
   source has no cross-cells), so every other asset attribute is an adjustment with a reason.
2. **No adjustment without a reason and a reference.** Reason of a stated length; ref is a register row id
   or a failure-mode id. The script rejects anything else.
3. **Direction.** A multiplier above 1 needs an upward basis tied to a register finding. A result above
   the benchmark needs a stated reason (failure mode FM-01).
4. **Sensitivity on every adjustment.** The output lists the overall mid without each adjustment.
5. **Ranges, not points.** Low, mid and high come from the adjustment bounds. They are not a confidence interval.
6. **Human owns the number.** `final_number` needs value, owner and date.
7. **Scope.** US benchmark only; EU probability [GAP]; other markets [GAP]. No peak sales, price or deal value.

## Method anchoring
Benchmarks: BIO/Informa/QLS 2021 (B1). Name the benchmark figure and page in the output. Adjustments cite the RoB 2, estimand or
precedent finding behind them (see skill A's references). See references/method-standards.md. If no source covers a judgement, say so and mark [CHECK].

## Connectors
- Navigator methods_risk_tornado / methods_scenario: replay the product formula from scripts/tornado_inputs.py as a cross-check. They score only inputs a person supplied.
- Navigator value_range: store the signed low / mid / high range on a draft; a point estimate is refused.
- VITAL Verify (qualify_source, check_claim): any new benchmark source.
- Literature search: locate a publication the team cites for an adjustment.

## Quality bar
- Every adjustment: reason, reference, bounds, sensitivity.
- Script exit 0 for chain and timeline; tornado payload replays to the same number.
- UNSIGNED shown until the owner is named.
- Open [CHECK] and [GAP] items, decisions (with decider) and next skill listed at the end.
- Upstream: the class precedent and evidence-chain flags in a signed mechanism register (assess-scientific-validity-and-moa) are inputs a person weighs when reading an adjustment; they set no number.
- Hand-off: the ranges are a condition in determine-commercial-viability (expected launch timing).
- Hand-off: the ranges feed evaluate-regulatory-pathway-and-legal-risk (route options refine the timeline assumption; they do not replace these numbers).
