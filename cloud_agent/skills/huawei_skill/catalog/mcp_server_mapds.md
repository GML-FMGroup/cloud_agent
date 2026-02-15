# MapDS MCP Server 

## 版本信息
v0.1.0

## 产品描述

MapDS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务MapDS交互的能力。可以基于自然语言对MapDS资源进行全链路管理。

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
                    <td rowspan="4">凭证管理</td>
                    <td>CreateSasToken</td>
                    <td>创建SAS token凭据,用于访问瓦片。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCredential</td>
                    <td>该接口用于创建访问地图数据服务的凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCredential</td>
                    <td>该接口用于查询访问地图数据服务的凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCedential</td>
                    <td>该接口用于删除访问地图数据服务的凭证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">获取地图瓦片</td>
                    <td>ShowMapTile</td>
                    <td>该接口用于获取地图瓦片。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>