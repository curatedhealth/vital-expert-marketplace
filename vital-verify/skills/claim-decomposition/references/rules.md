# Primary rules this skill applies

Last reviewed: 20 October 2026.

| Id | Rule | Primary source | Status |
|---|---|---|---|
| R1 | Claims in promotional material must be capable of substantiation. | IFPMA Code 2019 §4.3; ABPI 2024 clauses 6.1–6.2 | Confirmed 20 October 2026 (same sources as support-decision R1–R3) |
| R2 | `extract_claims` returns claims with offsets; it never decides support. Offsets are indexes into the exact submitted text. | VERIFY connector schemas / `mcps/verify`, 19 October 2026 | Confirmed from schemas |
| R3 | Claim kinds and checkable defaults: see `claim-kinds.md`. Normative and definitional are checkable false, not failures. | Verify method, 19 October 2026 | `[CHECK]` Method document, not an external standard |

R1 is for promotional stakes. For internal notes, splitability is good practice (VR-H8).
