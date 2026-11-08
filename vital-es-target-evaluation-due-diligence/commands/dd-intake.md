---
name: dd-intake
description: Open buyer-side diligence intake — five questions, workstream RACI, red-flag register, worksheet. Use when starting target evaluation / DD (CF-01.02.06).
---

# Diligence intake (short session)

Facilitation command · not a product UI. Pattern twin of ON `decision-room`.

## When to use

Owner wants a structured start on an asset/company without walking every skill file yet.

## Flow

1. Route via capability-map (`hooks` `H-dd-intake`) — refuse ON investment verdict / READY approve / self-Pass.
2. Fill `templates/workstream-intake.md` (Alacrita-style five questions + F→…→IR order).
3. Fill `templates/worksheet.md`; seed `templates/red-flag-register.md` + `templates/hitl-raci.md`.
4. Apply `skills/.../capability-map/references/gap-rules.md` — `[GAP]` not silent assumptions.
5. Run workstreams only as named; each closes with skill QC + `tools/stamp_check_line.py`.
6. Assemble IR with `recommended=false`; deal lead confirms R-STATUS.
7. Preflight: `scripts/preflight_refuse_scan.py` + eng refuse smoke.

## Required outputs

- Intake + worksheet (UNSIGNED)
- Red-flag register (may be empty rows)
- HITL RACI named
- Gap list started (`templates/gap-list.md`)

## Hard don'ts

- No AI GO/NO-GO or recommend-sign
- No FTO / tax / QoE opinion from this plugin alone
- No ASC / FC-* / Full enable; no Marketplace Done claim
- No inventing COI clearances
