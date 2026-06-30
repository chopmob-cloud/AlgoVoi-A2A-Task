# task_ref

A deterministic, content addressed reference to an A2A Task delegation.

    task_ref = "sha256:" + SHA-256(JCS({card_ref, instructions_hash, created_at_ms}))

Recomputes offline with only RFC 8785 (JCS) and SHA-256. No JWS, no JWKS, no key infrastructure.

## Why

A2A lets an agent accept a Task, but nothing makes the delegation tamper-evident. Change the
instructions after the fact and a consumer cannot tell. task_ref closes that gap: it is the
content address of exactly who was assigned and what they were asked to do.

Composing onto card_ref (AlgoVoi-A2A-Card): the card_ref field pins the exact AgentCard bytes
of the assigned agent, so a task_ref transitively binds agent identity to task instruction.

## Fields

| Field | Type | Description |
|---|---|---|
| `card_ref` | sha256: string | card_ref of the assigned agent (card_ref_v1) |
| `instructions_hash` | sha256: string | SHA-256 of the raw task instructions bytes |
| `created_at_ms` | integer | milliseconds since Unix epoch, must be > 0 |

## Construction

JCS (RFC 8785) sorts keys lexicographically before hashing, so the field order in the preimage
is always: `card_ref`, `created_at_ms`, `instructions_hash`.

## Use

Python:

    from task_ref import task_ref
    ref = task_ref(card_ref, instructions_hash, created_at_ms)

Node:

    import { taskRef } from "./task_ref.mjs";
    const ref = taskRef(cardRef, instructionsHash, createdAtMs);

CLI:

    python cli.py <card_ref> <instructions_hash> <created_at_ms>

## Conformance

Vectors live in the algovoi-jcs-conformance-vectors corpus, set task_ref_v1: positives,
invariants (field reorder does not change output), and negatives (changed card_ref, changed
instructions_hash, non-sha256 field, zero timestamp), verified byte for byte across independent
Python and Node runners.

## Composition

    card_ref  →  task_ref  →  artifact_ref

card_ref pins who the agent is. task_ref pins what they were asked to do. artifact_ref (AlgoVoi-A2A-Artifact)
pins what they produced. All three recompute offline from retained bytes.

## A2A Ecosystem

task_ref is published for the A2A ecosystem under the Apache 2.0 licence. Any A2A partner, implementer, or framework is free to adopt, implement, and build on it without asking permission. Retain the NOTICE file and licence header in derivative works, as required by Apache 2.0.

## License

Apache 2.0. Copyright (c) 2026 AlgoVoi (chopmob-cloud).
