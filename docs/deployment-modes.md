# Deployment Modes

## Purpose

This repository supports multiple levels of audit evidence adoption without exposing private runtime machinery.

---

## Mode 1 — Local Review

```text
Goal: understand evidence packet structure and decision logic.
```

Use:

- `README.md`
- `docs/why-and-how.md`
- `docs/audit-evidence-model.md`
- `examples/*.json`

---

## Mode 2 — Workshop

```text
Goal: map what evidence the enterprise must preserve for AI governance decisions.
```

Use:

- `docs/evidence-packet-template.md`
- `docs/replay-readiness-model.md`
- `docs/audit-evidence-scorecard.md`

---

## Mode 3 — Pilot Sandbox

```text
Goal: evaluate public-safe packet scenarios through ADMIT / HOLD / REFUSE / REVALIDATE.
```

Use:

- `src/elyria_audit_evidence_pack/engine.py`
- `examples/*.json`
- `sandbox/runner.py`
- `sandbox/outputs/sample-sandbox-results.json`

---

## Mode 4 — Enterprise Adaptation

Typical integration points:

- evidence store
- audit log
- model registry
- source registry
- approval workflow
- issue management
- identity and access management
- compliance reporting
- incident response

---

## Mode 5 — Production-Candidate Control

Required additions:

- durable storage
- retention policy
- access controls
- tamper resistance
- packet signing or integrity checks
- retrieval and reporting process
- incident review workflow
- legal/compliance approval

---

## Boundary

This public repository is a reference architecture and pilot sandbox. It is not a complete production enforcement system by itself.
