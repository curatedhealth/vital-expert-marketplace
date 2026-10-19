# B Name the strategic goal

Framework task: 1.1 Decision Framing, Part A, task B.

## What this task delivers

The strategic goal this decision serves, in one sentence, and the value theme behind it, chosen by the person from the catalogue at the level that fits the audience. It answers the Direction question: why does this matter?

Why it matters: an AI investment that serves no stated goal cannot be valued, prioritized or stopped. The method requires every walk to be oriented by direction and to reach an outcome (method.md M4). A goal written as a solution ("roll out AI across Medical") hides the real reason and fixes the answer before the options are compared.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 1.1 Decision Framing, Part A, Name the strategic goal |
| Workflow | The steps below |
| Knowledge | `references/method.md` (M4, M5); `references/audience-calibration.md` (value themes held by the catalogue) |
| Tools | `catalogue_search`, `catalogue_list_children` (value driver pillar) |
| Prompt | This guide |
| Template | `assets/decision-contract-output.md`, "Strategic goal" block |
| Input | The accepted decision statement from task A, the audience, any strategy documents in the conversation |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Ask for the goal

Ask: "Which strategic goal of the organization does this decision serve?" Accept a goal from a strategy document in the conversation (class V, cite it) or from the person (class O).

If there is none, ask for one sentence: where the organization wants to be and why. Record it as owner-stated. Never invent a goal and never refuse to proceed.

### Step 2. Check it is a goal, not an objective or a solution

Apply method.md M5:

- **A goal** says where the organization wants to be and why ("be the partner payers trust first on real-world value"). Keep it.
- **An objective** has a number and a date ("cut dossier time by 40% by 2027"). It belongs to the outcome work that follows. Keep it, label it "objective, carried to outcomes", and ask for the goal it serves.
- **A solution** names a means ("deploy AI agents in Medical"). Restate it as the goal it serves, and keep the solution as an option for later.

### Step 3. Offer value themes at the audience's level

Only once a goal has been stated. Without a goal there is nothing to match, and offering themes first steers the person toward the catalogue's words instead of their own.

Search the value driver catalogue for themes that match the goal: `catalogue_search` with `pillar` VD, `level` set by the audience (1 for C-suite, 2 for a head of function, 2 or 3 for a head of department), and the goal's key words as `query`. Do not pass `function`; it removes every value driver row (references/tools.md).

Show at most five candidates by display name, with the value dimension where the catalogue states one. The person picks one or two, or says none fits. Never pick for them.

To go one level deeper, take the chosen row's `id` (not its code) and call `catalogue_list_children`. Stop at the level the audience works at; deeper drivers are chosen in *Value-at-Stake Sizing*.

If the connector is unavailable, show the value themes listed in `references/audience-calibration.md` (as of its read date) and say they are the catalogue's themes as last read, not a live search.

### Step 4. Record the link

Write: *"This decision serves [goal] (class), through [value theme] (chosen by [person])."* If no theme fits, record the goal alone and mark the theme `[GAP]`: "no catalogue theme matched; goal kept as stated".

## Build the output

Fill the "Strategic goal" block of `assets/decision-contract-output.md`.

## Boundaries

- Do not write outcomes, objectives with numbers, or measures here. Carry them forward, labeled.
- Do not offer value drivers below the audience's level unless asked.
- Do not present a catalogue theme as the client's own strategy. It is a vocabulary the person chooses from.

## When you are unsure

If the person names two goals that pull in different directions, record both and say the tension will matter when options are compared. Do not resolve it for them.
