# Deployment Runbook

- Upload `hf-space/index.html` to the Space.
- Host payment and entitlement verification separately; no secrets in the Space.
- Produce release SHA-256, SBOM, signed metadata, and reproducible build records where practical.
- Configure the backend to authorize only the exact release digest.
- Test payment confirmation, replay protection, same-wallet signature binding, expiry, revocation, and offline-safe installer behavior in disposable VMs.
- Obtain independent security, legal, tax, privacy, and refund review before accepting payment.
