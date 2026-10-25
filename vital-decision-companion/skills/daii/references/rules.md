# Rules for DAI-I

Pack: vital-decision-companion. Method version: 0.2.0. Content pack: 2026-10-24.1.

- **R1.** roles.decide must be a display name the person gave. An empty decide returns the gap decide role empty.
- **R2.** Do not assign ai, model, or assistant to any role.
- **R3.** Do not invent a job title. If they gave a name, use the name. If they gave none, write owner not named and ask.
- **R4.** Advise, Inform, and Implement may be empty. Say they are empty.
- **R5.** Call decision_run_stage on implement with the same roles after the person confirms.
- **R6.** The implement stage completes when roles.decide is non-empty.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
