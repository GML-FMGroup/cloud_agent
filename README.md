# cloud_agent

`cloud_agent` is a lightweight cloud operations agent focused on automating cloud service workflows.
It can be used to plan and execute routine cloud tasks through natural language, such as environment setup,
resource inspection, scheduled operations, and multi-step operational automation via CLI/tools/channels/skills.

This project is modified from the open-source `nanobot` project:
https://github.com/HKUDS/nanobot

## Install

From source:

```bash
git clone https://github.com/GML-FMGroup/cloud_agent
cd cloud_agent
pip install -e .
```

With uv:

```bash
uv tool install cloud-agent
```

From PyPI:

```bash
pip install cloud-agent
```

## Quick Start

1. Initialize:

```bash
cloud_agent onboard
```

2. Edit config at `~/.cloud_agent/config.json` (set provider API key and model).

Example:

```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4-5"
    }
  }
}
```

3. Start chatting:

```bash
cloud_agent agent -m "Hello"
```

## Core Commands

```bash
cloud_agent onboard
cloud_agent agent -m "..."
cloud_agent agent
cloud_agent gateway
cloud_agent status
cloud_agent channels status
cloud_agent channels login
cloud_agent cron add --name "daily" --message "Good morning" --cron "0 9 * * *"
cloud_agent cron list
```

## Channels

Supported channels:

- Telegram
- Discord
- WhatsApp
- Feishu
- Mochat
- DingTalk
- Slack
- Email
- QQ

Run gateway after enabling channels in config:

```bash
cloud_agent gateway
```

## Local Models (vLLM)

```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000
```

Use OpenAI-compatible config:

```json
{
  "providers": {
    "vllm": {
      "apiKey": "dummy",
      "apiBase": "http://localhost:8000/v1"
    }
  },
  "agents": {
    "defaults": {
      "model": "meta-llama/Llama-3.1-8B-Instruct"
    }
  }
}
```

## Docker

```bash
docker build -t cloud_agent .
docker run -v ~/.cloud_agent:/root/.cloud_agent --rm cloud_agent onboard
docker run -v ~/.cloud_agent:/root/.cloud_agent -p 18790:18790 cloud_agent gateway
```

## Project Structure

```text
cloud_agent/
├── agent/
├── skills/
├── channels/
├── bus/
├── cron/
├── heartbeat/
├── providers/
├── session/
├── config/
└── cli/
```

## TODO

- [ ] Support Tencent Cloud
- [ ] Support Ali Cloud
- [ ] Support Terraform-style skills

## Contributing

PRs are welcome.
