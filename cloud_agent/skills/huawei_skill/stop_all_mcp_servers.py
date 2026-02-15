#!/usr/bin/env python3
"""Stop MCP servers started by start_all_mcp_servers.py."""

from __future__ import annotations

import argparse
import json
import os
import signal
import time
from pathlib import Path


def default_skill_root() -> Path:
    # The skill directory that contains this script.
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Stop all MCP servers")
    parser.add_argument(
        "--workspace-root",
        default=str(default_skill_root()),
        help="skill root directory (defaults to script directory)",
    )
    parser.add_argument("--runtime-dir", default=".mcp_runtime", help="runtime dir")
    parser.add_argument(
        "--only",
        default="",
        help="only stop selected servers, comma-separated, e.g. mcp_server_ecs,mcp_server_obs",
    )
    parser.add_argument("--timeout", type=float, default=8.0, help="SIGTERM wait seconds")
    args = parser.parse_args()

    workspace_root = Path(args.workspace_root).resolve()
    runtime_dir = (workspace_root / args.runtime_dir).resolve()
    state_file = runtime_dir / "mcp_servers_state.json"

    if not state_file.exists():
        print(f"State file not found: {state_file}")
        return 0

    try:
        state: dict[str, dict] = json.loads(state_file.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Invalid state file: {exc}")
        return 1

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
