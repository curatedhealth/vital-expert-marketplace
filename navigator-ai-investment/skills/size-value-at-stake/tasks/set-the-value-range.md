# B Set the value range

Framework task: 1.2 Value-at-Stake Sizing, Part B.

## What this task delivers

For the chosen drivers, the value at stake as a low, likely and high range, with unit, basis and the assumptions that must hold; and the cost of a wrong call. Together these are section 2 of the Decision Record, "Value at stake: a range, and the cost of a wrong decision" (method.md V2).

Why it matters: a single number invites false precision and turns a hypothesis into a promise. A range with its basis tells the room how much is known, and its width is information: a wide range on a big decision says "learn more before committing".

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | AI Investment Decision Lead |
| Skill | 1.2 Value-at-Stake Sizing, Part B |
| Workflow | The steps below |
| Knowledge | `references/method.md` (V1 to V4) |
| Tools | `value_range` (stores the range on the brief); `scripts/value_check.py range` |
| Prompt | This guide |
| Template | `assets/value-range-worksheet.md`; "Value at stake" section of the report |
| Input | The chosen drivers and their scores (task A); the decision frame; any figures the person supplies |
| Governance | `references/governance.md` |

## Workflow

### Step 1. Ask for the range, with its basis

Ask once, with the worksheet: "What is this worth: a low, a likely and a high figure, in what unit, and based on what?" The unit may be money, time, capacity or another measure of the driver's dimension. The basis is how the figure was reached ("6 hours a week per rep from our 2025 time study, times 400 reps", "the team's judgment").

Never propose a number yourself, and never fill in a benchmark from general knowledge. If the person asks for a benchmark, say that an external figure must name its primary source; offer to use one they supply, or to keep the range owner-stated and wide.

### Step 2. Check the range

Run `scripts/value_check.py range`, or check by hand:

- low, likely and high are all given, and low differs from high;
- low is not above likely, and likely is not above high;
- unit and basis are stated;
- every figure carries its class: measured with source (M), owner-stated (O), or from a document (V, cited); an external figure without a primary source is removed and listed as a gap (method.md V3);
- the width fits the confidence scored in task A: high confidence with a very wide range, or low confidence with a narrow one, is pointed out as a question, not corrected.

If any check fails, say which and ask for the fix in one question.

### Step 3. Name the assumptions

Ask: "What has to be true for this range to hold?" Record each assumption in the person's words, with an owner if they name one. These carry forward to the record's "Assumptions and risks" section.

### Step 4. The cost of a wrong call

Take it from the frame if present; otherwise ask. Keep it in the owner's words; a figure is welcome if the person has one, with its class.

### Step 5. Store the range (connector)

If a brief is open, call `value_range` with `brief_id` and the range inside `payload`: `{"low", "mid", "high", "unit", "basis", "drivers": [...]}`. Put the range inside `payload`, not at the top level: the hosted path drops top-level fields (references/tools.md). Measures are optional here; any measure passed must carry a baseline and an owner, otherwise leave measures to the outcome work. If no brief is open, say the range is held in the report only.

## Boundaries

- No point estimates, no number you made up, no benchmark from memory.
- No "will deliver" or "saves". The range is estimated value at stake, not value realized.
- No pricing, no investor forecast, no NPV model. If the person needs one, say it is outside this skill and that the range and basis here can feed it.

## When you are unsure

If the person cannot give any figure, record the range as `[GAP]` with "no basis yet" and name what would produce one (a baseline measurement, a pilot). The report still goes out, with the gap first in the gaps list.
