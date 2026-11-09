# Counting hand-check results

This is the only path. A hand check gives counts, not a confidence figure. Every count is
labeled "not tool-checked".

## Steps

1. **Take the results from `claim-assessment`**, in its six words (see
   `../../claim-assessment/references/statuses.md`). Do not re-read the claims and do not
   change a result. If a result was not given in one of the six words, send it back.
2. **Count each claim once** (one checkable fact), by result, including the zeros: found in your passage,
   partly found, not found in your passage, your passage says something different, no
   passage to compare with. The total counts these factual claims only; opinion,
   recommendation or definition lines are listed separately below it, and the header
   equals the sum of the rows under it. Where code can run,
   `../scripts/faithfulness.py` prints the same counts. It adds nothing else.
3. **List the open items first**, in this order: any item with no passage to compare with
   that carries a figure, then your passage says something different, not found, other
   items with no passage to compare with, partly found. For each, say the sentence, the
   result and the one action it needs.
4. **Say what is not counted.** Opinions, recommendations and definitions are on their own
   line. They are not checked and not open items.
5. **Give one recommendation** for what to do next, such as "resolve the two open items
   before this leaves the team". It is advice, not a pass.
6. **Print the fixed line:** "No confidence figure: these results were not tool-checked."

## If the person asks for a percent or a score

Say there is none, in one sentence: "A percent would suggest a tool measured it. These
results were not tool-checked, so I give the counts and the open items instead." Give the
open-items summary (`../templates/open-items.md`). Do not compute a ratio in the reply
and do not offer a "roughly" figure.

## What stays out

- No percent, ratio, score, grade, threshold or color.
- No "high", "medium" or "low" confidence label.
- No pass or fail, and no "ready", "safe to send", "ready to go", "good to go", "all
  set" or "fine to send".
- No mixing of a source note with the counts. They stay separate.

## Handing on

Counts and open items go to `citation-and-record` for the record note, and to
`trusted-check` as the check line. A person decides whether the work moves on, under the
review your process names (`../governance.md`).
