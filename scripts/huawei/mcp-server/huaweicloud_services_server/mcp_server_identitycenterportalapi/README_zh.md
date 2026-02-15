# IdentityCenterPortalAPI MCP Server 

## 版本信息
v0.1.0

## 产品描述

IdentityCenterPortalAPI MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IdentityCenterPortalAPI交互的能力。可以基于自然语言对IdentityCenterPortalAPI资源进行全链路管理。

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
                    <td rowspan="1">Account</td>
                    <td>ListAccounts</td>
                    <td>列出分配给用户的所有账号</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Agency</td>
                    <td>ListAccountAgencies</td>
                    <td>列出账号分配给用户的所有委托或信任委托</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Credential</td>
                    <td>GetAgencyCredentials</td>
                    <td>获取分配给用户的指定委托或信任委托的STS短期凭证</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">Token</td>
                    <td>Logout</td>
                    <td>向IAM身份中心服务发送API调用,使相应的服务端IAM身份中心登录会话失效。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>