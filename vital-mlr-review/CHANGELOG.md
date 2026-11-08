# Changelog — vital-mlr-review (READY / MLR Ready)

## 0.4.0 — 8 November 2026 (Pilot)

- Hybrid B + Standard: offline-first fold-in of the full `mlr-review` MCP tool surface into `tools/` (intake, list/get rulesets, packet schema, validate, align claims, compile checklist, VERIFY handoff packet, prep record).
- Ship local `rulesets/` + `schema/` with the plugin; stamp `READY-local` / `not tool-checked` / `not metered`.
- Empty default `.mcp.json` (opt-in). Optional `vmlr_` / `vvfy_` documented in `references/mcp-opt-in.md`.
- CF04 depth for all 8 skills: method kit, shared templates, good/poor examples, known-answer evals, `without-connector.md`.
- World-class digest + WC-* rows (access date 8 November 2026).
- LICENSE: Crossroads Catalyst GmbH. `release_state: Pilot` (not Released).

## 0.3.1 — prior

- Eight Anthropic-aligned skills with live MCP-first tools.md and per-skill scripts.

### 0.4.0 deepen — taxonomy challenge (same day)

- Challenged 8-skill set; added `mlr-channel-intent`, `mlr-claims-matrix`, `mlr-fair-balance-isi` (11 total).
- Templates: ISI checklist, channel-intent, claims-matrix, reconciliation, submission pack.
- Tools: `channel_intent_gate.py`, `check_isi_presence.py`, `mlr_claims_matrix_offline.py`.
- Workflows + hooks + `ready-pre-review-agent`.
- Hygiene: zero `assets/` / rules-patterns-gap path refs in skill `*.md`.

### 0.4.0 — Form 2253 deferral encoded

- Locked: no postmarketing filing skill in Pilot.
- Board cover + submission checklist + prep-record reminders; `references/post-clearance-deferred.md`.
- Workflows: reconcile-after-findings, post-clearance-human-ops-deferred.
- Tool: `check_submission_pack.py`; hooks refuse "file Form 2253" / FDA submit phrases.


### 0.4.0 — use-case registry + offline E2E (same day)

- `evals/USE_CASE_REGISTRY.json` + `.md`: **60** cases (5×11 skills + 5 journeys).
- Synced into each skill `daily_user_evals` (≥5); suite-evals lists all 11.
- `scripts/run_use_case_e2e.py` — registry + tool probes + DE/CH journey + meter + units.
- Runtime: refuse AI/assistant `cleared_by` (MLR-H5). `.mcp.json` empty Hybrid B restored.
- `tests/test_skills.py` updated for 11 skills / 0.4.0 Pilot (no PyYAML dep).

### 0.4.0 — world-class Pilot content uplift (same day)

- Hard meter: `scripts/world_class_meter.py` (Jaccard, offline tools.md, stamp, unique standards, knowledge floors).
- Rewrote all 11 `good-sourced-draft.md` with unique substance (no factory pads).
- Offline-first `tools.md` + `stamp_ready_line` on every skill; specialized `method-standards` / `without-connector`.
- `mlr-fair-balance-isi/references/standards-by-market.md`; pruned legacy `skills/*/assets/`.
- Regression: `tools/test_world_class_meter.py`. Closure: `../../READY_WORLD_CLASS_CONTENT_CLOSURE_2026-11-08.md`.
- **GRADE: world-class-pilot-content** (disk meter). Marketplace / Released still owner-gated.
