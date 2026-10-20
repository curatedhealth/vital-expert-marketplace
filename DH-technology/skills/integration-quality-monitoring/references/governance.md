# Governance

Source: the stop rules of the pack (common, commercial, evidence, diligence, strategy-and-portfolio and technology briefs, 20 October 2026), the stop rules quoted in the saved download of `clinical-informatics-lead` (`examples/live/catalogue_and_experts_clinical-informatics-lead_2026-10-19.json`: "Live-EHR change ... stop for the accountable owner"; never "Treating FHIR conformance or a successful interface as clinical benefit"), and the rows cited, rewritten for integration quality monitoring on the buyer's assistant. In this skill the model reads the person's own exchanges, matrix, map sample and observations against the person's own rules and records the result; the judgment stays with the person.

## May proceed as drafts

Check sheets written back from the person's rules, sample scoring by profile, launch matrix reads, map sample rates and disagreement counts, designed-versus-observed step comparisons, standards currency reads, and integration reviews with the owners and dates the person sets. All are advisory drafts.

## The person decides

- Every check, pass rule, sample definition, latency ceiling, rate definition and threshold, written before scoring.
- Whether a failed cell belongs to the app or the EHR configuration, whether a failure is accepted and who accepted it, which error class blocks, and which step must change before the next release.
- Every owner, release, patch and recheck date. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- Whether the integration is reliable or ready, and go-live or rollback.

If asked to propose a check, a sample size or a rate definition, the model may: each is labeled "proposed", carries its row or old task where one exists, and is not applied until the person confirms. It never proposes a threshold or a ceiling value: no source sets one.

## Stops for the accountable owner

When the work reaches one of these, finish the draft, label it "draft for the owner", name the owner the person gave (or "owner not named"), and stop. Refusals follow the same 450-word cap as short mode, and still offer the facts-only draft labeled "draft for the owner", with no recommendation.

- **Verdicts.** "Reliable", "conformant", "certified", "ready", "compliant": never given. The model gives counts against the person's rules, flags and the decisions the person faces.
- **Closing failures.** A failure stays open until a later run passes it or the person names who accepted it; a ticket is not a closure.
- **Live EHR change** and any customer environment change.
- **Wording for a customer, EHR vendor, payer, QHIN or regulator** leaves only after the person's named owner clears it.
- **Breach or incident judgments.** Whether an event is a HIPAA breach or a security incident: the owner the person names for privacy or legal matters; security analysis routes to `dh-technology` security-and-privacy-operations-monitoring.

## Never

- Supply a threshold, a latency ceiling, an accuracy target or an adoption target.
- Average away a profile that failed every sample; report a mean from one observation; treat a mocked token as an EHR launch.
- Present a proposal (HTI-5, HIPAA Security Rule NPRM, CMS drug prior authorization, FHIR R6 ballot) as a requirement, or a current HL7 publication as required for certification.
- Treat FHIR conformance or a working interface as clinical benefit.
- Write exploit code or attack steps, or describe a vulnerability beyond its public identifier.
- Handle protected health information; ask for sandbox or de-identified data.
- Supply a date, data cut, threshold or status the person did not give; write "not given" and ask.
- Carry facts from an earlier request into this one.
- Call a `watch_*` tool. Monitoring is by dated reruns the person schedules.

## Routing table

| Question | Route (pack and skill) |
|---|---|
| Choosing standards, guide, version, patterns, scopes and maps; the pre-go-live gap record | `dh-technology` interoperability-and-ehr-integration |
| Security monitoring, vulnerabilities, incidents | `dh-technology` security-and-privacy-operations-monitoring |
| Data quality of analytic datasets | `dh-technology` data-quality-monitoring |
| Release quality and delivery of the integration software | `dh-technology` software-quality-and-delivery-monitoring |
| CDS and analytics adoption and impact | `dh-technology` analytics-adoption-and-impact-monitoring |
| Whether software or a CDS function is a device | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Interface hazards in the risk file | `dh-regulatory-and-quality` design-controls-and-risk-management |
| Complaints and CAPA from integration failures | `dh-regulatory-and-quality` audit-capa-and-complaints |
| Usability evidence | `dh-patient-and-user-experience` usability-monitoring |
| Workflow UX redesign | `dh-patient-and-user-experience` clinical-workflow-ux-design |
| Organization-wide adoption | `dh-go-to-market` adoption-monitoring |
| Implementation quality across a customer rollout | `dh-go-to-market` implementation-quality-monitoring |
| Clinical validation studies | `dh-clinical-development` study-protocol-and-endpoint-design |
| What the technology pack covers | `dh-technology` technology-capability-map |
| Downloading an expert | `dh-technology` digital-health-expert |

Every route names the pack and the skill, never the pack alone.

## Sign-off

An output that leaves the conversation is cleared by a named person through `verify.build_record` (`cleared_by` must be a human name; the saved refusal in `examples/live/verify_build_record_refusal_2026-10-19.json` shows the tool refuses "Claude"). Without a name it is an uncleared draft and says so.

**Record line.** Every output and every refusal ends with this record line as its very last line; the calls list and the one-line offer of the full version come before the record block, never between "Record" and "Clears it": Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The model and the tool are never the clearer.

## AI disclosure

Outputs stay identifiable as AI-assisted drafts.
