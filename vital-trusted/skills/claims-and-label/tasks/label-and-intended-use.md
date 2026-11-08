# Task TR-2.1.1 Label and intended-use boundary

Keeps every product statement inside the approved indication, population, dose, line
of therapy, setting and label wording of a medicine, or the intended purpose of a
device or app, as the person supplied it for the market the work is for.

## Formula

| Slot | For this task |
|---|---|
| Worker | Regulatory and promotional reviewer who helps drafts through review |
| Workflow | Get the label, list its boundary, compare each product statement, rewrite inside it or mark the gap |
| Skill | TR-2.1.1 |
| Knowledge | `references/rules.md` (R1, R2, R4 to R8, R25 to R27), `references/patterns.md` (L1–L8) |
| Tool | None. Companion slot: a future label-source companion (`references/tools.md`) |
| Prompt | This guide |
| Template | `assets/label-request.md`, `assets/claims-note.md`, `assets/check-line.md` |
| Input | The request, the draft, the supplied label or intended-purpose statement, the context card (market, reader, product status) |
| Governance | TR-H1, TR-H3, TR-H6, TR-H7, TR-H11 |

## What the label sets

From the supplied label, write down the boundary in a few lines before drafting. Use
the label's own words.

| Boundary | For a medicine | For a device or app |
|---|---|---|
| What it is for | Indication, as worded | Intended purpose, as worded |
| Who | Population: age, severity, subtype, biomarker, prior therapy | Intended users and patient population |
| How | Dose, route, frequency, duration, combination or monotherapy | Use conditions, setting (home, clinic), who interprets the output |
| Where | Market and label version or date | Market, and the conformity or clearance status as the person states it |
| What it does not do | Contraindications, limits of use stated in the label | Functions it does not have; whether it diagnoses, monitors or only records; whether a clinician must confirm |

If the label was not supplied, ask for it (`assets/label-request.md`). If the person
says the product is not approved in this market, or is investigational, it is not
promoted there at all (R1, R5, R6, R7, R8); route to the promotional boundary task.

## What to look for

Any of these, when it goes beyond the boundary:

- a patient group the label does not name (age, severity, subtype, line of therapy,
  setting, pregnancy, children)
- a use: a different condition, a prevention use for a treatment label, a combination
  or monotherapy the label does not give
- a dose, frequency or duration different from the label
- an outcome the label does not support ("cures", "reverses", "prevents relapse")
- an implied use: wording that points to a group or use without naming it (pattern L3)
- a paraphrase that widens the label's wording (pattern L4)
- for a device or app: a verb that ascribes a function it does not have ("diagnoses",
  "detects", "predicts", "rules out", "replaces a visit"), or a user or setting outside
  the intended purpose (pattern L7)

`scripts/find_claim_cues.py` lists the use, population and absolute wording in a
longer draft. It finds words, not uses: read the draft against the label as well.

## Guard (while drafting)

1. **Write the boundary first**, from the label, in its own words.
2. **Draft each product statement from the boundary.** Indication, population, dose and
   setting keep the label's wording; plain language is fine around them.
3. **When the request wants a use beyond the label** ("add a message for teenagers",
   "say it works for mild cases too"), do not write it. Say in one plain line that the
   label supplied does not cover it, and offer what can be said instead.
4. **When the request reports practice** ("doctors are already using it for…"), treat
   it as a field insight, not a message. Questions doctors raise go to the medical
   information procedure; the brand message stays inside the label.
5. **For a device or app**, describe what it does in the terms of the intended purpose:
   what it records, measures or shows, who interprets it, and when to see a clinician.

## Repair (existing draft)

1. **List each product statement** and set it against the boundary.
2. **Classify:** inside the label wording; inside but reworded so it reads wider; beyond
   the label; cannot tell (label silent or not supplied).
3. **Fix:** keep what is inside; restore reworded statements to the label's wording;
   rewrite beyond-label statements to the label's scope, or remove them and say why;
   mark "cannot tell" as a gap and ask.
4. **Never delete silently.** Every change appears in the claims note.
5. **If no label was supplied**, do not judge statements as beyond the label. Mark them
   not checkable and ask for the label.

## "It's approved in the US, so it's fine here"

Approvals differ by market and date. Ask which market the piece is for and work from
that market's label. If two labels were supplied and they differ, mark the difference
`[GAP: conflicting — …]` and use the stricter wording until the person decides.

## Check line

See `assets/check-line.md`.

## Boundaries

- This task compares the draft with the label the person supplied. It does not decide
  what the product is approved for, whether the supplied label is current, or whether a
  use is lawful (TR-H6). Those are `[GAP: not checkable here]` or questions for the
  review process.
- Dosing, contraindications and warnings stated in the draft are checked for wording
  against the label here; whether they are stated safely and completely is
  `patient-safety`.
- Whether an app or software is a medical device at all is a regulatory determination.
  Work from the intended purpose the person supplies; if there is none, ask (TR-H6,
  TR-H7).
- No clinical advice on any use, inside or outside the label (TR-H6).
