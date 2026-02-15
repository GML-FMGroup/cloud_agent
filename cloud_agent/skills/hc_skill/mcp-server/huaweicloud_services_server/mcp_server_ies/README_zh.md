# IES MCP Server 

## 版本信息
v0.1.0

## 产品描述

IES MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IES交互的能力。可以基于自然语言对IES资源进行全链路管理。

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
                    <td rowspan="5">edge-site</td>
                    <td>ListEdgeSites</td>
                    <td>查询边缘小站列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeSite</td>
                    <td>查询边缘小站详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeSite</td>
                    <td>更新边缘小站。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeSite</td>
                    <td>创建边缘小站。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeSite</td>
                    <td>删除指定的边缘小站。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">monitor</td>
                    <td>ListEdgeSiteMetrics</td>
                    <td>查看站点容量信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">quota</td>
                    <td>ListQuotas</td>
                    <td>查询租户资源配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">rack</td>
                    <td>ShowRack</td>
                    <td>查询机柜详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRacks</td>
                    <td>查询机柜列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">region</td>
                    <td>ListSupportedRegions</td>
                    <td>查询支持智能边缘小站接入的华为云区域(region)列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">storage-pool</td>
                    <td>ShowStoragePool</td>
                    <td>查询存储池详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStoragePools</td>
                    <td>查询存储池列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>