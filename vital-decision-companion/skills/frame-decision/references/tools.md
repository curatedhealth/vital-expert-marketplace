# Tool calls

## Companion slot

`decision_run_stage` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_run_stage (how_to_decide)

Arguments: session_id, stage how_to_decide. Required for complete: payload.statement, payload.goal, payload.decider, payload.deadline. Optional: core_issue, consequence, reversibility, authority_mode, criteria, values, assumptions, decision_type, type_confirmed_by, people_decision.

Rigor: send `rigor` (decide_quickly | tradeoff | dig_deep | full_process) only on the first set. If the session already has a rigor, send `change_rigor: {to, by, reason}` with `by` as the person's name. Read back warning `rigor_unchanged` when it appears.

Returns: complete true when statement, goal, decider, and deadline are present. Gaps name missing fields when the connector supports it. Warning `people_decision` when that flag is set — read the warning text exactly.

Pitfall: Sending rigor again without change_rigor leaves the session rigor unchanged (warning `rigor_unchanged`).

A call the skill must refuse returns `gaps` whose text starts with `refused:`. The rejected field is not stored.

Schema source: `mcps/decision_companion/tools.py`, content pack `2026-10-26.1`.

## Also named

- `decision_classify`
- `decision_rigor_guide`

These tools stay on their own connector. This skill does not reimplement them.

## Connector version

| Condition | What to do |
|---|---|
| Session rigor unset | Send `rigor` once with the person's confirmed level. |
| Session already has rigor | Send `change_rigor {to, by: <person>, reason}`. Never re-send bare `rigor` expecting a change. |
| Warning `rigor_unchanged` | Say the rigor did not change and ask whether to send change_rigor. |
| Person says it is a people decision | Send `people_decision: true` first. Do not paraphrase the notice before the tool returns. Read the connector `people_decision` warning verbatim when it returns; if absent (v0.2), use rules R7 and say it is the skill's notice. |
| Gap `role_only_name` on decider | Ask who the person is. Do not store a role title alone. |
