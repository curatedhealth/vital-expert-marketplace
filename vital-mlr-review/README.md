# VITAL READY (MLR Ready) — Cowork plugin

**release_state: Released** · version **0.4.2** · Hybrid B offline-first.


READY prepares an MLR board packet offline with local rulesets and validators. Add a `vmlr_` key only for metered cloud tools or a durable prep record. Add `vvfy_` only when you want live VERIFY. Humans still approve.

## Install

1. Marketplace: `curatedhealth/vital-expert-marketplace` → **vital-mlr-review** (marketplace tip).
2. Default: **no keys required**. Skills + `tools/` run intake → chairs → compile → board pack locally and stamp `READY-local` / `not tool-checked` / `not metered`.
3. Optional: paste personal `vmlr_` for metered cloud MLR tools or durable prep record; paste `vvfy_` for live VERIFY. See `references/mcp-opt-in.md`.

Connector (optional): `https://mcp.vital.expert/api/mcp/mlr-review`

## Skills (v0.4.0 — Released — Hybrid B + Standard — **11 skills**)

Taxonomy challenge: `../../READY_SKILL_TAXONOMY_CHALLENGE_2026-11-08.md`.

| Skill | Role |
|---|---|
| `mlr-capability-map` | Routebook: TRUSTED vs VERIFY vs READY; skill index |
| `mlr-channel-intent` | Promo vs scientific exchange vs med_info gate |
| `mlr-intake` | Markets, channel, authorized use, load rulesets (offline CLI) |
| `mlr-claims-matrix` | Pre-chair verbatim claims + locators + authorised-use bind |
| `mlr-medical-chair` | **M** — label/clinical accuracy, evidence adequacy |
| `mlr-legal-chair` | **L** — misleadingness, comparative-ad, privacy/IP |
| `mlr-fair-balance-isi` | Fair balance / ISI / net impression prep |
| `mlr-regulatory-chair` | **R** — format, pre-approval gates, code process |
| `mlr-compile` | Align chairs; validate; conflict matrix; reconciliation |
| `mlr-verify-handoff` | Build VERIFY paste packet offline; live VERIFY only with `vvfy_` |
| `mlr-board-prep` | Reviewer pack + named-human prep record (`mlr_reviewed` stays false) |

**Do not blend M / L / R.** Fair-balance/ISI is a dedicated prep skill; Regulatory still owns format/gates.

## Offline happy path (default)

See `workflows/offline-prep-e2e.md`.

1. `mlr-capability-map` → `mlr-channel-intent` when channel is disputed.
2. `mlr-intake` with explicit markets (never US-default).
3. `mlr-claims-matrix` before chairs.
4. Chairs + `mlr-fair-balance-isi` (parallel prep).
5. `mlr-compile` → validate offline.
6. Optional `mlr-verify-handoff` (packet only unless `vvfy_` present).
7. `mlr-board-prep` with a named human → company MLR SOP.

Stamp every close with:

```bash
python tools/stamp_ready_line.py --skill mlr-board-prep --letter-lines
```

## Liability

Every summary ends with: *This prepares material for human MLR review. It is not medical, legal, or regulatory approval.*

## License

Proprietary — Crossroads Catalyst GmbH (Vital Expert). See `LICENSE`. `release_state: Pilot` until owner yes for Released.
