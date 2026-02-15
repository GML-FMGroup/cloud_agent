# LakeFormation MCP Server 

## 版本信息
v0.1.0

## 产品描述

LakeFormation MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务LakeFormation交互的能力。可以基于自然语言对LakeFormation资源进行全链路管理。

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
                    <td rowspan="13">Access</td>
                    <td>ShowSyncPolicy</td>
                    <td>获取同步权限策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAuthorizeInterface</td>
                    <td>批量授权接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAccessClient</td>
                    <td>根据ID删除服务接入客户端</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAccessClient</td>
                    <td>根据ID更新服务接入客户端</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInterfaces</td>
                    <td>通过过滤条件查询接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ApplyForAccess</td>
                    <td>申请接入服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAccessClient</td>
                    <td>根据ID获取服务接入客户端详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAccessClient</td>
                    <td>创建服务接入客户端。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicy</td>
                    <td>分页获取同步权限策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessClientInfos</td>
                    <td>根据LakeFormation实例获取服务实例相关的接入客户端信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAccessInfos</td>
                    <td>根据LakeFormation实例获取服务实例相关的接入信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCancelAuthorizationInterface</td>
                    <td>批量取消授权接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckPermission</td>
                    <td>批量鉴权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Agency</td>
                    <td>ShowAgency</td>
                    <td>委托查询</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAgency</td>
                    <td>删除委托</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgency</td>
                    <td>创建委托</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Catalog</td>
                    <td>UpdateCatalog</td>
                    <td>修改catalog信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCatalogs</td>
                    <td>根据catalog名字的通配符列举catalog的详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCatalog</td>
                    <td>获取catalog信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCatalog</td>
                    <td>删除空的catalog对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCatalog</td>
                    <td>创建catalog,会在catalog下创建默认数据库,默认数据库名称为:default</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Configuration</td>
                    <td>ListConfigs</td>
                    <td>获取所有用户可见的租户面配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Credential</td>
                    <td>ShowCredential</td>
                    <td>获取临时密钥和securityToken,失效时间大于等于1小时,请在1小时内更新</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">Database</td>
                    <td>ListDatabases</td>
                    <td>列举数据库信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseNames</td>
                    <td>列举数据库名称信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDatabase</td>
                    <td>获取数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabase</td>
                    <td>修改数据库属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabase</td>
                    <td>删除指定数据库,catalog的默认数据库不允许删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabase</td>
                    <td>创建数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Function</td>
                    <td>DeleteFunction</td>
                    <td>删除函数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllFunctions</td>
                    <td>获取catalog下所有的函数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateFunction</td>
                    <td>修改函数属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctionNames</td>
                    <td>查询数据库下的所有函数名称列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFunction</td>
                    <td>根据函数名称查询函数信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctions</td>
                    <td>列举函数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFunction</td>
                    <td>创建函数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">GrantAccess</td>
                    <td>AuthorizeAccessService</td>
                    <td>接入服务授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAccessService</td>
                    <td>查询租户当前的接入服务授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgreement</td>
                    <td>用户授权并委托</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgreement</td>
                    <td>查询租户当前协议和委托信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAgreement</td>
                    <td>用户取消授权,同时有权限用户删除委托</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgreementRule</td>
                    <td>查询当前系统协议</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Info</td>
                    <td>CountMetaObj</td>
                    <td>元数据数量统计接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Instance</td>
                    <td>DeleteLakeFormationInstance</td>
                    <td>根据实例Id删除LakeFormation实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLakeFormationInstance</td>
                    <td>修改LakeFormation实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLakeFormationInstanceScale</td>
                    <td>变更LakeFormation实例规格</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLakeFormationInstance</td>
                    <td>创建一个LakeFormation实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLakeFormationInstances</td>
                    <td>查询用户创建的实例列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLakeFormationInstance</td>
                    <td>使用实例Id查询LakeFormation实例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MoveLakeFormationInstanceOutRecycleBin</td>
                    <td>从回收站恢复LakeFormation实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLakeFormationInstanceDefault</td>
                    <td>设为默认实例,只有非默认实例可以设置为默认实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">OBS</td>
                    <td>ListObsObject</td>
                    <td>查询obs桶对象列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObsBuckets</td>
                    <td>查询OBS桶列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Partition</td>
                    <td>BatchUpdatePartition</td>
                    <td>所有partition必须要全部存在,如果存在某个partition不存在,就返回失败</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPartitionNamesWithoutLimit</td>
                    <td>遍历分区名称列表信息,返回全量的数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListPartitionByValues</td>
                    <td>批量获取分区信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePartition</td>
                    <td>非事务表:如果设置删除数据,立刻删除分区数据路径下的数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPartitions</td>
                    <td>遍历指定数据表下的分区列表,对于事务表,支持基于表的特定版本遍历分区列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPartitions</td>
                    <td>批量添加分区信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPartitionNames</td>
                    <td>遍历分区名字列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">PartitionColumnStatistic</td>
                    <td>BatchShowPartitionColumnStatistics</td>
                    <td>批量获取分区的列统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetPartitionColumnStatistics</td>
                    <td>批量设置分区的统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePartitionColumnStatistics</td>
                    <td>删除分区列的统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">QM</td>
                    <td>ListQuotas</td>
                    <td>查询用户的配额信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Role</td>
                    <td>UpdatePrincipals</td>
                    <td>更新角色中的principals</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRole</td>
                    <td>创建role</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRole</td>
                    <td>获取角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRole</td>
                    <td>修改角色信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociatePrincipals</td>
                    <td>将一个或者多个用户/用户组加入角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoles</td>
                    <td>返回所有角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPrincipals</td>
                    <td>查询角色下的用户/用户组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoleNames</td>
                    <td>查询所有角色名字列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRole</td>
                    <td>删除指定角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokePrincipals</td>
                    <td>将一个或者多个用户/用户组从角色移除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Specification</td>
                    <td>ListSpecs</td>
                    <td>查询规格列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">TAG</td>
                    <td>ListLakeFormationInstanceTags</td>
                    <td>查询租户在指定Project中实例类型的所有资源标签集合</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateLakeFormationInstanceTags</td>
                    <td>为指定实例批量更新标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Table</td>
                    <td>ListTablesByName</td>
                    <td>根据表名查询数据库下的表信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTable</td>
                    <td>获取表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTables</td>
                    <td>返回数据库下符合查询条件的表的元数据信息,不支持事务操作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTable</td>
                    <td>修改表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTable</td>
                    <td>创建表操作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTableMeta</td>
                    <td>通过数据库通配符和表通配符,找到符合条件的表并返回表的描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTableNames</td>
                    <td>查询数据库下的所有表名字列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTable</td>
                    <td>删除表及表下的分区</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TableColumnStatistic</td>
                    <td>DeleteTableColumnStatistics</td>
                    <td>删除表的指定列统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTableColumnStatistics</td>
                    <td>获取表的列统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetTableColumnStatistics</td>
                    <td>更新表的列统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">User</td>
                    <td>UpdateRoles</td>
                    <td>更新用户中的角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateRoles</td>
                    <td>将多个角色授予User</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsers</td>
                    <td>获取用户列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RevokeRoles</td>
                    <td>将一个或者多个角色从用户移除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserRoles</td>
                    <td>查询用户的角色列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">UserGroup</td>
                    <td>ListGroupsForDomain</td>
                    <td>获取租户的用户组</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>