# Task TR-8.4.2 Build the record

Absorbs the record method and the escalation method of the earlier Prove work, now written
by hand.

## Formula

| Slot | For this task |
|---|---|
| Worker | Quality and compliance lead. Prepares the record for the person who clears it. Does not clear |
| Workflow | Gather what was compared, list open items, get a decision and a named clearer from the person, hand on what cannot be cleared, then write the record or label it an uncleared draft |
| Skill | TR-8.4.2 |
| Knowledge | `references/rules.md` (R3, R4), `references/patterns.md` (C6 to C12), `governance.md` |
| Tool | None. The record note is written by hand |
| Prompt | This guide |
| Template | `templates/record-note.md`, `templates/open-items.md` |
| Input | The finished text; the claims and their results from `claim-assessment`; the source notes from `source-assessment`; the reference lines from TR-8.4.1; the person's decisions and the clearer's name, role and date as the person states them |
| Governance | TR-H3, TR-H4, TR-H5, TR-H11, TR-H13; `governance.md` |

## Steps

1. **Gather what was actually compared.** The claims, each with its result from
   `claim-assessment` in the six hand-check words (`../../claim-assessment/references/statuses.md`);
   the source notes; the reference lines. Every result is labeled "not tool-checked".
   Never fill in a result nobody read. If the person refers to a check done elsewhere,
   follow the stop rule in `governance.md`: counts as told, nothing reconstructed.
2. **List the open items.** An item is open when it is any of:
   - a sentence that is partly found, not found in the passage, one where
     your passage says something different, or has no passage to compare with;
   - two supplied sources that disagree;
   - a source the person has not been able to check for a retraction, correction or newer
     version, or with an unclear date;
   - a policy question (for example, whether a tool was allowed for the input used),
     usually from the Ethical skills.
   Sentences found in their passage are not open, but they are not cleared either. Finding
   a passage is not clearance.
3. **Prepare each open item for the person** (`templates/open-items.md`): the claim as
   written and where it sits; the result in plain words; the passage quoted, or "no
   passage was available"; one question the person can answer without rerunning
   anything; and who would normally decide it, as a kind of internal process. Do not
   write the decision you prefer into the question.
4. **Point disagreements and policy questions to the right process.** A claim where
   your passage says something different, two sources that disagree, or a policy question is not something
   the drafting team clears alone. Name the process in plain words: "your medical review
   process" for scientific content, "your promotional review process" for material for
   customers or agencies, "your AI use policy owner" for tool questions, "your safety
   reporting procedure" if a side effect appears (TR-H6, TR-H11). For the review the
   whole deliverable goes to next, use the table in `references/escalation-packet.md`.
   Do not name or invent a specific company's procedure.
5. **Ask for the decisions and the clearer.** For each open item the person decides
   one of: revised (the text was changed), removed (the claim was taken out), or
   escalated (sent to the process in step 4). Record "cleared" for an open item only if
   the named clearer says they reviewed it and gives a reason; never suggest it. Ask
   for the clearer's name and role exactly as the person states them, and the date of
   the decision.
6. **Check the clearer** (`governance.md`):
   - It is a person's name the owner of the work gave in this conversation. Not taken from
     the document's author line, an email signature or a meeting list.
   - That person reviewed the work. "Put my manager's name, she will sign later" means
     the manager has not cleared it: write "Uncleared draft (to be cleared by <name>, <role if
     given>)", as you told me. A clearance reported in the past without role or date is
     "Uncleared draft (you said <name> cleared it; add role and date to record the
     clearance)".
   - It is not a tool, model, connector, assistant or team name.
   - A request to clear ("clear it") is not a clearance (`governance.md`, the clearer).
7. **Write the record note by hand.**
   - **A named person who reviewed it, with role and date:** the first line names them:
     "Cleared by <name>, <role>, <date>". No tool is needed for this. The
     person's review is what clears it, not anything this skill did.
   - **No named reviewer, or an open item without a decision:** the first line is
     "Uncleared draft", and the open items are listed.
   Either way, label the note "Record note written by hand; not tool-checked".
8. **Evidence table only on request.** If the person asks to see the evidence table,
   build it by hand from `../../../templates/evidence-table.md`, using the six hand-check
   words. Otherwise do not print a table of claims and results in the reply.
9. **Point to the next step** when the work leaves the company: the record goes with
   the work into the internal review process; it does not replace it.

## Checks before returning

- First line says "Uncleared draft" (or its placeholder or reviewed form) unless the
  person named who cleared it, with role and date. Only the forms in
  `../../work-record/templates/status-line.md` are written.
- Every open item appears, with its decision or "no decision yet".
- No name appears that the person did not give; no tool or model is named as clearer.
- Claims whose passage says something different are revised, removed or escalated, or cleared only on the named
  clearer's stated review and reason.
- No evidence table unless asked.
- Nothing says the work is approved, compliant, validated or true.

## Check line

See `templates/check-line.md`.

## Boundaries

- The everyday record of sources, tools, assumptions and status while drafting is
  `work-record`. This task writes the formal record at the end. When both run, this task
  reuses the sources, tools and assumptions `work-record` noted rather than rewriting them.
- Deciding whether a claim matches its passage is `claim-assessment`. This task does not
  change a result while writing the record.
- The counts and open-items summary are `confidence-scoring`.
