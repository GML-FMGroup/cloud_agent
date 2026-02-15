# KooPhone MCP Server 

## 版本信息
v0.1.0

## 产品描述

KooPhone MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务KooPhone交互的能力。可以基于自然语言对KooPhone资源进行全链路管理。

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
                    <td rowspan="9">实例管理</td>
                    <td>AsyncInvokeInstance</td>
                    <td>实例执行异步命令接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchResetInstance</td>
                    <td>实例批量重置,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetVideo</td>
                    <td>实例视频设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelInstance</td>
                    <td>调用此api的前提条件是租户需要先购买koophone云手机实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteJob</td>
                    <td>实例执行任务批量查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowInstance</td>
                    <td>实例状态批量查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ProvisionInstance</td>
                    <td>调用此api的前提条件是租户需要先购买koophone云手机实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteInstanceAuthToken</td>
                    <td>租户实例串流前获取设备的device_token,</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncInvokeInstance</td>
                    <td>实例执行同步命令接口。调用此api的前提条件是租户需要先购买koophone云手机实例。可以通过调用该接口实现对自己的koophone云手机实例进行adb指令操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">实例订购</td>
                    <td>DeleteInstance</td>
                    <td>调用此api的前提条件是租户需要先购买koophone云手机实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowSku</td>
                    <td>实例sku批量查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>租户可以通过调用该接口生成实例。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>