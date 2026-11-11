# Task TR-8.1.2 Decide support for each claim against a quoted passage (Part B)

Absorbs the support-decision method of the earlier Prove work, now done by hand.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Compare each claim with its quoted passage by hand, name the result in plain words, act on it, recheck any rewrite |
| Skill | TR-8.1.2 |
| Knowledge | `references/rules.md` (R1 to R6), `references/patterns.md` (C5 to C12, C15) |
| Tool | None. Hand comparison, steps in `references/by-hand.md` |
| Prompt | This guide |
| Template | `templates/support-result.md`, `templates/check-line.md` |
| Input | The claim list from Part A, each claim paired with its quoted passage |
| Governance | TR-H1, TR-H3, TR-H4, TR-H5, TR-H11 |

## What "found in your passage" means

Tell the person this in plain words every time results are shown:

> Found in your passage means the passage you gave says the same thing as the sentence.
> It does not mean the sentence is true, that the source is good, or that the work is
> ready. I compared them by hand, so every result is labeled "not tool-checked".

A sentence can match a weak source, an old source or the wrong source. Source quality is
`source-assessment`. Whether the work may go out is the company's review process.

## Steps

1. **Check the pairing.** Each claim has a passage quoted word for word with a locator, or
   is marked "No passage to compare with". If a source is unnamed ("experts agree"), the
   claim has no passage.
2. **Never use a passage you wrote.** The passage is words quoted from the source. If there
   is none, do not write one to make the comparison work.
3. **Compare and name the result.** Use the six results in `references/statuses.md` and no
   other words. Show the quoted passage next to the sentence.
4. **Take the action the result names**, from the table in `references/statuses.md`: keep,
   rewrite to match, remove, ask, or leave to the person.
5. **Recheck every rewrite.** A rewritten sentence is a new claim. Check it again before it
   stays in the text, and label it "rewritten, not tool-checked".
6. **Hand on.** Counts by result go to `confidence-scoring`; the sources and passages that
   stay go to `citation-and-record`. Do not compute any percentage or score here.

## Reading rules

- A figure, name or quotation stays only when an exact quoted passage states it, paired
  with it by hand and shown next to it (R5). On "Partly found", the figure, name or
  quotation is the first thing to drop.
- "Not found in your passage" is not "false". It needs a supplied passage that covers
  the topic; when none does, the result is "no passage to compare with" and the sentence
  stays with a gap (`references/statuses.md`). "Your passage says something different"
  needs a passage that states the other value, not one that is silent (C6).
- A sentence with two facts is two claims, each with its own result. Never merge them
  into one "partly found" ("the only once-weekly patch": the patch is one claim, "the
  only" another).
- An unnamed authority ("experts agree", "guidelines recommend") is not a source. Treat
  the claim as having no passage to compare with unless the person names and supplies the
  source.
- A passage can match a sentence in words and still be narrower or older. When the passage
  states something narrower or dated, say so even on "Found in your passage".
- A figure worked out from the passage's numbers is not in the passage. Quote the numbers
  the passage gives and name the worked-out figure as the missing part.
- No ratio words worked out from supplied rates. "Twice as many", "half", "a third fewer"
  or "doubled" computed from two rates is a derived figure: write it only when the person
  asks for it, labeled "calculated from the two figures you supplied" (from three or more
  figures: "calculated from the figures you supplied"). A label alone never makes an
  unrequested figure acceptable. Otherwise quote the rates.
  Example: against "9% with drug D and 4% with placebo", write those two rates, not "more
  than twice as many people stopped drug D".
- Proportions are derived figures too. "62 of 140" stays as given; "44%", "more than 4 in
  10" or "nearly half" only if the person asks, labeled "calculated from the figures you
  supplied".
- "Your passage says something different": show both, hold the sentence out of the
  revised text with a `conflicting` gap that carries both values, write no replacement,
  and ask which is right. A sentence that is half found and half different is two claims;
  the whole sentence is held (`templates/support-result.md`).
- Close calls follow the decision rules in `references/statuses.md`: rounding words,
  "not assessed", evaluative words such as "well tolerated", worked-out figures, a named
  person's quote with no source, a related but different measure, a significance word
  backed by a stated p-value or interval (found, with a note on endpoint rank), and a
  correct sentence that misleads by omission (a framing point,
  not a seventh result, written as "A framing point: ..." with no skill name, and handed on
  to `honest-framing` or `balanced-evidence`).

## What to say

Head every result with the opening line from `references/statuses.md`: "Not
tool-checked: I compared each claim with your passages by hand." only when you did;
the other line when the results came from someone else. The check line carries the counts
and nothing else. Give no confidence percentage for a hand check.

A question about what a result means, with nothing to check, gets two to four plain
sentences and nothing else: no result block, counts or closing statement
(`templates/support-result.md`, explanation only). The "what found means" line above goes
with results, not with an explanation.

## When asked to mark claims as found without a check

Decline in plain words, without lecturing: "I can't mark these as found without comparing
them with a passage. A result nobody checked would look the same as one that was, and a
reviewer would rely on it." Offer one of: run the comparison now; label them "no passage
to compare with" so they go to review as open items; or list which passages would be
needed. Never produce the labels anyway (`governance.md`).

## Check line

See `templates/check-line.md`.

## Boundaries

- Part B decides support against supplied passages only. It does not search for sources,
  grade them, check currency or build citations.
- It does not judge clinical meaning, fair balance or whether a claim is permitted. Flag
  and route (`balanced-evidence`, `claims-and-label`).
- It never says the work is accurate, correct, verified or ready.
