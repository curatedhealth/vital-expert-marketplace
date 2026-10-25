# Task DC-1.0.2 Size it and set rigor

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (framing). Does not choose the option and does not sign. |
| Workflow | Ask the two sizing questions, show the 2x2 suggestion, wait for the person's rigor, store it, stop. |
| Skill | DC-1.1 Frame the decision |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_run_stage` and `decision_rigor_guide` |
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

1. Ask: if this goes wrong, how high is the consequence? Then ask: how hard is it to undo, and at what cost?
2. Show the Playbook 2x2 suggestion in one line. High consequence and hard to undo: dig deep (dig_deep, or full_process for a strategic or critical decision). High consequence and easy to undo: use available intelligence and decide quickly (decide_quickly), ready to course-correct. Low consequence and hard to undo: proportionate effort (tradeoff). Low consequence and easy to undo: decide and experiment (decide_quickly).
3. Ask the authority question: solo, inform, consult, consent, or consensus? Speed-critical decisions favour solo or inform; buy-in-critical ones favour consent or consensus.
4. Ask the person to confirm a rigor. Call `decision_rigor_guide` with it and read the required stages back.
5. Call `decision_status` first. If the session has no rigor yet, call `decision_run_stage` with `stage: how_to_decide` and `payload: {consequence, reversibility, authority_mode, rigor}` (plus statement, goal, decider, deadline when known). If the session already has a rigor, send `change_rigor: {to, by: <person>, reason}` instead of bare `rigor`. Read back `rigor_unchanged` if it appears. The person's choice wins over the suggestion.
6. When the person says this is a people decision, include `people_decision: true` and read the warning text exactly.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
