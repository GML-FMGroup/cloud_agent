# ocv2x MCP Server 

## 版本信息
v0.1.0

## 产品描述

ocv2x MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务ocv2x交互的能力。可以基于自然语言对ocv2x资源进行全链路管理。

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
                    <td rowspan="2">APIG-SN-DataAgingConfig</td>
                    <td>putDataAgingConfig</td>
                    <td>修改历史数据老化时间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>getDataAgingConfig</td>
                    <td>查询老化时间配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">APIG-SN-HistoryTrafficEvents</td>
                    <td>getHistoryTrafficEvents</td>
                    <td>条件查询交通事</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">APIG-SN-VehicleHistory</td>
                    <td>getVehicleHistory</td>
                    <td>条件查询车辆数据</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>