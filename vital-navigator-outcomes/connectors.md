# Connectors — Outcome Navigator (CF-01.06.01)

Live tools vs offline scripts. Behavior below is code-path grounded where noted; **re-smoke on Navigator frontend `/navigator` + ontology explorer** (`OPERATOR_SMOKE_NAVIGATOR_FRONTEND_2026-11-08.md`). Empty connector → `[GAP]` or `[CHECK]`, never invent.

Rule: live data → connector; offline → bundled skill scripts. Counted calls draw on plan allowance; check `my_usage` first.

---

## Ontology Navigator (`vont_` / Ontology_Navigator)

| Tool | Use for | Never for | Without it |
|---|---|---|---|
| `my_usage` (free) | allowance before counted runs | — | proceed offline; say once that usage is unknown |
| `catalogue_search` / `catalogue_list_children` | VD themes/levers/drivers by spoken name; DC lookups when owner asks | inventing catalogue rows; passing `function` on VD (wipes results) | frozen theme table in audience-calibration (say "as last read") |
| `bridge_*` | ontology bridges already on the graph | fabricating links | `[GAP]` |
| `methods_nav_compute` (`nav.sizing`, option templates) | compute on **people-entered** scores | scoring on a person's behalf; `nav.value_drivers` via this tool | skill local scripts (same formula); say connector failed once |
| `decide_start` | open brief (`intent` decision \| direction) | empty/unknown intent | draft contract in conversation only |
| `decide_attach_scores` / `decide_release_scores` | store/release named-person cells | AI as rater_id; inventing cells | keep scores in session worksheet |
| `decide_build_record` / prepare signoff | assemble unsigned record | assistant `signed=true`; Launch gate verdicts | `compile-board-pack` + `close-the-decision` templates offline |
| `decide_*` challenge helpers | dissent / assumptions slots when wired | inventing dissent names | Companion / facilitation lists |

Pitfall: tool docs may say `result_hash`; code returns `trace.inputs_hash` — do not cite a missing hash.

---

## Decision Companion / FOCUSED

| Use for | Never for | Without it |
|---|---|---|
| widen-options, tradeoff, premortem, gut-check, record-dissent, unsigned brief | naming a winner; filling unknowns from memory; signing | skill question lists + offline worksheets |

---

## VITAL Verify (`vvfy_`)

| Use for | Never for | Without it |
|---|---|---|
| `qualify_source` then `check_claim` on board-pack claims | inventing a figure; calling a sentence world-true without a quoted passage | label **not tool-checked**; run honesty cut by hand (`ground-the-numbers` / `cut-the-slop`) |

`external_ok` only when posture=`verified` and all claim-bearing lines tool-checked (`handoff-verify`).

---

## Ontology Curator (via Navigator)

| Use for | Never for | Without it |
|---|---|---|
| evidence figures with `{record_id, version, grade}` from the store | inventing when empty; minting steward ids | `[GAP]`; `handoff-evidence-steward` proposal only |

---

## Sibling plugins (hard stop)

| Sibling | Consume as | Never produce |
|---|---|---|
| Launch Navigator | gate dossier inputs as V | Pass/Hold/Escalate; G1–G5 verdicts |
| READY | MLR chair outputs as V | "MLR approved" chrome |
| Due diligence / Valuation | deal grades as V | inventing valuation grades |
| Function plugins (HTA, regulatory, …) | analysis products as V | re-running their method as Outcome skills |

---

## Offline scripts (always available)

`routing_check`, `frame_check`, `leak_screen`, `baseline_check`, `sizing_check`, `value_check` (drivers|range|benefit_profile|layers), `traceability_check` (TRC-V01…V10), `outcome_statement_check`, `outcome_priority_check`, `options_check`, `sensitivity_exhibit`, `placement_check`, `exhibit_check`, `chart_scale`, `reader_fit_check`, `grounding_check`, `substance_check`, `record_check`, `verify_handoff_check`, `steward_handoff_check`, `board_pack_check`, plus delivery/trial/capability scripts. These validate or compute from team JSON; they never invent inputs. Lane A catalog: `references/lane-a-sources-c1-c2-2026-11-07.md`, `references/lane-a-sources-c3-2026-11-07.md` (C3 investment choice).

---

## C3 — MCDA, readiness, portfolio, sensitivity (7 November 2026)

**Offline-first** for C3 skills unless a brief is open and the connector shape is confirmed. Humans supply weights, scores, ordinals and coordinates. **Proceed** vocabulary is owner close (GOV-04 §9), never sensitivity output.

| Tool | Scale / role | Boundaries |
|---|---|---|
| `methods_nav_compute` / `options_check` | **1–10** whole-number option cells (I7) | No AI scores; no opportunity→$; no silent 0–4 conversion |
| `methods_mcda_rank` | Human **0–4** scores + human weights — **VITAL adaptation**; original 2008 EVIDEM = **0–3** scores, **1–5** weights (LA-C3-010) | Not faithful EVIDEM without edition audit; not swing weighting if direct importance |
| `methods_risk_tornado` | Risk/driver tornado on declared model | **≠** MCDA weight sweep (`run-weight-sensitivity`) |
| `portfolio_place` | Brief-scoped candidate placement fields only | No invented x/y/bubble; grid metadata offline until versioned adapter |
| Readiness path | `readiness_check` / `maturity_check` + worksheets | No maturity %; no MLR waiver; no ORIC schema invention |

Detail per skill: `skills/compare-options|run-weight-sensitivity|assess-strategic-readiness|place-the-portfolio/references/tools.md`.
