# Task TR-4.1.2 Patient safety language (Part A, content)

## Formula

| Slot | For this task |
|---|---|
| Worker | Drug safety physician who supports colleagues |
| Workflow | Read the piece as the patient would; remove advice, false reassurance and scare framing; make sure there is always a route to a doctor, nurse or pharmacist |
| Skill | TR-4.1.2 |
| Knowledge | `references/rules.md` (S10, S13 to S15), `references/patterns.md` (L1 to L9) |
| Tool | `scripts/scan_safety_mentions.py --patient` where code can run. Companion slot: none yet |
| Prompt | This guide |
| Template | `assets/repair-note.md`, `assets/check-line.md` |
| Input | The patient-facing draft (leaflet, web page, app text, social reply, support program script, email to a patient), the supplied patient leaflet or label, the market |
| Governance | TR-H6, TR-H1, TR-H11, TR-H13 |

## Who counts as a patient reader

Patients, carers, family members and the public, wherever they read it: a leaflet, a
website, a social media reply, a patient support program call script, an app screen, a
letter. When unsure whether the public will see it, ask once.

## The four checks

| Check | What it looks like | What it should be |
|---|---|---|
| No advice | An instruction about this person's treatment that the patient leaflet does not give: "you can stop once you feel better", "take two if you miss one", "it's fine with alcohol", "no need to see your doctor" | Only instructions the supplied leaflet gives, quoted; anything else is "ask your doctor or pharmacist" |
| No false reassurance | "Completely safe", "no side effects", "nothing to worry about", "gentle", "natural so harmless", "everyone tolerates it" | Say what the leaflet says about side effects; never a comfort the leaflet does not give |
| No scare framing | Vivid or alarming wording meant to push action: "deadly", "your kidneys could fail if you skip a dose", fear used to drive adherence or uptake | Calm, factual wording from the leaflet, with what to do and whom to ask |
| A route to a clinician | No line telling the reader who to ask when unsure, when something feels wrong, or before changing anything | At least one clear line naming a doctor, nurse or pharmacist; where the leaflet tells patients how to report side effects, keep that |

## Guard (while drafting)

1. **Start from the patient leaflet** if one was supplied; quote its safety wording.
   If none was supplied and the piece needs safety content, ask for it, or leave
   `[GAP: not supplied — patient leaflet wording on <x> — supply the approved leaflet]`.
2. **Write no instruction the leaflet does not give.** Questions about a person's own
   treatment are answered with "ask your doctor, nurse or pharmacist".
3. **Put the route in.** At least one plain line, near the safety content: "If you have
   any questions, or if something does not feel right, talk to your doctor, nurse or
   pharmacist." Keep any side-effect reporting line the leaflet or the person supplied.
   Do not invent a phone number, website or reporting scheme.
4. **Keep urgent symptoms as the leaflet states them.** If the leaflet says "seek medical
   help immediately if…", quote it exactly. Do not add or remove symptoms.
5. **Keep the tone level.** No comfort beyond the leaflet, no fear beyond the leaflet.
6. **Plain words without new meaning.** Simplifying is `fit-for-reader`'s job; if a
   simplified sentence changes a safety meaning, keep the leaflet wording and say why.

## Repair (existing draft)

1. **Read it as the patient.** Where code can run, `scripts/scan_safety_mentions.py
   --patient <draft.txt>` lists reassurance, advice and alarm phrases and whether a route
   to a clinician appears. Read the whole text either way: the scan misses paraphrases.
2. **Mark each passage:** advice not in the leaflet; reassurance not in the leaflet;
   alarming framing; route to a clinician missing; safety statement changed from the
   leaflet (send to `tasks/clinical-safety-statements.md`).
3. **Fix:** remove or replace advice with "ask your doctor or pharmacist"; replace
   reassurance with the leaflet's wording; calm the framing; add the route line.
4. **Note each change** in `assets/repair-note.md`. Patient material always goes to the
   company's patient material review and promotional review process next (TR-H11).

## Replies to the public about a side effect

When a patient or member of the public describes a side effect (in a comment, a message,
an email), Part B runs first (`tasks/side-effect-flag.md`). The reply:

- thanks them ("thank you for letting us know"), with any further wording only as the
  person's procedure allows;
- does not discuss whether the product caused it, whether it is common or known, or what
  they should do about their treatment;
- does not ask for health details in public;
- tells them to talk to their doctor or pharmacist;
- gives the company's contact route for safety reports only if the person supplied it;
  otherwise `[GAP: needs a decision — contact route for this reply — from your safety
  reporting procedure or social media procedure]`.

## Check line

See `assets/check-line.md`.

## Boundaries

- Reading level, jargon and format are `fit-for-reader`; this task changes wording only
  where safety meaning is at stake.
- Whether patient material may be published at all is `claims-and-label` and
  `market-rules-and-data`, then the company's review.
- Never tell a patient what to do about their own treatment (TR-H6).
