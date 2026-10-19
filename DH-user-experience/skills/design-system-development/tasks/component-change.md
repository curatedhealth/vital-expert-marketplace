# A2 Component change

Framework task: DH-02.04.2.1, Part A, task A2. Replaces the register task "Component change" (CF-12.02.04.2.1.2).

## What this task delivers

A change note for one component change: the new version, what changed, which states and accessibility criteria it touches, which products and surfaces use the component (from the person's inventory), what must be rechecked on each, which clinical tasks depend on the changed states, and, where a surface is part of a medical device user interface, the change-control questions the change raises for the person's quality and regulatory owners. It answers "what does this change touch, what do we recheck, and is there a device question?"

Why it matters: a component change ships into every product that updates. Where the component sits in a device user interface, FDA treats any software modification as a design change (CH9), expects a risk and impact assessment before implementation (QS34), and a change to the user interface moves a modified device past HF Submission Category 1 (UX-US-49). The register rule: do not change a state that a clinical task depends on without naming that task.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | UX/UI Designer, Digital Health (`ux-ui-designer-digital-health`) |
| Skill | DH-02.04.2.1 Part A, Component change |
| Workflow | The steps below |
| Knowledge | `references/component-requirements.md` (sections 2, 3 and 5); `references/governance-models.md` section 4; `references/change-control-rows.md`; `references/UX_ACCESSIBILITY_USABILITY.md` |
| Tools | `scripts/ds_adoption.py` (version map, optional); `regulatory-dh.search_safety_events` (counted, optional, device surfaces only); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/component-change-output.md` |
| Input | The request and its context: the component, old and new version, what changed (states, behavior, tokens, markup), the inventory or list of products using it, which surfaces are clinical or device, the A1 contract if any |
| Governance | `references/governance.md`; the change note may proceed; significance, HF category, submissions and release stop |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. The post-market-watch job also reads safety events but sets a watch; it is not called. |

## Read the request

- **The change.** Old and new version, and what changed, in the person's words. Ask whether any state was added, removed or altered, and whether any token (color, spacing, type size) changed.
- **Where it is used.** The inventory, or a list of products and versions. Without it, the recheck list is "products not listed `[GAP]`".
- **Clinical and device surfaces.** Which products are clinical tasks and which are device user interfaces per the person's regulatory owner.
- **Versioning.** Whether the person's scheme marks breaking changes (for example by the first digit, as GOV.UK does, DSX-35). The person states whether this change breaks compatibility.
- **Mode.** Short for a direct question; full for a change record.

## Workflow

### Step 1. Fix the frame

Write back: component, old and new version, the change in the person's words, breaking or not (their call), products in scope. Confirm.

### Step 2. Version map

With the inventory and code execution, run `python3 scripts/ds_adoption.py INVENTORY.csv` and take the component's rows: which products use which version, owner, clinical and device flags. Without code execution, read the same from the person's list. Products on a fork receive no update from the system (DSX-33): list them separately, because the change will not reach them.

### Step 3. Criteria and states touched

Map the change to states and to the criteria in `component-requirements.md` section 2. Examples of the mapping, from the rows: a size or spacing change touches Target Size 2.5.8 (UX-STD-11); a color or token change touches contrast (UX-STD-15, UX-STD-16) and Use of Color (DSX-02); When the person gives hex values, compute the ratio for both the old and the new value against the background and text color they state (ask if not stated), using DSX-51, and label it "computed, not a test result". a focus style change touches 2.4.7 and 2.4.11 (DSX-04, UX-STD-09); an error state change touches 3.3.1 (UX-STD-19); a new drag interaction touches 2.5.7 (UX-STD-10). A modified component is checked against accessibility standards again (DSX-34). State the changed value and the threshold side by side; do not say a value meets or fails a criterion without a test result the person supplied (exceptions and spacing decide 2.5.8).

### Step 4. Recheck list

For each product using the component: what to recheck (criteria, states, clinical tasks), with which kind of test (automated, manual, with people; UX-UK-24, DSX-37), and that the product team tests in context (DSX-38). Name every clinical task that depends on a changed state, as the person describes it. If the person cannot name the tasks, write "clinical tasks depending on this state not named `[GAP]`" and ask.

### Step 5. Device user interface questions (only for device surfaces)

Lay out the questions the change raises, each with its row, for the person's quality and regulatory owners. Never answer them.

| Question for the owner | Rows |
|---|---|
| Has the change been assessed for risk and impact before implementation? | QS34, CH11 |
| Is it recorded as a design change in the QMS? | CH9, CH10, EU2 |
| Does it change the user interface, users, uses, environment, training or labeling (Decision Point B)? | UX-US-49 |
| Does it introduce or impact a critical task, per the use-related risk analysis? | UX-US-28, UX-US-50 |
| What is the UI's history of use, its complexity, and the adequacy of existing risk controls (Decision Point D)? | UX-US-51 |
| If a use error is being handled by labeling or training, is there data that the fix works? | UX-US-42 |
| Are human factors records kept whether or not submitted? | UX-US-53 |

Optional field context: if the person names their own product or a partner's, call `regulatory-dh.search_safety_events` with `manufacturer`, a `since` date they choose, `jurisdiction` "US" and `limit` 5 (see `references/tools.md`: `product` matches title words only). Report events only by what the record states, for example a summary saying steps "may be displayed out of order". No cause is inferred, and no events is not evidence of safety.

### Step 6. Stops

State once: whether the change is significant, which HF Submission Category applies, whether a submission or notification is needed, and release of the new version into a regulated interface are for the owners the person names (dh-regulatory-strategy, dh-quality). Any new or changed patient-facing copy or clinical content in the component stops for its owner.

## Build the output

Follow `assets/component-change-output.md`. Answer first: the products to recheck (clinical and device ones first), the criteria the change touches, and whether a device change-control question is open. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every product using the component appears, or the gap is stated; forks are listed separately.
- Every clinical task depending on a changed state is named by the person or marked `[GAP]`.
- Device questions are questions, with rows; none is answered by the model.
- No statement that the change is minor, safe, non-significant or compliant.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- A change note, not a change-control decision (dh-quality document and change control) or a regulatory assessment (dh-regulatory-strategy).
- Human factors testing and usability evidence belong to the Healthcare UX Design skills (DH-02.04.4.x).
- Measuring which products moved to the new version later is the monitoring skill.
