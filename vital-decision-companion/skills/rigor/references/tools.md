# Tool calls

## Companion slot

`decision_rigor_guide` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_rigor_guide

Arguments: rigor, one of decide_quickly, tradeoff, dig_deep, full_process.

Returns: label, required, skippable, checklist. The content pack version is 2026-10-24.1.

Pitfall: Passing a spoken label such as "Decide quickly" instead of decide_quickly is an unknown rigor error. The id stays in the payload. Speak the label.

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-24.1`.

## Also named

- none

These tools stay on their own connector. This skill does not reimplement them.
