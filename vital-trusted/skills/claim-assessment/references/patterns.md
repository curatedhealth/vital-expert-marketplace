# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; "Velostra", "Lumivra" and the NORLA registry are
fictional. Pattern ids are for this file only; describe the problem in plain words to
the person (TR-H13).

## Contents

- Splitting and pairing C1–C4, C13, C14
- Reading results C5–C7, C9, C10, C15
- Requests and framing C8, C11, C12

## Splitting and pairing (Part A)

**C1 The cleaned-up sentence.** The text is tidied before it is split, so the check runs
on words the person never wrote.
Why: the result describes a different text; offsets no longer point to the original.
Before: draft says "cuts admissions by 40%"; the check runs on "is associated with fewer
admissions". After: check "cuts admissions by 40%" as written; rewrite only after the
result, and recheck. (TR-H1, R4)

**C2 The bundled claim.** Two facts resting on different passages are checked as one.
Why: a `partial` result is then unreadable, and the unsupported half survives.
Before: "Velostra cut admissions by 40% in the NORLA trial of nearly 2,000 patients"
paired with the outcome passage only. After: note three parts (effect, design, size)
and pair each. (R6)

**C3 The paraphrased passage.** The assistant writes a summary of the source and checks
the claim against its own summary.
Why: the check compares the draft with the assistant, not with the source.
After: quote the source word for word with a locator. (R4, R5)

**C4 The skipped sentence.** Background or "obvious" sentences are left out of the list,
or a sentence without a reference marker is treated as not a claim.
Why: unmarked sentences are where invented details hide. After: list every factual
sentence at the depth the stakes need. (TR-H12)

**C13 The borrowed passage.** The text cites source A; the passage comes from source B
because B happens to say it.
Why: the reader will look in A and not find it. After: pair with the cited source, or
flag that the citation should change. (TR-H1)

**C14 The remembered passage.** No passage was supplied, so the assistant recalls what
the paper "says".
Why: memory is not a source; VERIFY cannot check a recollection. After: ask for the
material. (TR-H1, TR-H4)

## Reading results (Part B)

**C5 The replacement.** A sentence comes back unverifiable or unsupported and is replaced
with a likely value.
Why: the new value has no passage either, and now looks checked.
Before: "approved in March 2025" (passage silent) becomes "approved in early 2025".
After: sentence removed; `[GAP: not supplied — approval date — supply the approval
document]`. (R5, TR-H1)

**C6 Silence read as contradiction.** A passage that does not mention a point is reported
as saying the opposite.
Why: it accuses the draft of being wrong when it is only unsupported.
After: "your passage does not say this", not "your passage says otherwise". (R6)

**C7 The figure that survives a partial.** The passage supports the comparison but not
the number, and the number stays.
Before: "admissions fell by 40%" against a passage giving 12.0% and 20.0% with an
adjusted hazard ratio of 0.60. After: "admissions within 12 months were 12.0% with
Velostra and 20.0% with standard care (adjusted hazard ratio 0.60)". (R5)

**C9 The simulated status.** Without VERIFY, results are written as "supported" or
"partial", as if a tool ran.
Why: a manual reading presented as a tool result is a fabricated record.
After: manual result words and "not tool-checked". (TR-H4)

**C10 The unchecked rewrite.** A sentence is rewritten to match the passage and kept
without a second check.
Why: rewrites drift; a new number or word slips in. After: recheck the rewrite, or label
it "rewritten, not tool-checked". (TR-H4)

**C15 Supported read as true.** "Supported" is reported as "verified", "correct" or "true".
Why: the passage may be wrong, old or weak; the reader skips review.
After: "your passage says this", plus the plain-words line on what a match means. (TR-H3,
R5)

## Requests and framing

**C8 The unnamed authority.** "Experts agree", "guidelines recommend", "studies show".
Why: no one can be asked; nothing can be quoted.
After: name and supply the source, or remove the sentence. (R5)

**C11 The fact dressed as opinion.** "We believe Velostra cuts admissions by 40%" filed
as an opinion and skipped.
Why: the figure is still a claim the reader will rely on.
After: check the figure; the "we believe" does not exempt it. (R1)

**C12 "Just mark them all supported."** The person asks for labels without a check.
Why: an unchecked "supported" looks identical to a checked one.
After: decline plainly; offer to check now or mark them "not checked" for review.
(TR-H3, TR-H4, TR-H5)
