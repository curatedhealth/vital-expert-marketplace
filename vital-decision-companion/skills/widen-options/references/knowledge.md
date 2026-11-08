# Knowledge - widen-options

Step context: **Options**.

## Migrated working rules

# Rules for Widen options

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** Pass options as a list of objects with name. Empty names are refused.
- **R2.** Warnings, not errors: fewer than 3 options (`too_few_options` reads as "2 of 3 options"); do-nothing missing; do-it-internally missing. Warnings appear on both `decision_widen_options` and `run_stage`.
- **R3.** If a warning is present, ask the person for that option. Do not insert one.
- **R4.** The stage is complete when the stored list has at least three options.
- **R5.** Ids may be omitted. The tool assigns opt-1 and onward.
- **R6.** This skill does not rate and does not rank.
- **R7.** Ask one widening question per turn: and what else, vanishing options, opportunity cost, both-and, outside view.
- **R8.** A yes-or-no list is a whether-or-not frame. Name it and ask for another option.
- **R9.** Store widening answers via `decision_run_stage` on widen_options: `vanishing_options_answer`, `opportunity_cost`, `outside_view`.
- **R10.** After `decision_widen_options`, call `decision_status`. If the widen stage is still incomplete with 3 or more options stored, call `run_stage widen_options {options}` once so the stage completes.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Widen options

Sources for the method: the Playbook Widen Options stage (Part 7: and what else, vanishing options, opportunity cost, both-and); Nutt (1999, 2002) on whether-or-not decisions; Heath & Heath, Decisive (2013); Kahneman & Lovallo (1993) on the outside view.

## Pattern 1

Person lists: launch or do not launch. Name the whether-or-not frame and ask what else could reach the goal.

## Pattern 2

Person lists three vendors and no do-nothing. Ask what happens if they keep the current setup.

## Pattern 3

Person cannot add an option. Ask: if all three vendors vanished tomorrow, what would you do?

## Pattern 4

Person names two options that could combine. Ask whether doing both is a real option.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
