# Task TR-8.4.2 Build the record

Absorbs the record method and the escalation method of the earlier vital-verify plugin.

## Formula

| Slot | For this task |
|---|---|
| Worker | Quality and compliance lead. Prepares the record for the person who clears it. Does not clear |
| Workflow | Gather what was checked, list open items, get a decision and a named clearer from the person, hand on what cannot be cleared, then write the record or label it an uncleared draft |
| Skill | TR-8.4.2 |
| Knowledge | `references/rules.md` (R3, R4), `references/patterns.md` (C6–C12), `references/governance.md`, `references/tools.md` |
| Tool | VERIFY `build_record`, only after a named person has given a decision for every open item. VERIFY `build_evidence_table`, only when the person asks for the table |
| Prompt | This guide |
| Template | `assets/record-note.md`, `assets/open-items.md` |
| Input | The finished text; the claims and their results from `claim-assessment`; the sources and their results from `source-assessment`; the reference lines from TR-8.4.1; the person's decisions and the clearer's name and role as the person states them |
| Governance | TR-H3, TR-H4, TR-H5, TR-H11, TR-H13; `references/governance.md` |

## Steps

1. **Gather what was actually checked.** The claims, each with its result from
   `claim-assessment`; the sources, with any results from `source-assessment`; the
   reference lines. If claims were not checked with VERIFY, the record says "not
   tool-checked" for them. Never fill in a result that no tool returned.
2. **List the open items.** An item is open when it is any of:
   - a claim only partly supported, not supported, contradicted by its passage, or not
     checkable (no passage was available);
   - two supplied sources that disagree;
   - a source flagged as retracted, corrected or superseded, or with an unclear date;
   - a policy question (for example, whether a tool was allowed for the input used),
     usually from the Ethical skills.
   Supported claims are not open, but they are not cleared either. Support is not
   clearance.
3. **Prepare each open item for the person** (`assets/open-items.md`): the claim as
   written and where it sits; the result in plain words; the passage quoted, or "no
   passage was available"; one question the person can answer without rerunning
   anything; and who would normally decide it, as a kind of internal process. Do not
   write the decision you prefer into the question.
4. **Point contradictions and policy questions to the right process.** A claim the
   source contradicts, two sources that disagree, or a policy question is not something
   the drafting team clears alone. Name the process in plain words: "your medical review
   process" for scientific content, "your promotional review process" for material for
   customers or agencies, "your AI use policy owner" for tool questions, "your safety
   reporting procedure" if a side effect appears (TR-H6, TR-H11). Do not name or invent
   a specific company's procedure.
5. **Ask for the decisions and the clearer.** For each open item the person decides
   one of: revised (the text was changed), removed (the claim was taken out), or
   escalated (sent to the process in step 4). Record "cleared" for an open item only if
   the named clearer says they reviewed it and gives a reason; never suggest it. Ask
   for the clearer's name and role exactly as the person states them, and the date of
   the decision.
6. **Check the clearer** (`references/governance.md`):
   - It is a person's name the person gave in this conversation. Not taken from the
     document's author line, an email signature or a meeting list.
   - That person reviewed the work. "Put my manager's name, she will sign later" means
     the manager has not cleared it: write "To be cleared by: <name>" and keep the
     record an uncleared draft.
   - It is not a tool, model, connector, assistant or team name.
7. **Write the record.**
   - **Named clearer and a decision for every open item, VERIFY connected:** call
     `build_record` (`references/tools.md`). Report what it returned. If it refuses,
     say why in plain words and keep the uncleared draft.
   - **No named clearer, or an open item without a decision:** do not call
     `build_record`. Write the record note with "Uncleared draft" as its first line and
     the open items listed.
   - **Without VERIFY:** write the same record note by hand, in the shape `work-record`
     uses for the everyday record, marked "Record note built by hand; not tool-built".
     A hand-written note can carry a clearer the person named, but it is not a VERIFY
     record.
8. **Evidence table only on request.** If the person asks to see the evidence table,
   call `build_evidence_table` with the findings and show what it returns. Otherwise do
   not call it and do not print a table of claims and statuses in the reply.
9. **Point to the next step** when the work leaves the company: the record goes with
   the work into the internal review process; it does not replace it.

## Checks before returning

- First line says "Uncleared draft" unless `build_record` accepted a named clearer.
- Every open item appears, with its decision or "no decision yet".
- No name appears that the person did not give; no tool or model is named as clearer.
- Contradicted claims are revised, removed or escalated, or cleared only on the named
  clearer's stated review and reason.
- No evidence table unless asked.
- Nothing says the work is approved, compliant, validated or true.

## Check line

See `assets/check-line.md`.

## Boundaries

- The everyday record of sources, tools, assumptions and status while drafting is
  `work-record`. This task builds the formal record at the end, with VERIFY. When both
  run, this task reuses the sources, tools and assumptions `work-record` noted rather
  than rewriting them. [CHECK: `work-record` is not yet drafted; field alignment to be
  confirmed when it is.]
- Deciding whether a claim is supported is `claim-assessment`. This task does not
  change a result while writing the record.
- The confidence figure and the VERIFY card are `confidence-scoring`.
