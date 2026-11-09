# Governance for claims and label

## Boundaries

- This skill compares product statements with the label or intended purpose the person
  supplied, reads for promotional signals against the use the person stated, and tests
  comparisons against the data supplied. It does not decide what a product is approved
  for, whether a piece is legally promotion, whether a comparison is permitted, or
  whether an app is a medical device (TR-H3, TR-H6).
- Which market's rules apply and which statements a piece must carry:
  `market-rules-and-data`. Patient data in the output: `market-rules-and-data`.
- Balance of benefit and risk, selective reporting: `balanced-evidence`. Framing of
  numbers and charts: `honest-framing`.
- Dosing, contraindications, warnings and patient wording stated safely, and side
  effects in the input: `patient-safety`.
- Whether a statement matches its source: `grounded-statements`, and
  `claim-assessment`, by hand. Which source a claim needs: `sourced-claims`.
- Style and brand voice are the person's (TR-H9). Tone is in scope only where it turns
  information into promotion.

## Internal procedures

This skill prepares a draft for the company's own review. It never says a draft has
passed, or is ready for, that review (TR-H11). Name the kind of process in plain words:

| Situation | Kind of process to name |
|---|---|
| Promotional material, sales-force material, congress booth or stand material, agency brief, app or website copy about a product | Your promotional review process, and your medical review process as well where your process names it |
| Scientific exchange, MSL material, congress scientific sessions or advisory board material | Your medical review process |
| A reply to a doctor's own question | Your medical information procedure |
| A question about what the product is approved for, or whether a label is current | Your regulatory team |
| Whether an app or software is a medical device, or what its clearance covers | Your regulatory team |
| A side effect mentioned in a question or the material | Your safety reporting procedure |

Do not guess the name or content of a specific company's procedure.

## Stop rules

Before any stop below:

- **A possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person,
   medication error, lack of effect or product quality problem appears in any input.**
  Give patient-safety's flag first, in its template wording
  (`../patient-safety/templates/safety-flag.md`): pass it to the safety reporting
  procedure as soon as you can and forward the original unchanged; a quality problem also
  goes to the complaint procedure. This comes before any question and before every other
  stop in this list, whatever letters are active, with no judgment of cause, seriousness
  or reportability (TR-H14, TR-H6).

Do not stop when the label or intended purpose was not supplied: give a draft with
every product statement as a gap in the same reply, and ask for the label
(`templates/label-request.md`) in one combined question.

Stop and ask before continuing when:

Each stop holds back only the part it names. Draft the rest of the request in the same
reply, with a gap where the held part would go (draft first).

- **The person asks for a message about a use, population or dose beyond the supplied
  label** for promotional or sales use. Decline that message in one plain line; offer
  what the label supports; name medical information for questions doctors raise.
- **The person asks for a comparative or superiority claim with no direct comparison
  supplied.** Decline the claim; offer the alternatives in `tasks/comparative-claims.md`.
- **The person asks to prompt a doctor to ask a question** so that off-label
  information can be sent. Do not draft it; name the medical information procedure.
- **The person asks whether something is on-label, compliant, allowed or
  non-promotional.** Say what the comparison with the supplied label shows, and that
  the decision belongs to their review process.
- **A reply to a doctor asks for a recommendation** on dose or patient choice for a use
  outside the label. Give the data as supplied with its limits; make no recommendation
  (TR-H6).

## Never claimed

- That a statement is on-label, off-label as a legal finding, within the intended
  purpose as a regulatory finding, compliant, permitted or allowed.
- That a piece is non-promotional, scientific exchange or exempt from review.
- That a comparison is fair, valid, substantiated or acceptable.
- That the supplied label is the current approved version, unless the person says so,
  and then only "as you said".
- That a product or indication is approved in a market, except "per the label you
  supplied" or "as you said".
- That an app is or is not a medical device, or that its certification covers a claim.

## Where a person decides

A gate is a point where a named person decides, not this skill. The skill names it as
"as your process names" and stops there. It never names a role, a form or a deadline the
person did not give.

- `tasks/promotional-boundary.md`, Guard step 4 and replies step 8: whether the piece counts as promotion or scientific exchange, and whether it may go out, is decided at the review your process names (promotional review, or the medical information procedure for a reply).
- `tasks/comparative-claims.md`, Repair step 4: whether a cross-trial comparison may be shown at all is decided at that same review, as your process names.
- `tasks/label-and-intended-use.md`, Repair step 4: a contested statement stays, changes or goes at the review your process names. The claims note lists it either way.

## Closing statement

When this skill's check lines go into a TRUSTED summary, that summary ends with: "This
check flags issues. It is not medical, legal, regulatory or ethics review." Direct
replies, drafts and claims notes do not carry it.
