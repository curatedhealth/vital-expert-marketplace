# Rules for Gather intelligence

Pack: vital-decision-companion. Method version: 0.3.15. Content pack: 2026-10-26.1

- **R1.** Notes source is owner, participant, or draft. Any other source is refused.
- **R2.** A draft source is stored with draft true. Say the note is a draft.
- **R3.** The stage completes only through decision_run_stage with knowns and unknowns. decision_attach_notes alone never completes it.
- **R4.** An unknown stays in the unknowns list (never filled) until the person or a handed-off tool supplies it.
- **R5.** Ask for disconfirming evidence for the leading option. Seeking only confirming facts is the confirmation-bias trap.
- **R6.** For estimates, ask for the base rate or reference class before case details.
- **R7.** This skill does not call catalogue, literature, trials, or label connectors.
- **R8.** When the person needs a score, name handoff-navigator. When they need a claim checked, name handoff-verify.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
