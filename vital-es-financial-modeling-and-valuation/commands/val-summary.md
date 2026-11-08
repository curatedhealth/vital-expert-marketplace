---
command: /val-summary
args: [asset names, mode (asset|company), paths to the nine skill registers per asset (V1 to V9; a missing one is a gap), as_of date, optional thresholds file, optional prepared_by and reviewed_by]
tool: tools/assemble_valuation_summary.py
template: templates/valuation-summary.md
---
Assemble the valuation summary from the registers of the nine skills for one asset (company mode: one set per pipeline asset, then a side-by-side roll-up). This is a plugin-level command, not a competency: it runs `tools/assemble_valuation_summary.py` and fills `templates/valuation-summary.md`. It adds no finding of its own; every line points to a register row (skill code and path), and a line without a valid pointer fails.

Mission from the map: the closing step of the capability (after DCF & Risk-Adjusted NPV Modeling, Scenario & Sensitivity Analysis, and Benchmarking & Comparable Analysis).

Which intakes must have run: the intake of each skill whose register is supplied. This command has no intake of its own beyond the arguments above: ask for any missing argument in one message.

REQUIRES routing. For each register not supplied, record the GAP the tool writes and name the skill to run: V1 build-dcf-model; V2 calculate-risk-adjusted-npv (requires V1); V3 validate-valuation-assumptions; V4 design-valuation-scenarios; V5 analyze-valuation-sensitivity (requires V2, V4); V6 communicate-valuation-scenarios (requires V5); V7 identify-comparable-transactions; V8 compare-deal-terms-to-benchmarks (requires V7); V9 synthesize-market-standard-terms (requires V8, V2). The summary still assembles with the missing workstream marked red (proposed) and says what is blocked.

Steps: (1) write a manifest naming the registers; (2) run `python3 tools/assemble_valuation_summary.py manifest.json --out summary.json --md summary.md` (add `--thresholds client.json` to override the team defaults); (3) read the output, check the proposed statuses with the deal lead and hand over the summary. Exit 0 = assembled; exit 1 = a hard error (unresolved pointer, unsupported or recommending line, adopted valuation not HUMAN ONLY).

Never: recommend a price or a decision; produce a fairness or solvency view; reconcile a conflict between workstreams (show both sides); merge the model range with a benchmark range; fill a missing register. The deal lead signs; human only.
