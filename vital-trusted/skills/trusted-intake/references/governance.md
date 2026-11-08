# Governance for intake

## Boundaries

- Intake records context. It does not draft, check, classify or approve.
- It does not decide whether a piece is promotional, whether a product is approved in a
  market, or what class a device is. It records what the person or the supplied material
  says.
- It does not decide whether a tool is approved for any kind of data (TR-H11, and the
  never-claimed list in `trusted-capability-map`).
- It does not judge inputs in depth; that is `responsible-inputs`.
- It gives no clinical advice and makes no causality or reportability judgment (TR-H6).

## Careful defaults

When a field is missing and is not asked, the assumption is the careful one, and it is
stated in one line.

| Missing | Careful assumption |
|---|---|
| Whether it leaves the company | It may leave; depth at "leaving the company" until told otherwise |
| Product status in the named market | Not assumed approved there; product statements kept to the supplied label or marked as gaps |
| Scientific exchange or promotion, for doctor-facing work | Not assumed to be scientific exchange; the review process decides |
| Market, for internal work | Not needed; left unknown |
| Material supplied | Only what is in the conversation; nothing from memory (TR-H1) |
| AI policy | Not assumed to allow anything; the question is asked when sensitive input is involved |

## Internal processes

Name the kind of process in plain words (TR-H11). Do not guess a company's SOP name or
content.

| Situation | Kind of process to name |
|---|---|
| Material for doctors, pharmacists, payers, patients, agencies or the public about a product | Your promotional review process (or medical review, if the person says the piece is scientific) |
| A reply to a doctor's own question | Your medical information procedure |
| A side effect mentioned in any input | Your safety reporting procedure |
| A manuscript, abstract or poster | Your publications process |
| Personal or patient data in the input or output | Your data privacy function |
| Confidential, unpublished or client material going into an assistant | Your AI use policy and its owner; for client material, the client agreement |

## Stop rules

Stop and ask before continuing when:

- The person is about to paste confidential, unpublished, client or patient material and
  has not said what their AI use policy allows.
- The work leaves the company and the market or the use is unknown.
- Identifiable patient details would be carried into the output.
- The person asks the assistant to confirm that a tool is approved or that work is
  non-promotional. Say who decides, and offer what intake can do instead.

## Never claimed

- That a tool is approved, allowed or safe for a kind of data.
- That a piece is or is not promotional, or needs or does not need review.
- That a product is approved in a market, unless the person or a supplied label says so,
  and then only as "per your label" or "as you said".
- That the context card was checked against anything. It is what the person said and
  what the request showed.

## Closing statement

Intake outputs are not checks. The closing statement ("This check flags issues. It is not
medical, legal, regulatory or ethics review.") is not added to questions, assumptions or
the card. It appears on the TRUSTED summary that `trusted-check` writes.
