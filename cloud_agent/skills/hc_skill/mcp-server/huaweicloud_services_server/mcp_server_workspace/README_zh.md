# Workspace MCP Server 

## 版本信息
v0.1.0

## 产品描述

Workspace MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务Workspace交互的能力。可以基于自然语言对Workspace资源进行全链路管理。

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
                    <td rowspan="2">AccessConfig</td>
                    <td>ListAccessAddressBackupConfig</td>
                    <td>该接口用于获取云办公服务接入地址备份配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAccessAddressBackupConfig</td>
                    <td>该接口用于修改云办公服务接入地址备份配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">AccessPolicy</td>
                    <td>CreateAccessPolicy</td>
                    <td>该接口用于创建接入策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessPolicies</td>
                    <td>该接口用于查询接入策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAccessPolicyObjects</td>
                    <td>该接口用于更新指定接入策略的应用对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAccessPolicies</td>
                    <td>该接口用于删除指定接入策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAccessPolicy</td>
                    <td>该接口用于更新指定接入策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessPolicyObjects</td>
                    <td>该接口用于查询指定接入策略的应用对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Agency</td>
                    <td>ListAgencies</td>
                    <td>查询委托功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgencies</td>
                    <td>开通委托功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Alarms</td>
                    <td>ListAlarmStatistics</td>
                    <td>返回各级别告警数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAlarms</td>
                    <td>从ces查询告警列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">AppCenter</td>
                    <td>ListJobs</td>
                    <td>查询应用安装job信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateAppAuthorizations</td>
                    <td>批量设置应用授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppAuthorizations</td>
                    <td>设置应用授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApps</td>
                    <td>按照名称分页查询应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisableApps</td>
                    <td>批量设置不可见。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUploadedApp</td>
                    <td>修改应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchEnableApps</td>
                    <td>批量设置可见。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadApp</td>
                    <td>添加应用应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>删除应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryJobs</td>
                    <td>重试指定失败job(仅支持失败job重试,其他类型job重试会响应错误)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppAuthorizations</td>
                    <td>查询应用授权信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBucketCredential</td>
                    <td>生成桶凭证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteApps</td>
                    <td>批量删除应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchInstallApps</td>
                    <td>批量自动安装安装应用 (应用需支持静默安装或者解压安装)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InstallApp</td>
                    <td>自动安装应用(应用需支持静默安装或者解压安装)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteJobs</td>
                    <td>批量删除job。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAndAuthorizeBucket</td>
                    <td>添加并授权默认桶,桶不存在时会自动创建OBS桶。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppCatalogs</td>
                    <td>查询应用分类信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">AppRule</td>
                    <td>EnableRuleRestriction</td>
                    <td>启用规则管控。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRestrictedRule</td>
                    <td>查询管控规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppRule</td>
                    <td>修改应用规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppRule</td>
                    <td>创建应用规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppRule</td>
                    <td>查询应用规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRuleRestriction</td>
                    <td>设置管控规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppRule</td>
                    <td>删除应用规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAppRules</td>
                    <td>批量删除规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRestrictedRule</td>
                    <td>批量删除管控规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRuleRestriction</td>
                    <td>查询管控规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddRestrictedRule</td>
                    <td>增加管控规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableRuleRestriction</td>
                    <td>禁用规则管控。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AuthConfig</td>
                    <td>ShowAuthConfig</td>
                    <td>查询认证登录方式配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssistAuthConfig</td>
                    <td>查询辅助认证的配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAssistAuthMethodConfig</td>
                    <td>更新辅助认证策略配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuthMethodConfig</td>
                    <td>更新认证策略配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">AvailabilityZone</td>
                    <td>ListAzs</td>
                    <td>该接口用于查询云桌面支持的可用分区列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAzDetails</td>
                    <td>该接口用于查询云桌面支持的可用分区列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailabilityZones</td>
                    <td>该接口用于查询云桌面支持的可用分区列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Connection</td>
                    <td>ExportUserLoginInfoNew</td>
                    <td>该接口用于导出连接记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoginRecordsNew</td>
                    <td>该接口用于查询登录信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistoryOnlineInfoNew</td>
                    <td>该接口用于查询登录人数,注意查询参数不可全空。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesStatus</td>
                    <td>该接口用于查询桌面登录状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="37">Desktop</td>
                    <td>CancelRemoteAssistance</td>
                    <td>取消远程协助。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeDesktopToImage</td>
                    <td>桌面转镜像。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeDesktop</td>
                    <td>变更云桌面规格,只支持变更CPU和内存,不支持变更磁盘,不支持同规格互相变更。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterDomain</td>
                    <td>该接口用于Windows桌面重新加入AD域,一般用于解决桌面脱域的情况使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopsDetail</td>
                    <td>查询桌面详情信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchChangeDesktopNetwork</td>
                    <td>批量切换桌面vpc、子网、ip、安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchInstallAgent</td>
                    <td>批量为桌面安装agent。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachInstances</td>
                    <td>将桌面分配给用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchLogoffDesktops</td>
                    <td>批量注销桌面。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteDesktops</td>
                    <td>批量删除桌面,删除后无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopsConnectStatus</td>
                    <td>查询桌面连接状态列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRemoteConsoleAddress</td>
                    <td>用于直接获取远程登录控制台地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDesktopNetworks</td>
                    <td>查询桌面vpc、子网、privateIp、EIP、安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgentsInstallCondition</td>
                    <td>展示桌面安装agent详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeUserPrivilegeGroup</td>
                    <td>批量修改用户权限组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDetachInstances</td>
                    <td>批量将桌面和用户解绑。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesktop</td>
                    <td>修改桌面属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetMaintenanceMode</td>
                    <td>批量设置桌面管理员维护模式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRemoteAssistance</td>
                    <td>创建远程协助。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDesktopMonitorData</td>
                    <td>该接口可获取某一计算机在一段时间段(范围:1小时到30天)的数据信息(例如CPU占用率、内存占用率、用户的在线时间段等),最长数据保存时间不能超过180天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebuildDesktopsSystemDisk</td>
                    <td>批量重建桌面系统盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesktopUsername</td>
                    <td>AD场景支持桌面更换关联用户名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDesktopNetwork</td>
                    <td>查询桌面vpc、子网、privateIp、EIP、安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDesktopDetail</td>
                    <td>指定桌面Id查询详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesktop</td>
                    <td>创建桌面,并将此桌面分配给用户,当桌面创建成功后用户可以登录使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopActions</td>
                    <td>获取桌面开关机信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRunDesktops</td>
                    <td>批量操作桌面,用于批量开机、关机、休眠和重启。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesktop</td>
                    <td>删除单个桌面,删除后无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDesktopRemoteAssistanceInfo</td>
                    <td>根据桌面id查询远程协助信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateInstances</td>
                    <td>预批量将桌面分配给用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeDesktopNetwork</td>
                    <td>切换桌面vpc、子网、ip、安全组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSysprepInfo</td>
                    <td>查询sysprep版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesktopSids</td>
                    <td>该接口用于桌面sid和WindowsAD中的SID不同时,更新桌面SID使其与AD中的SID保持一致,一般用于解决桌面脱域的情况使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachInstances</td>
                    <td>将桌面和用户解绑。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAttachInstances</td>
                    <td>批量分配桌面给用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendNotifications</td>
                    <td>用于管理员向桌面发送消息通知。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktops</td>
                    <td>该接口用于查询桌面虚拟机列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DesktopNamePolicy</td>
                    <td>CreateDesktopNamePolicy</td>
                    <td>创建桌面名称策略,用于自动生成桌面名称,最多允许50个。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteDesktopNamePolicy</td>
                    <td>批量删除桌面名称策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopNamePolicy</td>
                    <td>获取桌面名称策略,用于自动生成桌面名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesktopNamePolicy</td>
                    <td>更新桌面名称策略,用于自动生成桌面名称。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">DesktopPool</td>
                    <td>ResizeDesktopPool</td>
                    <td>桌面池变更规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopPoolAuthorizedObjects</td>
                    <td>该接口用于查询指定桌面池授权的用户、用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPoolDesktopsDetail</td>
                    <td>该接口用于查询桌面池下的桌面信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDesktopPoolVolumes</td>
                    <td>桌面池批量添加磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDesktopPoolAction</td>
                    <td>操作桌面池,用于桌面池里面的桌面批量开机、关机、重启和休眠。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDesktopPoolScript</td>
                    <td>桌面池批量执行脚本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesktopPool</td>
                    <td>创建桌面池,可将此桌面池分配给用户、用户组,用户登录时会绑定其中一个桌面。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebuildDesktopPool</td>
                    <td>桌面池重建系统盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesktopPool</td>
                    <td>当桌面池内无桌面时可删除桌面池,桌面池删除后无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendDesktopPoolNotifications</td>
                    <td>用于管理员向桌面发送消息通知。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesktopPoolVolumes</td>
                    <td>桌面池批量删除磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDesktopPool</td>
                    <td>修改桌面池属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDesktopPoolsScriptExecTasks</td>
                    <td>桌面池的脚本执行任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDesktopPoolDetail</td>
                    <td>指定桌面池Id查询详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesktopPoolAuthorizedObjects</td>
                    <td>该接口用于桌面池授权用户、用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandDesktopPool</td>
                    <td>扩容桌面池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandDesktopPoolVolumes</td>
                    <td>桌面池批量扩容磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopPools</td>
                    <td>该接口用于查询桌面池列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">DesktopTag</td>
                    <td>BatchChangeTags</td>
                    <td>为指定桌面批量添加或删除标签。创建时,如果创建的标签已经存在(key相同),则覆盖。删除时,如果删除的标签不存在,默认处理成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAddDesktopsTags</td>
                    <td>同时对多个桌面批量添加标签,如果创建的标签已经存在(key相同)则覆,最大支持100个桌面,每个桌面最大20个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTag</td>
                    <td>该接口用于为桌面创建标签,一个桌面上最多有10个标签。创建时,如果创建的标签已经存在(key相同),则覆盖。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTagByDesktopId</td>
                    <td>查询指定桌面的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTags</td>
                    <td>查询租户的所有标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTag</td>
                    <td>该接口用于删除桌面标签。删除时,如果删除的标签不存在,默认处理成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteDesktopsTags</td>
                    <td>同时对多个桌面批量添加标签,删除时,如果删除的标签不存在默认处理成功,最大支持100个桌面,每个桌面最大20个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopByTags</td>
                    <td>使用标签过滤桌面。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Group</td>
                    <td>DeleteUserGroup</td>
                    <td>删除用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteUserGroups</td>
                    <td>该接口用于批量删除用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserGroup</td>
                    <td>该接口用于修改用户组信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunActionsOnGroup</td>
                    <td>操作用户组,如添加用户、删除用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserGroups</td>
                    <td>查询用户组列表,支持分页。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUserGroup</td>
                    <td>该接口用于创建用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsersOfGroup</td>
                    <td>该接口用于查询用户组中的用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Image</td>
                    <td>ListImages</td>
                    <td>该接口用于查询云桌面支持的产品镜像列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Images</td>
                    <td>ListMarketImages</td>
                    <td>获取云市场镜像列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Inquiry</td>
                    <td>EstimateChangeImages</td>
                    <td>批量包周期桌面切换镜像(由不收费镜像变更至收费镜像)询价。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EstimateDesktopPoolAddVolume</td>
                    <td>包周期桌面池添加单个磁盘批量询价。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EstimateAddResources</td>
                    <td>包周期桌面增配变更批量询价。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EstimateDesktopPoolChangeImage</td>
                    <td>包周期桌面池切换镜像(由不收费镜像变更至收费镜像)批量询价。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EstimateDesktopPoolExtendVolume</td>
                    <td>包周期桌面池扩容磁盘批量询价。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EstimateDesktopPoolResize</td>
                    <td>包周期桌面池变更规格批量询价。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job</td>
                    <td>RunActionsOnWorkspaceJob</td>
                    <td>该接口用来对失败的任务进行重试,当前仅支持开户和销户的任务重试。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Jobs</td>
                    <td>ShowJob</td>
                    <td>该接口用于查询异步任务的执行情况,比如查询创建桌面任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteSubJobs</td>
                    <td>该接口用于删除子任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListItaSubJobs</td>
                    <td>该接口用于查询异步任务执行情况,比如查询创建桌面的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">NatMappingConfigs</td>
                    <td>UpdateNatMappingConfigs</td>
                    <td>修改租户的NAT映射配置项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatMappingConfigs</td>
                    <td>查询租户的NAT映射配置项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="15">Network</td>
                    <td>ListPorts</td>
                    <td>查询端口列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateDesktopsEip</td>
                    <td>桌面绑定EIP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplySubnetBandwidth</td>
                    <td>创建按需云办公带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopsEips</td>
                    <td>查询已绑定桌面和未绑定的EIP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubnetBandwidthControlList</td>
                    <td>修改云办公带宽的控制配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUsingSubnets</td>
                    <td>根据子网id列表查询正在被桌面使用的子网id,并且返回subnetId列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInternet</td>
                    <td>查询上网功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyInternet</td>
                    <td>开通上网功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNatGateways</td>
                    <td>查询NAT网关列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisassociateDesktopsEip</td>
                    <td>批量桌面解绑EIP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubnetBandwidths</td>
                    <td>查询云办公带宽列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyDesktopsInternet</td>
                    <td>开通桌面上网功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubnetBandwidth</td>
                    <td>修改云办公带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSubnetBandwidth</td>
                    <td>删除云办公带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSubnetBandwidthControlList</td>
                    <td>查询云办公带宽的控制配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Order</td>
                    <td>CreateSubnetBandwidthChangeOrder</td>
                    <td>包周期云办公带宽变更下单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrder</td>
                    <td>包周期资源(桌面、磁盘)下订单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateChangeOrder</td>
                    <td>变更规格、扩容磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesktopBatchOrder</td>
                    <td>包周期桌面批量变更下单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesktopOrder</td>
                    <td>创建桌面订单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesktopPoolChangeOrder</td>
                    <td>包周期桌面池批量变更下单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Ou</td>
                    <td>ListOuDetails</td>
                    <td>查询OU列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateOuInfo</td>
                    <td>更新OU信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAdOus</td>
                    <td>查询AD里的OU列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddOu</td>
                    <td>该接口用于创建OU。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAdOuUsers</td>
                    <td>查询OU下用户信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOu</td>
                    <td>该接口用于删除OU信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">PolicyGroup</td>
                    <td>BatchUpdateTargetOfPolicyGroup</td>
                    <td>批量增加、删除应用对象到指定策略组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTargetOfPolicyGroup</td>
                    <td>查询指定策略组所应用的对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyDetailInfoById</td>
                    <td>根据策略组ID查询策略组详细信息,包含策略信息以及应用对象信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePoliciesOfPolicyGroup</td>
                    <td>修改一个策略组的部分或者所有策略项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyGroupInfo</td>
                    <td>包含策略信息以及应用对象的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyGroup</td>
                    <td>查询策略组概要信息列表,不包含策略信息以及应用对象信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePolicyGroup</td>
                    <td>删除指定策略组,包含策略组对应的策略信息以及应用对象信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPoliciesOfPolicyGroup</td>
                    <td>查询指定策略组内的策略项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyGroup</td>
                    <td>修改指定策略组的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicyGroup</td>
                    <td>新增策略组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOriginalPolicyInfo</td>
                    <td>查询初始策略项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Product</td>
                    <td>ListProducts</td>
                    <td>该接口用于查询云桌面支持的产品套餐列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSharerProducts</td>
                    <td>该接口用于查询协同套餐列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHourPackagesType</td>
                    <td>该接口用于查询可订购小时包类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Profile</td>
                    <td>UpdateTenantProfile</td>
                    <td>启禁用租户功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTenantProfiles</td>
                    <td>查询租户功能状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Quota</td>
                    <td>ShowQuotaDetails</td>
                    <td>查询租户单个站点配额详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQuotas</td>
                    <td>Console Framework和WKSDesktopManager调用该接口查询租户配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">ScheduledTask</td>
                    <td>CreateScheduledTasks</td>
                    <td>创建定时任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScheduledTasksRecords</td>
                    <td>查询定时任务执行记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScheduledTasks</td>
                    <td>查询定时任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScheduledTasks</td>
                    <td>查询定时任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScheduledTasks</td>
                    <td>删除定时任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteScheduledTasks</td>
                    <td>批量删除定时任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScheduledTasks</td>
                    <td>修改定时任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTimeZones</td>
                    <td>获取时区配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFutureExecutions</td>
                    <td>未来执行的具体时间列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScheduledTasksRecordsDetails</td>
                    <td>查询定时任务执行记录详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ScreenRecord</td>
                    <td>BatchDeleteScreenRecords</td>
                    <td>批量删除录屏记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopOperations</td>
                    <td>查询桌面关键事件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDownloadAddress</td>
                    <td>查询下载地址列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScreenRecords</td>
                    <td>查询录屏记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScreenRecord</td>
                    <td>查询录屏详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">Script</td>
                    <td>ShowScriptRecordDetail</td>
                    <td>查询脚本执行记录详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScript</td>
                    <td>更新脚本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScriptRecords</td>
                    <td>查询脚本执行记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScript</td>
                    <td>新增脚本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryScriptExecution</td>
                    <td>重试脚本或执行脚本失败的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopScriptExecution</td>
                    <td>停止脚本或者命令执行任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScript</td>
                    <td>删除脚本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScriptDetail</td>
                    <td>查询脚本详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScriptTasks</td>
                    <td>查询脚本任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScripts</td>
                    <td>查询脚本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteScriptOrCommand</td>
                    <td>批量执行脚本或命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ShareDesktop</td>
                    <td>DeleteDesktopSubResources</td>
                    <td>桌面删除附属资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDesktopSubResources</td>
                    <td>存量桌面购买附属资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">ShareSpaceConfig</td>
                    <td>UpdateShareSpaceConfig</td>
                    <td>设置协同桌面默认用户配置(当前功能公测中,需要使用请联系管理员申请使用)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowShareSpaceConfig</td>
                    <td>查询协同桌面默认用户配置(当前功能公测中,需要使用请联系管理员申请使用)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Site</td>
                    <td>UpdateAccessMode</td>
                    <td>用于修改站点接入方式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWksEdgeSites</td>
                    <td>查询边缘小站列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSite</td>
                    <td>用于删除站点的接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSite</td>
                    <td>用于查询站点信息的接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSiteConfigs</td>
                    <td>用于查询站点信息的接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSubnetIds</td>
                    <td>用于修改站点业务子网。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Snapshot</td>
                    <td>ListDesktopSnapshot</td>
                    <td>查询快照列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestoreDesktopSnapshot</td>
                    <td>批量恢快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteDesktopSnapshot</td>
                    <td>批量删除快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateDesktopSnapshot</td>
                    <td>批量创建快照。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">Statistics</td>
                    <td>ListMetricNotifyRecord</td>
                    <td>查询对应指标维度是否存在满足通知规则的记录;</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGrowthRate</td>
                    <td>查询指标环比值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopsStatistics</td>
                    <td>统计租户下的普通桌面、桌面池状态,默认仅统计总数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppUserAccessData</td>
                    <td>查询云应用接入统计数据,一次最多查询30天,支持最近30天的数据查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetrics</td>
                    <td>查询指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRunState</td>
                    <td>租户桌面运行状态统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricNotifyRule</td>
                    <td>查询对应指标的通知规则;。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserAccessStages</td>
                    <td>查询接入云桌面或云应用各阶段时长数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddMetricNotifyRule</td>
                    <td>新增对应指标的通知规则;对应指标满足相应的规则条件时发送通知</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDesktopUsageMetric</td>
                    <td>查询桌面使用统计信息;</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMetricNotifyRule</td>
                    <td>删除对应指标的通知规则;对应指标满足相应的规则条件时发送通知</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLoginState</td>
                    <td>查询租户桌面登录状态统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMetricNotifyRule</td>
                    <td>更新对应指标的通知规则;对应指标满足相应的规则条件时发送通知。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUnusedDesktops</td>
                    <td>查询在指定时间段未使用的桌面。已废弃,不推荐使用。统计数据推荐使用[查询桌面使用情况统计数据接口](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api=ListDesktopUsageMetric)和[查询用户使用统计数据接口](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api=ListUserUsageMetric)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetricsTrend</td>
                    <td>查询指标趋势。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsedDesktopInfo</td>
                    <td>查询使用桌面的时长。已废弃,不推荐使用。统计数据推荐使用[查询桌面使用情况统计数据接口](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api=ListDesktopUsageMetric)和[查询用户使用统计数据接口](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api=ListUserUsageMetric)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserUsageMetric</td>
                    <td>查询用户使用统计信息;</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Subnet</td>
                    <td>ShowAvailableIp</td>
                    <td>根据子网id查询该子网下可用的ip。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Tenant</td>
                    <td>ListTenantConfigs</td>
                    <td>查询租户个性配置列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTenantConfig</td>
                    <td>租户个性配置修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Terminal</td>
                    <td>DeleteTerminalsBindingDesktops</td>
                    <td>删除终端与桌面绑定配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTerminalsBindingDesktopsConfig</td>
                    <td>设置终端与桌面绑定的开关配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTerminalsBindingDesktopsConfig</td>
                    <td>查询终端与桌面绑定的开关配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTerminalsBindingDesktops</td>
                    <td>查询终端与桌面绑定配置列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTerminalsBindingDesktops</td>
                    <td>修改终端与桌面绑定配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTerminalsBindingDesktops</td>
                    <td>增加终端与桌面绑定配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">User</td>
                    <td>ListUsers</td>
                    <td>该接口用于查询桌面用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserInfo</td>
                    <td>该接口用于修改桌面用户信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteOtpDevices</td>
                    <td>该接口用于解绑用户的OTP设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendEmail</td>
                    <td>该接口用于重新发送邮件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetRandomPassword</td>
                    <td>该接口用于给用户重置一个密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeUserStatus</td>
                    <td>该接口用于操作用户,包含三种操作:锁定、解锁和重置密码(重置密码建议使用/v2/{project_id}/users/{user_id}/random-password接口,在没有通知方式的情况下必须使用/v2/{project_id}/users/{user_id}/random-password接口)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDesktopUser</td>
                    <td>该接口用于创建桌面用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserDetail</td>
                    <td>该接口用于查询指定的桌面用户详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUser</td>
                    <td>删除指定的桌面用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateUsers</td>
                    <td>该接口用于批量创建用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteUser</td>
                    <td>该接口用于批量删除桌面用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOtpDevicesByUserId</td>
                    <td>该接口用于查询相应用户下面的OTP设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">UserEvents</td>
                    <td>SetUserEventsLtsConfigurations</td>
                    <td>配置用户事件LTS。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserEvents</td>
                    <td>查询用户事件,一次最多查询30天,支持最近30天的数据查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserEventsLtsConfigurations</td>
                    <td>查询用户事件LTS配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Volume</td>
                    <td>ListVolumeProductInfo</td>
                    <td>查询磁盘产品信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDesktopVolumes</td>
                    <td>删除桌面数据盘,删除后无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandDesktopVolume</td>
                    <td>扩容磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddVolumes</td>
                    <td>批量增加桌面磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDesktopVolumes</td>
                    <td>给单个桌面增加磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandVolumes</td>
                    <td>扩容桌面磁盘。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Workspace</td>
                    <td>CancelWorkspace</td>
                    <td>该接口用于注销云办公服务。注销前请确保当前用户下的云桌面已经删除,注销后无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspaces</td>
                    <td>该接口用于查询云办公服务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkspace</td>
                    <td>该接口目前支持修改云办公服务属性。单次请求仅支持修改一种属性类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkspaceLock</td>
                    <td>查询云办公服务是否被锁定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyWorkspace</td>
                    <td>该接口用于开通云办公服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEnterpriseId</td>
                    <td>修改租户的企业ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnlockWorkspace</td>
                    <td>该接口目前支持解除云办公服务锁定状态。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>