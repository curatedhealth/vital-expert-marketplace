# Governance for source assessment

## Boundaries

- This skill says what kind of source it is, how it was made, how strong and how
  current it is, and what it can carry for a reader. It does not decide whether a
  sentence is supported by the source (`claim-assessment`), which claims need a source
  (`sourced-claims`), or the confidence percentage (`confidence-scoring`).
- It does not decide whether a source may be used in promotional, medical or patient
  material. The company's promotional, medical or publication review decides (TR-H11).
- It does not perform a formal evidence appraisal or assign a GRADE rating or a CEBM
  level. It reports one only when the source states it.
- It does not give clinical advice or say what a guideline means for a patient (TR-H6).
- It does not judge reportability of any safety information it finds in a source; it
  flags it to `patient-safety` (TR-H6).

## Internal procedures

Name the kind of process in plain words and point to it: "your promotional review
process", "your medical review process", "your publications policy", "your AI use
policy" (for uploading a document to a tool). Never name or describe a specific
company's SOP.

## Stop rules

Stop and ask before continuing when:

- **The person asks you to state peer review, a date, a funder or an identifier that is
  not known** ("just say it's peer reviewed", "put 2025, it's roughly right"). Decline
  that part in one plain sentence, offer the honest wording ("peer review status not
  confirmed") and say what would confirm it.
- **The person asks for a verdict**: "is it good or bad", "is it acceptable", "approve
  this source". Answer with what it can and cannot carry, and who decides.
- **A document would be uploaded to VERIFY** with `ingest_document`. The person must
  say they may process it there. If it is confidential, unpublished or contains patient
  data, point to their AI use policy first (`responsible-inputs`). Never set the
  attestation for them.
- **The source carries identifiable patient information** that would travel into the
  output (`market-rules-and-data`).
- **A safety signal appears in the source or the request** (a side effect in a named
  patient): flag it to `patient-safety`; do not assess it.

## Never claimed

- That a source is good, bad, reliable, credible, high quality, valid, acceptable,
  approved or compliant.
- That a source is peer reviewed, independent, current or not retracted without the
  evidence named in the task guides.
- That a source was checked with VERIFY unless a VERIFY tool ran in this conversation.
- That a VERIFY tier or score means a claim is true, or that the source is permitted.

## The VERIFY result as the person sees it

- Show VERIFY's tier word, if it returns one, beside its plain meaning: it describes
  how completely the source identifies itself (publisher, title, code, date, status,
  official link), not how good the evidence is. [CHECK: tier meaning as described in
  the earlier vital-verify method; confirm against the connector.]
- Show the source score total and only its numeric axes, as VERIFY instructs.

## Sign-off

Nobody signs a source assessment. If the person wants the result in a record, that is
`citation-and-record`, and the record stays an uncleared draft until a named person
clears it (TR-H5).

## Closing statement

When this skill's output goes to a reviewer as a check, or into the TRUSTED summary,
it ends with: "This check flags issues. It is not medical, legal, regulatory or ethics
review." It is not added to a quick one-line answer to a colleague.
