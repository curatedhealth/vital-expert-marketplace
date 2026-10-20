# Indicators: adoption, drift, accessibility status and concerns

Interpretive reference for DH-02.04.2.2 (A1, B1). Rows from `design-system-additions.md` (DSX) and `UX_ACCESSIBILITY_USABILITY.md` (UX-), read on 19 October 2026.

No published source in this skill measures design-system adoption, drift or effectiveness, and no benchmark exists for them (`literature.search_literature` found none on 19 October 2026) `[GAP]`. The indicators below are counts on the person's own inventory, defined here so they are computed the same way each time. They carry no target. A rule (for example "no clinical surface behind current") is the person's.

## 1. Inventory indicators (computed by `scripts/ds_adoption.py`)

| Indicator | Definition | What it does not show |
|---|---|---|
| Adoption of a component | Products using any version of it, out of the person's product list (or out of products named in the inventory, labeled) | Whether each product uses it correctly; presence of the system's code does not show the implementation is usable or accessible (DSX-41) |
| On current version | Products using the version the person declares current, out of products using the component | Whether "current" is itself tested (see accessibility status) |
| Drift distance | Per use: current, behind by major, minor or patch (when both versions are dotted numbers), ahead of current (an inconsistency to check), or differs (not computable) | Whether a minor step is a breaking change: that depends on the person's version rule (GOV.UK's convention, DSX-35, is one example) |
| Behind current, by owner | Uses not on current, per owner; clinical and device uses counted separately | Why a product is behind; causes are hypotheses for B1 |
| Version spread | Distinct versions of a component in use | Which spread is acceptable (the person's rule) |
| Accessibility status as recorded | The person's own status per component version, counted per use and for clinical and device uses | Conformance of any product: conformance is for full pages and processes (UX-STD-21, UX-STD-22) |
| Local modification | Uses marked override or fork per component | Whether the override still meets accessibility standards (DSX-34); forks receive no system updates (DSX-33) |
| Flagged lifecycle | Uses of components carrying a lifecycle value the person flags (default list: the USWDS names "use with caution", "deprecated", "retired", DSX-28, DSX-29) | Whether the component fails anything today: status is the system owner's label |
| Products using no listed component | From the person's full product list | Whether they should |
| Device UI unchanged (not an indicator) | None: drift counts cannot show it | That a device user interface is unchanged since certification: each component version shipped into a device is a software modification and so a design change (CH9), assessed before implementation (QS34) and taken into account in the QMS (EU2) |

The register's own method for this competency: count surfaces not on the current version by owner, separate clinical tasks from marketing surfaces, and never hide a clinical task on an old component.

## 2. Accessibility concern indicators (from the person's issue log, if they keep one)

GOV.UK's accessibility strategy names indicators for its own design system (DSX-47, DSX-48), measured every 6 months (DSX-49). They are offered as options the person may adopt:

| Indicator | GOV.UK wording, in short | Rows |
|---|---|---|
| Concerns recorded | Accessibility concerns recorded as issues | DSX-47 |
| Concerns in the accessibility statement | Concerns listed in the system's accessibility statement | DSX-47 |
| Time to resolution | Time from first recording or report of a concern to its resolution | DSX-48 |
| Regressions | Accessibility bugs that reach a release | DSX-48 |
| Who finds them | Concerns raised by product teams versus raised internally | DSX-48 |

Classification aids, as GOV.UK uses them: theoretical versus evidenced concerns (DSX-44); kinds of evidence (DSX-46); high severity when all three of its factors hold (DSX-45). The person decides whether to classify this way.

The script does not compute these; with an issue log (opened date, resolved date, component, version, found by, evidence type) they are counted by hand or with a short table, to an as-of date the person states.

## 3. What a live check adds (A2)

A component in the inventory at the current version can still breach its contract on a surface: a team overrides a state, changes a token, or puts clinical content in a component the contract forbids it in. USWDS expects product teams to test components in context at page level (DSX-38). A2 checks one surface against the contract; its results feed B1.

## 4. External context for device surfaces (optional)

`regulatory-dh.search_safety_events` returns FDA recalls and MHRA alerts by manufacturer, product title words or product code. It has no use-error or user-interface field (`references/tools.md`). Events are quoted as recorded, never counted as an indicator of the person's design system and never read as cause.
