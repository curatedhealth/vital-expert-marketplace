# Knowledge — Compile

Migrated from legacy rules + patterns (read-only archives may remain on disk).

## Rules

# Rules for Compile

Pack: vital-mlr-review. Method version: 0.3.1.

- **R1. Require chairs.medical, chairs.legal, chairs.regulatory separately.**
- **R2. Version pin or fail.**
- **R3. Forbidden phrases → validation error.**
- **R4. Next: verify-handoff optional, then board-prep.**

Hard rules MLR-H1 through MLR-H8 in `SKILL.md` still apply.

## Patterns (teaching only — MLR-H2)

> **Teaching material — never input.** The situations below are invented for shape (MLR-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Compile

## Pattern 1

Mixed chair decisions → conflict slot; do not launder.

## Pattern 2

Stub FR → explicit gap in coverage.

## Pattern 3

Fail-close row open + chair approve → never `prep_complete`; the status follows the shared map: a correctable copy fix → `revise`, a human judgment call or a chair disagreement → `human_gate_required` (TEH-RDY-027).


## Reconciliation
After conflicts or claim edits, follow `../../workflows/reconcile-after-findings.md` and `../../templates/reconciliation-loop.md`. Do not launder disagreements into a composite approval.

## World-class depth notes (8 November 2026)
- Schema validity is necessary, not sufficient.
- Checklist items map to owning skills; compile does not close them silently.
- prep_complete is owned by board-prep after human acceptance, not by compile alone.

## Operating memory (world-class)
- Status vocabulary is closed: findings_only | revise | human_gate_required | prep_complete.
- Liability line is mandatory on user-facing closes.
- Teaching examples are never live inputs (MLR-H2).
- Offline-first Hybrid B: local CLI before MCP.
- Pilot: no marketplace publish without owner yes.
- Chair isolation: Medical ≠ Legal ≠ Regulatory.
- Markets never silently default to the United States.
- VERIFY overlap ≠ clearance; stamp discipline via stamp_ready_line.py.

### Skill-specific memory — mlr-compile
Own the job in SKILL.md boundaries; refuse out-of-scope themes; stamp every close.
