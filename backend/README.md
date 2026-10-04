# CHAINSTATE OS Payment & Authorization Backend

Security-first reference backend for:

1. Creating a short-lived ETH checkout quote.
2. Verifying a payment server-side.
3. Issuing a wallet-bound entitlement.
4. Issuing a nonce-bound installation challenge.
5. Authorizing installation only after verifying the same wallet signature and exact release digest.

> **Important:** This backend is intentionally fail-closed. It does not accept real funds until a production blockchain verifier, persistent database, monitoring, legal review, and independent security review are configured. The default endpoints return `503` for payment verification.

## Structure

```text
backend/
├── .env.example
├── Dockerfile
├── README.md
├── requirements.txt
├── pyproject.toml
├── config/
│   └── policy.example.yaml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── schemas.py
│   ├── security.py
│   ├── storage.py
│   ├── blockchain.py
│   └── routes.py
└── tests/
    └── test_security.py
```

## Local setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000/docs` only for local development.

## Required production work

- Set a real RPC provider and chain allowlist.
- Configure the exact recipient address through a secret manager.
- Use a production database with unique constraints and encrypted backups.
- Implement and independently test the blockchain verifier.
- Require sufficient confirmations and protect against reorgs.
- Pin bundle SHA-256 digests and signed release metadata.
- Use HTTPS, reverse-proxy rate limiting, structured audit logs, alerting, backups, and key rotation.
- Never collect seed phrases or private keys.
- Never trust frontend-reported payment status.
- Run a legal review before charging users or distributing executable software.
