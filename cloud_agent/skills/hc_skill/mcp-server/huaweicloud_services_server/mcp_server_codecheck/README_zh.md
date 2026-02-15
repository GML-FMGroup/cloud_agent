# CodeCheck MCP Server 

## 版本信息
v0.1.0

## 产品描述

CodeCheck MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CodeCheck交互的能力。可以基于自然语言对CodeCheck资源进行全链路管理。

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
                    <td rowspan="18">任务管理</td>
                    <td>StopTaskById</td>
                    <td>根据任务ID终止检查任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>删除检查任务,执行中的任务删除无法再查看</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskRuleset</td>
                    <td>修改任务规则集。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTasklog</td>
                    <td>查询任务检查失败日志,不传execute_id则查询最近一次的检查日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskSettings</td>
                    <td>查询任务的高级选项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckParameters</td>
                    <td>查询任务规则集的检查参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskParameter</td>
                    <td>任务配置检查参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskPathTree</td>
                    <td>获取任务的目录树</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckRulesetParameters</td>
                    <td>查询任务规则集的检查参数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskSettings</td>
                    <td>任务配置高级选项,如自定义镜像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>新建检查任务但是不执行。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTasksRulesets</td>
                    <td>查询任务的已选规则集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProgressDetail</td>
                    <td>根据任务ID查询任务执行状态。任务状态:0表示检查中,1表示检查失败,2表示检查成功,3表示任务中止。只有正在检查中才有进度的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskListByProjectId</td>
                    <td>根据DEVCLOUD_PROJECT_UUID查询该项目下的任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckRecord</td>
                    <td>提供每次扫描的问题数量统计</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskRuleset</td>
                    <td>查询任务的已选规则集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunTask</td>
                    <td>执行检查任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIgnorePath</td>
                    <td>任务配置屏蔽目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">缺陷管理</td>
                    <td>ShowTaskDefectsStatistic</td>
                    <td>根据检查任务ID查询缺陷详情的统计</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDefectStatus</td>
                    <td>修改检查出的缺陷的状态为已解决、已忽略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskDetail</td>
                    <td>根据检查任务ID查询缺陷结果的概要。包括问题概述、问题状态、圈复杂度、代码重复率等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskCmetrics</td>
                    <td>根据检查任务ID查询cmertrics缺陷概要。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskDefects</td>
                    <td>根据检查任务ID分页查询缺陷结果详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">规则管理</td>
                    <td>ListRulesets</td>
                    <td>根据项目ID、语言等条件查询规则集列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRuleset</td>
                    <td>可根据需求灵活的组合规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplateRules</td>
                    <td>根据项目ID、规则集ID等条件查询规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRuleset</td>
                    <td>删除自定义规则集,正在使用中的或默认规则集不能删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDefaulTemplate</td>
                    <td>设置每个项目对应语言的默认规则集配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRules</td>
                    <td>根据语言、问题级别等条件查询规则列表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>