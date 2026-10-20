# Task TR-5.1.3 Method description

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced colleague with an evidence background |
| Workflow | Extract the study's design facts from the source, then hold the draft to them |
| Skill | TR-5.1.3 |
| Knowledge | `references/rules.md` (R3–R6), `references/patterns.md` (M1–M9) |
| Tool | None. Companion slot: VERIFY `check_claim` via `claim-assessment` |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/repair-note.md`, the study card below |
| Input | The draft and the supplied study material |
| Governance | TR-H1, TR-H3, TR-H7 |

## What counts as a study here

Clinical trials and observational studies, and also the evidence daily users quote most:
market research, physician or patient surveys, advisory board feedback, real-world data
analyses and internal analyses. The same discipline applies: say what kind of evidence it
is, who was in it and how many, what it measured, and do not let it say more than it can.
"8 of 12 advisory board members preferred option A" is not "physicians prefer option A".

## The study card

Before describing a study, fill this card from the supplied material only. Leave a field
as `[GAP: not supplied]` rather than inferring it.

```
Study: <name or identifier as given>
Design: <e.g. randomized, double-blind, placebo-controlled; single-arm; observational cohort; survey; advisory board; internal analysis>
Population: <who was enrolled, key criteria>
Comparator: <placebo, active drug, standard of care, none>
Primary endpoint: <as stated, with timepoint>
Endpoint type: <clinical outcome | surrogate | patient-reported | composite> (as the source labels it)
Key secondary endpoints: <as stated>
Analysis population for the figure used: <ITT, per protocol, safety set, subgroup>
Pre-specified or post hoc: <for any subgroup or exploratory result used>
Follow-up: <duration>
```

## Guard (while drafting)

1. **Fill the study card first.** Describe the study only in terms the card supports.
2. **Name the design as the source names it.** Do not upgrade it: a single-arm study is
   not "controlled", an observational cohort is not a "trial", an open-label extension is
   not the pivotal study.
3. **Keep the population.** A result in a subgroup is stated as a subgroup result, with
   whether it was pre-specified. Never present it as the overall result.
4. **Keep the endpoint.** A primary endpoint result is not a secondary one and vice versa.
   A surrogate (for example a biomarker or response rate) is not stated as a clinical
   outcome (for example survival or events) unless the source shows the clinical result.
5. **Keep the direction of inference.** An association from an observational study is not
   written as a cause. "Not statistically significant" is not "no difference" and not
   "trend toward benefit" unless the source uses those words.

## Repair (existing draft)

1. **Fill the study card** from the material.
2. **Compare each method statement in the draft** to the card and classify: matches;
   upgraded (design, endpoint or population made stronger than the source); conflated
   (two studies, arms or timepoints merged); not in the material.
3. **Fix** to the card's wording, or mark a gap. Upgrades are the priority: they are the
   errors reviewers treat as misleading.

## Check line

See `assets/check-line.md`.

## Boundaries

- Do not appraise the study's risk of bias or strength of evidence here; that is
  `source-assessment`.
- Do not decide whether a surrogate is acceptable for a regulatory or payer purpose. Say
  what the endpoint is; the reviewer decides what it is worth.
