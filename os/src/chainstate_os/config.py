from dataclasses import dataclass
from pathlib import Path
import yaml

@dataclass(frozen=True)
class RuntimeConfig:
    mode: str = "local-first"
    dry_run: bool = True
    allow_network: bool = False
    allow_shell: bool = False
    allow_filesystem_write: bool = False
    allow_hardware_actuation: bool = False
    require_human_approval: bool = True
    kill_gate_file: str = "/tmp/chainstate-os-kill"
    max_action_seconds: int = 10

def load_config(path: str | Path) -> RuntimeConfig:
    data = yaml.safe_load(Path(path).read_text()) or {}
    return RuntimeConfig(**data)
