# CodeArtsArtifact MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeArtsArtifact MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeArtsArtifact交互的能力。可以基于自然语言对CodeArtsArtifact资源进行全链路管理。

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
                    <td rowspan="2">仓库关联项目</td>
                    <td>ShowProjectList</td>
                    <td>查询项目管理关联仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProjectRelatedRepository</td>
                    <td>创建项目管理关联仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">仓库容量</td>
                    <td>ShowStorage</td>
                    <td>仓库用量查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">仓库管理</td>
                    <td>ModifyRepository</td>
                    <td>编辑仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRepository</td>
                    <td>删除仓库到回收站</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMavenRepo</td>
                    <td>创建maven仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMavenInfo</td>
                    <td>查询租户Maven仓库列表和账号密码,支持跨租户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDockerRepositories</td>
                    <td>创建docker仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateArtifactory</td>
                    <td>创建非maven仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateArtifactory</td>
                    <td>编辑非maven仓库信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepositoryInfo</td>
                    <td>查看仓库信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">仓库详情</td>
                    <td>ListArtifactoryStorageStatistic</td>
                    <td>查询存储容量趋势</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRepository</td>
                    <td>查询单个仓库详细信息,会去统计仓库下的制品数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllRepositories</td>
                    <td>查询仓库详情,不会去统计仓库下的制品数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">关注</td>
                    <td>CreateAttention</td>
                    <td>关注组件/取消关注组件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAttentions</td>
                    <td>查询关注列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">发布库文件查询</td>
                    <td>ShowReleaseProjectFiles</td>
                    <td>获取项目下文件版本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectReleaseFiles</td>
                    <td>获取项目下文件版本信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">回收站</td>
                    <td>BatchRestoreRepo</td>
                    <td>批量还原回收站</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTrashes</td>
                    <td>批量删除回收站</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">审计日志</td>
                    <td>ShowAudit</td>
                    <td>查询仓库或文件的审计日志信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">搜索</td>
                    <td>SearchByChecksum</td>
                    <td>通过checksum搜索文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchArtifacts</td>
                    <td>统筹搜索</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">文件管理</td>
                    <td>ShowFileTree</td>
                    <td>查询仓库文件夹目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListArtifactoryComponent</td>
                    <td>查询仓库文件详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteArtifactFile</td>
                    <td>非maven删除文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">权限查看</td>
                    <td>ShowUserPrivileges</td>
                    <td>查询用户在项目下的权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">用户管理</td>
                    <td>ResetUserPassword</td>
                    <td>重置用户密码</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>