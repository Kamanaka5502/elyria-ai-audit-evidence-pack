# Executive Demo Script

## Purpose

This script supports a concise buyer, hiring-panel, or executive walkthrough of the Elyria AI Audit Evidence Pack.

---

## Opening

```text
Governance that cannot be proven later is only an assertion.

The Elyria AI Audit Evidence Pack preserves the decision, owner, timestamp, reason codes, control checks, evidence references, and replay-readiness state needed to prove what governance happened.
```

---

## Walkthrough Path

1. Start with `README.md` and explain the evidence gap.
2. Open `docs/why-and-how.md` and show the decision path.
3. Open `docs/audit-evidence-model.md` and show required evidence fields.
4. Open `docs/evidence-packet-template.md` and show the buyer-facing packet format.
5. Open `docs/replay-readiness-model.md` and show how later review reconstructs the decision.
6. Open `src/elyria_audit_evidence_pack/engine.py` and explain the decision order.
7. Open `examples/` and show ADMIT, HOLD, REFUSE, and REVALIDATE packets.
8. Open `sandbox/outputs/sample-sandbox-results.json` and show sample results.
9. Open `reports/sample-audit-evidence-readiness-report.md` and show executive output.
10. Close with `docs/production-readiness-checklist.md`.

---

## Close

```text
The value is proof preservation. This gives the enterprise a repeatable evidence layer for audit, compliance, incident review, executive oversight, and future replay.
```
