# Gap rules

A gap is information. The person needs to know why something could not be checked, because each reason leads to a different next step.

## The person's documents and log

| Class | When | How to word it | Next step |
|---|---|---|---|
| Field missing | The list or log lacks a column a check needs (version, status, approval date) | "Not assessable: the list has no version column `[GAP]`." | Ask for an export with the field |
| Unreadable value | A date or status cannot be read | "Approval date unreadable ('Q2') `[GAP]`." | Ask the record owner |
| Title only | Only a document title was seen | "Present by title; content not checked." | Share the document if content matters |
| Out of the set | The record may exist outside the list given | "Not in the list provided (as of DATE)." Never "does not exist" | Ask whether another system holds it |

## Rules

| Class | When | How to word it |
|---|---|---|
| Sourced | A row states it | Rule and row id |
| Standard text not sourced | ISO 13485 clause content | "Required by your procedure PROC-ID" if the person's procedure states it; otherwise "ISO 13485 clause text not in the sourced references `[GAP]`" |
| Retention period not sourced | No row sets a period | `[GAP]`; never a period from memory |

## Never

- Never turn a gap into "missing", "noncompliant" or "failed". Missing means expected and not in the list given.
- Never fill a gap from memory or by guessing a date.
