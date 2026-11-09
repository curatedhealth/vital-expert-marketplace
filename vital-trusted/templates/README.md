# Shared output cards

Plain, scannable shapes that the Prove skills and `trusted-check` can reuse when a skill
has no card of its own for the job.

**A skill's own template wins.** When a skill ships its own template for an output, use
that one and ignore the shared card of the same name. The shared cards fill gaps; they
never override a skill.

Rules every card follows:

- No verdict words. A card never says a draft passes, is fit, is ready or is compliant,
  and never "ready to go", "good to go", "ready to send", "all set" or "fine to send".
- Figures as supplied. A card states both figures given ("62 of 140" stays as given),
  never a difference or a proportion ("44%", "nearly half") worked out from them unless
  the person asked, and then labeled "calculated from the two figures you supplied"
  ("calculated from the figures you supplied" for three or more). A label alone never
  makes an unrequested figure acceptable.
- Record status, when a card shows one: "Uncleared draft"; "Uncleared draft, reviewed by
  <name>, as you told me"; "Cleared by <name>, <role>, <date>". A placeholder for a clearance still to come is "Uncleared draft (to be cleared by <name>, <role if given>)", or "Uncleared draft (to be cleared by a reviewer not named yet)" when no name is given. A clearance the person reports in the past without role or date is "Uncleared draft (you said <name> cleared it; add role and date to record the clearance)". No other form.
- Counts: "<n> factual claims"; opinion, recommendation or definition lines listed
  separately and never in the total.
- The closing statement, when a reply carries one, is the last line, except a "Detail
  for reviewers" section the person asked for.
- No superlatives about our own wording ("strongest", "best"), no prediction of what a
  reviewer, payer or agency will do, and no document or approval said to exist unless
  the person supplied it or said so.
- Manual result words only: the six exact words in
  `skills/claim-assessment/references/statuses.md`. No raw status codes from any tool.
- Every result is read by hand and labeled "Not tool-checked".
- No scores and no percentages. Counts only.
- Letter words, never letter codes: Tangible, Rule-compliant, Unbiased, Safe, True,
  Ethical, Defensible. True has its own line.
- Plain text only. No box-drawing characters, no em dashes.

| Card | File | Use when |
|---|---|---|
| Claim | `claim-card.md` | One checkable claim compared with a quoted passage |
| Finding | `finding-card.md` | The same card, numbered in a longer pack |
| Source | `source-card.md` | Saying what a named source can and cannot carry |
| Counts | `confidence-card.md` | Counts by manual result, open items, no figure |
| Evidence table | `evidence-table.md` | Every claim on one board, when asked |
| Open items | `gap-list.md` | Open items only |
| Prove brief | `prove-brief.md` | A full pack for work leaving the company |
| Letter lines | `check-line-stamp.md` | Lines a skill hands to `trusted-check`, never shown to the person as they are |
