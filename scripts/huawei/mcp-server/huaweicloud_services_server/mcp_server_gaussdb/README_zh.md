# GaussDB MCP Server 

## 版本信息
v0.1.0

## 产品描述

GaussDB MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务GaussDB交互的能力。可以基于自然语言对GaussDB资源进行全链路管理。

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
                    <td rowspan="33">HTAP-标准版</td>
                    <td>RestartStarrocksInstance</td>
                    <td>重启StarRocks实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHtapDataStore</td>
                    <td>HTAP引擎资源查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckStarrocksParams</td>
                    <td>对比实例参数和默认模板的差异</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeSrKernelVersion</td>
                    <td>StarRocks内核版本升级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStarrocksInstance</td>
                    <td>删除StarRocks实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStarRocksDatabaseUser</td>
                    <td>查询StarRocks数据库账户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStarRocksDatabaseUserPassword</td>
                    <td>修改StarRocks数据库账号密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckStarRocksResource</td>
                    <td>StarRocks资源检查。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStarrocksInstance</td>
                    <td>创建StarRocks实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckTableConfig</td>
                    <td>HTAP数据同步表配置校验。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStarRocksDataReplications</td>
                    <td>查询StarRocks数据同步状态信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStarRocksDatabaseUserPermission</td>
                    <td>修改StarRocks数据库账号权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStarRocksDataReplication</td>
                    <td>创建StarRocks数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStarRocksDatabaseUser</td>
                    <td>创建StarRocks数据库账号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStarrocksParams</td>
                    <td>按节点类型查询参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHtapFlavor</td>
                    <td>HTAP查询规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStarRocksDbParameters</td>
                    <td>查询StarRocks数据同步的库参数配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartStarrocksNode</td>
                    <td>重启StarRocks节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncStarRocksUsers</td>
                    <td>StarRocks实例开启行列分流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStarRocksDataReplicationConfig</td>
                    <td>查询StarRocks数据同步配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStarRocksDataReplication</td>
                    <td>删除StarRocks数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStarRocksDatabaseUser</td>
                    <td>删除StarRocks数据库账户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHtapStorageType</td>
                    <td>获取HTAP实例存储类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStarrocksInstanceInfo</td>
                    <td>查询StarRocks实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDataBaseConfig</td>
                    <td>HTAP数据同步库配置校验。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PauseStarRocksDataReplication</td>
                    <td>暂停StarRocks数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeStarRocksFlavor</td>
                    <td>StarRocks实例规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStarrocksParams</td>
                    <td>按节点类型修改节点参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHtapInstanceInfo</td>
                    <td>查询HTAP实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyDataSync</td>
                    <td>修改StarRocks数据同步配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStarRocksDataReplicationConfigByDataBase</td>
                    <td>按目标库查询StarRocks数据同步配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumeStarRocksDataReplication</td>
                    <td>恢复StarRocks数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStarRocksDataBases</td>
                    <td>查询StarRocks数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="28">HTAP-轻量版</td>
                    <td>DeleteClickHouseDataBaseReplication</td>
                    <td>删除数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClickHouseInstance</td>
                    <td>创建实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClickHouseDataBaseParameter</td>
                    <td>查询数据同步的库参数配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClickHouseDataBaseReplication</td>
                    <td>查询数据同步信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClickHouseInstanceNode</td>
                    <td>查询错误日志、慢日志节点信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootClickHouseInstance</td>
                    <td>重启实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClickHouseDatabaseUser</td>
                    <td>删除数据库账户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClickHouseSlowLogSensitiveStatus</td>
                    <td>修改慢日志脱敏状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClickHouseLtsConfig</td>
                    <td>查询实例LTS日志配置列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckClickHouseDataBaseConfig</td>
                    <td>数据同步库配置校验。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClickHouseDataBaseConfig</td>
                    <td>停止修改数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClickHouseInstance</td>
                    <td>查询实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckClickHouseTableConfig</td>
                    <td>数据同步表配置校验。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClickHouseDatabaseUser</td>
                    <td>查询数据库账户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClickHouseLtsConfig</td>
                    <td>批量创建LTS日志配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClickHouseDataBaseConfig</td>
                    <td>修改数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeClickHouseInstance</td>
                    <td>实例磁盘扩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClickHouseSlowLogSensitiveStatus</td>
                    <td>查询慢日志脱敏状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClickHouseDatabaseUserPassword</td>
                    <td>修改数据库账号密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeClickHouseFlavor</td>
                    <td>实例规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClickHouseSlowLogDetail</td>
                    <td>获取内核慢日志信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClickHouseDataBaseReplicationConfig</td>
                    <td>查看数据同步配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClickHouseDataBaseReplication</td>
                    <td>创建数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClickHouseDatabaseUserPermission</td>
                    <td>修改数据库账号权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClickHouseLtsConfig</td>
                    <td>批量解除LTS日志配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteClickHouseInstance</td>
                    <td>删除实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClickHouseDatabaseUser</td>
                    <td>创建数据库账号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClickHouseDataBase</td>
                    <td>查询数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">任务中心</td>
                    <td>ShowGaussMySqlJobInfo</td>
                    <td>获取TaurusDB任务中心指定ID的任务信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTaskRecord</td>
                    <td>删除指定任务记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScheduleJobs</td>
                    <td>获取定时任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelScheduleTask</td>
                    <td>取消定时任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImmediateJobs</td>
                    <td>获取即时任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScheduleTasK</td>
                    <td>删除定时任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">参数模板管理</td>
                    <td>DeleteGaussMySqlConfiguration</td>
                    <td>删除指定参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGaussMySqlConfiguration</td>
                    <td>创建参数模板信息,包含参数模板名称、描述、数据库版本信息、参数值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListParamsTemplateApplyHistory</td>
                    <td>查询参数模板应用记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlConfiguration</td>
                    <td>获取指定参数模板的参数信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchGaussMySqlConfiguration</td>
                    <td>指定实例变更参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationsInstances</td>
                    <td>查询指定参数模板可被应用的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyInstanceConfigurations</td>
                    <td>复制实例参数组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyConfigurations</td>
                    <td>复制参数组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfigurations</td>
                    <td>修改指定实例的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListModifyHistory</td>
                    <td>查询参数修改历史。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlConfiguration</td>
                    <td>修改指定参数模板的参数信息,包括名称、描述、指定参数的值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlConfigurations</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceConfigurations</td>
                    <td>获取指定实例的参数信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationsDifferences</td>
                    <td>比较两个参数模板之间的差异。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">备份管理</td>
                    <td>UpdateGaussMySqlBackupPolicy</td>
                    <td>设置自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyBackupEncryptStatus</td>
                    <td>打开或关闭备份加密。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGaussMySqlBackup</td>
                    <td>创建手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreOldInstance</td>
                    <td>备份恢复到当前实例或已有实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlIncrementalBackupList</td>
                    <td>查询增量备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribeBackupEncryptStatus</td>
                    <td>查询实例是否开启备份加密功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlBackupList</td>
                    <td>查询全量备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGaussMySqlBackup</td>
                    <td>删除手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRestoreTables</td>
                    <td>查询表级时间点恢复可选表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRestoreTables</td>
                    <td>表级时间点恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupRestoreTime</td>
                    <td>查询实例的可恢复时间段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlBackupPolicy</td>
                    <td>查询自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBackupOffsitePolicy</td>
                    <td>设置跨区备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRestoreAvailableTables</td>
                    <td>查询表级时间点恢复可选表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">多租特性</td>
                    <td>UpdateMultiTenant</td>
                    <td>开启或者关闭多租特性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMultiTenant</td>
                    <td>查询多租特性开关状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="47">实例管理</td>
                    <td>SwitchGaussMySqlInstanceSsl</td>
                    <td>为实例设置SSL数据加密。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlInstanceName</td>
                    <td>修改实例名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstances</td>
                    <td>查询回收站实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDedicatedResourceInfo</td>
                    <td>查询专属资源信息详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeGaussMySqlInstanceSpecification</td>
                    <td>变更数据库实例的规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlInstanceInternalIp</td>
                    <td>修改实例内网地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRecyclePolicy</td>
                    <td>设置回收站策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandGaussMySqlInstanceVolume</td>
                    <td>包周期存储扩容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyAutoExpandPolicy</td>
                    <td>修改存储空间自动扩容策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartGaussMySqlNode</td>
                    <td>节点重启。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlInstanceDetailInfo</td>
                    <td>批量查询实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecyclePolicy</td>
                    <td>查询回收站策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlInstanceAlias</td>
                    <td>修改实例备注。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerlessPolicy</td>
                    <td>设置Serverless配置策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaurusNodeDataIp</td>
                    <td>修改只读节点的读内网地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoExpandPolicy</td>
                    <td>查询存储空间自动扩容策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlInstanceOpsWindow</td>
                    <td>设置可维护时间段。建议将可维护时间段设置在业务低峰期,避免业务在维护过程中异常中断。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlDedicatedResources</td>
                    <td>获取专属资源池列表,包括用户开通的所有专属资源池信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGaussMysqlDns</td>
                    <td>申请内网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceEip</td>
                    <td>查询弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartGaussMySqlInstance</td>
                    <td>重启数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceMonitor</td>
                    <td>设置实例秒级监控,包括1秒监控和5秒监控。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlInstanceSecurityGroup</td>
                    <td>修改指定实例安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlInstancesUnifyStatus</td>
                    <td>根据指定条件查询实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGaussMySqlInstance</td>
                    <td>创建云数据库TaurusDB实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetGaussMySqlPassword</td>
                    <td>重置数据库密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlInstanceInfoUnifyStatus</td>
                    <td>查询实例详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceMonitorExtend</td>
                    <td>查询实例秒级监控信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoScalingHistory</td>
                    <td>查询自动变配历史记录.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutoScalingPolicy</td>
                    <td>设置自动变配。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlInstanceInfo</td>
                    <td>查询实例详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceDatabaseVersion</td>
                    <td>查询内核版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGaussMySqlReadonlyNode</td>
                    <td>创建只读节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelGaussMySqlInstanceEip</td>
                    <td>实例解绑弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckResource</td>
                    <td>资源预校验。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyNodePriority</td>
                    <td>修改节点故障倒换优先级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGaussMySqlInstance</td>
                    <td>删除/退订数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoScalingPolicy</td>
                    <td>查询自动变配。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlInstances</td>
                    <td>根据指定条件查询实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyGaussMysqlDns</td>
                    <td>修改内网域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlInstancePort</td>
                    <td>修改实例数据库端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeGaussMySqlInstanceDatabase</td>
                    <td>内核版本升级。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RenameInstanceNode</td>
                    <td>批量修改节点名称.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlInstanceDetailInfoUnifyStatus</td>
                    <td>批量查询实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGaussMySqlReadonlyNode</td>
                    <td>删除/退订实例的只读节点。多可用区模式删除/退订只读节点时,要保证删除/退订后,剩余的只读节点和主节点在不同的可用区中,否则无法删除/退订该只读节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InvokeGaussMySqlInstanceSwitchOver</td>
                    <td>用户手动进行主备倒换。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlInstanceEip</td>
                    <td>实例绑定弹性公网IP,供外网连接使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="25">数据库代理</td>
                    <td>ChangeGaussMySqlProxySpecification</td>
                    <td>数据库代理规格变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProxyName</td>
                    <td>修改代理实例名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAccessControl</td>
                    <td>设置访问控制规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProxyConnectionPoolType</td>
                    <td>更改数据库代理连接池类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProxySessionConsistence</td>
                    <td>修改代理会话一致性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchAccessControl</td>
                    <td>开启或关闭访问控制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShrinkGaussMySqlProxy</td>
                    <td>缩容数据库代理节点的数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProxyConfigurations</td>
                    <td>查询数据库代理内核参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProxyPort</td>
                    <td>修改读写分离端口号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTransactionSplitStatus</td>
                    <td>设置proxy事务拆分。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlProxyFlavors</td>
                    <td>查询数据库代理规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartProxyInstance</td>
                    <td>重启数据库代理.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProxyIpgroup</td>
                    <td>查询代理实例访问控制</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchGaussMySqlProxySsl</td>
                    <td>为数据库代理设置SSL数据加密。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetGaussMySqlProxyWeight</td>
                    <td>设置读写分离权重。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlProxyList</td>
                    <td>查询数据库代理信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandGaussMySqlProxy</td>
                    <td>扩容数据库代理节点的数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProxyNewConfigurations</td>
                    <td>修改数据库代理参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeProxyVersion</td>
                    <td>升级数据库代理实例内核版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProxyVersion</td>
                    <td>查询代理实例小版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchGaussMySqlProxyEip</td>
                    <td>Proxy绑定解绑弹性公网IP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGaussMySqlProxy</td>
                    <td>开启数据库代理,只支持ELB模式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNewNodeAutoAddSwitch</td>
                    <td>开启或关闭新增节点自动加入该Proxy。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyGaussMySqlProxyRouteMode</td>
                    <td>设置读写分离路由模式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGaussMySqlProxy</td>
                    <td>关闭数据库代理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">数据库用户管理</td>
                    <td>UpdateGaussMySqlDatabaseUserComment</td>
                    <td>修改云数据库 TaurusDB实例数据库用户备注。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetGaussMySqlDatabasePassword</td>
                    <td>修改云数据库 TaurusDB实例数据库用户密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGaussMySqlDatabaseUser</td>
                    <td>创建云数据库TaurusDB实例数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabasePermission</td>
                    <td>删除云数据库 TaurusDB实例数据库用户的数据库权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDatabasePermission</td>
                    <td>授予云数据库 TaurusDB实例数据库用户数据库权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlDatabaseUser</td>
                    <td>查询云数据库 TaurusDB实例数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGaussMySqlDatabaseUser</td>
                    <td>删除云数据库 TaurusDB实例数据库用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">数据库管理</td>
                    <td>CreateGaussMySqlDatabase</td>
                    <td>创建云数据库 TaurusDB实例数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlDatabase</td>
                    <td>查询 TaurusDB实例数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGaussMySqlDatabaseCharsets</td>
                    <td>查询云数据库 TaurusDB实例数据库可用字符集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlDatabaseComment</td>
                    <td>修改云数据库 TaurusDB实例数据库备注。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGaussMySqlDatabase</td>
                    <td>删除云数据库 TaurusDB实例数据库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">日志管理</td>
                    <td>ListLtsErrorLogDetails</td>
                    <td>获取指定实例的错误日志详情列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuditLog</td>
                    <td>开启或者关闭全量SQL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLtsConfigs</td>
                    <td>批量创建LTS日志配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLtsConfigs</td>
                    <td>查询实例LTS日志配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSlowLogStatistics</td>
                    <td>查询慢日志统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAuditLog</td>
                    <td>查询全量SQL开关状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLtsConfigs</td>
                    <td>批量删除LTS日志配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLtsSlowlogDetails</td>
                    <td>获取指定实例的慢日志详情列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadSlowLogFile</td>
                    <td>获取慢日志下载链接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSlowlogSensitiveSwitch</td>
                    <td>开启或关闭慢日志脱敏状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuditLogDownloadLink</td>
                    <td>获取全量SQL的临时下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSlowlogSensitiveStatus</td>
                    <td>查询慢日志脱敏状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">智能诊断</td>
                    <td>ShowIntelligentDiagnosisAbnormalCountOfInstances</td>
                    <td>获取各指标的异常实例数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIntelligentDiagnosisInstanceInfosPerMetric</td>
                    <td>获取某个指标的异常实例信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询数据库引擎的版本</td>
                    <td>ShowGaussMySqlEngineVersion</td>
                    <td>获取指定数据库引擎对应的数据库版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询数据库规格</td>
                    <td>ShowGaussMySqlFlavors</td>
                    <td>获取指定数据库引擎版本对应的规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">标签管理</td>
                    <td>ListProjectTags</td>
                    <td>查询指定project ID下实例的所有标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceTags</td>
                    <td>查询指定实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchTagAction</td>
                    <td>批量添加或删除指定实例的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">流量管理</td>
                    <td>DeleteSqlFilterRule</td>
                    <td>删除SQL限流规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetSqlFilterRule</td>
                    <td>设置SQL限流规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlFilterControl</td>
                    <td>查询SQL限流开关状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSqlFilterRule</td>
                    <td>查询SQL限流规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSqlFilterControl</td>
                    <td>开启或者关闭SQL限流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTaurusDbNodeProcesses</td>
                    <td>终止TaurusDB节点中指定的用户会话线程,执行时将排除传入的内部会话线程。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaurusDbNodeProcesses</td>
                    <td>分页查询TaurusDB节点中的用户会话线程,对应于show processlist命令,返回结果不含内部会话线程。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">配额管理</td>
                    <td>ShowGaussMySqlQuotas</td>
                    <td>获取指定企业项目的资源配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetGaussMySqlQuotas</td>
                    <td>设置指定企业项目的资源配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGaussMySqlProjectQuotas</td>
                    <td>获取指定租户的资源配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGaussMySqlQuotas</td>
                    <td>修改指定企业项目的资源配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnterpriseProjects</td>
                    <td>查询企业项目。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>