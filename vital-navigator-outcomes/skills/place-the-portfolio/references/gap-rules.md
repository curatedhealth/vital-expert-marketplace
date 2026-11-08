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

## C3 refusals — placement (PLC; 7 November 2026)

| Refusal | Trigger | Response shape |
|---|---|---|
| GP-PLC-01 Invented coordinates | Assistant infers x/y for polish | Refuse; unplaced row; human entry |
| GP-PLC-02 Invented bubbles | Unsupported bubble sizes or probabilities | Refuse; equal markers or documented metric |
| GP-PLC-03 Quadrant approval | "Upper-right = approve / Proceed" | Refuse; OWNER close only; display aid |
| GP-PLC-04 Undocumented API fields | Generic x/y/bubble on `portfolio_place` without schema | Refuse; use declared candidate shape + offline metadata |
| GP-PLC-05 Guaranteed uplift | Blau 2004 28% case as promised return | Refuse; modelled case only (LA-C3-014) |
| GP-PLC-06 Universal pharma cutoffs | Default axes/thresholds without evidence | Refuse; WR-C3-018 open calibration |

## Rule-ID SSOT (8 November 2026)

The rule ids that scripts raise and the offline validator tests are the `V-C3-*` ids in `scripts/offline_c_validator/rule_register.csv` (behavior in `vital_validate.py`; live-schema mapping in `live_adapters.py`). Where this file or a known-answer case disagrees on an id, the register wins. The `GP-*` labels in this file are descriptive gap patterns, not rule ids.

| V-C3 id | Rule | Script content check (`placement_check.py`) | Gap pattern(s) |
|---|---|---|---|
| V-C3-PLC-01 | Unplaced rows carry no coordinates; coordinates come from named people | unplaced row with x, y, outcome fit or oversight; unplaced without a gap; AI or inferred coordinate source | GP-PLC-01 |
| V-C3-PLC-02 | Axes declared: definition, units, source, finite increasing bounds; coordinates inside bounds; adapted grid not labeled original | custom `axes` object validated; per-row bounds; `claims_original_grid` with adapted axes | GP-PLC-04, GP-PLC-06 |
| V-C3-PLC-03 | Placement never selects | `quadrant_approves`, `auto_select_from_bucket`, row-level `selected`/`approved`/`funded`/`decision`, selection wording | GP-PLC-03 |
| V-C3-PLC-04 | Bubble metric documented: metric, units, source, area mapping, one metric per exhibit | bubble fields; consistent metric, units and mapping across options | GP-PLC-02 |
| V-C3-PLC-05 | Capacity dependencies referenced; no uplift guarantee | `capacity_dependencies_ref` required; `guaranteed_uplift_pct`, `blau_28_percent_claim`, uplift wording | GP-PLC-05 |

`D-C3-PLC-ENGINE-XY` (documented, live schema still undocumented): the live `portfolio_place` x/y/bubble schema is not documented, so `submit_xy_to_portfolio_place` is refused unless `xy_adapter_verified` is true (V-C3-PLC-02). Setting that flag is a person's declaration; the script cannot verify it. When it is set, the soft gate additionally requires a non-empty `xy_adapter_ref` (adapter name and version) and a finite numeric `x` and `y` on every placed option, and a finite `bubble.value` where a bubble is given (bubble metric, units and source stay under V-C3-PLC-04). Unplaced options are skipped. The gate checks the shape of what would be sent; it does not describe, confirm or call the live schema, and no live write was tested.
