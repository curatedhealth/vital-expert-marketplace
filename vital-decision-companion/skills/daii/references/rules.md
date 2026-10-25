# Rules for DAI-I

Pack: vital-decision-companion. Method version: 0.3.3. Content pack: 2026-10-26.1

- **R1.** roles.decide must be a display name the person gave. An empty decide returns the gap decide role empty.
- **R2.** Do not assign ai, model, assistant, a product name, or a tool to any role.
- **R3.** Do not invent a job title. If they gave a name, use the name. If they gave none, write owner not named and ask.
- **R4.** Advise, Inform, and Implement may be empty. Say they are empty.
- **R5.** Call decision_run_stage on implement with the same roles after the person confirms.
- **R6.** The implement stage completes when roles.decide is non-empty. A complete stage is not a full plan; implement-plan adds owner, milestone, and review trigger.
- **R7.** On `role_only_name`, ask for the person. Advise, Inform, and Implement may keep role entries only if the person insists — say they stay unverified. Refuse AI and product names as Decide.
- **R8.** One Decide. If two names are given, ask which one holds the final call; the other advises.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
