# CHAINSTATE OS eBPF Security & Observability Layer

This directory contains the CHAINSTATE OS eBPF integration. It is deliberately **fail-closed and monitor-first**.

## Design

- eBPF is an observation/enforcement boundary below the cognitive runtime.
- The AI runtime never generates arbitrary eBPF source or bytecode at runtime.
- Programs are built ahead of time, reviewed, pinned to a release, and loaded by a restricted helper.
- Linux's eBPF verifier remains a mandatory kernel safety boundary.
- The default profile is **telemetry-only**. No network or filesystem denial program is enabled by default.
- Any future enforcement program must have a separate policy, signed artifact, test suite, rollback procedure, and explicit operator enablement.
- CO-RE/libbpf is used so one compiled object can adapt to supported kernels through BTF.

## Programs

| Program | Hook | Default | Purpose |
|---|---|---:|---|
| `process_monitor.bpf.c` | `sched_process_exec` tracepoint | ON | Process execution provenance |
| `syscall_monitor.bpf.c` | `raw_syscalls/sys_enter` tracepoint | ON | Syscall telemetry with sampling |
| `network_monitor.bpf.c` | `sock/inet_sock_set_state` tracepoint | ON | Socket lifecycle telemetry |
| `filesystem_monitor.bpf.c` | `syscalls/sys_enter_openat` tracepoint | ON | File-open telemetry, path-free by default |
| `security_lsm.bpf.c` | LSM hook | OFF | Reserved for separately reviewed MAC policy |

## Safety rules

1. Never load unsigned/unapproved eBPF artifacts in production.
2. Never give the AI runtime `CAP_BPF`, `CAP_SYS_ADMIN`, or equivalent loader authority.
3. Keep the loader as a small, dedicated privileged component.
4. Use a dedicated service account, read-only BPF object directory, and restrictive filesystem permissions.
5. Do not log secrets, file contents, credentials, or raw user data from eBPF.
6. Treat eBPF telemetry as evidence, not as proof of intent or truth.
7. A missing BTF, incompatible kernel, failed verifier check, invalid digest, or policy mismatch must fail closed.
8. Keep physical actuation, payment, credential use, and destructive operations outside the eBPF layer and behind CHAINSTATE safety gates.

## Build

On a Linux build host with Clang/LLVM, libbpf development files, bpftool, and a kernel exposing BTF:

```bash
make -C os/ebpf
```

The build generates `include/vmlinux.h` from `/sys/kernel/btf/vmlinux` when available. Do not hand-edit generated BTF headers.

## Runtime

The reference loader is monitor-only unless an explicitly reviewed enforcement profile is selected. It should be installed as a dedicated system service rather than started by the AI process.

See:

- `os/ebpf/loader/README.md`
- `os/docs/EBPF_SECURITY.md`
- `os/policies/ebpf-default-deny.yaml`
