# Status vocabulary (board-facing)

The packet status is a closed list of four values. Every user-facing result carries one line `Status: <value>` with exactly one of them.

| Status | Meaning for the committee |
|---|---|
| `findings_only` | Packet incomplete or blocked by validation errors, with no approval / bypass pressure (precedence order: `../../../references/finding-status-map.md`) |
| `revise` | Chairs ask for changes before/during board |
| `human_gate_required` | A request to approve or clear, or to bypass any hard rule MLR-H1–H8, including an AI owner request (precedence rule 1), or an open finding a human must judge — disagreement, `reject` / `abstain`, an unaccepted residual |
| `prep_complete` | Structurally valid for human review; every residual listed with the named human who accepted it (rule: `SKILL.md` § When `prep_complete` may be stated) |

## Record state (not a status)

The prep record built by `mlr_build_prep_record` carries a record state, reported on its own line and never on the `Status:` line:

`Record state (not a status, not use-clearance): prep_cleared_for_human_mlr`

It means a named human owns the prep record and the packet is ready for the company MLR process. It is **not** approved for use. The tool field `record.status` keeps this value for app compatibility.

## Output lines (copy exactly)

```
Status: <findings_only | revise | human_gate_required | prep_complete>
Record state (not a status, not use-clearance): prep_cleared_for_human_mlr   ← only when a prep record exists
```

Forbidden in any output: `approved for use`, `mlr approved`, `mlr_reviewed: true`, “cleared for promotion.”
