# 🐧 CHAINSTATE AGI OS Layer

This directory is a **safe reference runtime scaffold**, not a bootable operating-system kernel. It defines the user-space control plane for a future CHAINSTATE distribution.

## Included capabilities

- Local-first runtime configuration
- Observe → represent → hypothesise → challenge → authorize → execute → reflect lifecycle
- Default-deny capability policy
- Independent kill gate and emergency stop file
- Metacognition isolation boundary
- Append-only JSONL audit events
- Dry-run execution by default
- Branch/experiment metadata with explicit commit authorization
- Hardware adapter interfaces without direct actuation
- Health and safety metrics hooks
- CLI for status, policy check, dry-run, and kill-gate control

## Status

| Area | State |
|---|---|
| Reference runtime | Implemented scaffold |
| Real kernel / distro | Not implemented here |
| LLM inference | Adapter interface only |
| Voice / GUI | Outside this directory |
| Hardware actuation | Disabled by default |
| Temporal branch engine | Metadata interface only |
| Production security | Requires independent review |

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m chainstate_os.cli status
python -m chainstate_os.cli dry-run --action read_system_info
pytest
```

Never enable privileged actions or connect physical actuators without a separate safety case, sandbox, and human approval workflow.
