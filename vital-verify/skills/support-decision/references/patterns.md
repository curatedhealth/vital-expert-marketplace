# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching (VR-H2). Pattern ids are for this file only;
describe the problem in plain words to the person (VR-H13).

## Reading results

**C5 The replacement.** A sentence comes back unverifiable or unsupported and is replaced
with a likely value.
Why: the new value has no passage either, and now looks checked.
Before: "approved in March 2025" (passage silent) becomes "approved in early 2025".
After: sentence removed; name the gap. (R5, VR-H1)

**C6 Silence read as contradiction.** A passage that does not mention a point is reported
as saying the opposite.
After: "your passage does not say this", not "your passage says otherwise". (R6)

**C7 The figure that survives a partial.** The passage supports the comparison but not
the number, and the number stays.
After: keep only what the passage states; drop the figure; recheck. (R5)

**C9 The simulated status.** Without VERIFY, results are written as "supported" or
"partial", as if a tool ran.
After: manual result words and "not tool-checked". (VR-H4)

**C10 The unchecked rewrite.** A sentence is rewritten to match the passage and kept
without a second check.
After: recheck the rewrite, or label it "rewritten, not tool-checked". (VR-H4)

**C15 Supported read as true.** "Supported" is reported as "verified", "correct" or "true".
After: "your passage says this", plus the plain-words line on what a match means. (VR-H3, R5)

## Requests and framing

**C3 The paraphrased passage.** The assistant writes a summary of the source and checks
the claim against its own summary.
After: quote the source word for word with a locator. (R4, R5)

**C8 The unnamed authority.** "Experts agree", "guidelines recommend".
After: name and supply the source, or remove the sentence. (R5)

**C12 "Just mark them all supported."** Labels without a check.
After: decline plainly; offer to check now or mark them "not checked". (VR-H3, VR-H4, VR-H5)

**C16 Bronze upgraded.** A bronze passage is reported as supported because it "looks official".
After: at most partial; rationale source tier bronze. (R6)
