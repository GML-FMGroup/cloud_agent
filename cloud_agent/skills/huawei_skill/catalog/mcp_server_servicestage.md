# ServiceStage MCP Server 

## 版本信息
v0.1.0

## 产品描述

ServiceStage MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务ServiceStage交互的能力。可以基于自然语言对ServiceStage资源进行全链路管理。

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
                    <td rowspan="8">Application</td>
                    <td>ModifyApplication</td>
                    <td>此API通过应用ID修改应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApplications</td>
                    <td>获取所有应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApplicationInfo</td>
                    <td>此API通过应用ID获取应用详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyApplicationConfiguration</td>
                    <td>此API通过应用ID修改应用配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApplicationConfiguration</td>
                    <td>此API通过应用ID获取应用配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApplication</td>
                    <td>应用是一个功能相对完备的业务系统,由一个或多个特性相关的组件组成。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplication</td>
                    <td>此API通过应用ID删除应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplicationConfiguration</td>
                    <td>此API通过应用ID删除应用配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Component</td>
                    <td>ShowComponentRecords</td>
                    <td>此API用来通过组件ID获取记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponentsInApplication</td>
                    <td>通过此API获取应用下所有应用组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateComponent</td>
                    <td>此API用来在应用中创建组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponents</td>
                    <td>此API用来获取所有组件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteComponent</td>
                    <td>此API通过组件ID删除组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyComponent</td>
                    <td>此API通过组件ID修改组件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponentInfo</td>
                    <td>通过组件ID获取组件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateComponentAction</td>
                    <td>通过组件ID下发组件任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Environment</td>
                    <td>ShowEnvironmentInfo</td>
                    <td>此API通过环境ID获取环境详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEnvironment</td>
                    <td>环境是用于应用部署和运行的计算、存储、网络等基础设施的集合。Servicestage把相同VPC下的CCE集群加上多个ELB、RDS、DCS实例组合为一个环境,如:开发环境,测试环境,预生产环境,生产环境。环境内网络互通,可以按环境维度来管理资源、部署服务,减少具体基础设施运维管理的复杂性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvironmentResources</td>
                    <td>此API用来根据环境ID查询环境资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyEnvironment</td>
                    <td>此API通过环境ID修改环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyResourceInEnvironment</td>
                    <td>此API用来通过环境ID修改环境资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvironments</td>
                    <td>此API用来获取所有已经创建环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEnvironment</td>
                    <td>此API通过环境ID删除环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">GIT仓库</td>
                    <td>ListHooks</td>
                    <td>获取指定项目的所有hooks</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProject</td>
                    <td>创建指定组织下的软件仓库项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNamespaces</td>
                    <td>获取仓库的namespaces。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjects</td>
                    <td>获取指定组织下的所有项目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTag</td>
                    <td>创建指定项目的tag标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHook</td>
                    <td>创建指定项目的hook。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBranches</td>
                    <td>获取指定项目的所有分支列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTags</td>
                    <td>获取指定项目的所有tag标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTag</td>
                    <td>删除指定项目的tag标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHook</td>
                    <td>删除指定项目的hook。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommits</td>
                    <td>获取指定项目的最近10次commit提交记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectDetail</td>
                    <td>通过指定的clone url 获取仓库信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">GIT仓库文件</td>
                    <td>CreateFile</td>
                    <td>在指定仓库项目下创建文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFile</td>
                    <td>删除指定项目仓库下的文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFile</td>
                    <td>更新指定项目仓库下的文件内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTrees</td>
                    <td>获取指定项目仓库的文件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowContent</td>
                    <td>获取指定项目仓库下文件的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">GIT授权</td>
                    <td>CreatePersonalAuth</td>
                    <td>创建指定Git仓库类型的私人令牌授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePasswordAuth</td>
                    <td>创建指定Git仓库类型的口令授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOAuth</td>
                    <td>创建指定Git仓库类型的OAuth授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthorizations</td>
                    <td>获取所有Git仓库授权信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRedirectUrl</td>
                    <td>获取指定Git仓库类型的授权重定向URL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuthorize</td>
                    <td>通过名称删除仓库授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Job</td>
                    <td>ShowJobInfo</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Meta</td>
                    <td>ListRuntimes</td>
                    <td>此API用来获取所有支持应用组件运行时类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFlavors</td>
                    <td>通过此API获取所用支持的应用资源规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplates</td>
                    <td>此API用来获取所有内置应用组件模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">RuntimeStack</td>
                    <td>ShowRuntimeStacks</td>
                    <td>获取运行时信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">云应用模型</td>
                    <td>UpdateTemplate</td>
                    <td>更新模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstanceById</td>
                    <td>删除实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeployInstance</td>
                    <td>部署实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCamInstance</td>
                    <td>创建、更新实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplate</td>
                    <td>删除模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplate</td>
                    <td>创建模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">实例</td>
                    <td>ChangeInstance</td>
                    <td>通过此API修改应用组件实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>通过此API删除应用组件实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>通过此API获取组件下的所有组件实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstanceSnapshots</td>
                    <td>通过此API获取应用组件实例快照信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>此API用来创建应用组件实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstanceDetail</td>
                    <td>此API通过实例ID获取实例详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceAction</td>
                    <td>通过此API获取对组件实例的操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">应用</td>
                    <td>ShowApplicationDetail</td>
                    <td>此API通过应用ID获取应用详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApplications</td>
                    <td>通过此API可以获取所有已经创建的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeApplication</td>
                    <td>此API通过应用ID修改应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeApplicationConfiguration</td>
                    <td>通过此API修改应用配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">环境</td>
                    <td>ChangeResourceInEnvironment</td>
                    <td>此API用来修改环境资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnvironmentDetail</td>
                    <td>此API通过环境ID获取环境详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeEnvironment</td>
                    <td>此API通过环境ID修改环境信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEnvironments</td>
                    <td>此API用来获取所有已经创建环境。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">组件</td>
                    <td>ListComponents</td>
                    <td>通过此API获取应用下所有应用组件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowComponentDetail</td>
                    <td>通过组件ID获取应用组件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeComponent</td>
                    <td>此API通过组件ID修改组件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComponentOverviews</td>
                    <td>通过此API获取应用下所有应用组件部署信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">部署任务</td>
                    <td>ShowJobDetail</td>
                    <td>通过此API获取部署任务详细信息。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>