# Checking claims by hand

This is the only path. No tool decides a result. You compare each sentence with a passage
the person supplied, and every result is labeled "not tool-checked".

## Steps

1. **Get the passages.** Words the person pasted, or the page and section they point to. If
   nothing was supplied, ask once (`../intake.md`). With none, every factual sentence
   stays "No passage to compare with".
2. **Split the text into claims.** One checkable claim per part. A sentence with two
   figures is two claims. Where code can run, `../scripts/split_claims.py` lists the sentences
   for you. It decides nothing.
3. **Quote the passage.** For each claim, copy the exact words it rests on and say where
   they sit (page, section, table). Never write a passage yourself and never use one from
   memory.
4. **Compare and name the result** with one of the six results in `statuses.md`. Use those
   words and no others.
5. **Take the action the result names.** Keep, rewrite to match, remove, ask, or leave to
   the person (`../tasks/decide-support.md`).
6. **Check every rewrite again.** A rewritten sentence is a new claim. Label it "rewritten,
   not tool-checked".
7. **Report the counts** of claims, in the six words, with the open items. The result
   carries the revised text at every size when the person needs text back. Head the
   result with the opening line in `statuses.md` ("Not tool-checked: I compared each claim
   with your passages by hand." only when you did), and end with the closing statement
   by the one rule there.

## What stays out

- No percent, ratio or score. A hand check gives counts only.
- No claim that a sentence is true in the world. Found means the passage says it.
- No "supported" or "unsupported" as a result. See `statuses.md`.
- No derived figure, and no ratio word ("twice as many", "half") worked out from two
  rates, unless the person asks for it; then it is labeled "calculated from the two
  figures you supplied" (from three or more: "calculated from the figures you supplied").
  A label alone never makes an unrequested figure acceptable. If a number is not in the
  passage, say so and quote the ones that are.
- No proportion in another form: "62 of 140" stays as given, never "44%", "more than 4 in
  10" or "nearly half" unless the person asks and it is labeled.
- No source, data on file, attachment or approval said to exist unless the person
  supplied it or said so. Otherwise it is a gap.
- No link to a source you did not read. Say the claim has no passage to compare with.

## Handing on

The counts go to `confidence-scoring`. The sources and the passages that stay go to
`citation-and-record`. A person decides whether the work is used, under the review your
process names (`../governance.md`).
