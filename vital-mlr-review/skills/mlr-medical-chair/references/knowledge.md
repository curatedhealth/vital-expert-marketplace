# Knowledge — Medical chair

Migrated from legacy rules + patterns (read-only archives may remain on disk).

## Rules

# Rules for Medical chair

Pack: vital-mlr-review. Method version: 0.3.1.

- **R1. Apply only chairs.medical checklist items.**
- **R2. Every finding has claim_span, severity, rationale, applies_to[].**
- **R3. Same artefact_version as intake.**
- **R4. Hand legal/regulatory questions to sibling chairs.**

Hard rules MLR-H1 through MLR-H8 in `SKILL.md` still apply.

## Patterns (teaching only — MLR-H2)

> **Teaching material — never input.** The situations below are invented for shape (MLR-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Medical chair

## Pattern 1

No PI text → [GAP]; do not invent label.

## Pattern 2

ISI missing → hand to regulatory chair.

## Pattern 3

Disparagement → hand to legal chair.


## Fair balance / ISI (peer skill)
Prominence and ISI net-impression prep lives in `mlr-fair-balance-isi` (WC-US-OPDP). Medical chair stays on clinical/label accuracy; do not collapse fair-balance into a single 'approve' finding.

## World-class depth notes (8 November 2026)
- Population, dose, indication, contraindication, and safety statement mismatches are in-scope.
- Each finding needs pasted evidence; "generally known" is invalid (MLR-H1).
- Do not absorb comparative-ad or privacy issues (Legal).

## Operating memory (world-class)
- Status vocabulary is closed: findings_only | revise | human_gate_required | prep_complete.
- Liability line is mandatory on user-facing closes.
- Teaching examples are never live inputs (MLR-H2).
- Offline-first Hybrid B: local CLI before MCP.
- Pilot: no marketplace publish without owner yes.
- Chair isolation: Medical ≠ Legal ≠ Regulatory.
- Markets never silently default to the United States.
- VERIFY overlap ≠ clearance; stamp discipline via stamp_ready_line.py.

### Skill-specific memory — mlr-medical-chair
Own the job in SKILL.md boundaries; refuse out-of-scope themes; stamp every close.
