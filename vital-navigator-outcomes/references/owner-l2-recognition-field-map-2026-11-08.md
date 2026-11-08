# Owner L2 recognition — inspected field map (8 November 2026)

**Status:** Documentation of **existing** canon in `track-value-realized` / `review-the-portfolio` methods + native `realization_check.py`.  
**Not** a new owner ruling. **Not** Lane B Pass. Does **not** invent statuses absent from those surfaces.

Primary citations (in-plugin):

- `skills/track-value-realized/references/method.md` — GOV-02 R-MEASURE; OWNER rulings 1–4 (realization) / 5–9 (review adjacency)
- `skills/track-value-realized/scripts/realization_check.py` — runtime recognition split (WR-C5-025)

## Owner rulings (numbered as in method.md)

| Id | Locked rule (inspected prose) | Runtime implication |
|---|---|---|
| **L1 / ruling 1** | Value counts only for outcomes **measured as achieved**; unmet evaluation → **zero** recognized value, never partial | `counted_realized_value = 0` when any outcome `status == "not achieved"` and none remain unevaluated |
| **L2 / ruling 2** | Realized figure needs **source + date** (class M); estimate/forecast/impression ≠ realized | `realized.measured` + non-empty `realized.source` required before count |
| **L3 / ruling 3** | Placement (below/inside/above) **describes**; owner decides meaning | Script returns `place_against_range`; never auto-Proceed |
| **L4 / ruling 4** | Other influences are **owner-stated**; contribution ≠ causal proof | `other_changes` optional list; AI invent-confounders refused (`V-C5-ATTR-02`) |
| **L5 / ruling 5** | Walk must reach an outcome; stop/keep/fix traces or “none” | Review skill / `review_check` (not realization count) |
| **L6–L7 / rulings 6–7** | Learning order; named steward; no raw-KPI model mutation; readiness factors owner-named | `review_check` refuses AI disposition / lead→credit |
| **L8–L9 / rulings 8–9** | Scale only on keep + achieved outcome; re-score needs steward | Review/scale paths; not partial recognition formulas |

## Outcome evaluation → recognition (runtime)

Input fields inspected in `realization_check.evaluate`:

| Input | Meaning | Derived `outcomes[].status` |
|---|---|---|
| `evaluation_status` ∈ `met` / `achieved` | Explicit pass — **only with a sourced `result`**, else `not measured` + V-C5-REAL-07 | `achieved` |
| `evaluation_status` ∈ `unmet` / `not achieved` / `not_achieved` | Explicit fail | `not achieved` |
| `evaluation_status` ∈ `not_yet_evaluated` / `missing` / `not_due` / `not due` | Not evaluated | `not measured` |
| else: numeric `result`+`target`+`direction` with `source` | Computed vs target | `achieved` or `not achieved` |
| else: missing result or empty source | Cannot measure | `not measured` |

Recognition outputs:

| Output field | Role |
|---|---|
| `measured_figure` | Raw observed realized figure (`realized.value`) — **always preserved** when supplied |
| `counted_realized_value` | Recognized value: figure if all achieved + measured (source + `source_date`) + unit **and period** match the range; **`0`** if unmet (L2); **`null`** if not-yet-evaluated / incomplete |
| `place_against_range` | Descriptive placement or not-counted reason string |
| `problems[]` | Hard refuses / gaps (invented $, ODI→money, cash without `realization_action`, etc.) |

### Hard locks (do not reopen without owner)

1. Unmet → recognized **zero**; **no** partial-credit formula.  
2. Missing / not-yet-evaluated → **deferred** count — **must not** rewrite observation as measured zero.  
3. Cashable claims require `realization_action` (existing cash bridge).  
4. ODI / satisfaction scores are not money baselines or realized cash.

## HITL residual

Owner may countersign this map or supply additional status synonyms. Until then, only the statuses and fields above are enforced. Further synonyms without an owner protocol remain **[GAP]** (refuse silent mapping).

## Related gaps

| Id | Relation |
|---|---|
| WR-C5-025 | Documentation + runtime split: **engineering closed**; independent countersign optional |
| WR-C5-026 | Lane B / full facilitation grade of KA-ON-C5 — still open |
| WR-C5-019 | External “extent of realization” schemes do not override L2 |
