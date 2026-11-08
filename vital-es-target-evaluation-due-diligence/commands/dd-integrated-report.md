---
command: /dd-integrated-report
args: [mode (asset|company), asset names, paths to the nine skill outputs per asset (F A B C D E G R H; E may be one company-level file), as_of date, optional thresholds file, optional prepared_by and reviewed_by]
tool: tools/assemble_report.py
template: templates/integrated-diligence-report.md
---
Assemble the integrated diligence report from the outputs of the nine skills for one asset (company mode: one set per
pipeline asset, then a roll-up). This is a plugin-level command, not a competency: it runs `tools/assemble_report.py` and
fills `templates/integrated-diligence-report.md`. It adds no finding of its own; every line of the report points to a
register row (skill code and row id), and a line without a valid pointer fails the check.

Mission from the map: the closing step of the capability (after Scientific & Clinical, Commercial & Market, and Financial &
Legal Due Diligence). See skills/target-evaluation-due-diligence-capability-map/SKILL.md.

Which intakes must have run: the intake of each skill whose output is supplied (intake.md in each skill folder). This command
has no intake of its own beyond the arguments above: ask for any missing argument in one message and do not start on an assumption.

REQUIRES routing. For each of the nine outputs that is not supplied, stop short of inventing it: record the GAP the tool
writes (what is blocked) and name the skill to run:
- F: assess-scientific-validity-and-moa
- A: review-clinical-data-quality
- B: estimate-development-risk-and-timeline (requires A)
- C: assess-ip-portfolio-and-freedom-to-operate
- D: evaluate-regulatory-pathway-and-legal-risk (requires A, B, C)
- E: analyze-financial-statements-and-tax
- G: evaluate-market-opportunity-and-competitive-position
- R: forecast-revenue-and-price-ranges (requires G, B, C)
- H: determine-commercial-viability (requires G; reads R for price and revenue)
The report still assembles with the missing workstream marked red (proposed) and says what is blocked.

Steps: (1) write a manifest naming the outputs; (2) run `python3 tools/assemble_report.py manifest.json --out report.json --md report.md`
(add `--thresholds client.json` to override the team defaults); (3) read the output, check the proposed statuses with the deal lead,
and hand over the report. Exit 0 = assembled; exit 1 = a hard error (unresolved pointer, unsupported or recommending line, unknown
status word).

Never: recommend sign, sign with conditions or do not sign; certify a position; reconcile a conflict between workstreams (show both
sides); fill a missing output. The deal lead (BD head or investment lead) signs; human only. Quality of earnings, net debt,
accounting and tax opinions, the freedom-to-operate and legal opinions, the route choice and the commercial decision stay with the
people named in the underlying registers. US and EU only, except the revenue workstream R, which is country by country (US, DE, FR, IT, ES, UK).
