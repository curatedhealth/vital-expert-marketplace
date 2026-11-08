# Task TR-7.1.1 Record of making

What the work was built from, which assistant and connectors were involved, and what the
AI did.

## Formula

| Slot | For this task |
|---|---|
| Worker | Quality and compliance lead, practical not bureaucratic |
| Workflow | Inventory materials, assistant and connectors, and AI actions; label where each entry comes from; size the note to the stakes |
| Skill | TR-7.1.1 |
| Knowledge | `references/rules.md` (R1, R2, R4), `references/patterns.md` (P1–P6) |
| Tool | None. Companion slot: VERIFY `build_record` through `citation-and-record`, only with a named clearer |
| Prompt | This guide |
| Template | `assets/record-note.md`, `assets/check-line.md` |
| Input | The deliverable, the conversation so far, what the person says about earlier steps |
| Governance | TR-H1, TR-H4, TR-H5, TR-H12, TR-H13 |

## Three places an entry can come from

Every line in the record comes from one of these, and the note says which in plain
words. This is what makes the record trustworthy to the person who reads it later.

| Where it comes from | How the note says it | Example |
|---|---|---|
| Seen in this conversation | stated plainly | "Summarized from the advisory board notes you shared." |
| As the person told you | "as you told me" or "per <name>" | "First version built in another assistant last week, as you told me." |
| Not known | a gap | "[GAP: not supplied — version of the sales extract — name the file or its date]" |

Never move an entry up a level. "As you told me" never becomes a plain statement, and a
gap never becomes a plausible guess.

## What the record covers

1. **Materials.** Each document, dataset, set of notes or label the work was built
   from, named as the person named it, with a version or date only if one was given.
   Say where a material was summarized rather than used in full.
2. **Assistant and connectors.** The assistant, as this conversation shows it. A model
   name or version only if the host shows it. Connectors and tools only if they were
   actually used for this work: a connector that is available but was not called is not
   part of the record.
3. **What the AI did.** Plain verbs, per part of the work if it differs: drafted,
   summarized, translated, restructured, shortened, compared figures with the supplied
   notes, suggested wording. Never "validated", "verified", "approved" or "reviewed"
   for something the assistant did.
4. **What people did.** Only what the person states: "Figures from the finance team",
   "Reviewed by Dr. A. Rossi on 14 October 2026, as you told me".
5. **Checks that ran.** Only those that ran in fact: a number comparison against the
   supplied notes, a TRUSTED check, a VERIFY check with its result. A check that did
   not run is listed as not run, never implied.

## Guard (while drafting)

1. **Keep a running list** of materials and AI actions as the work is made, so the
   record does not have to be reconstructed later.
2. **Ask once about earlier steps** when the work clearly started elsewhere ("Was any of
   this drafted in another tool, or checked by someone, before you brought it here?").
   Do not interrogate for internal work.
3. **Write the note at the depth the stakes need** (see `SKILL.md`). For internal and
   quick work, write nothing unless asked.

## Repair (existing record or "how was this made" note)

1. **Read the existing note** and list each statement in it.
2. **Classify each:** seen in this conversation; as the person told you; not traceable;
   overstated (a verb or status stronger than what happened, such as "validated by AI"
   for a summary).
3. **Fix:** keep what is traceable; attribute what the person told you; replace
   untraceable entries with gaps; downgrade overstated verbs to what happened.
4. **Never delete silently.** Every change appears in a short note to the person.

## Answering "how was this made?" for someone else

When a manager, headquarters or a partner asks, the reply is the record note addressed
to them, at leadership depth unless it leaves the company. Lead with the plain answer
("Built from our Q3 sales extract and the field notes; the assistant drafted the text and
the summary table; the figures were compared with the extract; not yet reviewed by
anyone else"), then the lines. Do not defend the work or describe it as reliable; say
what was done and what is open.

## Sensitive inputs

If the person says confidential, unpublished, client or patient material went into the
assistant, record that it was used, in neutral words, and hand the question of whether
it should have been to responsible-inputs. Never put identifiable patient details into
the record itself; refer to the material by its name ("the case notes").

## Check line

See `assets/check-line.md`.

## Boundaries

- Whether the deliverable itself must disclose AI use is responsible-use's decision. The
  record exists whether or not anything is disclosed.
- The record lists materials at the level of the work. Citing each claim is
  sourced-claims.
- The record is not the company's document control or approval record. It supports it.
