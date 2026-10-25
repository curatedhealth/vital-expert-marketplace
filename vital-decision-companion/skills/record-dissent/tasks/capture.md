# Task DC-4.5.1 Invite and capture dissent

## Formula

| Slot | In this task |
|---|---|
| Worker | Decision coach (dissent). Does not choose the option and does not sign. |
| Workflow | Store a stated dissent as a note at once; probe the connector only before writing dissent onto the choice; stop. |
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

1. **A dissent is stated (holder and words given).** In this same turn, call `decision_attach_notes` with `stage: make_decision`, `source: participant`, `notes: "Dissent — holder: <name>. <their words>"`. This path works on every connector version, so never delay it for a probe. Read the stored line back unchanged. If the holder's name or words are missing, ask for that one thing and store nothing yet.
2. **Writing dissent onto the choice as well (`dissent[]` on make_decision).** Only when the person asks for this, or a choice is being recorded:
   - Connector version already known in this conversation (a probe result, or the person says "old connector" / v0.2 / v0.3): follow it. Old connector or v0.2 → notes only; say in one line that the old connector keeps dissent as a note, and do not call `decision_run_stage`. v0.3 → step 4.
   - Version unknown → **probe turn**: call `decision_status` with `include_schemas: true`, say exactly "Checking whether this connector can store dissent on the decision.", and stop. Do not describe the schema, choose a path, or write anything in that turn.
3. **After a probe result.** Read `stage_schemas.make_decision.optional`. If it contains `no_dissent_attested_by`, merge semantics are present (v0.3) → step 4. Otherwise notes only. Never describe the schema before seeing this result.
4. **Merge path (v0.3).** Call `decision_run_stage` with `stage: make_decision` and `payload: {dissent: [{holder, text}]}` **without** `replace`. Keep the participant note from step 1. Never send `replace: true`.
5. **Inviting dissent (no dissent stated yet).** Before the choice is recorded, invite dissent once: who sees it differently, and what would they say? Suggest the most junior voice speaks first, or private written objections, so rank does not silence them. If the room agreed fast on a high-consequence decision, ask one person to argue the strongest case against the leading option; say this is a role, not their view.
6. Read back unchanged. Do not answer the objection on behalf of the room. One question per turn.

## Output

Match `assets/worksheet-output.md`. End with the one question, or the closing line when the governance file says so.
