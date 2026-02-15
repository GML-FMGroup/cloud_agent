# Anti-DDoS MCP Server 

## 版本信息
v0.1.0

## 产品描述

Anti-DDoS MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务Anti-DDoS交互的能力。可以基于自然语言对Anti-DDoS资源进行全链路管理。

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
                    <td rowspan="1">DDoS任务管理</td>
                    <td>ShowNewTaskStatus</td>
                    <td>用户查询指定的Anti-DDoS防护配置任务,得到任务当前执行的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">DDoS防护管理</td>
                    <td>ShowLogConfig</td>
                    <td>查询全量日志设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDailyLog</td>
                    <td>查询指定EIP在过去24小时之内的异常事件信息,异常事件包括清洗事件和黑洞事件,查询延迟在5分钟之内。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogConfig</td>
                    <td>更新用户全量日志设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDDosStatus</td>
                    <td>查询指定EIP的Anti-DDoS防护状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDDosStatus</td>
                    <td>查询用户所有EIP的Anti-DDoS防护状态信息,用户的EIP无论是否绑定到云服务器,都可以进行查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableDefensePolicy</td>
                    <td>开通DDoS服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNewConfigs</td>
                    <td>查询系统支持的Anti-DDoS防护策略配置的可选范围,用户根据范围列表选择适合自已业务的防护策略进行Anti-DDoS流量清洗。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWeeklyReports</td>
                    <td>查询用户所有Anti-DDoS防护周统计情况,包括一周内DDoS拦截次数和攻击次数、以及按照被攻击次数进行的排名信息等统计数据。系统支持当前时间之前四周的周统计数据查询,超过这个时间的请求是查询不到统计数据的。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDailyReport</td>
                    <td>查询指定EIP在过去24小时之内的防护流量信息,流量的间隔时间单位为5分钟。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDDos</td>
                    <td>查询配置的Anti-DDoS防护策略,用户可以查询指定EIP的Anti-DDoS防护策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQuota</td>
                    <td>查询配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDDos</td>
                    <td>更新指定EIP的Anti-DDoS防护策略配置。调用成功,只是说明服务节点收到了关闭更新配置请求,操作是否成功需要通过任务查询接口查询该任务的执行状态,具体请参考查询Anti-DDoS任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">告警配置管理</td>
                    <td>ShowAlertConfig</td>
                    <td>查询用户配置信息,用户可以通过此接口查询是否接收某类告警,同时可以配置是手机短信还是电子邮件接收告警信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlertConfig</td>
                    <td>更新用户配置信息,用户可以通过此接口更新是否接收某类告警,同时可以配置是手机短信还是电子邮件接收告警信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">默认防护策略管理</td>
                    <td>DeleteDefaultConfig</td>
                    <td>删除用户配置的默认防护策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDefaultConfig</td>
                    <td>查询用户配置的默认防护策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDefaultConfig</td>
                    <td>配置用户的默认防护策略。配置防护策略后,新购买的资源在自动开启防护时,会按照该默认防护策略进行配置。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>