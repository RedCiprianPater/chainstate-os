from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Quote:
    quote_id: str
    chain_id: int
    recipient: str
    amount_wei: str
    expires_at: datetime


@dataclass(frozen=True)
class InstallChallenge:
    challenge_id: str
    wallet: str
    nonce: str
    bundle_sha256: str
    expires_at: datetime
