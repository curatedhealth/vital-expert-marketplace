# Release rules: the person's, with a starter option

Interpretive reference for task B1. Rows cited from `ux-accessibility-research.md`, read on 19 October 2026.

## Whose rule

Whether a release ships with open accessibility issues is the person's decision under their own release rule. No row sets a release rule for a product. National deadlines are facts about when an instrument applies (see `obligation-map.md`), never a release threshold the model sets.

## The register starter rule (offer it; apply only if adopted)

The earlier register method for this task, kept as an option the person may adopt in their own words:

1. Block the release if a day-one task has an open break.
2. Allow a later screen only with a named exclusion.
3. Record the decision against the build.

And: "Do not ship a day-one task that failed the assistive check." Ask the person to define "day-one task" for their product (for example sign-in, onboarding, the core clinical task). Without their definition, the rule cannot be applied; the output lists open issues by task and asks.

## Sourced facts that bear on an exclusion

| Basis | What it requires | Who determines | Row |
|---|---|---|---|
| ADA Title II and HHS 504 exceptions | Five listed exceptions, including individualized password-protected documents about a specific person | The covered entity | UX-US-12, UX-US-20 |
| ADA minimal-impact provision | Noncompliance treated as compliant only if it does not affect equal access with substantially equivalent timeliness, privacy, independence and ease of use | The covered entity, on facts | UX-US-13 |
| ADA undue burden or fundamental alteration | Head of the public entity or designee, with a written statement of reasons | Named by the rule | UX-US-14 |
| EAA disproportionate burden | Operator's own assessment against Annex VI | The economic operator | UX-EU-09 |
| EAA content exclusions | Pre-recorded media and office files published before 28 June 2025, some maps, uncontrolled third-party content, archives | Listed | UX-EU-08 |
| PSBAR exclusions and burden | Listed content exclusions; burden assessment weighing size, resources, costs and benefits | The public sector body | UX-UK-04, UX-UK-05 |

An exclusion without one of these bases is "the person's choice for this release", stated as such. It is not a legal exemption.

## What a release decision record holds

Build or version; date; the person's rule (theirs, or the starter rule as adopted); open issues on day-one tasks and on later screens, from A2; exclusions named with their basis; the decision (the person's words: ship, block, ship with exclusions); who decided. The model drafts the record; the decision line is filled by the person.

## Ranking repairs

If the person wants an order for repairs, they score each (RICE: reach, impact 0.25 to 3, confidence as a percent, effort) and `analytics.rice` ranks them (`tools.md`). Day-one status and the rule's outcome sit beside the rank; the person decides whether they override it.
