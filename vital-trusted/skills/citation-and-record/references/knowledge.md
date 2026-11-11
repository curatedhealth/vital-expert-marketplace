# Knowledge: citation-and-record

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
practice, not cited as a requirement (TR-H8). Scope is stated for each; outside that
scope the rule is good practice only.

Last reviewed: 20 October 2026.

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| R1 | Cite original research sources directly where possible; prefer published articles to abstracts; authors are responsible for citing accurately and should verify references against a bibliographic source (such as PubMed) or the original; check that no reference cites a retracted article except to refer to the retraction. | ICMJE, Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals, section "Preparing a Manuscript for Submission", References (icmje.org, page dated © 2026). | Manuscripts submitted to journals following ICMJE. Good practice for any reference list in this skill. | Confirmed from icmje.org on 20 October 2026. Version: ICMJE Recommendations, "Updated January 2026" (icmje.org PDF, read 9 November 2026). The references wording was not re-read in that pass `[CHECK]`. |
| R2 | Chicago and Harvard reference styles: the elements and their order. | Chicago: The Chicago Manual of Style (University of Chicago Press), current edition. Harvard: no single owning body; conventions vary by institution. | Style only. | `[CHECK]`: edition and rules not read from the primary document. In this skill, lines are written by hand from the supplied details; the skill does not enforce style rules of its own. Plain lines follow no named style and say so. |
| R3 | Data should be attributable, legible, contemporaneously recorded, original or a true copy, and accurate (ALCOA). | FDA, Data Integrity and Compliance With Drug CGMP: Questions and Answers, guidance for industry, December 2018 (fda.gov/media/119570). | US drug CGMP records under 21 CFR parts 210, 211 and 212. Nonbinding recommendations. Applied here only as good practice: a record says who did what and when, and keeps what was checked as it was. | Confirmed from the FDA document on 20 October 2026. |
| R4 | A signed electronic record shows the signer's printed name, the date and time of signing, and the meaning of the signature (such as review, approval, responsibility or authorship), and these appear in any human-readable form of the record. | 21 CFR 11.50 Signature manifestations (eCFR, Title 21 up to date as of 15 October 2026). | US records that fall under Part 11. Everyday TRUSTED work is usually outside it. Applied here only as good practice: a clearance names the person, the role, the date and what the clearance means. | Confirmed from eCFR on 20 October 2026. |

### How to use these rules in output

- Explain the practice in plain words: "the record names who cleared it, in what role,
  on what date and what the clearance covers". Do not cite R3 or R4 to a daily user as a
  requirement for their email or deck; they are US rules for specific regulated records.
- Never say a record "meets Part 11" or "is ALCOA compliant" (TR-H3). The skill does not
  establish either.
- R1 supports the habit of citing the original paper rather than a congress abstract or
  a secondary summary, and of not citing a retracted paper. The retraction check itself
  is `source-assessment`.
- Company procedures for records, sign-off and review come first (TR-H11). These rules
  describe good practice underneath them.

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it
breaks. All examples are invented for teaching; no real product, study or person.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

### Contents

- Citations C1–C5
- Record C6–C12

### Citations

**C1 The filled-in year.** A source supplied without a year gets one from memory or
from a similar paper.
Why: the reviewer looks up the reference and finds a different year, or none; every
other line in the list is then doubted.
Before: "Okafor A, Lind M. Home monitoring in condition X. Congress abstract. 2025."
(No year was supplied.)
After: the line without a year, and after the list: "The Okafor and Lind abstract has
no year in what you gave me. Add it from the congress program if you have it." (TR-H1,
R1)

**C2 The caption.** A label is put before the reference line.
Why: a caption adds text the reader takes as part of the reference, and implies a tool
produced the line.
Before: "Reference (as returned by the citation tool): Ferreira, L. ..."
After: "Ferreira, L. ..." (the line, alone). (TR-H13)

**C3 The chosen style.** The assistant picks a style when the person named none.
Why: it overrides the style the person's team uses, so the list does not match the rest
of their documents.
Before: lines written in Chicago though the person said only "format the references".
After: plain lines in one consistent order, and a note that no style was named. (TR-H7)

**C4 The citation as proof.** A reference list is presented as showing the claims are
backed up.
Why: a reference says where a statement came from, not that the source says it. The
reader stops checking.
Before: "All six claims are referenced, so the summary is fully supported."
After: "Six claims carry a reference. Whether each source says what the text says is a
separate check; I can run it." (TR-H3, R1)

**C5 The hand-made line passed off as tool-checked.** Reference lines are presented as
if a tool built or checked them.
Why: the person will tell their reviewer the references were tool-checked.
Before: "Citations checked with a citation tool: ..." (none was used.)
After: the lines, then "Reference lines built from the details you gave; not
tool-checked." (TR-H4)

### Record

**C6 The name nobody gave.** A clearer's name is taken from the document's author
line, an email signature or a meeting list.
Why: that person has not agreed to stand behind the work. Their name on the record is
a false statement about them.
Before: "Cleared by: Dr. M. Brandt" (the person never named a clearer; Dr. Brandt is
the author of a cited paper).
After: "Uncleared draft (to be cleared by a reviewer not named yet)." (TR-H5)

**C7 The future signature.** "Put my manager's name as cleared_by, she'll sign it
later."
Why: a clearance records a decision that was made. The manager has not reviewed it.
Before: "Cleared by: Dana Reyes, Head of Market Access."
After: "Uncleared draft (to be cleared by Dana Reyes, Head of Market Access)", as you told me. (TR-H5)

**C8 The tool as clearer.** A tool, the model or the assistant is put in the
clearer field.
Why: accountability sits with people. A record note must not carry a tool or an
assistant as clearer.
Before: "Cleared by: a tool" / "Cleared by: AI assistant".
After: a person's name the owner gave, or "Uncleared draft". (TR-H5)

**C9 A found passage as clearance.** Every claim was found in its passage, so the record is written
as cleared.
Why: finding a passage is a hand comparison. Clearance is a person's decision.
Before: "All 12 claims found in their passages. Record cleared."
After: "Uncleared draft. 12 claims found in your passages, not tool-checked. To be
cleared by: [name]." (TR-H3, TR-H5)

**C10 The disagreement smoothed over.** A claim whose passage says something different is softened in wording
and recorded as cleared, or left out of the open items.
Why: the passage says something different. The reviewer who finds it later finds a
record that hid it.
Before: claim "reduced visits by half"; passage "visits fell from 4.1 to 3.2 per
patient-year"; record lists it as cleared.
After: listed as an open item with the passage quoted and one question: "The passage
gives 4.1 to 3.2, which is not half. Revise to the passage's figures, remove, or send
to your medical review process?" (TR-H5, TR-H11)

**C11 The silent drop.** A claim is taken out of the text to avoid an open item, and
the record does not say so.
Why: the record no longer matches what was checked; the next reader cannot see what
changed.
After: the claim is recorded as removed, with the date and who decided. (TR-H5, R3)

**C12 The unrequested table, the jargon handover.** A table of claims and results is printed by default, or open items are handed on in codes ("escalate to CF04
gate, your passage says something different").
Why: daily users read the open items, not a status matrix; the table is for the person
who asks for it.
After: open items in plain sentences; the evidence table only on request. (TR-H13)

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/gap-rules.md`.

Same format and classes as every TRUSTED skill:
`[GAP: <class>; <what is missing>; <what would close it>]`

In what the person reads, including the reference list and the record note, a gap is a
plain sentence ("The second source has no year in what you gave me; I left it out"), as
`../templates/reference-list.md` shows. The bracketed form appears only inside a drafted
deliverable, such as a revised slide text.

| Class | Typical case in this skill |
|---|---|
| `not supplied` | A reference detail (year, pages, identifier, author) the person did not give; the clearer's role or the decision date |
| `not checkable here` | Something only a tool or a lookup could settle, such as whether a newer version of a source exists. The gap says what the person could check |
| `conflicting` | Two supplied sources disagree; a claim's passage says something different; two versions of the same source give different details |
| `needs a decision` | No named clearer; an open item without a decision; a policy question for the AI use policy owner |
| `out of date or unclear date` | A cited source flagged as retracted, corrected or superseded, or with no date |

### Wording rules

- Name the exact item: "year of the Okafor and Lind abstract", not "missing metadata".
- Never hint at a value inside a gap ("probably 2024").
- A missing clearer is `needs a decision`. The record note and a drafted deliverable both
  say "Uncleared draft (to be cleared by a reviewer not named yet)", never a placeholder
  name. Only a person who has cleared the work, with role and date, goes after "Cleared
  by"; someone who will review it later goes in "Uncleared draft (to be cleared by
  <name>, <role if given>)", as the person told you; a clearance reported in the past
  without role or date goes in "Uncleared draft (you said <name> cleared it; add role and
  date to record the clearance)" (`../../work-record/templates/status-line.md`).

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-CR-01 | Invented clearer | Was a named clearer fabricated? | Record | TR-H5 | VERIFIED practice |
| FM-CR-02 | Refs conflated with support | Were Chicago lines used as claim-support statuses? | Surfaces | VITAL citation gold standard | VERIFIED practice |
| FM-CR-03 | Gaps dropped on stamp | Was the record stamped complete with open gaps? | Honesty | TRUSTED citation-and-record | [CHECK] |
| FM-CR-04 | Detail supplied by the assistant | Does any reference line hold a year, page, identifier or access date the person did not give? | Honesty | TR-H1 | VERIFIED practice |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
