# RabbitMQ MCP Server 

## 版本信息
v0.1.0

## 产品描述

RabbitMQ MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务RabbitMQ交互的能力。可以基于自然语言对RabbitMQ资源进行全链路管理。

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
                    <td rowspan="3">Binding管理</td>
                    <td>CreateBinding</td>
                    <td>添加绑定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBinding</td>
                    <td>删除绑定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBindings</td>
                    <td>查询Exchange绑定信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Exchange管理</td>
                    <td>ListExchanges</td>
                    <td>查询Exchange列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateExchange</td>
                    <td>创建Exchange。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteExchanges</td>
                    <td>批量删除指定Exchange。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Queue管理</td>
                    <td>DeleteQueueInfo</td>
                    <td>清空Queue消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateQueue</td>
                    <td>创建Queue。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQueueDetails</td>
                    <td>查询指定Queue详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteQueues</td>
                    <td>批量删除指定Queue。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueues</td>
                    <td>查询所属Vhost下Queue的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Vhost管理</td>
                    <td>ListVhosts</td>
                    <td>查询Vhost列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteVhosts</td>
                    <td>批量删除指定Vhost。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVhost</td>
                    <td>创建Vhost。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">其他接口</td>
                    <td>ShowCesHierarchy</td>
                    <td>查询实例在CES的监控层级关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEngineProducts</td>
                    <td>查询产品规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMaintainWindows</td>
                    <td>查询维护时间窗开始时间和结束时间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRabbitMqProductCores</td>
                    <td>查询RabbitMQ产品规格核数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAvailableZones</td>
                    <td>在创建实例时,需要配置实例所在的可用区ID,可通过该接口查询可用区的ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">后台任务管理</td>
                    <td>ListBackgroundTasks</td>
                    <td>查询实例的后台任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackgroundTask</td>
                    <td>查询后台任务管理中的指定记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBackgroundTask</td>
                    <td>删除后台任务管理中的指定记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">实例管理</td>
                    <td>UpdatePlugins</td>
                    <td>开启或关闭插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlugins</td>
                    <td>查询插件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPassword</td>
                    <td>重置密码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">标签管理</td>
                    <td>ShowRabbitMqProjectTags</td>
                    <td>查询项目标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateOrDeleteRabbitMqTag</td>
                    <td>批量添加或删除实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRabbitMqTags</td>
                    <td>查询实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">生命周期管理</td>
                    <td>UpdateInstance</td>
                    <td>修改实例的名称和描述信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询指定实例的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePostPaidInstanceByEngine</td>
                    <td>创建实例,该接口支持创建按需和包周期计费方式的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除指定实例,释放该实例的所有资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRestartOrDeleteInstances</td>
                    <td>批量删除实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableDns</td>
                    <td>开启RabbitMQ实例域名访问功能后,客户端可以通过域名连接RabbitMQ实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstancesDetails</td>
                    <td>查询租户的实例列表,支持按照条件查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">用户管理</td>
                    <td>ListUser</td>
                    <td>查询用户列表(仅AMQP版本支持)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUser</td>
                    <td>创建用户(仅AMQP版本支持)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUser</td>
                    <td>修改用户参数(仅AMQP版本支持)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUser</td>
                    <td>删除用户(仅AMQP版本支持)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">规格变更管理</td>
                    <td>ShowEngineInstanceExtendProductInfo</td>
                    <td>查询新规格实例可扩容列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeEngineInstance</td>
                    <td>实例规格变更。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>