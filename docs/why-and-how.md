# Why and How

## Why This Exists

Enterprise AI governance cannot rely on memory, screenshots, or informal claims.

When an AI system is reviewed, admitted, held, refused, or revalidated, the organization needs evidence that can survive later audit, incident review, executive review, compliance review, or replay.

---

## Core Problem

```text
Governance that cannot be proven later is only an assertion.
```

A decision record must show what happened, why it happened, who owned it, what controls were checked, what evidence supported it, and whether the decision can be reconstructed later.

---

## How The Pack Works

The public-safe engine evaluates an evidence packet and checks:

1. Are critical proof fields present?
2. Are required evidence fields complete?
3. Did the governed system change after the decision?
4. Is replay readiness confirmed?
5. Can the packet support audit reliance?

---

## Decision Path

```text
Critical proof missing      -> REFUSE
System changed after packet -> REVALIDATE
Required evidence missing   -> HOLD
Replay not confirmed        -> HOLD
Packet complete             -> ADMIT
```

---

## Enterprise Use Pattern

1. Capture governance decision.
2. Assemble evidence packet.
3. Link packet to system, owner, decision, timestamp, reason codes, and controls.
4. Check replay readiness.
5. Preserve packet in an evidence store.
6. Use packet for audit, compliance, incident review, and future replay.
