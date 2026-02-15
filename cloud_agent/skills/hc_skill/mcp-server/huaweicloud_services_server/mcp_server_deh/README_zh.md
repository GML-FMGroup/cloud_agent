# DeH MCP Server 

## 版本信息
v0.1.0

## 产品描述

DeH MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务DeH交互的能力。可以基于自然语言对DeH资源进行全链路管理。

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
                    <td rowspan="2">查询API版本信息</td>
                    <td>ShowDehVersion</td>
                    <td>返回专属主机指定版本的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDehVersions</td>
                    <td>返回专属主机当前所有可用的版本信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签管理</td>
                    <td>BatchCreateDedicatedHostTags</td>
                    <td>为指定专属主机批量添加标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteDedicatedHostTags</td>
                    <td>批量删除指定专属主机标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDedicatedHostTags</td>
                    <td>查询指定专属主机的标签信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDedicatedHostsByTags</td>
                    <td>使用标签过滤专属主机列表,并返回专属主机使用的所有标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">生命周期管理</td>
                    <td>ShowDedicatedHost</td>
                    <td>查询某一台专属主机的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListServersDedicatedHost</td>
                    <td>查询专属主机上已部署的云服务器信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDedicatedHost</td>
                    <td>该接口用于变更专属主机的“auto_placement”和“name”属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDedicatedHostTypes</td>
                    <td>查询某一AZ内可用的专属主机类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDedicatedHosts</td>
                    <td>通过该接口查询专属主机列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">配额设置</td>
                    <td>ShowQuotaSets</td>
                    <td>该接口用于查询租户的专属主机配额。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>