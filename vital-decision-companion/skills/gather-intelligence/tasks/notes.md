# Task DC-3.1 Gather knowns, unknowns, and one disconfirming question

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (intelligence). Does not choose the option and does not sign. |
| Workflow | Ask one intelligence question, store the answer as a note, store the stage when knowns and unknowns exist, stop. |
| Skill | DC-3.1 Gather intelligence |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_attach_notes` and `decision_run_stage` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_attach_notes` with the arguments in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Ask one question per turn from the intelligence set, in this order unless the person is already further: What do we know for certain, and from which source? What are we uncertain about? What has to be true for the leading option to be the best? What is the best disconfirming question we could ask, and how would we find the answer? Who else needs to be in the room? How current and reliable are our sources?
2. For any estimate (a share, a timeline, a probability), ask first how similar past cases turned out (the base rate) before discussing this case.
3. Call `decision_attach_notes` with `stage: gather_intelligence`, the person's words, and the source they named (owner or participant). Your own summary is `source: draft`.
4. When the person has given at least one known and one unknown, call `decision_run_stage` with `stage: gather_intelligence` and `payload: {knowns: [...], unknowns: [...], disconfirming_question}` so the stage is marked complete. Notes alone never complete it.
5. Leave an unknown as a gap. Do not fill it from memory. A claim that needs checking goes to handoff-verify.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
