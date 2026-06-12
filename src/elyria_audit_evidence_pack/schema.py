"""Public-safe schema helpers for Elyria AI Audit Evidence Pack."""

ADMIT = "ADMIT"
HOLD = "HOLD"
REFUSE = "REFUSE"
REVALIDATE = "REVALIDATE"

REQUIRED_EVIDENCE_FIELDS = [
    "packet_id",
    "system_id",
    "decision",
    "decision_timestamp",
    "decision_owner",
    "governance_owner",
    "reason_codes",
    "control_checks",
    "evidence_refs",
]

CRITICAL_PROOF_FIELDS = [
    "packet_id",
    "decision",
    "decision_owner",
    "decision_timestamp",
]


def missing_required_fields(packet: dict) -> list[str]:
    """Return required evidence fields missing from a packet."""
    return [field for field in REQUIRED_EVIDENCE_FIELDS if not packet.get(field)]


def missing_critical_fields(packet: dict) -> list[str]:
    """Return critical proof fields missing from a packet."""
    return [field for field in CRITICAL_PROOF_FIELDS if not packet.get(field)]
