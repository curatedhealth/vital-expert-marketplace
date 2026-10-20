# Inclusive changes and partners for unseen groups

Interpretive reference for A2 and B1. Every rule cites its row in `patient-engagement-equity-research.md` (PE) or `accessibility-pointer-rows.md` (UX). Read on 19 October 2026.

## Change types with a sourced basis

The person chooses the change. These are the types whose basis the rows state; anything else the person proposes is theirs, labeled as such.

| Change type | Barrier it answers | Sourced basis | Notes |
|---|---|---|---|
| Language help at a step (interpreter, translated content) | Limited English proficiency | 92.201 meaningful access, free, accurate, timely (PE-107); no own interpreter (PE-109) | Whether 92.201 binds the person is their legal owner's call |
| Human review of machine translation | Errors in critical or technical text | PE-108 | Applies to critical, accuracy-essential, or complex text |
| Notice of language assistance in the relevant State languages | People unaware help exists | 92.11, at least 15 languages (PE-117) | Covered entities |
| Health-literacy or culturally tailored content | Literacy and cultural barriers | CMS priority 4 (PE-119) | Framework, standing not established (equity-frames.md section 3) |
| Accessible alternative or fix | Disability | 92.204 (PE-110); conformance via dh-patient-and-user-experience accessibility skills | Point there for WCAG and conformance |
| Review of decision-support inputs | Race, color, national origin, sex, age or disability used as inputs | 92.210 identify and mitigate (PE-113) | The model lists inputs; mitigation adequacy is the owner's |
| Wider recruitment or involvement | Groups absent from co-design or preference work | Representative population (PE-27); Inclusive Opportunities (PE-66) | |
| Alternate path (phone, in person, low-bandwidth, shared device, site support) | Device, connectivity, site type | No row sets a rule `[GAP]`; the person's own barrier evidence is the basis | Label the basis "your evidence" |

## The version rule (from the register)

The register's own method: name a change only if it can ship in a named version, and name the version that carries it (old task "Inclusive change"). If the person cannot name a version or release, record "version not set" and ask; never pick one.

## Partners and data owners for groups the data cannot see

The register's own method: name the group marked `[GAP]`, name the partner or the data owner who could see it, state the question to ask them, and never invent a rate for an unseen group (old task "Partner for the gap").

Kinds of holder the person can consider (the person names the actual organization):

| Holder | What they may see | Sourced context |
|---|---|---|
| The customer or deploying provider | Its own patient mix by language, age, area | If it is a 1557 covered entity, its language-access duties are its own (PE-107) |
| A patient organization | Members' experience and barriers | EMA defines patient organizations as not-for-profit with patients or carers a majority of governing bodies (PE-44); its eligibility criteria require funding transparency (PE-50) and sponsor independence (PE-51) |
| A community or public involvement group | People not reached through clinical channels | UK Standards: Inclusive Opportunities, Governance, Impact (PE-66 to PE-68); a framework, not a rule (PE-65) |
| A public data owner | Area-level indices (SVI, IMD) | SVI (PE-120 to PE-123); Core20 by IMD [WF] (PE-127) |

## Rules for the ask

- **Aggregate only.** Ask a partner for counts by group, never for patient-level records. OIG advisory practice for independent charities limits donor reports to aggregate counts of applicants, qualifying patients and amounts (PE-87): a sourced example of aggregate-only reporting in a related setting, not a rule for this case.
- **Independence.** Where the partner is a patient organization and the person's company is an EFPIA or ABPI member: independence must be assured, a written agreement states amount and purpose of support, and the company must not influence the organization's material in its own commercial favor (PE-70 to PE-72, PE-80, PE-81). These are industry codes [INDUSTRY], not law; say so. A company may not require to be the sole funder (PE-73). Logo use needs written permission (PE-74). Support is disclosed annually (PE-75, PE-82).
- **Payments and free items.** Any payment to a partner, any free item or service to patients, any payment tied to referrals or enrollment volume stops for the person's compliance or legal owner (governance.md). The model never says an arrangement is permitted or protected.
- **Conflicts in HTA work.** If the partner's input will go to an EU joint clinical assessment, patients there act in an individual capacity and declare interests (PE-56, PE-57); that route is the person's market access owner's.

## Aggregate counts and small cells

When the person has counts by subgroup, `scripts/equity_compare.py` computes reach and outcome rates per subgroup with Wilson 95 percent intervals, the difference and ratio against the reference group the person names, and each subgroup's share of the eligible and of the reached. The small-cell threshold is the person's (or their data provider's) rule: no threshold is sourced in this skill `[GAP]`. The script refuses to run without one.
