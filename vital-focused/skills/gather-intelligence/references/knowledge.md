# Knowledge - gather-intelligence

Step context: **Unknowns**.

## Migrated working rules

# Rules for Gather intelligence

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** Notes source is owner, participant, or draft. Any other source is refused.
- **R2.** A draft source is stored with draft true. Say the note is a draft.
- **R3.** The stage completes only through decision_run_stage with knowns and unknowns. decision_attach_notes alone never completes it.
- **R4.** An unknown stays in the unknowns list (never filled) until the person or a handed-off tool supplies it.
- **R5.** Ask for disconfirming evidence for the option the person is leaning toward. Seeking only confirming facts is the confirmation-bias trap.
- **R6.** For estimates, ask for the base rate or reference class before case details.
- **R7.** This skill does not call catalogue, literature, trials, or label connectors.
- **R8.** When the person needs their own weights and ratings added up, name the tradeoff skill (`decision_score`). Only if they ask for a sealed score on Ontology Navigator, name handoff-navigator. When they need a claim checked, name handoff-verify.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Gather intelligence

Sources for the method: the Playbook Gather Intelligence stage (Part 8: six intelligence questions, source quality, disconfirming evidence); reference-class forecasting (Kahneman & Tversky; Flyvbjerg 2006).

## Pattern 1

Person lists three knowns and says the rival share is unknown. Store both. Share stays in the unknowns list. Then store the stage with knowns and unknowns.

## Pattern 2

Person pastes a sentence and asks if the source supports it. Do not answer here. Open handoff-verify.

## Pattern 3

source draft. Tell them the note is a draft before it is treated as a known.

## Pattern 4

Person estimates launch in six months. Ask how long the last comparable launches took before discussing this one.

## Pattern 5

Room agrees fast. Ask the disconfirming question: what would have to be true for this option to fail?

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
