import argparse, json
from .config import load_config
from .audit import AuditLog
from .runtime import Runtime

def build():
    cfg = load_config("config/runtime.yaml")
    return Runtime(cfg, AuditLog())

def main():
    p = argparse.ArgumentParser(prog="chainstate-os")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    d = sub.add_parser("dry-run"); d.add_argument("--action", required=True); d.add_argument("--approved", action="store_true")
    args = p.parse_args(); rt = build()
    if args.cmd == "status": print(json.dumps(rt.status(), indent=2)); return
    if args.cmd == "dry-run":
        result = rt.dry_run(args.action, args.approved); print(json.dumps(result.__dict__, indent=2))

if __name__ == "__main__": main()
