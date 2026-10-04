import hashlib
import hmac
import secrets
from datetime import datetime, timezone


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def random_token(prefix: str) -> str:
    return f"{prefix}_{secrets.token_urlsafe(32)}"


def sha256_hex(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def constant_time_equal(left: str, right: str) -> bool:
    return hmac.compare_digest(left.encode(), right.encode())


def normalize_wallet(wallet: str) -> str:
    return wallet.lower()
