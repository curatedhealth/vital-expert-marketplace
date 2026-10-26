# Rules for Handoff to Navigator

Pack: vital-decision-companion. Method version: 0.3.16. Content pack: 2026-10-26.1

- **R1.** Call decision_handoff_navigator first. called_navigator is false. This connector does not call Navigator over HTTP.
- **R2.** Speak Approach. suggested_stage_entry is options. compile_key is 4_options.
- **R3.** Then call the named tool on vital-ontology-navigator: decide_start or a methods_* tool.
- **R4.** methods_mcda_rank receives the same human cells, mapped as in references/tools.md. Decision Companion does not average them.
- **R5.** Check the scale. methods_mcda_rank needs 0 to 4. Ask the person how to map any other scale; never rescale silently.
- **R6.** Several raters go one call per rater, or into the governed Navigator flow with decide_attach_scores. Never average them here.
- **R7.** Without a vont_ key, say the shared tool is not connected.
- **R8.** People supply scores. The coach does not. A Navigator result informs the choice; it is not the choice.

Hard rules DC-H1 through DC-H8 in `SKILL.md` still apply.
