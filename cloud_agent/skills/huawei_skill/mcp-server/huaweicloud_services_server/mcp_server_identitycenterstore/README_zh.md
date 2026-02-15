# IdentityCenterStore MCP Server 

## 版本信息
v0.1.0

## 产品描述

IdentityCenterStore MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IdentityCenterStore交互的能力。可以基于自然语言对IdentityCenterStore资源进行全链路管理。

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
                    <td rowspan="6">Group</td>
                    <td>DescribeGroup</td>
                    <td>根据用户组ID,查询IAM身份中心用户组的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroups</td>
                    <td>查询指定身份源下的IAM身份中心用户组列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGroup</td>
                    <td>根据用户组ID,删除对应的IAM身份中心用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGroup</td>
                    <td>在指定的身份源中创建一个IAM身份中心用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGroup</td>
                    <td>根据用户组ID,更新对应IAM身份中心用户组的属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetGroupId</td>
                    <td>根据显示名或外部身份源ID,以精确匹配的方式查询用户组ID。显示名和外部身份源ID两种查询方式二选一,不支持同时传入。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">GroupMembership</td>
                    <td>ListGroupMemberships</td>
                    <td>根据用户组ID,列出用户组中的用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>IsMemberInGroups</td>
                    <td>根据用户ID和用户组ID列表,查询用户是否为用户组的成员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroupMembershipsForMember</td>
                    <td>根据用户ID,列出用户加入的用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetGroupMembershipId</td>
                    <td>根据用户ID和用户组ID,查询对应的关联关系ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGroupMembership</td>
                    <td>将用户添加到用户组中,用户和用户组必须在同一身份源下。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribeGroupMembership</td>
                    <td>根据关联关系ID,查询此关联关系的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGroupMembership</td>
                    <td>根据关联关系ID解绑用户和用户组,也就是将用户移出用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">User</td>
                    <td>DeleteUser</td>
                    <td>根据用户ID,删除对应的IAM身份中心用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsers</td>
                    <td>查询指定身份源下的IAM身份中心用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUser</td>
                    <td>在指定的身份源中创建一个IAM身份中心用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUser</td>
                    <td>根据用户ID,更新对应IAM身份中心用户的属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribeUser</td>
                    <td>根据用户ID,查询对应IAM身份中心用户的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetUserId</td>
                    <td>根据用户名或外部身份源ID,以精确匹配的方式查询用户ID。用户名和外部身份源ID两种查询方式二选一,不支持同时传入。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>