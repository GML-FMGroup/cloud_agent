# DataArtsStudio MCP Server 

## 版本信息
v0.1.0

## 产品描述

DataArtsStudio MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DataArtsStudio交互的能力。可以基于自然语言对DataArtsStudio资源进行全链路管理。

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
                    <td rowspan="17">API管理接口</td>
                    <td>PublishApiToInstance</td>
                    <td>发布API。API只有发布后,才能够被调用。API发布时,可以将API发送至指定网关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceList</td>
                    <td>查看API不同操作对应的实例信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AuthorizeActionApiToInstance</td>
                    <td>- API主动授权: API审核人可发起,API主动授权成功后,在有效期内,APP即可访问该API。API授权包含授权和续约两部分功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugApi</td>
                    <td>调试API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDataServiceExcelTemplate</td>
                    <td>下载excel模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApis</td>
                    <td>查询API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AuthorizeApiToInstance</td>
                    <td>APP创建成功后,还不能访问API,如果想要访问某个API,需要将该API授权给APP。API主动授权成功后,在有效期内,APP即可访问该API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportDataServiceExcel</td>
                    <td>导入包含API信息的excel文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApi</td>
                    <td>更新API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteApiToInstance</td>
                    <td>- 下线API。将已发布的API下线。下线后,所有授权关系都会被解除,API将无法再被调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchDebugInfo</td>
                    <td>查看API在不同集群上的调试信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchPublishInfo</td>
                    <td>查看API在不同集群上的发布信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApi</td>
                    <td>创建API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApi</td>
                    <td>查询API信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDataServiceExcel</td>
                    <td>导出包含API信息的excel文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApi</td>
                    <td>批量删除API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDataServiceZip</td>
                    <td>全量导出包含API的excel压缩文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">业务指标接口</td>
                    <td>ListBizMetrics</td>
                    <td>通过名称、创建者、修改时间分页查找业务指标信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBizMetric</td>
                    <td>创建业务指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBizMetric</td>
                    <td>删除业务指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBizMetricById</td>
                    <td>通过ID查看指标的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBizMetric</td>
                    <td>更新业务指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBizMetricOwners</td>
                    <td>查看指标责任人信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricRelations</td>
                    <td>获取当前指标图谱。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBizMetricDimensions</td>
                    <td>查看指标维度信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">业务资产接口</td>
                    <td>ShowBusinessAssetsTree</td>
                    <td>逐级查询业务资产目录树,包含数据规范同步过来的业务对象和逻辑实体。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBusinessAssets</td>
                    <td>业务资产查询接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">主题层级接口</td>
                    <td>ChangeSubjects</td>
                    <td>修改或删除主题层级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubjectLevels</td>
                    <td>获取主题层级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">主题管理接口</td>
                    <td>UpdateSubject</td>
                    <td>修改主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubject</td>
                    <td>创建主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchSubject</td>
                    <td>通过名称(支持模糊查询)、创建者、责任人、状态、修改时间分页查找主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBusiness</td>
                    <td>获取数据资产主题树信息l1,l2,l3。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubjectNew</td>
                    <td>修改主题(新)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubject</td>
                    <td>删除主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubjectNew</td>
                    <td>删除主题(新)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchSubjectNew</td>
                    <td>查找主题(新)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubjectNew</td>
                    <td>创建主题(新)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">事实表接口</td>
                    <td>ShowFactLogicTableById</td>
                    <td>通过ID查看事实表的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckFactLogicTableStatus</td>
                    <td>查看逆向事实表任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesignFactLogicTable</td>
                    <td>根据ID集合删除事实表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFactLogicTables</td>
                    <td>通过中英文名称、创建者、审核人、状态、修改时间分页查找事实表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">企业模式发布包管理</td>
                    <td>DeployFactoryPackages</td>
                    <td>发布任务包</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFactoryPackageDetail</td>
                    <td>查询指定发布包详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFactoryReleasePackages</td>
                    <td>查询发布包列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelFactoryPackages</td>
                    <td>撤销任务包</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">作业开发接口</td>
                    <td>RetryFactoryJobInstance</td>
                    <td>支持重跑作业实例以及上下游的作业实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFactoryAlarmInfo</td>
                    <td>查询告警通知记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopFactorySupplementDataInstance</td>
                    <td>停止补数据实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFactoryJobName</td>
                    <td>修改作业名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFactorySupplementData</td>
                    <td>查询补数据实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFactorySupplementDataInstance</td>
                    <td>创建补数据实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFactoryJobInstancesByName</td>
                    <td>查询指定作业的实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFactoryFullText</td>
                    <td>全局搜索</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetFactoryJobTags</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">信息架构接口</td>
                    <td>ListAllTables</td>
                    <td>从信息架构中查询多种类型的表信息,包括逻辑实体、物理表、维度表、事实表、汇总表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">元数据实时同步</td>
                    <td>BatchSyncMetadata</td>
                    <td>元数据实时同步接口,支持批量。该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">元数据采集任务接口</td>
                    <td>DeleteTaskInfo</td>
                    <td>删除单个采集任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteTaskAction</td>
                    <td>启动、调度、停止采集任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceLog</td>
                    <td>获取任务日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskInfo</td>
                    <td>编辑采集任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskInfo</td>
                    <td>查询采集任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskList</td>
                    <td>查询采集任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>创建采集任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">关系建模接口</td>
                    <td>CreateTableModel</td>
                    <td>在关系建模中创建一个表模型,包括逻辑实体和物理表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTableModelRelations</td>
                    <td>查询模型下所有关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRelations</td>
                    <td>通过关系名称(支持模糊查询)、创建人、开始时间、结束时间等分页查找关系信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkspaces</td>
                    <td>删除模型工作区。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkspace</td>
                    <td>新建模型工作区。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkspaceDetailById</td>
                    <td>查询物理模型或逻辑模型的工作区空间详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTableModelById</td>
                    <td>通过ID获取模型表详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTableModels</td>
                    <td>通过中英文名称、创建者、审核人、状态、修改时间分页查找关系建模中的表模型信息,包括逻辑实体、物理表和其属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchFieldsForRelation</td>
                    <td>查询目的表和字段(待下线)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkspace</td>
                    <td>更新模型工作区。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspaces</td>
                    <td>获取当前空间下的全部模型信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTableModel</td>
                    <td>在关系建模中删除一个表模型及其属性,包括逻辑实体和物理表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDesignOperationResult</td>
                    <td>获取批量操作的结果,如逻辑模型转物理模型和逆向数据库操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateDesignTableModelsFromLogic</td>
                    <td>转换逻辑模型为物理模型,转换成功则显示转换后的目标模型信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDesignModelTableDdl</td>
                    <td>根据模型ID导出指定表的DDL语句。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRelationById</td>
                    <td>通过ID获取关系详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTableModel</td>
                    <td>在关系建模中更新一个表模型及其属性,包括逻辑实体和物理表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">动态数据脱敏接口</td>
                    <td>ShowSecurityDynamicMaskingPolicy</td>
                    <td>查询某个脱敏策略的详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSecurityDynamicMaskingPolicies</td>
                    <td>批量删除动态脱敏策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityDynamicMaskingPolicies</td>
                    <td>查询动态数据脱敏策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityDynamicMaskingPolicy</td>
                    <td>更新动态数据脱敏策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityDynamicMaskingPolicy</td>
                    <td>创建动态数据脱敏策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">原子指标接口</td>
                    <td>DeleteDesignAtomicIndex</td>
                    <td>批量删除原子指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAtomicIndexById</td>
                    <td>通过ID获取原子指标详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchAtomicIndexes</td>
                    <td>通过中英文名称、创建者、审核人、状态、修改时间分页查找原子指标信息看,中英文名称支持模糊查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesignAtomicIndex</td>
                    <td>更新单个原子指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesignAtomicIndex</td>
                    <td>新建单个原子指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">发布包管理</td>
                    <td>CreateFactoryPendingItemsPackage</td>
                    <td>待发布包发布</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFactoryPendingItems</td>
                    <td>查询待发布包列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">复合指标接口</td>
                    <td>CreateDesignCompoundMetric</td>
                    <td>根据参数,新建复合指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesignCompoundMetric</td>
                    <td>根据ID集合删除复合指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCompoundMetrics</td>
                    <td>通过中英文名称、创建者、审核人、状态、修改时间、l3Id分页查找复合指标信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCompoundMetricById</td>
                    <td>通过ID获取复合指标详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesignCompoundMetric</td>
                    <td>根据参数,更新复合指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">安全管理员接口</td>
                    <td>ShowSecurityAdmin</td>
                    <td>查看安全管理员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifySecurityAdmin</td>
                    <td>创建或更新安全管理员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实例管理接口</td>
                    <td>ListDataArtsStudioInstances</td>
                    <td>获取实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实例规格变更接口</td>
                    <td>ChangeResource</td>
                    <td>规格变更接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">审批管理接口</td>
                    <td>SearchApprovals</td>
                    <td>获取审批单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesignLatestApproval</td>
                    <td>当已发布的实体被编辑时,其会生成下展,该接口用于删除实体的下展信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConfirmApprovals</td>
                    <td>审批驳回/通过,单个或多个action-id=reject/resolve。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchDesignLatestApprovalDiff</td>
                    <td>当已发布的实体被编辑时,其会生成下展,该接口用于获取下展信息与已发布实体的差异。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollbackApproval</td>
                    <td>撤回审批单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchPublish</td>
                    <td>批量发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApprover</td>
                    <td>删除审批人。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchOffline</td>
                    <td>批量下线。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApprovers</td>
                    <td>查询审批人列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApprover</td>
                    <td>创建审批人。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">密级管理接口</td>
                    <td>BatchDeleteSecuritySecrecyLevels</td>
                    <td>批量删除密级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecuritySecrecyLevel</td>
                    <td>根据指定的id查询密级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecuritySecrecyLevel</td>
                    <td>删除指定的id的密级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecuritySecrecyLevel</td>
                    <td>根据指定的id修改密级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecuritySecrecyLevel</td>
                    <td>创建密级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecuritySecrecyLevels</td>
                    <td>获取密级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">对账作业接口</td>
                    <td>ShowConsistencyTaskDetail</td>
                    <td>获取对账作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConsistencyTask</td>
                    <td>获取对账作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">导入导出接口</td>
                    <td>ImportModels</td>
                    <td>导入模型,关系建模,维度建模,码表,业务指标以及流程架构。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportCatalogs</td>
                    <td>用于导入主题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDesignModels</td>
                    <td>根据请求参数,导出业务数据,可以导出:码表、数据标准、原子指标、衍生指标、复合指标、汇总表、业务指标、主题、流程、逻辑模型、物理模型、维度、事实表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDesignResult</td>
                    <td>根据请求导出业务数据(/export-model)时返回的uuid,获取excel导出结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportResult</td>
                    <td>查询导入excel的处理结果(其中参数uuid获取为:/design/models/action或/design/catalogs/action接口返回结果)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">工作空间用户管理接口</td>
                    <td>DeleteWorkspaceusers</td>
                    <td>删除工作空间用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkSpaceUserOrGroup</td>
                    <td>编辑工作空间用户或用户组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspaceusers</td>
                    <td>获取工作空间用户信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddWorkSpaceUsers</td>
                    <td>添加工作空间用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspaceRoles</td>
                    <td>获取工作空间用户角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">工作空间管理接口</td>
                    <td>CreateManagerWorkSpace</td>
                    <td>创建工作空间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspacesForUser</td>
                    <td>获取指定用户所有的工作空间集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkSpace</td>
                    <td>获取单个工作空间信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListManagerWorkSpaces</td>
                    <td>获取工作空间列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">应用管理接口</td>
                    <td>CreateApp</td>
                    <td>创建应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApps</td>
                    <td>查询应用列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>更新应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppInfo</td>
                    <td>查询应用详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>删除应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">总览接口</td>
                    <td>ShowApisOverview</td>
                    <td>查询统计用户相关的总览开发指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApisDetail</td>
                    <td>查询api 统计数据详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppsDetail</td>
                    <td>查询app 统计数据详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApisDashboard</td>
                    <td>查询api 仪表板数据详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppsDashboard</td>
                    <td>查询app 仪表板数据详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApisTop</td>
                    <td>查询api 服务调用topN。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApiDashboard</td>
                    <td>查询指定api 仪表板数据详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppsOverview</td>
                    <td>查询统计用户相关的总览调用指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppsTop</td>
                    <td>查询app 服务使用topN。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiTopN</td>
                    <td>查询指定api 应用调用topN。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">成本管理计算维度接口</td>
                    <td>SearchSgcComputeDimensions</td>
                    <td>获取计算维度成本列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">指标资产接口</td>
                    <td>ShowMetricTree</td>
                    <td>查询指标资产目录树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetricAssets</td>
                    <td>指标资产查询接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">授权管理接口</td>
                    <td>SearchAuthorizeApp</td>
                    <td>查询API已授权的APP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchBindApi</td>
                    <td>查询APP已拥有授权的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">敏感数据结果管理接口</td>
                    <td>ListSecuritySensitiveDataOverviews</td>
                    <td>查询敏感数据发现概览结果(以分类和密级为单位)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">数仓分层接口</td>
                    <td>UpdateDesignDataLayers</td>
                    <td>修改或删除数仓分层</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesignDataLayers</td>
                    <td>获取数仓分层信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">数据分类接口</td>
                    <td>ImportSecurityBuiltinCategoryGroups</td>
                    <td>导入预置分类。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityDataCategories</td>
                    <td>查询数据分类列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">数据地图接口</td>
                    <td>ShowDataSets</td>
                    <td>资产搜索</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCategoriesTree</td>
                    <td>获取某空间下资产目录树。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchTag</td>
                    <td>批量给资产打标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLogicEntities</td>
                    <td>获取主题目录下逻辑实体。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTableData</td>
                    <td>表数据预览,展示10条数据,该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceInfos</td>
                    <td>查询表相关的作业算子运行实例信息,该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodes</td>
                    <td>查询表相关的作业算子列表,该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataDetail</td>
                    <td>资产详情接口,该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatamapLineage</td>
                    <td>资产血缘接口,该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEntity</td>
                    <td>根据guid删除资产。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQueues</td>
                    <td>队列列表,展示10条数据,该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLineageBulk</td>
                    <td>批量血缘接口,根据作业算子分页批量查询血缘。该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTags</td>
                    <td>搜索查询标签分页展示</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrUpdateEntities</td>
                    <td>创建或修改资产,该接口功能处于邀测阶段,后续将随功能公测将逐步开放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEntityDetails</td>
                    <td>批量获取资产信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ParseUserBehavior</td>
                    <td>用户行为分析</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">数据安全诊断接口</td>
                    <td>ExecuteSecurityDiagnose</td>
                    <td>执行数据安全诊断。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityNoMaskingTableResult</td>
                    <td>查询未进行静态脱敏任务的表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityUnreasonablePermissions</td>
                    <td>查询不合理的权限配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecuritySensitiveDataDiagnoseResult</td>
                    <td>查询敏感数据保护模块诊断结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityDatasourceProtectionDiagnoseResult</td>
                    <td>查询数据源防护模块诊断结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityPermissionManagementDiagnoseResult</td>
                    <td>查询数据权限控制模块诊断结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据权限查询接口</td>
                    <td>ListSecurityRoleActions</td>
                    <td>查询角色对一组库、表的权限交集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">数据标准接口</td>
                    <td>CreateStandard</td>
                    <td>创建数据标准。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStandard</td>
                    <td>修改数据标准。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStandard</td>
                    <td>删除数据标准。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStandardById</td>
                    <td>通过ID获取数据标准详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllStandards</td>
                    <td>根据查询条件分页获取数据标准集合,按修改时间降序排序。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetLinkAttributeAndStandard</td>
                    <td>关联属性与数据标准。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">数据标准模板接口</td>
                    <td>CreateStandardTemplate</td>
                    <td>创建当前工作空间下的数据标准模板自定义项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStandardTemplate</td>
                    <td>查询当前工作空间下的数据标准模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InitializeStandardTemplate</td>
                    <td>初始化数据标准模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStandardTemplate</td>
                    <td>删除数据标准模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStandardTemplate</td>
                    <td>修改数据标准模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">数据源元数据获取接口</td>
                    <td>ListDataTables</td>
                    <td>获取数据源中的表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListColumns</td>
                    <td>获取数据源中表的字段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSchemas</td>
                    <td>获取schemas,目前只有DWS和采用postgresql驱动的RDS数据源支持schema,请在调用前确认该数据源是否支持schema字段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabases</td>
                    <td>获取数据库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据源接口</td>
                    <td>SearchDwByType</td>
                    <td>获取指定类型下的数据连接信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">数据连接管理</td>
                    <td>AuthorizeDataConnection</td>
                    <td>数据连接跨空间授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">数据连接管理接口</td>
                    <td>ShowDataconnection</td>
                    <td>查询单个数据连接信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DebugDataconnection</td>
                    <td>测试创建数据连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataconnection</td>
                    <td>更新数据连接信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnections</td>
                    <td>创建数据连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataconnection</td>
                    <td>删除数据连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataconnections</td>
                    <td>查询数据连接列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">服务目录管理接口</td>
                    <td>ListAllCatalogList</td>
                    <td>获取当前目录下所有类型列表(包括api和目录,均以目录的数据格式形式展示)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPathObjectById</td>
                    <td>通过目录id获取路径对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServiceCatalog</td>
                    <td>批量删除服务目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateServiceCatalog</td>
                    <td>创建服务目录。 根目录编号为0。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApiCatalogList</td>
                    <td>获取当前目录下的api列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchIdByPath</td>
                    <td>通过路径获取id。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCatalogList</td>
                    <td>获取当前目录下的目录列表(全量数据,不分页,推荐仅用于生成目录树等无法分页的场景)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataServiceMarketApis</td>
                    <td>查询服务目录API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCatalogDetail</td>
                    <td>查询服务目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPathById</td>
                    <td>通过id获取路径。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateApi</td>
                    <td>批量移动api至新目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCatalog</td>
                    <td>更新服务目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MigrateCatalog</td>
                    <td>移动当前目录至新目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">权限审批接口</td>
                    <td>BatchRejectSecurityApplications</td>
                    <td>批量驳回工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AcceptSecurityApplication</td>
                    <td>审批通过工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeclineSecurityApplication</td>
                    <td>驳回工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchApproveSecurityApplications</td>
                    <td>批量审批通过工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityApprovals</td>
                    <td>获取工单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityTableApprovers</td>
                    <td>获取表权限审批人列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplySecurityTableAuthority</td>
                    <td>提交表权限申请</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">权限应用接口</td>
                    <td>DebugSecurityDlfDataWareHouses</td>
                    <td>测试数据开发连接细粒度连通性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityDlfDataWareHouses</td>
                    <td>查询数据开发细粒度连接列表(全量)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateSecurityDlfDataWareHouses</td>
                    <td>批量更新数据开发连接细粒度认证状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">权限申请接口</td>
                    <td>UnpublishSecurityApplication</td>
                    <td>撤回工单申请</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">权限管理接口</td>
                    <td>CreateSecurityPermissionSetMember</td>
                    <td>添加权限集成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSecurityPermissionSetPermissions</td>
                    <td>删除权限集的权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityDatasourceUrls</td>
                    <td>查询url信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSecurityPermissionSetMembers</td>
                    <td>批量删除权限集成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityPermissionSetPermission</td>
                    <td>添加权限集的权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityPermissionSetPermission</td>
                    <td>更新权限集的权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityPermissionSet</td>
                    <td>更新权限集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityMemberPermission</td>
                    <td>查询我的权限、空间账号权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityPermissionSet</td>
                    <td>删除权限集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSecurityPermissionSetPermissions</td>
                    <td>批量添加权限集的权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityPermissionSet</td>
                    <td>查询权限集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityMemberPermissionExpireTime</td>
                    <td>批量变更权限有效期</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateSecurityPermissionSetMembers</td>
                    <td>批量添加权限集成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityDatasourceConfigurations</td>
                    <td>查询数据源可配置权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityPermissionSets</td>
                    <td>查询权限集列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityPermissionSetMembers</td>
                    <td>查询权限集成员列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityPermissionSetPermissions</td>
                    <td>查询权限集的权限列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityPermissionSet</td>
                    <td>创建权限集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityDatasourceActions</td>
                    <td>查询数据操作信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签接口</td>
                    <td>ShowGlossaryList</td>
                    <td>查询标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTagToAsset</td>
                    <td>标签关联到资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveDesignEntityTags</td>
                    <td>根据资产(表或属性)的ID删除资产标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDesignEntityTags</td>
                    <td>根据资产(表或属性)的ID给资产打上标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">概览</td>
                    <td>CountStandards</td>
                    <td>查看某个数据标准在所有模型字段中的覆盖率,即使用该标准的字段占总字段的百分比。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountTableModels</td>
                    <td>单个模型中的统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountAllModels</td>
                    <td>关系建模页面,外层的统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountOverviews</td>
                    <td>总览统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">汇总表接口</td>
                    <td>ShowAggregationLogicTableById</td>
                    <td>通过ID查看汇总表的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAggregationLogicTables</td>
                    <td>通过中英文名称、创建者、审核人、状态、修改时间分页查找汇总表信息,中英文名称支持模糊查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesignAggregationLogicTable</td>
                    <td>更新汇总表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesignAggregationLogicTable</td>
                    <td>根据入参,手动创建汇总表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesignAggregationLogicTable</td>
                    <td>批量删除汇总表,只能删除状态为草稿、已线下、已驳回的表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">流程架构接口</td>
                    <td>ListCatalogTree</td>
                    <td>获取所有目录树。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchCatalogs</td>
                    <td>查询流程架构列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCatalog</td>
                    <td>创建流程架构。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCatalog</td>
                    <td>删除流程架构。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBizCatalogDetail</td>
                    <td>查找流程架构详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeCatalog</td>
                    <td>修改流程架构。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">消息管理接口</td>
                    <td>ShowMessageDetail</td>
                    <td>获取消息详情。此功能仅用作信息详情展示,不用做业务处理,因此不展示编号等后台参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessage</td>
                    <td>查询审核中心的通知消息列表。与申请不同,通知类消息,无法驳回,仅能在指定的时间范围内作出处理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConfirmMessage</td>
                    <td>对收到的通知消息进行确认,可以在指定的时间范围内选择何时进行处理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">版本信息接口</td>
                    <td>CompareDesignVersions</td>
                    <td>通过两个版本id,比较两者差异。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchVersions</td>
                    <td>通过名称、创建者、修改时间查找版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">用户同步任务接口</td>
                    <td>ShowSecurityMemberSyncTask</td>
                    <td>查询单个用户同步任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">用户同步接口</td>
                    <td>ListSecurityMemberSyncTasks</td>
                    <td>查询用户同步列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">申请管理接口</td>
                    <td>ListApply</td>
                    <td>查询申请列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchApproveApply</td>
                    <td>审核申请。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApplyDetail</td>
                    <td>获取申请详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">监控运维</td>
                    <td>ListFactoryTaskOverview</td>
                    <td>查询实例运行状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFactoryTaskCompletion</td>
                    <td>查询任务完成情况</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">目录接口</td>
                    <td>ListCategory</td>
                    <td>获取作业目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">目录管理</td>
                    <td>DeleteDirectory</td>
                    <td>删除目录(数据标准、码表)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDirectory</td>
                    <td>修改目录(数据标准、码表)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDirectories</td>
                    <td>获取所有目录(数据标准、码表)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDirectory</td>
                    <td>创建目录(数据标准、码表)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">码表管理接口</td>
                    <td>SearchCodeTableValues</td>
                    <td>查看码表字段值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCodeTable</td>
                    <td>修改码表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCodeTableById</td>
                    <td>通过ID查看码表的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCodeTable</td>
                    <td>删除码表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCodeTableValues</td>
                    <td>编辑码表字段值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchCodeTables</td>
                    <td>查询码表列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCodeTable</td>
                    <td>创建码表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">空间资源权限策略管理接口</td>
                    <td>ShowSecurityResourcePermissionPolicy</td>
                    <td>查询单个资源权限策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSecurityResourcePermissionPolicies</td>
                    <td>批量删除资源权限策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityResourcePermissions</td>
                    <td>查询空间资源权限策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityResourcePermissionPolicy</td>
                    <td>创建空间资源权限策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityResourcePermissionPolicy</td>
                    <td>更新空间资源权限策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">统计资产接口</td>
                    <td>ShowTechnicalAssetsStatistic</td>
                    <td>获取技术资产统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBusinessAssetsStatistic</td>
                    <td>获取业务资产统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">维度接口</td>
                    <td>CreateDesignDimension</td>
                    <td>根据参数新建维度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesignDimension</td>
                    <td>根据传入的维度ID,删除维度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesignDimension</td>
                    <td>根据参数,更新维度信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDimensionGroups</td>
                    <td>查询维度颗粒度,依据tableId查询涉及所有维度,不传tableId查询所有维度组颗粒度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDimensionById</td>
                    <td>通过ID查看维度详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDimensionStatus</td>
                    <td>查看逆向维度表任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDimensions</td>
                    <td>通过中英文名称、描述、创建者、审核人、状态、l3Id、衍生指标idList、修改时间分页查找维度信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">维度表接口</td>
                    <td>DeleteDesignDimensionLogicTable</td>
                    <td>根据维度表ID,删除维度表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDimensionLogicTableById</td>
                    <td>通过ID查看维度表的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDimensionLogicTables</td>
                    <td>通过中英文名称、创建者、审核人、状态、修改时间分页查找维度表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">网关管理接口</td>
                    <td>ListApicGroups</td>
                    <td>获取网关分组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApicInstances</td>
                    <td>获取网关实例(专享版)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">脚本开发接口</td>
                    <td>ListFactoryScripts</td>
                    <td>此接口用来查询脚本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">自定义项接口</td>
                    <td>SearchCustomizedFields</td>
                    <td>查询自定义项(包括表自定义项、属性自定义项、主题自定义项、业务指标自定义项)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyCustomizedFields</td>
                    <td>修改自定义项(包括表自定义项、属性自定义项、主题自定义项、业务指标自定义项)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">血缘信息</td>
                    <td>ShowUnrelatedTable</td>
                    <td>无血缘关系表查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportLineage</td>
                    <td>血缘查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLineage</td>
                    <td>血缘查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLineageInfo</td>
                    <td>创建血缘信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">衍生指标接口</td>
                    <td>ListDerivativeIndexes</td>
                    <td>通过中英文名称、创建者、审核人、状态、修改时间、l3Id分页查找衍生指标信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDerivativeIndexById</td>
                    <td>通过ID获取衍生详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesignDerivativeIndex</td>
                    <td>根据衍生指标ID,删除衍生指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesignDerivativeIndex</td>
                    <td>根据传入参数,更新衍生指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesignDerivativeIndex</td>
                    <td>根据参数,新建衍生指标指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">规则分组接口</td>
                    <td>CreateSecurityDataClassificationRuleGroup</td>
                    <td>创建规则分组接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityDataClassificationRuleGroups</td>
                    <td>查询规则组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityDataClassificationRuleGroup</td>
                    <td>删除规则分组接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityDataClassificationRuleGroup</td>
                    <td>修改规则分组接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityDataClassificationRuleGroup</td>
                    <td>查询规则组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">规则模板接口</td>
                    <td>BatchDeleteTemplates</td>
                    <td>批量删除规则模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTemplate</td>
                    <td>更新规则模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplate</td>
                    <td>创建规则模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQualityTemplates</td>
                    <td>分页获取规则模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemplatesDetail</td>
                    <td>获取规则模板详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">识别规则接口</td>
                    <td>UpdateSecurityRuleEnableStatus</td>
                    <td>修改识别规则状态接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecurityDataClassificationRule</td>
                    <td>查询特定识别规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckSecurityDataClassificationCombineRule</td>
                    <td>组合识别规则测试</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityDataClassificationRules</td>
                    <td>查询识别规则列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSecurityDataClassificationRule</td>
                    <td>批量删除识别规则接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityDataClassificationCombineRule</td>
                    <td>创建组合识别规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityDataClassificationRule</td>
                    <td>删除识别规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityDataClassificationCombineRule</td>
                    <td>修改组合识别规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityDataClassificationRule</td>
                    <td>修改识别规则接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityDataClassificationRule</td>
                    <td>创建识别规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">质量作业接口</td>
                    <td>ListQualityTask</td>
                    <td>获取质量作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQualityTaskDetail</td>
                    <td>获取质量作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQualityTaskLists</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">质量规则接口</td>
                    <td>RemoveDesignQualityInfos</td>
                    <td>清空表的质量规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesignTableQuality</td>
                    <td>更新表的异常数据输出配置,包括是否生成异常数据、设置异常数据数据库或Schema、设置异常表表前缀/表后缀。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">购买实例接口</td>
                    <td>PayForDgcOneKey</td>
                    <td>DataArtsStudio实例一键购买接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">资产信息</td>
                    <td>ShowDataProfile</td>
                    <td>查询概要</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RenewDataProfile</td>
                    <td>指定字段采集概要信息接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataPreview</td>
                    <td>表数据预览</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">资产分类接口</td>
                    <td>AssociateClassificationToEntity</td>
                    <td>将一个分类关联到一个或多个指定guid的资产上</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateClassificationToEntities</td>
                    <td>批量资产关联分类:只支持对数据表的列和OBS对象添加分类</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClassificationFromEntities</td>
                    <td>移除资产关联分类:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">资产分级接口</td>
                    <td>DeleteSecurityLevelFromEntity</td>
                    <td>移除资产关联密级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateSecurityLevelToEntities</td>
                    <td>批量资产关联密级:单个密级关联到多个资产上</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateSecurityLevelToEntitie</td>
                    <td>关联资产到密级,资产关联指定密级</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">资产管理接口</td>
                    <td>UpdateEntityAttribute</td>
                    <td>修改资产指定属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEntityInfoByGuid</td>
                    <td>根据表guid可以获取表的详情信息,表的详情信息包含column的信息,也可以根据column的guid直接获取column的信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEntities</td>
                    <td>查询技术资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrUpdateAsset</td>
                    <td>添加或修改资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAsset</td>
                    <td>删除资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">运维管理接口</td>
                    <td>ShowInstanceResult</td>
                    <td>获取实例结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>获取任务执行结果列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">队列权限接口</td>
                    <td>UpdateSecurityAssignedQueue</td>
                    <td>修改当前空间下分配的队列资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecurityAssignedQueue</td>
                    <td>分配队列资源给指定空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSecurityAssignedQueue</td>
                    <td>删除当前空间下分配的队列资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecurityAssignedQueues</td>
                    <td>查询当前空间下分配的队列资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">限定接口</td>
                    <td>ShowConditionById</td>
                    <td>通过ID查看限定详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCondition</td>
                    <td>通过中英文名称、描述、创建者、审核人、限定分组id、修改时间状态分页查找限定信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">集群管理接口</td>
                    <td>ShowDataServiceInstance</td>
                    <td>查询集群详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataServiceInstancesOverview</td>
                    <td>查询集群概览信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataServiceInstancesDetail</td>
                    <td>查询集群详情信息列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>