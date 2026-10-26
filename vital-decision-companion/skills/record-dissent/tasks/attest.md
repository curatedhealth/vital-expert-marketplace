# Task DC-4.5.2 Attest no dissent

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (dissent). Does not choose the option and does not sign. |
| Workflow | Ask who attests (one question), store the attestation, stop. |
| Skill | DC-4.6 Record dissent |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_attach_notes`; optional `decision_run_stage` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_attach_notes` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask exactly one question: **Who confirms there is no dissent?** Store nothing until there is a named answer. Silence is not attestation. Do not combine this with a second question in the same turn.
2. With a named person, call `decision_attach_notes` with `stage: make_decision`, `source: owner`, `notes: "No dissent — attested by <name>"`.
3. When merge semantics are available (see capture task), also `decision_run_stage` with `payload: {no_dissent_attested_by: <name>}` and **never** `replace: true`.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
