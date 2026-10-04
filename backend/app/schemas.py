from pydantic import BaseModel, Field


class QuoteRequest(BaseModel):
    wallet: str = Field(min_length=42, max_length=42, pattern=r"^0x[a-fA-F0-9]{40}$")


class QuoteResponse(BaseModel):
    quote_id: str
    chain_id: int
    asset: str
    recipient: str
    amount_wei: str
    price_usd: int
    expires_at: str
    live: bool


class ClaimRequest(BaseModel):
    quote_id: str = Field(min_length=8, max_length=128)
    tx_hash: str = Field(min_length=66, max_length=66, pattern=r"^0x[a-fA-F0-9]{64}$")
    wallet: str = Field(min_length=42, max_length=42, pattern=r"^0x[a-fA-F0-9]{40}$")


class ChallengeRequest(BaseModel):
    wallet: str = Field(min_length=42, max_length=42, pattern=r"^0x[a-fA-F0-9]{40}$")
    bundle_sha256: str = Field(min_length=64, max_length=64, pattern=r"^[a-fA-F0-9]{64}$")


class AuthorizeRequest(BaseModel):
    challenge_id: str = Field(min_length=8, max_length=128)
    wallet: str = Field(min_length=42, max_length=42, pattern=r"^0x[a-fA-F0-9]{40}$")
    signature: str = Field(min_length=2, max_length=2048)
