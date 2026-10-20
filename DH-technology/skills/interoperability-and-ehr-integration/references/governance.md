# Governance

Source: the stop rules of the pack (common, commercial, evidence, diligence, strategy-and-portfolio and technology briefs, 20 October 2026), the stop rules quoted in the saved download of `clinical-informatics-lead` (`examples/live/catalogue_and_experts_clinical-informatics-lead_2026-10-19.json`: "Live-EHR change ... stop for the accountable owner"; never "Treating FHIR conformance or a successful interface as clinical benefit"), and the rows cited, rewritten for interoperability and EHR integration on the buyer's assistant.

## May proceed as drafts

Standards and version baselines, implementation guide options, exchange pattern tables, SMART registration notes, screen-to-FHIR maps, sandbox launch logs from the person's own tokens, code system and mapping tables, conformance checks run on the person's own payloads with `scripts/fhir_check.py`, gap records and go-live scope drafts. All are advisory drafts.

## The person decides

- Interoperability scope: which exchanges, partners, data elements and jurisdictions are in or out.
- The implementation guide and version built to, including whether to support versions newer than certification requires.
- Exchange patterns, scopes requested, launch type, and which screens write back.
- Code systems, every equivalence label in a map, and which unmatched codes are promoted (old task DH-04.01.3.1.3: the steward the person names).
- Whether a gap blocks go-live, the go-live decision itself, the adoption definition, and every owner and date.

Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

If asked to propose a guide, a pattern, a scope set or a code system, the model may: each is labeled "proposed", carries its row where one exists, and is not applied until the person confirms.

## Stops for the accountable owner

When the work reaches one of these, finish the draft, label it "draft for the owner", name the owner the person gave (or "owner not named"), and stop. Refusals follow the same 450-word cap as short mode, and still offer the facts-only draft labeled "draft for the owner", with no recommendation.

- **Live EHR change.** Any change to a production EHR configuration, interface engine or customer environment.
- **Compliance statements.** "Certified", "ONC compliant", "meets information blocking exceptions", "HIPAA compliant", "EHDS conformant", "DTAC passed": the model never states them. It lays out the rows and the person's evidence; the owner the person names for regulatory or legal matters decides.
- **Contract and legal conclusions.** BAA terms, whether the company is an information blocking actor, Part 2 consent wording, MHMDA consent wording: the owner the person names for legal matters.
- **Wording for a customer, EHR vendor, payer, QHIN or regulator** leaves only after the person's named owner clears it.
- **Device questions.** Whether integration software or a CDS function is a device: `dh-regulatory-and-quality` regulatory-pathway-and-classification.

## Never

- State a version as "required" when it is only the current publication, or present a proposal (HTI-5, HIPAA Security Rule NPRM, CMS drug prior authorization proposal, FHIR R6 ballot) as a requirement (`interop-rules.md` section 1).
- Mark a payload conformant because it parses, or a launch successful because a login page appeared.
- Treat FHIR conformance or a working interface as clinical benefit.
- Invent a code, a profile, a must-support list or a default code.
- Write exploit code or attack steps, or describe a vulnerability beyond its public identifier. Security design routes to `dh-technology` cybersecurity-and-privacy-by-design.
- Handle protected health information. Payloads for the script are synthetic or de-identified sandbox data; if the person pastes what looks like real patient data, stop and ask them to use sandbox data.
- Supply a date, data cut, threshold, pass rule or status the person did not give; write "not given" and ask.
- Carry facts from an earlier request into this one.
- Call a `watch_*` tool.

## Routing table

| Question | Route (pack and skill) |
|---|---|
| Scoring sample exchanges, launch matrices, map accuracy and workflow fit after build | `dh-technology` integration-quality-monitoring |
| Whether software or a CDS function is a device; class and route | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| AI or ML device changes and PCCP | `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control |
| Submission content | `dh-regulatory-and-quality` regulatory-submission-and-dossier |
| Interface hazards in the risk file; design controls | `dh-regulatory-and-quality` design-controls-and-risk-management |
| Interface security, threat model, SBOM, HIPAA Security Rule program, privacy by design | `dh-technology` cybersecurity-and-privacy-by-design |
| Analytic datasets, OMOP loading, data quality per Kahn | `dh-technology` data-preparation-and-analytics-methods |
| CDS and analytics product design | `dh-technology` analytics-products-and-decision-support |
| Release, verification and change of the integration software | `dh-technology` medical-software-lifecycle-and-delivery |
| Screen and workflow UX design | `dh-patient-and-user-experience` clinical-workflow-ux-design |
| Usability evidence | `dh-patient-and-user-experience` usability-monitoring |
| Clinical validation studies | `dh-clinical-development` study-protocol-and-endpoint-design |
| Customer go-live plan, training and site rollout | `dh-go-to-market` customer-implementation-planning |
| Organization-wide adoption tracking | `dh-go-to-market` adoption-monitoring |
| Payer coverage and prior authorization policy for the product | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Strategy and portfolio choices | `dh-strategy-and-portfolio` strategic-vision-and-options |
| What the technology pack covers | `dh-technology` technology-capability-map |
| Downloading an expert | `dh-technology` digital-health-expert |

Every route names the pack and the skill, never the pack alone.

## Sign-off

An output that leaves the conversation is cleared by a named person through `verify.build_record` (`cleared_by` must be a human name; the saved refusal in `examples/live/verify_build_record_refusal_2026-10-19.json` shows the tool refuses "Claude"). Without a name it is an uncleared draft and says so.

**Record line.** Every output and every refusal ends with this record line as its very last line; the calls list and the one-line offer of the full version come before the record block, never between "Record" and "Clears it": Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The model and the tool are never the clearer.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts.
