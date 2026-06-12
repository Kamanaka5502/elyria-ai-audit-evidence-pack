<div align="center">

# Elyria AI Audit Evidence Pack

## AI Governance Evidence · Audit Packets · Replay Readiness · Proof Preservation

![License](https://img.shields.io/badge/license-MIT-1f4f5a?style=for-the-badge)
![AI Governance](https://img.shields.io/badge/AI%20Governance-Audit%20Evidence%20Pack-1f4f5a?style=for-the-badge)
![Evidence](https://img.shields.io/badge/Evidence-Decision%20Record%20%7C%20Owner%20%7C%20Proof-5f8fa3?style=for-the-badge)
![Replay](https://img.shields.io/badge/Replay-Verification%20Ready-2f6f73?style=for-the-badge)
![Deployable Sandbox](https://img.shields.io/badge/Deployable-Sandbox%20Runner-2f6f73?style=for-the-badge)
![Validation](https://img.shields.io/badge/GitHub%20Actions-Validation%20Workflow-62d9ff?style=for-the-badge)
![Executive Ready](https://img.shields.io/badge/Executive--Ready-Board%20Readable-c9a66b?style=for-the-badge)

### **Prove what governance happened, what decision was made, what evidence supported it, who owned it, and whether replay can verify it later.**

![Decision](https://img.shields.io/badge/Decision-ADMIT%20%7C%20HOLD%20%7C%20REFUSE%20%7C%20REVALIDATE-1f4f5a?style=flat-square)
![Audit](https://img.shields.io/badge/Audit-Owner%20%7C%20Evidence%20%7C%20Timestamp%20%7C%20Reason-c9a66b?style=flat-square)
![Public Safe](https://img.shields.io/badge/Public--Safe-Protected%20Boundary-1f4f5a?style=flat-square)

</div>

---

## Executive Signal

```text
Governance that cannot be proven later is only an assertion.
```

Enterprise AI governance does not end with a decision. It must preserve the evidence needed to prove what happened, why it happened, who owned it, what controls were checked, and whether the decision can be replayed later.

The **Elyria AI Audit Evidence Pack** turns governance decisions into reviewable, replay-ready evidence packets.

---

## Repository Navigation

| Area | Start Here | Outcome |
|---|---|---|
| Executive overview | `README.md` | Understand audit evidence and replay-readiness value. |
| Why and how | `docs/why-and-how.md` | Explain why proof preservation matters and how the pack works. |
| Evidence model | `docs/audit-evidence-model.md` | Define required evidence fields and audit packet structure. |
| Replay readiness | `docs/replay-readiness-model.md` | Determine whether later review can reconstruct the decision. |
| Evidence template | `docs/evidence-packet-template.md` | Use a buyer-facing audit packet template. |
| Production readiness | `docs/production-readiness-checklist.md` | Review production-candidate requirements and deployment boundaries. |
| Deployment modes | `docs/deployment-modes.md` | Use local, workshop, pilot, enterprise, and production-adaptation modes. |
| Architecture diagram | `docs/architecture-diagram.md` | Review the end-to-end evidence flow. |
| Pilot sandbox | `sandbox/runner.py` and `sandbox/outputs/sample-sandbox-results.json` | Execute public-safe evidence scenarios. |
| Scorecard | `docs/audit-evidence-scorecard.md` | Assess audit evidence completeness. |
| Demo script | `docs/executive-demo-script.md` | Present the repo to buyers, hiring panels, or executives. |
| Visual system | `docs/design-language.md` and `docs/visual-index.md` | Review visual language and buyer scan path. |
| Sample report | `reports/sample-audit-evidence-readiness-report.md` | Review enterprise-style output. |

---

## Deployable Sandbox Quick Start

Run the public-safe sandbox from the repository root:

```bash
python sandbox/runner.py
```

Expected scenario path:

```text
complete-evidence-packet.json      → ADMIT
missing-owner-evidence.json        → HOLD
missing-decision-record.json       → REFUSE
changed-system-needs-replay.json   → REVALIDATE
```

The sandbox writes results to:

```text
sandbox/outputs/sandbox-results.json
```

A sample output is preserved at:

```text
sandbox/outputs/sample-sandbox-results.json
```

---

## What This Solves

Many AI governance programs can say a review happened. Fewer can prove it later.

Audit-readiness requires more than logs. It requires a decision record, owner record, evidence record, reason codes, timestamps, source references, control checks, remediation path, and replay readiness.

The **Elyria AI Audit Evidence Pack** provides a public-safe, enterprise-ready reference architecture for producing evidence packets that support audit, compliance review, executive oversight, incident review, and future replay.

---

## Decision Model

```text
ADMIT       Evidence packet is complete and replay-ready.
HOLD        Evidence is incomplete but recoverable.
REVALIDATE  Prior packet is stale because system conditions changed.
REFUSE      Evidence is missing a critical proof boundary.
```

---

## Enterprise Architecture Flow

```text
Governance decision made
        ↓
Evidence packet assembled
        ↓
Owner, decision, reason, and control records checked
        ↓
Replay readiness evaluated
        ↓
ADMIT / HOLD / REFUSE / REVALIDATE
        ↓
Audit packet preserved
        ↓
Future review can reconstruct decision
```

---

## End-to-End Coverage

| Layer | Enterprise Question | Repository Asset |
|---|---|---|
| Evidence model | What must be preserved? | `docs/audit-evidence-model.md` |
| Replay readiness | Can the decision be reconstructed later? | `docs/replay-readiness-model.md` |
| Evidence template | What does a reusable packet look like? | `docs/evidence-packet-template.md` |
| Production readiness | What must be true before production adaptation? | `docs/production-readiness-checklist.md` |
| Deployment | How can this be used at local, workshop, pilot, or enterprise level? | `docs/deployment-modes.md` |
| Sandbox | Can packet scenarios be executed locally? | `sandbox/runner.py` |
| Sample output | What do the sample packet results look like? | `sandbox/outputs/sample-sandbox-results.json` |
| Tests | Does the engine enforce expected outcomes? | `tests/test_audit_evidence_pack.py` |
| Scorecard | How complete is the evidence packet? | `docs/audit-evidence-scorecard.md` |
| Report | What does enterprise output look like? | `reports/sample-audit-evidence-readiness-report.md` |

---

## Public-Safe Components

| Asset | Purpose |
|---|---|
| `src/elyria_audit_evidence_pack/engine.py` | Public-safe evidence packet decision engine. |
| `src/elyria_audit_evidence_pack/schema.py` | Evidence schema helpers and decision constants. |
| `examples/*.json` | Public-safe evidence packet scenarios. |
| `sandbox/runner.py` | Executable sandbox runner. |
| `sandbox/outputs/sample-sandbox-results.json` | Pre-generated public-safe sandbox output. |
| `docs/why-and-how.md` | Why this exists and how the pack works. |
| `docs/audit-evidence-model.md` | Core evidence model. |
| `docs/replay-readiness-model.md` | Replay readiness model. |
| `docs/evidence-packet-template.md` | Buyer-facing evidence packet template. |
| `docs/production-readiness-checklist.md` | Production-candidate requirements. |
| `docs/deployment-modes.md` | Local, workshop, pilot, enterprise, and production-adaptation modes. |
| `docs/architecture-diagram.md` | Mermaid architecture diagram. |
| `docs/audit-evidence-scorecard.md` | Buyer-facing audit evidence scorecard. |
| `docs/executive-demo-script.md` | 10-minute buyer or hiring-panel demo path. |
| `docs/design-language.md` | Visual identity, palette, badges, and language rules. |
| `docs/visual-index.md` | Executive scan path and visual decision system. |
| `reports/sample-audit-evidence-readiness-report.md` | Enterprise-style sample report. |
| `tests/test_audit_evidence_pack.py` | Executable public-safe engine tests. |
| `tests/expected-audit-evidence-outcomes.md` | Expected public-safe outcomes. |
| `.github/workflows/validate.yml` | GitHub Actions validation workflow. |
| `pyproject.toml` | Python project metadata. |
| `requirements.txt` | Local validation dependency list. |
| `LICENSE.md` | MIT license. |
| `SECURITY.md` | Public-safe security policy. |
| `CONTRIBUTING.md` | Public-safe contribution rules. |
| `NOTICE.md` | Public boundary and attribution notice. |

---

## Relationship to the Elyria Enterprise AI Governance Suite

```text
Elyria Enterprise AI Control Plane
= governs enterprise AI movement across the organization.

Elyria Agent Action Boundary
= governs tool-using agents that may touch systems, data, workflows, communications, or operational action.

Elyria RAG Source Authority Gate
= governs retrieval trust: what knowledge AI may retrieve, trust, cite, and use.

Elyria AI Revalidation Engine
= governs when prior approval becomes stale after change.

Elyria AI Audit Evidence Pack
= proves governance happened and preserves replayable evidence.
```

This repository is the evidence-and-proof layer of the suite.

---

## Public Boundary

This repository is public-safe. It demonstrates architecture surfaces, sandbox logic, examples, tests, and enterprise readiness models, not private Elyria Systems runtime machinery, protected validators, customer-specific builds, commercial proof-corridor internals, credentials, keys, or confidential implementation details.

**Show the architecture. Protect the machinery.**
