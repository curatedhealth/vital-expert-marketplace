# Task DC-4.8 By-hand bias prompts by stage

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (bias card). Does not choose the option and does not sign. |
| Workflow | Name the current stage, read one prompt from the stage list in rules, ask the person, stop. |
| Skill | DC-4.8 Bias |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | By hand; `decision_attach_notes` to keep the answer |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_bias_check` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Name the current stage from `decision_status` or the conversation.
2. Pick one bias from the stage list in `references/rules.md` R8 that fits what the person just said.
3. Ask its question. These prompts are by-hand content from the Playbook, not tool output; say so.
4. Record the person's answer with `decision_attach_notes` (source participant) if they want it kept.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
