## Changelog

### Curator steward skills (Draft additive — 8 November 2026)
Added Curator side-channel skills on this pack home: `pull-evidence`, `classify-incoming`, `file-and-process`, `steward-decide`, `enrich-record`. `.mcp.json` now includes `vital-ontology-curator` (`vcur_`). **Not** a Marketplace republish / Done claim for Curator skills — owner must authorize publish separately. Paraphrase-only chrome; no Lane A quote redistribution.

### 0.3.0-live-test (8 November 2026)
Marketplace v1 live-test close: C1–C5 owner Pass; C6 Gate H Pass-with-exceptions (WR-032 closed; VP-ON-C6 Option A internal pack); eng_enforcement_green; C7 facilitation eng-bound (independent grade deferred). Claude buyer id `vital-navigator-outcomes` (legacy `navigator-ai-investment`). Listing chrome paraphrase-only. Production frontend smoke: `/navigator` + ontology explorer.

### 0.2.1 (7 November 2026)
Remaining uplift W0–W6: live smoke offline path, KA suite, substrate CF-01.06.01, marketplace republish pack, Decision Room UI route.

# VITAL · Outcome Navigator (Marketplace v1 live-test, v0.3.0)

Investment decisions and measurement — from value-at-stake to value realized. Peer use-case-family plugin to Launch Navigator. GenAI is the first worked vertical, not the brand.

**Status:** Marketplace v1 live-test (`0.3.0-live-test`). Anatomy upgrade from marketplace pack `navigator-ai-investment` (legacy alias retained until buyer install smoke retires it). Expert review **Pass** (Hicham Naim, 7 November 2026). Capability code **pinned CF-01.06.01**. Non-claims: C7 KA not independently graded; host OAuth/SSRF parallel; Lane A quotes not redistributed in buyer chrome.

## Tier
Standard (authoring standard): known-answer / smoke fixtures; practitioner review still due.

## Rules this plugin follows
- People score; the AI never scores, weights, chooses or signs.
- Evidence classes: M measured, V asserted by a document, H design proposal. [CHECK] = rule not traced to a dated primary source. [GAP] = fact missing, never filled.
- Offline first; connectors add cited data.
- Integrity pack before claim-bearing board packs; exhibits must be honestly framed.
- Shared 10-part decision record (non-gate path): Proceed / Investigate first / Handle it internally — not Launch Pass/Conditional/Hold/Escalate.

## What is in this plugin
| Part | Path | Role |
|---|---|---|
| Recommended agent | agents/outcome-navigator-agent.md | WORKER |
| Capability map | skills/outcome-navigator-capability-map/ | missions + integrity + routing |
| Spine + packs | skills/<verb-object>/ | decision, measurement, exhibits, integrity |
| Connectors | connectors.md | use-for / never-for / offline |
| Commands | commands/start-outcome-navigator.md | entry |

## Back-test and expert review
Expert review: **Pass** — `diligence/EXPERT_REVIEW_LOG_2026-11-07.md` (live prod test after deploy).  
Back-test: not run. Known-answer: spine rubrics present; twelve added skills still smoke-level (`diligence/METHODOLOGY_GAP_REVIEW_2026-11-07.md`).

## Flags
[CHECK] means a rule is not traced to a dated primary source. [GAP] means a fact is missing and was not filled.

## Depends on
vital-core-atoms (compose-draft, compare-against-criteria, rank-by-consequence, classify-text-labels). Ontology Navigator, Decision Companion (FOCUSED), Verify and Curator via connectors.

## Not covered
Portfolio & Launch Excellence (CF-04.01.09) and all vital-launch-navigator skills. Asset valuation / deal thesis grading (due-diligence valuation plugins). READY M/L/R chairs and promotional approval. Function analyses (HTA, regulatory pathway, etc.) — consume their outputs, never produce them.
## Kit depth (honesty)

As of 7 November 2026 every job skill (all 25) carries the ANATOMY Standard kit plus
diligence scaffolding: patterns, tools, source-register, grounding-register, verbatim
scaffold, assets/, and enriched good/poor worked examples (GenAI vertical). Peer methods
from TRUSTED / FOCUSED / LN / READY are adapted and tagged [CHECK].

See `diligence/HONEST_GAP_REGISTER.md`. This remains **Draft**: lint green ≠ production.
Still open: expert review, real known-answer/back-test, CF02 pin, marketplace republish,
primary verbatim passages.


## Live test
Operator smoke (canonical): `diligence/OPERATOR_SMOKE_NAVIGATOR_FRONTEND_2026-11-08.md` — `/navigator` + ontology explorer. Historical connector notes: `diligence/LIVE_TEST_PACK_CF-01.06.01_2026-11-07.md` (Decision Room / B2–B4 retired as product smoke).
