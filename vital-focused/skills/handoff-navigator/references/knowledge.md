# Knowledge - handoff-navigator

Step context: **Score**.

## Migrated working rules

# Rules for Handoff to Navigator

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** Call decision_handoff_navigator first. called_navigator is false. This connector does not call Navigator over HTTP.
- **R2.** Speak Approach. suggested_stage_entry is options. compile_key is 4_options.
- **R3.** Then call the named tool on vital-ontology-navigator: decide_start or a methods_* tool.
- **R4.** methods_mcda_rank receives the same human cells, mapped as in references/tools.md. Decision Companion does not average them.
- **R5.** Check the scale. methods_mcda_rank needs 0 to 4. Ask the person how to map any other scale; never rescale silently.
- **R6.** Several raters go one call per rater, or into the governed Navigator flow with decide_attach_scores. Never average them here.
- **R7.** Without a vont_ key, say the shared tool is not connected.
- **R8.** People supply scores. The coach does not. A Navigator result informs the choice; it is not the choice.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Handoff to Navigator

## Pattern 1

Person asks for the score on Ontology Navigator (an optional extra). Packet first. Then methods_mcda_rank with Ada's cells.

## Pattern 2

No vont_ key. Stop after the packet. Say the shared tool is not connected.

## Pattern 3

Person wants an ontology record. decide_start with intent decision. Do not rebuild Navigator stages here.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
