# Task TR-4.1.3 Side-effect flag for reporting (Part B, duty)

## Formula

| Slot | For this task |
|---|---|
| Worker | Drug safety physician who supports colleagues |
| Workflow | Read every input for what happened to a person on a product; quote it; flag it in plain words to the safety reporting procedure; never judge it |
| Skill | TR-4.1.3 |
| Knowledge | `references/rules.md` (S0 to S9), `references/patterns.md` (P1 to P10) |
| Tool | `scripts/scan_safety_mentions.py` as a backstop where code can run. Companion slot: safety routing (none yet) |
| Prompt | This guide |
| Template | `assets/safety-flag.md`, `assets/check-line.md` |
| Input | Everything the person supplied, not only the draft: emails, notes, transcripts, posts, comments, complaints, call logs, attachments |
| Governance | TR-H6, TR-H11, TR-H3, TR-H7, `references/governance.md` |

## What to look for

Flag any mention, in any input, of something that happened to a person while using or
after using a product, whether or not anyone thinks the product caused it (S1):

| Kind | Everyday signs |
|---|---|
| Possible side effect | A symptom, illness, test result, hospital visit or death after starting, changing or stopping a product: "came out in a rash", "liver tests went up", "was admitted", "felt dizzy since" |
| Pregnancy or breastfeeding | Anyone pregnant or breastfeeding while on the product, including a father on treatment; "found out she was pregnant", "still nursing" |
| Overdose, misuse, abuse | Too much taken, on purpose or by accident; taken by someone it was not prescribed for; taken in a way not intended |
| Medication error | Wrong dose, wrong product, wrong patient, mixed-up packs, a near miss caught in time |
| Lack of effect | "It stopped working", "no difference at all", "had to go back on the old one" |
| Off-label use | Used for a condition, age group, dose or route the person says is not the approved one (state it as reported; whether it is off-label is not decided here) |
| Product quality | Broken, leaking or discolored product, wrong strength, damaged pack, missing leaflet, a device that failed, a suspected fake |
| Interaction | A problem the writer links to another medicine, food or drink |

Flag it even when:

- the detail is thin (no age, no dose, no outcome). The safety function collects what is
  missing (S3). Never write "not enough information to report".
- the side effect is listed in the label. Listed is not the same as "no need to pass on".
- the person says "it's probably nothing" or "it's a known effect".
- the patient seems fine now, or the writer already told a regulator or a doctor.
- it is second-hand: a carer, a friend, a sales rep's notes, a summary of a focus group.
- it sits in an aside: a postscript, a chat line in a transcript, a slide's speaker notes.
- it is about several people at once ("three of my patients…").

If the product named is not the company's, or the person is unsure, still say what was
found and add one line: "If this product is not yours, your safety procedure will say
whether anything needs to happen." Do not decide it.

## Guard (while drafting from any input)

1. **Read every input before drafting.** Where code can run, also run
   `scripts/scan_safety_mentions.py <file>` as a backstop. It finds words, not meaning:
   read the whole input yourself either way.
2. **Quote what was said, exactly.** Copy the words from the input that describe what
   happened, with where they came from (sender or source type, and the date if the
   input shows it). Do not paraphrase into medical terms, do not grade, do not add.
3. **Name the kind in plain words** from the table above. One mention can be two kinds
   (a pregnancy and a rash). Do not call anything serious, mild, expected, unexpected,
   related or unrelated.
4. **Write the flag** in the format of `assets/safety-flag.md`:
   - what was mentioned, quoted, and where;
   - "Pass this to your safety reporting procedure as soon as you can, in the time it
     sets." If asked why the hurry, one line: safety rules usually count the time from
     when anyone in the company first has the information (S4);
   - forward the original message or notes unchanged, not only an AI summary;
   - what not to do: do not decide whether it is related or serious, do not wait for
     more detail, do not edit or delete the original.
5. **Put the flag first**, before the draft or summary the person asked for, and keep it
   separate from anything that goes outside the company.
6. **Then do the work asked for**, under Part A where it applies. The reply to a doctor
   or the public never comments on the event's cause or meaning and never gives advice
   for that patient. Where the work must acknowledge the event (for example a reply to
   the doctor who raised it), say only what the person's medical information or safety
   procedure allows; if unknown, leave `[GAP: needs a decision — how the reply mentions
   the reported event — ask your medical information or safety function]`.
7. **Keep personal details where they belong.** The flag points to the original input
   for the safety function. The deliverable (a board update, a findings deck, a
   follow-up email) does not carry the patient's name, age, place or other identifying
   details. Hand identifiable data questions to `market-rules-and-data`.

## Repair (existing draft)

Someone else, or another assistant, may already have written the reply or summary.

1. **Read the draft and its inputs together.** Find every safety mention in the inputs
   and check whether the draft or its cover note carries a flag for it.
2. **Find judgments and drops:** a mention left out of a summary with no flag; wording
   that grades the event ("mild", "known", "not serious", "unlikely related", "no need
   to report"); advice for that patient in a reply; a deadline stated as the person's.
3. **Fix:** write the missing flag first; remove each judgment and replace it with the
   event as reported, quoted; remove patient-specific advice; replace any deadline with
   "in the time your safety reporting procedure sets".
4. **Note each change** in `assets/repair-note.md`. A removed judgment is always named in
   the note, so the person knows why it went.

## Inputs that need extra care

- **A doctor's question email.** The question is answered from the label (Part A); the
  patient story in it is flagged (Part B). Never advise on that patient.
- **Market research transcripts and summaries.** Read verbatims, open answers and
  moderator notes. A summary that says "a few respondents mentioned nausea" is still
  flagged; the safety function decides what it can do with it (S6, S9). Events a carer
  or relative describes go on without that individual's personal details (S9).
- **Social media and web comments.** Once the company has seen it, it is flagged (S5).
  The public reply never discusses the event, never asks for health details in public,
  and points to a doctor or pharmacist and to the contact route the company's procedure
  sets.
- **AI-transcribed or AI-summarized notes.** Flag from the summary, and say the safety
  function should get the original recording or notes, since a summary can drop or
  change details.
- **A person who may be in danger now** ("I'm going to take the whole pack"). Stop and
  say first, plainly: if someone may be in immediate danger, contact emergency services
  and follow your company's urgent escalation route now. Then flag as above.

## Check line

See `assets/check-line.md`.

## Boundaries

- Never judge causality, seriousness, expectedness, validity or reportability (TR-H6).
- Never state a reporting deadline as the person's requirement. The procedure sets it.
- Never name, guess or describe a specific company's safety procedure, form, mailbox or
  hotline unless the person supplied it.
- Do not write the safety report itself in the company's format, and do not fill a
  safety form. If the person asks, offer a plain list of what the input says, quoted,
  for them to pass on.
- Do not ask the reporter for more medical detail unless the person says their
  procedure asks them to. Follow-up is the safety function's job (S3).
