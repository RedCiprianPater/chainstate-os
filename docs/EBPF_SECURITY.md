# CHAINSTATE OS eBPF Security Model

## Position in the trust architecture

eBPF sits below the cognitive and constitutional layers and close to the Linux kernel:

```text
Cognitive runtime
      |
Constitutional policy / authorization
      |
CHAINSTATE execution sandbox
      |
eBPF observation / narrowly reviewed enforcement
      |
Linux kernel verifier + LSM / cgroups / networking
      |
Hardware
```

The AI is not a kernel principal. It cannot generate, compile, load, unload, or replace eBPF programs.

## Default profile

The shipped profile is monitor-only. Process, sampled syscall, socket-state, and file-open events are telemetry. The reserved LSM program is not loaded.

This avoids creating a new kernel enforcement surface before it has its own security case.

## Why libbpf + CO-RE

The integration uses libbpf and BPF CO-RE. CO-RE uses kernel BTF to relocate type information at load time, improving portability across supported kernel versions. The build obtains `vmlinux.h` from `/sys/kernel/btf/vmlinux`.

## Admission controls

Before production enforcement is enabled, the loader must require:

1. approved release manifest;
2. SHA-256 digest match;
3. trusted signature/keyring policy;
4. kernel/BTF compatibility;
5. operator-selected policy profile;
6. successful test suite in the target kernel family;
7. explicit rollback path.

A missing or invalid requirement causes a fail-closed result.

## Privacy

Telemetry deliberately avoids reading file contents and does not capture network payloads. File path collection is disabled by default. Event retention should be minimized and governed by the same privacy policy as the rest of CHAINSTATE.

## Enforcement

LSM-BPF can implement MAC/audit policies, but CHAINSTATE should not enable an LSM policy merely because a model proposes one. Any enforcement program must be independently reviewed, signed, tested, versioned, and explicitly enabled by an administrator.

## Physical and high-impact actions

eBPF is not an authorization substitute for physical actuation, payment, credential use, destructive operations, or other high-impact actions. Those remain behind CHAINSTATE capability and human-approval gates.
