# Component requirements: what a design-system component must meet

Interpretive reference for DH-02.04.2.1 and DH-02.04.2.2. Every rule cites the row it rests on in `UX_ACCESSIBILITY_USABILITY.md` (UX- rows), `design-system-additions.md` (DSX rows) or `change-control-rows.md` (QS, EU, CH rows). Facts were read on 19 October 2026. Where no row supports a point, it says `[GAP]`.

## 1. Which accessibility target applies: the person chooses, the rows show what buyers and markets cite

A component has no legal target of its own. Its target follows the products it serves and the obligations of the people who buy or run them. The person sets the system's target; lay out what each market cites:

| Who or where | What the source cites | Rows |
|---|---|---|
| US federal agencies (Section 508) | WCAG 2.0 Level A and AA for content and software; non-web software is excused four criteria and the complete-processes requirement; "Web page" reads as "software" | UX-US-02, UX-US-03, UX-US-04 |
| US state and local government (ADA Title II) | WCAG 2.1 A and AA (5 June 2018 text). Compliance from 26 April 2027 (population 50,000 or more) and 26 April 2028 (smaller entities and special districts), dates moved by a DOJ interim final rule effective 20 April 2026 | UX-US-08, UX-US-09, UX-US-10, UX-US-11 |
| Recipients of HHS funding, for example most hospitals (Section 504) | WCAG 2.1 A and AA from 11 May 2027 (15 or more employees) and 10 May 2028 (fewer), dates moved by an HHS interim final rule effective 7 May 2026; covers what they provide through contractors | UX-US-15, UX-US-16, UX-US-17, UX-US-18 |
| Section 1557 covered health programs | Websites and apps must comply with Section 504 as interpreted consistent with ADA Title II; 92.204 names no WCAG version itself | UX-US-21, UX-US-22 |
| NHS England, GOV.UK services | WCAG 2.2 AA as a minimum; the six new 2.2 A and AA criteria are a requirement for NHS websites and apps | UX-UK-08, UX-UK-22, UX-UK-23 |
| EU public sector (Web Accessibility Directive) | EN 301 549 V3.2.1 (WCAG 2.1 AA equivalent for clause 9) is the cited harmonized standard | UX-EU-01, UX-EU-13, UX-STD-34 |
| EU products and services under the European Accessibility Act | EN 301 549 V4.1.1 (2026-09) aligns clauses 9 to 11 to WCAG 2.2 and was adopted 24 August 2026; whether it is cited in the Official Journal was not checked `[GAP]`. Health apps are not a listed EAA category | UX-STD-26 to UX-STD-30, UX-EU-04 |

Points that hold whichever target is chosen:

- Content that conforms to WCAG 2.2 also conforms to 2.0 and 2.1 (UX-STD-03, UX-STD-24), and W3C advises adopting 2.2 even where obligations cite an earlier version (UX-STD-04, advice, not law). Teams bound to 2.0 or 2.1 may still need to test 4.1.1 Parsing, which 2.2 removed (UX-STD-08).
- Conformance is claimed for full pages and complete processes, never for a component on its own (UX-STD-21, UX-STD-22). A component test is evidence toward the conformance of the pages that use it.
- Mobile apps and web views inside apps are tested against EN 301 549 clause 11 (UX-STD-31, UX-STD-32).
- A conformance claim is optional; if made it must carry the date, version, level and the pages covered (UX-STD-23). Making one stops for the owner (`governance.md`).

## 2. WCAG 2.2 criteria by component type

The table lists the Level A and AA criteria the sourced rows quote; criterion numbers and names are as printed in WCAG 2.2 (UX-STD-07, DSX-50). It is not the full WCAG list: criteria not quoted in the rows are `[GAP]` here and are read in the WCAG 2.2 text before they are relied on. Level AAA is not recommended as a general requirement for whole sites (UX-STD-20).

| Component type | Criteria (level, row) |
|---|---|
| Every interactive component (button, link, input, toggle, tab, menu) | Keyboard 2.1.1 (A, DSX-03); Focus Visible 2.4.7 (AA, DSX-04); Focus Not Obscured (Minimum) 2.4.11 (AA, UX-STD-09); Name, Role, Value 4.1.2 (A, DSX-06); Label in Name 2.5.3 (A, DSX-09); Target Size (Minimum) 2.5.8: at least 24 by 24 CSS pixels, five exceptions (AA, UX-STD-11, DSX-10); Non-text Contrast 1.4.11: 3:1 for boundaries and states (AA, UX-STD-16); Use of Color 1.4.1 (A, DSX-02) |
| Form inputs (text, date, dose, select, checkbox, radio) | Labels or Instructions 3.3.2 (A, DSX-05); Error Identification 3.3.1: errors identified and described in text (A, UX-STD-19); Info and Relationships 1.3.1 (A, DSX-01); Redundant Entry 3.3.7 (A, UX-STD-13) |
| Sliders, range and drag controls | Dragging Movements 2.5.7: a single-pointer alternative (AA, UX-STD-10); a slider counts as one target for 2.5.8 (DSX-11, non-normative) |
| Text and type tokens | Contrast (Minimum) 1.4.3: 4.5:1, large text 3:1 (AA, UX-STD-15); Reflow 1.4.10 at 320 CSS pixels (AA, UX-STD-17) |
| Tooltips, popovers, hover content | Content on Hover or Focus 1.4.13: dismissible without moving focus (AA, DSX-08) |
| Status messages, toasts, inline alerts | Status Messages 4.1.3: exposed without taking focus (AA, DSX-07) |
| Sign-in and authentication | Accessible Authentication (Minimum) 3.3.8: no cognitive function test without an alternative (AA, UX-STD-14) |
| Help and contact links repeated across screens | Consistent Help 3.2.6: same relative order (A, UX-STD-12) |
| Layout containers and screens | Orientation 1.3.4: no locked orientation unless essential (AA, UX-STD-18) |

W3C's Understanding document for 2.5.8 recommends meeting 24 by 24 regardless of spacing, as a best practice, and pointing important controls to 2.5.5 (AAA) (DSX-12). That is advice, offered to the person as an option.

## 3. Evidence a component should carry

| Evidence | What the source says | Rows |
|---|---|---|
| Three kinds of testing | Testing with people, automated testing, manual testing; automated tests check only part | UX-UK-24 |
| Representative users, including disabled people | GOV.UK publishes a component only after research with a representative sample including disabled people; NHS asks the same and allows "experimental" status without enough research | UX-UK-30, DSX-19 |
| Browsers, assistive technologies, devices | Tested and shown to work across them | UX-UK-31 |
| What USWDS runs | Automated scans on every code change, no merge on failure; screen readers, keyboard only, zoom, touch only, cross-browser tests | DSX-36, DSX-37 |
| Research participants with access needs | NHS advice: 1 person with access needs in every 5 participants (guidance, not law) | UX-UK-25 |
| In-context testing by product teams | Teams using a component test it at page level in context | DSX-38, UX-US-78 |

The design system's tests do not make a product accessible: GOV.UK, USWDS and the USWDS maturity model all say so (UX-UK-28, UX-US-78, DSX-41). Contracts and checks say this once.

## 4. Clinical safety and content a component must not invent

- NHS publishes a component only if it is "clinically safe": a clinician involved in the design where appropriate, clinical safety issues addressed, and approval from a clinician trained in clinical safety where NHS asks (DSX-17, DSX-18). This is NHS practice, offered as a criterion the person may adopt.
- The register method for this competency (old task "Component contract") names the content a component must not invent, for example clinical claims and doses, and forbids a marketing page and a clinical task sharing a component that invents clinical content. This is VITAL's method, not a sourced legal rule.
- Patient-facing copy and any clinical claim shown by a component stop for the owner (`governance.md`).

## 5. When the component is part of a medical device user interface

Whether a product is a device is decided by the person's regulatory owner (dh-regulatory-and-quality). If they say it is, the component is part of the device user interface and these rows apply:

| Point | Rows |
|---|---|
| The user interface includes packaging, labeling, training materials, controls, displays, alarms and logic of operation | UX-US-31 |
| MDR Annex I: reduce use-error risk from ergonomic features and use environment, and consider users' knowledge, training and medical and physical conditions, including disabled users | UX-EU-14 |
| MDR Annex I: measurement, monitoring and display scales follow ergonomic principles | UX-EU-15 |
| MDR Annex I: software on mobile platforms accounts for screen size and contrast, light and noise | UX-EU-16 |
| MDR Annex I: lay-use devices reduce user error in handling and interpreting results, and warn when no valid result was produced | UX-EU-17, UX-EU-18, UX-EU-19 |
| FDA: a critical task is one that, done wrong or not done, could cause serious harm; severity matters more than probability | UX-US-28, UX-US-32 |
| FDA: risk control order is inherent safety by design, then protective measures, then information for safety | UX-US-33 |
| FDA: saying labeling or training fixes a critical-task error is not acceptable without data | UX-US-42 |
| FDA human factors guidance reissued 3 August 2026; content-of-submissions guidance final 29 May 2026 | UX-US-25, UX-US-47 |

Change control for such a component:

| Point | Rows |
|---|---|
| Any software modification is a design change under FDA's quality system rules (2017 guidance, issued before the QMSR; check against the QMSR, effective 2 February 2026) | CH9, CH10, QS1 |
| Start with a risk-based assessment of whether the change could significantly affect safety or effectiveness | CH11 |
| FDA inspection looks for changes assessed for risk and impact before implementation, software changes included | QS34 |
| MDR: design changes are taken into account in a timely manner within the QMS | EU2 |
| FDA HF submission categories: a change to the user interface, users, uses, environment, training or labeling moves a modified device past Category 1 (Decision Point B); no new or impacted critical tasks gives Category 2 with a rationale; validation data depend on UI history, complexity and existing controls; Category 3 needs a full HFE/UE report with validation | UX-US-48 to UX-US-52 |
| FDA recommends keeping human factors information whether or not it is submitted | UX-US-53 |

The model lays these out as questions for the owner. It never decides the HF submission category, significance, or whether a submission is needed.

## 6. Components that show decision support to clinicians

If a component displays a recommendation from clinical decision support, FDA's Criterion 4 expects the clinician to be able to review the basis independently: inputs explained, plain-language basis, knowns and unknowns, decision-relevant information first (UX-US-65, UX-US-67 to UX-US-70); usability testing may be needed (UX-US-71). Whether software meets the criteria is the regulatory owner's call.
