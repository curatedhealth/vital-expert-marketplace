# Task DC-1.2 Confirm the type

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (classifier). Does not choose the option and does not sign. |
| Workflow | Read the draft back, wait for a named person to confirm, store the confirmed type, stop. |
| Skill | DC-1.2 Classify |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_classify`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_classify` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Read the draft type and rigor back in one sentence. Ask the person to confirm or correct it, and for their name.
2. If the name is missing, do not store. Ask for the name.
3. Call `decision_classify` with `statement`, `session_id`, `confirmed: true`, and `confirmed_by` set to that name.
4. If the host does not expose `confirmed` and `confirmed_by` (the published v0.1 schema shows only statement and session_id), store the confirmed rigor through `decision_run_stage` on `how_to_decide` instead (see frame-decision), and say that the type itself stays a draft on the connector.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
