# Misuse patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; no real product, trial or person.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

**P1 The percent as a verdict.** The number is presented as a grade or a release signal.
Why: the percent counts overlap with supplied passages. It says nothing about truth,
balance, permission or whether the right sources were supplied.
Before: "Faithfulness 96%: high confidence, safe to send to the payer."
After: "Faithfulness 96%: of the 12 factual statements checked, 11 are backed by the
passages supplied and 1 is partly backed. Open: 1 statement on cost. Your market access
review decides whether it goes." (TR-H3, TR-H5, C5)

**P2 The simulated percent.** A figure computed from the assistant's own reading, or
estimated, when VERIFY did not run.
Why: it looks like a tool result and is not one. It is a fabricated record.
Before: "I've checked it: about 80% faithful."
After: "No confidence figure: VERIFY is not connected. Read, not tool-checked: 5
statements match your material, 1 does not appear in it." (TR-H1, TR-H4)

**P3 Out of scope in the denominator.** Normative or definitional statements counted.
Why: they cannot be backed by a passage, so counting them lowers the figure for no
reason; leaving them off the card hides that they exist.
Before: 6 supported, 2 partial, 1 unsupported, 1 unverifiable, 3 out of scope → "54%".
After: (6 + 1) ÷ 10 = 70%; "3 statements are not factual and are not counted". (C1)

**P4 Unverifiable dropped to lift the figure.** "Leave out the ones it couldn't check."
Why: a statement nobody could check is still in the text. Dropping it from the count but
not from the draft overstates support.
After: keep it in the denominator, or remove the statement from the text and check
again. (C1, TR-H1)

**P5 Unverifiable read as false.** "Two claims are wrong."
Why: unverifiable means no usable source or passage, not that the statement is false.
After: "2 statements could not be checked: no source was supplied for them." (C4)

**P6 Source score called confidence.** "Source confidence 78", or the faithfulness
percent averaged with the source scores.
Why: the source score is about the page; the percent is about the statements. Mixing
them produces a number that means nothing.
After: print the source score under its reference and the faithfulness line once, apart.
(C6, C7)

**P7 The empty axis as zero.** A null relevance or currency axis printed as 0.
Why: zero says the check ran and scored nothing; null says it did not run.
After: leave the axis out; if it matters, say "currency not checked". (C6)

**P8 Two recommendations, or a send decision.** "Fix the cost line, add a reference,
check the subgroup, then it's good to go."
Why: one recommendation keeps the next action clear; a send decision is not the card's
to make.
After: "Recommendation: remove the cost-savings statement or supply the analysis that
backs it, and check again." (C6, TR-H5)

**P9 Zero denominator printed as a number.** "0%" or "100%" when nothing factual was
checked.
After: "No confidence figure: nothing factual was checked." (C1)

**P10 Comparing drafts without the counts.** "Version 2 is better: 85% against 70%."
Why: the two drafts may have had different statements checked.
After: show both counts side by side and say what changed.
