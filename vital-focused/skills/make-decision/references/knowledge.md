# Knowledge - make-decision

Step context: **Decide**.

## Migrated working rules

# Rules for Make the decision

Pack: vital-decision-companion. Method version: 0.4.0. Content pack: 2026-10-29.1

- **R1.** Payload keys choice, chosen_option, decision, or winner with authored_by ai, model, or assistant are refused.
- **R2.** The stage completes only when chosen_option and authored_by are present and the author was not refused.
- **R3.** Never rely on the tool default author. Ask for the name; on `role_only_name` ask who the person is.
- **R4.** Read the option back. Ask if that is the choice. Then store.
- **R5.** A matrix winner is always null. It cannot fill chosen_option, and a top rank is not a choice.
- **R6.** Speak Make the decision. The stage id stays make_decision.
- **R7.** Ask what the choice says no to. Store it as saying_no_to. Optional trade_offs when given.
- **R8.** Ask for confidence as a percentage. Store as `confidence_pct`, never `confidence`.
- **R9.** Refuse Claude, ChatGPT, Copilot, Decision Companion, and the assistant yourself; not only ai/model/assistant tokens.
- **R10.** On `stage_order`, name unmet stages and offer complete-or-skip. On `unknown_option`, read stored options back.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.

## Patterns

> **Teaching material, never input.** The situations below are invented for shape (DC-H2). Do not copy a name, a date, or a figure into a live answer.

# Patterns for Make the decision

Sources for the method: the Playbook Make the Decision stage (Part 9: confidence check, saying no to, final decision check); Tetlock & Gardner (2015) on stating probabilities; Annie Duke (2018) on decision records.

## Pattern 1

Decider says: go with the second vendor, I'm 70 percent sure, we're saying no to building in-house. Read back all three, then store.

## Pattern 2

Someone says: the matrix says option two. Reply that the matrix has no winner and ask the decider what they choose.

## Pattern 3

Decider answers no to the would-we-explain-it-in-public check. Record the no and ask whether they still proceed.

## FOCUSED constants

- Person decides; skills never name a winner.
- Local session is default durability.
- MCP is special-service only.
