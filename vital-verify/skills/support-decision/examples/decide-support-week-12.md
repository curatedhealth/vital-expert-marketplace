> **Teaching material — never input.** The names, figures, dates and passages below are
> invented for shape only (VR-H2). Do not copy them into a live answer.

# Support decision examples

## Supported

Claim: "The announcement is dated 1 September 2026."
Passage: "Content current as of September 1, 2026."
Tier: silver.
Status: `supported`. Rationale: the passage states that date.

## Partial, because the figure is missing

Claim: "Response was 62 percent at week 12."
Passage: "Response was higher at week 12 than at week 4."
Tier: gold.
Status: `partial`. Rationale: the passage supports the week-12 comparison and does not state 62 percent. The answer keeps the comparison and drops the figure.

## Partial, because the tier is bronze

Claim: "The page describes the sponsor workflow."
Passage: a paragraph from a page graded bronze.
Status: `partial`. Rationale: `source tier bronze`. Do not report `supported`.

## Unverifiable

Claim: any sentence.
Source: `qualify_source` returned `inadmissible`, or the passage text is empty.
Status: `not_checked`. Reason: `source not admitted`. Omit the sentence. Do not replace it with a plausible date or number. Point the caller to `verify_text` (paste) or `ingest_document` then `qualify_source`.

## Out of scope

Claim: "Clinicians should discuss the label with patients."
Kind: normative.
Status: `out_of_scope`. It is not in the faithfulness denominator.
