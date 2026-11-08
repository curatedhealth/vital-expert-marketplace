"""Locked product constants (MLR Review v0.2, 24 October 2026)."""

from __future__ import annotations

PRODUCT = "mlr-review"
DISPLAY_NAME = "MLR Review"
KEY_PREFIX = "vmlr_"
PLUGIN = "vital-mlr-review"
SCOPE_READ = "mlr-review:read"
SCOPE_RECORD = "mlr-review:record"
MCP_PATH = "/api/mcp/mlr-review"
METHOD_VERSION = "2026-10-24.2"

LIABILITY_LINE = (
    "This prepares material for human MLR review. "
    "It is not medical, legal, or regulatory approval."
)

FORBIDDEN_PHRASES = (
    "approved for use",
    "mlr approved",
    "mlr_reviewed",
    "cleared for promotion",
    "regulator approved this copy",
    "fda approved this copy",
    "ema approved this copy",
    "mhra approved this copy",
)

AUDIENCES = ("hcp", "patient", "payer", "internal", "mixed")
CHANNELS = ("promo", "scientific_exchange", "med_info", "digital", "congress", "other")
CHAIRS = ("medical", "legal", "regulatory")
MLR_STATUSES = ("findings_only", "revise", "human_gate_required", "prep_complete")
CHAIR_DECISIONS = ("approve", "revise", "reject", "abstain")

TOOL_NAMES = (
    "mlr_intake",
    "mlr_list_rulesets",
    "mlr_get_ruleset",
    "mlr_get_packet_schema",
    "mlr_validate_packet",
    "mlr_align_claims",
    "mlr_compile_checklist",
    "mlr_handoff_verify",
    "mlr_build_prep_record",
    "my_usage",
)

COUNTED_TOOLS = frozenset(
    {
        "mlr_intake",
        "mlr_get_ruleset",
        "mlr_validate_packet",
        "mlr_align_claims",
        "mlr_compile_checklist",
        "mlr_build_prep_record",
    }
)
