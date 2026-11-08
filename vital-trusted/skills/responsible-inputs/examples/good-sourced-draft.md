# Rendered example: CSR excerpt before paste (sourced draft)

Invented teaching case. Input note, finding cards for PHI risk, gap list, check-line
stamp. No patient-level inventing; policy answer left to the company.

## Request

"Summarize the efficacy section of this CSR for a payer email — can I paste it here?"

Material described: unpublished Phase III CSR PDF (~400 pages), includes subject IDs in
appendices; person uses a consumer chat tool without naming company policy.

## Input note (`templates/input-note.md`, full)

Responsible inputs: before this goes into the tool

What it looks like
1. Unpublished clinical study report (Phase III), not public.
2. Subject-level identifiers may appear in appendices (patient-level detail).
3. Intended output may go to a payer (outside the company).

Questions for your company (not answered here)
1. Does your AI use policy allow this tool for unpublished CSR text?
2. Does your policy allow patient-level or identifiable trial data in this tool?
3. Who owns those answers? (Typically privacy, legal, or the AI governance lead.)

Safer routes (pick one)
1. Use a company-approved assistant on approved infrastructure, if policy allows.
2. Paste only the blinded, aggregate efficacy tables the policy names — not appendices.
3. Ask biostatistics or clinical for a redacted aggregate summary cleared for AI use.

I did not decide whether this tool is approved or whether data is anonymous.

## Finding cards (shared `../../templates/finding-card.md`)

### Finding 1
- **Material:** Full CSR with appendices.
- **Issue:** Unpublished study data; possible PII/PHI if subject IDs or small-n cells travel.
- **Action:** Pause paste; route through policy and minimum redacted extract.

### Finding 2
- **Material:** Payer-bound summary from CSR.
- **Issue:** Output may leave the company before human medical review.
- **Action:** Pair with `responsible-use` human oversight after any allowed extract.

## Open items (`../../templates/gap-list.md`)

```text
Open items
1. AI tool approval for CSR paste — company AI use policy — next: Named policy owner
2. Redacted aggregate tables — not supplied — next: Clinical/biostats extract

Not yet checked
- Whether payer email is the final channel (affects both input and use skills)
```

## Work offered only after route chosen

If the person supplies a redacted, policy-cleared aggregate table only:

> Efficacy (supplied redacted table only): primary endpoint met in population stated in
> the table; figures copied verbatim from the extract — no subject-level rows invented.

## Check-line stamp (`../../templates/check-line-stamp.md`)

```text
TRUSTED / responsible-inputs: not tool-checked (offline tools) · confidentiality: CSR+identifiers flagged; PHI: no paste until policy; IP: unpublished CSR
```

## Letter lines (`templates/check-line.md`, trusted-check only)

```text
Responsible-inputs · confidentiality: unpublished CSR with identifier risk, paste paused (not tool-checked)
Responsible-inputs · intellectual property: full CSR not reproduced, aggregate route offered (not tool-checked)
```
