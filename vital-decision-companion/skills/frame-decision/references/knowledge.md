# Knowledge - frame-decision

Step context: **Frame**.

## Migrated working rules

# Rules for Frame the decision

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** how_to_decide completes with statement, goal, decider, and deadline. Name missing fields when the connector reports them.
- **R2.** Frame before solving: no option is listed and no rating is asked in this skill.
- **R3.** Reframe a yes/no question as how might we reach the goal. Do not add the options yourself.
- **R4.** The 2x2 gives a suggestion, proposed in plain words without level names. Store it unless the person objects; the person's preference wins.
- **R5.** The decider is a named person, not a role, a committee title, or the assistant.
- **R6.** Criteria are named before any rating. A criterion added after ratings is flagged as late.
- **R7.** People-decision notice (skill wording, used **only** when the connector returns no `people_decision` warning): say that the companion supports the process only, will not score or rank named individuals, and that company HR and legal processes apply (in the EU, employment decisions are a high-risk AI use under the AI Act). Then continue only with process questions. Prefer the connector's warning text verbatim when it returns; label R7 as the skill's notice only when the connector is silent. Never speak R7 (or any HR/legal/AI Act wording) in the same turn as sending `people_decision: true`.
- **R8.** No clinical, legal, or regulatory advice. A regulatory consequence is noted as the person stated it.
- **R9.** After sending `people_decision: true`, say only: "I've flagged this as a people decision; the connector's notice will follow." Stop. Do not invent the connector warning, do not speak R7 yet, and do not ask who/when in that turn.
- **R10.** Send rigor only on the first set; later changes use `change_rigor {to, by, reason}`. Read `rigor_unchanged`.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Frame the decision

Sources for the method: the Playbook Decide How to Decide stage (Part 6: ten framing questions, consequence × reversibility matrix, ladder of rigor); authority spectrum (Part 12); Nutt (1999) on binary framing; EU AI Act Annex III point 4.

## Pattern 1

Person asks: should we launch the program? Reframe: what goal is the program for, and how else could we reach it? Store the statement in the person's words.

## Pattern 2

Person says the decision is easy to reverse but costly if wrong. 2x2 suggests deciding quickly with what is known. Say so in plain words ("since it's easy to undo, let's decide with what we know and adjust") and continue unless they object.

## Pattern 3

Person names the leadership team as decider. Ask which named person holds the final call, and whether the team mode is consult or consent.

## Pattern 4

Decision is about promoting a named manager. Give the people-decision notice first, then ask only about process: criteria, who advises, timing.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
