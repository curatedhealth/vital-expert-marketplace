# Rendered example: patient letter repair (sourced draft)

Invented teaching case only ("Medicine X", figures fictional). Shape of a full bundle after
`fit-for-reader` repair: patient-facing text, reader card, repair note, gap list, check-line stamp.

## Context

- **Reader:** Adult patient starting Medicine X (supplied clinician memo).
- **Deliverable:** One-page patient letter (asked for).
- **Material supplied:** Internal memo: Medicine X 50 mg once daily with food; nausea in
  about 1 in 10 people; severe allergic reaction rare; call doctor if rash or swelling;
  do not stop without talking to your doctor.

## Reader card (`templates/reader-card.md`)

```text
Reader: patient (adult, lay)
Decides: whether to start Medicine X and when to call the doctor
Depth: what the medicine is for, how to take it, common and serious side effects, next step
Vocabulary: everyday words; medical term only with plain explanation
```

## Fixed patient letter (person-facing)

> **Starting Medicine X**
>
> Your doctor has prescribed Medicine X to help with [GAP: indication wording not supplied —
> use approved patient wording from your label team].
>
> **How to take it.** Take one 50 mg tablet once a day with food.
>
> **Side effects.** About 1 in 10 people feel sick to their stomach (nausea). A severe
> allergic reaction is rare. Get medical help straight away if you get a rash, swelling of
> the face or throat, or trouble breathing.
>
> **Do not stop on your own.** Talk to your doctor before you stop taking this medicine.

## Repair note (`templates/repair-note.md`, short header)

Fit for reader: what I changed and left open (draft, not yet reviewed)

Based on: clinician memo, 4 November 2026 (internal).

Changed
1. Replaced "concomitant therapy" and "adverse event profile" with plain sentences above.
2. Cut the four-page draft to one page; moved repetition into a single side-effects
   paragraph.
3. Removed "completely safe" — not in the memo.

Left open
1. Indication sentence — needs approved patient wording from your label review.

Next step: medical review and, if required, user testing of the patient leaflet process.

## Finding cards (shared `../../templates/finding-card.md`)

### Finding 1
- **Draft line:** "Optimize concomitant therapy through adherence."
- **Issue:** Clinician language; patient cannot act on it.
- **Action:** Rewrote as how-to-take and when-to-call-doctor bullets.

### Finding 2
- **Draft line:** Four pages for a one-page request.
- **Issue:** Deliverable fit failure.
- **Action:** Restructured to one page; listed cuts in this note.

## Open items (`../../templates/gap-list.md`)

```text
Open items
1. Indication wording — not in memo — next: Label / medical writing

Not yet checked
- User testing (EU Article 59(3) process) — not run by this skill
```

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / fit-for-reader: not tool-checked (offline tools) · audience: 12→4 clinician terms; deliverable: 4pp→1pp
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
Fit · audience: 12 clinician terms flagged → 4 replaced with plain wording (not tool-checked)
Fit · deliverable: 4 pages → 1 page per request (not tool-checked)
```
