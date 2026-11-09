# Rules for Board prep

Pack: vital-mlr-review. Method version: 0.3.1.

- **R1. Prefer prior validate success (or explicit gate the board will act on).**
- **R2. Named human cleared_by — refuse any name that is or contains, as a whole word: assistant, ai, a.i., model, system, auto, automated, automation, bot, chatbot, chatgpt, gpt (and gpt4-style variants), openai, claude, anthropic, copilot, gemini, llm, agent, n/a, tbd, unknown, empty or whitespace.**
- **R2a. A real name that collides with a token** — explain the collision; ask the person to confirm a form of the owner's name without the token as a standalone word (full given name, or the company-record form such as family name with given-name initial), supplied by the person, or a different human owner, or escalation to the plugin owner. Never re-spell it yourself; never accept an AI (TEH-RDY-036).
- **R5. Status line carries one of the four statuses only; `prep_cleared_for_human_mlr` is reported as the record state on its own line.**
- **R3. mlr_reviewed always false.**
- **R4. Do not launder chair disagreements.**

Hard rules MLR-H1 through MLR-H8 in `SKILL.md` still apply.
