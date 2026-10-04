class InferenceAdapter:
    """Interface only. Implementations must run in a sandbox and emit provenance."""
    def infer(self, observation: dict) -> dict:
        raise NotImplementedError

class HardwareAdapter:
    """Read-only interface by default; no actuation implementation is provided."""
    def read_sensors(self) -> dict:
        raise NotImplementedError
    def actuate(self, command: dict):
        raise PermissionError("hardware actuation is not implemented")
