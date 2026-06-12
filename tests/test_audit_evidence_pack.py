from elyria_audit_evidence_pack import evaluate_evidence_packet


def base_packet():
    return {
        "packet_id": "TEST-AUD-001",
        "system_id": "test-system",
        "decision": "ADMIT",
        "decision_timestamp": "2026-06-12T22:00:00Z",
        "decision_owner": "AI Governance Office",
        "governance_owner": "Enterprise Risk",
        "reason_codes": ["TEST_REASON"],
        "control_checks": ["owner_present", "decision_present"],
        "evidence_refs": ["test-evidence-001"],
        "replay_ready": True,
    }


def test_complete_packet_admits():
    result = evaluate_evidence_packet(base_packet())
    assert result["outcome"] == "ADMIT"
    assert "EVIDENCE_PACKET_AUDIT_READY" in result["reason_codes"]


def test_missing_required_evidence_holds():
    packet = base_packet()
    packet.pop("governance_owner")
    result = evaluate_evidence_packet(packet)
    assert result["outcome"] == "HOLD"
    assert "EVIDENCE_PACKET_INCOMPLETE" in result["reason_codes"]


def test_missing_critical_proof_refuses():
    packet = base_packet()
    packet.pop("decision")
    result = evaluate_evidence_packet(packet)
    assert result["outcome"] == "REFUSE"
    assert "CRITICAL_PROOF_BOUNDARY_MISSING" in result["reason_codes"]


def test_changed_system_revalidates():
    packet = base_packet()
    packet["system_changed_after_decision"] = True
    result = evaluate_evidence_packet(packet)
    assert result["outcome"] == "REVALIDATE"
    assert "PACKET_REVALIDATION_REQUIRED" in result["reason_codes"]
