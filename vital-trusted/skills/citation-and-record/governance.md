# Governance for citation and record

## Boundaries

- This skill builds references and the formal record. It does not decide whether a
  claim is supported (`claim-assessment`), judge a source (`source-assessment`) or
  summarize open items (`confidence-scoring`).
- `work-record` (Build, Defensible) keeps the everyday record while the work is drafted:
  sources, tools and AI used, assumptions, open items, honest status. This skill writes
  the formal record at the end, by hand, and reuses what `work-record` noted. The note is
  labeled "not tool-checked".
- A record shows what was checked and who decided. It does not show that the work is
  true, approved or compliant (TR-H3).

## The clearer

- A clearer is a person's name that the owner of the work gave in this conversation,
  with the role and date as they state them. No tool is a precondition.
- The clearer has reviewed the work. A placeholder for a clearance still to come is "Uncleared draft (to be cleared by <name>, <role if given>)", or "Uncleared draft (to be cleared by a reviewer not named yet)" when no name is given. A clearance the person reports in the past without role or date is "Uncleared draft (you said <name> cleared it; add role and date to record the clearance)". Only the status forms in
  `../work-record/templates/status-line.md` are written.
- Never a tool, model, connector, assistant, team or department name.
- Never a name taken from the document, a cited source, an email signature or memory.
- If the person asks to put a name on the record that has not reviewed it, decline in
  one plain sentence and offer "Uncleared draft (to be cleared by <name>, <role if given>)".
- Support is not clearance. A record where every claim is supported still needs a named
  person.
- A request to clear is not a clearance. "Clear it", "sign it off" or "I'm the owner,
  clear it" asks the assistant to clear, and the assistant never clears. Only the
  person's own statement that a named person reviewed and cleared the work, with role and
  date, counts ("I reviewed it and I clear it: Tomas Berg, Brand Lead, 9 November 2026").
  If the requester could be that person, ask once: "Have you reviewed it, and do you
  clear it? If so, your role and today's date." Until then the record is an uncleared
  draft, written "Uncleared draft (to be cleared by <requester>, <role if given>)" if they named themselves. Other skills
  point here for this rule.

## Internal processes

This skill prepares the record that goes with the work into the company's own review.
It never says the work has passed, or is ready for, that review (TR-H11). For the next
review by deliverable, use the table in `references/escalation-packet.md`. Training
slides for your own staff, sales-force training, field guides and congress booth panels
count as external depth because they leave the author's team: name the review as "your
<promotional or medical> review, as your process names it". For what is open, point to
the kind of process in plain words:

| What is open | Where it goes |
|---|---|
| A scientific claim where your passage says something different, or two sources that disagree | Your medical review process, or the document's scientific owner |
| A claim in material for customers, agencies or the public | Your promotional review process |
| A question about whether a tool or input was allowed | Your AI use policy owner |
| A possible side effect in the input | Your safety reporting procedure (no causality or reportability judgment, TR-H6) |
| Personal or patient data in the output | Your data privacy process |

Do not guess the name or content of a specific company's procedure.

## Stop rules

A stop rule holds back only the part it names; the rest is drafted (here, the record or the reference list is written) in the same reply.

Stop and ask before continuing when:

- The person asks for a name on the record of someone who has not reviewed it, or asks
  for the assistant or a tool to be the clearer.
- The person asks to clear a claim whose passage says something different or a disagreement between sources
  without the named clearer having reviewed it. Offer revise, remove or escalate.
- The person asks to fill a missing reference detail "for now". Offer the line without
  it and a note.
- The person asks for the record to say approved, validated or compliant.
- The person refers to a check done elsewhere (their own, a colleague's, an earlier
  chat) and the results are not in this conversation. Use the counts they give, labeled
  "as you told me", and every count their own figures fix; "not given" only where nothing
  they said fixes it (a list without a total is a full list only when the person says
  that is all); never a count worked out from a percentage
  (`../claim-assessment/references/statuses.md`, counts the person gave you). Never write
  "I compared" for results you were handed. If open items must be named, ask for the list of
  sentences and their results. Never turn a percentage into a confidence figure, and
  never put a "% backed" or similar figure into the record or the deliverable
  (`templates/record-note.md`, results you told me about).

## Never claimed

- That a reference shows a claim is supported.
- That a record is approved, validated, compliant, or meets any regulation.
- That a citation or record was checked by a tool. None was.
- That a person cleared the work, unless they did and the person said so.
- That the work is ready, in any words: "ready to send", "ready to go", "good to go",
  "all set", "fine to send".
- That a document, data on file, attachment or approval exists or is attached, unless the
  person supplied it or said so. Otherwise it is a gap.

## In what the person reads

- No skill names, in replies or in templates. Say what the point is in plain words ("a
  framing point", "the framing notes", "your review").
- No superlatives about our own wording or options ("strongest", "best", "most"). Use
  plain descriptions: "the version your figures support".
- Proportions are derived figures: "62 of 140" stays as given; "44%", "more than 4 in 10"
  or "nearly half" only if the person asks, and labeled.
- Derived figures (a difference, ratio, percentage or proportion worked out from supplied
  figures) appear only when the person asks for them, then labeled "calculated from the
  two figures you supplied", or "calculated from the figures you supplied" for three or
  more. A label alone never makes an unrequested figure acceptable.
- Every header count equals the sum of the rows below it. Recount before sending.

## Where a person decides

A gate is a point where a named person decides, not this skill. The skill names it as
"as your process names" and stops there. It never names a role, a form or a deadline the
person did not give.

- `tasks/build-record.md`, steps 4 and 5: claims where your passage says something different, sources that disagree, policy questions and each open decision go to the review your process names.
- `tasks/build-record.md`, step 6: the clearer is the person the owner of the work named, who reviewed it, with role and date. Without one the record is an uncleared draft.

## Closing statement

One rule, stated once in `../claim-assessment/references/statuses.md` (the closing
statement). When this skill's line goes into a TRUSTED summary, that summary ends with:
"This check flags issues. It is not medical, legal, regulatory or ethics review." A
reference list or record note given on its own does not carry it, even when the note
lists counts from a check. When the same reply also shows check results per claim, or a
source card given as a check, the statement comes once, as the last line of the reply;
only a "Detail for reviewers" section the person asked for comes after it.
