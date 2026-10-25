# Task DC-6.2 Review what happened

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (review). Does not choose the option and does not sign. |
| Workflow | On or after the review date, ask the review questions one at a time, store via run_stage (merge) and a note, stop. |
| Skill | DC-6.2 Learning loop |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_run_stage`, `decision_attach_notes`, and `decision_status` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call `decision_run_stage` then `decision_attach_notes` as in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. Call `decision_status` and read back what was expected: the stored success signal, probability, and assumptions. Show them before asking what happened, so hindsight does not rewrite the forecast.
2. Ask what actually happened, in the person's words. Then ask the after-action questions one per turn: what went well and why; what did not and why; what we would do differently.
3. Ask the process-versus-outcome question: given what we knew then, was the decision process sound? Place the answer in one of four cells the person chooses: good process and good outcome (deserved success), good process and bad outcome (bad break), poor process and good outcome (dumb luck), poor process and bad outcome. Do not choose the cell for them.
4. Ask the double-loop question: which assumption or decision rule should change for next time?
5. Call `decision_run_stage` with `stage: learning_loop` (merge, no `replace`) and `payload: {what_happened, process_quality_note, outcome_vs_process, lessons, assumption_to_change}` plus `authored_by`. Map the person's words exactly: what happened → `what_happened`; anything about how the decision was made (skipped a base-rate check, rushed, good debate) → `process_quality_note`; the cell they chose → `outcome_vs_process`. Keep process and outcome in separate fields. Then call `decision_attach_notes` with `stage: learning_loop`, the person's words, and `source: owner`. If the words are your summary, use `source: draft` and say so.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
