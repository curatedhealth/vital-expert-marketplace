# Rules for Handoff to Navigator

Pack: vital-decision-companion. Method version: 0.2.0. Content pack: 2026-10-24.1.

- **R1.** Call decision_handoff_navigator first. called_navigator is false. This connector does not call Navigator over HTTP.
- **R2.** Speak Approach. suggested_stage_entry is options. compile_key is 4_options.
- **R3.** Then call the named tool on vital-ontology-navigator: decide_start or a methods_* tool.
- **R4.** methods_mcda_rank receives the same human cells. Decision Companion does not average them.
- **R5.** Without a vont_ key, say the shared tool is not connected.
- **R6.** People supply scores. The coach does not.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
