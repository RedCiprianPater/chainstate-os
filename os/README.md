# 🐧 CHAINSTATE OS Runtime

Reference user-space runtime and Linux integration layer for CHAINSTATE. The runtime separates cognitive planning from authorization and kernel execution.

## eBPF integration

CHAINSTATE includes a monitor-first eBPF layer under `os/ebpf/` for process, sampled syscall, socket-state, and file-open telemetry. A reserved LSM-BPF hook is included for future, separately reviewed enforcement but is **disabled by default**.

The AI runtime cannot load or modify eBPF policy. The privileged loader is a separate boundary. See `docs/EBPF_SECURITY.md` and `policies/ebpf-default-deny.yaml`.

## Status

- Runtime architecture: reference implementation
- eBPF source: reference implementation; target-kernel build required
- eBPF enforcement: disabled by default
- Physical actuation: disabled by default
- Production security audit: not yet performed

Do not describe the eBPF layer as production-hardened until the target kernels, loader, signatures, integration tests, and independent review have been completed.
