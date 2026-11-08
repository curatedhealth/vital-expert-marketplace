# Knowledge - where-to-start

Step context: **orchestrator**.

## Migrated working rules

# Rules for Where to start

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** Intents are quick, tradeoff, deep, full, and classify_first. An unknown intent is refused.
- **R2.** Without an intent, decision_start returns opened false and the template menu. Ask which intent.
- **R3.** Pass session_id on every later call. Chat memory is not the session.
- **R4.** decision_status names the open stage. Speak the label. Keep the stage id in the tool payload.
- **R5.** Practice mode returns watermark SIMULATED. Say the session is practice.
- **R6.** Read `persistence` and `durable_connected` from the tool result and report only what they say. `supabase` with `durable_connected: true` means the session is stored durably; `memory` or a `store_not_durable` warning means it is not. Never claim more than the result shows.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Where to start

## Pattern 1

Person says they need to decide but names no intent. Show the five intents in plain words and wait.

## Pattern 2

Status returns open_stage gather_intelligence. Speak Gather intelligence. Do not jump to the brief.

## Pattern 3

durable_connected is false. Tell the person the session lives in this process until the table is applied.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
