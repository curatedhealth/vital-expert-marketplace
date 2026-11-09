# Task DC-6.0.1 Run the checklist

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (readiness check). Does not choose the option and does not sign. |
| Workflow | Read the session, mark each item from stored evidence, ask about one unknown, report, stop. |
| Skill | DC-6.0 Decision check |
| Knowledge | `references/knowledge.md`, `references/knowledge.md`, `references/failure-modes.md` |
| Tool | Decision Companion `decision_status` and `decision_rigor_guide` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `templates/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_status` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps with the plugin's local tools, or by hand when they cannot run. Do not label the reply. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_status` (and `decision_rigor_guide` for the session rigor). Prefer `required_stages_unmet`, `daii_valid`, and `complete_with_gaps` over trusting stage flags alone.
2. Cross-check the widen stage against the stored options count. If the flag says complete with fewer than 3 options, mark widen not met (`too_few_options`). If the flag says incomplete with 3 or more options, treat widen as met for readiness and note the stale flag.
3. Mark each checklist item in `references/knowledge.md` as met, not met, or not known. Role-only names are not met. Met needs a stored field or the person's own answer in this conversation.
4. Ask about the single not-known item that matters most for this rigor. One question.
5. Report per section (for example: Options 2 of 4 met) and list what is not met. Give the Playbook guidance once: all items met means the checklist is complete; a few gaps means the person can address them or go ahead knowing what is open; many gaps means more preparation. The person decides whether they are ready. Say it is Playbook guidance, not a validated score.
6. If a brief is present, read its ✓/✗/? checklist marks as evidence, not as a score.
7. Name the weakest of the six quality elements and the skill that addresses it. Do not say the decision is good or bad.

## Output

Reply as a coach: short plain prose and one question. Use `templates/worksheet-output.md` only when the person asks for the record or a summary of this step. End with the one question, or the closing line when the governance file says so.
