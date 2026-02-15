# IdentityCenterSCIM MCP Server 

## 版本信息
v0.1.0

## 产品描述

IdentityCenterSCIM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IdentityCenterSCIM交互的能力。可以基于自然语言对IdentityCenterSCIM资源进行全链路管理。

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
                    <td rowspan="5">Group</td>
                    <td>CreateGroup</td>
                    <td>使用SCIM协议,同步用户组到IAM身份中心。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetGroup</td>
                    <td>查询现有用户组的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PatchGroup</td>
                    <td>修改现有用户组的部分属性,和管理用户组中的用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGroup</td>
                    <td>删除现有用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroups</td>
                    <td>对现有用户组列表执行筛选查询,最多只能返回50个结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ServiceProviderConfig</td>
                    <td>ServiceProviderConfig</td>
                    <td>查询IAM身份中心的SCIM相关配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">User</td>
                    <td>PatchUser</td>
                    <td>修改现有用户的部分属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsers</td>
                    <td>对现有用户列表执行筛选查询,最多只能返回50个结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUser</td>
                    <td>删除现有用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PutUser</td>
                    <td>更新现有用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetUser</td>
                    <td>查询现有用户的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUser</td>
                    <td>使用SCIM协议,同步用户到IAM身份中心。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>