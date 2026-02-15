# Huawei Cloud MCP Skill Guide

## 目标
- 为大模型提供分层导航能力: 先选 mcp server, 再看 README, 最后按 schema 精确调用 API。
- 避免一次性加载 173 个 server 的全部 schema, 降低上下文开销并提高调用准确率。

## 资料目录
- 根目录: `./`
- 资源目录: `./catalog/`
- MCP 启动脚本: `./start_all_mcp_servers.py`
- MCP 停止脚本: `./stop_all_mcp_servers.py`
- MCP 运行时目录: `./.mcp_runtime/`
- MCP server 源码目录: `./mcp-server/`
- 每个 server 的 schema: `catalog/mcp_server_<name>.json`
- 每个 server 的说明文档: `catalog/mcp_server_<name>.md` (优先 README_zh)
- 每个 server 的运行索引(端口/transport/命令): `catalog/server_runtime_index.json`
- 总服务数: 173
- 有 README 的服务数: 172

## 运行与调用方法
1. 启动 MCP servers (由大模型在任务开始时执行)
   先解析 `SKILL.md` 所在目录为 `<skill_root>`，再执行:
   `<python_cmd> <skill_root>/start_all_mcp_servers.py`
   - `python_cmd` 优先 `python3`，不可用时退化为 `python`
   - 可选: `--only mcp_server_ecs,mcp_server_obs`
   - 可选: `--transport http|sse|stdio`
2. 查看某个服务的默认端口和传输方式
   在 `catalog/server_runtime_index.json` 按 `server` 查 `defaultPort` 和 `defaultTransport`。
3. 连接方式
   `http` 模式: `http://127.0.0.1:<port>/mcp`
   `sse` 模式: `http://127.0.0.1:<port>/sse`
   `stdio` 模式: 使用 `python -m <module> -t stdio`
4. 任务结束后停止 MCP servers (由大模型执行收尾)
   `<python_cmd> <skill_root>/stop_all_mcp_servers.py`
   - `python_cmd` 优先 `python3`，不可用时退化为 `python`
   - 可选: `--only mcp_server_ecs,mcp_server_obs`
   - 可选: `--timeout 8`

## 启停脚本依赖说明
- 代码依赖: Python 标准库(`argparse/json/os/subprocess/signal/time/pathlib`)，无需额外 pip 包。
- 运行依赖: `<skill_root>/mcp-server/` 目录(用于按模块启动各服务)。
- 脚本默认按当前仓库结构自动定位 `skill root`，并将运行状态写入 `<skill_root>/.mcp_runtime/mcp_servers_state.json`。

## 认证与环境变量
- 使用华为云 MCP server 前，用户环境变量中必须提供以下凭证:
  - `HUAWEI_ACCESS_KEY`
  - `HUAWEI_SECRET_KEY`
- 可选: 若业务需要，也可设置 `HUAWEI_REGION` 指定默认区域。
- 建议在启动 MCP servers 前先检查变量是否存在，避免调用时出现鉴权失败。
- 示例(Unix shell):
  - `export HUAWEI_ACCESS_KEY=\"<your-ak>\"`
  - `export HUAWEI_SECRET_KEY=\"<your-sk>\"`
  - `export HUAWEI_REGION=\"cn-north-4\"`

## 首次复制后的依赖准备
- 仅复制 `hc_skill` 目录后，需要在目标环境安装 `mcp-server` 依赖，否则服务可能因缺少 `uvicorn` 等包启动失败。
- 进入 `<skill_root>/mcp-server` 后，执行以下任一方式:
  - 推荐: `uv sync`
  - 备选: `<python_cmd> -m pip install -e .`
- 可选自检:
  - `<python_cmd> -c \"import uvicorn,fastmcp,pydantic,yaml,requests,aiohttp,huaweicloudsdkcore; print('deps ok')\"`

## mcp-server Python 依赖汇总
- 根项目依赖(来源: `mcp-server/pyproject.toml`):
  - `aiohttp>=3.11.18`
  - `fastmcp>=2.0.0`
  - `pydantic>=2.0.0`
  - `pyyaml>=6.0.2`
  - `requests>=2.32.3`
  - `tzdata>=2024.2`
  - `huaweicloudsdkcore>=3.1.150`
- 通用时间服务依赖(来源: `mcp-server/common_servers/mcp_server_time/pyproject.toml`):
  - `fastmcp>=2.9.2`
  - `pydantic>=2.11.7`
  - `tzlocal>=5.3.1`
- DWS 内部服务依赖(来源: `mcp-server/huaweicloud_dws_mcp_inner/pyproject.toml` 与 `requirements.txt`):
  - `httpx>=0.28.1` (`requirements.txt` 中为 `httpx==0.28.1`)
  - `mcp[cli]>=1.9.3` (`requirements.txt` 中为 `mcp[cli]==1.10.1`)
  - `psycopg2>=2.9.10` (`requirements.txt` 中为 `psycopg2==2.9.10`)
- 最小安装建议:
  - 若只使用主服务集合，优先安装 `mcp-server/pyproject.toml` 依赖即可。
  - 若需要 `mcp_server_time` 或 `huaweicloud_dws_mcp_inner`，再补充对应子项目依赖。

## 可移植性说明
- `catalog/mcp_server_*.json` 中 `openapiFile` 已改为相对路径(前缀 `mcp-server/...`)，可直接随 `hc_skill` 目录迁移。

## 上游来源
- `hc_skill/mcp-server` 来自 HuaweiCloudDeveloper 官方仓库: [mcp-server](https://github.com/HuaweiCloudDeveloper/mcp-server)。

## API 调用模板
1. 从 `catalog/mcp_server_<name>.json` 中选择目标工具,读取:
   `tools[].name`, `tools[].description`, `tools[].inputSchema`
2. 按 `inputSchema.required` 组装参数,缺失字段不得调用。
3. 调用参数应与 schema 严格一致,不要添加未定义字段。
4. 常见最小调用结构:
   - `tool`: 工具名(例如 `ListServersDetails`)
   - `arguments`: 与 `inputSchema` 对齐的 JSON 对象
   - `region`: 若该 API 需要区域,优先显式传入

## 分层使用流程
1. 先根据用户意图选择候选服务(1-3 个), 不要立即展开全部 schema。
2. 打开候选服务的 `catalog/mcp_server_*.md`, 读取 Overview 与工具分类。
3. 打开对应 `catalog/mcp_server_*.json`, 在 `tools` 中定位最相关 API。
4. 仅提取目标 API 的 `name`、`description`、`inputSchema` 组织调用参数。
5. 调用前校验必填字段(`required`)、路径参数、区域(`region`)与凭证。
6. 调用失败时先做参数纠错, 再考虑切换到同域备选 server。

## 调用约束
- 不要凭空构造 schema 字段; 只能使用 `inputSchema` 中定义的字段。
- 对高风险操作(删除/变更类)先二次确认。
- 一次任务优先少量 API 迭代调用, 每次调用后依据返回结果调整下一步。
- 若文档缺失(例如 `mcp_server_mss`), 直接以 json schema 为准。

## 检索与调用示例
1. 用户意图: 查询 ECS 实例列表。
2. 选服务: `mcp_server_ecs`。
3. 查文档: 打开 `catalog/mcp_server_ecs.md`, 找到“云服务器查询/列表”相关工具。
4. 查 schema: 打开 `catalog/mcp_server_ecs.json`, 在 `tools` 中定位工具并读取 `inputSchema`。
5. 组参数: 仅填写 `required` 字段, 再按需补充可选字段, 最终发起调用。
6. 若返回权限或参数错误: 先修正 `region`、资源 ID、必填参数, 再重试。

## 服务索引
| server | service | tools | 用途 | README | Schema |
|---|---:|---:|---|---|---|
| `mcp_server_aad` | AAD | 61 | 用于华为云 AAD 服务的资源查询与操作。 重点能力: DDoS原生高级防护-告警配置管理 / DDoS原生高级防护-实例管理 / DDoS原生高级防护-策略管理。 | [`mcp_server_aad.md`](./catalog/mcp_server_aad.md) | [`mcp_server_aad.json`](./catalog/mcp_server_aad.json) |
| `mcp_server_anti_ddos` | Anti-DDoS | 18 | 用于华为云 Anti-DDoS 服务的资源查询与操作。 重点能力: DDoS任务管理 / DDoS防护管理 / 告警配置管理。 | [`mcp_server_anti_ddos.md`](./catalog/mcp_server_anti_ddos.md) | [`mcp_server_anti_ddos.json`](./catalog/mcp_server_anti_ddos.json) |
| `mcp_server_aom` | AOM | 86 | 用于华为云 AOM 服务的资源查询与操作。 重点能力: AppManagement / Component / Permission。 | [`mcp_server_aom.md`](./catalog/mcp_server_aom.md) | [`mcp_server_aom.json`](./catalog/mcp_server_aom.json) |
| `mcp_server_apiexplorer` | APIExplorer | 6 | 用于华为云 APIExplorer 服务的资源查询与操作。 重点能力: ApiServerV2 / ApiServerV3 / GroupServer。 | [`mcp_server_apiexplorer.md`](./catalog/mcp_server_apiexplorer.md) | [`mcp_server_apiexplorer.json`](./catalog/mcp_server_apiexplorer.json) |
| `mcp_server_apig` | APIG | 273 | 用于华为云 APIG 服务的资源查询与操作。 重点能力: ACL策略管理 / API分组管理 / API管理。 | [`mcp_server_apig.md`](./catalog/mcp_server_apig.md) | [`mcp_server_apig.json`](./catalog/mcp_server_apig.json) |
| `mcp_server_apm` | APM | 45 | 用于华为云 APM 服务的资源查询与操作。 重点能力: AKSK / ALARM / APM。 | [`mcp_server_apm.md`](./catalog/mcp_server_apm.md) | [`mcp_server_apm.json`](./catalog/mcp_server_apm.json) |
| `mcp_server_as` | AS | 62 | 用于华为云 AS 服务的资源查询与操作。 重点能力: TAG功能 / 伸缩活动日志管理 / 伸缩策略日志管理。 | [`mcp_server_as.md`](./catalog/mcp_server_as.md) | [`mcp_server_as.json`](./catalog/mcp_server_as.json) |
| `mcp_server_asm` | ASM | 4 | 用于华为云 ASM 服务的资源查询与操作。 重点能力: 网格接口。 | [`mcp_server_asm.md`](./catalog/mcp_server_asm.md) | [`mcp_server_asm.json`](./catalog/mcp_server_asm.json) |
| `mcp_server_bcs` | BCS | 32 | 用于华为云 BCS 服务的资源查询与操作。 重点能力: BCS监控 / BCS管理 / BCS联盟。 | [`mcp_server_bcs.md`](./catalog/mcp_server_bcs.md) | [`mcp_server_bcs.json`](./catalog/mcp_server_bcs.json) |
| `mcp_server_bms` | BMS | 31 | 用于华为云 BMS 服务的资源查询与操作。 重点能力: Job管理 / 查询API版本信息 / 状态管理。 | [`mcp_server_bms.md`](./catalog/mcp_server_bms.md) | [`mcp_server_bms.json`](./catalog/mcp_server_bms.json) |
| `mcp_server_cae` | CAE | 56 | 用于华为云 CAE 服务的资源查询与操作。 重点能力: Application / Application操作 / Component。 | [`mcp_server_cae.md`](./catalog/mcp_server_cae.md) | [`mcp_server_cae.json`](./catalog/mcp_server_cae.json) |
| `mcp_server_campusgo` | CampusGo | 4 | 用于华为云 CampusGo 服务的资源查询与操作。 重点能力: 服务作业管理。 | [`mcp_server_campusgo.md`](./catalog/mcp_server_campusgo.md) | [`mcp_server_campusgo.json`](./catalog/mcp_server_campusgo.json) |
| `mcp_server_cbh` | CBH | 49 | 用于华为云 CBH 服务的资源查询与操作。 重点能力: DDM实例管理 / 云堡垒机信息查询 / 云堡垒机管理。 | [`mcp_server_cbh.md`](./catalog/mcp_server_cbh.md) | [`mcp_server_cbh.json`](./catalog/mcp_server_cbh.json) |
| `mcp_server_cbr` | CBR | 71 | 用于华为云 CBR 服务的资源查询与操作。 重点能力: Checkpoint管理 / 主机管理 / 任务。 | [`mcp_server_cbr.md`](./catalog/mcp_server_cbr.md) | [`mcp_server_cbr.json`](./catalog/mcp_server_cbr.json) |
| `mcp_server_cbs` | CBS | 29 | 用于华为云 CBS 服务的资源查询与操作。 重点能力: 其他问答 / 其他问答API / 形象管理。 | [`mcp_server_cbs.md`](./catalog/mcp_server_cbs.md) | [`mcp_server_cbs.json`](./catalog/mcp_server_cbs.json) |
| `mcp_server_cc` | CC | 111 | 用于华为云 CC 服务的资源查询与操作。 重点能力: Authorisation / BandwidthPackage / CentralNetwork。 | [`mcp_server_cc.md`](./catalog/mcp_server_cc.md) | [`mcp_server_cc.json`](./catalog/mcp_server_cc.json) |
| `mcp_server_cce` | CCE | 151 | 用于华为云 CCE 服务的资源查询与操作。 重点能力: DDM实例管理 / 存储管理 / 实例管理。 | [`mcp_server_cce.md`](./catalog/mcp_server_cce.md) | [`mcp_server_cce.json`](./catalog/mcp_server_cce.json) |
| `mcp_server_cci` | CCI | 148 | 用于华为云 CCI 服务的资源查询与操作。 重点能力: API groups / ClusterRole / ConfigMap。 | [`mcp_server_cci.md`](./catalog/mcp_server_cci.md) | [`mcp_server_cci.json`](./catalog/mcp_server_cci.json) |
| `mcp_server_ccm` | CCM | 42 | 用于华为云 CCM 服务的资源查询与操作。 重点能力: 标签管理 / 私有CA管理 / 私有证书管理。 | [`mcp_server_ccm.md`](./catalog/mcp_server_ccm.md) | [`mcp_server_ccm.json`](./catalog/mcp_server_ccm.json) |
| `mcp_server_cdm` | CDM | 27 | 用于华为云 CDM 服务的资源查询与操作。 重点能力: Job相关接口 / Job管理 / 任务管理。 | [`mcp_server_cdm.md`](./catalog/mcp_server_cdm.md) | [`mcp_server_cdm.json`](./catalog/mcp_server_cdm.json) |
| `mcp_server_ces` | CES | 71 | 用于华为云 CES 服务的资源查询与操作。 重点能力: Agent任务相关接口 / 一键告警 / 主机监控。 | [`mcp_server_ces.md`](./catalog/mcp_server_ces.md) | [`mcp_server_ces.json`](./catalog/mcp_server_ces.json) |
| `mcp_server_cfw` | CFW | 95 | 用于华为云 CFW 服务的资源查询与操作。 重点能力: ACL规则管理 / EIP管理 / IPS管理。 | [`mcp_server_cfw.md`](./catalog/mcp_server_cfw.md) | [`mcp_server_cfw.json`](./catalog/mcp_server_cfw.json) |
| `mcp_server_cloudide` | CloudIDE | 44 | 用于华为云 CloudIDE 服务的资源查询与操作。 重点能力: IDE实例管理 / codebreeze / codebreezetsbot。 | [`mcp_server_cloudide.md`](./catalog/mcp_server_cloudide.md) | [`mcp_server_cloudide.json`](./catalog/mcp_server_cloudide.json) |
| `mcp_server_cloudpipeline` | CloudPipeline | 21 | 用于华为云 CloudPipeline 服务的资源查询与操作。 重点能力: Logstash接口 / 模板管理 / 流水线模板管理--新。 | [`mcp_server_cloudpipeline.md`](./catalog/mcp_server_cloudpipeline.md) | [`mcp_server_cloudpipeline.json`](./catalog/mcp_server_cloudpipeline.json) |
| `mcp_server_cloudrtc` | CloudRTC | 42 | 用于华为云 CloudRTC 服务的资源查询与操作。 重点能力: OBS桶管理 / RtcStatisticsDataApi / 单流任务管理。 | [`mcp_server_cloudrtc.md`](./catalog/mcp_server_cloudrtc.md) | [`mcp_server_cloudrtc.json`](./catalog/mcp_server_cloudrtc.json) |
| `mcp_server_cloudtable` | CloudTable | 10 | 用于华为云 CloudTable 服务的资源查询与操作。 重点能力: CloudTable集群管理接口 / CloudTable集群管理接口v3。 | [`mcp_server_cloudtable.md`](./catalog/mcp_server_cloudtable.md) | [`mcp_server_cloudtable.json`](./catalog/mcp_server_cloudtable.json) |
| `mcp_server_cloudtest` | CloudTest | 140 | 用于华为云 CloudTest 服务的资源查询与操作。 重点能力: ApigAutoInitController / Attachments / ITaskController。 | [`mcp_server_cloudtest.md`](./catalog/mcp_server_cloudtest.md) | [`mcp_server_cloudtest.json`](./catalog/mcp_server_cloudtest.json) |
| `mcp_server_cms` | CMS | 7 | 用于华为云 CMS 服务的资源查询与操作。 重点能力: 智能购买组管理 / 生命周期管理 / 规格推荐管理。 | [`mcp_server_cms.md`](./catalog/mcp_server_cms.md) | [`mcp_server_cms.json`](./catalog/mcp_server_cms.json) |
| `mcp_server_coc` | COC | 62 | 用于华为云 COC 服务的资源查询与操作。 重点能力: Application操作 / CustomEventMessageIntegration / DocumentManagement。 | [`mcp_server_coc.md`](./catalog/mcp_server_coc.md) | [`mcp_server_coc.json`](./catalog/mcp_server_coc.json) |
| `mcp_server_codeartsartifact` | CodeArtsArtifact | 28 | 用于华为云 CodeArtsArtifact 服务的资源查询与操作。 重点能力: 仓库关联项目 / 仓库容量 / 仓库管理。 | [`mcp_server_codeartsartifact.md`](./catalog/mcp_server_codeartsartifact.md) | [`mcp_server_codeartsartifact.json`](./catalog/mcp_server_codeartsartifact.json) |
| `mcp_server_codeartsbuild` | CodeArtsBuild | 63 | 用于华为云 CodeArtsBuild 服务的资源查询与操作。 重点能力: CodeArtsBuild / Job管理 / Offline。 | [`mcp_server_codeartsbuild.md`](./catalog/mcp_server_codeartsbuild.md) | [`mcp_server_codeartsbuild.json`](./catalog/mcp_server_codeartsbuild.json) |
| `mcp_server_codeartscheck` | CodeArtsCheck | 29 | 用于华为云 CodeArtsCheck 服务的资源查询与操作。 重点能力: ITaskController / 任务管理 / 缺陷管理。 | [`mcp_server_codeartscheck.md`](./catalog/mcp_server_codeartscheck.md) | [`mcp_server_codeartscheck.json`](./catalog/mcp_server_codeartscheck.json) |
| `mcp_server_codeartsdeploy` | CodeArtsDeploy | 65 | 用于华为云 CodeArtsDeploy 服务的资源查询与操作。 重点能力: AppGroupsController / AppManagement / AppPermissionsController。 | [`mcp_server_codeartsdeploy.md`](./catalog/mcp_server_codeartsdeploy.md) | [`mcp_server_codeartsdeploy.json`](./catalog/mcp_server_codeartsdeploy.json) |
| `mcp_server_codeartsinspector` | CodeArtsInspector | 28 | 用于华为云 CodeArtsInspector 服务的资源查询与操作。 重点能力: Group / host_groups / host_results。 | [`mcp_server_codeartsinspector.md`](./catalog/mcp_server_codeartsinspector.md) | [`mcp_server_codeartsinspector.json`](./catalog/mcp_server_codeartsinspector.json) |
| `mcp_server_codeartspipeline` | CodeArtsPipeline | 81 | 用于华为云 CodeArtsPipeline 服务的资源查询与操作。 | [`mcp_server_codeartspipeline.md`](./catalog/mcp_server_codeartspipeline.md) | [`mcp_server_codeartspipeline.json`](./catalog/mcp_server_codeartspipeline.json) |
| `mcp_server_codecheck` | CodeCheck | 29 | 用于华为云 CodeCheck 服务的资源查询与操作。 重点能力: 任务管理 / 缺陷管理 / 规则管理。 | [`mcp_server_codecheck.md`](./catalog/mcp_server_codecheck.md) | [`mcp_server_codecheck.json`](./catalog/mcp_server_codecheck.json) |
| `mcp_server_codecraft` | CodeCraft | 4 | 用于华为云 CodeCraft 服务的资源查询与操作。 重点能力: 作品管理。 | [`mcp_server_codecraft.md`](./catalog/mcp_server_codecraft.md) | [`mcp_server_codecraft.json`](./catalog/mcp_server_codecraft.json) |
| `mcp_server_codehub` | CodeHub | 87 | 用于华为云 CodeHub 服务的资源查询与操作。 重点能力: Commit / DDM实例管理 / Discussion。 | [`mcp_server_codehub.md`](./catalog/mcp_server_codehub.md) | [`mcp_server_codehub.json`](./catalog/mcp_server_codehub.json) |
| `mcp_server_config` | Config | 101 | 用于华为云 Config 服务的资源查询与操作。 重点能力: Aggregator / ConformancePack / History。 | [`mcp_server_config.md`](./catalog/mcp_server_config.md) | [`mcp_server_config.json`](./catalog/mcp_server_config.json) |
| `mcp_server_cph` | CPH | 51 | 用于华为云 CPH 服务的资源查询与操作。 重点能力: ADB命令 / TAG功能 / Tags。 | [`mcp_server_cph.md`](./catalog/mcp_server_cph.md) | [`mcp_server_cph.json`](./catalog/mcp_server_cph.json) |
| `mcp_server_cpts` | CPTS | 45 | 用于华为云 CPTS 服务的资源查询与操作。 重点能力: ITaskController / PerfTest工程管理 / 事务管理。 | [`mcp_server_cpts.md`](./catalog/mcp_server_cpts.md) | [`mcp_server_cpts.json`](./catalog/mcp_server_cpts.json) |
| `mcp_server_craftartsipdcenter` | CraftArtsIPDCenter | 9 | 用于华为云 CraftArtsIPDCenter 服务的资源查询与操作。 重点能力: Station / 数字化制造云平台生产数据管理。 | [`mcp_server_craftartsipdcenter.md`](./catalog/mcp_server_craftartsipdcenter.md) | [`mcp_server_craftartsipdcenter.json`](./catalog/mcp_server_craftartsipdcenter.json) |
| `mcp_server_cse` | CSE | 35 | 用于华为云 CSE 服务的资源查询与操作。 重点能力: DDM实例管理 / gateway / nacos。 | [`mcp_server_cse.md`](./catalog/mcp_server_cse.md) | [`mcp_server_cse.json`](./catalog/mcp_server_cse.json) |
| `mcp_server_csms` | CSMS | 45 | 用于华为云 CSMS 服务的资源查询与操作。 重点能力: TAG功能 / 临时登录指令 / 事件管理。 | [`mcp_server_csms.md`](./catalog/mcp_server_csms.md) | [`mcp_server_csms.json`](./catalog/mcp_server_csms.json) |
| `mcp_server_css` | CSS | 105 | 用于华为云 CSS 服务的资源查询与操作。 重点能力: Kibana公网访问接口 / Logstash接口 / TemplateManagement。 | [`mcp_server_css.md`](./catalog/mcp_server_css.md) | [`mcp_server_css.json`](./catalog/mcp_server_css.json) |
| `mcp_server_cts` | CTS | 16 | 用于华为云 CTS 服务的资源查询与操作。 重点能力: Tags / 事件管理 / 关键操作通知管理。 | [`mcp_server_cts.md`](./catalog/mcp_server_cts.md) | [`mcp_server_cts.json`](./catalog/mcp_server_cts.json) |
| `mcp_server_das` | DAS | 61 | 用于华为云 DAS 服务的资源查询与操作。 重点能力: 云DBA / 开发工具 / 查询版本操作。 | [`mcp_server_das.md`](./catalog/mcp_server_das.md) | [`mcp_server_das.json`](./catalog/mcp_server_das.json) |
| `mcp_server_dataartsfabric` | DataArtsFabric | 38 | 用于华为云 DataArtsFabric 服务的资源查询与操作。 重点能力: Agency / Agreement / ConfigCenter。 | [`mcp_server_dataartsfabric.md`](./catalog/mcp_server_dataartsfabric.md) | [`mcp_server_dataartsfabric.json`](./catalog/mcp_server_dataartsfabric.json) |
| `mcp_server_dataartsinsight` | DataArtsInsight | 33 | 用于华为云 DataArtsInsight 服务的资源查询与操作。 重点能力: 产品实例 / 仪表板大屏资源统一 / 协同授权。 | [`mcp_server_dataartsinsight.md`](./catalog/mcp_server_dataartsinsight.md) | [`mcp_server_dataartsinsight.json`](./catalog/mcp_server_dataartsinsight.json) |
| `mcp_server_dataartsstudio` | DataArtsStudio | 373 | 用于华为云 DataArtsStudio 服务的资源查询与操作。 重点能力: API管理接口 / 业务指标接口 / 业务资产接口。 | [`mcp_server_dataartsstudio.md`](./catalog/mcp_server_dataartsstudio.md) | [`mcp_server_dataartsstudio.json`](./catalog/mcp_server_dataartsstudio.json) |
| `mcp_server_dbss` | DBSS | 39 | 用于华为云 DBSS 服务的资源查询与操作。 重点能力: TMS标签 / 审计Agent / 审计实例。 | [`mcp_server_dbss.md`](./catalog/mcp_server_dbss.md) | [`mcp_server_dbss.json`](./catalog/mcp_server_dbss.json) |
| `mcp_server_dc` | DC | 53 | 用于华为云 DC 服务的资源查询与操作。 重点能力: BindingGlobalEip / ConnectGateway / DirectConnect。 | [`mcp_server_dc.md`](./catalog/mcp_server_dc.md) | [`mcp_server_dc.json`](./catalog/mcp_server_dc.json) |
| `mcp_server_dcs` | DCS | 137 | 用于华为云 DCS 服务的资源查询与操作。 重点能力: IP白名单管理 / 会话管理 / 其他接口。 | [`mcp_server_dcs.md`](./catalog/mcp_server_dcs.md) | [`mcp_server_dcs.json`](./catalog/mcp_server_dcs.json) |
| `mcp_server_ddm` | DDM | 56 | 用于华为云 DDM 服务的资源查询与操作。 重点能力: DDM会话管理 / DDM实例管理 / DDM帐号管理。 | [`mcp_server_ddm.md`](./catalog/mcp_server_ddm.md) | [`mcp_server_ddm.json`](./catalog/mcp_server_ddm.json) |
| `mcp_server_dds` | DDS | 123 | 用于华为云 DDS 服务的资源查询与操作。 重点能力: ITaskController / OpenStack - API版本信息 / Tags。 | [`mcp_server_dds.md`](./catalog/mcp_server_dds.md) | [`mcp_server_dds.json`](./catalog/mcp_server_dds.json) |
| `mcp_server_deh` | DeH | 12 | 用于华为云 DeH 服务的资源查询与操作。 重点能力: 查询API版本信息 / 标签管理 / 生命周期管理。 | [`mcp_server_deh.md`](./catalog/mcp_server_deh.md) | [`mcp_server_deh.json`](./catalog/mcp_server_deh.json) |
| `mcp_server_devsecurity` | DevSecurity | 4 | 用于华为云 DevSecurity 服务的资源查询与操作。 重点能力: secapp。 | [`mcp_server_devsecurity.md`](./catalog/mcp_server_devsecurity.md) | [`mcp_server_devsecurity.json`](./catalog/mcp_server_devsecurity.json) |
| `mcp_server_dgc` | DGC | 38 | 用于华为云 DGC 服务的资源查询与操作。 重点能力: Job管理 / Resource / 任务中心API。 | [`mcp_server_dgc.md`](./catalog/mcp_server_dgc.md) | [`mcp_server_dgc.json`](./catalog/mcp_server_dgc.json) |
| `mcp_server_dis` | DIS | 38 | 用于华为云 DIS 服务的资源查询与操作。 重点能力: AppManagement / App管理 / Checkpoint管理。 | [`mcp_server_dis.md`](./catalog/mcp_server_dis.md) | [`mcp_server_dis.json`](./catalog/mcp_server_dis.json) |
| `mcp_server_dlf` | DLF | 39 | 用于华为云 DLF 服务的资源查询与操作。 重点能力: Job管理 / Resource / 任务中心API。 | [`mcp_server_dlf.md`](./catalog/mcp_server_dlf.md) | [`mcp_server_dlf.json`](./catalog/mcp_server_dlf.json) |
| `mcp_server_dli` | DLI | 160 | 用于华为云 DLI 服务的资源查询与操作。 重点能力: Flink作业-作业相关API / Flink作业-模板相关API / Flink作业-管理相关API。 | [`mcp_server_dli.md`](./catalog/mcp_server_dli.md) | [`mcp_server_dli.json`](./catalog/mcp_server_dli.json) |
| `mcp_server_dns` | DNS | 87 | 用于华为云 DNS 服务的资源查询与操作。 重点能力: DNSSEC / 公网域名管理 / 内网域名管理。 | [`mcp_server_dns.md`](./catalog/mcp_server_dns.md) | [`mcp_server_dns.json`](./catalog/mcp_server_dns.json) |
| `mcp_server_dris` | DRIS | 58 | 用于华为云 DRIS 服务的资源查询与操作。 重点能力: APIG-SN-DATACHANNEL / APIG-SN-EDGE / APIG-SN-ForwardingConfigResources。 | [`mcp_server_dris.md`](./catalog/mcp_server_dris.md) | [`mcp_server_dris.json`](./catalog/mcp_server_dris.json) |
| `mcp_server_drs` | DRS | 143 | 用于华为云 DRS 服务的资源查询与操作。 重点能力: Tags / 任务中心API / 任务管理。 | [`mcp_server_drs.md`](./catalog/mcp_server_drs.md) | [`mcp_server_drs.json`](./catalog/mcp_server_drs.json) |
| `mcp_server_dsc` | DSC | 35 | 用于华为云 DSC 服务的资源查询与操作。 重点能力: API调用记录 / 告警通知 / 图片水印。 | [`mcp_server_dsc.md`](./catalog/mcp_server_dsc.md) | [`mcp_server_dsc.json`](./catalog/mcp_server_dsc.json) |
| `mcp_server_dss` | DSS | 4 | 用于华为云 DSS 服务的资源查询与操作。 重点能力: 后端云服务器组 / 查询密钥API版本信息 / 查询版本操作。 | [`mcp_server_dss.md`](./catalog/mcp_server_dss.md) | [`mcp_server_dss.json`](./catalog/mcp_server_dss.json) |
| `mcp_server_dws` | DWS | 195 | 用于华为云 DWS 服务的资源查询与操作。 重点能力: ClusterManagement / Query / VpnGateway。 | [`mcp_server_dws.md`](./catalog/mcp_server_dws.md) | [`mcp_server_dws.json`](./catalog/mcp_server_dws.json) |
| `mcp_server_ec` | EC | 54 | 用于华为云 EC 服务的资源查询与操作。 重点能力: EcnAccessPoint / EnterpriseConnectNetwork / Equipment。 | [`mcp_server_ec.md`](./catalog/mcp_server_ec.md) | [`mcp_server_ec.json`](./catalog/mcp_server_ec.json) |
| `mcp_server_ecs` | ECS | 106 | 用于华为云 ECS 服务的资源查询与操作。 重点能力: 云服务器操作管理 / 云服务器组管理 / 元数据管理。 | [`mcp_server_ecs.md`](./catalog/mcp_server_ecs.md) | [`mcp_server_ecs.json`](./catalog/mcp_server_ecs.json) |
| `mcp_server_eds` | EDS | 11 | 用于华为云 EDS 服务的资源查询与操作。 重点能力: offer / user / 合约。 | [`mcp_server_eds.md`](./catalog/mcp_server_eds.md) | [`mcp_server_eds.json`](./catalog/mcp_server_eds.json) |
| `mcp_server_eg` | EG | 65 | 用于华为云 EG 服务的资源查询与操作。 重点能力: obs桶管理 / 事件模型管理 / 事件流管理。 | [`mcp_server_eg.md`](./catalog/mcp_server_eg.md) | [`mcp_server_eg.json`](./catalog/mcp_server_eg.json) |
| `mcp_server_eihealth` | eiHealth | 353 | 用于华为云 eiHealth 服务的资源查询与操作。 重点能力: ADMET / CPI / CPI作业管理。 | [`mcp_server_eihealth.md`](./catalog/mcp_server_eihealth.md) | [`mcp_server_eihealth.json`](./catalog/mcp_server_eihealth.json) |
| `mcp_server_eip` | EIP | 61 | 用于华为云 EIP 服务的资源查询与操作。 重点能力: GEIP与实例的绑定关系 / OpenStack - 浮动IP / 公共池。 | [`mcp_server_eip.md`](./catalog/mcp_server_eip.md) | [`mcp_server_eip.json`](./catalog/mcp_server_eip.json) |
| `mcp_server_elb` | ELB | 122 | 用于华为云 ELB 服务的资源查询与操作。 重点能力: IP地址组 / VpnGateway / 主备后端服务器组。 | [`mcp_server_elb.md`](./catalog/mcp_server_elb.md) | [`mcp_server_elb.json`](./catalog/mcp_server_elb.json) |
| `mcp_server_eps` | EPS | 12 | 用于华为云 EPS 服务的资源查询与操作。 重点能力: 企业项目管理操作 / 查询标签管理支持的服务 / 查询版本操作。 | [`mcp_server_eps.md`](./catalog/mcp_server_eps.md) | [`mcp_server_eps.json`](./catalog/mcp_server_eps.json) |
| `mcp_server_er` | ER | 47 | 用于华为云 ER 服务的资源查询与操作。 重点能力: Association / Attachments / AvailableZone。 | [`mcp_server_er.md`](./catalog/mcp_server_er.md) | [`mcp_server_er.json`](./catalog/mcp_server_er.json) |
| `mcp_server_evs` | EVS | 31 | 用于华为云 EVS 服务的资源查询与操作。 重点能力: 云硬盘 / 云硬盘快照 / 云硬盘标签。 | [`mcp_server_evs.md`](./catalog/mcp_server_evs.md) | [`mcp_server_evs.json`](./catalog/mcp_server_evs.json) |
| `mcp_server_frs` | FRS | 29 | 用于华为云 FRS 服务的资源查询与操作。 重点能力: 人脸库资源管理 / 人脸搜索 / 人脸检测。 | [`mcp_server_frs.md`](./catalog/mcp_server_frs.md) | [`mcp_server_frs.json`](./catalog/mcp_server_frs.json) |
| `mcp_server_functiongraph` | FunctionGraph | 92 | 用于华为云 FunctionGraph 服务的资源查询与操作。 重点能力: 函数依赖包 / 函数导入导出 / 函数应用中心。 | [`mcp_server_functiongraph.md`](./catalog/mcp_server_functiongraph.md) | [`mcp_server_functiongraph.json`](./catalog/mcp_server_functiongraph.json) |
| `mcp_server_gaussdb` | GaussDB | 212 | 用于华为云 GaussDB 服务的资源查询与操作。 重点能力: HTAP-标准版 / HTAP-轻量版 / 任务中心。 | [`mcp_server_gaussdb.md`](./catalog/mcp_server_gaussdb.md) | [`mcp_server_gaussdb.json`](./catalog/mcp_server_gaussdb.json) |
| `mcp_server_gaussdbfornosql` | GaussDBforNoSQL | 145 | 用于华为云 GaussDBforNoSQL 服务的资源查询与操作。 重点能力: 任务管理 / 企业项目管理 / 参数模板管理。 | [`mcp_server_gaussdbfornosql.md`](./catalog/mcp_server_gaussdbfornosql.md) | [`mcp_server_gaussdbfornosql.json`](./catalog/mcp_server_gaussdbfornosql.json) |
| `mcp_server_gaussdbforopengauss` | GaussDBforopenGauss | 145 | 用于华为云 GaussDBforopenGauss 服务的资源查询与操作。 重点能力: ITaskController / SQL限流 / Tags。 | [`mcp_server_gaussdbforopengauss.md`](./catalog/mcp_server_gaussdbforopengauss.md) | [`mcp_server_gaussdbforopengauss.json`](./catalog/mcp_server_gaussdbforopengauss.json) |
| `mcp_server_geip` | GEIP | 66 | 用于华为云 GEIP 服务的资源查询与操作。 重点能力: Job相关接口 / Region限制 / 任务中心API。 | [`mcp_server_geip.md`](./catalog/mcp_server_geip.md) | [`mcp_server_geip.json`](./catalog/mcp_server_geip.json) |
| `mcp_server_ges` | GES | 61 | 用于华为云 GES 服务的资源查询与操作。 重点能力: GraphPlugins管理API / 任务中心API / 元数据管理API。 | [`mcp_server_ges.md`](./catalog/mcp_server_ges.md) | [`mcp_server_ges.json`](./catalog/mcp_server_ges.json) |
| `mcp_server_gsl` | GSL | 39 | 用于华为云 GSL 服务的资源查询与操作。 重点能力: Attribute / BackPool / NetworkSwitchPolicies。 | [`mcp_server_gsl.md`](./catalog/mcp_server_gsl.md) | [`mcp_server_gsl.json`](./catalog/mcp_server_gsl.json) |
| `mcp_server_hilens` | HiLens | 58 | 用于华为云 HiLens 服务的资源查询与操作。 重点能力: 作业管理 / 固件管理 / 密钥管理。 | [`mcp_server_hilens.md`](./catalog/mcp_server_hilens.md) | [`mcp_server_hilens.json`](./catalog/mcp_server_hilens.json) |
| `mcp_server_hss` | HSS | 237 | 用于华为云 HSS 服务的资源查询与操作。 重点能力: Tags / 主机安装与配置 / 主机管理。 | [`mcp_server_hss.md`](./catalog/mcp_server_hss.md) | [`mcp_server_hss.json`](./catalog/mcp_server_hss.json) |
| `mcp_server_iam` | IAM | 152 | 用于华为云 IAM 服务的资源查询与操作。 重点能力: AccountSummary / Credential管理 / IAM用户管理。 | [`mcp_server_iam.md`](./catalog/mcp_server_iam.md) | [`mcp_server_iam.json`](./catalog/mcp_server_iam.json) |
| `mcp_server_identitycenter` | IdentityCenter | 37 | 用于华为云 IdentityCenter 服务的资源查询与操作。 重点能力: AccountAssignment / Instance / InstanceAccessControlAttributeConfiguration。 | [`mcp_server_identitycenter.md`](./catalog/mcp_server_identitycenter.md) | [`mcp_server_identitycenter.json`](./catalog/mcp_server_identitycenter.json) |
| `mcp_server_identitycenteroidc` | IdentityCenterOIDC | 3 | 用于华为云 IdentityCenterOIDC 服务的资源查询与操作。 重点能力: Client / DeviceAuthorization / Token。 | [`mcp_server_identitycenteroidc.md`](./catalog/mcp_server_identitycenteroidc.md) | [`mcp_server_identitycenteroidc.json`](./catalog/mcp_server_identitycenteroidc.json) |
| `mcp_server_identitycenterportalapi` | IdentityCenterPortalAPI | 4 | 用于华为云 IdentityCenterPortalAPI 服务的资源查询与操作。 重点能力: Account / Agency / Credential。 | [`mcp_server_identitycenterportalapi.md`](./catalog/mcp_server_identitycenterportalapi.md) | [`mcp_server_identitycenterportalapi.json`](./catalog/mcp_server_identitycenterportalapi.json) |
| `mcp_server_identitycenterscim` | IdentityCenterSCIM | 12 | 用于华为云 IdentityCenterSCIM 服务的资源查询与操作。 重点能力: Group / ServiceProviderConfig / User。 | [`mcp_server_identitycenterscim.md`](./catalog/mcp_server_identitycenterscim.md) | [`mcp_server_identitycenterscim.json`](./catalog/mcp_server_identitycenterscim.json) |
| `mcp_server_identitycenterstore` | IdentityCenterStore | 19 | 用于华为云 IdentityCenterStore 服务的资源查询与操作。 重点能力: Group / GroupMembership / User。 | [`mcp_server_identitycenterstore.md`](./catalog/mcp_server_identitycenterstore.md) | [`mcp_server_identitycenterstore.json`](./catalog/mcp_server_identitycenterstore.json) |
| `mcp_server_idme` | iDME | 9 | 用于华为云 iDME 服务的资源查询与操作。 重点能力: 应用管理 / 运行服务管理。 | [`mcp_server_idme.md`](./catalog/mcp_server_idme.md) | [`mcp_server_idme.json`](./catalog/mcp_server_idme.json) |
| `mcp_server_idmeclassicapi` | iDMEClassicAPI | 91 | 用于华为云 iDMEClassicAPI 服务的资源查询与操作。 重点能力: 业务编码生成器 / 关系实体服务 / 基础数据服务。 | [`mcp_server_idmeclassicapi.md`](./catalog/mcp_server_idmeclassicapi.md) | [`mcp_server_idmeclassicapi.json`](./catalog/mcp_server_idmeclassicapi.json) |
| `mcp_server_idt` | IDT | 930 | 用于华为云 IDT 服务的资源查询与操作。 重点能力: Linkx同步任务 / XDM基线对象 / XDM权限属性。 | [`mcp_server_idt.md`](./catalog/mcp_server_idt.md) | [`mcp_server_idt.json`](./catalog/mcp_server_idt.json) |
| `mcp_server_iec` | IEC | 89 | 用于华为云 IEC 服务的资源查询与操作。 重点能力: Misc / VPC / port。 | [`mcp_server_iec.md`](./catalog/mcp_server_iec.md) | [`mcp_server_iec.json`](./catalog/mcp_server_iec.json) |
| `mcp_server_ief` | IEF | 110 | 用于华为云 IEF 服务的资源查询与操作。 重点能力: AppManagement / IAlgorithmController / 临时登录指令。 | [`mcp_server_ief.md`](./catalog/mcp_server_ief.md) | [`mcp_server_ief.json`](./catalog/mcp_server_ief.json) |
| `mcp_server_ies` | IES | 12 | 用于华为云 IES 服务的资源查询与操作。 重点能力: edge-site / monitor / quota。 | [`mcp_server_ies.md`](./catalog/mcp_server_ies.md) | [`mcp_server_ies.json`](./catalog/mcp_server_ies.json) |
| `mcp_server_image` | Image | 6 | 用于华为云 Image 服务的资源查询与操作。 重点能力: 主体识别 / 名人识别 / 图像标签。 | [`mcp_server_image.md`](./catalog/mcp_server_image.md) | [`mcp_server_image.json`](./catalog/mcp_server_image.json) |
| `mcp_server_imagesearch` | ImageSearch | 5 | 用于华为云 ImageSearch 服务的资源查询与操作。 重点能力: 删除数据 / 搜索 / 更新数据。 | [`mcp_server_imagesearch.md`](./catalog/mcp_server_imagesearch.md) | [`mcp_server_imagesearch.json`](./catalog/mcp_server_imagesearch.json) |
| `mcp_server_ims` | IMS | 46 | 用于华为云 IMS 服务的资源查询与操作。 重点能力: 查询密钥API版本信息 / 查询版本操作 / 标签管理。 | [`mcp_server_ims.md`](./catalog/mcp_server_ims.md) | [`mcp_server_ims.json`](./catalog/mcp_server_ims.json) |
| `mcp_server_iotanalytics` | IoTAnalytics | 66 | 用于华为云 IoTAnalytics 服务的资源查询与操作。 重点能力: AssetModel / AssetNew / AssetProperty。 | [`mcp_server_iotanalytics.md`](./catalog/mcp_server_iotanalytics.md) | [`mcp_server_iotanalytics.json`](./catalog/mcp_server_iotanalytics.json) |
| `mcp_server_iotda` | IoTDA | 131 | 用于华为云 IoTDA 服务的资源查询与操作。 重点能力: AccessCodeManagement / AmqpQueueManagement / ApplicationManagement。 | [`mcp_server_iotda.md`](./catalog/mcp_server_iotda.md) | [`mcp_server_iotda.json`](./catalog/mcp_server_iotda.json) |
| `mcp_server_iotdm` | IoTDM | 9 | 用于华为云 IoTDM 服务的资源查询与操作。 重点能力: InstanceManagement。 | [`mcp_server_iotdm.md`](./catalog/mcp_server_iotdm.md) | [`mcp_server_iotdm.json`](./catalog/mcp_server_iotdm.json) |
| `mcp_server_iotedge` | IoTEdge | 107 | 用于华为云 IoTEdge 服务的资源查询与操作。 重点能力: App / AppInstance / AppVersion。 | [`mcp_server_iotedge.md`](./catalog/mcp_server_iotedge.md) | [`mcp_server_iotedge.json`](./catalog/mcp_server_iotedge.json) |
| `mcp_server_ivs` | IVS | 6 | 用于华为云 IVS 服务的资源查询与操作。 重点能力: 人证核身标准版(三要素) / 人证核身证件版(二要素)。 | [`mcp_server_ivs.md`](./catalog/mcp_server_ivs.md) | [`mcp_server_ivs.json`](./catalog/mcp_server_ivs.json) |
| `mcp_server_kafka` | Kafka | 95 | 用于华为云 Kafka 服务的资源查询与操作。 重点能力: Smart Connect / 主题管理 / 其他接口。 | [`mcp_server_kafka.md`](./catalog/mcp_server_kafka.md) | [`mcp_server_kafka.json`](./catalog/mcp_server_kafka.json) |
| `mcp_server_kms` | KMS | 58 | 用于华为云 KMS 服务的资源查询与操作。 重点能力: 专属密钥库管理 / 别名管理 / 多区域密钥。 | [`mcp_server_kms.md`](./catalog/mcp_server_kms.md) | [`mcp_server_kms.json`](./catalog/mcp_server_kms.json) |
| `mcp_server_koomap` | KooMap | 40 | 用于华为云 KooMap 服务的资源查询与操作。 重点能力: 卫星影像任务管理 / 卫星影像数据管理 / 卫星影像用量统计。 | [`mcp_server_koomap.md`](./catalog/mcp_server_koomap.md) | [`mcp_server_koomap.json`](./catalog/mcp_server_koomap.json) |
| `mcp_server_koomessage` | KooMessage | 62 | 用于华为云 KooMessage 服务的资源查询与操作。 重点能力: AIMCallBack / AIMResolveTask / AIMSendTask。 | [`mcp_server_koomessage.md`](./catalog/mcp_server_koomessage.md) | [`mcp_server_koomessage.json`](./catalog/mcp_server_koomessage.json) |
| `mcp_server_koophone` | KooPhone | 12 | 用于华为云 KooPhone 服务的资源查询与操作。 重点能力: 实例管理 / 实例订购。 | [`mcp_server_koophone.md`](./catalog/mcp_server_koophone.md) | [`mcp_server_koophone.json`](./catalog/mcp_server_koophone.json) |
| `mcp_server_kps` | KPS | 18 | 用于华为云 KPS 服务的资源查询与操作。 重点能力: 密钥对任务管理 / 密钥对管理。 | [`mcp_server_kps.md`](./catalog/mcp_server_kps.md) | [`mcp_server_kps.json`](./catalog/mcp_server_kps.json) |
| `mcp_server_kvs` | KVS | 13 | 用于华为云 KVS 服务的资源查询与操作。 重点能力: KV接口 / 仓接口 / 表接口。 | [`mcp_server_kvs.md`](./catalog/mcp_server_kvs.md) | [`mcp_server_kvs.json`](./catalog/mcp_server_kvs.json) |
| `mcp_server_lakeformation` | LakeFormation | 94 | 用于华为云 LakeFormation 服务的资源查询与操作。 重点能力: Access / Agency / Catalog。 | [`mcp_server_lakeformation.md`](./catalog/mcp_server_lakeformation.md) | [`mcp_server_lakeformation.json`](./catalog/mcp_server_lakeformation.json) |
| `mcp_server_live` | Live | 94 | 用于华为云 Live 服务的资源查询与操作。 重点能力: DataStatisticsAnalysis / HTTPS证书管理 / OBS桶管理。 | [`mcp_server_live.md`](./catalog/mcp_server_live.md) | [`mcp_server_live.json`](./catalog/mcp_server_live.json) |
| `mcp_server_lts` | LTS | 92 | 用于华为云 LTS 服务的资源查询与操作。 重点能力: AOM容器日志接入LTS / SDK流式消费开放API / SQL告警规则。 | [`mcp_server_lts.md`](./catalog/mcp_server_lts.md) | [`mcp_server_lts.json`](./catalog/mcp_server_lts.json) |
| `mcp_server_mapds` | MapDS | 5 | 用于华为云 MapDS 服务的资源查询与操作。 重点能力: 凭证管理 / 获取地图瓦片。 | [`mcp_server_mapds.md`](./catalog/mcp_server_mapds.md) | [`mcp_server_mapds.json`](./catalog/mcp_server_mapds.json) |
| `mcp_server_mas` | MAS | 53 | 用于华为云 MAS 服务的资源查询与操作。 重点能力: Application操作 / ETCD证书 / 全局配置。 | [`mcp_server_mas.md`](./catalog/mcp_server_mas.md) | [`mcp_server_mas.json`](./catalog/mcp_server_mas.json) |
| `mcp_server_meeting` | Meeting | 202 | 用于华为云 Meeting 服务的资源查询与操作。 重点能力: OpenQosMetrics / OpenStatisticMetrics / 云会议室管理。 | [`mcp_server_meeting.md`](./catalog/mcp_server_meeting.md) | [`mcp_server_meeting.json`](./catalog/mcp_server_meeting.json) |
| `mcp_server_metastudio` | MetaStudio | 197 | 用于华为云 MetaStudio 服务的资源查询与操作。 重点能力: ActiveCodeManagement / AgencyManagement / AsrVocabularyManagement。 | [`mcp_server_metastudio.md`](./catalog/mcp_server_metastudio.md) | [`mcp_server_metastudio.json`](./catalog/mcp_server_metastudio.json) |
| `mcp_server_modelarts` | ModelArts | 5 | 用于华为云 ModelArts 服务的资源查询与操作。 重点能力: AI应用管理 / APP认证管理 / DevServer管理。 | [`mcp_server_modelarts.md`](./catalog/mcp_server_modelarts.md) | [`mcp_server_modelarts.json`](./catalog/mcp_server_modelarts.json) |
| `mcp_server_moderation` | Moderation | 9 | 用于华为云 Moderation 服务的资源查询与操作。 重点能力: 图像内容审核 / 图像审核批量同步接口 / 文本内容审核。 | [`mcp_server_moderation.md`](./catalog/mcp_server_moderation.md) | [`mcp_server_moderation.json`](./catalog/mcp_server_moderation.json) |
| `mcp_server_mpc` | MPC | 44 | 用于华为云 MPC 服务的资源查询与操作。 重点能力: AnimatedGraphicsTaskManager / AuthorizationAndConfiguration / EncryptManager。 | [`mcp_server_mpc.md`](./catalog/mcp_server_mpc.md) | [`mcp_server_mpc.json`](./catalog/mcp_server_mpc.json) |
| `mcp_server_mrs` | MRS | 50 | 用于华为云 MRS 服务的资源查询与操作。 重点能力: ClusterManagement / DataConnectorManagement / IAMSyncManagement。 | [`mcp_server_mrs.md`](./catalog/mcp_server_mrs.md) | [`mcp_server_mrs.json`](./catalog/mcp_server_mrs.json) |
| `mcp_server_msgsms` | MSGSMS | 20 | 用于华为云 MSGSMS 服务的资源查询与操作。 重点能力: AppManagement / SignatureManagement / TemplateManagement。 | [`mcp_server_msgsms.md`](./catalog/mcp_server_msgsms.md) | [`mcp_server_msgsms.json`](./catalog/mcp_server_msgsms.json) |
| `mcp_server_mss` | MSS | 12 | 用于华为云 MSS 服务的资源查询与操作。 | N/A | [`mcp_server_mss.json`](./catalog/mcp_server_mss.json) |
| `mcp_server_mssi` | MSSI | 16 | 用于华为云 MSSI 服务的资源查询与操作。 重点能力: 流 / 流模板 / 连接。 | [`mcp_server_mssi.md`](./catalog/mcp_server_mssi.md) | [`mcp_server_mssi.json`](./catalog/mcp_server_mssi.json) |
| `mcp_server_nat` | NAT | 53 | 用于华为云 NAT 服务的资源查询与操作。 重点能力: 中转IP标签管理 / 公网DNAT规则 / 公网NAT网关。 | [`mcp_server_nat.md`](./catalog/mcp_server_nat.md) | [`mcp_server_nat.json`](./catalog/mcp_server_nat.json) |
| `mcp_server_nlp` | NLP | 27 | 用于华为云 NLP 服务的资源查询与操作。 重点能力: 机器翻译服务 / 自然语言处理基础服务 / 语言理解服务。 | [`mcp_server_nlp.md`](./catalog/mcp_server_nlp.md) | [`mcp_server_nlp.json`](./catalog/mcp_server_nlp.json) |
| `mcp_server_obs` | OBS | 81 | 用于华为云 OBS 服务的资源查询与操作。 重点能力: 多段操作 / 对象操作 / 查询版本操作。 | [`mcp_server_obs.md`](./catalog/mcp_server_obs.md) | [`mcp_server_obs.json`](./catalog/mcp_server_obs.json) |
| `mcp_server_ocr` | OCR | 38 | 用于华为云 OCR 服务的资源查询与操作。 重点能力: VIN码识别 / 不动产证识别 / 保险单识别。 | [`mcp_server_ocr.md`](./catalog/mcp_server_ocr.md) | [`mcp_server_ocr.json`](./catalog/mcp_server_ocr.json) |
| `mcp_server_ocv2x` | ocv2x | 4 | 用于华为云 ocv2x 服务的资源查询与操作。 重点能力: APIG-SN-DataAgingConfig / APIG-SN-HistoryTrafficEvents / APIG-SN-VehicleHistory。 | [`mcp_server_ocv2x.md`](./catalog/mcp_server_ocv2x.md) | [`mcp_server_ocv2x.json`](./catalog/mcp_server_ocv2x.json) |
| `mcp_server_oms` | OMS | 33 | 用于华为云 OMS 服务的资源查询与操作。 重点能力: ITaskController / 云服务 / 区域。 | [`mcp_server_oms.md`](./catalog/mcp_server_oms.md) | [`mcp_server_oms.json`](./catalog/mcp_server_oms.json) |
| `mcp_server_optverse` | OptVerse | 4 | 用于华为云 OptVerse 服务的资源查询与操作。 重点能力: OptVerse Service。 | [`mcp_server_optverse.md`](./catalog/mcp_server_optverse.md) | [`mcp_server_optverse.json`](./catalog/mcp_server_optverse.json) |
| `mcp_server_organizations` | Organizations | 58 | 用于华为云 Organizations 服务的资源查询与操作。 重点能力: Account / DelegatedAdministrator / Handshake。 | [`mcp_server_organizations.md`](./catalog/mcp_server_organizations.md) | [`mcp_server_organizations.json`](./catalog/mcp_server_organizations.json) |
| `mcp_server_orgid` | OrgID | 3 | 用于华为云 OrgID 服务的资源查询与操作。 重点能力: Cas30Service / OAUTH。 | [`mcp_server_orgid.md`](./catalog/mcp_server_orgid.md) | [`mcp_server_orgid.json`](./catalog/mcp_server_orgid.json) |
| `mcp_server_oroas` | OROAS | 4 | 用于华为云 OROAS 服务的资源查询与操作。 重点能力: ITaskController / OROAS Service / 服务作业管理。 | [`mcp_server_oroas.md`](./catalog/mcp_server_oroas.md) | [`mcp_server_oroas.json`](./catalog/mcp_server_oroas.json) |
| `mcp_server_pangulargemodels` | PanguLargeModels | 2 | 用于华为云 PanguLargeModels 服务的资源查询与操作。 重点能力: Completions。 | [`mcp_server_pangulargemodels.md`](./catalog/mcp_server_pangulargemodels.md) | [`mcp_server_pangulargemodels.json`](./catalog/mcp_server_pangulargemodels.json) |
| `mcp_server_projectman` | ProjectMan | 77 | 用于华为云 ProjectMan 服务的资源查询与操作。 重点能力: Scrum项目的工作项 / Scrum项目的模块 / Scrum项目的状态。 | [`mcp_server_projectman.md`](./catalog/mcp_server_projectman.md) | [`mcp_server_projectman.json`](./catalog/mcp_server_projectman.json) |
| `mcp_server_rabbitmq` | RabbitMQ | 41 | 用于华为云 RabbitMQ 服务的资源查询与操作。 重点能力: Binding管理 / Exchange管理 / Queue管理。 | [`mcp_server_rabbitmq.md`](./catalog/mcp_server_rabbitmq.md) | [`mcp_server_rabbitmq.json`](./catalog/mcp_server_rabbitmq.json) |
| `mcp_server_ram` | RAM | 28 | 用于华为云 RAM 服务的资源查询与操作。 重点能力: AssociatedPermission / Misc / OrganizationSharing。 | [`mcp_server_ram.md`](./catalog/mcp_server_ram.md) | [`mcp_server_ram.json`](./catalog/mcp_server_ram.json) |
| `mcp_server_rds` | RDS | 232 | 用于华为云 RDS 服务的资源查询与操作。 重点能力: OpenStack - API版本信息 / Tags / 任务管理。 | [`mcp_server_rds.md`](./catalog/mcp_server_rds.md) | [`mcp_server_rds.json`](./catalog/mcp_server_rds.json) |
| `mcp_server_res` | RES | 33 | 用于华为云 RES 服务的资源查询与操作。 重点能力: 在线服务 / 场景 / 工作空间。 | [`mcp_server_res.md`](./catalog/mcp_server_res.md) | [`mcp_server_res.json`](./catalog/mcp_server_res.json) |
| `mcp_server_rgc` | RGC | 9 | 用于华为云 RGC 服务的资源查询与操作。 重点能力: Governance / ManagedOrganization。 | [`mcp_server_rgc.md`](./catalog/mcp_server_rgc.md) | [`mcp_server_rgc.json`](./catalog/mcp_server_rgc.json) |
| `mcp_server_rms` | RMS | 62 | 用于华为云 RMS 服务的资源查询与操作。 重点能力: Aggregator / History / Policy。 | [`mcp_server_rms.md`](./catalog/mcp_server_rms.md) | [`mcp_server_rms.json`](./catalog/mcp_server_rms.json) |
| `mcp_server_rocketmq` | RocketMQ | 51 | 用于华为云 RocketMQ 服务的资源查询与操作。 重点能力: Topic管理 / 主题操作 / 元数据迁移。 | [`mcp_server_rocketmq.md`](./catalog/mcp_server_rocketmq.md) | [`mcp_server_rocketmq.json`](./catalog/mcp_server_rocketmq.json) |
| `mcp_server_roma` | ROMA | 320 | 用于华为云 ROMA 服务的资源查询与操作。 重点能力: ACL策略管理 / API分组管理 / API管理。 | [`mcp_server_roma.md`](./catalog/mcp_server_roma.md) | [`mcp_server_roma.json`](./catalog/mcp_server_roma.json) |
| `mcp_server_sa` | SA | 61 | 用于华为云 SA 服务的资源查询与操作。 重点能力: AlertRules / Alerts / Incidents。 | [`mcp_server_sa.md`](./catalog/mcp_server_sa.md) | [`mcp_server_sa.json`](./catalog/mcp_server_sa.json) |
| `mcp_server_scm` | SCM | 25 | 用于华为云 SCM 服务的资源查询与操作。 重点能力: CSR管理 / 证书标签管理 / 证书生命周期管理。 | [`mcp_server_scm.md`](./catalog/mcp_server_scm.md) | [`mcp_server_scm.json`](./catalog/mcp_server_scm.json) |
| `mcp_server_sdrs` | SDRS | 49 | 用于华为云 SDRS 服务的资源查询与操作。 重点能力: API版本信息 / Job管理 / 任务中心。 | [`mcp_server_sdrs.md`](./catalog/mcp_server_sdrs.md) | [`mcp_server_sdrs.json`](./catalog/mcp_server_sdrs.json) |
| `mcp_server_secmaster` | SecMaster | 72 | 用于华为云 SecMaster 服务的资源查询与操作。 重点能力: 事件关系管理 / 事件管理 / 剧本动作管理。 | [`mcp_server_secmaster.md`](./catalog/mcp_server_secmaster.md) | [`mcp_server_secmaster.json`](./catalog/mcp_server_secmaster.json) |
| `mcp_server_servicestage` | ServiceStage | 77 | 用于华为云 ServiceStage 服务的资源查询与操作。 重点能力: Application / Component / Environment。 | [`mcp_server_servicestage.md`](./catalog/mcp_server_servicestage.md) | [`mcp_server_servicestage.json`](./catalog/mcp_server_servicestage.json) |
| `mcp_server_sfsturbo` | SFSTurbo | 47 | 用于华为云 SFSTurbo 服务的资源查询与操作。 重点能力: 任务管理 / 共享标签 / 名称管理。 | [`mcp_server_sfsturbo.md`](./catalog/mcp_server_sfsturbo.md) | [`mcp_server_sfsturbo.json`](./catalog/mcp_server_sfsturbo.json) |
| `mcp_server_sis` | SIS | 10 | 用于华为云 SIS 服务的资源查询与操作。 重点能力: 热词管理接口 / 语音合成接口 / 语音识别接口。 | [`mcp_server_sis.md`](./catalog/mcp_server_sis.md) | [`mcp_server_sis.json`](./catalog/mcp_server_sis.json) |
| `mcp_server_smn` | SMN | 53 | 用于华为云 SMN 服务的资源查询与操作。 重点能力: Application endpoint操作 / Application操作 / Application直发消息操作。 | [`mcp_server_smn.md`](./catalog/mcp_server_smn.md) | [`mcp_server_smn.json`](./catalog/mcp_server_smn.json) |
| `mcp_server_smnglobal` | SMNGLOBAL | 4 | 用于华为云 SMNGLOBAL 服务的资源查询与操作。 重点能力: 订阅用户。 | [`mcp_server_smnglobal.md`](./catalog/mcp_server_smnglobal.md) | [`mcp_server_smnglobal.json`](./catalog/mcp_server_smnglobal.json) |
| `mcp_server_smsapi` | SMSApi | 2 | 用于华为云 SMSApi 服务的资源查询与操作。 重点能力: 短信能力开放。 | [`mcp_server_smsapi.md`](./catalog/mcp_server_smsapi.md) | [`mcp_server_smsapi.json`](./catalog/mcp_server_smsapi.json) |
| `mcp_server_sts` | STS | 2 | 用于华为云 STS 服务的资源查询与操作。 重点能力: AuthorizationResult / Caller。 | [`mcp_server_sts.md`](./catalog/mcp_server_sts.md) | [`mcp_server_sts.json`](./catalog/mcp_server_sts.json) |
| `mcp_server_swr` | SWR | 50 | 用于华为云 SWR 服务的资源查询与操作。 重点能力: 临时登录指令 / 共享帐号管理 / 其他。 | [`mcp_server_swr.md`](./catalog/mcp_server_swr.md) | [`mcp_server_swr.json`](./catalog/mcp_server_swr.json) |
| `mcp_server_tics` | TICS | 19 | 用于华为云 TICS 服务的资源查询与操作。 重点能力: 作业实例管理 / 可信节点管理 / 审计日志管理。 | [`mcp_server_tics.md`](./catalog/mcp_server_tics.md) | [`mcp_server_tics.json`](./catalog/mcp_server_tics.json) |
| `mcp_server_tms` | TMS | 14 | 用于华为云 TMS 服务的资源查询与操作。 重点能力: 查询标签管理支持的服务 / 查询版本操作 / 资源标签。 | [`mcp_server_tms.md`](./catalog/mcp_server_tms.md) | [`mcp_server_tms.json`](./catalog/mcp_server_tms.json) |
| `mcp_server_vas` | VAS | 7 | 用于华为云 VAS 服务的资源查询与操作。 重点能力: ITaskController / 服务作业管理。 | [`mcp_server_vas.md`](./catalog/mcp_server_vas.md) | [`mcp_server_vas.json`](./catalog/mcp_server_vas.json) |
| `mcp_server_vcm` | VCM | 8 | 用于华为云 VCM 服务的资源查询与操作。 重点能力: 视频内容审核 / 长语音内容审核。 | [`mcp_server_vcm.md`](./catalog/mcp_server_vcm.md) | [`mcp_server_vcm.json`](./catalog/mcp_server_vcm.json) |
| `mcp_server_vias` | VIAS | 29 | 用于华为云 VIAS 服务的资源查询与操作。 重点能力: IAlgorithmController / IBatchTaskController / IEdgePoolController。 | [`mcp_server_vias.md`](./catalog/mcp_server_vias.md) | [`mcp_server_vias.json`](./catalog/mcp_server_vias.json) |
| `mcp_server_vis` | VIS | 33 | 用于华为云 VIS 服务的资源查询与操作。 重点能力: obs桶策略管理 / 凭证管理 / 服务开通管理。 | [`mcp_server_vis.md`](./catalog/mcp_server_vis.md) | [`mcp_server_vis.json`](./catalog/mcp_server_vis.json) |
| `mcp_server_vod` | VOD | 62 | 用于华为云 VOD 服务的资源查询与操作。 重点能力: OBS托管管理 / 媒资上传 / 媒资分类。 | [`mcp_server_vod.md`](./catalog/mcp_server_vod.md) | [`mcp_server_vod.json`](./catalog/mcp_server_vod.json) |
| `mcp_server_vpc` | VPC | 184 | 用于华为云 VPC 服务的资源查询与操作。 重点能力: IP地址组 / OpenStack - API版本信息 / OpenStack - 子网。 | [`mcp_server_vpc.md`](./catalog/mcp_server_vpc.md) | [`mcp_server_vpc.json`](./catalog/mcp_server_vpc.json) |
| `mcp_server_vpcep` | VPCEP | 31 | 用于华为云 VPCEP 服务的资源查询与操作。 重点能力: TAG功能 / 版本管理 / 终端节点功能。 | [`mcp_server_vpcep.md`](./catalog/mcp_server_vpcep.md) | [`mcp_server_vpcep.json`](./catalog/mcp_server_vpcep.json) |
| `mcp_server_vpn` | VPN | 76 | 用于华为云 VPN 服务的资源查询与操作。 重点能力: ClientCaCertificate / ConnectionMonitor / CustomerGateway。 | [`mcp_server_vpn.md`](./catalog/mcp_server_vpn.md) | [`mcp_server_vpn.json`](./catalog/mcp_server_vpn.json) |
| `mcp_server_waf` | WAF | 112 | 用于华为云 WAF 服务的资源查询与操作。 重点能力: 云模式防护网站管理 / 告警管理 / 地址组管理。 | [`mcp_server_waf.md`](./catalog/mcp_server_waf.md) | [`mcp_server_waf.json`](./catalog/mcp_server_waf.json) |
| `mcp_server_workspace` | Workspace | 280 | 用于华为云 Workspace 服务的资源查询与操作。 重点能力: AccessConfig / AccessPolicy / Agency。 | [`mcp_server_workspace.md`](./catalog/mcp_server_workspace.md) | [`mcp_server_workspace.json`](./catalog/mcp_server_workspace.json) |
| `mcp_server_workspaceapp` | WorkspaceApp | 142 | 用于华为云 WorkspaceApp 服务的资源查询与操作。 重点能力: AppWareHouse / Application / ApplicationConfig。 | [`mcp_server_workspaceapp.md`](./catalog/mcp_server_workspaceapp.md) | [`mcp_server_workspaceapp.json`](./catalog/mcp_server_workspaceapp.json) |

## 快速路由建议
- 计算相关: `mcp_server_ecs`, `mcp_server_bms`, `mcp_server_as`
- 网络相关: `mcp_server_vpc`, `mcp_server_elb`, `mcp_server_eip`, `mcp_server_vpn`, `mcp_server_vpcep`
- 存储与数据库: `mcp_server_obs`, `mcp_server_evs`, `mcp_server_rds`, `mcp_server_dds`, `mcp_server_gaussdb`
- 安全与身份: `mcp_server_iam`, `mcp_server_kms`, `mcp_server_hss`, `mcp_server_waf`, `mcp_server_sts`
- 运维与治理: `mcp_server_aom`, `mcp_server_apm`, `mcp_server_ces`, `mcp_server_lts`, `mcp_server_cts`, `mcp_server_config`
- 开发与交付: `mcp_server_codehub`, `mcp_server_codeartsbuild`, `mcp_server_codeartsdeploy`, `mcp_server_codecheck`
- AI 与数据智能: `mcp_server_modelarts`, `mcp_server_metastudio`, `mcp_server_nlp`, `mcp_server_ocr`, `mcp_server_dataartsstudio`
