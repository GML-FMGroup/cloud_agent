#!/usr/bin/env python3
"""Stop HuaweiCloud MCP servers started by start_all_mcp_servers.py."""

from __future__ import annotations

import argparse
import json
import os
import re
import signal
import time
from pathlib import Path


def default_script_root() -> Path:
    return Path(__file__).resolve().parent


def is_process_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def terminate_process_group(pid: int, timeout: float) -> bool:
    try:
        os.killpg(pid, signal.SIGTERM)
    except ProcessLookupError:
        return True
    except Exception:
        # fallback to single process
        try:
            os.kill(pid, signal.SIGTERM)
        except ProcessLookupError:
            return True

    deadline = time.time() + timeout
    while time.time() < deadline:
        if not is_process_alive(pid):
            return True
        time.sleep(0.2)

    # force kill
    try:
        os.killpg(pid, signal.SIGKILL)
    except Exception:
        try:
            os.kill(pid, signal.SIGKILL)
        except ProcessLookupError:
            return True

    time.sleep(0.2)
    return not is_process_alive(pid)


def parse_only(value: str) -> set[str]:
    if not value:
        return set()
    return {x.strip() for x in value.split(",") if x.strip()}


def recover_state_from_logs(logs_dir: Path) -> dict[str, dict]:
    recovered: dict[str, dict] = {}
    if not logs_dir.exists():
        return recovered

    pid_pattern = re.compile(r"Started server process \[(\d+)\]")
    for log_file in sorted(logs_dir.glob("mcp_server_*.log")):
        name = log_file.stem
        pid = None
        try:
            for line in log_file.read_text(encoding="utf-8", errors="ignore").splitlines():
                match = pid_pattern.search(line)
                if match:
                    pid = int(match.group(1))
        except Exception:
            continue

        if pid is not None:
            recovered[name] = {
                "pid": pid,
                "log": str(log_file),
                "recovered_from_log": True,
            }
    return recovered


def main() -> int:
    parser = argparse.ArgumentParser(description="Stop HuaweiCloud MCP servers")
    parser.add_argument(
        "--runtime-dir",
        default=".mcp_runtime",
        help="runtime dir (absolute or relative to scripts/huawei)",
    )
    parser.add_argument(
        "--only",
        default="",
        help="only stop selected servers, comma-separated, e.g. mcp_server_ecs,mcp_server_obs",
    )
    parser.add_argument("--timeout", type=float, default=8.0, help="SIGTERM wait seconds")
    args = parser.parse_args()

    runtime_dir_input = Path(args.runtime_dir)
    runtime_dir = (
        runtime_dir_input.resolve()
        if runtime_dir_input.is_absolute()
        else (default_script_root() / runtime_dir_input).resolve()
    )
    state_file = runtime_dir / "mcp_servers_state.json"
    logs_dir = runtime_dir / "logs"

    state: dict[str, dict] = {}
    if state_file.exists():
        try:
            state = json.loads(state_file.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"Invalid state file: {exc}")
            return 1
    else:
        print(f"State file not found: {state_file}")
        state = recover_state_from_logs(logs_dir)
        if state:
            print(f"Recovered {len(state)} server(s) from logs: {logs_dir}")
        else:
            print("No recoverable server pid found in logs.")
            return 0

    only = parse_only(args.only)
    targets = sorted(state.keys())
    if only:
        targets = [x for x in targets if x in only]

    if not targets:
        print("No matching servers to stop.")
        return 0

    stopped = 0
    missing = 0
    failed = 0

    for name in targets:
        info = state.get(name, {})
        pid = info.get("pid")
        if not isinstance(pid, int):
            print(f"[MISS] {name}: invalid pid")
            missing += 1
            state.pop(name, None)
            continue

        if not is_process_alive(pid):
            print(f"[MISS] {name}: not running (pid={pid})")
            missing += 1
            state.pop(name, None)
            continue

        ok = terminate_process_group(pid, timeout=args.timeout)
        if ok:
            print(f"[OK]   {name}: stopped (pid={pid})")
            stopped += 1
            state.pop(name, None)
        else:
            print(f"[FAIL] {name}: failed to stop (pid={pid})")
            failed += 1

    state_file.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    print("\nDone.")
    print(f"- stopped: {stopped}")
    print(f"- missing: {missing}")
    print(f"- failed:  {failed}")
    print(f"- state:   {state_file}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
