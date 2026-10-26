# Task DC-1.0.2 Size it and set rigor

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (framing). Does not choose the option and does not sign. |
| Workflow | Ask the two sizing questions, propose a depth in plain words, store it unless the person objects, continue. |
| Skill | DC-1.1 Frame the decision |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_run_stage` and `decision_rigor_guide` |
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

1. Ask: if this goes wrong, how high is the consequence? Then ask: how hard is it to undo, and at what cost?
2. Map the answers backstage (never say these ids to the person): high consequence and hard to undo → dig_deep (full_process for a strategic or critical decision); high consequence and easy to undo → decide_quickly, ready to course-correct; low consequence and hard to undo → tradeoff; low and easy → decide_quickly.
3. Propose the depth in one plain sentence and keep going, for example: "Since this is costly and hard to undo, let's also weigh what matters and check what could go wrong before you choose." Do not offer a menu of levels. If the person wants it lighter or heavier, follow them.
4. Ask the authority question only when it changes who must be heard (several people involved, buy-in needed); in plain words: "Will you decide alone, or do others need to agree?" Whatever the depth, the decision-quality floor (DC-H16) still applies.
5. Call `decision_status` first. If the session has no rigor yet, call `decision_run_stage` with `stage: how_to_decide` and `payload: {consequence, reversibility, authority_mode, rigor}` (plus statement, goal, decider, deadline when known). If the session already has a rigor, send `change_rigor: {to, by: <person>, reason}` instead of bare `rigor`. On `rigor_unchanged`, fix it silently (DC-H11). The person's preference wins over the suggestion.
6. When the person says this is a people decision, include `people_decision: true` and read the warning text exactly.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
