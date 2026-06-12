# Visual Index

## Elyria AI Audit Evidence Pack

This index gives the repository a fast executive scan path.

---

## Control Signal

| Signal | Meaning |
|---|---|
| **Evidence Packet** | A structured record of a governance decision. |
| **Decision Record** | ADMIT / HOLD / REFUSE / REVALIDATE is preserved. |
| **Ownership** | Decision owner and governance owner are explicit. |
| **Reason Codes** | Rationale is structured and reviewable. |
| **Control Checks** | Controls evaluated before decision are recorded. |
| **Replay Readiness** | Future reviewer can reconstruct the decision. |
| **Proof Boundary** | Missing critical proof blocks audit reliance. |

---

## Repository Experience Path

```text
Executive signal
  ↓
Why and how
  ↓
Audit evidence model
  ↓
Evidence packet template
  ↓
Replay readiness model
  ↓
Decision engine
  ↓
Examples
  ↓
Sample sandbox output
  ↓
Readiness report
  ↓
Production checklist
```

---

## Decision Visuals

```text
ADMIT       Evidence packet is complete and replay-ready.
HOLD        Required evidence is incomplete but recoverable.
REVALIDATE  Packet is stale because system conditions changed.
REFUSE      Critical proof boundary is missing.
```

---

## Buyer Readiness Signal

The repository should communicate:

```text
This is not a log dump.
This is governance proof architecture.
This is replay-ready.
This is buyer-readable.
This is pilot-operable.
This is public-safe.
```
