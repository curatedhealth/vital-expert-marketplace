# Task DC-4.7 Final check before storing

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (choice recorder). Does not choose the option and does not sign. |
| Workflow | Ask the open items of the final check, one per turn, then hand back to the record task. |
| Skill | DC-4.7 Make the decision |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_status` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_status` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_status`. Note which stages are open.
2. Ask only the items not already answered: Is the problem clearly defined? Did we consider at least three options? Was the information sufficient for this level of risk? Did we hear different perspectives, including dissent? Did we check the stored bias card? Would we be comfortable explaining this in public? Are we committed to implementing it? Is there a plan for the first steps? Do we know how we will learn whether it worked?
3. A no is recorded, not argued away. The decider may proceed with the gap named.
4. If dissent has not been invited, point to record-dissent before storing.
5. Return to `tasks/record.md`.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
