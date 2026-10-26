# Task DC-5.2.2 Turn risks into if–then plans

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (implementation). Does not choose the option and does not sign. |
| Workflow | Read the stored pre-mortem, ask for one if–then plan per failure, store them, stop. |
| Skill | DC-5.2 Implementation plan |
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

1. Read the stored pre-mortem hypotheses back (from the session or this conversation).
2. For each failure, one per turn, ask: what early signal would tell us it is happening, and if we see it, then who does what?
3. Write each answer as: if [signal], then [owner] will [action]. Reject a vague action such as monitor closely and ask for a concrete one.
4. Add the if–then plans to the Implement stage payload as `if_then_plans` and call `decision_run_stage` with `stage: implement`.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
