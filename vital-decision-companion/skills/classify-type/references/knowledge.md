# Knowledge - classify

Step context: **Frame**.

## Migrated working rules

# Rules for Classify

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** decision_classify is a keyword draft. rationale says so. draft is true.
- **R2.** Read decision_type and recommended_rigor back in one sentence. Ask the person to confirm.
- **R3.** Store rigor on how_to_decide with decision_run_stage only after the person confirms.
- **R4.** A statement with no keyword returns decision_type null and a gap. Say the pack has no row.
- **R5.** Types in this pack: response_customer, tradeoff_resource, sequence_strategic, go_nogo_people, prioritization_operational, pivot_strategic, escalation_risk, standard_setting.
- **R6.** how_to_decide is complete only when statement, goal, and rigor are all present.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Classify

## Pattern 1

Statement mentions a budget reallocation. Draft type tradeoff_resource, rigor tradeoff. Ask for a yes.

## Pattern 2

Statement is "we should do better." No keyword. Gap. Ask them to name the type.

## Pattern 3

Person confirms. Store statement, goal, and rigor together.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
