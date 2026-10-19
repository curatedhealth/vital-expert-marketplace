# Conformance sampling and the issue log

Interpretive reference for tasks A1 and A2. Every rule cites its row in `ux-accessibility-research.md` (UX- rows) or `wcag-criteria-additions.md` (WX rows), read on 19 October 2026.

## What a sample can and cannot show

| Rule | What it means for a sample | Row |
|---|---|---|
| Conformance is for full pages, including every responsive variation | A screen is sampled whole, at each size it is served in; a page with a part excluded does not conform | UX-STD-21 |
| Complete processes | If any page in a process (sign-in, onboarding, booking) fails, no page in that process conforms at that level | UX-STD-22 |
| Levels are cumulative | AA means every A and AA criterion | UX-STD-20 |
| Test what was claimed | Sample against the version and level in the person's requirement, not another one (old register rule, kept) | UX-STD-23 |
| Apps and web views | Under EN 301 549, mobile apps and web views inside them are tested under clause 11, not clause 9 | UX-STD-31, UX-STD-32 |
| EN 301 549 and WCAG | WCAG 2.1 AA equals clauses 9.1 to 9.4 plus 9.6 in V3.2.1; WCAG 2.2 AA equals the same clauses in V4.1.1 | UX-STD-34, UX-STD-30 |
| EN 301 549 is self-scoping | A requirement applies only when its "Where ICT ..." precondition is true; Annex C gives a test per requirement | UX-STD-33 |
| Section 508 exceptions | Non-web documents and software are excused 2.4.1, 2.4.5, 3.2.3, 3.2.4; non-web software is excused complete processes; "Web page" reads as "software" | UX-US-02 to UX-US-04 |

## Status per criterion, per screen

Record one of: **pass** (checked with the method named, result and date recorded), **fail** (with the issue id), **not applicable** (the person's call, with the reason; under EN 301 549 a false precondition, UX-STD-33), **not tested**. "Not tested" is never shown as pass. A criterion with no issue logged is not a pass (WX1 note; the log records issues found, not tests run).

## Methods

- Automated tests check only part of what needs testing (UX-UK-24). A sample built only from automated results covers only the criteria those tools test; the rest are "not tested".
- Manual checks are, in NHS guidance, the most effective way to test individual pages or components (WX8).
- Testing with people, including assistive technology users, is one of three types (UX-UK-24, UX-US-78).
- Component libraries and their conformance reports do not make a service accessible (UX-UK-28, UX-US-78); the USWDS report covers its own 44 components of version 3.11.0 (UX-US-77), not a product built with them.

Which criteria a given automated tool checks is not in this skill's sources `[GAP]`; ask the person for their tool's coverage list, or treat every criterion as "not tested" unless a manual or person-based check is recorded.

## Candidate criterion for an issue described without one

Copied from the sibling skill's `references/barrier-criteria.md`. A candidate only; the person's tester confirms.

| Barrier as people describe it | Criterion (level in 2.2) | Requirement as sourced | Row |
|---|---|---|---|
| Screen reader announces "button" with no name | 4.1.2 Name, Role, Value (A) | Criterion text not quoted in the rows `[GAP]` | wcag_criteria.csv (level only) |

## Sampling which screens

The rows set no sampling rule for products: no minimum number of screens and no selection method `[GAP]`. The person picks the sample. The model checks that every process in the requirement has at least one sampled page, and flags processes with none.

## The issue log

`scripts/a11y_issue_log.py` reads the person's log (criterion, level, severity they assigned, status, dates, day-one task, how found) and reports it against their target: which issues are in the target, outside it (2.2-only against a 2.1 target, AAA against AA, 4.1.1 against 2.2), open counts by the person's severity labels and by W3C level, ages to an as-of date, day-one tasks first, and data problems (a logged level that differs from the W3C level, a closed issue without a date). Severity stays the person's label; the script counts it, never assigns or reinterprets it.

## Statements and reports a team may be asked for

- WCAG conformance claim content, if a claim is made: date, guideline title, version and URI, level, pages covered (UX-STD-23).
- WAD accessibility statement (public bodies): inaccessible parts and reasons, feedback mechanism, enforcement link (UX-EU-12).
- PSBAR accessibility statement (UK public bodies): model statement, kept under review (UX-UK-06).
- ONC certified health IT: the accessibility-centered design standard used, or none (UX-US-23).

All of these stop for the accountable owner before publication.
