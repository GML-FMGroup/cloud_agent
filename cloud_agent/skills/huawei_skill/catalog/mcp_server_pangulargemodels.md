# PanguLargeModels MCP Server 

## 版本信息
v0.1.0

## 产品描述

PanguLargeModels MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务PanguLargeModels交互的能力。可以基于自然语言对PanguLargeModels资源进行全链路管理。

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
                    <td rowspan="2">Completions</td>
                    <td>ExecuteTextCompletion</td>
                    <td>给定一个提示和一些参数,模型会根据这些信息生成一个或多个预测的补全,还可以返回每个位置上不同词语的概率。它可以用来做文本生成、自动写作、代码补全等任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteChatCompletion</td>
                    <td>基于对话问答功能,用户可以与模型进行自然而流畅的对话和交流。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>