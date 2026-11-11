# Worked example: a study report the person wants to paste

Invented case for teaching. No real product, company or person.

## Context card (from trusted-intake, already in the conversation)

```
TRUSTED context: payer email built from a study report

Reader          a payer, through the person's email                 (stated)
Use             promotional                                         (assumed)
Material        an unpublished phase III clinical study report, about 400 pages,
                with subject listings in the appendices (as you described it)
Inputs          unpublished study data, possibly patient-level details
AI use policy   not asked yet
Stakes          leaving the company
```

## Request

"Summarize the efficacy section of this study report for a payer email. Can I paste it
here? I'm using the free version of the chat tool."

## Input note (as the person sees it)

Before this goes into the assistant

What it looks like: an unpublished clinical study report. These usually include
patient-level listings and case narratives in the appendices.

The question for your company: does your AI use policy allow this tool for unpublished
study data, and for patient-level details? I can't answer that; your policy, its owner,
or your data protection team can.

Safer ways to get what you need
1. The minimum extract: only the efficacy summary tables, without the appendices.
2. A company-approved tool for this material, if your policy names one.
3. Biostatistics or clinical operations can prepare an aggregate summary with
   identifiers removed. That reduces what is shared; it does not make it anonymous.

Tell me which route you want, and what the result is for.

I have not decided whether this tool may be used for this material, and I have not
judged whether anything in the report is anonymous.

## Work offered only after a route is chosen

If the person pastes only an aggregate efficacy table that their policy allows, the
summary uses the figures in that table exactly as they appear and adds nothing from the
appendices. Because the summary goes to a payer, it then goes through the person's
review process for material sent to payers before it is sent.

## Why it is written this way

- The decision about the tool and the data is put back to the person and their policy
  owner, with the people who can answer named by kind.
- No summary was written from material that has not been cleared to go in.
- The note repeats no identifier and no detail from the report.
- The routes are the ones that fit, three and not a generic list of five.

## Lines returned to trusted-check (not shown to the person)

```
Ethical · what went in: 2 questions for your AI use policy (unpublished study data, patient-level details), 3 safer routes offered, 0 sensitive details kept out of the output (not tool-checked)
```
