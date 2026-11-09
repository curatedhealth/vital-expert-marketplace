# Knowledge: work-record

This file is the single home for this skill's sourced rules, failure patterns, gap
wording and failure modes. Where the same rule or pattern appeared in more than one
earlier file, one copy is kept.

## Contents

- Part 1: Rules (sourced, with scope and confirmation status)
- Part 2: Failure patterns (before and after)
- Part 3: Gap rules (shared wording, with this skill's cases)
- Part 4: Failure modes (detection questions)

## Part 1: Rules

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` has not been confirmed against the primary document and is applied as good
practice, not cited as a requirement (TR-H8).

Most of these rules govern regulated records (GxP data, signed electronic records,
journal submissions). Everyday work such as a board update or a payer deck is usually
outside their legal scope. This skill borrows their practice, not their obligation, and
never tells a person that a rule applies to their document unless its scope plainly
covers it.

Last reviewed: 20 October 2026.

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| R1 | Data should be attributable to the person generating it; records should identify both the person performing a task and the person completing the record; processing should include attribution to who performed the activity. | MHRA, "GXP Data Integrity Guidance and Definitions", Revision 1, March 2018, sections 3.10 (ALCOA), 5.2 (scribes), 6.1 (data), 6.9 (data processing). Official copy on assets.publishing.service.gov.uk. | UK, GxP data and records | Confirmed from the MHRA PDF on 20 October 2026. Applied here as practice for attributing every record entry. |
| R2 | An audit trail allows reconstruction of the "who, what, when and why" of an action; changes are associated with the persons making them and dated. | Same MHRA document, section 6.13 (audit trail). | UK, GxP computerized systems | Confirmed 20 October 2026. Applied here as practice: the record says who did what, in which order, and when where dates were given. |
| R3 | Signed electronic records show the printed name of the signer, the date and time of signing, and the meaning of the signature (such as review, approval, responsibility or authorship), in any human-readable form of the record. | US Code of Federal Regulations, 21 CFR 11.50 (a) and (b), signature manifestations. eCFR, up to date as of 15 October 2026. | US, electronic records and signatures under FDA predicate rules | Confirmed from eCFR on 20 October 2026. Applied here as practice: a status above "draft" carries a name, a date and its meaning. |
| R4 | Authors who use AI-assisted technologies should disclose it and describe how they used it, in the cover letter and the submitted work; AI tools are not listed as authors because they cannot be responsible for the accuracy, integrity and originality of the work; humans are responsible for submitted material that used AI. | International Committee of Medical Journal Editors (ICMJE), Recommendations, section "Artificial Intelligence: A. Use of AI by Authors", icmje.org. | Manuscripts submitted to journals that follow ICMJE | Confirmed from icmje.org on 20 October 2026 and re-read 9 November 2026: "Chatbots (such as ChatGPT) and other AI-assisted tools should not be listed as authors"; "Authors who use such technology should describe, in both the cover letter and the submitted work ..."; "humans are responsible for any submitted material that included the use of AI-assisted technologies". Version: ICMJE Recommendations, "Updated January 2026" (icmje.org PDF, read 9 November 2026). Used here for "what the AI did" and for "a human stands behind it". Whether a disclosure is required in a given deliverable is responsible-use. |
| R5 | Deployers of an AI system that generates or manipulates text published to inform the public on matters of public interest disclose that the text was artificially generated or manipulated, unless it has undergone human review or editorial control and a person holds editorial responsibility. | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Article 50(4); application date per Article 113. | EU | Confirmed 20 October 2026 from the Commission's official copy of the text consolidated at 27 July 2026, read during the responsible-use build (see that skill's rule U6); applies from 2 August 2026. Not applied by this skill. Listed so the record captures the facts (AI involvement, named human review) that responsible-use needs to decide. |

### How to use these rules in output

- When the person asks why the record or status matters, explain the practice in plain
  words: "A reader should be able to tell who did what and who stands behind it."
- Cite a rule by name only when its scope covers the work (for example R4 for a journal
  manuscript, R3 for a signed electronic record in a GxP system) and the person asks.
- Never extend a rule beyond its scope. R1 to R3 do not make a board update a GxP
  record. R5 is not applied by this skill; responsible-use owns the disclosure question.

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it
breaks. All examples are invented for teaching; no real product, company or person.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

### Contents

- Provenance P1–P6
- Assumptions and open items A1–A5
- Status S1–S7
- Depth D1–D2

### Provenance

**P1 The reconstructed source list.** Source titles, versions or dates filled in to make
the record look complete.
Why: a record with an invented version is worse than one with a gap; it sends the next
reader to the wrong file.
Before: "Built from the Q3 national sales extract (v2.1, 3 October 2026)." Supplied:
"the Q3 sales file".
After: "Built from the Q3 sales file [GAP: not supplied; file version or date; name
it so others can find it]." (TR-H1, R1)

**P2 The assistant that validated.** The AI's work described with review words.
Why: "validated" and "verified" tell a reader a qualified check happened. A summary is
not a validation.
Before: "Data validated by AI." After: "The assistant compared the figures in the text
with the sales file you shared; no differences left open." (TR-H3)

**P3 The model name from memory.** A model or version stated that the host did not show.
Why: the record is only as good as its least certain line.
Before: "Made with GPT-5 Turbo." After: "Made with the assistant in this conversation
[GAP: not supplied; model or version; add it if your policy asks for it]." (TR-H1)

**P4 The connector that was not used.** Every connected tool listed as if it took part.
Why: a reader will assume a literature search or fact-check happened.
Before: "Sources: literature connector, citation tool." (Neither was used.)
After: list only tools that ran for this work. (TR-H4)

**P5 Earlier steps written as seen.** Work done elsewhere recorded as if the assistant
saw it.
Before: "First draft written in another assistant and reviewed by the team."
After: "First draft written in another assistant and reviewed by the team, as you told
me." (TR-H1, R1)

**P6 The silent sensitive input.** A confidential or unpublished document used, and the
record leaves it out to look tidy.
Why: the record is where a reviewer would find it; leaving it out removes the chance to
ask the right question.
After: "Built from the unpublished study report you shared. Whether it should have gone
into this assistant is a question for your AI use policy." (TR-H11)

### Assumptions and open items

**A1 The quiet estimate.** An assumed figure written as data.
Before: "Eligible population: 4,000 patients." (The person said "say around 4,000".)
After: "Eligible population assumed at about 4,000, as you told me; no source supplied."
(TR-H1, TR-H2)

**A2 The decision written as taken.** A pending choice stated as settled.
Before: "The subgroup result will be shown to payers."
After: "Open: whether the subgroup result may be shown to payers. Owner to be named."
(TR-H5)

**A3 The guessed owner.** A role or name assigned that the person did not give.
After: "Owner to be named." (TR-H1)

**A4 The list that buries the point.** Twenty minor items, with the one that changes the
conclusion in the middle.
After: lead with the items that change what a reader would do; drop the rest or group
them. (TR-H12)

**A5 Gaps in the text, missing from the list.** Inline gaps nobody will collect.
After: every inline gap appears once in the open items, in plain words. (TR-H13)

### Status

**S1 Approved on request.** "Mark it approved" leads to "Approved" with no name.
Why: a reader takes it as fact about the document, and nobody can say who stands behind
it.
After: ask who, through which process, when; keep "Uncleared draft" until the person says. (TR-H5,
R3)

**S2 Final by default.** Headers or file names say "final" because the drafting is done.
Before: "Payer deck FINAL". After: "Payer deck, draft for review". (TR-H5)

**S3 Reviewed by the check.** A TRUSTED check presented as a review.
Before: "Reviewed with TRUSTED: no issues." After: "TRUSTED check run: 2 flags, 1 open
item. Uncleared draft." (TR-H3, TR-H10)

**S4 The approval with no meaning.** A name with no indication of what they did.
Before: "A. Rossi, 14 October 2026." After: "Status: Uncleared draft, reviewed by Dr. A.
Rossi, as you told me." Her role and the date go in the people's part of the note. (R3)

**S5 The invented reference.** An approval code, job number or date filled in to make
the status look complete.
After: "[Approval reference: as given by your review process]". (TR-H1)

**S6 The lost draft marking.** Draft status removed when the text was pasted into a new
format (slide, email), without anyone clearing it.
After: carry the status line into the new format. (TR-H5)

**S7 Product status confused with document status.** "Approved" about the product
treated as a status of the document, or the reverse.
After: leave statements about the product to grounded-statements; this skill handles
the status of the document only.

### Depth

**D1 The record nobody asked for.** A full record note, draft banner and open-items list
under a two-line team email.
Why: if every note gets the full treatment, people stop using it.
After: nothing, or one line if asked. (TR-H12)

**D2 The external deck with no record.** A payer deck sent with no note of sources,
assumptions or status.
After: the full record note and status line, with a pointer to the internal review
process. (TR-H12, TR-H11)

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/knowledge.md` (Part 2).

Same format and classes as every TRUSTED skill:
`[GAP: <class>; <what is missing>; <what would close it>]`

| Class | Typical case in this skill |
|---|---|
| `not supplied` | A source title, version or date; a model name the host does not show; who did an earlier step; an owner for a decision |
| `conflicting` | The person's account of an earlier step differs from what the conversation shows (for example, a file said to be the final extract has a different period in it) |
| `out of date or unclear date` | A material described as "latest" or "current" with no date |
| `not checkable here` | Whether the record matches what happened outside this conversation |
| `needs a decision` | Whether a status may be raised, who owns an open item, whether AI use must be disclosed (handed to responsible-use) |

Wording rules:

- In the record note the person reads, gaps can be written in plain words in the "Open"
  section ("Version of the sales file not given"). Keep the bracket form inline in the
  deliverable, where a reviewer scans for it.
- Never put a likely value inside a gap ("probably the October extract").
- A gap in the record is not a criticism of the person. Do not apologize for it or
  blame anyone.
- A status still to come reads "Uncleared draft (to be cleared by <name>, <role if given>)", or "Uncleared
  draft (to be cleared by a reviewer not named yet)" when no name was given, in the
  deliverable and in the record note alike. It is never filled by the assistant. Only a
  person who has cleared the work, with role and date, goes after "Cleared by". The forms,
  and only these, are in `templates/status-line.md`.

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-WR-01 | Invented approver | Was an approver/date/reference fabricated? | Status | TR-H5 | VERIFIED practice |
| FM-WR-02 | Draft marked final | Were draft watermarks removed without named clearance? | Status | TRUSTED work-record | VERIFIED practice |
| FM-WR-03 | Missing open items | Can a reviewer not see assumptions and gaps? | Record | TRUSTED work-record | [CHECK] |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
