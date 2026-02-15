# WorkspaceApp MCP Server 

## 版本信息
v0.1.0

## 产品描述

WorkspaceApp MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务WorkspaceApp交互的能力。可以基于自然语言对WorkspaceApp资源进行全链路管理。

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
                    <td rowspan="8">AppWareHouse</td>
                    <td>DeleteWarehouseApp</td>
                    <td>删除应用仓库中的指定应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AuthorizeObs</td>
                    <td>获取上传至OBS桶的临时ak/sk。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWarehouseApp</td>
                    <td>在应用仓库中新增应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBucketOrAcl</td>
                    <td>添加桶或者桶授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWarehouseApps</td>
                    <td>查询租户应用仓库中的应用列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWarehouseApp</td>
                    <td>修改应用仓库中的指定应用信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadWarehouseAppIcon</td>
                    <td>在应用仓库中上传图标文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteWarehouseApp</td>
                    <td>批量删除应用仓库中的指定应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Application</td>
                    <td>DeleteAppIcon</td>
                    <td>删除自定义应用应用图标,恢复使用默认应用图标,重复执行会按照成功处理(响应200)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadAppIcon</td>
                    <td>修改自定义应用图标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchEnableApp</td>
                    <td>批量启用应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublishedApp</td>
                    <td>查询已发布的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublishableApp</td>
                    <td>查询应用组下可发布的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishApp</td>
                    <td>批量发布应用,不允许发布同名的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>编辑修改应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisableApp</td>
                    <td>批量禁用应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppDetail</td>
                    <td>查询应用详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnpublishApp</td>
                    <td>批量取消应用发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ApplicationConfig</td>
                    <td>InitializeTenant</td>
                    <td>租户服务激活。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTenantProfile</td>
                    <td>查询租户信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCorpConfigInfo</td>
                    <td>配置加载顺序: 查询企业级配置--&gt; 查不到则赋默认阿波罗配置--&gt; 阿波罗没有则不返回。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">ApplicationGroup</td>
                    <td>CreateAppGroup</td>
                    <td>该API用于创建应用组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppGroupDetail</td>
                    <td>查询应用组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppGroup</td>
                    <td>查询用户创建的应用组,按照名称、授权类型分页查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppGroup</td>
                    <td>修改应用组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppGroup</td>
                    <td>删除指定的应用组,重复执行会按照成功处理(响应200)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAppGroup</td>
                    <td>批量删除应用组,重复执行会按照成功处理(响应200)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateAppGroup</td>
                    <td>解除服务组关联的所有应用组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ApplicationOrder</td>
                    <td>CreateOrder</td>
                    <td>创建订单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ApplicationProduct</td>
                    <td>ListProduct</td>
                    <td>查询云应用套餐,按照条件过滤。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSessionTypes</td>
                    <td>该接口用于查询会话套餐列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSessionType</td>
                    <td>该接口用于查询会话套餐列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Authorization</td>
                    <td>BatchDeleteAppGroupAuthorization</td>
                    <td>移除应用组内的指定用户的授权,用户授权删除后,用户将没有权限访问应用组内的任何应用。注意:重复执行会按照操作成功处理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppGroupAuthorization</td>
                    <td>查询应用内已授权的用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAppGroupAuthorization</td>
                    <td>应用组添加用户授权,授权后用户就获得应用组下所有已发布应用的权限访问。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">AvailabilityZone</td>
                    <td>ListAz</td>
                    <td>该接口用于查询支持的可用分区列表,按站点分类。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailabilityZone</td>
                    <td>该接口用于查询支持的可用分区列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">ImageServer</td>
                    <td>CreateImageServer</td>
                    <td>创建镜像实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RecreateServerImage</td>
                    <td>构建云应用镜像。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageServer</td>
                    <td>查询指定的镜像实例当前这个接口的查询数据和list查询的一致</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteImageServer</td>
                    <td>批量删除镜像实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLatestAttachedServerApp</td>
                    <td>查询最近一次分发软件信息列表,返回ID列表,不包含具体信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageServers</td>
                    <td>查询镜像实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateImageServer</td>
                    <td>修改镜像实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachImageServerApp</td>
                    <td>分发应用软件信息至镜像实例,管理员可以按需下载并安装应用软件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Job</td>
                    <td>ShowJob</td>
                    <td>查询Job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageSubJobs</td>
                    <td>该接口用于查询异步子任务执行情况,sub_job_ids非空时offset和limit不会生效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteAppSubJobs</td>
                    <td>批量删除子任务,忽略不存在的服务器并且返回成功响应。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageJobs</td>
                    <td>该接口用于查询租户的异步任务执行情况</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountSubJobs</td>
                    <td>该接口用于查询异步子任务数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobDetail</td>
                    <td>查询Job的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSubJobs</td>
                    <td>该接口用于查询异步子任务执行情况,sub_job_ids非空时offset和limit不会生效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImageJob</td>
                    <td>该接口用于查询异步任务的执行情况,比如查询创建镜像实例任务的执行状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteImageSubJobs</td>
                    <td>批量删除子任务,忽略不存在的服务器并且返回成功响应。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Mail</td>
                    <td>ListAuthorizationMailRecord</td>
                    <td>查询应用组授权邮件发送记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendAuthorizationMail</td>
                    <td>重发应用组授权邮件(根据授权邮件记录)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendAuthorizedMail</td>
                    <td>重发应用组授权邮件(根据授权记录)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">Persistent</td>
                    <td>CreateShareFolder</td>
                    <td>创建共享存储目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSfs3Storage</td>
                    <td>查询SFS3.0存储。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePersistentStorage</td>
                    <td>创建WKS存储,目前仅支持创建 SFS3.0 容量型文件系统。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePersistentStorage</td>
                    <td>删除WKS存储。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePersistentStorage</td>
                    <td>删除共享存储,只会解除NAS与文件系统之间的关联关系,不会删除文件系统和文件系统中的数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrUpdateStoragePolicyStatement</td>
                    <td>新增或更新存储目录访问权限自定义策略(已存在自定义策略时会对已有策略更新)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPersistentStorage</td>
                    <td>查询WKS存储。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListShareFolder</td>
                    <td>查询共享存储目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUserStorageAttachment</td>
                    <td>删除个人存储目录,个人目录中的数据也将永久删除且无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateShareFolderAssignment</td>
                    <td>批量添加或者移除共享目录成员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStorageAssignment</td>
                    <td>查询个人存储目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStorageClaim</td>
                    <td>删除共享存储目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStoragePolicyStatement</td>
                    <td>查询存储目录访问权限策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserFolderAssignment</td>
                    <td>创建个人存储目录,已存在对应目录时,仅更新策略不会重复创建目录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">PolicyGroup</td>
                    <td>UpdatePolicyTemplate</td>
                    <td>修改指定策略模板的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicyTemplate</td>
                    <td>新增策略模板。策略模板创建好后,用户在创建策略组的时候,就可以根据已有策略模板按需调整配置,快速完成策略组的创建。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyGroup</td>
                    <td>查询策略组概要信息列表,包括应用对象和详细策略项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePolicyGroup</td>
                    <td>删除指定策略组,包含策略组对应的策略信息以及应用对象信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePolicyGroup</td>
                    <td>修改指定策略组的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyOfPolicyGroup</td>
                    <td>查询指定策略组内的策略项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePolicyTemplate</td>
                    <td>删除指定策略模板,包含策略模板对应的策略信息以及应用对象信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePolicyGroup</td>
                    <td>新增策略组,通过策略组能灵活的控制客户端访问与接入策略,如:文件、剪切板、会话等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTargetsOfPolicyGroup</td>
                    <td>查询指定策略组所应用的对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyGroupDetailInfo</td>
                    <td>包含策略信息以及应用对象的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPolicyGroup</td>
                    <td>根据策略组ID查询策略组详细信息,包含策略信息以及应用对象信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyTemplate</td>
                    <td>查询策略模板概要信息列表,包含策略信息以及应用对象信息。用户在创建策略组的时候,可以根据已有策略模板按需调整配置,快速完成策略组的创建。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOriginalPolicyInfo</td>
                    <td>查询初始策略项,初始策略项是所有协议策略配置项的默认配置,用户可以在初始策略项的基础上根据需求修改指定的配置,创建新的策略组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>CheckQuota</td>
                    <td>配额校验,购买服务器前可用调用该接口,校验本次创建服务器资源是否足够。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ScalingPolicy</td>
                    <td>CreateOrUpdateScalingPolicy</td>
                    <td>新增/修改弹性伸缩策略,仅按需的服务器支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScalingPolicy</td>
                    <td>删除弹性伸缩策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScalingPolicy</td>
                    <td>查询服务器组弹性伸缩策略,如果服务器未配置策略时响应默认策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">ScheduleTask</td>
                    <td>ListScheduleTasks</td>
                    <td>查询定时任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScheduleTask</td>
                    <td>修改定时任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScheduleTask</td>
                    <td>新增定时任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFutureExecutions</td>
                    <td>未来执行的具体时间列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScheduleTask</td>
                    <td>删除任务,忽略不存在的任务并且返回成功响应。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskExecuteDetail</td>
                    <td>查询定时任务执行子任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteScheduleTask</td>
                    <td>批量删除定时任务,忽略不存在的服务器组并且返回成功响应。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScheduleTask</td>
                    <td>查询指定定时任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskExecuteHistory</td>
                    <td>查询定时任务执行列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="25">Server</td>
                    <td>BatchUpgradeHdaVersion</td>
                    <td>批量升级服务器HDA版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerHdaDetails</td>
                    <td>查询服务器的HDA相关信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerMetricData</td>
                    <td>查询指定时间范围指定指标的指定粒度的监控数据,可以通过参数指定需要查询的数据维度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStartServer</td>
                    <td>启动服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServer</td>
                    <td>删除服务器,忽略不存在的服务器并且返回成功响应。订单退订成功后调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServer</td>
                    <td>修改服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServer</td>
                    <td>查询指定的服务器当前这个接口的查询数据和list查询的一致。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteServer</td>
                    <td>批量删除服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateTsvi</td>
                    <td>批量更新服务器虚拟会话IP配置,按需重启机器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerHdaUpgradeRecords</td>
                    <td>查询服务器的HDA升级跟踪记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServers</td>
                    <td>查询服务器列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRejoinDomain</td>
                    <td>批量服务器重新加入AD域,一般用于解决服务器脱域的情况使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeServerImage</td>
                    <td>修改服务器的镜像。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppServers</td>
                    <td>创建云服务器接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchMigrateHostsServer</td>
                    <td>迁移云办公主机下面的服务器到目标云办公主机。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessAgentLatestVersion</td>
                    <td>查询租户的所有HDA最新版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebootServer</td>
                    <td>重启服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchChangeServerImage</td>
                    <td>批量修改服务器的镜像。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerVnc</td>
                    <td>获取VNC远程登录地址。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAccessAgentLatestVersion</td>
                    <td>查询租户的HDA最新版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchStopServer</td>
                    <td>关闭服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchReinstallServer</td>
                    <td>批量重装服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerMetricData</td>
                    <td>该接口可获取某一计算机在一段时间段(范围:1小时到30天)的数据信息(例如CPU占用率、内存占用率、用户的在线时间段等),最长数据保存时间不能超过180天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ReinstallServer</td>
                    <td>重装服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchChangeServerMaintainMode</td>
                    <td>标记服务器维护状态,处于维护状态中的服务器不再分配流量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">ServerGroup</td>
                    <td>ShowServerGroupState</td>
                    <td>查询指定的服务器组内服务器状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateServerGroup</td>
                    <td>创建服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServerGroup</td>
                    <td>修改服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTenantServerGroups</td>
                    <td>查询租户服务器组基础信息列表(用于创建应用组时绑定服务器组)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerGroup</td>
                    <td>查询指定的服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerGroups</td>
                    <td>查询服务器组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerGroups</td>
                    <td>删除服务器组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerGroupRestrict</td>
                    <td>指定租户服务器组限制查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Session</td>
                    <td>ListUserConnection</td>
                    <td>查询用户登录记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LogoffUserSession</td>
                    <td>用户会话注销。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSessions</td>
                    <td>查询用户会话列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppConnection</td>
                    <td>查询应用使用记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSessionByUserName</td>
                    <td>根据用户名查询当前会话。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Tag</td>
                    <td>BatchDeleteServerGroupTags</td>
                    <td>此接口为幂等接口:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteServerGroupTags</td>
                    <td>此接口为幂等接口:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServerGroupTag</td>
                    <td>查询指定服务器组的标签信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateServerGroupTags</td>
                    <td>此接口为幂等接口:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateServerGroupTags</td>
                    <td>此接口为幂等接口:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServerGroupTag</td>
                    <td>查询租户在所有服务器组上的资源标签集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">VolumeType</td>
                    <td>ListVolumeType</td>
                    <td>该接口用于查询可用磁盘类型。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>