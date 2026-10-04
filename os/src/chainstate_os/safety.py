from pathlib import Path
from .config import RuntimeConfig

class SafetyError(RuntimeError):
    pass

class SafetyGate:
    def __init__(self, config: RuntimeConfig, audit):
        self.config, self.audit = config, audit
    def killed(self) -> bool:
        return Path(self.config.kill_gate_file).exists()
    def check(self, action: str, human_approved: bool = False):
        if self.killed():
            self.audit.write("blocked", action=action, reason="kill_gate")
            raise SafetyError("kill gate is active")
        restricted = {"network_access", "filesystem_write", "shell_command", "package_install", "hardware_actuation"}
        if action in restricted and not human_approved:
            self.audit.write("blocked", action=action, reason="human_approval_required")
            raise SafetyError("human approval required")
        if action == "hardware_actuation" and not self.config.allow_hardware_actuation:
            self.audit.write("blocked", action=action, reason="hardware_disabled")
            raise SafetyError("hardware actuation is disabled")
        self.audit.write("authorized", action=action, dry_run=self.config.dry_run)
        return True
