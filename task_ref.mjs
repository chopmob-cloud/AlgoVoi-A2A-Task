// SPDX-License-Identifier: Apache-2.0
// Copyright (c) 2026 AlgoVoi (chopmob-cloud). Open A2A primitive, Apache-2.0.
// task_ref = "sha256:" + SHA-256(JCS({card_ref, instructions_hash, created_at_ms}))
// Recomputes offline with only RFC 8785 (JCS) and SHA-256.
import { createHash } from "node:crypto";
import { canonicalize } from "@algovoi/substrate";

const ARTIFACT_TYPES = new Set(["TEXT", "FILE", "DATA", "ERROR"]);

export function taskRef(cardRef, instructionsHash, createdAtMs) {
  for (const [name, val] of [["cardRef", cardRef], ["instructionsHash", instructionsHash]]) {
    if (typeof val !== "string" || !val.startsWith("sha256:"))
      throw new TypeError(`${name} must be a sha256: string`);
  }
  if (!Number.isInteger(createdAtMs) || createdAtMs <= 0)
    throw new TypeError("createdAtMs must be a positive integer");
  const payload = {
    card_ref: cardRef,
    created_at_ms: createdAtMs,
    instructions_hash: instructionsHash,
  };
  return "sha256:" + createHash("sha256").update(Buffer.from(canonicalize(payload), "utf-8")).digest("hex");
}
