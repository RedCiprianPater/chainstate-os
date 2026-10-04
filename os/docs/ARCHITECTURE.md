# OS Architecture

- Interface plane: CLI, GUI, voice, and API adapters.
- Observation plane: local sensors and system telemetry.
- Representation plane: typed state, provenance, and uncertainty.
- Cognitive plane: planning, tool selection, and hypothesis generation.
- Metacognitive plane: critique, contradiction checks, and confidence limits.
- Constitutional plane: policy, permissions, kill gate, and human approval.
- Execution plane: sandboxed, reversible operations.
- Continuity plane: branch metadata, checkpoints, audit history, and rollback.
- Hardware plane: read-only adapters unless separately authorized.

The invariant is: perception is not intent; intent is not authorization; authorization is not execution.
