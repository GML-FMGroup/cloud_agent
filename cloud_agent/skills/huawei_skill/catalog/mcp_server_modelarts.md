# ModelArts MCP Server 

## 版本信息
v0.1.0

## 产品描述

ModelArts MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务ModelArts交互的能力。可以基于自然语言对ModelArts资源进行全链路管理。

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
                    <td rowspan="5">AI应用管理</td>
                    <td>ShowModel</td>
                    <td>查询AI应用详情,根据AI应用ID查询AI应用的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteModel</td>
                    <td>删除AI应用,根据AI应用ID删除指定AI应用,cascade取值为true时除了删除AI应用ID指定的AI应用,还会删除其他与指定AI应用同名不同版本的AI应用;默认只删除当前AI应用ID所对应的AI应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowModelEngineAndRuntime</td>
                    <td>查询模型AI引擎以及runtime。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateModel</td>
                    <td>导入元模型创建AI应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListModels</td>
                    <td>查询AI应用列表,可以根据不同的检索参数进行查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="20">APP认证管理</td>
                    <td>CreateAndAuthAppAuthApi</td>
                    <td>注册API并将API授权给APP,只有对服务有更新权限的华为云用户可以调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetApigAppSecret</td>
                    <td>重置指定API网关应用的AppSecret,只有APP的创建用户才可以重置AppSecret。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetServiceAppAuthApiAuthInfo</td>
                    <td>查询服务授权的API、APP信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApiAppAuth</td>
                    <td>解除指定的API对APP的授权,请求用户对API所属服务必须有更新权限。同URL:/v1/{project_id}/app-auth/{service_id}/apis/{api_id}/auths</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApigAppCode</td>
                    <td>为指定API网关应用创建新的AppCode,只有APP的创建用户才可以创建AppCode,且只有共享/专享版APIG的APP才能创建AppCode。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApigApp</td>
                    <td>查询指定的APP详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApisBindToApp</td>
                    <td>获取用户绑定app的API列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApigApp</td>
                    <td>创建API网关应用(简称APP),每个用户最多只能创建5个APP,有需求可以申请增加配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppAuthApi</td>
                    <td>创建API,未将API授权给APP。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetApigAppCode</td>
                    <td>重置指定API网关应用的指定的AppCode,只有APP的创建用户才可以重置AppCode,且只有共享/专享版APIG的APP才支持AppCode。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AuthorizeApiToApigApps</td>
                    <td>将指定的API授权给APP。API的认证方式必须为APP认证,APP的创建用户必须是API所属服务的创建者,且请求用户对API所属服务必须有更新权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApigApps</td>
                    <td>获取APIG APP基本信息列表,用户只能获取自己创建的APP信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApigAppExists</td>
                    <td>查询APP是否存在。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetAppAuthApisInfo</td>
                    <td>查询APP的API认证信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApiAuthInfos</td>
                    <td>获取指定的API与APP授权关系列表,API的认证方式必须是APP认证,管理员可以获取所有API的授权信息,普通用户只能获取自己有访问权限的服务下的API的授权信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetAppAuthApiInfo</td>
                    <td>查询指定API详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApigApp</td>
                    <td>删除指定的APP,只有APP的创建用户才可以删除APP,且APP没有绑定的API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppAuthApi</td>
                    <td>删除指定的API,只有对API所属服务有删除权限的用户才可以删除API。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApigAppCode</td>
                    <td>删除指定API网关应用的指定的AppCode,只有APP的创建用户才可以删除AppCode,且只有共享/专享版APIG的APP才支持AppCode。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAuthApiToApigApps</td>
                    <td>更新API的授权关系。API的认证方式必须为APP认证,APP的创建用户必须是API所属服务的创建者,且请求用户对API所属服务必须有更新权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">DevServer管理</td>
                    <td>StartDevServer</td>
                    <td>启动DevServer实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevServer</td>
                    <td>删除DevServer实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDevServer</td>
                    <td>创建DevServer。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncDevServers</td>
                    <td>实时同步用户所有DevServer实例状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevServers</td>
                    <td>查询用户所有DevServer实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopDevServer</td>
                    <td>停止DevServer实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDevServer</td>
                    <td>查询DevServer实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">Notebook实例管理</td>
                    <td>ListFlavors</td>
                    <td>查询运行Notebook实例所支持的有效规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartNotebook</td>
                    <td>启动Notebook实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotebook</td>
                    <td>创建Notebook实例,可以根据您指定的实例规格,不同AI引擎镜像,存储等相关参数,为您创建一个Notebook,您可以通过网页和SSH客户端访问Notebook实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotebook</td>
                    <td>该接口用于更新Notebook实例,包括名称、描述信息、规格、镜像ID,该接口仅可以在Notebook实例停止状态下使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotebook</td>
                    <td>删除Notebook实例,删除的资源包括Notebook容器以及对应的所有存储资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNotebook</td>
                    <td>查询Notebook实例详情,可查询实例详细信息包括实例ID、名称、规格、镜像、实例状态和实例可打开的URL等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSwitchableFlavors</td>
                    <td>查询创建Notebook实例支持的可切换的规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImage</td>
                    <td>运行的实例可以保存成容器镜像,保存的镜像中,安装的依赖包(pip包)不丢失,VS Code远程开发场景下,在Server端安装的插件不丢失。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllNotebooks</td>
                    <td>查询所有Notebook实例列表,用户可按需查询满足条件的Notebook实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RenewLease</td>
                    <td>该接口用于延长运行中的Notebook实例的运行时间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLease</td>
                    <td>该接口用于查询运行中的Notebook实例的可用时长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopNotebook</td>
                    <td>停止Notebook实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotebooks</td>
                    <td>查询Notebook实例列表,用户可按需查询满足条件的Notebook实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Notebook标签管理</td>
                    <td>ShowNotebookTags</td>
                    <td>查询用户当前project下Notebook实例类型下的标签,默认查询所有工作空间,无权限不返回标签数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotebookTags</td>
                    <td>删除指定Notebook资源的标签,支持批量删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotebookTags</td>
                    <td>给指定Notebook资源添加标签,支持批量添加,当添加的标签key已存在,则覆盖该标签的value。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Workflow</td>
                    <td>ShowWorkflow</td>
                    <td>通过ID查询Workflow工作流详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowsOverview</td>
                    <td>获取Workflow工作流统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkflow</td>
                    <td>通过ID删除Workflow工作流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkflow</td>
                    <td>更新Workflow工作流信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflows</td>
                    <td>展示Workflow工作流列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflowServiceAuth</td>
                    <td>计费工作流在线服务鉴权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflow</td>
                    <td>创建Workflow工作流。可参考[如何开发Workflow](https://support.huaweicloud.com/usermanual-standard-modelarts/modelarts_workflow_0292.html),创建工作流。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflowPurchasePool</td>
                    <td>计费工作流购买资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowsTodolist</td>
                    <td>获取Workflow待办列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">WorkflowExecution</td>
                    <td>ShowWorkflowExecution</td>
                    <td>通过ID查询Workflow Execution详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkflowExecution</td>
                    <td>通过ID删除Workflow Execution。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflowExecutionsActions</td>
                    <td>本接口支持对Workflow Execution进行停止或重跑操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflowExecution</td>
                    <td>创建Workflow Execution。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflowExecutions</td>
                    <td>查询Workflow下的执行记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkflowExecution</td>
                    <td>通过ID更新Workflow Exectuion。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflowStepExecutionsActions</td>
                    <td>本接口支持对Workflow StepExecution进行重试、停止和继续操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowStepExecutionMetrics</td>
                    <td>获取Workflow工作流节点的度量信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">WorkflowSchedule</td>
                    <td>UpdateWorkflowSchedule</td>
                    <td>更新WorkflowSchedule信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflowSchedule</td>
                    <td>创建Workflow定时调度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkflowScheduleId</td>
                    <td>删除工作流调度信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowSchedule</td>
                    <td>查询工作流调度详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">WorkflowSubscription</td>
                    <td>DeleteWorkflowSubscription</td>
                    <td>删除已订阅的消息订阅Subscription。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkflowSubscription</td>
                    <td>更新Workflow工作流已订阅的订阅信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflowSubscription</td>
                    <td>查询Workflow工作流已订阅的订阅信息详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflowSubscriptions</td>
                    <td>为Workflow工作流添加消息订阅功能。工作流已订阅的事件发生时,会产生消息提醒。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">事件管理</td>
                    <td>ListEvents</td>
                    <td>查询事件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">动态挂载OBS</td>
                    <td>ShowAttachableObs</td>
                    <td>获取动态挂载OBS实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachObs</td>
                    <td>在运行中的Notebook实例,支持将“OBS并行文件系统”挂载到实例中指定的文件目录,挂载后可以在容器中以文件系统操作方式完成OBS并行文件系统对象的读写。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelObs</td>
                    <td>卸载后,OBS存储中的对象保持不变,Notebook容器中无法再操作OBS对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttachableObSs</td>
                    <td>获取动态挂载OBS实例信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">工作空间管理</td>
                    <td>UpdateWorkspace</td>
                    <td>修改工作空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkspaceQuotas</td>
                    <td>修改工作空间配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkspace</td>
                    <td>查询工作空间详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspace</td>
                    <td>查询工作空间列表,响应消息体中包含详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkspace</td>
                    <td>删除工作空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkspaceQuotas</td>
                    <td>查询工作空间配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkspace</td>
                    <td>创建工作空间("default"为系统预留的默认工作空间名称,不能使用)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">授权管理</td>
                    <td>CreateModelArtsAgency</td>
                    <td>创建包含OBS、SWR、IEF等依赖服务的ModelArts委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAuthorization</td>
                    <td>配置ModelArts授权。若没有授权,ModelArts训练管理、开发环境、数据管理、在线服务等功能将不能正常使用。该API支持管理员给IAM子用户设置委托,支持设置当前用户的访问密钥。调用该API需要在IAM系统里配置Security Administrator权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuthorizations</td>
                    <td>删除指定用户的授权或者删除全量用户的授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetAuthorizations</td>
                    <td>查看授权列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">插件模板管理</td>
                    <td>ShowPluginTemplate</td>
                    <td>获取指定插件模板的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="17">服务管理</td>
                    <td>BatchDeleteServiceTags</td>
                    <td>删除服务(目前只支持在线服务)的标签,支持批量删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServiceMonitorInfo</td>
                    <td>查询服务监控信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeNodeStatus</td>
                    <td>启动停止边缘节点服务实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateServiceByProperty</td>
                    <td>更新模型服务的单个属性,目前只支持instance_count(更新模型服务实例数量),仅运行中、告警、异常状态下的在线服务可以执行该操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServiceSpecifications</td>
                    <td>查询支持的服务部署规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateService</td>
                    <td>将模型部署为服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>查询专属资源池列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateServiceTags</td>
                    <td>给指定服务添加标签(目前只支持在线服务),当添加的标签key已存在,则覆盖该标签的value。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServiceUpdateLogs</td>
                    <td>查询实时服务更新日志。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServices</td>
                    <td>查询模型服务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowService</td>
                    <td>查询模型服务详情,根据服务ID查询服务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PatchServiceV2</td>
                    <td>通过patch操作对服务进行更新。patch的格式可以参照json patch。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServiceTags</td>
                    <td>查询当前项目下的推理服务标签,默认查询所有工作空间,无权限不返回标签数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteService</td>
                    <td>删除模型服务,仅可删除本人名下的服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowServiceEvents</td>
                    <td>查询服务事件日志,包含服务的操作记录及部署过程中的关键动作、部署失败原因。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInternalChannelVpcepApi</td>
                    <td>该接口用于查询推理VPC访问通道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateService</td>
                    <td>更新模型服务配置。也可以使用此接口启停服务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">算法管理</td>
                    <td>ListAlgorithms</td>
                    <td>查询算法列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSearchAlgorithms</td>
                    <td>获取支持的超参搜索算法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeTrainingExperiment</td>
                    <td>通过实验ID更新训练实验信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeAlgorithm</td>
                    <td>更新算法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAlgorithmByUuid</td>
                    <td>根据算法id查询指定算法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAlgorithm</td>
                    <td>删除算法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAlgorithm</td>
                    <td>创建一个算法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">网络管理</td>
                    <td>ListNetworks</td>
                    <td>查询网络资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNetwork</td>
                    <td>创建网络资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PatchNetwork</td>
                    <td>更新指定网络资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNetwork</td>
                    <td>删除指定网络资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNetwork</td>
                    <td>查询指定网络资源的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">节点池管理</td>
                    <td>ListNodePoolNodes</td>
                    <td>查询节点池的节点列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNodePool</td>
                    <td>创建节点池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodePools</td>
                    <td>查询节点池列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodePool</td>
                    <td>查询指定节点池详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PatchNodePool</td>
                    <td>更新节点池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNodePool</td>
                    <td>删除节点池。包周期资源池不支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">节点管理</td>
                    <td>ListPoolNodes</td>
                    <td>查询资源池中的节点列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRebootPoolNodes</td>
                    <td>批量重启指定资源池中的节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePoolNodes</td>
                    <td>批量删除指定资源池中的节点,资源池中至少保留一个节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">节点配置模板</td>
                    <td>ShowNodeConfigTemplate</td>
                    <td>获取指定节点配置模板的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="22">训练作业管理</td>
                    <td>ShowTrainJobTags</td>
                    <td>查询训练作业标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSaveImageJob</td>
                    <td>查询训练作业镜像保存任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrainJobTags</td>
                    <td>删除训练作业标签,支持批量删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrainingJobEvents</td>
                    <td>获取训练作业事件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoSearchTrials</td>
                    <td>查询超参搜索所有trial的结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoSearchYamlTemplatesInfo</td>
                    <td>获取自动化搜索作业yaml模板的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeTrainingJobDescription</td>
                    <td>更新训练作业描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrainingJobDetails</td>
                    <td>查询训练作业详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTrainingJob</td>
                    <td>删除训练作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrainingJobLogsPreview</td>
                    <td>查询训练作业指定任务的日志(预览)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoSearchYamlTemplateContent</td>
                    <td>获取自动化搜索作业yaml模板的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSaveImageJob</td>
                    <td>创建训练作业镜像保存任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrainJobTags</td>
                    <td>创建训练作业标签,支持批量添加,当添加的标签key已存在,则覆盖该标签的value。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrainingJobMetrics</td>
                    <td>查询训练作业指定任务的运行指标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowObsUrlOfTrainingJobLogs</td>
                    <td>查询训练作业指定任务的日志(OBS临时链接,有效期5分钟),可全量查看或直接下载。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoSearchPerTrial</td>
                    <td>根据传入的trial_id,查询指定trial的搜索结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopTrainingJob</td>
                    <td>终止训练作业,只可终止创建中、等待中、运行中的作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrainingJob</td>
                    <td>创建训练作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoSearchParamsAnalysis</td>
                    <td>获取超参敏感度分析结果的汇总表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrainingJobs</td>
                    <td>根据指定查询条件查询用户创建的训练作业列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoSearchParamAnalysisResultPath</td>
                    <td>获取某个超参敏感度分析图像的保存路径。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoSearchTrialEarlyStop</td>
                    <td>提前终止自动化搜索作业的某个trial。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">资源和引擎规格</td>
                    <td>ShowTrainingJobEngines</td>
                    <td>获取训练作业支持的AI预置框架。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrainingJobFlavors</td>
                    <td>获取训练作业支持的公共规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源指标</td>
                    <td>ShowPoolRuntimeMetrics</td>
                    <td>查询当前项目下所有资源池的实时利用率。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">资源标签管理</td>
                    <td>ShowPoolTags</td>
                    <td>查询指定资源池的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPoolTags</td>
                    <td>查询用户当前项目下资源池的所有标签,默认查询所有工作空间,无权限的工作空间不返回标签数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">资源池作业管理</td>
                    <td>ShowWorkloadStatistics</td>
                    <td>查询专属资源池作业统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkloads</td>
                    <td>查询专属资源池作业列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">资源池管理</td>
                    <td>ListPools</td>
                    <td>查询资源池列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePool</td>
                    <td>删除指定的资源池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPool</td>
                    <td>查询指定资源池的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPoolMonitor</td>
                    <td>获取资源池的监控信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPoolStatistics</td>
                    <td>获取资源池的统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PatchPool</td>
                    <td>更新指定的资源池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePool</td>
                    <td>用户创建资源池。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">资源规格管理</td>
                    <td>ListResourceFlavors</td>
                    <td>查询资源规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配置管理</td>
                    <td>ShowOsConfig</td>
                    <td>获取ModelArts OS服务的配置参数,如网络网段,用户资源配额等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额管理</td>
                    <td>ShowOsQuota</td>
                    <td>获取ModelArts OS服务中部分资源的配额,如资源池配额、网络配额等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">镜像管理</td>
                    <td>DeleteImage</td>
                    <td>删除镜像对象,对于个人私有镜像可以通过参数一并删除SWR镜像内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImage</td>
                    <td>查询镜像详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImage</td>
                    <td>根据指定条件分页查询满足条件的所有镜像。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageGroup</td>
                    <td>查询用户镜像信息概览,以镜像名称作为聚合的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterImage</td>
                    <td>将用户自定义的镜像注册到ModelArts镜像管理。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>