# Governance for grounded statements

## Boundaries

- This skill checks a draft against the material supplied in the conversation. It does
  not establish that a statement is true in the world (TR-H3).
- It does not judge source quality (`source-assessment`), decide which claims need a
  citation (`sourced-claims`), or balance benefits and risks (`balanced-evidence`).
- It does not judge clinical meaning or give clinical advice (TR-H6).

## Internal procedures

This skill improves a draft before it reaches the company's own review. It never says a
draft is ready for, or has passed, that review (TR-H11). When the work will leave the
company, the note names the kind of process it goes through next in plain words.

## Stop rules

Stop and ask before continuing when:

Each stop holds back only the part it names. Draft the rest of the request in the same
reply, with a gap where the held part would go (draft first).

- The person asks for a figure, citation or study detail to be filled in "for now" or "as
  a placeholder" with a realistic value. Offer a visible gap marker instead, for example
  `[GAP: not supplied; 95% CI for the primary endpoint; the table in your source that gives it]`.
- Two supplied sources conflict on a figure that changes the message. Hold back only
  that figure: draft the rest with a gap where it goes and ask which source holds.
- The draft carries identifiable patient information from case material (hand to
  `market-rules-and-data` and `responsible-inputs`).

Do not stop when no source material was supplied for factual content: give a gapped
structure in the same reply and ask for the material.

## Never claimed

- That the draft is accurate, verified or correct.
- That a claim was checked against its source with a tool. None was.

## Where a person decides

A gate is a point where a named person decides, not this skill. The skill names it as
"as your process names" and stops there. It never names a role, a form or a deadline the
person did not give.

- `tasks/no-fabrication.md`, Guard step 5: a figure with no supplied source is offered as a gap. The person supplies the source, or the review your process names decides.
- `tasks/number-consistency.md`, Repair step 5: when two supplied figures disagree, the person says which is correct. The person or review your process names confirms it.

## Closing statement

When this skill produces a check line or repair note for a reviewer, the TRUSTED summary
that carries it ends with: "This check flags issues. It is not medical, legal,
regulatory or ethics review."
