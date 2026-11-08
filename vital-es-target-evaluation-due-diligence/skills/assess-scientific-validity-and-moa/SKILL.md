---
name: assess-scientific-validity-and-moa
description: "Use when a buyer (pharma business development or life-sciences investor) needs to know how well the science behind a drug asset's target and mechanism of action is supported, before the clinical data are read: the target and mechanism, human genetic or clinical evidence linking the target to the disease, preclinical model evidence and its translatability, independent reproduction, biomarkers of target engagement, class precedent (successes and failures of the same target or mechanism) and differentiation against the class. Produces a mechanism register and the questions for the named scientist. Never states a scientific go/no-go (human only). Feeds review-clinical-data-quality and estimate-development-risk-and-timeline. Not for the clinical data themselves, not for deal value, not for markets other than US and EU."
metadata:
  level: CF04
  register_code: CF-01.02.06.1.1
  register_id: 1887c82d-a30f-4b8e-859c-f656e5669061
  version: 0.1.0
  verb: assess
  capability: CF-01.02.06 Target Evaluation & Due Diligence
  mission: CF-01.02.06.1 Scientific & Clinical Due Diligence
  agent: bd-due-diligence-lead
  atoms: [extract-requirements-from-source, compare-against-criteria, classify-text-labels, compose-draft]
  requires: []
  feeds: [review-clinical-data-quality, estimate-development-risk-and-timeline, evaluate-market-opportunity-and-competitive-position, determine-commercial-viability]
  tools: [scripts/mechanism_check.py, scripts/validate_register.py]
  tier: "Full (owner ruling 7 November 2026): the Full proof is the chain F -> A -> B; back-test set designed, not frozen"
  release_state: Draft (Q1-Q6 built; Q7 back-test pending; Q8 practitioner review pending)
---

# Assess scientific validity and MOA

## What competent output looks like
- A mechanism register for one asset (company unit: one per pipeline asset, then a side-by-side roll-up) with
  seven sections, each sourced or a named gap:
  1. target and mechanism, as the seller states them (the claim, with its source);
  2. human genetic or clinical evidence linking the target to the disease, graded by the best sourced human evidence supplied;
  3. preclinical model evidence and its translatability (species, model, what the model does and does not represent), with the ARRIVE 2.0 Essential 10 items reported, not reported or not assessable for each animal study;
  4. independent reproduction: a finding counts as independently reproduced only if a different organization repeated it and collected its own data (a replicability definition from the National Academies; the different-organization requirement is the plugin's own rule);
  5. biomarkers, and whether target engagement was shown with a pharmacodynamic biomarker in humans;
  6. class precedent: successes and failures of the same target or mechanism, including class-wide safety warnings;
  7. differentiation against the class, each claim with its basis and source.
- The register states what the evidence chain is and where it is thin. It never states that the target or
  mechanism is validated, proven or de-risked, and never recommends going ahead or stopping. The scientific
  go/no-go judgment is human only.
- No probability is computed. Published population-level findings (for example about genetic support) are
  context, not a probability for this asset.
- Absent evidence is a GAP with the consequence stated. Never "unknown".
- The register feeds `review-clinical-data-quality` (a register row whose mechanism rationale is a GAP can be
  recovered by this skill) and `estimate-development-risk-and-timeline` (the class and evidence-chain flags are inputs a person weighs).

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake (intake.md): buyer mode, unit, documents, the named scientist | none | agent asks; human supplies |
| 2 | Target and mechanism as claimed (task 01) | extract-requirements-from-source | agent drafts; human reviews |
| 3 | Human genetic and clinical evidence (task 02) | extract-requirements-from-source; classify-text-labels (human_genetic, clinical_pharmacology, other) | agent drafts; scientist reviews |
| 4 | Preclinical evidence, translatability and ARRIVE items (task 03) | extract-requirements-from-source; scripts/mechanism_check.py | agent drafts; scientist reviews |
| 5 | Independent reproduction and biomarkers (task 04) | scripts/mechanism_check.py | agent alone (script); human confirms the inputs |
| 6 | Class precedent and differentiation (task 05) | extract-requirements-from-source; compare-against-criteria | agent drafts; scientist reviews |
| 7 | Screen failure modes and write the questions (task 06) | compare-against-criteria (triggered / not triggered / cannot tell) | agent drafts; human reviews every "triggered" |
| 8 | Validate and write the register (task 07) | scripts/validate_register.py; compose-draft with templates/mechanism-register.md | agent alone (script) |
| 9 | Whether the evidence chain is strong enough to proceed (the scientific go/no-go); sign-off of the register | none | human only |

## Rules (general, apply to every case)
1. **No go/no-go.** `validate_register.py` rejects text that says a target or mechanism is validated, proven
   or de-risked, or that recommends proceeding or stopping. Write the question for the scientist instead.
2. **Independence is by organization.** A reproduction by the originating group is recorded as "reproduced by
   the originator only", never as independent. The script rejects a reproduction marked independent that the
   originator performed.
3. **Animal studies are graded on reporting, not on results.** The ARRIVE items show what is reported; they do
   not say the result is true. A missing item is "not reported"; an item that cannot be judged from the
   source is "not assessable" (a GAP).
4. **Human evidence is graded by what is sourced.** An unsourced statement of genetic support does not count.
5. **Class failures are named.** A failed or withdrawn class member, and any class-wide safety warning, must
   be addressed by a sourced differentiation; if none is supplied the script flags it.
6. **Rule status.** Only VERIFIED-REOPENED rules compute; contested or unverified findings are disabled and
   print [CHECK] (references/rules/mechanism-rules.json).
7. **Markets.** US and EU only for any regulatory precedent; another market is a [GAP].
8. **Sources of conflict.** Industry-affiliated authors and funders of a cited analysis are named in the reference.

## Method anchoring
Name the source id from references/method-standards.md beside every judgement. No published standard exists
for judging the scientific validity of a mechanism as a whole; the skill does not name one. It anchors on the
reporting checklist for animal research (ARRIVE 2.0), the biomarker definitions of the FDA-NIH BEST glossary,
published analyses of reproducibility and translation, the GOT-IT target-assessment structure (written for academic use), and a replicability definition from the National Academies, and the sourced failure modes in references/failure-modes.md.

## Connectors
- Literature (literature_search_literature, literature_grade_evidence): locate and grade named publications; Open Targets and ChEMBL where connected, for target-disease association and mechanism records (a lead for a person to check, not evidence on its own).
- ClinicalTrials.gov and regulator pages: class precedent and class warnings (read by a person or a read-only page reader).
- VITAL Verify (qualify_source, check_claim, build_citation): admit a source and check a claim against a quoted passage.
- Navigator (catalogue_get): the competency row and its siblings.

## Quality bar
- 100% of evidence rows: source or [CHECK]; absent sections are named GAPs with consequence.
- mechanism_check exit 0; validate_register exit 0; disabled rules listed.
- All five failure modes (FM-01 to FM-05) screened and resolved.
- At least one question for the named scientist; scientific_go_no_go shows HUMAN ONLY; status UNSIGNED until a named reviewer signs.
- Open [CHECK] and [GAP] items, decisions (with decider) and the hand-off (review-clinical-data-quality; the market and viability skills cite its rows and read its class flags) listed at the end.
