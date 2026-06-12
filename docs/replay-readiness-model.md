# Replay Readiness Model

## Purpose

Replay readiness determines whether a future reviewer can reconstruct the governance decision from preserved evidence.

---

## Replay Questions

1. What system was governed?
2. What decision was made?
3. When was the decision made?
4. Who owned the decision?
5. Which governance owner was accountable?
6. What reason codes applied?
7. What controls were checked?
8. What evidence supported the decision?
9. Did the system change after the packet was created?
10. Can the decision be reconstructed without relying on memory?

---

## Replay States

| State | Meaning | Decision Guidance |
|---|---|---|
| Replay-ready | Packet can be reconstructed from evidence. | ADMIT |
| Evidence incomplete | Some fields are missing but recoverable. | HOLD |
| Critical proof missing | The decision cannot be proven. | REFUSE |
| Stale packet | System changed after packet creation. | REVALIDATE |

---

## Replay Rule

```text
A packet is replay-ready only when a future reviewer can reconstruct decision, ownership, evidence, controls, and outcome without relying on informal memory.
```
