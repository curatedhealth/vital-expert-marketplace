# Tool calls

## Companion slot

`decision_attach_notes` is available when Decision Companion is connected with a `vdec_` key. Without it, run the task by hand and label the turn not tool-checked (DC-H4).

## decision_status (first)

Arguments: session_id, `include_schemas: true`.

Use the returned `stage_schemas.make_decision.optional`: if it contains `no_dissent_attested_by`, merge semantics are present (v0.3).

## decision_attach_notes

Arguments: session_id, stage make_decision, notes (dissent or no-dissent template), source (`participant` | `owner`).

This path always works. Always keep the participant/owner note.

## decision_run_stage (make_decision) — merge path only

Optional: `dissent: [{holder, text}]` or `no_dissent_attested_by`. Never send `replace: true`.

## Connector version

| Condition | What to do |
|---|---|
| First | `decision_status {include_schemas: true}`. |
| `no_dissent_attested_by` in make_decision.optional | Merge path: notes + dissent[] / no_dissent_attested_by without replace. |
| Field absent (v0.2) | Notes only. Do not call make_decision for dissent. |
| Always | Never `replace: true`. |
