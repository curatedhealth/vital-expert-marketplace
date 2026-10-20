# Task TR-2.2.3 Privacy in the output

## Formula

| Slot | For this task |
|---|---|
| Worker | Regulatory and promotional reviewer with a privacy background |
| Workflow | Find details that could point to a person, keep them out of the output, remove, generalize or aggregate, say what was done without calling the result anonymous, point to the privacy function |
| Skill | TR-2.2.3 |
| Knowledge | `references/rules.md` (P1 to P7), `references/patterns.md` (D1 to D9) |
| Tool | `scripts/scan_output.py --data` where code can run. Companion slot: none yet |
| Prompt | This guide |
| Template | `assets/privacy-note.md`, `assets/check-line.md` |
| Input | The draft, the material it was written from, the context card (reader, market, stakes) |
| Governance | TR-H1, TR-H3, TR-H6, TR-H11, `references/governance.md` |

## What to look for

Personal data is anything that relates to a person who can be identified directly or
indirectly (P1). Removing the name is not enough when other details still point to the
person (P2).

| Kind | Typical signs in life-sciences output |
|---|---|
| Direct identifiers | Names, initials, record or subject numbers, contact details, photos |
| Indirect identifiers | Age with a place or a date, a small village, a job, a hospital and an admission month, a rare condition in a small region |
| Case stories | A payer's or doctor's account of one patient, a testimonial, a case study in a deck |
| Small numbers | "2 patients in canton X", a table cell of 1 to a few, a subgroup that is one hospital's patients |
| Health details | Any of the above with a diagnosis, treatment, admission or outcome (P3, P4) |
| People who are not patients | Named doctors, pharmacists, payer staff, with what they said or prescribed |

This task covers the output: what the draft, the reply, the note and the check line
would show. What went into the assistant is `responsible-inputs`; run both when patient
details arrived in the material.

## Guard (while drafting)

1. **Read the material for people before drafting.** Note each detail that could point
   to someone. Do not write them down in the reply.
2. **Ask what the job needs.** Most work needs the point of the case, not the person: "the
   payer raised a patient case about hospital costs in year 2".
3. **Choose the lightest route that does the job**, in this order:
   - **Leave out**: the case is not needed for the purpose.
   - **Describe generically**: "a patient on treatment since the summer" with no age,
     place or dates.
   - **Generalize**: age band instead of age, region instead of village, quarter instead
     of date.
   - **Aggregate**: counts across groups large enough that no one is singled out. Where a
     count is small, ask the person what minimum their privacy function sets
     (`[GAP: needs a decision — minimum count to show — your data privacy function]`);
     never set the number yourself (P6).
4. **Keep named professionals out** unless the person confirms they agreed to be named
   for this use. Attribute views to a role ("a payer pharmacist") instead.
5. **Never write the details back**, in the draft, the note, the check line or a gap.

## Repair (existing draft)

1. **List each detail** that could point to a person. Where code can run, use
   `scripts/scan_output.py <draft.txt> --data` for formats (titles with names, dates,
   ages, small counts), then read the text: names without a title, places and stories
   are not found by a scan.
2. **Apply the routes above** to each one, the lightest that keeps the meaning.
3. **Say what was done in plain words**: "I took out the patient's name, age, village
   and the month of the hospital stay." Never say the result is anonymous, anonymized
   or de-identified, and never say it is now fine to share (TR-H3, TR-H6).
4. **Point to the privacy function** when the work leaves the company or a case story is
   needed in it: they decide whether the result can be used and whether consent or
   another basis is needed.
5. **If the material describes something that happened to a patient on a product**
   (a hospital stay, a side effect), note in one line that it may need to go to the
   safety reporting procedure. Do not judge whether it is related or reportable
   (TR-H6); that is `patient-safety` and the safety function.

## Check line

See `assets/check-line.md`. The line counts items; it never quotes them.

## Boundaries

- Never decide that data is anonymous, that a count is small enough, that consent
  exists, that a transfer is permitted, or that an incident occurred (TR-H6). Name the
  privacy function.
- A US de-identification checklist (P5) is a list of what to take out. It does not make
  the text de-identified, and it is not the EU or Swiss test (P2, P4).
- Runs at every depth, including a quick internal email, because a copy of the output
  travels further than the person intends.
