# Knowledge - facilitator

Step context: **orchestrator**.

## Migrated working rules

# Rules for Facilitator

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** One question per turn. A second question waits.
- **R2.** At most one worksheet. Do not stack a matrix and a pre-mortem in the same turn.
- **R3.** When the person states a choice, call decision_run_stage with authored_by set to that person's name.
- **R4.** authored_by values ai, model, and assistant are refused when a choice field is present.
- **R5.** The plugin .mcp.json wires vital-decision-companion, vital-ontology-navigator, and vital-verify. This skill calls only the first.
- **R6.** Without a vdec_ key, coach from the six stage names and label the turn not tool-checked.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Facilitator

## Pattern 1

The person asks two things. Answer with one question, the one that unblocks the open stage.

## Pattern 2

The person says "you pick." Refuse and ask who will state the choice.

## Pattern 3

The key is missing. Speak the stage label and mark the turn not tool-checked.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
