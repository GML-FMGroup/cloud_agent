# APIExplorer MCP Server 

## 版本信息
v0.1.0

## 产品描述

APIExplorer MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务APIExplorer交互的能力。可以基于自然语言对APIExplorer资源进行全链路管理。

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
                    <td rowspan="1">ApiServerV2</td>
                    <td>ListApis</td>
                    <td>获取指定产品的API列表,或者根据api中英文名模糊匹配API列表,支持分页</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ApiServerV3</td>
                    <td>ShowApi</td>
                    <td>根据产品短名、api名及regionId获取API的详情信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">GroupServer</td>
                    <td>ListGroups</td>
                    <td>根据产品短名,获取该产品的所有分组信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">MockServer</td>
                    <td>ShowMockData</td>
                    <td>根据Yaml中API返回的示例获取模拟数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">ProductServerV4</td>
                    <td>ListProductsV4</td>
                    <td>查询云服务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">RegionServerV4</td>
                    <td>ListRegionsV4</td>
                    <td>- 获取用户在该API有调试权限的region列表</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>