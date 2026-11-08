# Owner protocol registry — Outcome Navigator

Protocols that may be cited in `input_pipeline.owner_protocol_ref` when converting or bridging external survey pipelines into the locked **1–10 Importance / Satisfaction** contract.

| Protocol id | Status | Title | Signed by | Signed on | Notes |
|---|---|---|---|---|---|
| `VITAL-ODI-TTB-1_10-v0` | **signed-option-A** | Top-two-box → 1–10 (SC-C1C2-R2-03) | Hicham | 8 November 2026 | **No conversion.** Fresh 1–10 people scores only. Not listed in `SIGNED_OWNER_PROTOCOLS` (that set is Option B conversion bridges only). |

**Rule:** A non-empty string alone is not a conversion allow. `outcome_priority_check.py` accepts a top-two-box→1–10 bridge only when `owner_protocol_ref` is in `SIGNED_OWNER_PROTOCOLS` (Option B). Option A signatures document refusal of silent conversion.

When an Option B mapping is approved: new protocol version, Status `signed-option-B`, fill mapping in the protocol file, add id to `SIGNED_OWNER_PROTOCOLS`.
