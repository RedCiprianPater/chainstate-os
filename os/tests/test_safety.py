from pathlib import Path
from chainstate_os.config import RuntimeConfig
from chainstate_os.audit import AuditLog
from chainstate_os.runtime import Runtime
from chainstate_os.safety import SafetyError

def test_restricted_action_requires_approval(tmp_path):
    cfg = RuntimeConfig(kill_gate_file=str(tmp_path / "kill"))
    rt = Runtime(cfg, AuditLog(str(tmp_path / "events.jsonl")))
    try:
        rt.dry_run("shell_command")
        assert False
    except SafetyError:
        assert True

def test_kill_gate_blocks(tmp_path):
    kill = tmp_path / "kill"; kill.touch()
    cfg = RuntimeConfig(kill_gate_file=str(kill))
    rt = Runtime(cfg, AuditLog(str(tmp_path / "events.jsonl")))
    try:
        rt.dry_run("read_system_info")
        assert False
    except SafetyError:
        assert True
