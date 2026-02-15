# Findings

- Primary package directory was `cloud_agent/`; now renamed to `cloud_agent/`.
- Packaging metadata and console entrypoint were updated to `cloud_agent`.
- Runtime data path defaults migrated from `~/.cloud_agent` to `~/.cloud_agent`.
- Environment variable prefix updated from `CLOUD_AGENT_` to `CLOUD_AGENT_`.
- Added extension surface via CLI group: `cloud_agent extensions info`.
