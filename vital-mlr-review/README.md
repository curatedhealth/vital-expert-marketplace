# VITAL MLR Review (Cowork plugin)

Prepare Medical–Legal–Regulatory **board packets** on the host you already use.  
Your model writes chair findings. VITAL tools supply multi-jurisdiction rulesets, validation, and VERIFY handoff. **Nothing here approves copy.**

## Install

1. Marketplace: `curatedhealth/vital-expert-marketplace` → **vital-mlr-review** (when published).
2. Paste personal `vmlr_` key when prompted.
3. Optional: paste `vvfy_` for VERIFY (same connector as **vital-trusted** / **vital-verify**). Do not add a second Verify server.

Connector: `https://mcp.vital.expert/api/mcp/mlr-review`

## Skills (v0.3.1 — complete set of 8, Anthropic-aligned)

Each skill matches VITAL gold **and** Anthropic Agent Skills practice: third-person description (“This skill should be used…”), imperative body, progressive disclosure, 10 route phrases, `references/{tools,rules,patterns,gap-rules,governance}.md`, formula tasks, worksheet output, teaching example, routing evals, fully qualified MCP names (`vital-mlr-review:…` / `vital-verify:…`), and deterministic `scripts/` where checks are fragile. Regenerator: `mcps/mlr_review/scripts/harden_skills.py`. Harness: `mcps/mlr_review/tests/test_skills.py`.

| Skill | Role |
|---|---|
| `mlr-capability-map` | Routebook: TRUSTED vs VERIFY vs MLR; M / L / R index; hard rules |
| `mlr-intake` | Markets, channel, authorized use, load rulesets |
| `mlr-medical-chair` | **M** — label/clinical accuracy (FDA/CFR, Directive/EFPIA, ABPI, HWG, Swissmedic…) |
| `mlr-legal-chair` | **L** — misleadingness, comparative-ad, privacy/IP |
| `mlr-regulatory-chair` | **R** — ISI/format, pre-approval gates, code process |
| `mlr-compile` | Align three chairs; validate; conflicts |
| `mlr-verify-handoff` | Compose VERIFY (`qualify_source` → `check_claim`) |
| `mlr-board-prep` | Reviewer pack + named-human prep record (`mlr_reviewed` stays false) |

**Do not blend M / L / R.** Each chair loads only its ruleset slice.

## Happy path

1. `mlr-capability-map` or straight to `mlr-intake` with explicit markets (include a non-US set once).
2. `mlr-medical-chair` → `mlr-legal-chair` → `mlr-regulatory-chair`.
3. `mlr-compile` → `mlr_validate_packet`.
4. Optional `mlr-verify-handoff`.
5. `mlr-board-prep` with a named human → company MLR SOP.

## Liability

Every summary ends with: *This prepares material for human MLR review. It is not medical, legal, or regulatory approval.*
