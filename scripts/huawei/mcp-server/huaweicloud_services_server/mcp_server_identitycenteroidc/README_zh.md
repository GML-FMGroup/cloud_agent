# IdentityCenterOIDC MCP Server 

## 版本信息
v0.1.0

## 产品描述

IdentityCenterOIDC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IdentityCenterOIDC交互的能力。可以基于自然语言对IdentityCenterOIDC资源进行全链路管理。

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
                    <td rowspan="1">Client</td>
                    <td>RegisterClient</td>
                    <td>向IAM身份中心注册客户端,这允许客户端启动设备授权,输出应该持久化以便于身份验证请求重用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DeviceAuthorization</td>
                    <td>StartDeviceAuthorization</td>
                    <td>发起设备授权请求</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Token</td>
                    <td>CreateToken</td>
                    <td>获取访问令牌</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>