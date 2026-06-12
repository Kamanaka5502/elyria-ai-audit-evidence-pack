# Audit Evidence Scorecard

## Purpose

The Audit Evidence Scorecard gives buyers and enterprise reviewers a practical way to assess whether an AI governance evidence packet is complete, replay-ready, and suitable for audit reliance.

---

## Scoring Model

| Domain | Score | Notes |
|---|---:|---|
| Packet identity | 0-5 | Packet ID and system ID are present and unique. |
| Decision record | 0-5 | Decision and timestamp are explicit. |
| Ownership | 0-5 | Decision owner and governance owner are identified. |
| Reason codes | 0-5 | Decision rationale is structured and reviewable. |
| Control checks | 0-5 | Controls checked before decision are recorded. |
| Evidence references | 0-5 | Supporting evidence references are traceable. |
| Replay readiness | 0-5 | Future reviewer can reconstruct the decision. |
| Change awareness | 0-5 | Post-decision system change is checked. |
| Retention readiness | 0-5 | Packet can survive later audit and review. |
| Access protection | 0-5 | Packet access can be controlled and monitored. |

Maximum score: 50

---

## Readiness Bands

| Score | Readiness Band | Decision Guidance |
|---:|---|---|
| 45-50 | Audit-ready | ADMIT if no critical proof blocker exists. |
| 35-44 | Evidence-ready with conditions | HOLD until gaps are closed. |
| 20-34 | Weak evidence | HOLD or REFUSE depending on missing fields. |
| 0-19 | Not audit-reliable | REFUSE until evidence is rebuilt. |

---

## Critical Blockers

Any of the following should override the numeric score:

- missing packet ID
- missing decision
- missing decision owner
- missing decision timestamp
- missing system ID
- no evidence references
- replay readiness cannot be established

---

## Executive Summary Template

```text
This evidence packet is currently [ADMIT / HOLD / REFUSE / REVALIDATE].
The primary audit factors are [decision record, ownership, reason codes, control checks, evidence references, replay readiness].
The required next steps are [remediation items].
```
