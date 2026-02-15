# DataArtsInsight MCP Server 

## 版本信息
v0.1.0

## 产品描述

DataArtsInsight MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DataArtsInsight交互的能力。可以基于自然语言对DataArtsInsight资源进行全链路管理。

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
                    <td rowspan="1">产品实例</td>
                    <td>ListInstances</td>
                    <td>查询用户已开通产品实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">仪表板大屏资源统一</td>
                    <td>ListResources</td>
                    <td>仪表板和大屏资源统一</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">协同授权</td>
                    <td>SaveOrUpdateAuthProperties</td>
                    <td>保存或修改资源属性值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthed</td>
                    <td>协同授权列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSaveAuth</td>
                    <td>批量保存、修改、删除指定自研的协同授权规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthProperties</td>
                    <td>获取资源属性值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">导入导出参数</td>
                    <td>CreateAndUpdateExportConfig</td>
                    <td>配置导出参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">工作空间</td>
                    <td>CreateWorkspace</td>
                    <td>创建工作空间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWorkspace</td>
                    <td>删除工作空间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkspaces</td>
                    <td>查询工作空间详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkspace</td>
                    <td>修改工作空间</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">数据源</td>
                    <td>DeleteDataConnectionByConnectionId</td>
                    <td>删除数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataConnection</td>
                    <td>获取数据源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDataConnection</td>
                    <td>数据源新增</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataConnectionByConnectionId</td>
                    <td>获取数据源详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataConnection</td>
                    <td>数据源更新</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">数据集</td>
                    <td>ShowDatasetDetail</td>
                    <td>获取数据集详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCubeAndCatalogList</td>
                    <td>查询数据集列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveDatasetForOpenApi</td>
                    <td>保存数据集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">数据集权限</td>
                    <td>UpdatePermissionConfig</td>
                    <td>打开/关闭权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAndUpdatePermission</td>
                    <td>配置数据集权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermissionConfig</td>
                    <td>获取数据集权限配置信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRule</td>
                    <td>删除权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermission</td>
                    <td>获取数据集权限列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">用户标签</td>
                    <td>ListUserTagValue</td>
                    <td>获取用户标签值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserTag</td>
                    <td>编辑用户标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserTagHead</td>
                    <td>获取用户标签头</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUserTag</td>
                    <td>创建用户标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUserTag</td>
                    <td>删除用户标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveUserTagValue</td>
                    <td>保存用户标签内容(按用户)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">资源迁移</td>
                    <td>ImportResourcePackage</td>
                    <td>API 导入资源包文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportResourcePackage</td>
                    <td>API导出资源包</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowImportResourceTaskDetail</td>
                    <td>获取导入任务详情</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>