# Barriers, criteria and checking methods

Interpretive reference for tasks A2 and B1. Every success criterion and level comes from `data/wcag_criteria.csv` (W3C pages, rows WX1 to WX7); criterion wording comes from UX-STD rows in `ux-accessibility-research.md`. Where a criterion's text is not quoted in a row, name the criterion and level from the table only and do not paraphrase its requirement from memory: write "criterion text not quoted in this skill's rows; read it at https://www.w3.org/TR/WCAG22/" `[GAP]`.

## Common barriers in health apps and the criteria they meet

| Barrier as people describe it | Criterion (level in 2.2) | Requirement as sourced | Row |
|---|---|---|---|
| Text hard to read against its background | 1.4.3 Contrast (Minimum) (AA) | At least 4.5:1; large text 3:1 | UX-STD-15 |
| Buttons, inputs or chart lines hard to see | 1.4.11 Non-text Contrast (AA) | At least 3:1 against adjacent colors | UX-STD-16 |
| Keyboard focus hidden under a sticky header or banner | 2.4.11 Focus Not Obscured (Minimum) (AA, new in 2.2) | Not entirely hidden by author-created content | UX-STD-09 |
| Small tap targets (dose buttons, close icons) | 2.5.8 Target Size (Minimum) (AA, new in 2.2) | At least 24 by 24 CSS pixels, with listed exceptions | UX-STD-11 |
| Slider or drag-to-reorder with no tap alternative | 2.5.7 Dragging Movements (AA, new in 2.2); candidate in any version: 2.1.1 Keyboard (A) if the control cannot be set from a keyboard | Single-pointer alternative unless dragging is essential (UX-STD-10); 2.1.1 text not quoted [GAP] | UX-STD-10; wcag_criteria.csv (2.1.1 level) |
| Login needs remembering a password or solving a puzzle | 3.3.8 Accessible Authentication (Minimum) (AA, new in 2.2) | No cognitive function test unless an alternative or mechanism is offered | UX-STD-14 |
| Patient asked again for details already given in the same flow | 3.3.7 Redundant Entry (A, new in 2.2) | Auto-populate or offer for selection, with exceptions | UX-STD-13 |
| Help or contact link moves between screens | 3.2.6 Consistent Help (A, new in 2.2) | Same relative order where repeated | UX-STD-12 |
| Content breaks or scrolls sideways when zoomed | 1.4.10 Reflow (AA) | No two-dimensional scrolling at 320 CSS pixels wide | UX-STD-17 |
| App locked to portrait | 1.3.4 Orientation (AA) | No orientation lock unless essential | UX-STD-18 |
| Form error shown only by color or not at all | 3.3.1 Error Identification (A) | Error identified and described in text | UX-STD-19 |
| Screen reader announces "button" with no name | 4.1.2 Name, Role, Value (A) | Criterion text not quoted in the rows `[GAP]` | wcag_criteria.csv (level only) |
| Image or icon with no text alternative | 1.1.1 Non-text Content (A) | Criterion text not quoted in the rows `[GAP]` | wcag_criteria.csv (level only) |

A barrier that matches none of these: look the criterion up in `data/wcag_criteria.csv` by number with the person, give the level from the table, and mark the requirement text `[GAP]`. If the person cannot name a criterion, write "criterion not identified" rather than guessing one.

## Version and level checks for any criterion

- If the person targets WCAG 2.1, the six A and AA criteria new in 2.2 (2.4.11, 2.5.7, 2.5.8, 3.2.6, 3.3.7, 3.3.8) are outside the target (UX-STD-07); say so, and say which obligations in `obligation-map.md` still require them (GDS and NHS, UX-UK-08, UX-UK-23).
- If the person targets WCAG 2.0 (for example under Section 508), the 17 criteria new in 2.1 are outside the target (WX3).
- AAA criteria are outside an AA target. W3C does not recommend requiring AAA for whole sites (UX-STD-20).
- 4.1.1 Parsing is not in 2.2; test and report it only where a 2.0 or 2.1 policy applies (UX-STD-08, WX7).

## Checking methods

| Method | What the sources say | Row |
|---|---|---|
| Automated testing | "Automated tests only check some of what you need to test." Use it in the build or for scans, never alone. | UX-UK-24, WX9 |
| Manual testing with guidelines | NHS calls manual checks the most effective way to test individual pages or components (guidance). | UX-UK-24, WX8 |
| Testing with people, including assistive technology users | NHS names testing with people as one of three types; USWDS recommends tests "with real people who need assistive accommodations"; GOV.UK requires disabled people in research for government services | UX-UK-24, UX-US-78, UX-UK-08 |
| Recruiting | NHS guidance: include 1 person with access needs in every 5 research participants (guidance, not law) | UX-UK-25 |
| Components | Accessible components do not make a service accessible; teams test their own service | UX-UK-28, UX-US-78 |

The method a check uses is the one the person's requirement names. If the requirement names a person using a screen reader, an automated scan does not substitute for it (old register rule, kept). Named assistive technologies (which screen readers, which magnifiers) are the person's choice; the sources here do not list them `[GAP]`.

## A barrier is fixed only with a path

A barrier is recorded as fixed when the person can say how someone using the named method completes the task on that screen after the change, and who checked it with which method. A fix shown only by a better scan score is not a fix (old register rule, kept).
