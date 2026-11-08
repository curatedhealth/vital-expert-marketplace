# Knowledge — VERIFY handoff

Migrated from legacy rules + patterns (read-only archives may remain on disk).

## Rules

# Rules for Verify handoff

Pack: vital-mlr-review. Method version: 0.3.1.

- **R1. `vital-mlr-review:mlr_handoff_verify` first — it does not call Verify.**
- **R2. One vvfy_ connector; no second claim checker.**
- **R3. Happy path `vital-verify:qualify_source` → `vital-verify:check_claim`.**
- **R4. Never invent statuses without tools.**

Hard rules MLR-H1 through MLR-H8 in `SKILL.md` still apply.

## Patterns (teaching only — MLR-H2)

> **Teaching material — never input.** The situations below are invented for shape (MLR-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Verify handoff

## Pattern 1

No vvfy_ → mark-unchecked task.

## Pattern 2

Inadmissible source → claim stays out.

## Pattern 3

Partial → board sees partial, not supported.

## World-class depth notes (8 November 2026)
- Handoff packet preserves claim text + passage + locator.
- Without vvfy_, never print tool-checked VERIFY results.
- Passage support can coexist with misleading-omission flags for chairs.

## Operating memory (world-class)
- Status vocabulary is closed: findings_only | revise | human_gate_required | prep_complete.
- Liability line is mandatory on user-facing closes.
- Teaching examples are never live inputs (MLR-H2).
- Offline-first Hybrid B: local CLI before MCP.
- Pilot: no marketplace publish without owner yes.
- Chair isolation: Medical ≠ Legal ≠ Regulatory.
- Markets never silently default to the United States.
- VERIFY overlap ≠ clearance; stamp discipline via stamp_ready_line.py.

### Skill-specific memory — mlr-verify-handoff
Own the job in SKILL.md boundaries; refuse out-of-scope themes; stamp every close.
