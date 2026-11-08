# Delivery dependency view

No invented dates. List Verify / steward siblings when they gate circulation.

| Field | Value |
|---|---|
| Owner | |
| Exhibit id / locked | |
| Interpretable question | |

## Layout — table (authoritative)

| From | To | Dependency type | Owner of dependency | Date (only if supplied) | [GAP]? |
|---|---|---|---|---|---|
| Baseline study | Pilot design | finish-to-start | | | |
| Integrity pack | Board seal | finish-to-start | | | |
| Verify run | External circulation | finish-to-start | | | |

## Layout — visual

```mermaid
%%{init: {'theme': 'neutral'}}%%
flowchart LR
  A[Baseline / evidence] --> B[Trial or delivery design]
  B --> C[Integrity path]
  C --> D[Board seal]
  V[Verify / steward] -.->|gates circulation| D
```

Prepared by: ________  Reviewed by: ________
