# EC MCP Server 

## 版本信息
v0.1.0

## 产品描述

EC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务EC交互的能力。可以基于自然语言对EC资源进行全链路管理。

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
                    <td rowspan="4">EcnAccessPoint</td>
                    <td>UpdateEcnAccessPoint</td>
                    <td>根据企业连接网络ID,更新接入点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEcnAccessPoint</td>
                    <td>添加新的接入点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEcnAccessPointByEcnId</td>
                    <td>根据企业连接网络ID,查询其下所有接入点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEcnAccessPoint</td>
                    <td>根据企业连接网络ID,删除接入点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">EnterpriseConnectNetwork</td>
                    <td>ListEcnWithIeg</td>
                    <td>根据企业连接网络ID,查询企业连接网络与智能企业网关绑定关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEcnWithIeg</td>
                    <td>绑定智能企业网关到企业连接网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEcn</td>
                    <td>查询租户的企业连接网络列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEcn</td>
                    <td>根据企业连接网络ID,更新企业连接网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEcnInfo</td>
                    <td>根据企业连接网络ID,查询企业连接网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEcnWithIeg</td>
                    <td>查询企业连接网络与单个智能企业网关绑定关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEcnWithIeg</td>
                    <td>解除智能企业网关和企业连接网络的绑定</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Equipment</td>
                    <td>ShowEquipmentInfo</td>
                    <td>查询智能企业网关设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEquipmentSpecificConfig</td>
                    <td>查询智能企业网关设备基础规格配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEquipmentInfo</td>
                    <td>更新智能企业网关设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEquipment</td>
                    <td>激活智能企业网关设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEquipment</td>
                    <td>移除智能企业网关设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootEquipment</td>
                    <td>重启智能企业网关设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEquipmentEsn</td>
                    <td>修改智能企业网关设备ESN</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEquipments</td>
                    <td>根据智能企业网关ID,查询智能企业网关设备列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GenerateInitialConfiguration</td>
                    <td>生成智能企业网关设备初始配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">EquipmentLan</td>
                    <td>ShowEquipmentDnsInfo</td>
                    <td>查询智能企业网关设备主备DNS配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEquipmentLanInfo</td>
                    <td>查询智能企业网关设备LAN口配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEquipmentInterfaceName</td>
                    <td>查询智能企业网关已配置的接口名字</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEquipmentLanConfig</td>
                    <td>删除智能企业网关设备LAN口配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEquipmentLanConfig</td>
                    <td>创建智能企业网关设备LAN口配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEquipmentLanConfig</td>
                    <td>更新智能企业网关设备LAN口配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEquipmentDnsInfo</td>
                    <td>更新智能企业网关设备主备DNS配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">EquipmentOspf</td>
                    <td>ShowEquipmentOspf</td>
                    <td>查询智能企业网关设备OSPF配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEquipmentOspf</td>
                    <td>配置智能企业网关设备OSPF协议</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">EquipmentStaticRoute</td>
                    <td>UpdateEquipmentStaticRouteConfig</td>
                    <td>更新智能企业网关设备静态路由配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEquipmentStaticRouteInfo</td>
                    <td>查询智能企业网关设备静态路由配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEquipmentStaticRouteConfig</td>
                    <td>创建智能企业网关设备静态路由配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEquipmentStaticRouteConfig</td>
                    <td>删除智能企业网关设备静态路由配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">EquipmentWan</td>
                    <td>ShowEquipmentWanInfo</td>
                    <td>查询智能企业网关设备WAN口配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEquipmentWanConfig</td>
                    <td>更新智能企业网关设备WAN口配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">EquipmentWlan</td>
                    <td>ShowEquipmentWlan</td>
                    <td>查询智能企业网关设备Wlan配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEquipmentWlan</td>
                    <td>配置智能企业网关设备Wlan</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ErRelationship</td>
                    <td>DeleteEcnWithEr</td>
                    <td>解除企业路由器和企业连接网络的关联</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddEcnWithEr</td>
                    <td>关联企业路由器到企业连接网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEcnWithEr</td>
                    <td>根据企业连接网络ID,查询企业连接网络网与企业路由器关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">IntelligentEnterpriseGateway</td>
                    <td>ChangeIegPassword</td>
                    <td>修改IEG设备admin账户密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchEquipmentHaType</td>
                    <td>交换双机主备属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIeg</td>
                    <td>查询租户智能企业网关列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIegInfo</td>
                    <td>根据智能企业网关ID,查询租户智能企业网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIeg</td>
                    <td>根据智能企业网关ID,更新智能企业网关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Quota</td>
                    <td>ShowQuotasInfo</td>
                    <td>查询EC相关的指定租户的配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">VpcRelationship</td>
                    <td>AddEcnWithVpc</td>
                    <td>关联虚拟私有云到企业连接网络</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEcnWithVpc</td>
                    <td>根据企业连接网络ID,查询企业连接网络与虚拟私有云关联关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEcnWithVpc</td>
                    <td>更新虚拟私有云和企业连接网络的关联</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEcnWithVpc</td>
                    <td>解除虚拟私有云和企业连接网络的关联</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">VrrpConfig</td>
                    <td>UpdateVrrpConfig</td>
                    <td>更新vrrp配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVrrpConfig</td>
                    <td>删除vrrp配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVrrpConfig</td>
                    <td>查询vrrp配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddVrrpConfig</td>
                    <td>创建vrrp配置</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>