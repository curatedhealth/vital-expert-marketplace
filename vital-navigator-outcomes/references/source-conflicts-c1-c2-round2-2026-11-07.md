# Source conflicts — C1/C2 round 2 (7 November 2026)

Authority posture: [`authority-and-evidence-posture.md`](authority-and-evidence-posture.md).  
Lane A catalog: [`lane-a-sources-c1-c2-2026-11-07.md`](lane-a-sources-c1-c2-2026-11-07.md).  
Round-2 findings: [`../diligence/c1-c2-round2-exports-2026-11-07/C2_Lane_A_Findings_Review.md`](../diligence/c1-c2-round2-exports-2026-11-07/C2_Lane_A_Findings_Review.md).

These conflicts are **documentation and integration guardrails**. They do not authorize formula change, silent scale conversion, canvas quadrant import, or synthetic-as-human evidence.

---

## Primary conflicts (must not cause regressions)

### SC-C1C2-R2-03 — Top-two-box proportions vs locked 1–10 descriptions

| Field | Detail |
|---|---|
| Sources | Strategyn *Quantify Your Customers' Unmet Needs* (2019) — ordinal / top-two-box proportions [LA-STRAT-QUANT-2019]; current Navigator template and GOV-06 — whole numbers 1–10 on Importance and Satisfaction [NAV-O, O10] |
| Issue | Two pipelines describe different raw response geometry and aggregation. No precise equivalence, chronological migration rule, or shared estimand has been established. |
| **Disposition** | **Provenance required; no silent conversion.** Draft protocol `VITAL-ODI-TTB-1_10-v0` lives at `owner-protocols/` with **empty mapping until signed**. Runtime accepts a top-two-box bridge only when `owner_protocol_ref` is in `SIGNED_OWNER_PROTOCOLS` (currently empty) — unsigned draft ids are refused except test fixtures with `allow_unsigned_protocol_for_fixture`. |

### SC-C1C2-R2-04 — Unclamped Strategyn display vs locked `I + max(0, I − S)`

| Field | Detail |
|---|---|
| Sources | 2019 Strategyn page displays `I + (I − S)` without a floor; locked template and DR-0827 / O11 use `I + max(0, Importance − Satisfaction)` |
| Issue | Pedagogical or marketing copy on an external page does not match the ratified compute contract. |
| **Disposition** | **Compute stays clamped** (`formula_locked`). Pedagogy may mention the unclamped source display only as **non-authoritative** historical discrepancy — never as an instruction to change the engine or validators. Regression inputs remain: I8/S9→8; I7/S7→7; I9/S3→15; I1/S1→1; I10/S1→19. |

### SC-C1C2-R2-05 — High/high landscape label contradiction

| Field | Detail |
|---|---|
| Sources | JTBD Canvas (2024 upload) — high importance + high satisfaction as **table stakes**; low importance + high satisfaction as overserved in canvas prose; current plugin/engine bands use **overserved** language for low opportunity scores and VITAL opportunity bands (extreme / strong / moderate / low) [O11, NAV-O] |
| Issue | Quadrant marketing labels on the canvas do not align with the plugin's approved opportunity-band narrative. Cannot infer universal numerical cutoffs from prose. |
| **Disposition** | **Owner decision locked (Draft, 7 Nov 2026):** keep VITAL opportunity bands only — see `diligence/OWNER_DECISION_SC05_LANDSCAPE_LABELS_2026-11-07.md`. **No canvas quadrant / table-stakes import.** Countersign line on that file remains HITL; code already refuses other `landscape_label_mode` values. |

---

## Documentation quarantine (brief SC entries)

These are catalogued for cite hygiene and reviewer awareness. They do **not** open new runtime rules beyond what Round-1 absorb already locked.

### SC-C1C2-R2-01 — SDG manifesto date vs upload path (same as Round-2 brief SC-01)

| Field | Detail |
|---|---|
| Issue | PDF URL path contains `2024`; document states **created 16 March 2016** |
| **Disposition** | Catalogue **publication year 2016**; upload/filename year is not document year. |

### SC-C1C2-R2-02 — Bain one decider vs group Decide with rule (SC-02)

| Field | Detail |
|---|---|
| Issue | Older Bain/RAPID wording favors one decider; **Bain 2023** permits group Decide when a resolution rule is documented |
| **Disposition** | Cite bounded 2023 wording in methods; **preserve locked group allowance** with `authority.kind` + `resolution_rule` — do not force fictional solo Decide. |

### SC-C1C2-R2-06 — Variable Strategyn sample-size ranges (SC-06)

| Field | Detail |
|---|---|
| Issue | Strategyn pages cite different suggested N ranges (e.g. 120–1200 vs 180–3000). Neither is a universal validity threshold. |
| **Disposition** | **No fixed sample-size validity rule** in the plugin. Workshop attendance or convenience N does not prove representativeness. Study design must be justified per question; AAPOR nonprobability precision guidance is **disclosure and inference discipline**, not a substitute threshold. |

### AAPOR — authority lane quarantine

| Artifact | Role in plugin |
|---|---|
| AAPOR Best Practices (wording, pretest, missingness) [LA-AAPOR-BP] | Survey craft warrants — one-concept items, intended-respondent pretest, missing vs substantive options |
| AAPOR 2026 formal disclosure elements [LA-AAPOR-DISC-2026] | Public-reporting / Transparency Initiative context — **not automatically law** for internal workshops |
| AAPOR AI task-force report [LA-AAPOR-AI-2026] | Professional guidance on AI use, synthetic validity risks, task-specific human evaluation — **not a universal ban** on synthetic research |

**Disposition:** Retain exact document versions in the catalog. VITAL owns the **stricter human-score pipeline** (no synthetic-as-human, no AI-filled ratings). Do not collapse AAPOR artifacts into one "AAPOR says" warrant.

---

## Related precaution (not a numbered SC)

Some Strategyn pages suggest opportunity "almost never lives in Execute." **Do not** promote that into a rule that **excludes Execute from elicitation**. Interview may start at Execute (WR-013); inspect all job steps without predetermining where unmet needs sit.

---

## Licensing note (Strategyn canvas)

JTBD Canvas declares **CC BY-NC-ND 4.0**. Source citation ≠ commercial redistribution or modification clearance. Ship original VITAL prose; rights review before redistributing branded artifacts.
