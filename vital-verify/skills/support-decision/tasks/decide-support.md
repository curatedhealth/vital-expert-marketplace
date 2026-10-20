# Task VR-1.2 Decide support for one claim against a quoted passage

Maps to TRUSTED Prove `claim-assessment` Part B (`TR-8.1.2`).

## Formula

| Slot | In this task |
|---|---|
| Worker | Evidence lead (claim checker). Does not search and does not sign. |
| Workflow | Admit the source, compare the quoted passage, choose one status, act on it, recheck any rewrite, then print the faithfulness line only after every finding. |
| Skill | VR-1.2 Support decision |
| Knowledge | `references/rules.md` (R1–R6), `references/patterns.md`, `references/statuses.md` |
| Tool | VERIFY `check_claim` or `verify_text`; see companion slot |
| Prompt | Decide this passage only. Name the unsupported part when the status is partial. |
| Template | `assets/decide-support-output.md` |
| Input | One claim, one already graded source, one quoted passage. |
| Governance | Inadmissible or an empty passage is unverifiable. Do not replace the sentence with a guess. VR-H1, VR-H3, VR-H4, VR-H5, VR-H11 |

## What "supported" means

Tell the person this in plain words every time results are shown:

> A match means the passage you gave says the same thing as the sentence. It does not
> mean the sentence is true, that the source is good, or that the work is ready. VERIFY
> compares words in the sentence with words in the passage.

## Companion

| State | What to do |
|---|---|
| VERIFY connected | Call `check_claim` with claim, admitted source id, and quoted passage. Or `verify_text` for a short first pass on text the person already supplied with its sources (at most 60 findings). Exact arguments: `references/tools.md`. |
| VERIFY absent | Compare by hand. Use the **manual result words** below. Never use VERIFY status words. Head the result "Not tool-checked". |

Never send a passage you wrote. Never invent a status, tier or faithfulness percent the
tool did not produce (VR-H4).

## Steps

1. Confirm the tier from source grading. If it is inadmissible, or the passage is empty,
   status is unverifiable and the reason is "No admissible source was available."
2. If the tier is bronze, status is at most partial and the rationale is "source tier bronze."
3. For gold or silver, call `check_claim` when a key is present. Otherwise apply the table
   and mark the decision manual.
4. If the scorer says supported on anything other than gold or silver, demote it to partial.
5. Map the result onto a gap class in the gap rules.
6. Recheck every rewrite. Without VERIFY, label it "rewritten, not tool-checked".
7. After the reference list, print one faithfulness line:
   (supported + 0.5 × partial) ÷ (supported + partial + unsupported + contradicted + unverifiable),
   as a whole percent. Leave out_of_scope out of the denominator.

## Each result in plain words, and what to do

| VERIFY status | Say to the person | Do |
|---|---|---|
| `supported` | "Your passage says this." | **Keep** as written. Show the passage. |
| `partial` | "Your passage says part of this. It does not say <the missing part>." | **Rewrite to match**; recheck. |
| `unsupported` | "Your passage does not say this." | **Remove**, or **ask** for a passage that does. |
| `contradicted` | "Your passage says something different: <quote>." | **Ask.** Do not send the sentence. |
| `unverifiable` | "This could not be checked: <reason>." | **Remove.** Never replace with a likely value. |
| `out_of_scope` | "This is an opinion, recommendation or definition." | **Leave to the person** and their review. |

## Without VERIFY: the same method by hand

| Manual result (not tool-checked) | Do |
|---|---|
| Found in your passage | Keep; show the passage |
| Partly found: <missing part> not in your passage | Rewrite to match |
| Not found in your passage | Remove or ask |
| Your passage says something different | Ask |
| No passage to compare with | Remove |
| Opinion, recommendation or definition | Leave to the person |

## When asked to mark claims supported without a check

Decline in plain words. Offer: run the check now; label them "not checked"; or list which
passages would be needed. Never produce the labels (`references/governance.md`).

## Checks

- The rationale quotes the deciding words.
- Partial names the part the passage does not state.
- The faithfulness line is not labelled as the source score.

## Boundaries

- Does not search, grade sources, check currency, or build citations.
- Does not judge clinical meaning, fair balance or whether a claim is permitted.
- Never says the work is accurate, correct, verified or ready.
