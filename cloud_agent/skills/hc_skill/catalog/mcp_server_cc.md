# CC MCP Server 

## 版本信息
v0.1.0

## 产品描述

CC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CC交互的能力。可以基于自然语言对CC资源进行全链路管理。

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
                    <td rowspan="5">Authorisation</td>
                    <td>UpdateAuthorisation</td>
                    <td>更新授权实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPermissions</td>
                    <td>云连接实例所属租户查询其可加载其他租户的网络实例权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAuthorisations</td>
                    <td>网络实例所属租户查看其已经授予其他租户的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAuthorisation</td>
                    <td>网络实例所属租户授予云连接实例所属租户加载其网络实例的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAuthorisation</td>
                    <td>网络实例所属租户取消授予云连接实例所属租户加载其网络实例的权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">BandwidthPackage</td>
                    <td>ListBandwidthPackageTags</td>
                    <td>查询带宽包的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBandwidthPackage</td>
                    <td>查询带宽包实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateBandwidthPackage</td>
                    <td>解除带宽包实例与云连接实例的绑定。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBandwidthPackage</td>
                    <td>创建带宽包实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBandwidthPackage</td>
                    <td>删除带宽包实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthPackages</td>
                    <td>查询带宽包列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateBandwidthPackage</td>
                    <td>将带宽包实例绑定到云连接实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthPackagesByTags</td>
                    <td>通过标签过滤带宽包实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>TagBandwidthPackage</td>
                    <td>创建带宽包标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBandwidthPackage</td>
                    <td>更新带宽包实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UntagBandwidthPackage</td>
                    <td>删除带宽包标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">CentralNetwork</td>
                    <td>ApplyCentralNetworkPolicy</td>
                    <td>应用中心网络策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCentralNetworkTags</td>
                    <td>查询中心网络的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCentralNetwork</td>
                    <td>创建中心网络。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCentralNetwork</td>
                    <td>删除中心网络,请先清除附件后再删除中心网络。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCentralNetwork</td>
                    <td>更新中心网络详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCentralNetworkPolicy</td>
                    <td>删除中心网络策略版本。您无法删除正在被应用的中心策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCentralNetworkPolicyChangeSet</td>
                    <td>查询与当前应用中心网络策略的变化集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCentralNetworkPolicies</td>
                    <td>查询所有版本的中心网络策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCentralNetworkPolicy</td>
                    <td>创建一份只读的中心网络的策略。如果您有策略文档内容改动,需要基于此版本重新创建一个新版本的策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCentralNetworks</td>
                    <td>查询中心网络列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UntagCentralNetwork</td>
                    <td>删除中心网络标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCentralNetwork</td>
                    <td>查询中心网络详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>TagCentralNetwork</td>
                    <td>创建中心网络标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCentralNetworksByTags</td>
                    <td>通过标签过滤中心网络实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">CentralNetworkAttachment</td>
                    <td>ShowCentralNetworkGdgwAttachment</td>
                    <td>查询中心网络GDGW附件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCentralNetworkErRouteTableAttachment</td>
                    <td>创建中心网络的路由表附件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCentralNetworkAttachment</td>
                    <td>删除中心网络附件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCentralNetworkErRouteTableAttachment</td>
                    <td>更新中心网络ER路由表附件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCentralNetworkAttachments</td>
                    <td>查询中心网络附件列表,分页查询使用的参数为marker、limit。limit默认值为0,没有指定marker时返回第一条数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCentralNetworkGdgwAttachment</td>
                    <td>更新中心网络GDGW附件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCentralNetworkGdgwAttachment</td>
                    <td>创建中心网络的GDGW附件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCentralNetworkErRouteTableAttachments</td>
                    <td>查询中心网络ER路由表附件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCentralNetworkGdgwAttachments</td>
                    <td>查询中心网络GDGW附件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCentralNetworkErRouteTableAttachment</td>
                    <td>查询中心网络ER路由表附件详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CentralNetworkCapabilities</td>
                    <td>ListCentralNetworkCapabilities</td>
                    <td>查询中心网络能力列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">CentralNetworkConnection</td>
                    <td>ListCentralNetworkConnections</td>
                    <td>查询中心网络连接列表接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCentralNetworkConnection</td>
                    <td>更新中心网络连接接口(仅支持更新带宽)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CentralNetworkQuotas</td>
                    <td>ListCentralNetworkQuotas</td>
                    <td>查询中心网络配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">CloudConnection</td>
                    <td>TagCloudConnection</td>
                    <td>创建云连接实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UntagCloudConnection</td>
                    <td>删除云连接实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCloudConnection</td>
                    <td>创建云连接实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudConnectionsByTags</td>
                    <td>通过标签过滤云连接实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudConnectionTags</td>
                    <td>查询云连接实例的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCloudConnection</td>
                    <td>更新云连接实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCloudConnection</td>
                    <td>删除云连接实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudConnections</td>
                    <td>查询云连接列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCloudConnection</td>
                    <td>查询云连接实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CloudConnectionCapabilities</td>
                    <td>ListCloudConnectionCapabilities</td>
                    <td>查询云连接的能力列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CloudConnectionQuotas</td>
                    <td>ListCloudConnectionQuotas</td>
                    <td>查询云连接配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">CloudConnectionRoute</td>
                    <td>ShowCloudConnectionRoutes</td>
                    <td>查询云连接路由条目列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCloudConnectionRoutes</td>
                    <td>查询云连接路由条目列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">GcbTagManager</td>
                    <td>CreateGcbResourceTag</td>
                    <td>添加账户全域互联带宽资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateGcbResourceTags</td>
                    <td>TMS批量添加资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGcbResourceTag</td>
                    <td>删除账户全域互联带宽资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteGcbResourceTags</td>
                    <td>批量删除账户全域互联带宽资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountGcbResourceByTag</td>
                    <td>查询账户全域互联带宽资源标签数量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGcbTenantTags</td>
                    <td>查询账户全域互联带宽所有资源标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGcbResourceByTag</td>
                    <td>查询账户全域互联带宽资源实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGcbResourceTags</td>
                    <td>查询账户全域互联带宽资源的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">GlobalConnectionBandwidth</td>
                    <td>UpdateGlobalConnectionBandwidth</td>
                    <td>更新全域互联带宽详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGlobalConnectionBandwidth</td>
                    <td>删除全域互联带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSupportBindingConnectionBandwidths</td>
                    <td>查询符合绑定条件的全域互联带宽列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalConnectionBandwidthLineLevels</td>
                    <td>查询线路等级列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGlobalConnectionBandwidth</td>
                    <td>查询全域互联带宽详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AssociateGlobalConnectionBandwidthInstance</td>
                    <td>全域互联带宽绑定实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalConnectionBandwidths</td>
                    <td>查询全域互联带宽列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalConnectionBandwidthSpecCodes</td>
                    <td>查询线路规格列表。租户白名单控制,默认为空。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateGlobalConnectionBandwidthInstance</td>
                    <td>全域互联带宽解绑实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGlobalConnectionBandwidth</td>
                    <td>创建全域互联带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalConnectionBandwidthSites</td>
                    <td>查询站点列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalConnectionBandwidthConfigs</td>
                    <td>查询全域互联带宽租户配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">InterRegionBandwidth</td>
                    <td>ListInterRegionBandwidths</td>
                    <td>查询域间带宽列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInterRegionBandwidth</td>
                    <td>查询域间带宽实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInterRegionBandwidth</td>
                    <td>更新域间带宽实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInterRegionBandwidth</td>
                    <td>删除域间带宽实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInterRegionBandwidth</td>
                    <td>创建域间带宽实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">NetworkInstance</td>
                    <td>ShowNetworkInstance</td>
                    <td>查询网络实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNetworkInstances</td>
                    <td>查询网络实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNetworkInstance</td>
                    <td>创建网络实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNetworkInstance</td>
                    <td>更新网络实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNetworkInstance</td>
                    <td>删除网络实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">SiteConnection</td>
                    <td>AssociateSiteNetworkBandwidth</td>
                    <td>关联分支连接带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSiteNetworkBandwidthSize</td>
                    <td>更改分支连接带宽大小。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateSiteNetworkBandwidth</td>
                    <td>解关联分支连接带宽。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSiteNetworkBandwidth</td>
                    <td>更改分支连接带宽包。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">SiteNetwork</td>
                    <td>DeleteSiteNetwork</td>
                    <td>删除分支网络。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSiteNetwork</td>
                    <td>查询分支网络详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateP2PSiteNetwork</td>
                    <td>创建P2P类型的分支网络。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSiteNetwork</td>
                    <td>更新分支网络详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSiteNetworks</td>
                    <td>查询分支网络列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">SiteNetworkCapabilities</td>
                    <td>ListSiteNetworkCapabilities</td>
                    <td>查询分支网络的能力列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">SiteNetworkQuotas</td>
                    <td>ListSiteNetworkQuotas</td>
                    <td>查询分支网络配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">Specifications</td>
                    <td>ListBandwidthPackageSites</td>
                    <td>查询带宽包站点列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthPackageLines</td>
                    <td>查询带宽包线路列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRegionBandwidthPackageSpecifications</td>
                    <td>查询区域互通类型的带宽包规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthPackageLevels</td>
                    <td>查询带宽包等级列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAreaBandwidthPackageSpecifications</td>
                    <td>查询大区互通类型的带宽包资源规格列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRegions</td>
                    <td>查询当前支持的Region列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAreas</td>
                    <td>查询当前支持的大区列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">TagManager</td>
                    <td>BatchCreateDeleteTags</td>
                    <td>批量创建和删除标签。此API为历史API,请优先使用《 创建云连接实例标签》、《 创建带宽包标签》、《 删除云连接实例标签》、《 删除带宽包标签》。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceByFilterTag</td>
                    <td>查询资源实例。此API为历史API,请优先使用《通过标签过滤云连接实例》、《通过标签过滤带宽包实例》。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTags</td>
                    <td>查询资源标签。此API为历史API,请优先使用《查询云连接实例的标签信息》、《查询带宽包的标签信息》。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainTags</td>
                    <td>查询账户资源标签。此API为历史API,请优先使用《查询云连接实例的标签信息》、《查询带宽包的标签信息》。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTag</td>
                    <td>删除资源标签。此API为历史API,请优先使用《 删除云连接实例标签》或《 删除带宽包标签》。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTag</td>
                    <td>添加资源标签。此API为历史API,请优先使用《 创建云连接实例标签》、《 创建带宽包标签》。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>