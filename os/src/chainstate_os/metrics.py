from dataclasses import dataclass

@dataclass
class SafetyMetrics:
    blocked_actions: int = 0
    approved_actions: int = 0
    kill_gate_events: int = 0
    policy_errors: int = 0
    unverified_outputs: int = 0

    def as_dict(self):
        return self.__dict__.copy()
