# Governance for market rules and data

## Boundaries

- This skill covers what the output says about its market (wording, approvals, reach),
  the statements a market usually expects on promotional or external material, and
  personal details the output would show.
- It does not judge whether a claim is within the label or a comparison is supported
  (`claims-and-label`), whether benefits and risks are balanced (`balanced-evidence`),
  whether safety statements match the label (`patient-safety`), or what may go into the
  assistant (`responsible-inputs`).
- It gives no legal, regulatory or privacy advice. It names the question and the
  function that answers it.

## Decisions this skill never makes

| Decision | Who makes it, in plain words |
|---|---|
| Whether material may be used in a market, or is promotional | Your promotional review process (or medical review, if the person says the piece is scientific) |
| Whether the statements on a piece are sufficient | Your promotional review process for that market |
| The job code, date of preparation and PI version | Your approval system and the people who run it |
| Whether a product is approved in a market, for what | The approved label for that market, as the person supplies it |
| Whether a post or page may reach the public | Your promotional review process |
| Whether data is anonymous, or a count small enough to show | Your data privacy function |
| Whether a case story or a named professional may be used | Your data privacy function, with the consent or permission records |
| Whether a reported event must go to safety reporting | Your safety reporting procedure (`patient-safety`) |

## Internal procedures

TRUSTED supports the company's own procedures and never replaces them (TR-H11). Name the
kind of procedure in plain words: "your promotional review process", "your medical
information procedure", "your data privacy function", "your safety reporting
procedure". Never name or invent a company's SOP, and never say a piece satisfies one.

## Careful defaults

| Missing | Careful assumption |
|---|---|
| Market, for external product material | Not assumed; draft with market-specific elements as gaps and ask in the same reply |
| Product status in that market | Not assumed approved; product statements kept to the supplied label or left as gaps |
| Channel | May reach the public if it is a post, page or anything forwardable |
| Whether a case may be used | Not assumed; leave the person out and ask |
| Minimum count | Not set; ask the privacy function |

## Stop rules

Before any stop below:

- **A possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person,
   medication error, lack of effect or product quality problem appears in any input.**
  Give patient-safety's flag first, in its template wording
  (`../patient-safety/templates/safety-flag.md`): pass it to the safety reporting
  procedure as soon as you can and forward the original as received; a quality problem also
  goes to the complaint procedure. This comes before any question and before every other
  stop in this list, whatever letters are active, with no judgment of cause, seriousness
  or reportability (TR-H14, TR-H6).

Stop and ask before continuing when:

Each stop holds back only the part it names. Draft the rest of the request in the same
reply, with a gap where the held part would go (draft first).

- The person asks for a job code, date of preparation or PI text to be filled in "so it
  looks finished". Offer visible placeholders instead, and draft the rest of the
  piece in the same reply.
- The person asks you to confirm the material is compliant, complete or approved, or
  that data is anonymous. Say who decides and what you can do instead.
- Identifiable patient details would be carried into the output, and the work cannot be
  done without them.

Do not stop for internal work with no product statements, for an external email that
only lists agreed attachments or actions with no product claims, or for a draft that
names no person. When the market is unknown for external product material, do not stop
either: draft with the market-specific elements as gaps and ask the market in the same
reply.

## Never claimed

- That material is compliant, approved, allowed, complete or ready for any market.
- That the list of expected statements is complete.
- That a job code, date or PI is current or correct.
- That data is anonymous, anonymized, de-identified or fine to share.
- That this skill satisfies any industry code, regulation or data protection obligation.

## Where a person decides

A gate is a point where a named person decides, not this skill. The skill names it as
"as your process names" and stops there. It never names a role, a form or a deadline the
person did not give.

- `tasks/jurisdiction.md`, step 5: whether the piece may be used in that market is decided at the review your process names.
- `tasks/required-statements.md`, Guard step 6: whether a reminder exemption applies is decided at the review your process names, not here.
- `tasks/privacy-in-output.md`, Repair step 4: whether details are anonymous enough is decided by the data privacy process, as your process names. This skill only keeps identifiable details out.

## Closing statement

When this skill's check line reaches the TRUSTED summary, the summary ends with: "This
check flags issues. It is not medical, legal, regulatory or ethics review." Direct
replies, drafts and notes do not carry it.
