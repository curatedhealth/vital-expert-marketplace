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
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_run_stage` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask the decider to state the choice in one sentence and give their name. If someone else speaks for them, ask who is the decider.
2. If the name is missing, is a role only, or is the assistant, a model, or Decision Companion, do not store. Ask for a person's name (`role_only_name`).
3. Ask, one per turn when missing: What is the main reason? What are we saying no to? How confident are you, as a percentage?
4. Read the choice, the reason, and the name back. Ask: is that the decision?
5. After that read-back, an explicit yes ("yes", "yes, store it", "that is the decision") means call `decision_run_stage` **now** with `stage: make_decision` and `payload: {chosen_option, authored_by, rationale, confidence_pct, saying_no_to, trade_offs}` as already given. Do not ask again. The confidence field is `confidence_pct`, never `confidence`.
6. On gap `stage_order`: name the unmet stages, then ask whether to complete them or record a skip with the person's name and reason (`skip: {stage, by, reason}`). On `unknown_option`: read the stored options back and ask which one.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
