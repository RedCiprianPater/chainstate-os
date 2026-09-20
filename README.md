# 🐧 CHAINSTATE AGI Linux OS

> A proposed local-first, safety-oriented cognitive operating system architecture for sovereign AI, temporal state management, multimodal interaction, hardware integration, and verifiable execution.

[![Status: Research Prototype](https://img.shields.io/badge/status-research--prototype-black.svg)](https://github.com/RedCiprianPater/chainstate-os)
[![Demo: Hugging Face](https://img.shields.io/badge/demo-Hugging%20Face-orange.svg)](https://huggingface.co/spaces/CPater/chainstate-os/)
[![Platform: Linux](https://img.shields.io/badge/platform-Linux-black.svg)](https://www.kernel.org/)
[![Architecture: Local First](https://img.shields.io/badge/architecture-local--first-white.svg)](#design-principles)

**Project:** [GitHub repository](https://github.com/RedCiprianPater/chainstate-os)  
**Interactive demo:** [Hugging Face Space](https://huggingface.co/spaces/CPater/chainstate-os/)  
**Static demo URL:** `https://cpater-chainstate-os.static.hf.space/index.html` *(available only after successful Space deployment)*

---

## ⚠️ Project Status and Scope

CHAINSTATE AGI Linux OS is currently a **research and engineering framework**, not a completed or independently validated AGI operating system. Several components are architectural proposals, simulations, or integration plans.

| Classification | Meaning |
|---|---|
| **Implemented** | Present in this repository and runnable as documented. |
| **Prototype** | Partial implementation or demonstration code. |
| **Proposed** | Design specification requiring implementation and testing. |
| **Simulated** | Demonstration telemetry or behavior that is not connected to production hardware or an autonomous AGI. |
| **Unverified** | Requires independent testing, security review, reproducibility checks, or scientific validation. |

The current public demo is primarily a **visual and architectural demonstration**. It must not be interpreted as evidence that AGI, omniscience, time travel, autonomous robotics, or quantum computing capabilities have been achieved.

## ✦ Vision

CHAINSTATE is designed around a separation between:

1. **Perception** — collecting observations from approved sources.
2. **Representation** — encoding observations into structured state.
3. **Hypothesis** — generating candidate interpretations or plans.
4. **Challenge** — testing uncertainty, contradictions, and failure modes.
5. **Authorization** — applying policy, capability, and human-approval gates.
6. **Execution** — performing only authorized actions.
7. **Reflection** — recording outcomes, provenance, and lessons.

The system is intended to support local sovereignty, explicit authorization, reversible actions, inspectable reasoning artifacts, and independent safety controls.

## 🧭 Core Design Principles

- **Local-first operation:** Prefer local processing and local state storage where practical.
- **Offline tolerance:** Core interfaces should remain useful without continuous network access.
- **Explicit authority boundaries:** Perception, intent, authorization, and execution are separate stages.
- **Fail closed:** Missing credentials, unclear policy, invalid signatures, or uncertain authorization must stop the action.
- **Human control:** High-impact operations require explicit user approval.
- **Reversibility:** Prefer preview, simulation, dry-run, rollback, and transaction logs.
- **Provenance:** Track source, timestamp, model/version, policy decision, and output digest.
- **Metacognitive isolation:** The system's internal monitoring state must not silently control or alter the user's local operating-system state.
- **Hardware independence:** Hardware acceleration is optional and must not be treated as authority.
- **Falsifiability:** Claims and experimental results should define measurable tests and failure conditions.

---

## 🧩 System Architecture

CHAINSTATE is organized as layered trust planes rather than one unrestricted agent process.

```text
┌──────────────────────────────────────────────────────────┐
│ User Interface Plane                                    │
│ Desktop · CLI · Voice · Accessibility · Web Console     │
├──────────────────────────────────────────────────────────┤
│ Skill and Plugin Plane                                   │
│ Sandboxed tools · Capability manifests · Permissions     │
├──────────────────────────────────────────────────────────┤
│ Cognitive Plane                                          │
│ Planning · Retrieval · Tool selection · Multimodal I/O   │
├──────────────────────────────────────────────────────────┤
│ Metacognitive Plane                                      │
│ Uncertainty · Self-checks · Contradiction detection      │
├──────────────────────────────────────────────────────────┤
│ Constitutional / Safety Plane                            │
│ Policy-as-code · Kill gate · Human approval · Audit      │
├──────────────────────────────────────────────────────────┤
│ Execution Plane                                          │
│ Sandboxed processes · Filesystem · Network · Devices     │
├──────────────────────────────────────────────────────────┤
│ Continuity Plane                                         │
│ State snapshots · BranchState · Provenance · Rollback    │
├──────────────────────────────────────────────────────────┤
│ Hardware Plane                                           │
│ CPU/GPU/NPU · RISC-V SoC · Sensors · Optional devices    │
└──────────────────────────────────────────────────────────┘
```

### Trust invariants

```text
perception ≠ intent
intent ≠ authorization
authorization ≠ execution
representation ≠ authority
hardware acceleration ≠ permission
model confidence ≠ truth
network availability ≠ trust
```

## 🖥️ Operating System Features

### Desktop and CLI

- Linux-based desktop integration concept.
- Command-line assistant and structured command execution.
- Voice interaction layer with explicit activation and permissions.
- System status dashboard for CPU, memory, latency, state, and safety events.
- Accessibility-friendly text-first workflows.
- Local configuration and policy inspection.
- Dry-run mode for commands and workflows.
- Session receipts and execution history.

### Cognitive and AI Services

- Local and remote model routing.
- Retrieval-augmented workflows with source tracking.
- Task decomposition and plan generation.
- Tool discovery through declared skill manifests.
- Context and memory management.
- Multimodal input abstraction.
- Structured outputs and schema validation.
- Confidence and uncertainty annotations.
- Contradiction and consistency checks.
- Human review checkpoints for consequential outputs.

### Metacognition and Continuity

- BranchState-inspired state branching and comparison.
- Snapshot-based continuity and rollback concepts.
- Temporal state indexing and event timelines.
- Hypothesis tracking and falsification records.
- Model/version provenance.
- Separation of user workspace state from internal metacognitive state.
- State integrity checks and tamper-evident event records.
- Optional external anchoring for audit evidence, subject to privacy review.

### Skills and Plugins

Each skill should declare:

- Name, version, owner, and source.
- Input and output schemas.
- Required capabilities.
- Network and filesystem access.
- Data classification.
- Human approval requirements.
- Rollback or compensation behavior.
- Logging and provenance requirements.

Example capability classes:

```text
filesystem.read
filesystem.write
network.request
process.spawn
device.observe
device.control
credential.use
payment.request
```

Capability grants should be narrow, time-limited where possible, auditable, and denied by default.

---

## 🛡️ Safety and Security Model

Safety is treated as a system property requiring independent controls, not as a claim made by a language model.

### Safety gates

1. **Input gate** — validate source, format, scope, and trust level.
2. **Intent gate** — identify requested action and ambiguity.
3. **Policy gate** — compare action against explicit policy.
4. **Capability gate** — verify the process has the required permission.
5. **Human approval gate** — request approval for high-impact operations.
6. **Execution gate** — run in a constrained environment.
7. **Postcondition gate** — verify the result and detect unexpected changes.
8. **Kill gate** — provide an independent stop mechanism.

### Protected actions

The following should be disabled or separately safety-cased by default:

- Autonomous physical actuation.
- Weapon targeting or harmful physical control.
- Unrestricted shell execution.
- Destructive filesystem operations.
- Credential extraction or secret handling.
- Unbounded network scanning.
- Autonomous financial transfers.
- Self-modification that bypasses policy or review.

Robotics and hardware controls should use explicit device allowlists, rate limits, emergency stop mechanisms, human approval, and a separate validation process.

### Security controls

- Signed release artifacts.
- SHA-256 or stronger artifact digests.
- Software bill of materials (SBOM).
- Reproducible or independently rebuildable releases where feasible.
- Dependency pinning and vulnerability scanning.
- Secret scanning and push protection.
- Secure boot/TPM integration where hardware supports it.
- Sandboxing and least-privilege service accounts.
- Audit logs with integrity protection.
- Backup, rollback, and recovery procedures.
- Privacy-preserving telemetry defaults.
- No private keys or seed phrases requested from users.

GitHub recommends repository security controls such as dependency alerts, secret scanning, push protection, code scanning, and a security policy; these should be enabled as the implementation matures.

## 📊 Safety Metrics and Evaluation Plan

The metrics below are **proposed evaluation targets**, not measured production results.

| Metric | Definition | Evaluation approach |
|---|---|---|
| Authorization precision | Fraction of executed actions that were authorized | Compare execution logs against policy decisions |
| Unauthorized execution rate | Actions executed without valid authorization | Adversarial and regression testing |
| Kill-gate latency | Time from stop signal to execution halt | Controlled benchmark with instrumented processes |
| Policy bypass rate | Attempts that evade or circumvent policy | Red-team test suite |
| Rollback success | Percentage of reversible tests restored correctly | Snapshot and fault-injection tests |
| Provenance completeness | Required events containing valid source metadata | Log schema validation |
| Sandbox escape rate | Successful escapes from constrained execution | Isolation and penetration testing |
| False refusal rate | Safe, authorized actions incorrectly blocked | Curated task benchmark |
| Offline availability | Functions available without network access | Network-disconnect test matrix |
| Recovery time | Time to restore from a corrupted or failed state | Disaster-recovery drills |
| Privacy leakage | Sensitive values emitted to logs or remote services | DLP and redaction tests |
| Reproducibility | Agreement between repeated builds/runs | Deterministic build and replay checks |

No metric should be reported as passed without publishing the test setup, dataset or scenario set, version identifiers, limitations, and raw or reproducible evidence.

## 💳 Payment and Installation Authorization

The proposed distribution model includes a **one-time price of USD 666**, settled in ETH through a wallet such as MetaMask. The payment workflow is a reference design and must not be activated for real funds until it has undergone legal, security, and operational review.

Recommended flow:

```text
HF Space checkout UI
        ↓
Backend creates time-limited quote
        ↓
Wallet submits ETH transaction
        ↓
Backend verifies chain, recipient, value, status, confirmations
        ↓
Entitlement bound to paying wallet + bundle digest
        ↓
Installer requests nonce-bound challenge
        ↓
Same wallet signs structured authorization
        ↓
Backend verifies recovered signer and entitlement
        ↓
Installer may proceed only after authorization
```

Requirements:

- Never request a seed phrase or private key.
- Verify the transaction on the backend, not only in the browser.
- Validate chain ID, recipient address, exact value in wei, confirmations, quote expiry, and replay protection.
- Bind entitlement to the paying wallet and exact release digest.
- Use a nonce-bound installation challenge.
- Verify the recovered signature address matches the entitled wallet.
- Fail closed when any verification step is missing or ambiguous.
- Provide refund, support, tax, and jurisdictional terms before accepting payment.

See [`docs/PAYMENT_PROTOCOL.md`](docs/PAYMENT_PROTOCOL.md) for the current reference protocol.

## 🧱 Technology Stack

| Layer | Proposed or current technology |
|---|---|
| Base OS | Linux; distribution and kernel profile to be selected |
| User interface | HTML/CSS/JavaScript demo; future desktop shell |
| CLI | POSIX shell and future typed command service |
| AI runtime | Local model runtime plus optional remote providers |
| Plugin execution | Sandboxed processes and capability manifests |
| State | Versioned local state store, snapshots, and event logs |
| Backend | API service for entitlement, payment verification, and authorization |
| Payments | Ethereum-compatible wallet flow; backend verification required |
| Hardware | x86-64, ARM, RISC-V, and optional accelerators where supported |
| Deployment | GitHub releases, Hugging Face Space, optional server deployment |
| Integrity | SHA-256 digests, signatures, SBOM, provenance metadata |
| Testing | Unit, integration, policy, fault-injection, security, and replay tests |

The stack is intentionally modular. A listed technology is not evidence that the corresponding production implementation is complete.

## 🔬 Research and Experimental Modules

The broader CHAINSTATE research direction includes exploratory concepts involving:

- Temporal branching and continuity.
- RISC-V SoC and hardware integration.
- Unified cognitive interfaces.
- Spatial and hyperspectral sensory representations.
- Robotics interfaces with external-control isolation.
- Quantum-compute and edge simulation concepts.
- Planetary, cyberspace, and large-scale simulation models.
- Provenance, content authenticity, and synthetic-media labeling.
- Emoji/Unicode machine-code representations and defensive parsing.
- Neuromarketing simulation and falsification-oriented modeling.

These modules should be treated as research hypotheses or design references unless a specific implementation, benchmark, and independent validation record is provided.

## 📁 Repository Structure

```text
chainstate-os/
├── README.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── PAYMENT_PROTOCOL.md
│   └── RUNBOOK.md
├── hf-space/
│   ├── README.md
│   └── index.html
├── installer/
│   └── install-chainstate.sh
├── scripts/
│   └── verify-bundle.sh
├── backend/                 # planned payment/authorization service
├── os/                      # planned OS implementation
├── tests/                   # planned test suites
├── .github/
│   └── workflows/           # planned CI and security checks
└── SHA256SUMS
```

## 🚀 Quick Start: Repository Scaffold

Clone the repository:

```bash
git clone https://github.com/RedCiprianPater/chainstate-os.git
cd chainstate-os
```

Run the scaffold verification script:

```bash
bash scripts/verify-bundle.sh
```

Review the architecture and security model:

```bash
less docs/ARCHITECTURE.md
less docs/PAYMENT_PROTOCOL.md
less docs/RUNBOOK.md
```

### Run the static demo locally

```bash
cd hf-space
python3 -m http.server 7860
```

Open:

```text
http://localhost:7860/index.html
```

The dashboard telemetry is simulated unless a separately documented backend is connected.

## 🧪 Testing Strategy

Planned test categories:

- **Unit tests:** parsers, schemas, policy evaluation, state transitions.
- **Integration tests:** UI, backend, installer, entitlement, and release metadata.
- **Security tests:** dependency scanning, secret scanning, sandboxing, authorization bypass attempts.
- **Fault injection:** network loss, corrupted state, invalid signatures, expired quotes, interrupted installation.
- **Replay tests:** duplicate transaction claims, repeated installation challenges, stale nonces.
- **Privacy tests:** secret redaction, telemetry minimization, local-only mode.
- **Hardware tests:** device allowlists, rate limits, emergency stop, and simulated actuation.
- **Reproducibility tests:** clean environment builds and artifact digest comparison.

## 🗺️ Roadmap

- [x] Initial architecture and trust-plane documentation.
- [x] Static Hugging Face demo scaffold.
- [x] Reference payment and installation authorization protocol.
- [x] Installer fail-closed authorization scaffold.
- [ ] Implement a production backend with server-side blockchain verification.
- [ ] Implement signed release bundles and reproducible build pipeline.
- [ ] Add SBOM generation and dependency security automation.
- [ ] Build a minimal Linux service supervisor and policy engine.
- [ ] Add sandboxed skill execution.
- [ ] Add local model routing and offline-first state management.
- [ ] Implement formal policy and authorization test suites.
- [ ] Validate hardware integrations in controlled environments.
- [ ] Conduct independent security, safety, privacy, and legal reviews.

## 🤝 Contribution Guidelines

Contributions should include:

1. A clear problem statement.
2. A threat model or safety impact assessment when relevant.
3. Tests or reproducible validation steps.
4. Documentation updates.
5. Explicit identification of proposed, implemented, simulated, and unverified behavior.
6. No secrets, private keys, seed phrases, personal data, or unlicensed third-party material.

Suggested workflow:

```bash
git checkout -b feature/your-change
# make changes and add tests
git diff
# open a pull request with evidence and limitations
```

## 🔐 Responsible Disclosure

Do not publicly publish an exploitable vulnerability with operational details before giving maintainers an opportunity to investigate. Include affected versions, reproduction steps, impact, and a proposed mitigation where possible. A dedicated `SECURITY.md` should be added before accepting security-sensitive contributions at scale.

## 📜 License and Research Use

A definitive license should be selected and committed before the project is presented as open source. Until then, users should not assume permission to redistribute, modify, or commercially deploy the repository contents.

Research claims should include source references, assumptions, experimental setup, limitations, and reproducible evidence. Architectural language such as “AGI,” “omniscience,” “time machine,” or “quantum” describes project themes and hypotheses; it does not establish that those capabilities are operational.

## 📬 Links

- [GitHub repository](https://github.com/RedCiprianPater/chainstate-os/tree/main)
- [Hugging Face demo](https://huggingface.co/spaces/CPater/chainstate-os/)
- [Static Space URL](https://cpater-chainstate-os.static.hf.space/index.html)

---

**CHAINSTATE AGI Linux OS** — local-first systems research, explicit authorization, verifiable state, and human-controlled execution. 🐧
