# Task DC-4.5.1 Invite and capture dissent

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (dissent). Does not choose the option and does not sign. |
| Workflow | Detect merge vs replace, invite dissent, store notes always (+ dissent[] when merge-safe), stop. |
| Skill | DC-4.5 Record dissent |
| Knowledge | `references/rules.md`, `references/patterns.md`, `references/gap-rules.md` |
| Tool | Decision Companion `decision_status`, `decision_attach_notes`; optional `decision_run_stage` |
| Prompt | Use only fields the person supplied or the tool returned. |
| Template | `assets/worksheet-output.md` |
| Input | The person's words and, when a session exists, `session_id`. |
| Governance | DC-H1, DC-H3, DC-H4, DC-H5. A missing field stays `[GAP]`. |

## Companion

| State | What to do |
|---|---|
| `vdec_` connected | Call tools as in `references/tools.md`. |
| `vdec_` absent | Follow the same steps by hand. Head the result **not tool-checked**. Do not invent a tool field. |

Navigator tools, when this skill names them, use `vont_` on `vital-ontology-navigator`. Verify tools use `vvfy_` on `vital-verify`. Those calls are not simulated here.

## Steps

1. **Schema probe (its own turn).** Call `decision_status` with `include_schemas: true`. Say exactly: "Checking whether this connector can store dissent on the decision." Then **stop**. Do not describe the schema, do not choose merge vs notes, and do not invite dissent in this turn.
2. **After the probe result.** Read `stage_schemas.make_decision.optional`. If it contains `no_dissent_attested_by`, merge semantics are present (v0.3): you may later write `dissent[] {holder, text}` without `replace`. Otherwise (v0.2) use notes only for the make_decision payload path. Never describe the schema before seeing this result.
3. Before the choice is recorded, invite dissent once: who sees it differently, and what would they say? Suggest the most junior voice speaks first, or that objections are written privately, so rank does not silence them.
4. If the room agrees fast on a high-consequence decision, ask one person to argue the strongest case against the leading option. Say this is a role, not their view.
5. For each dissent, ask for the holder's name and their words.
6. Always call `decision_attach_notes` with `stage: make_decision`, `source: participant`, and `notes: "Dissent — holder: <name>. <their words>"`. Keep this participant note on every connector version.
7. On the merge path only, also call `decision_run_stage` with `stage: make_decision` and `payload: {dissent: [{holder, text}]}` **without** `replace`. Never send `replace: true`.
8. Read it back unchanged. Do not answer the objection on behalf of the room.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
