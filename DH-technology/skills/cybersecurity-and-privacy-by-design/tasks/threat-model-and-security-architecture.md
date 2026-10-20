# A2 Threat model and security architecture

Framework task: DH-04.02.2.1, Part A, task A2. Carries the old tasks "DH-04.02.2.1.1 Trust boundary drawing", "DH-04.02.2.1.2 Threat enumeration" and "DH-04.02.2.1.3 Mitigation or accepted risk", and the SBOM part of the reviewer document set.

## What this task delivers

From the person's architecture: the components and the hops where trust changes, a threat register keyed to hops (actor, hop, asset), the control category that addresses each threat or an explicit acceptance by a named person with a reopen condition, the architecture views and control categories the FDA premarket guidance names, and a check of the person's SBOM for identification, level of support, end-of-support dates and KEV entries. It answers "where can this product be attacked, what stops it, and what have we not covered?"

Why it matters: the old tasks warned against "a single box labeled cloud" and "a generic STRIDE list that is not tied to a hop". FDA asks for a threat model that captures supply chain, deployment, interoperation, update and decommissioning risk (EN-050) and for an SBOM with each component's support status (EN-054); a component past its end of support is a fact the owner needs before release.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `security-engineer-digital-health` (old DH-04.02.2.1.1 to .3). Work as a security architect who structures the person's design against sourced expectations |
| Skill | DH-04.02.2.1, Part A, Threat model and security architecture |
| Workflow | The steps below |
| Knowledge | `references/security-and-privacy-requirements.md` sections 5, 6 and 8; rows EN-036 to EN-040, EN-047 to EN-060, EN-069, EN-070, EN-075 to EN-085 |
| Tools | None from the library. `scripts/secdesign_check.py threats` and `sbom`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/threat-model-and-security-architecture-output.md` |
| Input | The request and its context: components, data flows, third parties, the person's threat register if any, the SBOM, the KEV export if the person has one, the design version, the read date, the person's risk scale and support horizon if set |
| Governance | `references/governance.md`; scores, acceptance and release are the person's; no exploit detail |
| Catalogue job | none (`list_jobs_2026-10-19.json` lists no security or privacy job) |

## Read the request

- **Architecture.** The components (app, device, sensor, cloud services, EHR, identity provider, data stores, update server, admin console) and how data moves. If the person gives only "it runs in the cloud", ask for the components once.
- **Design version and read date.** Both are the person's; "not given" otherwise. A threat model is dated to one design version.
- **Existing register and SBOM.** Keep the person's ids and words.
- **Risk scale.** If the person uses one, keep it as theirs. No source here sets a scale; the model never scores.

## Workflow

### Step 1. Components and trust boundaries (old DH-04.02.2.1.1)

List the components and each hop that crosses a network, a tenant or a privilege level; label what is inside the product boundary and what is a third party. Map the hops to the four FDA architecture views the person will need: Global System, Multi-Patient Harm, Updateability/Patchability, Security Use Case (EN-056). Never one box labeled cloud.

### Step 2. Threats per hop (old DH-04.02.2.1.2)

For each hop, write threats as actor, hop and asset, using the risk sources FDA names (supply chain, manufacturing, deployment, interoperation, maintenance and update, decommissioning, EN-050) and the assumption that an adversary controls the network and can alter, drop and replay packets (EN-051). Describe threats at that level only: never exploit steps, payloads or bypass instructions. Drop a threat with no asset. Every threat the model adds is labeled "proposed".

### Step 3. Control or acceptance (old DH-04.02.2.1.3)

For each threat: the control the person names, mapped to one of the eight FDA control categories (EN-057), or an explicit acceptance with the person who accepts it and the condition that reopens it. No threat is left with neither; no acceptance is anonymous. With code execution, save the register as CSV (id, hop, actor, asset, threat, control, accepted_by, reopen_condition, design_version) and run `python3 scripts/secdesign_check.py threats --file THREATS.csv`; report covered, accepted and open counts by hop and flags T1 to T6.

### Step 4. SBOM check

With code execution, run `python3 scripts/secdesign_check.py sbom --file SBOM.csv --as-of DATE [--kev KEV.csv] [--support-horizon DATE]` on the person's SBOM (CSV with component, supplier, version, release_date, patch, level_of_support, end_of_support, known_vulnerabilities, or CycloneDX JSON with those as properties). Report: components missing identification fields (EN-026), level of support or end-of-support date (EN-054), components past end of support on the read date, components whose end of support falls before the person's support horizon (only if they gave one), and known vulnerabilities in the person's KEV export (KEV entries should be designed out, EN-052; KEV is an input to prioritization, EN-080 [WF]). NTIA minimum elements are not in the sources `[GAP]`. The support horizon is the person's; the CRA's five-year minimum support period applies only to products in CRA scope (EN-091), never to MDR devices (EN-086).

### Step 5. Testing and frameworks the person must still evidence

List the security testing FDA names (EN-058) and the penetration test report contents (EN-059) as items the person evidences or marks `[GAP]`. If the person asks for a framework mapping, map their controls to NIST CSF 2.0 functions (EN-075) or SSDF practice groups (EN-037 to EN-040); a CSF Tier (EN-077) assigned by the model is "proposed".

## Build the output

Follow `assets/threat-model-and-security-architecture-output.md`. Answer first: hops and threats counted, how many are covered, accepted and open (by hop), the SBOM facts that most affect release (past end of support, KEV entries), and what is missing for the FDA views. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/secdesign_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every threat is tied to a hop and an asset; added threats are "proposed".
- No score, severity, likelihood or acceptance comes from the model.
- No exploit code, attack step or payload appears anywhere.
- Every SBOM fact is computed by the script or shown arithmetic on the person's file, with the read date.
- The model is dated to one design version, or "design version not given".
- `python3 scripts/secdesign_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [WF] labels travel with their rows.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Requests for exploit code, proof-of-concept attacks or bypass steps: refuse that part; offer instead, labeled "draft for the owner", the control categories (EN-057), the testing FDA names (EN-058) and what an independent penetration test report states (EN-059).
- The ISO 14971 safety risk file and how security risk feeds it: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Whether a design change needs a new submission: `dh-regulatory-and-quality` regulatory-submission-and-dossier.
- SMART scopes and FHIR API design at the EHR hop: `dh-technology` interoperability-and-ehr-integration.
- Build pipeline and release process: `dh-technology` medical-software-lifecycle-and-delivery.
- Whether the threat model is kept current in operation: `dh-technology` security-and-privacy-operations-monitoring.
