Shared origin: authored in design-system-development (DH-02.04.2.1) on 19 October 2026 and copied unchanged so this skill stands alone.
# Governance models: how three public design systems run contribution, lifecycle, versions and change

Interpretive reference for DH-02.04.2.1 (B1, A2) and DH-02.04.2.2 (B1). Every point cites its row in `design-system-additions.md` (DSX) or `UX_ACCESSIBILITY_USABILITY.md` (UX-). Read on 19 October 2026.

These are the practices of the GOV.UK Design System, the NHS design system and the U.S. Web Design System (USWDS) on their own official pages. They are evidence of how mature public systems govern themselves. They are not rules for the person's products. The person chooses which, if any, to adopt, and in what words. Present them as options, never as requirements, and never as a benchmark the person is "behind".

## 1. Who owns the system

| System | Owner as stated | Rows |
|---|---|---|
| NHS design system | Maintained by the service manual team at NHS England; anyone can propose or develop components against published criteria | UX-UK-21, UX-UK-27 |
| USWDS | A product of GSA's Technology Transformation Services, maintained by the Digital Services Division | UX-US-75 |
| GOV.UK Design System | Built by the GOV.UK Design System team; proposals start as GitHub discussions; the community prioritizes work yearly | UX-UK-33 |

The person names the owner of their system and of each product. A system with no named owner is recorded as "owner not named".

## 2. Contribution and publication criteria

| Stage | GOV.UK | NHS | Rows |
|---|---|---|---|
| Proposal | Useful (evidence of use across teams) and unique (does not replicate; a replacement needs evidence it is better) | Useful and unique, same wording in substance | UX-UK-29, DSX-15 |
| Publication | Usable (tested with a representative sample including disabled people), consistent (reuses existing styles and components), versatile (works across services; tested across browsers, assistive technologies and devices) | Usable, consistent, versatile and clinically safe (clinician involved where appropriate; approval from a clinician trained in clinical safety may be required) | UX-UK-30, UX-UK-31, DSX-13, DSX-14, DSX-17, DSX-18 |
| Not enough research yet | Published with trial status | Published as "experimental" if based on relevant research and meeting the other criteria | DSX-22, DSX-19 |

For a digital health system the NHS "clinically safe" criterion is the one public criterion that speaks to clinical content (DSX-18).

## 3. Lifecycle statuses

| System | Statuses as published | Rows |
|---|---|---|
| GOV.UK | Trial and Stable; trial for new or significantly changed components that might not meet all criteria; trial components may change substantially or be deprecated; a trial moves to stable after 6 months without negative feedback; the system deprecates components that do not adapt | UX-UK-32, DSX-21, DSX-22 |
| USWDS | Four phases: Proposal, Development, Released, Deprecated. Proposals open for comment at least 45 days. Released components are Experimental (pass accessibility tests, may change more often), Stable (established production history, audited regularly for accessibility and usability) or Use with caution (fails accessibility, usability or development requirements; USWDS advises against use). Deprecated components get no updates and should be removed; Retired ones are removed from the code | DSX-24 to DSX-29 |
| NHS | Experimental is named in the publication criteria; other statuses not sourced `[GAP]` | DSX-19 |

A status can move down: USWDS moved Input mask to "use with caution" on 7 July 2026 (DSX-30). A lifecycle with a downgrade path tells product teams when a component they use stops being safe to keep.

## 4. Versions and breaking changes

- GOV.UK Frontend marks a breaking release by an increment in the first digit of the version (for example 5.x to 6.0.0); a breaking release is one where some services must change their code to keep working (DSX-35). This is GOV.UK's convention; whether the person's versions follow it is the person's fact.
- NHS releases numbered versions with update guides; version 10 was current on its page on 19 October 2026 (DSX-20). USWDS offered v3.14.0 for download on 19 October 2026 (DSX-30).
- GOV.UK requires a linked community resource to state which version of GOV.UK Frontend it supports, to have a clear owner, and to be no more than 3 months behind the latest version (DSX-16). That rule governs community resources, not services. It is the only sourced "how far behind" rule, and it is offered to the person only as an example of the kind of rule they may write.
- USWDS aims to ship accessibility fixes in the next available release (DSX-39).

## 5. Local modification and forks

- Modifying a system component creates risk: the service may break on update or become less accessible (DSX-31).
- Small modifiers are not for changing most of a component, for a component that no longer meets the original need, or for large markup changes (DSX-32).
- A forked component cannot be broken by updates but receives no future updates from the original (DSX-33). A fork of a component that later receives an accessibility fix keeps the old behavior until someone ports the fix.
- Any modified component is checked against accessibility standards (DSX-34).
- Design tokens are the shared color, spacing and typography values that new components should use (DSX-42).

## 6. Adoption and feedback

- USWDS's maturity model starts with an inventory of the components a site uses, checked against the component guidance (DSX-40); the presence of the system's classes or stylesheet does not show that an implementation is usable or accessible (DSX-41). The 2020 worksheet is withdrawn (DSX-43).
- GOV.UK asks teams to say whether they use a component and why they do not (DSX-23).
- No published measure of design-system adoption or effectiveness was found `[GAP]`. Adoption and drift in these skills are counts on the person's inventory, computed by `scripts/ds_adoption.py`.

## 7. Accessibility concerns raised against components

GOV.UK's strategy sorts concerns into theoretical and evidenced and usually prioritizes evidenced ones (DSX-44); names the kinds of evidence (research findings, usability results, new standards, user feedback, assistive technology behavior, audits) (DSX-46); calls a concern high severity when all three hold: evidence that some people cannot complete tasks, essential services affected, and service teams cannot resolve it alone (DSX-45). It measures concerns recorded and listed, and if capacity allows time to resolution, regressions reaching a release and concerns raised by service teams versus internally, gathering results every 6 months (DSX-47 to DSX-49). All of this is GOV.UK's own practice.
