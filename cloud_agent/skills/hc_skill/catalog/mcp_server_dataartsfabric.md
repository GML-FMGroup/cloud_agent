# DataArtsFabric MCP Server 

## 版本信息
v0.1.0

## 产品描述

DataArtsFabric MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DataArtsFabric交互的能力。可以基于自然语言对DataArtsFabric资源进行全链路管理。

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
                    <td rowspan="3">Agency</td>
                    <td>CreateAgency</td>
                    <td>为用户自动创建服务所需要的服务委托。委托需要附加必需的权限策略才能使用,创建委托会自动附加必需的权限策略,也可以指定附加需要的权限策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAgency</td>
                    <td>删除用户的服务委托权限。可以通过指定权限策略来删除委托中附加的权限策略,必需的权限策略无法被删除;如果不指定权限策略,会删除整个委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAgency</td>
                    <td>查询用用户服务委托详情是否满足系统所需权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Agreement</td>
                    <td>CreateAgreement</td>
                    <td>注册租户协议</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgreementRule</td>
                    <td>查询系统协议</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAgreement</td>
                    <td>删除用户注册协议</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgreement</td>
                    <td>查询用户是否注册协议</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ConfigCenter</td>
                    <td>ListFeatures</td>
                    <td>查询用户支持特性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Endpoint</td>
                    <td>ShowEndpoint</td>
                    <td>查询endpioint详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEndpoint</td>
                    <td>修改Endpoint</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEndpoints</td>
                    <td>查询Endpoint列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEndpoint</td>
                    <td>创建Endpoint</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEndpoint</td>
                    <td>删除endpioint</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SubscribeEndpoint</td>
                    <td>在用户Workspace下订阅Endpoint(公共Endpoint场景)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Framework</td>
                    <td>ListFrameworks</td>
                    <td>查询Framework列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Health</td>
                    <td>ShowAdminHealthCheck</td>
                    <td>服务健康检查</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Message</td>
                    <td>ListMessageNotificationPolicy</td>
                    <td>查询消息通知策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMessageNotificationPolicy</td>
                    <td>创建消息通知策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMessageNotificationPolicy</td>
                    <td>删除消息通知策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Metric</td>
                    <td>UpdateMetricsConfig</td>
                    <td>更新AOM监控采集配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">ModelDefinition</td>
                    <td>CreateModelDefinition</td>
                    <td>创建模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBaseModels</td>
                    <td>列举基模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListModelVersions</td>
                    <td>查询模型的版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteModelVersion</td>
                    <td>删除模型版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListModels</td>
                    <td>列举模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CleanupModel</td>
                    <td>清理未使用的模型定义</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateModelDefinition</td>
                    <td>更新模型,会生成新版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Specification</td>
                    <td>ListSpecs</td>
                    <td>查询服务规格列表,购买计算资源使用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">TMS</td>
                    <td>BatchCreateFabricWorkspaceTags</td>
                    <td>批量打资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFabricProjectTags</td>
                    <td>查询项目标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagFabricWorkspaces</td>
                    <td>查询资源实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteFabricWorkspaceTags</td>
                    <td>批量删除资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFabricWorkspaceTags</td>
                    <td>查询资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountTagFabricWorkspaces</td>
                    <td>查询资源实例数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">Workspace</td>
                    <td>UpdateWorkspace</td>
                    <td>更新Workspace</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkspace</td>
                    <td>删除Workspace</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspaces</td>
                    <td>查询Workspace列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkspace</td>
                    <td>Create workspace</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>