# CloudTable MCP Server 

## 版本信息
v0.1.0

## 产品描述

CloudTable MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CloudTable交互的能力。可以基于自然语言对CloudTable资源进行全链路管理。

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
                    <td rowspan="9">CloudTable集群管理接口</td>
                    <td>ShowClusterDetail</td>
                    <td>通过集群ID唯一标识一个集群,根据集群ID查询特定CloudTable集群的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>创建一个CloudTable集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RebootCloudTableCluster</td>
                    <td>重启集群的api入口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCluster</td>
                    <td>集群ID为集群唯一标识,根据集群ID删除指定集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>查看用户创建的集群列表信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateClusterSetting</td>
                    <td>修改集群配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExpandClusterComponent</td>
                    <td>扩容指定类型的集群节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusterSetting</td>
                    <td>查询集群配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableComponent</td>
                    <td>开启opentsdb组件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CloudTable集群管理接口v3</td>
                    <td>CreateCloudTableCluster</td>
                    <td>创建一个CloudTable集群。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>