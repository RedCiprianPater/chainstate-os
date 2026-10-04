from dataclasses import dataclass
from .safety import SafetyGate

@dataclass
class ActionResult:
    action: str
    status: str
    detail: str

class Runtime:
    def __init__(self, config, audit):
        self.config, self.audit = config, audit
        self.safety = SafetyGate(config, audit)
    def status(self):
        return {"mode": self.config.mode, "dry_run": self.config.dry_run, "killed": self.safety.killed(), "hardware_actuation": self.config.allow_hardware_actuation}
    def dry_run(self, action: str, human_approved: bool = False) -> ActionResult:
        self.safety.check(action, human_approved)
        self.audit.write("dry_run", action=action)
        return ActionResult(action, "simulated", "No external side effect performed")
