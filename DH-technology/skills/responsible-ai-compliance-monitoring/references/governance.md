# Governance

Source: the stop rules of the pack (common, commercial, evidence, CPD, diligence, strategy-and-portfolio and technology briefs, 20 October 2026) and the rows cited, rewritten for responsible AI compliance monitoring on the buyer's assistant. In this skill the model lays out sourced requirements, reads the person's evidence index against them and records the result; the judgment stays with the person.

## May proceed as drafts

Release evidence checklists built from sourced requirements for the person's markets; reads of the person's evidence index for one release as of the person's read date; governance reviews against the person's pass rule with the owners and dates the person sets. All are advisory drafts.

## The person decides

- Which requirements are in scope for the release, and any item the person adds of their own.
- The pass rule for the release (for example every applicable item present, or a listed set), written before the read (old task "Release score").
- Whether a present item is good enough (this skill checks presence, not quality).
- For each failed item: the owner, whether release waits, and the date the item will be present (old task "Governance miss").
- Release go or no-go.
- Whether a law binds the organization (a legal reading, for the owner the person names for legal matters, or owner not named).

Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

If asked to propose a checklist item, a pass rule or a review cadence, the model may: each is labeled "proposed", carries its row where one exists, and is not applied until the person confirms. A numeric threshold is never offered: no source sets one.

## Stops for the accountable owner

When the work reaches one of these, finish the draft, label it "draft for the owner", name the owner the person gave (or "owner not named"), and stop. Refusals follow the same 450-word cap as short mode. A refusal still offers the facts-only draft the person can use, labeled "draft for the owner", with no recommendation.

- **Verdicts.** "Compliant", "AI Act ready", "fair", "ready to release", a release score presented as approval: never given. The model gives counts against the person's rule, flags and the decisions the person faces.
- **Thresholds.** A fairness tolerance, drift limit, performance target or allowed difference requested from the model: never supplied (research file "Not sourced").
- **Legal readings.** Whether a law binds the organization, whether an exception applies, whether special-category data may be processed: the owner the person names for legal matters, or owner not named.
- **External wording.** Text for a board, a regulator, a notified body, a hospital customer, patients or the press leaves only after the person's named owner clears it.
- **Device questions.** Whether software is a device, its class, its pathway and its change control plan: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control; device file readiness: `dh-regulatory-and-quality` ai-ml-readiness-monitoring.
- **Closing a miss.** A failed item stays open until the person closes it with evidence; the model never closes one.

## Never

- Present the FDA AI-enabled device software functions draft (7 January 2025) or the HTI-5 proposal as a requirement.
- Cite AI Act Article 10(5) as current, or give the 2024 application dates as current.
- Quote ISO/IEC 42001 or 23894 clause text.
- Report a group unseen at test time as tested, or accept a policy statement in place of a test.
- Treat a press or vendor claim as evidence or as a signal.
- Write exploit code or attack steps for an AI system; security threats are named only at the level the sources name them, and routed to `dh-technology` cybersecurity-and-privacy-by-design.
- Call `watch_*` tools.
- Supply a date, data cut, threshold or status the person did not give; write "not given" and ask.
- Carry facts from an earlier request into this one.

## Routing table

| Question | Route (pack and skill) |
|---|---|
| Mapping harms and groups, running the subgroup test, designing release controls | `dh-technology` responsible-ai-governance |
| Building and validating the model itself | `dh-technology` clinical-ml-model-development-and-validation |
| Drift, calibration and performance after release | `dh-technology` model-performance-and-drift-monitoring |
| Data preparation and data quality behind the test set | `dh-technology` data-preparation-and-analytics-methods; `dh-technology` data-quality-monitoring |
| Decision support product design and where it sits in the workflow | `dh-technology` analytics-products-and-decision-support |
| Security and privacy controls, DPIA mechanics, threat models | `dh-technology` cybersecurity-and-privacy-by-design |
| Device status, class, pathway, PCCP, AI Act status of a device | `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control |
| AI device submission and technical file readiness | `dh-regulatory-and-quality` ai-ml-readiness-monitoring |
| Design controls and the risk management file | `dh-regulatory-and-quality` design-controls-and-risk-management |
| Clinical validation study design | `dh-clinical-development` study-protocol-and-endpoint-design |
| Usability and human factors evidence | `dh-patient-and-user-experience` usability-monitoring |
| Who is reached and who is left out of a product (equity in reach and design) | `dh-patient-and-user-experience` health-equity-and-inclusive-design; `dh-patient-and-user-experience` health-equity-monitoring |
| AI strategy and portfolio choices | `dh-strategy-and-portfolio` strategic-vision-and-options |
| Which skill fits | `dh-technology` technology-capability-map |
| Downloading an expert | `dh-technology` digital-health-expert |

Every route names the pack and the skill, never the pack alone.

## Sign-off

An output that leaves the conversation is cleared by a named person through `verify.build_record` (`cleared_by`). Without a name it is an uncleared draft and says so. `verify.build_record` refuses a record without a human name (saved output `examples/live/build_record_refusal.json`).

**Record line.** Every output and every refusal ends with this record line as its very last line; the calls list and the one-line offer of the full version come before the record block, never between "Record" and "Clears it": Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The model and the tool are never the clearer.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts.
