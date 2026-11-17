# Tools and companion slot

## Companion slot

No companion exists for this skill. VERIFY tests sentences against supplied passages;
it does not judge certainty, framing or charts, and this skill does not hand off to it.

| Task | What a companion would do | Tool | Without it |
|---|---|---|---|
| Uncertainty at its real size | Read the supplied paper's results table and limitations section and return, per result, the estimate, interval, n, follow-up and whether it was primary, so the result card is filled from the source rather than from the assistant's reading | No companion yet | Method runs; the result card is filled by reading the material; check line says "not tool-checked" |
| Numbers and charts | Read a chart image or file and return the axis start and end, scale per panel, series plotted and the values behind each mark, then compute the distortion | No companion yet | Method and `scripts/chart_scale.py` run on what the person supplies or describes; where the chart's values or axis are not supplied, `[GAP: not checkable here — whether the chart matches its data — supply the data or the chart file]` |
| Conflict disclosure | Read the source's funding and disclosure sections and return the sponsor, its stated role and author ties, quoted | No companion yet. Related: `source-assessment` records what a source discloses, with VERIFY `qualify_source` when connected | Method runs from the supplied material; "not tool-checked" |

Never describe any of the above as having run (TR-H4).

# Offline check (deterministic, no program)

This skill ships **data + instructions** instead of Python. Apply the rules in
`check-rules.json` exactly as written below. Hits are prompts to read, not findings,
unless the skill's method says otherwise.

**Source of truth for lists/patterns/formulas:** `references/check-rules.json`  
**Do not** invent extra cue words. **Do not** run shell or package managers.


## Checks in this skill

### `chart_scale`

How much a chart's construction enlarges or shrinks a difference.

Data: `check-rules.json` → `checks.chart_scale.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.



### `find_framing_cues`

List framing words in a draft for a person to review.

Data: `check-rules.json` → `checks.find_framing_cues.data`.

## Procedure

1. Load the lists/patterns for this check from check-rules.json.
2. Scan the draft (and source material if the check requires it) line by line or sentence by sentence.
3. Record every match with location (line or sentence).
4. Apply any pairing/window/threshold fields in the data object exactly.
5. Report matches as prompts to read; do not invent extra categories.

### `chart_scale` — procedure steps

1. Bars: lengths = value − axis_min (both must be >0). actual_ratio=b/a; displayed_ratio=lb/la; looks_larger_by = displayed_change/actual_change when actual_change≠0.
2. Optional axis_max: difference_share_of_plotted_range_pct = |b−a|/(axis_max−axis_min)×100.
3. Icons: height → scale with ratio; both → area scales with ratio².
4. Cumulative series: convert to per-period increments.
5. Derived from supplied values only; measures the drawing, not meaning.

