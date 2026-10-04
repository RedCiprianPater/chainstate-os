from datetime import datetime
from typing import Any


class MemoryStore:
    """Development-only store. Replace with a transactional DB in production."""

    def __init__(self) -> None:
        self.quotes: dict[str, Any] = {}
        self.claims: dict[str, Any] = {}
        self.challenges: dict[str, Any] = {}
        self.used_tx_hashes: set[str] = set()

    def expired(self, expires_at: datetime) -> bool:
        from app.security import utc_now
        return utc_now() >= expires_at


store = MemoryStore()
