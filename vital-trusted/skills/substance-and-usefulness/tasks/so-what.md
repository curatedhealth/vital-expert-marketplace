# Task TR-1.1.3 So what

## Formula

| Slot | For this task |
|---|---|
| Worker | Senior editor and engagement lead |
| Workflow | Name the reader's job, find sections that list facts with no implication, draw the implication from the material or ask |
| Skill | TR-1.1.3 |
| Knowledge | `references/patterns.md` (W1–W5) |
| Tool | None. Companion slot: none yet |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/repair-note.md` |
| Input | The draft, the supplied material, the context card (reader, deliverable, stakes) |
| Governance | TR-H1, TR-H2, TR-H5, TR-H6, TR-H7 |

## What the "so what" is

The sentence that tells this reader what the facts mean for their job: what changes,
what is at risk, what they should watch or decide. A competitor summary for a brand team
asks "what does this mean for our plan?"; the same facts for the board ask "does this
change the forecast or the investment case?".

A section has no "so what" when it lists facts and stops, and the reader would have to
work out the implication alone.

## Guard (while drafting)

1. **Name the reader and their job** from the context card or the request: "brand team,
   preparing the 2027 plan", "board, deciding whether to fund the second indication". If
   neither shows it, ask once.
2. **After each group of facts, write the implication for that job**, in one or two
   sentences, and put it first where the reader skims: the finding, then the facts that
   support it.
3. **Draw only what the facts support.** Use the material's own facts and the person's
   stated plan or goal. Word it as a reading: "This puts our Q1 listing ahead of
   Competitor B's", not "Competitor B will lose share".
4. **Keep inference visible.** Where the implication depends on an assumption, name it:
   "If their launch date holds, …". Where it needs a fact the material does not hold,
   write the gap.
5. **When the implication is a judgment only the person can make** (strategy, budget,
   priority), offer it as a question or a labeled proposal for them to confirm.

## Repair (existing draft)

1. **Mark each section** that lists facts without saying what they mean for the reader.
2. **For each one, draft the "so what"** from the facts in that section and the reader's
   job. If no implication follows from what is there, say so in the note rather than
   writing one.
3. **Check the new sentence does not add a fact, cause or forecast** the material does
   not hold (`references/patterns.md` W3, W4). If True is active, it is passed to
   `grounded-statements` like any new sentence.
4. **Move the "so what" to the top** of its section when the reader skims (board papers,
   slide headlines, email openings).
5. **List each added implication** in the repair note as "added, for you to confirm",
   because it is the assistant's reading of the person's facts.

## In medical and safety material

The "so what" of a study summary for a medical team is what the result means for the
evidence base and the team's next step (for example, "the primary endpoint was missed,
so the secondary results need careful framing in the advisory board pre-read"). It is
never what a prescriber should do for a patient, never a causality judgment about a
side effect and never a call on whether something must be reported (TR-H6). Name the
function that decides.

## Check line

Counts feed the substance line in `assets/check-line.md`: sections with no "so what".

## Boundaries

- A "so what" that changes the balance of benefits and risks is Unbiased
  (`balanced-evidence`, `honest-framing`). A "so what" that states a cause or a forecast
  the material does not hold is True (`grounded-statements`).
- In promotional or external material, a new implication can become a claim. Keep it
  within the material and point to the review process (TR-H11).
