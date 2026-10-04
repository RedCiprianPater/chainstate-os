from datetime import timedelta
from fastapi import APIRouter, HTTPException, Request

from .blockchain import verifier
from .config import settings
from .models import InstallChallenge, Quote
from .schemas import (AuthorizeRequest, ChallengeRequest, ClaimRequest, QuoteRequest,
                      QuoteResponse)
from .security import normalize_wallet, random_token, utc_now
from .storage import store

router = APIRouter()


def require_live_payments() -> None:
    if not settings.enable_live_payments:
        raise HTTPException(status_code=503, detail="Live payment verification is disabled")
    if not settings.payment_recipient_address or not settings.min_payment_wei:
        raise HTTPException(status_code=503, detail="Payment policy is incomplete")


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "live_payments": settings.enable_live_payments,
            "install_authorization": settings.enable_install_authorization}


@router.post("/v1/checkout/quote", response_model=QuoteResponse)
def create_quote(payload: QuoteRequest) -> QuoteResponse:
    require_live_payments()
    now = utc_now()
    quote = Quote(
        quote_id=random_token("quote"),
        chain_id=settings.payment_chain_id,
        recipient=settings.payment_recipient_address,
        amount_wei=settings.min_payment_wei,
        expires_at=now + timedelta(seconds=settings.quote_ttl_seconds),
    )
    store.quotes[quote.quote_id] = {"quote": quote, "wallet": normalize_wallet(payload.wallet)}
    return QuoteResponse(quote_id=quote.quote_id, chain_id=quote.chain_id,
                         asset=settings.payment_asset, recipient=quote.recipient,
                         amount_wei=quote.amount_wei, price_usd=settings.payment_price_usd,
                         expires_at=quote.expires_at.isoformat(), live=True)


@router.post("/v1/checkout/claim")
def claim_payment(payload: ClaimRequest) -> dict:
    require_live_payments()
    record = store.quotes.get(payload.quote_id)
    if not record or store.expired(record["quote"].expires_at):
        raise HTTPException(status_code=400, detail="Invalid or expired quote")
    if normalize_wallet(payload.wallet) != record["wallet"]:
        raise HTTPException(status_code=403, detail="Wallet does not match quote")
    tx_hash = payload.tx_hash.lower()
    if tx_hash in store.used_tx_hashes:
        raise HTTPException(status_code=409, detail="Transaction already claimed")
    valid = verifier.verify_native_eth_payment(
        tx_hash=tx_hash, expected_chain_id=record["quote"].chain_id,
        expected_recipient=record["quote"].recipient,
        expected_amount_wei=record["quote"].amount_wei, payer_wallet=record["wallet"],
        required_confirmations=settings.required_confirmations,
    )
    if not valid:
        raise HTTPException(status_code=402, detail="Payment could not be verified")
    store.used_tx_hashes.add(tx_hash)
    entitlement = random_token("ent")
    store.claims[entitlement] = {"wallet": record["wallet"], "tx_hash": tx_hash,
                                 "bundle_sha256": settings.allowed_bundle_sha256}
    return {"entitlement": entitlement, "wallet": record["wallet"]}


@router.post("/v1/install/challenge")
def install_challenge(payload: ChallengeRequest) -> dict:
    if not settings.enable_install_authorization:
        raise HTTPException(status_code=503, detail="Install authorization is disabled")
    if not settings.allowed_bundle_sha256 or payload.bundle_sha256.lower() != settings.allowed_bundle_sha256.lower():
        raise HTTPException(status_code=400, detail="Bundle digest is not approved")
    challenge = InstallChallenge(
        challenge_id=random_token("challenge"), wallet=normalize_wallet(payload.wallet),
        nonce=random_token("nonce"), bundle_sha256=payload.bundle_sha256.lower(),
        expires_at=utc_now() + timedelta(seconds=settings.install_challenge_ttl_seconds),
    )
    store.challenges[challenge.challenge_id] = challenge
    return {"challenge_id": challenge.challenge_id, "nonce": challenge.nonce,
            "wallet": challenge.wallet, "bundle_sha256": challenge.bundle_sha256,
            "expires_at": challenge.expires_at.isoformat()}


@router.post("/v1/install/authorize")
def authorize_install(payload: AuthorizeRequest) -> dict:
    if not settings.enable_install_authorization:
        raise HTTPException(status_code=503, detail="Install authorization is disabled")
    challenge = store.challenges.get(payload.challenge_id)
    if not challenge or store.expired(challenge.expires_at):
        raise HTTPException(status_code=400, detail="Invalid or expired challenge")
    if normalize_wallet(payload.wallet) != challenge.wallet:
        raise HTTPException(status_code=403, detail="Wallet mismatch")
    message = f"CHAINSTATE-INSTALL|{challenge.challenge_id}|{challenge.nonce}|{challenge.bundle_sha256}"
    if not verifier.recover_and_verify_signature(message=message, signature=payload.signature,
                                                 expected_wallet=challenge.wallet):
        raise HTTPException(status_code=403, detail="Signature verification failed")
    return {"authorized": True, "installToken": random_token("install")}
