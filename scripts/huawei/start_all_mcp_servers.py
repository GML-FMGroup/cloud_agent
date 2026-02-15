#!/usr/bin/env python3
"""Start HuaweiCloud MCP servers in background."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path


def default_script_root() -> Path:
    return Path(__file__).resolve().parent


def default_mcp_root() -> Path:
    return default_script_root() / "mcp-server"


def is_process_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def discover_server_modules(services_root: Path) -> list[tuple[str, str]]:
    modules: list[tuple[str, str]] = []
    for server_dir in sorted(services_root.glob("mcp_server_*")):
        if not server_dir.is_dir():
            continue
        name = server_dir.name
        run_py = server_dir / "src" / name / "run.py"
        if not run_py.exists():
            continue
        module = f"huaweicloud_services_server.{name}.src.{name}.run"
        modules.append((name, module))
    return modules


def parse_only(value: str) -> set[str]:
    if not value:
        return set()
    return {x.strip() for x in value.split(",") if x.strip()}


def main() -> int:
    parser = argparse.ArgumentParser(description="Start HuaweiCloud MCP servers")
    parser.add_argument(
        "--mcp-root",
        default=str(default_mcp_root()),
        help="mcp root path (absolute or relative to scripts/huawei)",
    )
    parser.add_argument(
        "--runtime-dir",
        default=".mcp_runtime",
        help="runtime dir (absolute or relative to scripts/huawei)",
    )
    parser.add_argument(
        "--only",
        default="",
        help="only start selected servers, comma-separated, e.g. mcp_server_ecs,mcp_server_obs",
    )
    parser.add_argument(
        "--transport",
        choices=["http", "sse", "stdio"],
        default="",
        help="optional transport override for all servers",
    )
    args = parser.parse_args()

    mcp_root_input = Path(args.mcp_root)
    mcp_root = (
        mcp_root_input.resolve()
        if mcp_root_input.is_absolute()
        else (default_script_root() / mcp_root_input).resolve()
    )
    services_root = mcp_root / "huaweicloud_services_server"
    if not services_root.exists():
        print(f"MCP services root not found: {services_root}")
        return 1

    runtime_dir_input = Path(args.runtime_dir)
    runtime_dir = (
        runtime_dir_input.resolve()
        if runtime_dir_input.is_absolute()
        else (default_script_root() / runtime_dir_input).resolve()
    )
    logs_dir = runtime_dir / "logs"
    runtime_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    state_file = runtime_dir / "mcp_servers_state.json"

    existing: dict[str, dict] = {}
    if state_file.exists():
        try:
            existing = json.loads(state_file.read_text(encoding="utf-8"))
        except Exception:
            existing = {}

    only = parse_only(args.only)
    modules = discover_server_modules(services_root)
    if only:
        modules = [(n, m) for n, m in modules if n in only]

    if not modules:
        print("No MCP servers found to start.")
        return 1

    started = 0
    skipped = 0
    failed = 0
    now = int(time.time())

    for name, module in modules:
        info = existing.get(name)
        if info and isinstance(info, dict):
            pid = info.get("pid")
            if isinstance(pid, int) and is_process_alive(pid):
                print(f"[SKIP] {name}: already running (pid={pid})")
                skipped += 1
                continue

        log_file = logs_dir / f"{name}.log"
        log_fp = log_file.open("ab")
        cmd = [sys.executable, "-m", module]
        if args.transport:
            cmd.extend(["-t", args.transport])

        try:
            proc = subprocess.Popen(
                cmd,
                cwd=str(mcp_root),
                stdout=log_fp,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
            time.sleep(0.2)
            if proc.poll() is not None:
                print(f"[FAIL] {name}: exited immediately, check {log_file}")
                failed += 1
                continue

            existing[name] = {
                "pid": proc.pid,
                "module": module,
                "cwd": str(mcp_root),
                "log": str(log_file),
                "transport_override": args.transport,
                "started_at": now,
            }
            print(f"[OK]   {name}: pid={proc.pid}")
            started += 1
        finally:
            log_fp.close()

    state_file.write_text(json.dumps(existing, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nDone.")
    print(f"- started: {started}")
    print(f"- skipped: {skipped}")
    print(f"- failed:  {failed}")
    print(f"- state:   {state_file}")
    print(f"- logs:    {logs_dir}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
