# Task VR-3.1 Drop unsupported detail

## Formula

| Slot | In this task |
|---|---|
| Worker | Evidence lead (claim checker), editing the draft. Does not sign. |
| Workflow | List the specific details, match each to a finding, delete the rest, then stop. |
| Skill | VR-3.1 Honesty |
| Knowledge | `references/rules.md`, `references/drop-list.md`, `references/patterns.md` |
| Tool | None. Read the findings. Do not call a new checker to bless a guess. |
| Prompt | Keep a detail only when a finding's passage states it. |
| Template | `assets/drop-unsupported-detail-output.md` |
| Input | The draft plus the findings from support decision. |
| Governance | Do not invent a citation for a sentence you deleted. VR-H1, VR-H3, VR-H4, VR-H5 |

## Companion

| State | What to do |
|---|---|
| Findings present (VERIFY or manual) | Apply the drop list against those findings only. |
| No findings | Stop; ask for support-decision. Do not invent supported rows. |

## Steps

1. List every number, date, named person, quotation, and performance or compliance claim.
2. Keep one only when a finding is supported or partial and the passage states that detail.
3. Delete "experts say," "leading analysts," and "people report."
4. Delete a guess that fills a silence, including a plausible decade or a certification the passage does not name.
5. End on a fact the passage states. Do not add a generic closing sentence.
6. A citation line is the formatted line from build_citation, with no caption, and only for a source that survived.

## Checks

- No number remains that the passage does not state.
- A deleted sentence is not rewritten as a softer guess.

## Boundaries

Do not apply layout, contrast, or punctuation rules from another project.
