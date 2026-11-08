# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it
breaks. All examples are invented for teaching; no real product, study or person.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

## Contents

- Citations C1–C5
- Record C6–C12

## Citations

**C1 The filled-in year.** A source supplied without a year gets one from memory or
from a similar paper.
Why: the reviewer looks up the reference and finds a different year, or none; every
other line in the list is then doubted.
Before: "Okafor A, Lind M. Home monitoring in condition X. Congress abstract. 2025."
(No year was supplied.)
After: the line without a year, and after the list: "The Okafor and Lind abstract has
no year in what you gave me. Add it from the congress program if you have it." (TR-H1,
R1)

**C2 The caption.** A label is put before the citation line.
Why: VERIFY's line is meant to be pasted as the reference itself; a caption adds text
the reader takes as part of the reference, and announces the tool to an external
reader.
Before: "Reference (as returned by VERIFY): Ferreira, L. ..."
After: "Ferreira, L. ..." (the returned line, alone). (TR-H13)

**C3 The chosen style.** The assistant picks Chicago or Harvard when the person named
none.
Why: it overrides the preference the person's team set on their key, so the list does
not match the rest of their documents.
Before: `build_citation` called with `style: "chicago"` though the person said only
"format the references".
After: style left out. (TR-H7)

**C4 The citation as proof.** A reference list is presented as showing the claims are
backed up.
Why: a reference says where a statement came from, not that the source says it. The
reader stops checking.
Before: "All six claims are referenced, so the summary is fully supported."
After: "Six claims carry a reference. Whether each source says what the text says is a
separate check; I can run it." (TR-H3, R1)

**C5 The hand-made line passed off as tool-built.** Without VERIFY, plain lines are
presented as if VERIFY built them, or a missing VERIFY result is described.
Why: the person will tell their reviewer the references were tool-built.
Before: "Citations built with VERIFY: ..." (VERIFY is not connected.)
After: the lines, then "Reference lines built from the details you gave; not
tool-built." (TR-H4)

## Record

**C6 The name nobody gave.** A clearer's name is taken from the document's author
line, an email signature or a meeting list.
Why: that person has not agreed to stand behind the work. Their name on the record is
a false statement about them.
Before: "Cleared by: Dr. M. Brandt" (the person never named a clearer; Dr. Brandt is
the author of a cited paper).
After: "Uncleared draft. To be cleared by: [name of the person who reviews it]." (TR-H5)

**C7 The future signature.** "Put my manager's name as cleared_by, she'll sign it
later."
Why: a clearance records a decision that was made. The manager has not reviewed it.
Before: "Cleared by: Dana Reyes, Head of Market Access."
After: "Uncleared draft. To be cleared by: Dana Reyes, Head of Market Access." (TR-H5)

**C8 The tool as clearer.** The connector, the model or the assistant is put in the
clearer field.
Why: accountability sits with people. VERIFY refuses such a record; a hand-made note
must not carry one either.
Before: "Cleared by: VERIFY" / "Cleared by: AI assistant".
After: a person's name the owner gave, or "Uncleared draft". (TR-H5)

**C9 Support as clearance.** Every claim came back supported, so the record is written
as cleared.
Why: support is overlap with a quoted passage. Clearance is a person's decision.
Before: "All 12 claims supported. Record cleared."
After: "Uncleared draft. 12 claims supported by their quoted passages. To be cleared
by: [name]." (TR-H3, TR-H5)

**C10 The contradiction smoothed over.** A contradicted claim is softened in wording
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

**C12 The unrequested table, the jargon handover.** A table of claims, statuses and
tiers is printed by default, or open items are handed on in codes ("escalate to CF04
gate, status CONTRADICTED").
Why: daily users read the open items, not a status matrix; the table is for the person
who asks for it.
After: open items in plain sentences; the evidence table only on request. (TR-H13)
