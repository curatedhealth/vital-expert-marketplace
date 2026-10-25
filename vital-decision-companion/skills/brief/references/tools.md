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

- `decision_status` (enrich omitted fields)

These tools stay on their own connector. This skill does not reimplement them.

## Connector version

| Condition | What to do |
|---|---|
| Brief prints `None`, `null`, or `{}` | Show "not given yet" to the person (keep `[GAP]` only as the stored marker), or fill from `decision_export` / `decision_status`, and say you did so. |
| watermark SIMULATED | Keep it on every page; say practice. |
| Stored field omitted from brief | Pull from `decision_status` and note the enrichment. |
| Do not | Reintroduce compensations for raw JSON as if they were still the default. |
