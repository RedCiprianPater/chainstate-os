# Payment and Wallet-Binding Protocol

The browser is not an authority. The backend must independently verify:

1. Exact chain ID, recipient, native ETH value in wei, status, and confirmations.
2. Quote expiry and replay protection for quote IDs and transaction hashes.
3. Entitlement binding to the wallet that paid.
4. Exact release/bundle SHA-256 digest and expiry.
5. A nonce-bound install challenge containing wallet, entitlement, bundle hash, origin, and expiry.
6. The signature recovered from the challenge equals the paying wallet.

Recommended endpoints (illustrative):

- `POST /v1/checkout/quote` → `{quoteId, chainId, recipient, weiAmount, usdCents, expiresAt}`
- `POST /v1/checkout/claim` → validates `txHash`, returns entitlement
- `POST /v1/install/challenge` → returns EIP-712 typed data or readable challenge
- `POST /v1/install/authorize` → verifies signature and returns short-lived install token

Use EIP-712 typed data for structured signing where supported. Never ask for seed phrases or private keys. Installation must fail closed if the backend is unavailable, entitlement is expired, bundle hash differs, or signer does not match the paying wallet.
