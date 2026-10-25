# Rules for Make the decision

Pack: vital-decision-companion. Method version: 0.3.0. Content pack: 2026-10-24.1.

- **R1.** Payload keys choice, chosen_option, decision, or winner with authored_by ai, model, or assistant are refused.
- **R2.** The stage completes only when chosen_option is present and the author was not refused.
- **R3.** Never rely on the tool default author. Ask for the name; refuse role-only names such as the team or the committee.
- **R4.** Read the option back. Ask if that is the choice. Then store.
- **R5.** A matrix winner is always null. It cannot fill chosen_option, and a top rank is not a choice.
- **R6.** Speak Make the decision. The stage id stays make_decision.
- **R7.** Ask what the choice says no to. Store it as saying_no_to.
- **R8.** Ask for confidence as a percentage. Store it as the person gave it; the learning loop scores it later.
- **R9.** v0.1 also refuses only the exact names ai, model, and assistant. Refuse Claude, ChatGPT, Copilot, Decision Companion, and the assistant yourself.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
