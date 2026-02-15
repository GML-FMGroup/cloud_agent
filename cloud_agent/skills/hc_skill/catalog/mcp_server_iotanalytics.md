# IoTAnalytics MCP Server 

## 版本信息
v0.1.0

## 产品描述

IoTAnalytics MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IoTAnalytics交互的能力。可以基于自然语言对IoTAnalytics资源进行全链路管理。

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
                    <td rowspan="5">AssetModel</td>
                    <td>UpdateAssetModel</td>
                    <td>修改资产模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAssetModel</td>
                    <td>创建资产模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssetModels</td>
                    <td>获取资产模型列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAssetModel</td>
                    <td>删除资产模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetModel</td>
                    <td>获取资产模型详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">AssetNew</td>
                    <td>DeleteAssetNew</td>
                    <td>删除资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishRootAsset</td>
                    <td>发布资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssetsNew</td>
                    <td>获取资产列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAssetNew</td>
                    <td>修改资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAssetNew</td>
                    <td>创建资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetNew</td>
                    <td>获取资产详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">AssetProperty</td>
                    <td>ShowLastPropertyValue</td>
                    <td>获取资产属性最新值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPropertyRawValue</td>
                    <td>获取资产属性历史值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMetricValue</td>
                    <td>获取资产属性聚合值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DataSource</td>
                    <td>ShowAllDataSource</td>
                    <td>查询数据源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatasource</td>
                    <td>创建数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataSource</td>
                    <td>查询数据源详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataSource</td>
                    <td>修改数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatasource</td>
                    <td>删除数据源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DataStoreGroupManagement</td>
                    <td>UpdateGroup</td>
                    <td>更新存储组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGroup</td>
                    <td>删除存储组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGroups</td>
                    <td>查询存储组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGroup</td>
                    <td>创建存储组</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">DataStoreManagement</td>
                    <td>DeleteDataStore</td>
                    <td>删除存储</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataStores</td>
                    <td>查询存储列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataStore</td>
                    <td>更新存储</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">DataStoreQuery</td>
                    <td>ListHistory</td>
                    <td>根据标签查询设备历史值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMetrics</td>
                    <td>根据标签聚合、查询数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPropertyValues</td>
                    <td>查询设备属性最新状态值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DataStoreTags</td>
                    <td>ListTagValues</td>
                    <td>查询标签的值列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DevData</td>
                    <td>AddDevData</td>
                    <td>通过API数据源上报设备数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">PipelineManagement</td>
                    <td>StopPipelineJob</td>
                    <td>停止一个正在运行中的管道作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPipelineJobs</td>
                    <td>获取用户下的所有管道作业,支持分页。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPipelineJob</td>
                    <td>获取指定管道作业的详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPipelineJob</td>
                    <td>新建管道作业时,需要在URL中指定是更新哪一个作业,将在body中附带完整的作业信息。(作业中各算子的详细配置请参考算子配置章节。) check参数表示是否需要对作业配置进行检查,若为false,则不检查,将作业保存为草稿;若为true,则对作业配置进行检查。当检查不通过时,将作业状态修改为草稿;检查通过时,将作业状态修改为就绪,并返回成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePipelineJob</td>
                    <td>删除用户指定的管道作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartPipelineJob</td>
                    <td>提交管道作业到运行环境,实时接收数据源的数据并按用户定义的数据清洗逻辑对数据进行处理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePipelineJob</td>
                    <td>更新管道作业时,需要在URL中指定是更新哪一个作业,将在body中附带完整的作业信息。(管道作业详细配置,每个作业可选择不同的算子进行组合,各算子的使用方法详见:数据管道算子配置指南。) check参数表示是否需要对作业配置进行检查,若为false,则不检查,将作业保存为草稿;若为true,则对作业配置进行检查。当检查不通过时,将作业状态修改为草稿;检查通过时,将作业状态修改为就绪,并返回成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">RTAManagement</td>
                    <td>UpdateStreamingJob</td>
                    <td>更新作业时,需要在URL中指定是更新哪一个作业,将在body中附带完整的作业信息。 check参数表示是否需要对作业配置进行检查,若为false,则不检查,将作业保存为草稿;若为true,则对作业配置进行检查,无论检查是否通过,都将作业及配置信息保存为草稿,当检查不通过时,返回失败及错误信息,检查通过时,将作业状态修改为就绪,并返回成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStreamingJob</td>
                    <td>除名称和描述外,可先不提供作业的详细配置信息。 check参数表示是否需要对作业配置进行检查,若为false,则不检查,将作业保存为草稿;若为true,则对作业配置进行检查,无论检查是否通过,都将作业及配置信息保存为草稿,当检查不通过时,返回失败及错误信息,检查通过时,将作业状态修改为就绪,并返回成功。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobs</td>
                    <td>获取用户下的所有实时分析作业,支持分页。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobById</td>
                    <td>获取指定作业的详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStreamingJobById</td>
                    <td>删除用户指定的作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">RTAOperation</td>
                    <td>StartJob</td>
                    <td>提交作业到运行环境,实时接收数据并按用户定义的业务逻辑对数据进行处理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopJob</td>
                    <td>停止一个正在运行中的作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">computingResource</td>
                    <td>DeleteComputingResource</td>
                    <td>删除批计算资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateComputingResource</td>
                    <td>创建批计算资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComputingResources</td>
                    <td>查询批计算资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">dataset</td>
                    <td>ImportData</td>
                    <td>将数据从文件导入OBS表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportDataset</td>
                    <td>将SQL语句的查询结果下载到本地,只支持下载“QUERY”类型作业的查询结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataset</td>
                    <td>在执行SQL查询语句的作业完成后,查看该作业执行的结果。目前仅支持查看“QUERY”类型作业的执行结果。该API只能查看前1000条的结果记录,若要查看全部的结果记录,需要先导出查询结果再进行查看。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateSql</td>
                    <td>检查离线作业SQL语法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">job</td>
                    <td>DeleteBatchJob</td>
                    <td>删除离线作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBatchJob</td>
                    <td>创建离线作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBatchJob</td>
                    <td>查询离线作业详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBatchJob</td>
                    <td>修改离线作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBatchJobs</td>
                    <td>查询离线作业列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">run</td>
                    <td>ListRuns</td>
                    <td>查询离线作业运行列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRun</td>
                    <td>查询离线作业运行详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRun</td>
                    <td>停止提交中或运行中的离线作业,若作业已经执行结束或失败则无法停止。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRun</td>
                    <td>执行离线作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">table</td>
                    <td>ShowTablePreview</td>
                    <td>预览离线数据表内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTableSchema</td>
                    <td>查询离线数据表结构。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTable</td>
                    <td>创建离线数据表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTables</td>
                    <td>查询离线数据表列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTable</td>
                    <td>删除离线数据表。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>