import json, time
from pathlib import Path

class AuditLog:
    def __init__(self, path: str = "audit/events.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
    def write(self, event: str, **fields):
        record = {"ts": time.time(), "event": event, **fields}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, sort_keys=True) + "\n")
