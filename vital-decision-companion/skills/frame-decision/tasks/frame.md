# Task DC-1.0.1 Frame the decision

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (framing). Does not choose the option and does not sign. |
| Workflow | Ask one framing question, store what is known, ask the next, stop. |
| Skill | DC-1.0 Frame the decision |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_run_stage` |
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

1. Ask for the decision in one sentence, using the form: we need to decide what, by when, because why. Read it back.
2. Then, one per turn, ask only what is still missing: What is the goal, and what would success look like? What is the core of the issue? Who makes the final decision, as a named person? What is the deadline? Which criteria will guide the choice? What values matter here? What is the ripple effect if we get it wrong?
3. If the person frames a yes/no question (should we do X?), reframe it as: how might we achieve the goal? Tell them binary framing is the most common cause of failed decisions. Do not add options yourself; widen-options does that.
4. Is now the right time? If the person says the decision should wait, store that answer and the date they name.
5. When statement, goal, and rigor exist, call `decision_run_stage` with `stage: how_to_decide` and `payload: {statement, goal, rigor, decider, deadline, core_issue, criteria, values}`. Send only fields the person gave.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
