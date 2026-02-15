# GaussDBforNoSQL MCP Server 

## 版本信息
v0.1.0

## 产品描述

GaussDBforNoSQL MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务GaussDBforNoSQL交互的能力。可以基于自然语言对GaussDBforNoSQL资源进行全链路管理。

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
                    <td rowspan="1">任务管理</td>
                    <td>ListJobs</td>
                    <td>查询任务列表和详情,默认查询任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">企业项目管理</td>
                    <td>ListEpsQuotas</td>
                    <td>查询企业项目配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyEpsQuotas</td>
                    <td>修改企业项目配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">参数模板管理</td>
                    <td>UpdateConfiguration</td>
                    <td>修改参数模板参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationDatastores</td>
                    <td>查询支持参数模板的接口信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyConfigurationToInstances</td>
                    <td>将参数模板应用到实例,可以指定一个或多个实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyConfiguration</td>
                    <td>复制参数模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfiguration</td>
                    <td>修改指定实例的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurations</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfiguration</td>
                    <td>创建参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyConfiguration</td>
                    <td>将参数模板应用到实例,可以指定一个或多个实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfiguration</td>
                    <td>删除指定参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceConfigurations</td>
                    <td>修改指定实例的参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetParamGroupTemplate</td>
                    <td>重置自定义参数模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceConfiguration</td>
                    <td>查询实例参数配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigurationTemplates</td>
                    <td>获取参数模板列表,包括所有数据库的默认参数模板和用户创建的参数模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigurationDetail</td>
                    <td>获取指定参数模板的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApplyHistory</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareConfiguration</td>
                    <td>比较两个参数模板之间的差异</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowModifyHistory</td>
                    <td>查询实例参数的修改历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApplicableInstances</td>
                    <td>查询参数模板可应用的实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="22">备份与恢复</td>
                    <td>ShowBackupPolicies</td>
                    <td>查询自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackup</td>
                    <td>删除手动备份</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAllInstancesBackups</td>
                    <td>根据指定条件查询备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBackup</td>
                    <td>支持紧急情况下停止备份功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRedisPitrInfo</td>
                    <td>查询Redis实例指定时间点恢复所占用的存储空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteManualBackup</td>
                    <td>批量删除数据库实例的手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreTime</td>
                    <td>查询实例可恢复的时间段</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreDatabases</td>
                    <td>获取GeminiDB(for Cassandra)实例表级恢复的数据库信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreRedisPitr</td>
                    <td>恢复当前Redis实例到指定时间点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRedisPitrPolicy</td>
                    <td>查询Redis恢复到指定时间点策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAllInstancesBackupsNew</td>
                    <td>根据指定条件查询备份列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestoreTables</td>
                    <td>获取GeminiDB(for Cassandra)实例表级恢复的表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRedisPitrRestoreTime</td>
                    <td>查询Redis可恢复时间点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetBackupPolicy</td>
                    <td>设置自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreExistingInstance</td>
                    <td>恢复到已有实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBack</td>
                    <td>创建手动备份。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRecyclePolicy</td>
                    <td>设置已删除实例保留天数,修改保留天数后删除的实例按照新的天数保留,修改之前已在回收站的实例保留天数不变。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecyclePolicy</td>
                    <td>查询回收策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecycleInstances</td>
                    <td>查询回收站所有引擎的实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRestorableList</td>
                    <td>查询用户可恢复的实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupPolicy</td>
                    <td>查询自动备份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRedisPitrPolicy</td>
                    <td>设置Redis恢复到指定时间点策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="52">实例管理</td>
                    <td>UpdatePasswordlessConfig</td>
                    <td>支持修改GeminiDB Redis的免密配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbCacheMappings</td>
                    <td>根据指定条件查询内存加速映射关系列表和详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRedisDisabledCommands</td>
                    <td>查询Redis禁用命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveRedisDisabledCommands</td>
                    <td>设置Redis禁用命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableFlavorInfos</td>
                    <td>查询实例可变更规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyPort</td>
                    <td>修改数据库实例的端口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnlargeFailNode</td>
                    <td>删除扩容失败的节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckWeekPassword</td>
                    <td>判断弱密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyPublicIp</td>
                    <td>实例下的节点绑定弹性公网IP/解绑弹性公网IP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNosqlTaskList</td>
                    <td>根据指定条件查询定时任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRedisDisabledCommands</td>
                    <td>删除Redis禁用命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbCacheMapping</td>
                    <td>创建内存加速映射。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelInstanceScheduleWindow</td>
                    <td>取消定时任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchOver</td>
                    <td>切换实例的主备节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHighRiskCommands</td>
                    <td>查询Redis的高危命令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeDbVersion</td>
                    <td>升级数据库补丁版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShrinkInstanceNode</td>
                    <td>缩容指定集群实例的节点数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSecondLevelMonitoring</td>
                    <td>开启或关闭指定实例的5秒级监控。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>修改实例的管理员密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceMaintenanceWindow</td>
                    <td>查询实例可维护时间段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAutoEnlargePolicy</td>
                    <td>设置磁盘自动扩容策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRedisBigKeys</td>
                    <td>支持查询Redis实例的大key。value长度大于bigkeys-string-threshold参数的string类型的key或者元素数大于bigkeys-composite-threshold参数的hash/list/zset/set/stream类型key,会被判断为大key。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHighRiskCommands</td>
                    <td>批量修改高危命令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDbCacheRule</td>
                    <td>删除内存加速规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbCacheRules</td>
                    <td>查询内存加速规则列表和详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>根据指定条件查询数据库实例列表和详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesSession</td>
                    <td>获取节点会话列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRedisHotKeys</td>
                    <td>支持查询Redis实例的热key。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceName</td>
                    <td>修改实例名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecurityGroup</td>
                    <td>变更实例关联的安全组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpgradeDatabaseVersion</td>
                    <td>批量升级数据库补丁版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIpNumRequirement</td>
                    <td>查询创建实例或扩容节点时需要的IP数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSsl</td>
                    <td>切换实例SSL开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyVolume</td>
                    <td>变更实例的存储容量大小</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeColdVolume</td>
                    <td>扩容冷数据存储。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>创建数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeInstanceVolume</td>
                    <td>扩容实例的存储容量大小。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDbCacheMapping</td>
                    <td>解除指定内存加速映射。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandInstanceNode</td>
                    <td>扩容指定集群实例的节点数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetInstanceDataDump</td>
                    <td>开启/关闭实例数据导出。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoEnlargePolicy</td>
                    <td>查询磁盘自动扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateColdVolume</td>
                    <td>‘创建冷数据存储’</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecondLevelMonitoringStatus</td>
                    <td>查询秒级监控配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPasswordlessConfig</td>
                    <td>获取GeminiDB Redis的免密配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbCacheRule</td>
                    <td>创建内存加速规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeInstance</td>
                    <td>变更实例的规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestartInstance</td>
                    <td>重启实例或节点的数据库服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyInstanceMaintenanceWindow</td>
                    <td>设置指定实例可维护时间段。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClientNetwork</td>
                    <td>修改副本集跨网段访问配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDbCacheRule</td>
                    <td>修改指定内存加速规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>OfflineNodes</td>
                    <td>当底层故障导致节点无法正常工作时,可以对该节点执行关机操作,关机后会由其他节点接管业务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">实例负载均衡管理</td>
                    <td>ShowElbIpGroup</td>
                    <td>查询实例负载均衡的IP访问黑白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchIpGroup</td>
                    <td>设置实例负载均衡的IP访问黑白名单,黑名单、白名单只能选一种,每次调用此接口覆盖之前的设置。关闭后不限制连接的源IP地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">容灾管理</td>
                    <td>ShowPauseResumeStutus</td>
                    <td>获取容灾实例数据同步状态,主备实例id,数据同步指标值,以及倒换和切换场景下的RPO,RTO指标值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDisasterRecovery</td>
                    <td>解除实例与特定实例的容灾关系。 该接口需要对搭建容灾关系的两个实例分别各调用一次,2次接口都调用成功才能成功解除容灾关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDisasterRecoverySettings</td>
                    <td>查询实例容灾切换的故障节点比例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceBiactiveRegions</td>
                    <td>查询实例可搭建双活关系的Region。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGeminiDbDualActive</td>
                    <td>解除跨区域双活。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDisasterRecoverySettings</td>
                    <td>设置实例容灾切换的故障节点比例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceRole</td>
                    <td>该接口用于获取容灾实例主/备角色信息,以便后续容灾实例备升主和容灾实例主降备接口调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PauseResumeDataSynchronization</td>
                    <td>该接口用于暂停/恢复具备容灾关系的实例数据同步。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDisasterRecoveryOperation</td>
                    <td>校验实例是否可以与指定实例建立/解除容灾关系。若接口返回成功,表示可以与指定实例建立/解除容灾关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGeminiDbDualActive</td>
                    <td>为了实现跨区域实例数据同步,GeminiDB提供了异地双活功能,即创建异地双活实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchToMaster</td>
                    <td>该接口用于对已经搭建容灾关系的实例,将备实例升级为主实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDisasterRecovery</td>
                    <td>搭建实例与特定实例的容灾关系。 该接口需要对搭建容灾关系的两个实例分别各调用一次,2次接口都调用成功才能成功搭建容灾关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchToSlave</td>
                    <td>该接口用于对已经搭建容灾关系的实例,将主实例降级为备实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">日志管理</td>
                    <td>ListRedisSlowLogs</td>
                    <td>查询GeminiDB(for Redis)数据库慢日志信息,支持日志关键字搜索。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInfluxdbSlowLogs</td>
                    <td>查询GeminiDB(for influxdb)数据库慢日志信息,支持日志关键字搜索。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMongodbErrorLogs</td>
                    <td>查询GeminiDB(for Mongo)数据库错误日志信息,支持日志关键字搜索。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveLtsConfigs</td>
                    <td>- 将实例日志与LTS日志流关联,后台将自动上传实例日志到关联的LTS日志流里。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchSlowlogDesensitization</td>
                    <td>设置慢日志脱敏状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMongodbSlowLogs</td>
                    <td>查询GeminiDB(for Mongo)数据库慢日志信息,支持日志关键字搜索。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSlowLogDesensitization</td>
                    <td>查询慢日志脱敏状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLtsConfigs</td>
                    <td>分页查询实例关联的LTS日志配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLtsConfigs</td>
                    <td>将实例日志与LTS日志流解除关联,后台将取消上传实例日志到的LTS日志流里。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowErrorLog</td>
                    <td>查询数据库错误日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCassandraSlowLogs</td>
                    <td>查询GeminiDB(for Cassandra)数据库慢日志信息,支持日志关键字搜索。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSlowLogs</td>
                    <td>查询数据库慢日志信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询API版本</td>
                    <td>ListApiVersion</td>
                    <td>查询当前支持的API版本信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApiVersion</td>
                    <td>查询指定API版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询专属资源列表</td>
                    <td>ListDedicatedResources</td>
                    <td>查询专属资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询所有实例规格信息</td>
                    <td>ListFlavors</td>
                    <td>查询指定条件下的所有实例规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavorInfos</td>
                    <td>查询指定条件下的实例规格信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">查询数据库版本信息</td>
                    <td>ListDatastores</td>
                    <td>查询指定实例类型的数据库版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">标签管理</td>
                    <td>ListInstanceTags</td>
                    <td>查询指定实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTags</td>
                    <td>查询指定项目的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesByTags</td>
                    <td>根据标签查询指定的数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesByResourceTags</td>
                    <td>根据标签查询指定的数据库实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchTagAction</td>
                    <td>批量添加或删除指定数据库实例的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">管理数据库和用户</td>
                    <td>UpdateDatabases</td>
                    <td>操作GeminDB实例数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceDatabases</td>
                    <td>获取Redis实例数据库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetDbUserPassword</td>
                    <td>重置Redis数据库账号密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDbUser</td>
                    <td>在Redis实例中创建数据库帐号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyDbUserPrivilege</td>
                    <td>修改Redis数据库帐号权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDbUsers</td>
                    <td>获取Redis数据库账号列表和详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDbUser</td>
                    <td>删除Redis实例的数据库账号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">连接管理</td>
                    <td>ListInstanceSessions</td>
                    <td>获取实例的会话。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesSessionStatistics</td>
                    <td>查询实例节点会话统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ClearInstanceSessions</td>
                    <td>关闭实例所有节点会话。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstancesSession</td>
                    <td>关闭实例节点会话。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ShowQuotas</td>
                    <td>查询单租户在GeminiDB服务下的资源配额。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>