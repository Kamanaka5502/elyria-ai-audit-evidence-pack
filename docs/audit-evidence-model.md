# Audit Evidence Model

## Purpose

The audit evidence model defines the minimum evidence required to prove that an AI governance decision happened and can be reviewed later.

---

## Required Evidence Fields

| Field | Purpose |
|---|---|
| Packet ID | Unique evidence packet identifier. |
| System ID | AI system or workflow governed. |
| Decision | ADMIT / HOLD / REFUSE / REVALIDATE. |
| Decision timestamp | When the decision occurred. |
| Decision owner | Accountable person or team for the decision. |
| Governance owner | Accountable governance function. |
| Reason codes | Why the decision happened. |
| Control checks | Controls evaluated before decision. |
| Evidence references | Records supporting the decision. |
| Replay readiness | Whether the decision can be reconstructed later. |

---

## Critical Proof Boundary

The following fields are critical. If missing, the packet cannot prove the governance decision:

- packet ID
- decision
- decision owner
- decision timestamp

---

## Evidence Rule

```text
An audit packet is valid only when decision, ownership, evidence, controls, and replay state can be reconstructed later.
```
