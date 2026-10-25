# Task DC-5.2.1 Build the plan

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (implementation). Does not choose the option and does not sign. |
| Workflow | Ask for the missing plan field, store the Implement stage, ask one question, stop. |
| Skill | DC-5.2 Implementation plan |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_run_stage` and `decision_status` |
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

1. Check that a choice is recorded (`decision_status` or `decision_export` when present). If not, say the plan waits for make-decision. Do not treat "implement complete" as progress while no choice is recorded (R13 / connector 0.3.1 behaviour).
2. Ask, one per turn, only what is missing: Who is the single owner? What happens in the next 48 hours (first milestone)? What are the key actions? Who must be told, when, and how (communication plan)? What does the person need first (resources, dependencies)? When will we review progress? What would make us revisit the decision (review trigger)?
3. A review trigger is a condition, not a date: for example a metric crossing a threshold the person names. If they give only a date, ask what condition would bring the review forward.
4. If DAI-I decide is empty, run daii first.
5. Call `decision_run_stage` with `stage: implement` and `payload: {roles: {decide, advise, inform, implement}, owner, first_milestone, key_actions, communication_plan, review_date, review_trigger, if_then_plans: [{signal, owner, action}]}`. Send only what the person gave.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.

Read `optional_missing` warnings (first_milestone, review_date) and ask for them. On `role_only_name`, ask who the person is.
