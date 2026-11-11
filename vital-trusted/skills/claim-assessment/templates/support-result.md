# Output format: fact-check result (Part B)

What the person sees. Plain language, no rule or pattern ids (TR-H13). Sized to the
stakes (TR-H12). Use the six results from `../references/statuses.md` and no other
words. Every result is by hand and labeled "not tool-checked".

## Full result

```
Fact-check against the passages you supplied (draft, for your review)

Not tool-checked: I compared each claim with your passages by hand.
<If the results came from someone else: use the other opening line in ../references/statuses.md>
Checked against: <one line per source>

What a match means: the passage you gave says the same thing as the sentence. It does
not mean the sentence is true, that the source is good, or that the work is ready.

<total> factual claims: <n> found in your passage, <n> partly found, <n> not found in
your passage, <n> your passage says something different, <n> no passage to compare with.
Listed separately, not in the total: <n> opinion, recommendation or definition.
<The five factual counts add up to the total, zeros included. Recount before sending.>

Found in your passage: keep (<n>)
1. "<sentence>" with "<quoted words>" (<source, locator>)
<A sentence with one found part and one different part is two claims. List the found
part here as "<found part>" (part of sentence <k>; held with it until you answer the
question below), and the other part under "says something different".>

Partly found: rewrite to match (<n>)
1. "<before>" → "<after>". Your passage says <x>; it does not say <y>.
   Rewritten, not tool-checked.
   A worked-out difference is rewritten to both stated figures. Wrong: "share rose 3
   points". Right: "share 12% in June and 15% in September". The before sentence is one
   claim; the rewrite states two facts, so a recheck counts it as two claims.

Not found in your passage: removed or rewritten to what the passage states (<n>)
1. "<sentence>". Not found in your passage: <what the passage does cover, in one line>.
   <Left out, not replaced. | Rewritten to what the passage states: "<after>".>
   <Only when a supplied passage covers the topic. When none does, the result is no
   passage to compare with (`../references/statuses.md`).>

No passage to compare with: open, not removed (<n>)
1. "<sentence>". No passage to compare with: <no supplied passage covers <topic> | the
   source is unnamed>. Kept in the revised text with a visible gap until you supply a
   passage or take it out.

Your passage says something different: ask you (<n>)
1. Your draft: "<sentence or part>". Your passage: "<quote>" (<source, locator>).
   Which is right? Held out of the revised text until you say.
   <Show both. Write no replacement sentence until the person answers.>

Opinion, recommendation or definition: for your judgment (<n>)
1. "<recommendation or opinion>". Not something a passage can settle.

<Only if a correct sentence misleads by what it leaves out:> A framing point: "<sentence>"
is accurate, but the framing may mislead; <what is left out, quoted from the passage>.
See the framing notes. Not a result and not counted.

Revised text
<the text with keeps and rewrites, removed sentences out, a gap after each sentence with
no passage, a held gap in place of each sentence your passage says something different
about, opinion and recommendation lines kept as written, and no other gaps>

<If the reader is not known: give the full result, then ask once, at the end, who will
read it; the next-step line follows the answer.>
<If the work leaves the company or the author's team (external depth):> Next: source
quality, the open-items summary and the record can be added, and this goes through your
<promotional or medical> review, as your process names it, before use.

This check flags issues. It is not medical, legal, regulatory or ethics review.
```

Held text for "your passage says something different": the sentence does not go out,
and no replacement is written. In its place:
`[GAP: conflicting; your draft says "<draft words>", your passage says "<passage words>"; tell me which is right]`.
When only part of a sentence differs, the whole sentence is held this way, and the found
part is listed under "found" as part of the held sentence.

Wrong: the draft's "fell to 4" kept, or quietly changed to the passage's "5.2" in the
revised text. Right: the sentence held with both values shown, and the question asked.

## Short result (leadership or cross-team)

Counts, the differing sentences side by side, what was removed or left open, the main
change, and the revised text. No per-claim lists of found sentences.

```
Fact-check against your passage (not tool-checked: I compared each claim with your
passages by hand)

<total> factual claims: <n> found in your passage, <n> partly found, <n> not found in
your passage, <n> your passage says something different, <n> no passage to compare with.
Listed separately, not in the total: <n> opinion, recommendation or definition.

Your passage says something different (<n>), held until you say which is right:
- Your draft: "<sentence or part>" | Your passage: "<quote>"
<Only when there are any:> Not found in your passage, removed or rewritten: "<part>".
<Only when there are any:> No passage to compare with, kept with a gap: "<part>".

Main change: <one line on the rewrite or removal that matters to the reader>.

Revised text
<the revised text, built as in the full result>

A match means your passage says it, not that it is true.

This check flags issues. It is not medical, legal, regulatory or ethics review.
```

## Quick result (internal and quick, two or three lines)

```
<total> factual claims (figures, names and quotes) checked by hand against your passage,
not tool-checked: <n> found in your passage, <n> partly found, <n> not found in your
passage, <n> your passage says something different, <n> no passage to compare with.
<One line on the main change, or the held sentence with both values.> A match means your
passage says it, not that it is true.
<When the person needs text back:> Revised: <the revised text>

This check flags issues. It is not medical, legal, regulatory or ethics review.
```

The closing statement follows the one rule in `../references/statuses.md`: once, as the
last line of any reply that shows results (only a "Detail for reviewers" section the
person asked for comes after it); never on a decline with no check run or on an
explanation.

## Explanation only (no check asked for)

Two to four plain sentences: what the result means, what to do with it, and, if useful,
a short invented illustration marked as such. No result block, no counts, no "not
tool-checked" label and no closing statement. Count the sentences before sending: at
least two and at most four, with no list, heading or follow-up offer added after them.

## Nothing to check

When the request needs no fact-check (the person wants the text tidied, translated or
formatted, not checked), give the edited text and nothing else: no "nothing needed
changing" line, no source note, no counts line, no result block. A safety flag still
comes first, and for a translation, the short translation note still follows
(`../../fit-for-reader/templates/translation-note.md`). The one-sentence "nothing to
change" form is only for a request to check.
