# Task DC-6.1 Record the review plan

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (learning loop). Does not choose the option and does not sign. |
| Workflow | Ask for the missing journal field, call `decision_run_stage`, read the result, ask one question, stop. |
| Skill | DC-6.1 Learning loop |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_run_stage`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_run_stage` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask only for what is missing, one field per turn: the review date in the person's words; the success signal (what observable result would show it worked); the expected outcome; how likely they think it is, as their own percentage; the two or three assumptions that must hold; and the name of the person recording it.
2. Call `decision_run_stage` with `stage: learning_loop` and `payload: {review_date, success_signal, authored_by, expected_outcome, probability, key_assumptions}`. `review_date`, `success_signal`, and `authored_by` are required by the connector. Send the optional fields only when the person gave them.
3. If the result is `refused:` and `authored_by` is a person's name, say the connector rejected the author field and ask the person to confirm the name. Do not retry with another name and do not use the assistant.
4. If the result says required fields missing, name the three required fields back to the person. The v0.1 connector does not name them.
5. Do not invent a KPI, a date, or a probability. A missing value stays `[GAP]`.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
