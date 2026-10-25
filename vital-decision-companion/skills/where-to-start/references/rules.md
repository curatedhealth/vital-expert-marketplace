# Rules for Where to start

Pack: vital-decision-companion. Method version: 0.3.0. Content pack: 2026-10-24.1.

- **R1.** Intents are quick, tradeoff, deep, full, and classify_first. An unknown intent is refused.
- **R2.** Without an intent, decision_start returns opened false and the template menu. Ask which intent.
- **R3.** Pass session_id on every later call. Chat memory is not the session.
- **R4.** decision_status names the open stage. Speak the label. Keep the stage id in the tool payload.
- **R5.** Practice mode returns watermark SIMULATED. Say the session is practice.
- **R6.** Persistence in this build is process memory. durable_connected is false. Do not claim the row was saved to a database.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
