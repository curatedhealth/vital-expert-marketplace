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
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field is left out of the payload and shown as "not given yet". |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Required for complete are statement, goal, decider, and deadline. Call `decision_run_stage` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask for the decision in one sentence, using the form: we need to decide what, by when, because why. Read it back.
2. Then, one per turn, ask only what is still missing: What is the goal, and what would success look like? What is the core of the issue? Who makes the final decision, as a named person? What is the deadline? Which criteria will guide the choice? What values matter here? What is the ripple effect if we get it wrong?
3. If the person frames a yes/no question (should we do X?), reframe it as: how might we achieve the goal? Tell them binary framing is the most common cause of failed decisions. Do not add options yourself; widen-options does that.
4. Is now the right time? If the person says the decision should wait, store that answer and the date they name.
5. When the person says this is a people decision (hiring, promotion, performance, termination of a named person), send `people_decision: true` on the how_to_decide payload **first**. In that same turn say only: "I've flagged this as a people decision; the connector's notice will follow. I won't compare, score or rank the people involved." Give **no** HR, legal, or AI Act wording, and ask **no** further question (not "who" and not "when") until the connector's `people_decision` warning returns. If a required field is ambiguous (for example a deadline with no year), do not store a guessed value: send `people_decision: true` with only the fields that are certain, and ask about the ambiguous one after the notice has returned. When it returns, read its text **verbatim**. If the tool returns with no warning (v0.2), then use the R7 wording and say it is the skill's notice, not the connector's — still one question after that notice, not before.
6. When statement, goal, decider, and deadline exist, call `decision_run_stage` with `stage: how_to_decide` and `payload: {statement, goal, decider, deadline, core_issue, criteria, values}` (plus `people_decision: true` when applicable). Send only fields the person gave. Set rigor in the size task (once, or via change_rigor).

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
