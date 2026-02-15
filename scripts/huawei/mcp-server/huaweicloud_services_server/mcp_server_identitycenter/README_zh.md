# IdentityCenter MCP Server 

## 版本信息
v0.1.0

## 产品描述

IdentityCenter MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IdentityCenter交互的能力。可以基于自然语言对IdentityCenter资源进行全链路管理。

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
                    <td rowspan="7">AccountAssignment</td>
                    <td>DeleteAccountAssignment</td>
                    <td>使用指定的权限集从指定的账号删除主体的访问权限,主体可为IAM身份中心用户或用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAccountAssignment</td>
                    <td>使用指定的权限集为指定账号分配对应主体的访问权限,主体可为IAM身份中心用户或用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccountAssignments</td>
                    <td>列出与指定账号以及指定权限集关联的用户或用户组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccountAssignmentDeletionStatus</td>
                    <td>查询指定IAM身份中心实例下的账号分配的删除状态列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribeAccountAssignmentDeletionStatus</td>
                    <td>根据请求ID,查询指定IAM身份中心实例下的账号分配删除状态详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribeAccountAssignmentCreationStatus</td>
                    <td>根据请求ID,查询指定IAM身份中心实例下的账号分配创建状态详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccountAssignmentCreationStatus</td>
                    <td>查询指定IAM身份中心实例下的账号分配的创建状态列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Instance</td>
                    <td>ListInstances</td>
                    <td>查询IAM身份中心的实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">InstanceAccessControlAttributeConfiguration</td>
                    <td>CreateInstanceAccessControlAttributeConfiguration</td>
                    <td>启用指定实例的访问控制功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceAccessControlAttributeConfiguration</td>
                    <td>更新可与IAM身份中心实例一起使用的IAM身份中心身份源属性,以进行基于属性的访问控制(ABAC)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribeInstanceAccessControlAttributeConfiguration</td>
                    <td>返回已配置为与指定IAM身份中心实例的基于属性的访问控制(ABAC)一起使用的IAM身份中心身份源属性列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstanceAccessControlAttributeConfiguration</td>
                    <td>禁用指定IAM身份中心实例的基于属性的访问控制(ABAC)功能,并删除已配置的所有属性映射。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">PermissionSet</td>
                    <td>ListPermissionSetProvisioningStatus</td>
                    <td>查询指定实例中的权限集预分配状态列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachManagedPolicyToPermissionSet</td>
                    <td>在指定的权限集中添加系统身份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermissionSets</td>
                    <td>查询指定实例下的权限集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomRoleFromPermissionSet</td>
                    <td>删除指定权限集中的自定义策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ProvisionPermissionSet</td>
                    <td>将指定权限集预分配给指定账号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePermissionSet</td>
                    <td>根据权限集ID,更新指定权限集的属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetCustomRoleForPermissionSet</td>
                    <td>获取分配给权限集的自定义策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribePermissionSetProvisioningStatus</td>
                    <td>根据请求ID,查询权限集预分配状态的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePermissionSet</td>
                    <td>在指定的IAM身份中心实例中创建一个权限集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PutCustomPolicyToPermissionSet</td>
                    <td>在指定的权限集中添加自定义身份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCustomPolicyFromPermissionSet</td>
                    <td>删除指定权限集中的自定义身份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermissionSetsProvisionedToAccount</td>
                    <td>查询分配给指定账号的权限集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GetCustomPolicyForPermissionSet</td>
                    <td>查询指定权限集中的自定义身份策略详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DescribePermissionSet</td>
                    <td>根据权限集ID,查询指定权限集的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DetachManagedPolicyFromPermissionSet</td>
                    <td>删除指定权限集中的系统身份策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListManagedPoliciesInPermissionSet</td>
                    <td>获取添加到指定权限集中的系统身份策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PutCustomRoleToPermissionSet</td>
                    <td>将自定义策略附加到权限集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePermissionSet</td>
                    <td>根据权限集ID,删除指定的权限集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccountsForProvisionedPermissionSet</td>
                    <td>查询与指定权限集关联的账号列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Tag</td>
                    <td>ListTagResources</td>
                    <td>列出绑定到指定资源的标签。当前支持为权限集添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTagResource</td>
                    <td>从指定资源中删除指定的标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTagResource</td>
                    <td>给指定的资源添加一个或多个标签。当前支持为权限集添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">UnexposedPermissionSet</td>
                    <td>DetachManagedRoleFromPermissionSet</td>
                    <td>删除指定权限集中的系统策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AttachManagedRoleToPermissionSet</td>
                    <td>在指定的权限集中添加系统策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListManagedRolesInPermissionSet</td>
                    <td>获取添加到指定权限集中的系统策略列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>