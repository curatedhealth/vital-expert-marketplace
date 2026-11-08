# Method: run-weight-sensitivity

Warrants: LA-C3-001 DESNZ 2024 (sensitivity as appraisal step); LA-C3-002 ISPOR 2016 (MCDA uncertainty steps); LA-C3-003 DCLG 2009 (stakeholder scenario sensitivity); LA-C3-011 EVIDEM 2018 (qualitative criteria outside incomplete numeric models). Catalogue: `references/lane-a-sources-c3-2026-11-07.md`.

## Purpose

Recompute option ranks under **human-approved** weight perturbations. **Diagnostic only** — sensitivity shows conditional rank fragility; it is **not** investment choice and must **never** emit Proceed · Investigate first · Handle it internally (OWNER vocabulary only; WR-C3-004…006).

## Diagnostic contract (WR-C3-004…006)

1. **Never choose.** Rank swaps and crossing intervals inform humans; the assistant does not select a winner, close a decision, or imply that stable numeric ordering resolves the whole decision (KA-ON-C3-018 class refusals).
2. **Conditional, not predictive.** Rank robustness within the declared model is not success probability, confidence in implementation, or a substitute for dissent scenarios.
3. **Retain qualitative exclusions.** Material criteria left outside the aggregate — including EVIDEM-style qualitative-only rows when anchors are not shared (WR-C3-021) — stay visible in the exhibit narrative; removing them to show a clean numeric winner is refused.
4. **Retain dissent.** Unresolved stakeholder perspectives may be shown as separate scenarios (LA-C3-003) without collapsing to one sweep result.

## Frozen base model

Before any sweep:

- Pin **score matrix**, **criterion anchors**, **aggregation rule**, and **model version** (same inputs as the base comparison).
- Base weights are **human-entered** and must sum to **1.0 ± 0.01** (existing rule).
- Changed **anchors** or **criteria set** are not a weight sweep — they require **model revalidation** and a new comparison pass, not a sensitivity bar in isolation.

Script `sensitivity_exhibit.py` computes weighted totals and rank swaps from team JSON only.

## Declared normalization

Every exhibit states:

- Which weight moved and over what **human-approved interval** (not assistant-invented bounds).
- **Redistribution rule** when one weight changes (e.g. remaining weights renormalized to sum to 1).
- **Output units** (same composite scale as base comparison, typically 1–10 offline).

Refuse hiding normalization — e.g. raising one weight to 70% while leaving others unchanged without disclosure (KA-ON-C3-005 class). Label unsupported redistribution as `[GAP]` until owners approve a convention.

## Ties and crossings

- **Ties** stay visible; the assistant does not break ties.
- **Crossings:** record rank order at base vs sweep; note **tie tolerance** if owners declare one.
- **"No crossing found"** means none within the **tested domain only** — not global robustness across anchor changes, option-set changes, or joint uncertainty.
- Interpretation (what instability means for the decision) is **human-only**.

## Optional one-way sweep convention (VITAL design, not law)

A **proposed** default for facilitated sessions (owners may override):

- Freeze scores; vary **one criterion weight at a time** within an owner-stated band (e.g. ±20% of base share, or explicit min/max).
- Distinguish **parameter sweep** from **multi-criterion perspective scenario** (different stakeholder weight vectors shown side by side, LA-C3-003).

This convention is **VITAL design** for worksheets and `sensitivity_exhibit.py`, not a claim that every external MCDA guide mandates identical mechanics.

## Scope separation

| Analysis | What it tests | What it does not prove |
|---|---|---|
| One-way weight sweep | Rank changes under declared weight bounds | Whole-decision robustness |
| Leave-one-scorer-out (compare-options I7) | Scorer influence on base rank | Sensitivity skill output unless re-run here |
| `methods_risk_tornado` (if wired elsewhere) | Risk/driver tornado on declared model | MCDA weight sweep — different tool contract |

Do not present tornado bars with unspecified inputs, units, or invented distributions.

## Outputs

Sensitivity exhibit: base rank, perturbations tried, swaps/crossings, qualitative exclusions noted. Feeds `compare-options`, `place-the-portfolio`, and board pack — **without** a route choice.

## Lane A absorb — C3 (7 November 2026)

C3 investment-choice boundaries for this skill only. Do not regress C1/C2 locked rules (no opportunity→$; humans score).

## Quotation rights (8 November 2026)

VP-ON-C3-* verbatim candidates carry `reuse_cleared: owner_internal_pack_yes` (owner Option A, 8 November 2026 — `diligence/OWNER_HITL_TRIAGE_C3_VP_REUSE_2026-11-08.md`). Internal method text only; not marketing, chrome, or external redistribution. Full verbatim landing remains optional; paraphrase/id pointers may remain until a deliberate landing edit. Does not clear VP-ON-C6.
