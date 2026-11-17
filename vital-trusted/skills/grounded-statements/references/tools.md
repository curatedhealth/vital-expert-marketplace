# Tools and companion slot

## Companion slot

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| No fabrication | Test each claim against the quoted passage it rests on | VERIFY `check_claim`, `verify_text`, through `claim-assessment` | Method runs; check line says "not tool-checked" |
| Number consistency | Test that each figure appears in its passage | VERIFY `check_claim`, through `claim-assessment` | Method and scripts run; "not tool-checked" |
| Method description | Test that design and endpoint statements match the passage | VERIFY `check_claim`, through `claim-assessment` | Method runs; "not tool-checked" |

This skill never calls VERIFY directly. It hands finished text to `claim-assessment`,
which owns the tool calls and their interpretation. That keeps the tool contract in one
place. [CHECK: VERIFY argument and return contracts to be confirmed in claim-assessment.]

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `extract_numbers`

List every number in a text with its context, for matching against the source.

Data: `check-rules.json` → `checks.extract_numbers.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.



### `risk_metrics`

Absolute and relative effects for a binary outcome, from supplied arm values.

Data: `check-rules.json` → `checks.risk_metrics.data`.

## Procedure: risk metrics (binary outcome)

Inputs: treatment and control each as either (events, n) or a rate in 0..1 — not both forms for one arm.

1. treatment_risk = events_t/n_t or rate_t; same for control.
2. risk_difference = treatment_risk − control_risk (as proportion).
3. If control_risk > 0: relative_risk = treatment/control; relative_change_pct = (rr − 1) × 100.
4. If risk_difference ≠ 0: NNT/NNH = ceil(1 / |risk_difference|); direction = lower risk with treatment (NNT) if rd < 0 else higher (NNH).
5. Optional draft checks (tolerances): rr ±0.01; rrr ±0.5 (stated rrr compared to **−**relative_change_pct); arr ±0.05 (stated arr compared to **−**risk_difference in percentage points); nnt ±0.5 vs rounded_up.
6. Label every figure `derived from supplied values`. Nothing is looked up.

### `extract_numbers` — procedure steps

1. For each line, find all number_regex matches.
2. Classify kind from unit (pp/percentage points; %/percent; patients→count; other unit→quantity; bare decimal <10→ratio-like or decimal; else number).
3. Emit line, number as written, kind, surrounding text.
4. Also list units that appear with more than one distinct value.
5. Do not judge correctness.

