# eBPF loader

`chainstate_ebpf_loader.c` is a deliberately small reference loader. It loads only the four monitor objects and never loads the reserved LSM enforcement object.

Production requirements before enabling any enforcement:

- signed BPF objects and trusted keyring policy;
- fixed release manifest with SHA-256 digests;
- kernel/BTF compatibility check;
- dedicated privileged service account;
- no AI-controlled loader credentials;
- systemd sandboxing and restricted filesystem access;
- integration tests in a disposable VM;
- rollback/disable procedure;
- independent security review.

The loader emits structured JSONL telemetry to stdout so a supervisor can ingest it into CHAINSTATE audit/provenance. It does not make policy decisions.
