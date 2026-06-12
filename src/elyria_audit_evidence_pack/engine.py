"""Public-safe Elyria AI Audit Evidence Pack engine."""

from __future__ import annotations

from .schema import ADMIT, HOLD, REFUSE, REVALIDATE, missing_critical_fields, missing_required_fields


def evaluate_evidence_packet(packet: dict) -> dict:
    """Evaluate whether an AI governance evidence packet is audit-ready."""
    critical_missing = missing_critical_fields(packet)
    required_missing = missing_required_fields(packet)
    reasons: list[str] = []
    remediation: list[str] = []

    if critical_missing:
        reasons.append("CRITICAL_PROOF_BOUNDARY_MISSING")
        remediation.append("Rebuild the evidence packet before relying on the governance decision.")
        return _decision(REFUSE, reasons, remediation, packet, critical_missing, required_missing)

    if packet.get("system_changed_after_decision") is True:
        reasons.append("PACKET_REVALIDATION_REQUIRED")
        remediation.append("Revalidate the packet because system conditions changed after the decision.")
        return _decision(REVALIDATE, reasons, remediation, packet, critical_missing, required_missing)

    if required_missing:
        reasons.append("EVIDENCE_PACKET_INCOMPLETE")
        remediation.append("Complete missing required evidence fields before audit reliance.")
        return _decision(HOLD, reasons, remediation, packet, critical_missing, required_missing)

    if packet.get("replay_ready") is not True:
        reasons.append("REPLAY_READINESS_NOT_CONFIRMED")
        remediation.append("Confirm replay readiness before treating packet as audit-ready.")
        return _decision(HOLD, reasons, remediation, packet, critical_missing, required_missing)

    reasons.append("EVIDENCE_PACKET_AUDIT_READY")
    return _decision(ADMIT, reasons, remediation, packet, critical_missing, required_missing)


def _decision(outcome: str, reasons: list[str], remediation: list[str], packet: dict, critical_missing: list[str], required_missing: list[str]) -> dict:
    return {
        "packet_id": packet.get("packet_id"),
        "system_id": packet.get("system_id"),
        "outcome": outcome,
        "reason_codes": reasons,
        "required_remediation": remediation,
        "evidence": {
            "decision": packet.get("decision"),
            "decision_owner": packet.get("decision_owner"),
            "decision_timestamp": packet.get("decision_timestamp"),
            "governance_owner": packet.get("governance_owner"),
            "critical_missing": critical_missing,
            "required_missing": required_missing,
            "replay_ready": packet.get("replay_ready"),
        },
    }
