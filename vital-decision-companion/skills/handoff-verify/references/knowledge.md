# Knowledge - handoff-verify

Step context: **Unknowns**.

## Migrated working rules

# Rules for Handoff to Verify

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** Call decision_handoff_verify with session_id and the claims the person listed. called_verify is false.
- **R2.** next_tools are qualify_source and check_claim. Call them on vital-verify, in that order.
- **R3.** check_claim needs the admitted source object and a quoted passage. A passage the coach wrote does not count.
- **R4.** Without a vvfy_ key, say Verify is not connected. Do not invent a status.
- **R5.** Do not restate source grading, claim decomposition, currency, honesty, or the Verify record. Those skills live in vital-verify.
- **R6.** An unverifiable sentence stays out of the brief. It is not replaced with a guess.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Handoff to Verify

## Pattern 1

One sentence and a URL. Packet, then qualify_source, then check_claim with the passage the person pasted.

## Pattern 2

No passage. Do not call check_claim with a summary. Say the sentence is not covered.

## Pattern 3

No vvfy_ key. Stop after the packet. Label the check not tool-checked. Do not use Verify status words.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
