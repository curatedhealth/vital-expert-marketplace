# Knowledge — Regulatory chair

Migrated from legacy rules + patterns (read-only archives may remain on disk).

## Rules

# Rules for Regulatory chair

Pack: vital-mlr-review. Method version: 0.3.1.

- **R1. Apply only chairs.regulatory items.**
- **R2. Format/process gates — not clinical truth.**
- **R3. Same artefact_version as intake.**
- **R4. Hand clinical/legal questions to sibling chairs.**

Hard rules MLR-H1 through MLR-H8 in `SKILL.md` still apply.

## Patterns (teaching only — MLR-H2)

> **Teaching material — never input.** The situations below are invented for shape (MLR-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Regulatory chair

## Pattern 1

ISI missing on product claim → regulatory finding.

## Pattern 2

Efficacy vs SmPC → medical chair.

## Pattern 3

Disparagement → legal chair.


## Fair balance / ISI (peer skill)
Use `mlr-fair-balance-isi` for ISI prominence checklists. Regulatory chair owns format/pre-approval/code process overlays; both feed compile — neither approves.

## World-class depth notes (8 November 2026)
- Approval status unknown + efficacy promo → human_gate_required.
- Form 2253 is deferred: only when US is a supplied market or the person asks, write one line `[DEFERRED] Form 2253 — out of READY scope`; never a finding, rule row or rule id; do not fake a filing path (TEH-RDY-025).
- Fail-close is a property of the rule row, not a status: a correctable wording or format finding is `revise`; a human judgment call (pre-approval, audience/channel gate on supplied facts) is `human_gate_required` (TEH-RDY-027); a missing audience, channel or ruleset is a `[GAP]` with `findings_only` (TEH-RDY-047).
- National advertising rules (e.g. HWG) stay market-scoped.

## Operating memory (world-class)
- Status vocabulary is closed: findings_only | revise | human_gate_required | prep_complete.
- Liability line is mandatory on user-facing closes.
- Teaching examples are never live inputs (MLR-H2).
- Offline-first Hybrid B: local CLI before MCP.
- Pilot: no marketplace publish without owner yes.
- Chair isolation: Medical ≠ Legal ≠ Regulatory.
- Markets never silently default to the United States.
- VERIFY overlap ≠ clearance; stamp discipline via stamp_ready_line.py.

### Skill-specific memory — mlr-regulatory-chair
Own the job in SKILL.md boundaries; refuse out-of-scope themes; stamp every close.
