# Rules for Use-case library

Pack: vital-decision-companion. Method version: 0.3.15. Content pack: 2026-10-26.1

- **R1.** Gold ids are UC01, UC02, and UC05. Any other id returns card null and the gold set.
- **R2.** Walk beats in order. One beat, then a question.
- **R3.** The card's decision_type and rigor are applied to the session only when session_id is passed and those fields are still empty.
- **R4.** Do not treat a beat as the person's choice.
- **R5.** leverage_packages name other connectors. This skill does not call them.
- **R6.** Playbook content version is 2026-10-24.1.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
