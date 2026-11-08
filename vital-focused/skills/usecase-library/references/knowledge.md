# Knowledge - usecase-library

Step context: **library**.

## Migrated working rules

# Rules for Use-case library

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** Gold ids are UC01, UC02, and UC05. Any other id returns card null and the gold set.
- **R2.** Walk beats in order. One beat, then a question.
- **R3.** The card's decision_type and rigor are applied to the session only when session_id is passed and those fields are still empty.
- **R4.** Do not treat a beat as the person's choice.
- **R5.** leverage_packages name other connectors. This skill does not call them.
- **R6.** Playbook content version is 2026-10-26.2.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Use-case library

## Pattern 1

Person asks for a vendor example. UC05. First beat: write the job the vendor must do.

## Pattern 2

Person asks for UC03. card is null. Say the connector set is UC01, UC02, and UC05.

## Pattern 3

Person says "use the example's answer." Refuse. The beats are a walk, not a choice.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
