# SecMaster MCP Server 

## 版本信息
v0.1.0

## 产品描述

SecMaster MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务SecMaster交互的能力。可以基于自然语言对SecMaster资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="3">事件关系管理</td>
                    <td>DeleteDataobjectRelations</td>
                    <td>取消关联Dataobject</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataobjectRelations</td>
                    <td>查询关联Dataobject列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataobjectRelations</td>
                    <td>关联Dataobject</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">事件管理</td>
                    <td>CreateIncident</td>
                    <td>创建事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeIncident</td>
                    <td>编辑事件,根据实际修改的属性更新,未修改的列不更新</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIncidents</td>
                    <td>搜索事件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIncident</td>
                    <td>获取事件详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIncident</td>
                    <td>删除事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">剧本动作管理</td>
                    <td>CreatePlaybookAction</td>
                    <td>创建剧本动作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlaybookActions</td>
                    <td>查询剧本动作列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlaybookAction</td>
                    <td>删除剧本动作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePlaybookAction</td>
                    <td>更新剧本动作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">剧本实例管理</td>
                    <td>ShowPlaybookInstance</td>
                    <td>Show playbook instance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePlaybookInstance</td>
                    <td>操作剧本实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookTopology</td>
                    <td>查询剧本拓扑关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlaybookInstances</td>
                    <td>查询剧本实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlaybookAuditLogs</td>
                    <td>查询剧本实例审计日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">剧本审核管理</td>
                    <td>ListPlaybookApproves</td>
                    <td>查询剧本审核结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlaybookApprove</td>
                    <td>审核剧本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">剧本版本管理</td>
                    <td>ListPlaybookVersions</td>
                    <td>查询剧本版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookVersion</td>
                    <td>Show playbook version version</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyPlaybookVersion</td>
                    <td>克隆剧本及版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlaybookVersion</td>
                    <td>删除剧本版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePlaybookVersion</td>
                    <td>更新剧本版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlaybookVersion</td>
                    <td>创建剧本版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">剧本管理</td>
                    <td>CreatePlaybook</td>
                    <td>创建剧本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybook</td>
                    <td>查询剧本详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookMonitors</td>
                    <td>剧本运行监控</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlaybooks</td>
                    <td>查询剧本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlaybook</td>
                    <td>删除剧本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookStatistics</td>
                    <td>剧本统计数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePlaybook</td>
                    <td>修改剧本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">剧本规则管理</td>
                    <td>UpdatePlaybookRule</td>
                    <td>更新剧本规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePlaybookRule</td>
                    <td>删除剧本规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlaybookRule</td>
                    <td>查询剧本规则详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePlaybookRule</td>
                    <td>创建剧本规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">告警管理</td>
                    <td>CreateAlert</td>
                    <td>创建告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBatchOrderAlerts</td>
                    <td>告警转事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeAlert</td>
                    <td>编辑告警,根据实际修改的属性更新,未修改的列不更新</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlerts</td>
                    <td>搜索告警列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlert</td>
                    <td>获取告警详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlert</td>
                    <td>删除告警</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">告警规则管理</td>
                    <td>CreateAlertRuleSimulation</td>
                    <td>Simulate alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlertRuleTemplate</td>
                    <td>List alert rule templates</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertRuleTemplates</td>
                    <td>List alert rule templates</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlertRule</td>
                    <td>Delete alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlertRule</td>
                    <td>查看告警规则 Get alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableAlertRule</td>
                    <td>Disable alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertRuleMetrics</td>
                    <td>List alert rule metrics</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlertRule</td>
                    <td>Create alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlertRules</td>
                    <td>List alert rules</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableAlertRule</td>
                    <td>Enable alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlertRule</td>
                    <td>Update alert rule</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">基线检查</td>
                    <td>SearchBaseline</td>
                    <td>搜索基线检查结果列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">威胁情报管理</td>
                    <td>DeleteIndicator</td>
                    <td>删除威胁情报</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIndicator</td>
                    <td>创建威胁情报</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIndicators</td>
                    <td>查询威胁情报列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIndicatorDetail</td>
                    <td>查询威胁情报详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIndicator</td>
                    <td>更新威胁情报</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">工作空间管理</td>
                    <td>DeleteWorkspace</td>
                    <td>删除工作空间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkspace</td>
                    <td>更新工作空间名称、描述等信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspaces</td>
                    <td>可通过工作空间名称、工作空间描述、创建时间等条件对租户的工作空间进行筛选。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkspace</td>
                    <td>查询工作空间名称、描述等详情信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkspace</td>
                    <td>在使用安全云脑的基线检查、告警管理、安全分析、安全编排等功能前,需要创建工作空间,它可以将资源划分为各个不同的工作场景,避免资源冗余查找不便,影响日常使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">指标查询</td>
                    <td>BatchSearchMetricHits</td>
                    <td>批量查询指标结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据空间管理</td>
                    <td>CreateDataspace</td>
                    <td>创建数据空间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">数据类管理</td>
                    <td>ListDataclass</td>
                    <td>查询数据类列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataclassFields</td>
                    <td>查询字段列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">流程实例管理</td>
                    <td>OperateWorkflowInstance</td>
                    <td>操作流程实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">流程管理</td>
                    <td>ListWorkflows</td>
                    <td>查询流程列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">管道管理</td>
                    <td>CreatePipe</td>
                    <td>创建数据管道</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">计量计费管理</td>
                    <td>CreatePostPaidOrder</td>
                    <td>开通安全云脑按需服务</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>