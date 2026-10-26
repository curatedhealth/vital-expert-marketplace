# Task DC-5.0 Assign the four roles

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (roles). Does not choose the option and does not sign. |
| Workflow | Ask for the names, check them, call `decision_daii_plan`, ask one question, stop. |
| Skill | DC-5.0 DAI-I |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_daii_plan`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_daii_plan` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask, one per turn: Who makes the final call (Decide)? Whose input is needed (Advise)? Who must be told the outcome (Inform)? Who carries it out (Implement)?
2. Decide is one named person. Refuse the assistant, a model, a tool, or Decision Companion in any role, and refuse a role title alone (the committee, the team, leadership). Ask for the name.
3. Call `decision_daii_plan` with `roles: {decide, advise, inform, implement}` holding only the **names given as strings**. An unnamed role stays empty; say so. Do not send `{name, status}` objects.
4. Read the response: advise / inform / implement entries may be strings or `{name, status}`. On `role_only_name`, ask for the person. If a returned entry has `status: "unverified_person"`, print `"<name> (unverified, role not person)"` and put it under Gaps.
5. Ask the planning questions the Playbook attaches to DAI-I, one per turn, when relevant: Who has the expertise and should advise? Who will be affected and must be informed? Who has the authority to decide?
6. After the person confirms, call `decision_run_stage` with `stage: implement` and the same roles (still as strings), or hand over to implement-plan.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
