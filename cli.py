# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 AlgoVoi (chopmob-cloud). Apache-2.0.
"""Compute task_ref from card_ref, instructions_hash and created_at_ms.

Usage:
  python cli.py <card_ref> <instructions_hash> <created_at_ms>
"""
import sys
from task_ref import task_ref

def main():
    if len(sys.argv) != 4:
        print("usage: python cli.py <card_ref> <instructions_hash> <created_at_ms>", file=sys.stderr)
        sys.exit(1)
    print(task_ref(sys.argv[1], sys.argv[2], int(sys.argv[3])))

if __name__ == "__main__":
    main()
