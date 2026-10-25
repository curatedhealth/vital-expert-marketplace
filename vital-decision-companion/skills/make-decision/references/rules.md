# Rules for Make the decision

Pack: vital-decision-companion. Method version: 0.3.14. Content pack: 2026-10-26.1

- **R1.** Payload keys choice, chosen_option, decision, or winner with authored_by ai, model, or assistant are refused.
- **R2.** The stage completes only when chosen_option and authored_by are present and the author was not refused.
- **R3.** Never rely on the tool default author. Ask for the name; on `role_only_name` ask who the person is.
- **R4.** Read the option back. Ask if that is the choice. Then store.
- **R5.** A matrix winner is always null. It cannot fill chosen_option, and a top rank is not a choice.
- **R6.** Speak Make the decision. The stage id stays make_decision.
- **R7.** Ask what the choice says no to. Store it as saying_no_to. Optional trade_offs when given.
- **R8.** Ask for confidence as a percentage. Store as `confidence_pct`, never `confidence`.
- **R9.** Refuse Claude, ChatGPT, Copilot, Decision Companion, and the assistant yourself — not only ai/model/assistant tokens.
- **R10.** On `stage_order`, name unmet stages and offer complete-or-skip. On `unknown_option`, read stored options back.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
