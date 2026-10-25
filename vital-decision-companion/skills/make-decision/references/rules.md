# Rules for Make the decision

Pack: vital-decision-companion. Method version: 0.2.0. Content pack: 2026-10-24.1.

- **R1.** Payload keys choice, chosen_option, decision, or winner with authored_by ai, model, or assistant are refused.
- **R2.** The stage completes only when chosen_option is present and the author was not refused.
- **R3.** Default author in the tool is owner only when a human choice was accepted. Prefer the name the person gave.
- **R4.** Read the option back. Ask if that is the choice. Then store.
- **R5.** A matrix winner is always null. It cannot fill chosen_option.
- **R6.** Speak Make the decision. The stage id stays make_decision.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
