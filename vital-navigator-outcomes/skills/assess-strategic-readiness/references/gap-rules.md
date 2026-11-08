# Gap rules

A gap is a fact the decision needs that nobody has supplied or no source states. Write `[GAP]` with the reason and what would close it. Never fill a gap from general knowledge; never let a gap become an assumption silently.

| Kind | Example | How to word it |
|---|---|---|
| No attested priorities | Outcomes not scored or Gate 2 not taken | "[GAP] Outcome priorities not attested; capability weights are provisional." |
| Capability serves no outcome | A capability linked to no scored outcome | "Serves no scored outcome: flag for restating or retirement." |
| No baseline | Shortlist without doing nothing and doing it internally | "[GAP] Reference lines missing: add doing nothing and doing it internally." |
| Not scored | A scorer did not return the sheet | "[GAP] Not scored by [name]; no score was filled in." |
| No capacity score | Nobody scored the oversight the organization can carry | "[GAP] Oversight capacity not scored; placement cannot be computed." |
| No context of use | AI option at a critical point without a context-of-use statement | "[GAP] No context-of-use statement; AI cannot be assigned at this point yet." |
| Missing instrument | Data readiness, change capacity, risk appetite | "[GAP] No instrument for [name] yet; owner view recorded as O if given." |
| Play tag missing | Option not tagged augmentation or automation | "Not tagged" in the lens; not a blocker. |
| Not readable | Library capability links at levels 1 or 2 | "[GAP] The library's links are readable only at mission level." |

Who said it: a fact the decision owner states is O. A fact another named person states is O with their name ("stated by Head of Sales Ops"). A view passed on from someone absent is "relayed by [name]", never the absent person's O. When no owner is named, write "stated by the person".

Rules:

- A missing library row is never evidence that a capability or option does not matter.
- In the full report list every gap, most blocking first; merge gaps that close the same way. In a direct answer, at most three.

## C3 refusals — readiness (REA; 7 November 2026)

| Refusal | Trigger | Response shape |
|---|---|---|
| GP-REA-01 AI maturity % | Website scan → "validated GenAI maturity percentage" | Refuse; human ordinals + named rubric |
| GP-REA-02 MLR waiver | High readiness claimed to waive MLR/regulatory block | Refuse; eligibility independent; sibling authority |
| GP-REA-03 Success probability | Readiness score → implementation odds | Refuse; WR-C3-023; heterogeneous evidence |
| GP-REA-04 False validation | Adapted checklist called validated pharma instrument | Refuse; label VITAL synthesis or pinned instrument version |
| GP-REA-05 AI ordinals | Assistant-filled readiness cells | Refuse; named respondents only |
| GP-REA-06 Universal composite | Single maturity index for all investments | Refuse; construct-specific selection or qualitative default |

## Rule-ID SSOT (8 November 2026)

The rule ids that scripts raise and the offline validator tests are the `V-C3-*` ids in `scripts/offline_c_validator/rule_register.csv` (behavior in `vital_validate.py`; live-schema mapping in `live_adapters.py`). Where this file or a known-answer case disagrees on an id, the register wins. The `GP-*` labels in this file are descriptive gap patterns, not rule ids.

| V-C3 id | Rule | Script content check (`readiness_check.py`, `maturity_check.py`) | Gap pattern(s) |
|---|---|---|---|
| V-C3-REA-01 | Evidence factors are human ordinals against a named rubric | maturity percent or AI score refused; percentage wording; AI provenance on a score or rater; ordinal without `rubric_ref` | GP-REA-01, GP-REA-05 |
| V-C3-REA-02 | Constraints are never waived | `waive_mlr`, `waive_mandatory_constraints`, waiver wording, `waived` rows, "met" without `evidence_ref` | GP-REA-02 |
| V-C3-REA-03 | Readiness is for a specific change in a specific unit, with at least two respondents behind a group claim | `specific_change` and `unit` required with a checklist or when either is given (generic change refused); `respondent_count` below 2 refused; `claims_group_readiness` needs two scorers; otherwise `scope_gaps` and `single_respondent` are reported | none |
| V-C3-REA-04 | No universal percentage, no predictive probability, no inherited validation | `success_probability_from_readiness`, predictive wording, "validated" label without a record, `adapted_instrument` + `validated_claim` | GP-REA-03, GP-REA-04, GP-REA-06 |

Maturity instruments (`maturity_check.py`): see `references/maturity-instruments.md`. The same REA ids apply: specific change and unit, rubric reference, no AI rater, two raters for a group claim, no validation by label.
