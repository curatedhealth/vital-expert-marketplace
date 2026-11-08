# Knowledge - bias

Step context: **Examine**.

## Migrated working rules

# Rules for Bias

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** Pass decision_type or session_id. With a session and no type, the tool uses the stored type.
- **R2.** Matched items are those whose types include the decision type. With no type, the full card returns when the connector allows it.
- **R3.** When the pack returns `stages[]` and `contested` (content pack 2026-10-26.1), prefer the tool items over the by-hand list and keep the contested label.
- **R4.** draft is true. Do not say the decision is unbiased.
- **R5.** Read the countermeasure. Ask the person to do that step. Do not do it for them.
- **R6.** This skill does not set chosen_option.
- **R7.** On `unknown_decision_type`, read `valid_types` from the tool result and ask the person which type applies. Do not treat silence as "no bias".
- **R8.** By-hand prompts by stage are fallback only when the tool does not return stages[]. Framing: framing effect; status quo; overconfidence. Widen: anchoring; availability. Gather: confirmation; authority. Decide: sunk cost; groupthink; loss aversion. Implement: planning fallacy; escalation of commitment.
- **R9.** Decision fatigue is a contested effect. If raised, suggest scheduling hard decisions with breaks, without claiming the effect is settled. Keep the contested label from the pack when present.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Bias

Sources for the method: the Playbook cognitive bias reference (Part 13, 12 biases); Kahneman (2011); Kahneman, Lovallo & Sibony (2011), Before you make that big decision; Danziger et al. (2011) and the critique by Weinshall-Margel & Shapard (2011) on decision fatigue.

## Pattern 1

Leadership team has spent a year on a program. Ask the sunk-cost question: knowing what we know, would we start this today?

## Pattern 2

First price quoted dominates the talk. Ask what range they would set if that number had never been said.

## Pattern 3

Card returns nothing for the type. Say the card has no entry; offer one by-hand prompt for the stage.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
