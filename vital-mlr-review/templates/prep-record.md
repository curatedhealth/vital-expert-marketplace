# Prep record (offline JSON shape)

Requires `cleared_by.name` (human). Statuses allowed: `findings_only` · `revise` · `human_gate_required` · `prep_complete` only.

| Field | Value |
|---|---|
| record_id | |
| artefact_version | |
| jurisdictions | |
| ruleset_ids | |
| mlr_status (the packet status: one of the four only) | |
| record state (tool field `record.status`) | `prep_cleared_for_human_mlr` — report as `Record state (not a status, not use-clearance): prep_cleared_for_human_mlr`, never as the status |
| cleared_by.name | **required** |
| cleared_by.role | |
| purpose | |
| mlr_reviewed flag | always false — prep only |
| local_path | `./ready-sessions/<id>.ready.json` when offline |
| mode | READY-local · not metered |

## Explicit non-goals

- Never claim copy is cleared or approved
- Never claim a regulator submission filing (for example Form 2253) was filed or submitted
- Not regulator clearance

Liability: This prepares material for human MLR review. It is not medical, legal, or regulatory approval.
