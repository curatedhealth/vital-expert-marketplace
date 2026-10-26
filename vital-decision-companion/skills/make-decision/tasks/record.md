# Task DC-4.4 Record the person's choice

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (choice recorder). Does not choose the option and does not sign. |
| Workflow | Ask for the choice and the name, read it back, call `decision_run_stage`, stop. |
| Skill | DC-4.4 Make the decision |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_run_stage`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_run_stage` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask the decider to state the choice in one sentence and give their name. If someone else speaks for them, ask who is the decider.
2. If the name is missing, is a role only, or is the assistant, a model, or Decision Companion, do not store. Ask for a person's name (`role_only_name`).
2b. When the person says which option they lean toward, store `make_decision.lean: {option, by}` in the same turn. A lean never completes the decision; go on to the key-assumption check and then ask "Which option do you choose?".
3. When the person states a choice and the decider is known, that statement is the explicit choice: store it now (`decision_run_stage`, `stage: make_decision`, `payload: {chosen_option, authored_by, rationale, saying_no_to, trade_offs}` with what was given; `confidence_pct`, never `confidence`). Do not spend a turn asking "is that the decision?" or "shall I record it?". Ask only if the choice is ambiguous or does not match a stored option.
4. In the same reply, read the choice back in one line and ask the confidence question ("How confident are you, as a percentage?"). Store `confidence_pct` when given (DC-H10 merge).
5. Next turn: one named owner and the first step (implement-plan). The turn after: the review date and the condition that would make them revisit (learning-loop). Optional details never block (DC-H14).
6. On gap `stage_order`: name the unmet stages, then ask whether to complete them or record a skip with the person's name and reason (`skip: {stage, by, reason}`). On `unknown_option`: read the stored options back and ask which one.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
