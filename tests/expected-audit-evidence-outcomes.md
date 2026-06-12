# Expected Audit Evidence Outcomes

## Purpose

This file documents expected public-safe scenario outcomes for review, testing, and buyer walkthroughs.

---

| Scenario | Expected Decision | Reason |
|---|---|---|
| `complete-evidence-packet.json` | ADMIT | Evidence packet is complete and replay-ready. |
| `missing-owner-evidence.json` | HOLD | Required ownership evidence is incomplete. |
| `missing-decision-record.json` | REFUSE | Critical decision proof is missing. |
| `changed-system-needs-replay.json` | REVALIDATE | System changed after packet creation. |

---

## Validation Rule

```text
A scenario passes when the engine output matches the expected decision and preserves reason codes, remediation, and evidence fields.
```
