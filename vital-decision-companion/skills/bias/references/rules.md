# Rules for Bias

Pack: vital-decision-companion. Method version: 0.3.15. Content pack: 2026-10-26.1

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
