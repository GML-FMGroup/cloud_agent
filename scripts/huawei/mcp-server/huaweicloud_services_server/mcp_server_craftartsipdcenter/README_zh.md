# CraftArtsIPDCenter MCP Server 

## 版本信息
v0.1.0

## 产品描述

CraftArtsIPDCenter MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CraftArtsIPDCenter交互的能力。可以基于自然语言对CraftArtsIPDCenter资源进行全链路管理。

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
                    <td rowspan="1">Station</td>
                    <td>SearchStationsByConditionsForTest</td>
                    <td>测试根据条件获取工位、工序、线体详细信息,工位编码必填。其他非必填入参需保证与工位编码存在关联关系。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">数字化制造云平台生产数据管理</td>
                    <td>BatchDeleteWos</td>
                    <td>批量删除工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateWos</td>
                    <td>导入工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateWoInstantiations</td>
                    <td>批量实例化工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchWoInfo</td>
                    <td>获取工单相关信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCancelWos</td>
                    <td>批量取消工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchGenerateWoSchemes</td>
                    <td>批量生成工单方案</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchWosForPage</td>
                    <td>分页查询工单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchWoPartInfo</td>
                    <td>获取工单产品信息</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>