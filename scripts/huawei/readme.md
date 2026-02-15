# Huawei MCP Server 管理说明

本目录用于管理华为云 MCP 服务进程，供 `huawei_skill` 调用。

目录结构:
- `start_all_mcp_servers.py`: 启动脚本
- `stop_all_mcp_servers.py`: 停止脚本
- `mcp-server/`: 上游服务源码

## 前置条件
- 需设置凭证环境变量:
  - `HUAWEI_ACCESS_KEY`
  - `HUAWEI_SECRET_KEY`
- 建议可选设置:
  - `HUAWEI_REGION`
- 依赖安装（在仓库根目录执行）:
  - `cd scripts/huawei/mcp-server`
  - `uv sync`
  - 或 `python3 -m pip install -e .`

## 快速开始
在仓库根目录执行:

```bash
python3 scripts/huawei/start_all_mcp_servers.py
```

停止全部服务:

```bash
python3 scripts/huawei/stop_all_mcp_servers.py
```

## 常用参数
启动脚本:
- `--only mcp_server_ecs,mcp_server_iam`: 仅启动指定服务
- `--transport http|sse|stdio`: 统一覆盖传输方式
- `--skill-root <path>`: 指定 `huawei_skill` 根目录
- `--mcp-root <path>`: 指定 `mcp-server` 目录（默认 `scripts/huawei/mcp-server`）
- `--runtime-dir <path>`: 运行状态目录（默认 `.mcp_runtime`）

停止脚本:
- `--only mcp_server_ecs,mcp_server_iam`: 仅停止指定服务
- `--timeout 8`: 优雅停止等待秒数
- `--skill-root <path>`: 指定 `huawei_skill` 根目录
- `--runtime-dir <path>`: 运行状态目录（默认 `.mcp_runtime`）

## 服务可用性检查（推荐）
不要只看状态文件。应直接请求目标服务 endpoint 判断是否可用:
- endpoint 格式: `http://127.0.0.1:<port>/mcp`
- 端口来源: `cloud_agent/skills/huawei_skill/catalog/server_runtime_index.json`

例如 ECS:

```bash
curl -sS -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8888/mcp
```

若连接失败、超时或拒绝连接，说明服务未启动或不可用。

## 运行状态与日志
- 状态文件: `cloud_agent/skills/huawei_skill/.mcp_runtime/mcp_servers_state.json`
- 日志目录: `cloud_agent/skills/huawei_skill/.mcp_runtime/logs/`

注意: 状态文件仅用于记录，不作为服务可用性的唯一依据。

## Python 依赖汇总
- 根项目依赖(来源: `scripts/huawei/mcp-server/pyproject.toml`):
  - `aiohttp>=3.11.18`
  - `fastmcp>=2.0.0`
  - `pydantic>=2.0.0`
  - `pyyaml>=6.0.2`
  - `requests>=2.32.3`
  - `tzdata>=2024.2`
  - `huaweicloudsdkcore>=3.1.150`
- 通用时间服务依赖(来源: `scripts/huawei/mcp-server/common_servers/mcp_server_time/pyproject.toml`):
  - `fastmcp>=2.9.2`
  - `pydantic>=2.11.7`
  - `tzlocal>=5.3.1`
- DWS 内部服务依赖(来源: `scripts/huawei/mcp-server/huaweicloud_dws_mcp_inner/pyproject.toml` 与 `requirements.txt`):
  - `httpx>=0.28.1` (`requirements.txt` 中为 `httpx==0.28.1`)
  - `mcp[cli]>=1.9.3` (`requirements.txt` 中为 `mcp[cli]==1.10.1`)
  - `psycopg2>=2.9.10` (`requirements.txt` 中为 `psycopg2==2.9.10`)

## 可移植性说明
- `cloud_agent/skills/huawei_skill/catalog/mcp_server_*.json` 中 `openapiFile` 使用相对路径前缀 `../../../scripts/huawei/mcp-server/...`。
- 调整目录结构时需同步更新该前缀。

## 上游来源
- `scripts/huawei/mcp-server` 来自 HuaweiCloudDeveloper 官方仓库:
  - https://github.com/HuaweiCloudDeveloper/mcp-server
