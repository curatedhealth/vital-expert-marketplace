# Task DC-4.2 Capture the hypotheses

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (failure hypotheses). Does not choose the option and does not sign. |
| Workflow | Set the scene, collect failures privately, ask signal, mitigation, and owner, call `decision_premortem`, stop. |
| Skill | DC-4.2 Pre-mortem |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_premortem`; see the companion slot |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_premortem` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Set the scene: imagine it is six months from now (or the horizon the person names) and this decision failed badly. What happened?
2. In a group, ask each person to write their reasons alone before anyone speaks, then share one at a time, most junior first.
3. For each failure, one per turn, ask: what early signal would show it is happening? What would we do to prevent or soften it? Who owns watching for it?
4. Call `decision_premortem` with `hypotheses: [{failure, early_signal, mitigation, owner, raised_by}]` in the person's words. Leave a missing field as [GAP].
5. Never send `recommendation`. Handle per-index refusals; if one bad item drops the whole batch, resend without it and tell the person. Do not rank the list and do not turn it into advice. Point to implement-plan to turn each failure into an if–then plan.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
