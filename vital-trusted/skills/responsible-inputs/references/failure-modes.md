# Failure modes

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-RI-01 | Public derivative of confidential | Was unpublished partner/CSR content pushed to a public pack? | Inputs | TRUSTED responsible-inputs | VERIFIED practice |
| FM-RI-02 | AI-use policy skipped | Was sensitive input pasted to a public tool without policy check? | AI policy | TRUSTED responsible-inputs | [CHECK] |
| FM-RI-03 | PHI assumed anonymized | Was identifiable data treated as fine without confirmation? | Privacy | TRUSTED responsible-inputs | PARTIAL |
| FM-08 | Tool status treated as world-truth | Is a local or Verify status described as "true in the world"? | Prove honesty | VERIFY / TRUSTED Prove | VERIFIED |

Skill-specific rows for `responsible-inputs`. Shared FM-08 is universal Prove honesty.
