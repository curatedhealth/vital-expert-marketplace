# Tool calls

## Companion slot

`decision_build_brief` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_build_brief

Arguments: session_id.

Returns: brief_markdown, brief_structured, watermark null or SIMULATED.

Pitfall: Filling [GAP] from earlier chat messages that were never stored writes a brief the session does not hold.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-26.1`.

## Also named

- `decision_export` (0.3.2+: canonical stored record; preferred fill-in)
- `decision_status` (0.3.1 fallback when export is absent)

These tools stay on their own connector. This skill does not reimplement them.

## Connector version

| Condition | What to do |
|---|---|
| Refusal / gap / warning with `message_for_person` (0.3.2+) | Say that sentence (light adapt OK). Never print the code. |
| Same item without `message_for_person` (0.3.1) | Translate the code with the DC-H8 list. Never print the code. |
| Brief prints `None`, `null`, or `{}` | Show "not given yet" to the person (keep `[GAP]` only as the stored marker), or fill from `decision_export` / `decision_status` and say you did so. |
| watermark SIMULATED | Keep it on every page; say practice. |
| Stored field omitted from brief (e.g. second rater, note dissent on 0.3.1) | Fill from `decision_export` when present (0.3.2+), else `decision_status` (0.3.1). Say in plain words that you filled it from the stored record. |
| Do not | Reintroduce compensations for raw JSON as if they were still the default. |
