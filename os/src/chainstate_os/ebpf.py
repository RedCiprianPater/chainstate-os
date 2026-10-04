"""eBPF integration boundary for CHAINSTATE OS.

The Python runtime does not load eBPF itself. A separate privileged loader is
responsible for kernel interaction. This module validates the policy boundary
and consumes JSONL telemetry from that helper.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Iterable, Iterator


@dataclass(frozen=True)
class EBPFEvent:
    ts_ns: int
    pid: int
    uid: int
    type: int
    syscall_id: int = 0
    old_state: int = 0
    new_state: int = 0
    comm: str = ""


def parse_event(line: str) -> EBPFEvent:
    data = json.loads(line)
    required = ("ts_ns", "pid", "uid", "type")
    if any(k not in data for k in required):
        raise ValueError("invalid eBPF event")
    return EBPFEvent(
        ts_ns=int(data["ts_ns"]),
        pid=int(data["pid"]),
        uid=int(data["uid"]),
        type=int(data["type"]),
        syscall_id=int(data.get("syscall_id", 0)),
        old_state=int(data.get("old_state", 0)),
        new_state=int(data.get("new_state", 0)),
        comm=str(data.get("comm", ""))[:16],
    )


def parse_events(lines: Iterable[str]) -> Iterator[EBPFEvent]:
    for line in lines:
        if line.strip():
            yield parse_event(line)


def runtime_policy() -> dict[str, object]:
    """Return the non-negotiable runtime boundary for eBPF."""
    return {
        "mode": "monitor-only",
        "ai_can_load_bpf": False,
        "ai_can_change_policy": False,
        "runtime_compilation": False,
        "unsigned_objects": False,
        "enforcement_default": False,
    }
