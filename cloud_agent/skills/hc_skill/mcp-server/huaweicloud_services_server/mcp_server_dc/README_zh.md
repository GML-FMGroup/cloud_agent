# DC MCP Server 

## 版本信息
v0.1.0

## 产品描述

DC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DC交互的能力。可以基于自然语言对DC资源进行全链路管理。

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
                    <td rowspan="3">BindingGlobalEip</td>
                    <td>UnbindGlobalEips</td>
                    <td>解绑GEIP</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BindGlobalEips</td>
                    <td>绑定GEIP操作</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalEips</td>
                    <td>查询已经绑定的GEIP列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ConnectGateway</td>
                    <td>DeleteConnectGateway</td>
                    <td>删除互联网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConnectGateway</td>
                    <td>更新互联网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConnectGateway</td>
                    <td>创建互联网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConnectGateways</td>
                    <td>查询互联网关列表信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConnectGateway</td>
                    <td>查询互联网关详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">DirectConnect</td>
                    <td>UpdateDirectConnect</td>
                    <td>更新物理连接信息,包括名字,描述等信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHostedDirectConnect</td>
                    <td>合作伙伴更新托管专线.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHostedDirectConnects</td>
                    <td>查询合作伙伴创建的托管专线连接列表.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDirectConnect</td>
                    <td>查询物理连接详细信息.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHostedDirectConnect</td>
                    <td>查询合法作伙伴的Hosted专线类型.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDirectConnect</td>
                    <td>删除物理连接,本接口只适用于按需计费物理专线,对于包周期购买的专线通过订单退订的方式删除物理连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHostedDirectConnect</td>
                    <td>用于合作伙伴用户最终租户创建托管专线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHostedDirectConnect</td>
                    <td>合作伙伴删除托管专线</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDirectConnects</td>
                    <td>查询租户创建的所有的direct connect对象.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">DirectConnectLocation</td>
                    <td>ShowDirectConnectLocation</td>
                    <td>查询指定的专线接入点详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDirectConnectLocations</td>
                    <td>查询本区域下所有专线的接入点的信息,分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效,单独使用无效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">GdgwRoutetable</td>
                    <td>UpdateGdgwRouteTable</td>
                    <td>支持的修改操作:新增、删除、修改</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGdgwRouteTables</td>
                    <td>查询全域接入网关路由表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">GlobalDcGateway</td>
                    <td>ShowGlobalDcGateway</td>
                    <td>查询专线全域接入网关实例详情信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGlobalDcGateway</td>
                    <td>更新专线全域接入网关global-dc-gateway的名字,描述等信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalDcGateway</td>
                    <td>删除专线全域接入网关global-dc-gateway实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGlobalDcGateway</td>
                    <td>创建专线全域接入网关实例(global-dc-gateway),用于接入全球的ER实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalDcGateways</td>
                    <td>查询专线全域接入网关列表,建议使用分页查询 分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效,单独使用无效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">PeerLink</td>
                    <td>DeletePeerLink</td>
                    <td>删除全域接入网关与ER的关联连接peer-link</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPeerLink</td>
                    <td>查询指定接入网关的指定的关联连接(peer link)详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePeerLink</td>
                    <td>创建专线全域接入网关的关联连接peer-link对象,用于连接企业路由器或者其他接入网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePeerLink</td>
                    <td>更新接入网关与ER对接的关联连接peer-link</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPeerLinks</td>
                    <td>查询全域接入网关与ER等对象的关联连接列表,分页查询使用的参数为marker、limit。marker和limit一起使用时才会生效,单独使用无效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">QuotaManager</td>
                    <td>ShowQuotas</td>
                    <td>查询租户各类资源的使用情况,如Directconnect的使用量,虚拟接口的使用量等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">TagManage</td>
                    <td>CreateResourceTag</td>
                    <td>- 一个资源上最多有10个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceTag</td>
                    <td>查询资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResourceTag</td>
                    <td>删除时,不对标签字符集做校验,调用接口前必须要做encodeURI,服务端需要对接口uri做decodeURI。删除的key不存在报404,Key不能为空或者空字符串。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProjectTags</td>
                    <td>- 查询租户在指定Project中实例类型的所有资源标签集合。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateResourceTags</td>
                    <td>- 为指定实例批量添加或删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTagResourceInstances</td>
                    <td>通过标签查询资源实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VirtualGateway</td>
                    <td>DeleteVirtualGateway</td>
                    <td>删除指定的虚拟网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVirtualGateways</td>
                    <td>查询虚拟网关列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVirtualGateway</td>
                    <td>更新虚拟网关的信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVirtualGateway</td>
                    <td>创建虚拟网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVirtualGateway</td>
                    <td>查询指定虚拟网关的详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">VirtualInterface</td>
                    <td>UpdateVirtualInterface</td>
                    <td>更新虚拟接口的详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchoverTest</td>
                    <td>客户双专线接入,需要支持双线自动倒换,方便进行功能测试。 虚拟接口进行倒换测试会导致接口关闭,业务流量中断。 对于虚拟接口,支持“关闭接口”和“开放接口”两种操作。 1、关闭接口:下发shutdown命令,关闭接口; 2、开放接口:下发undo_shutdown命令,使能接口。 倒换测试选择shutdown时,虚拟接口的状态为ADMIN_SHUTDOWN,此状态不允许虚拟接口的其他操作。 倒换测试选择undo_shutdown时,虚拟接口的状态为ACTIVE。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVifPeer</td>
                    <td>每个虚拟接口可支持两个对等体,IPv4和IPv6对等体,在创建虚拟接口时默认创建IPv4对等体, 本接口一般用于增加ipv6对等体。创建虚拟接口对接体之后,可以通过虚拟接口查询配置结果 本接口只在支持Ipv6的区域开放,如需要使用请联系客服</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVirtualInterface</td>
                    <td>删除虚拟接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSwitchoverTestRecords</td>
                    <td>查询倒换测试记录列表,只展示operate_status为COMPELTE的记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVirtualInterface</td>
                    <td>查询虚拟接口详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVifPeer</td>
                    <td>删除虚拟接口对等体信息,虚拟接口至少要含一个对等体,最后一个对等体不能删除 本接口只在支持Ipv6的区域开放,如需要使用请联系客服</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVirtualInterface</td>
                    <td>虚拟接口配置物理专线上与客户互联的IP和路由等相关信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVirtualInterfaces</td>
                    <td>查询租户所有的虚拟接口列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVifPeer</td>
                    <td>更新虚拟接口对等体信息,包括远端子网,名字和描述等。 本接口只在支持Ipv6的区域开放,如需要使用请联系客服</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>