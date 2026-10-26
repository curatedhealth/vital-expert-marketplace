# Rules for Frame the decision

Pack: vital-decision-companion. Method version: 0.3.16. Content pack: 2026-10-26.1

- **R1.** how_to_decide completes with statement, goal, decider, and deadline. Name missing fields when the connector reports them.
- **R2.** Frame before solving: no option is listed and no rating is asked in this skill.
- **R3.** Reframe a yes/no question as how might we reach the goal. Do not add the options yourself.
- **R4.** The 2x2 gives a suggestion, proposed in plain words without level names. Store it unless the person objects; the person's preference wins.
- **R5.** The decider is a named person, not a role, a committee title, or the assistant.
- **R6.** Criteria are named before any rating. A criterion added after ratings is flagged as late.
- **R7.** People-decision notice (skill wording, used **only** when the connector returns no `people_decision` warning): say that the companion supports the process only, will not score or rank named individuals, and that company HR and legal processes apply (in the EU, employment decisions are a high-risk AI use under the AI Act). Then continue only with process questions. Prefer the connector's warning text verbatim when it returns; label R7 as the skill's notice only when the connector is silent. Never speak R7 (or any HR/legal/AI Act wording) in the same turn as sending `people_decision: true`.
- **R8.** No clinical, legal, or regulatory advice. A regulatory consequence is noted as the person stated it.
- **R9.** After sending `people_decision: true`, say only: "I've flagged this as a people decision; the connector's notice will follow." Stop. Do not invent the connector warning, do not speak R7 yet, and do not ask who/when in that turn.
- **R10.** Send rigor only on the first set; later changes use `change_rigor {to, by, reason}`. Read `rigor_unchanged`.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
