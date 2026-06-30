# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 AlgoVoi (chopmob-cloud). Open A2A primitive, Apache-2.0.
"""task_ref: a deterministic, content addressed reference to an A2A Task delegation.

task_ref = "sha256:" + SHA-256(JCS({card_ref, instructions_hash, created_at_ms}))

Recomputes offline with only RFC 8785 (JCS) and SHA-256.

Fields
------
card_ref          sha256: reference to the assigned agent's AgentCard (card_ref_v1)
instructions_hash sha256: SHA-256 of the raw task instructions bytes
created_at_ms     integer milliseconds since Unix epoch (must be > 0)
"""
import hashlib
from algovoi_substrate import canonicalize

TASK_REF_VERSION = "task_ref_v1"
_REQUIRED = {"card_ref", "instructions_hash", "created_at_ms"}
_SHA_FIELDS = {"card_ref", "instructions_hash"}


def task_ref(card_ref: str, instructions_hash: str, created_at_ms: int) -> str:
    for name, val in (("card_ref", card_ref), ("instructions_hash", instructions_hash)):
        if not isinstance(val, str) or not val.startswith("sha256:"):
            raise ValueError(f"{name} must be a sha256: string")
    if not isinstance(created_at_ms, int) or created_at_ms <= 0:
        raise ValueError("created_at_ms must be a positive integer")
    payload = {
        "card_ref": card_ref,
        "created_at_ms": created_at_ms,
        "instructions_hash": instructions_hash,
    }
    return "sha256:" + hashlib.sha256(canonicalize(payload).encode("utf-8")).hexdigest()
