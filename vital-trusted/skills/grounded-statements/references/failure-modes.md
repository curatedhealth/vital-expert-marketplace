# Failure modes

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-GS-01 | Model-memory fill | Was a gap filled from training knowledge not the passage? | Grounding | TR-H1 | VERIFIED practice |
| FM-GS-02 | Exploratory as primary | Was a secondary/exploratory result stated as the primary finding? | Hierarchy | TRUSTED grounded | [CHECK] |
| FM-GS-03 | Silent on non-significant primary | Was a failed primary endpoint omitted beside a positive secondary? | Completeness | TRUSTED grounded | PARTIAL |
| FM-08 | Tool status treated as world-truth | Is a local or Verify status described as "true in the world"? | Prove honesty | VERIFY / TRUSTED Prove | VERIFIED |

Skill-specific rows for `grounded-statements`. Shared FM-08 is universal Prove honesty.
