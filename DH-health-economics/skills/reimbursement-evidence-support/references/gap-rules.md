# Gap rules

A gap is information. Each reason for a gap leads to a different next step, so name the reason.

## For a rule against the person's model or evidence (A2)

| Class | When | How to word it | Next step |
|---|---|---|---|
| Shown | The person's document, model or a checked passage shows it | "Shown: [what], [document, section]" | None |
| Not shown | The rule applies and nothing supplied shows it | "Not shown in the material supplied" | Ask for the document, or plan the evidence (B1) |
| Departure | The material does something other than the rule (another perspective, discount rate, value set, mapping) | "Departure: [what the model does] against [rule, row]; whether it is acceptable is for [body] and the owner" | Owner decides whether to justify it or add a reference-case analysis |
| `[GAP]` material silent | The material does not say (for example the value set, the cost year, the discount rate) | "`[GAP]`: the material does not state [field]" | The person supplies it |
| `[GAP]` record silent | The library record cannot answer (registration, endpoints, effect size) | "`[GAP]`: the library record does not hold [field]; check the paper, section X" | If the paper is open access, read the full text first and quote it; otherwise the person supplies the section |
| `[GAP]` full text silent | The open-access full text was read and does not state the field | "`[GAP]`: the full text (PMC id, read DATE) does not state [field]" | The person supplies it |
| `[GAP]` rule not sourced | The references do not hold the body's rule | "`[GAP]`: rule not in the sourced references (read 19 October 2026); check [body]" | Check the body's text |
| Not applicable | The rule's condition does not hold (for example S18 when the owner has judged the technology not higher financial risk; early-use items for routine use) | "Not applicable: [reason, row]" | None |

## For a claim the economic case rests on

| Verify status | Your reading | Usable? |
|---|---|---|
| supported or partial, and the passage states the finding in the same direction and with the same strength (significance, interval, horizon) | Checked | Yes, with source and passage |
| supported or partial, but the passage is not a result, or the claim is stronger than the passage (for example "significantly lower costs" where the cost interval includes zero) | Not checked | No |
| unsupported or any other status | As returned | No, until resolved |
| no source supplied | Unverified | No |

Read the passage yourself every time. `check_claim` decides on word overlap: it rated a correct cost-and-QALY claim and an overstated "significantly reduces costs" claim the same ("partial", 44 and 40 percent overlap) from one passage (`tools.md`).

## For a computation

A calculator or script output on the person's inputs is a hypothesis. State the inputs beside it. A calculator that refuses the payload is `[GAP]` ("calculator returned HTTP 422; computed by hand from the inputs shown" or "not computed").

## Never

- Never turn "not shown" into "the product does not meet the standard".
- Never say a model "meets the threshold" or that a product "is cost-effective". Report the ratio and the body's written range side by side with rows; the body decides.
- Never treat a library absence (no guidance passage, no precedent) as a rule.
- Never fill a gap from memory, from an unsourced passage, or from a Verify status alone.
