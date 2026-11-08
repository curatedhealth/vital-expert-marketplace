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

## Lane A gaps (7 November 2026)

- `is_decoy` / sham options → refuse (LA-SDG-ALT).
- Excluded baseline without exclusion_reason → `[GAP]`.

## C3 refusals — compare-options (OPT; 7 November 2026)

Refuse and state why; do not silently comply.

| Refusal | Trigger | Response shape |
|---|---|---|
| AI weights/scores | Assistant asked to invent weights, scores or ordinals | Refuse; request named human raters and human-entered cells |
| ODI dollars | Opportunity index multiplied into MCDA money | Refuse; keep opportunity units separate from preference model |
| NICE defaults | NICE QALY/discount/HTA parameters as mandatory enterprise MCDA | Refuse; cite LA-C3-007 boundary; use owner criteria only |
| False EVIDEM fidelity | Claim 0–4 API = exact 2008 EVIDEM implementation | Refuse misattribution; label VITAL adaptation; cite LA-C3-010 scales |
| False swing label | Direct importance ratings called swing weights | Refuse; name method (WR-C3-020); swing needs defined performance range |
| Silent scale conversion | Rescale 0–4, 0–3 and 1–10 without declared adapter | Refuse; pin edition and path (offline 1–10 vs live 0–4) |
| Missing anchors | Team disagrees low/high; numeric scores invented anyway | Refuse numeric fill; retain qualitative criterion rows (WR-C3-021) |

## Rule-ID SSOT (8 November 2026)

The rule ids that scripts raise and the offline validator tests are the `V-C3-*` ids in `scripts/offline_c_validator/rule_register.csv` (behavior in `vital_validate.py`; live-schema mapping in `live_adapters.py`). Where this file or a known-answer case disagrees on an id, the register wins. The `GP-*` labels in this file are descriptive gap patterns, not rule ids.

| V-C3 id | Rule | Script content check (`options_check.py`) |
|---|---|---|
| V-C3-OPT-01 | Human provenance for weights and scores | `ai_filled_weights` and kin refused |
| V-C3-OPT-02 | Criteria set: unique id and name, weights normalized to 1, declared weight convention, no "complete" with omitted criteria | content: ids, names, sum of weights, `weight_convention` enum, `claims_complete_mcda` + `omitted_criteria` |
| V-C3-OPT-03 | Overlap and double counting reviewed | content: near-duplicate names, `overlaps_with`, `double_counting_risk` need `overlap_review_ref` |
| V-C3-OPT-04 | No ODI dollars | `odi_to_money` refused |
| V-C3-OPT-05 | HTA/NICE defaults not enterprise defaults | `hta_defaults`, `nice_as_enterprise_mcda` refused |
| V-C3-OPT-06 | Option set: unique ids and labels, no decoys, reference lines recognizable, unranked rows carry a reason | content: duplicate id or label, decoy wording, `unranked` without `unranked_reason`, odd baseline without `baseline_rationale` |
| V-C3-OPT-07 | EVIDEM 2008 claim only with 0-3 score and 1-5 weight scales or a documented adaptation | `claims_evidem_2008_exact` |
| V-C3-OPT-08 | Swing weights need defined anchors | `weights_labeled_swing` |
| V-C3-OPT-09 | Numeric scores need agreed low/high anchors | `infer_scores_without_anchors`, `ai_inferred_scores` |

Before 8 November 2026 the script raised OPT-07 for missing anchors and OPT-09 for the EVIDEM claim; the two ids are now swapped to match the register. A `schema_version=vital-c-validator/0.1` envelope with `cluster=C3` and `stage=compare_options` is validated by the shared validator and returned as a summary (the script no longer falls through to the live schema).
