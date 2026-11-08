---
name: review-clinical-data-quality
description: Use when a buyer (pharma business development or life-sciences investor) has clinical data on a drug asset, or on a company's pipeline assets, and needs an evidence register that shows what each trial or analysis actually measured, how biased it may be, whether it replicated, and what is missing. Produces a register, one row per trial or analysis, with gaps scored and failure modes carried. US and EU only. Not for judging the mechanism (Scientific Validity & MOA, not in this release), not for probability or timing (use estimate-development-risk-and-timeline), not for revenue or deal value.
metadata:
  level: CF04
  register_code: CF-01.02.06.1.2
  register_id: 59ead1cd-61ed-4b54-aefd-179d65b38ed6
  version: 0.1.0
  verb: review
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.1 Scientific & Clinical Due Diligence
  agent: bd-due-diligence-lead
  atoms: [extract-requirements-from-source, compare-against-criteria, classify-text-labels, compose-draft]
  requires: []
  feeds: [estimate-development-risk-and-timeline, evaluate-regulatory-pathway-and-legal-risk, evaluate-market-opportunity-and-competitive-position, determine-commercial-viability]
  tools: [scripts/validate_register.py]
  tier: "Full (owner ruling 7 November 2026): the Full proof is the chain F -> A -> B; back-test set designed, not frozen"
  release_state: Draft (Q1-Q6 built; Q7 back-test pending; Q8 practitioner review pending)
---

# Review clinical data quality

## What competent output looks like
- One register row per trial or analysis: design, phase, size, control, primary endpoint, estimand (what
  was actually measured: the four E9(R1) attributes, with a strategy for each intercurrent event), risk of bias, replication status, safety signals, regulatory precedent for the
  endpoint, and gaps.
- Absent evidence is a GAP with what is missing and why it matters. Never "unknown".
- Every failure mode in references/failure-modes.md is screened; each triggered mode is a register row
  or is dismissed in writing.
- Subgroup claims and single-arm results are flagged. A press release or conference abstract is never
  treated as the regulatory record.
- US regulatory precedent for the endpoint is checked against the FDA surrogate table; for the EU the
  register says that no EU surrogate table exists and cites a qualification opinion only if one is found.
- Each gap carries one to three options to close it (for example request the study report, an independent analysis, a seller call), each with effort and risk. Options only; the team decides.
- Each gap carries one to three options to close it (for example request the study report, an independent analysis, a seller call), each with effort and risk. Options only; the team decides.
- Nothing from memory: [CHECK] for an unverified rule, [GAP] for a missing fact.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): buyer mode, unit, markets, documents provided | none | agent asks; human supplies |
| 2 | Extract trial and analysis facts from the documents (task 01) | extract-requirements-from-source (rows of facts with passages) | agent alone |
| 3 | State the estimand per primary analysis (task 02) | references/method-standards.md (ICH E9(R1)) | agent drafts; human reviews |
| 4 | Judge risk of bias per randomized trial (task 03) | references/method-standards.md (RoB 2); non-randomized: tool named in the row | agent drafts; human reviews every judgement |
| 5 | Replication, safety, regulatory precedent (task 04) | classify-text-labels for status labels; connectors | agent, human review |
| 6 | Screen against failure modes (task 05) | compare-against-criteria (state set: triggered / not triggered / cannot tell) | agent; human reviews every "triggered" |
| 7 | Validate and write the register (task 06) | scripts/validate_register.py; compose-draft with templates/evidence-register.md | agent alone (script) |
| 8 | Sign-off of the register | none | human only |

## Rules (general, apply to every case)
1. **Absence rule.** No evidence for a field gives the value GAP, with `missing` and `why_it_matters`
   in `gaps[]`. The value "unknown" is rejected by the script.
2. **Failure-mode carry-through.** Each mode marked triggered names a register row (`register_ref`) or
   carries a written dismissal. The script run does not pass while one is unresolved.
3. **Source tier.** A row whose only sources are a company press release or a conference abstract is
   flagged NOT_REGULATORY_RECORD and carries a regulatory_record gap.
4. **Subgroup and single-arm.** A subgroup claim needs `prespecified` and `interaction_test`. A
   single-arm or externally controlled result needs `external_control`, `sat_prespecified` (protocol, control data and analysis plan fixed before the trial: FDA draft guidance, EMA reflection paper) and `effect_isolation` (does the endpoint isolate the treatment effect: EMA reflection paper); it carries the flag EXTERNAL_CONTROL_CAUTION (ICH E10: much more extreme evidence is needed; no source gives a number, so no numeric discount is applied) and cannot be marked replicated on its own.
5. **Risk-of-bias consistency.** The overall judgement is the highest concern among the five RoB 2 domains (Table 3); the
   script rejects any other value and warns when "some concerns" sit in multiple domains, because RoB 2 lets a reviewer raise the overall to high then. A RoB 2 row names the result assessed and the effect of interest (assignment or adherence).
6. **Markets.** US and EU only. Another market is a [GAP], never a guess.

## Method anchoring
Name the standard behind each judgement in the row (RoB 2 domain, ICH E9(R1) estimand attribute, single-arm credibility check from the EMA reflection paper or the FDA draft external-control guidance (draft status stated), FDA
surrogate table row). See references/method-standards.md. If no listed standard covers a judgement, say so and mark [CHECK].

## Connectors
- Literature (literature_search_literature, literature_find_trial, literature_grade_evidence,
  literature_check_retraction): locate a named publication; check retraction; CEBM grade is a design
  label, not a risk-of-bias judgement.
- ClinicalTrials.gov (search_trials, get_trial_details): the registered design and prespecified endpoints.
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.
- Navigator (catalogue_get): the competency row and its siblings.

## Quality bar
- 100% of rows: source or [CHECK]; absent fields GAP with consequence.
- 100% of failure modes screened and resolved; script exit 0.
- Estimand attributes stated or GAP; risk-of-bias basis quoted.
- Reviewer name and date on the register before it goes to skill B.
- Upstream: a signed mechanism register from assess-scientific-validity-and-moa recovers any row whose mechanism rationale is a GAP.
- Hand-off: the signed register is also the evidence behind skill G's differentiation claims (rows are cited by id) and a condition in skill H.
- Hand-off: the signed register also feeds evaluate-regulatory-pathway-and-legal-risk, which matches register rows to the criteria of each regulatory route.
