# Rules for Bias

Pack: vital-decision-companion. Method version: 0.3.0. Content pack: 2026-10-24.1.

- **R1.** Pass decision_type or session_id. With a session and no type, the tool uses the stored type.
- **R2.** Matched items are those whose types include the decision type. With no type, the full card returns.
- **R3.** The four tool items in pack 2026-10-24.1 are confirmation, anchoring, sunk_cost, and groupthink.
- **R4.** draft is true. Do not say the decision is unbiased.
- **R5.** Read the countermeasure. Ask the person to do that step. Do not do it for them.
- **R6.** This skill does not set chosen_option.
- **R7.** An empty card for a type means the card has no entry, not that no bias applies (v0.1 is silent on unknown types).
- **R8.** By-hand prompts by stage, labelled as Playbook content, not tool output. Framing: framing effect (how would this look framed as a loss?), status quo (would we choose this today if starting fresh?), overconfidence (what is our range, not our point estimate?). Widen options: anchoring (what if the first number had never been said?), availability (are we judging by the most vivid case?). Gather intelligence: confirmation (what evidence would change our mind?), authority (would we accept this from a junior colleague?). Make the decision: sunk cost (ignoring what is spent, would we start this today?), groupthink (who has not spoken?), loss aversion (are we weighting losses over equal gains?). Implement: planning fallacy (how long did similar work take before?), escalation of commitment (what result would make us stop?).
- **R9.** Decision fatigue is a contested effect (the parole-board finding has been challenged). If raised, suggest scheduling hard decisions with breaks, without claiming the effect is settled.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
