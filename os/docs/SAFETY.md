# Safety and Security Baseline

1. **Default deny:** unknown capabilities are blocked.
2. **Kill gate:** a local kill-gate file blocks actions immediately.
3. **Human approval:** restricted actions require explicit approval.
4. **Dry run:** runtime actions produce no external side effects by default.
5. **Isolation:** inference, planning, metacognition, and execution should run in separate trust domains in production.
6. **Provenance:** every authorization and block must be logged.
7. **No secret handling:** this layer must never request seed phrases, private keys, or credentials.
8. **Hardware:** sensor reads and actuation must be separate; actuation requires an independent safety case.
9. **Rollback:** production deployments require signed artifacts, SBOMs, and tested rollback.
10. **Evaluation:** measure false approvals, blocked unsafe actions, policy failures, audit completeness, and recovery time.
