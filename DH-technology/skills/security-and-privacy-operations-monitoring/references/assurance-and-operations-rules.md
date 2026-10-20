# Assurance and operations rules

What the sources and the old monitoring tasks say about checking security and privacy in operation: whether a claimed control has evidence, whether the threat model is current, how open vulnerabilities age, what counts as closed, whether consent text matches practice, and who owns a miss. The requirements themselves are in `security-and-privacy-requirements.md` (copied from the sibling design skill). Rows live in the copied research files: EN in `engineering-interop-security-research.md`, CP in `channels-partners-research.md`, CS in `customer-success-research.md`, DL in `diligence-research.md`, PL in `product-lifecycle-research.md`. No [PAPER] rows are used in this skill.

Every pass rule, window, severity, cadence, owner and recheck date is the person's. No source here sets a patch window, an aging threshold, a proof standard, a consent-match rate or an audit cadence; never supply one.

## 1. Claimed control versus artifact (old DH-04.02.1.2.1 and .2)

- Read the control matrix; for each row, name the policy, configuration or log that is supposed to prove it; mark the row proven, unproven or contradicted (old method). A control whose only evidence is the matrix itself is unproven (old "Do not").
- The model marks "proven as stated" when an artifact is named and the person has not shown it; it marks "proven (artifact read)" only when the person shares the artifact and it shows the control. "Contradicted" comes from what the artifact or a reviewer note shows.
- Score each unproven control against the citation it claims: name the clause, state what it requires (from the rows) and what the artifact shows. Whether a gap is blocking or a documentation miss is the person's classification; never rank every gap as blocking (old method and "Do not").
- Activity review is a required HIPAA specification: regular review of audit logs, access reports and incident tracking (EN-101). Security Rule documentation is kept six years (EN-105). FDA's CSA guidance recommends system logs and audit trails as assurance evidence for production and quality system software (EN-022); it does not cover device software (EN-015).
- A NIST CSF 2.0 Tier (Partial, Risk Informed, Repeatable, Adaptive, EN-077) assigned by the model is "proposed", never a score of the person's program.

## 2. Threat model currency (old DH-04.02.2.2.1 and .3)

- Read the threat register; mark each threat covered, accepted or open; count open threats by hop (old method). A tool scan is not a threat model (old "Do not").
- Changes that force the model to be redrawn are the person's list; the old task names new third party, new write-back and new device. FDA names changes that may impact cybersecurity: new authentication or encryption algorithms, new connectivity, a changed update mechanism (EN-060). Any software change re-opens validation status (FDA GPSV, EN-008).
- Record the last design version the model matches and who watches for the triggers; an undated model is a finding (old method and "Do not").

## 3. Residual risk (old DH-04.02.2.2.2)

- For each covered threat, state what the control does not stop. Residual risk is not scored before the threat list exists (old "Do not").
- The old method rated a remainder high only when the asset is identifiable patient data or a therapy-controlling function. That is the old skill's rule, kept as a proposed rule the person confirms; no source row sets it.
- Controlled and uncontrolled risk are defined in the 2016 FDA postmarket guidance (EN-063, EN-064). Which applies is the person's call. Say when the residual note was made and against which design version.

## 4. Vulnerability aging and closure (old DH-04.02.3.2.1 and .2)

- List reachable items that are not patched and not accepted; compute age from the intake date; separate items past the person's stated window from items inside it. Unreachable items are left out of the age count (old method and "Do not"). Items with reachability not stated are listed apart and not aged.
- Windows are the person's. Sourced context, labeled each time: 524B asks for a justified regular patch cycle and, for critical vulnerabilities that could cause uncontrolled risks, out of cycle as soon as possible (EN-044); for uncontrolled risk, FDA's 2016 enforcement policy for 21 CFR 806 asks for customer communication within 30 days and a validated, distributed fix within 60 days (EN-066, EN-067), not statutory deadlines.
- KEV: an input to prioritization (EN-080 [WF]); an entry needs a CVE ID, reliable evidence of active exploitation and a clear remediation (EN-081 [WF]). A KEV flag in the person's file is checked against the catalog entry itself.
- Closed means evidence: for a patched item, the deployed version; for an accepted item, an acceptance that has a named acceptor and has not expired. An item whose evidence is a ticket with no deployment is reopened, and a merged pull request is not deployment (old method and "Do not"). Reopening is proposed to the person, who closes or reopens.
- SBOM support status over time: a component past its end-of-support date (EN-054) is a fact for the owner; the response is theirs.

## 5. Repeat failure class (old DH-04.02.3.2.3)

- Group open and recently closed items into classes (the old task's examples: dependency, auth, exposed admin, device protocol); the period for "recently" is the person's. Name the class with the most reachable items and the engineering change that would shrink it, as distinct from patching one item; a new scanner is not that change (old method and "Do not"). The SSDF asks organizations to identify residual vulnerabilities and prevent recurrence (EN-040). The engineering change the model names is "proposed".

## 6. Consent text versus practice (old DH-04.02.4.2.1 and .2)

- Read the current consent text; list the processing the system performs on each data class; mark each step described, broader than described, or missing from the text. A draft text is never reviewed against a future design (old method and "Do not").
- Rules a broader step may touch, for the person's legal owner: by default only data necessary for each purpose (GDPR Article 25(2), EN-109); MHMDA sharing consent separate from collection consent (EN-123) and sale authorization (EN-125); Part 2 counseling notes need their own consent (EN-117); minimum necessary under HIPAA (CS103). Cite only the rows for the market in the request.
- Withdrawal test: run a withdrawal in a non-production environment, check the jobs, exports and model inputs that should have stopped, and record any job that still ran. A flipped preference flag is not a pass (old method and "Do not").
- Deletion flows to processors and third parties within 45 days under MHMDA (EN-126). For certified health IT APIs, the authorization server revokes an app's access at the patient's direction within one hour (45 CFR 170.315(g)(10), EN-144); that is an interoperability duty routed to `dh-technology` integration-quality-monitoring.

## 7. Owners of misses (old DH-04.02.1.2.3 and DH-04.02.4.2.3)

- Each missing artifact gets the owner the person names (a person or a role, not a department slogan) and the date the person sets; an owner nobody named is recorded as "owner not named" (old method). The assessment is not closed because the matrix looks complete (old "Do not").
- A consent mismatch or failed withdrawal names the owner of the text and the owner of the job if they differ, which one must change, and the version that should carry the fix; both owners are never assigned without saying who moves first (old method and "Do not"). Who moves first is the person's call; the model shows the facts.

## 8. Safety events in the product's category

- `regulatory-dh.search_safety_events` returns FDA recalls and MHRA alerts as records; describe each only by what its record states, never judge its relevance to the person's product (`tools.md`). No saved output returns a recall whose summary names a cybersecurity cause; finding cybersecurity recalls needs a live check.

## 9. Incident clocks while monitoring

The clocks in `security-and-privacy-requirements.md` section 7 apply to incidents found while monitoring. They are laid beside the person's facts for their legal owner, each as a fact, never as pressure. The Cyber Resilience Act does not apply to MDR or IVDR devices (EN-086). NIS2 scope depends on size thresholds and national transposition not read here `[GAP]` (EN-093 to EN-096).
