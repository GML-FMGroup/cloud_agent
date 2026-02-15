# CodeCraft MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeCraft MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeCraft交互的能力。可以基于自然语言对CodeCraft资源进行全链路管理。

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
                    <td rowspan="4">作品管理</td>
                    <td>UpdateCompetitionScore</td>
                    <td>针对在大赛平台提交作品的场景:第三方服务对作品完成判分后,根据作品ID调用该接口将作品分数、作品状态等信息返回给大赛平台</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterCompetitionInfo</td>
                    <td>第三方服务验证用户是否在大赛平台报名、是否组建团队、是否可以提交作品。如果已经报名但是未组建团队,则创建一个虚拟团队,设置为允许提交作品。如果已经组建团队则根据大赛报名截止时间判断是否可以提交作品。返回团队ID、是否可以提交作品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCompetitionWorks</td>
                    <td>第三方服务获取某个大赛某个阶段中一段时间内提交的作品信息。其中以请求参数read_time作为结束时间,定义向前一天或一小时内的时间作为查询范围</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCompetitionScore</td>
                    <td>针对在第三方提交作品的场景:第三方服务对作品完成判分后,调用该接口将作品信息及作品得分返回给大赛平台</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>