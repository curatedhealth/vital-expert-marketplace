# Task TR-8.3.1 The open-items summary

Counts by result, the open items in order of risk, one recommendation and the fixed line.
There is no percentage and no score.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Take the results from `claim-assessment`, count each once, order the open items by risk, choose one recommendation, print the fixed line |
| Skill | TR-8.3.1 |
| Knowledge | `references/rules.md` (C1 to C6), `references/patterns.md` (P1 to P8) |
| Tool | None. `scripts/faithfulness.py` prints the counts where code can run |
| Prompt | This guide |
| Template | `templates/open-items.md`, `templates/check-line.md` |
| Input | The results from `claim-assessment` (one of the six results per sentence), who will read the work |
| Governance | TR-H3, TR-H5, TR-H10, TR-H11, TR-H13 |

## Steps

1. **Take the results as `claim-assessment` gave them,** in its six words
   (`../../claim-assessment/references/statuses.md`). Do not re-read the claims and do not
   change a result. If a result is not in one of the six words, send it back to
   `claim-assessment`. When the person pasted the material and its passages but no check
   has run, run the claim check by hand first and give one combined summary
   (`templates/open-items.md`, combined form). When the person reports results from a check
   done elsewhere, follow the stop rule in `governance.md` and use the "results you told me
   about" form.
2. **Count each claim once, by result,** including the zeros. A claim is one checkable
   fact; a sentence with two facts is two claims. The total counts factual claims only
   (the five factual results); opinion, recommendation or definition lines are listed
   separately below it and never added to it. The header equals the sum of the rows
   under it; recount before sending. For counts the person gave, follow
   "counts the person gave you" in `../../claim-assessment/references/statuses.md`. Where code can run:
   `python scripts/faithfulness.py --found <n> --partly <n> --not-found <n> --different <n> --no-passage <n> --not-factual <n>`.
3. **List the open items in order of risk:** first any item with no passage to compare
   with that carries a figure (a number, date, dose or price), because the figure has
   nothing behind it; then your passage says something different, then not found in your
   passage, then the other items with no passage to compare with, then partly found. For
   each, name the sentence (short quote) and, in one plain sentence, what is missing:
   - your passage says something different: what the passage says instead, quoted;
   - not found in your passage: a supplied passage covers the topic and does not state it;
     the sentence is removed or rewritten to what the passage states;
   - no passage to compare with: no supplied passage covers the topic, or its source is
     unnamed; the sentence stays in the revised text with a gap;
   - partly found: the part the result names as missing. Say what the passage gives only
     when the result you were handed says it; never fill that in yourself.
   When the person gave results without sentences, list the open items by result in the
   same order, with their counts. Referring to items by the position the person gave them
   in ("statement 6") is fine. When you cannot tell whether a no-passage item carries a
   figure, list it with the other no-passage items and say so in one line. For internal work, a count per type is enough.
4. **Say what is not counted as open.** Opinions, recommendations and definitions sit on
   their own line, left to the person and their review.
5. **Give one recommendation,** one sentence aimed at the first open item in the list.
   It says what to do to the text or the sources, never whether to send. With no open
   items, give no recommendation.
6. **No open items?** Say so, and still say that a named person reviews the work through
   the usual process. Do not write "ready", "clean", "safe to send", "ready to go", "good
   to go", "all set" or "fine to send".
7. **Print the fixed line:** "No confidence figure: these results were not tool-checked."
8. **Status.** The summary is a draft for human review. It is not a clearance; a named
   person clears through `citation-and-record` (TR-H5).
9. **Close.** Every summary, short or full, ends with: "This check flags issues. It is not
   medical, legal, regulatory or ethics review.", once, as the last line of the reply, by
   the one rule in `../../claim-assessment/references/statuses.md`. When it goes into the
   TRUSTED summary, send only the check line; the summary carries the statement once.

## When asked for a percentage, a score or "how confident"

Say there is none, in one or two plain sentences, and do not compute one:

> "There is no confidence figure. I compared each claim with your passages by hand, and
> a percentage would suggest a tool measured it. Here are the counts and what is still
> open instead."

Say "I compared" only when you did; for results you were handed, "These results were
read by hand". Then give the summary.

When the person supplies a percentage from elsewhere ("85% backed"), say plainly that it
cannot be relied on as a confidence figure because how it was worked out is unknown; do
not restate or recompute it; offer to help fix or source the open items and compare them
again (`../governance.md`). Do not offer a "roughly" figure, a range, a grade or a
"high, medium, low" label. If asked whether the work is "solid" or "good enough to send",
say that your review process decides that, and point to the open items.

Every decline of a percentage, a score or a supplied figure ends with who judges
reliance, as the last line before the closing statement:
"How far to rely on this is for <the named person, or your review process> to decide." Use the
name the person gave; otherwise "your review process".

## If a sentence has no result yet

Do not guess one. If its passage is in the conversation, run `claim-assessment` by hand on
it first; otherwise ask for the passage. Count it only after it has one of the six results.

## Check line

See `templates/check-line.md`.

## Boundaries

- No pass or fail, no threshold, no grade, no color scale, no "high", "medium" or "low".
- No mixing of a source note with the counts. They stay separate.
- No evidence table unless the person asks for it; then `citation-and-record` builds it by
  hand.
- No clinical meaning of an open item (TR-H6); name it and route it.
