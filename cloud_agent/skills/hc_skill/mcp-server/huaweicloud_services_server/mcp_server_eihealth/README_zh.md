# eiHealth MCP Server 

## 版本信息
v0.1.0

## 产品描述

eiHealth MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务eiHealth交互的能力。可以基于自然语言对eiHealth资源进行全链路管理。

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
                    <td rowspan="2">ADMET</td>
                    <td>ShowAdmetWithCustomProps</td>
                    <td>计算小分子的物化性质,包括默认的吸收(adsorption)、分布(distribution)、代谢(metabolism)、清除(excretion)与毒性(toxicity),以及用户自定义的属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAdmetProperties</td>
                    <td>计算小分子的物化性质,包括吸收(adsorption)、分布(distribution)、代谢(metabolism)、清除(excretion)与毒性(toxicity)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">CPI</td>
                    <td>CreateCpiTask</td>
                    <td>输入蛋白序列、小分子库,创建分子-蛋白互作预测任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCpiTaskResult</td>
                    <td>通过CPI任务ID查询CPI任务状态及结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">CPI作业管理</td>
                    <td>CreateCpiJob</td>
                    <td>创建CPI作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCpiJob</td>
                    <td>查询CPI作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">CSS集群管理</td>
                    <td>DeleteCssCluster</td>
                    <td>CSS集群解绑</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCssCluster</td>
                    <td>绑定CSS集群</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTermTenantCssCluster</td>
                    <td>获取最终租户CSS集群列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateCssConnection</td>
                    <td>测试CSS集群连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCssCluster</td>
                    <td>获取CSS集群列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">CustomProps</td>
                    <td>ShowCustomPropsTaskResult</td>
                    <td>通过自定义属性任务ID查询任务状态及结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCustomPropsTask</td>
                    <td>输入自定义属性的任务数据,创建自定义属性建模任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Generation</td>
                    <td>ShowGenerationTaskResult</td>
                    <td>通过分子生成任务ID查询分子生成任务状态及结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGenerationTask</td>
                    <td>输入分子属性约束,创建分子生成任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">IDrugCommonController</td>
                    <td>CreateDrugLigandInteraction2dSvg</td>
                    <td>生成相互作用2D图,若不提供配体文件,则受体文件中必须包含配体;若提供配体文件,则受体中的配体(若有)则会被忽略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDrugLigandSimilarityGraphTask</td>
                    <td>查询配体相似性图计算任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDrugLigandSdf</td>
                    <td>生成分子SDF三维结构</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckDrugLigandDifference</td>
                    <td>计算配体间的3D结构差异</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDrugLigandSimilarityGraphTask</td>
                    <td>删除配体相似性图计算任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ParseDrugReceptorInfo</td>
                    <td>受体信息解析,如果有多个受体蛋白则只处理第一个,如果一个受体蛋白里结合了多个配体,则最多只处理前10个</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDrugLigandPreviewTask</td>
                    <td>创建配体文件预览任务,支持SMI、SDF、PDB、MOL2</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDrugLigandPreviewTask</td>
                    <td>查询配体文件预览任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDrugReceptorPreprocess</td>
                    <td>受体预处理,用于前端显示预处理后的受体</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RecognizeDrugReceptorPocket</td>
                    <td>检测受体口袋,检测类型基于配体,基于氨基酸残基,自动检测,自定义和全局对接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDrugLigandSimilarityGraphTask</td>
                    <td>创建配体相似性图计算任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunDrugLigandToSmilesConversion</td>
                    <td>配体格式转换为SMILES,若配体文件中存在多个分子,则只取第一个返回</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDrugLigandPreviewTask</td>
                    <td>删除配体文件预览任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDrugLigandSvg</td>
                    <td>生成分子SVG图</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">IObsController</td>
                    <td>DownloadData</td>
                    <td>文件下载</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">IOverviewController</td>
                    <td>ShowOverview</td>
                    <td>获取医疗平台信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Nextflow任务管理</td>
                    <td>ListNextflowTask</td>
                    <td>获取task列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNextflowTaskLog</td>
                    <td>获取Nextflow任务日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNextflowTaskDetail</td>
                    <td>获取task详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">Nextflow作业管理</td>
                    <td>ShowNextflowJobLog</td>
                    <td>获取Nextflow作业日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNextflowJob</td>
                    <td>删除Nextflow作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopNextflowJob</td>
                    <td>停止Nextflow作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNextflowJob</td>
                    <td>查询nextflow作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNextflowJob</td>
                    <td>获取Nextflow作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNextflowJob</td>
                    <td>创建nextflow作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNextflowJobReports</td>
                    <td>获取Nextflow作业报告</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryNextflowJob</td>
                    <td>重试Nextflow作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Nextflow引擎生命周期管理</td>
                    <td>InstallNextflow</td>
                    <td>安装Nextflow(file和version参数必须提供其中一种)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNextflowVersion</td>
                    <td>查询Nextflow版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNextflow</td>
                    <td>查询Nextflow配置详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CleanNextflowCache</td>
                    <td>清理Nextflow缓存</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UninstallNextflow</td>
                    <td>卸载Nextflow</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Nextflow流程管理</td>
                    <td>ShowNextflowWorkflow</td>
                    <td>获取流程详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNextflowWorkflow</td>
                    <td>获取流程列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNextflowWorkflow</td>
                    <td>删除流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNextflowWorkflow</td>
                    <td>更新流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNextflowWorkflow</td>
                    <td>创建流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">OBS桶管理</td>
                    <td>DownloadPublicData</td>
                    <td>文件下载</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObsBucketObject</td>
                    <td>获取用户OBS桶内对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObsBucket</td>
                    <td>获取用户OBS桶列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Optimization</td>
                    <td>CreateOptimizationTask</td>
                    <td>输入起始小分子以及属性约束,创建分子优化任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOptimizationTaskResult</td>
                    <td>通过分子优化任务ID查询分子优化任务状态及结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Search</td>
                    <td>CreateSearchTask</td>
                    <td>输入要查询的分子以及查询条件,创建分子搜索任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSearchTaskResult</td>
                    <td>通过分子搜索任务ID查询分子搜索任务状态及结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Synthesis</td>
                    <td>CreateSynthesisTask</td>
                    <td>输入要进行合成路径规划的分子以及输出可行方案的个数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSynthesisTaskResult</td>
                    <td>通过分子合成路径规划任务ID查询分子合成路径规划任务状态及结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">notebook开发环境</td>
                    <td>ListUserNotebook</td>
                    <td>获取用户所属空间的notebook列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotebook</td>
                    <td>获取notebook列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNotebook</td>
                    <td>创建notebook</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotebookTool</td>
                    <td>获取notebook工作环境</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNotebook</td>
                    <td>更新notebook</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNotebook</td>
                    <td>删除notebook</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopOrStartNotebook</td>
                    <td>启停notebook</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNotebook</td>
                    <td>获取notebook详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNotebookToken</td>
                    <td>获取notebook鉴权信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">业务委托管理</td>
                    <td>ShowAgency</td>
                    <td>获取业务委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAgency</td>
                    <td>更新业务委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">作业清理配置</td>
                    <td>ShowJobConfig</td>
                    <td>获取作业配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJobConfig</td>
                    <td>设置作业配置,目前支持修改作业保存条数(1万条-1000万条),默认设置为500万条;</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="18">作业管理</td>
                    <td>ExecuteJob</td>
                    <td>启动作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskInstanceEvents</td>
                    <td>获取子任务中实例的事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateJob</td>
                    <td>更新作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskInstances</td>
                    <td>获取子任务实例信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRetryJob</td>
                    <td>批量重试作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelJob</td>
                    <td>取消或强制作业调度</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobEvent</td>
                    <td>获取作业事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskInstancePod</td>
                    <td>获取子任务中实例的pod信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryJob</td>
                    <td>重试作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJob</td>
                    <td>获取作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskEvents</td>
                    <td>获取子任务启动事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserJob</td>
                    <td>获取用户所属空间的作业列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCancelJob</td>
                    <td>批量取消作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteJob</td>
                    <td>批量删除作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobLog</td>
                    <td>获取作业日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJob</td>
                    <td>获取作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteJob</td>
                    <td>删除作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskInstanceMetricData</td>
                    <td>获取子任务中实例的资源监控数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">供应商管理</td>
                    <td>ListVendor</td>
                    <td>获取供应商列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">分子优化作业管理</td>
                    <td>CreateOptmJob</td>
                    <td>创建分子优化作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOptmJob</td>
                    <td>查询分子优化作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">分子合成路径规划作业管理</td>
                    <td>CreateSynthesisJob</td>
                    <td>创建分子合成路径规划作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSynthesisJob</td>
                    <td>查询分子合成路径规划作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">分子对接作业管理</td>
                    <td>CreateDockingJob</td>
                    <td>创建分子对接作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDockingJob</td>
                    <td>查询分子对接作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">分子属性预测作业管理</td>
                    <td>ShowAdmetJob</td>
                    <td>查询分子属性预测作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAdmetJob</td>
                    <td>创建分子属性预测作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">分子搜索作业管理</td>
                    <td>CreateSearchJob</td>
                    <td>创建分子搜索作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSearchJob</td>
                    <td>查询分子搜索作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">分子生成作业管理</td>
                    <td>ShowGenJob</td>
                    <td>查询分子生成作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGenJob</td>
                    <td>创建分子生成作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">初始化平台</td>
                    <td>InitializePlatform</td>
                    <td>初始化平台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">存储资源查询</td>
                    <td>ListStorageResources</td>
                    <td>查询存储资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">应用管理</td>
                    <td>PublishApp</td>
                    <td>发布应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>删除应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchImportApp</td>
                    <td>批量导入应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserApp</td>
                    <td>获取用户所属空间的应用列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>更新应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApp</td>
                    <td>创建应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApp</td>
                    <td>获取应用详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApp</td>
                    <td>获取应用列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SubscribeApp</td>
                    <td>订阅应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">性能加速资源管理</td>
                    <td>ListPerformanceResources</td>
                    <td>查询性能加速资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePerformanceResource</td>
                    <td>购买性能加速资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSfsTurbos</td>
                    <td>获取sfs-turbo资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePerformanceResource</td>
                    <td>删除性能加速资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePerformanceResource</td>
                    <td>更新性能加速资源配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">收藏管理</td>
                    <td>CreateFavorite</td>
                    <td>添加收藏。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFavorite</td>
                    <td>取消收藏。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFavorite</td>
                    <td>获取收藏夹列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">数据作业管理</td>
                    <td>CancelDataJob</td>
                    <td>取消数据作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCheckpoint</td>
                    <td>获取数据作业执行日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDataJob</td>
                    <td>获取数据作业详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDataJob</td>
                    <td>获取数据作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadDataJobLog</td>
                    <td>下载数据作业执行日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryDataJob</td>
                    <td>重试数据作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDataJob</td>
                    <td>删除数据作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">数据库管理</td>
                    <td>QuoteInstance</td>
                    <td>引用数据库实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDatabaseData</td>
                    <td>删除指定行数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDatabaseData</td>
                    <td>更新数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabaseData</td>
                    <td>插入单条数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询实例详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>创建数据库实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportDatabaseData</td>
                    <td>导入数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseData</td>
                    <td>查询数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstance</td>
                    <td>获取实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">数据库资源管理</td>
                    <td>DeleteDatabaseResource</td>
                    <td>删除数据库资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseResource</td>
                    <td>查询数据库资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDatabaseResource</td>
                    <td>购买数据库资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDatabaseResourceFlavor</td>
                    <td>获取数据库资源规格列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">数据归档</td>
                    <td>DeleteBackup</td>
                    <td>删除指定的归档</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBackupPath</td>
                    <td>根据归档ID获取该归档的全数据清单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBackup</td>
                    <td>将需要归档的重要数据拷贝到数据归档桶</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreBackup</td>
                    <td>将指定的归档数据拷贝到目标项目的某个目录下</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBackup</td>
                    <td>分页查询用户管理的项目的所有历史归档记录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">数据管理</td>
                    <td>ShowDataPolicy</td>
                    <td>查询项目级数据权限控制策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SubscribeData</td>
                    <td>订阅资产市场数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateData</td>
                    <td>创建文件夹</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataPolicy</td>
                    <td>设置项目级权限控制策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBucket</td>
                    <td>获取桶列表(包含当前项目桶和引用项目桶)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportNetworkData</td>
                    <td>导入网上数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyData</td>
                    <td>复制项目数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteData</td>
                    <td>批量删除项目数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportData</td>
                    <td>导入项目数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBucketStorage</td>
                    <td>获取桶存量信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>QuoteData</td>
                    <td>引用项目数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowData</td>
                    <td>获取指定数据对象的详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDataPathPolicy</td>
                    <td>设置数据对象策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishData</td>
                    <td>发布数据资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListData</td>
                    <td>查询指定目录下的数据列表,如果不指定默认查询根目录</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadData</td>
                    <td>上传数据文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">标签管理</td>
                    <td>ListLabel</td>
                    <td>获取标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLabel</td>
                    <td>删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLabel</td>
                    <td>创建标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteLabel</td>
                    <td>批量删除标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">标签页面管理</td>
                    <td>CreateLabelPage</td>
                    <td>创建标签页面</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLabelPage</td>
                    <td>删除标签页面</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLabelPage</td>
                    <td>获取标签页面列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">模板管理</td>
                    <td>ShowTemplate</td>
                    <td>查询模板详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadTemplate</td>
                    <td>上传模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTemplate</td>
                    <td>创建模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTemplate</td>
                    <td>查询模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplate</td>
                    <td>删除模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportTemplate</td>
                    <td>从其他项目导入模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">流程管理</td>
                    <td>DeleteWorkflow</td>
                    <td>删除流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkflow</td>
                    <td>创建流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishWorkflow</td>
                    <td>发布流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflow</td>
                    <td>获取流程列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SubscribeWorkflow</td>
                    <td>订阅流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserWorkflow</td>
                    <td>获取用户所属空间的流程列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkflow</td>
                    <td>更新流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportWorkflow</td>
                    <td>导入流程</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkflow</td>
                    <td>获取流程详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">流程统计管理</td>
                    <td>ListPerformanceResourceStat</td>
                    <td>获取性能加速资源上统计信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkflowStatistic</td>
                    <td>统计应用、流程、作业数目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGlobalWorkflowStatistic</td>
                    <td>统计全局流程、作业信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">消息中心管理</td>
                    <td>CheckEmailConnection</td>
                    <td>邮箱连通性测试</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessageStatistics</td>
                    <td>统计消息信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMessageEmailConfig</td>
                    <td>设置消息邮件配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteNotice</td>
                    <td>批量删除通知消息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNotice</td>
                    <td>获取通知消息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMessageReceiveConfig</td>
                    <td>设置用户邮件配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateNotice</td>
                    <td>批量更新消息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMessage</td>
                    <td>从消息中心获取当前用户有权限查看的消息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMessageClearRule</td>
                    <td>获取消息清理规则</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMessageReceiveConfig</td>
                    <td>获取用户邮件配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMessageEmailConfig</td>
                    <td>获取消息邮件配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMessageClearRuleRequestBody</td>
                    <td>设置消息清理规则,支持修改记录数(1W-1000W)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMessageEmailConfig</td>
                    <td>删除消息邮件配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="19">用户管理</td>
                    <td>ListMfa</td>
                    <td>获取可用的认证方法</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserByDomain</td>
                    <td>最终租户修改子用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIamGroups</td>
                    <td>查询IAM用户组列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckTokenVerification</td>
                    <td>校验token是否可访问当前环境</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserSetting</td>
                    <td>查询用户设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateCode</td>
                    <td>预验证</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserSetting</td>
                    <td>更新用户设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUser</td>
                    <td>修改用户基本信息(邮箱,手机)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportUser</td>
                    <td>导入用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUserRole</td>
                    <td>更新用户角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIamGroupUsers</td>
                    <td>查询IAM用户组的用户列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCode</td>
                    <td>发送验证码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUser</td>
                    <td>获取用户列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUser</td>
                    <td>获取指定用户详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUser</td>
                    <td>删除用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangePassword</td>
                    <td>修改密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUser</td>
                    <td>创建用户</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInitPassword</td>
                    <td>新用户重置密码</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIamUsers</td>
                    <td>查询IAM用户列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">盘古药物分子大模型计费管理</td>
                    <td>ListDrugModelResource</td>
                    <td>查询盘古药物分子大模型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDrugModelResource</td>
                    <td>创建盘古药物分子大模型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDrugModelResource</td>
                    <td>退订盘古药物分子大模型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">空间管理</td>
                    <td>UpdateTopProject</td>
                    <td>置顶空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">空间统计接口</td>
                    <td>ListProjectStatistics</td>
                    <td>获取当前用户所属空间资源统计信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">系统配置内部接口</td>
                    <td>ListArchiveConfigs</td>
                    <td>获取跨域归档配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVendor</td>
                    <td>获取供应商配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEnv</td>
                    <td>获取系统配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateVendor</td>
                    <td>设置供应商配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateArchiveConfig</td>
                    <td>修改跨域归档设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">系统配额及资源使用情况获取</td>
                    <td>ListQuota</td>
                    <td>获取当前系统配额及资源使用情况</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">聚类分析作业管理</td>
                    <td>CreateClusteringJob</td>
                    <td>创建聚类分析作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowClusteringJob</td>
                    <td>查询聚类分析作业详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">自动作业管理</td>
                    <td>StartAutoJob</td>
                    <td>启动自动作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAutoJob</td>
                    <td>查询自动作业模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAutoJob</td>
                    <td>获取自动作业模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAutoJob</td>
                    <td>创建自动作业模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAutoJob</td>
                    <td>删除自动作业模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopAutoJob</td>
                    <td>停止自动作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutoJob</td>
                    <td>更新自动作业模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">自由能微扰作业管理</td>
                    <td>CreateFepJob</td>
                    <td>创建自由能微扰作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFepJob</td>
                    <td>查询自由能微扰作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">节点标签管理</td>
                    <td>ListPresetLabel</td>
                    <td>获取预置标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateNodeLabel</td>
                    <td>设置节点标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodeLabel</td>
                    <td>获取节点标签集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterAllNodeLabel</td>
                    <td>获取节点标签集</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">药物作业管理</td>
                    <td>DeleteDrugJob</td>
                    <td>删除药物作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterJob</td>
                    <td>创建分子聚类作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDrugJob</td>
                    <td>获取药物作业列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelDrugJob</td>
                    <td>取消药物作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserDrugJob</td>
                    <td>获取用户所属空间的药物作业列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDrugJob</td>
                    <td>更新药物作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">药物数据库管理</td>
                    <td>DeleteDrugDatabase</td>
                    <td>删除数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDrugDatabase</td>
                    <td>更新药物数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDrugDatabaseFile</td>
                    <td>数据库追加文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDrugDatabase</td>
                    <td>获取数据库列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDrugDatabase</td>
                    <td>创建数据库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">药物模型管理</td>
                    <td>ListDrugModel</td>
                    <td>获取模型列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBaseModel</td>
                    <td>获取基模型列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDrugModel</td>
                    <td>创建模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDrugModel</td>
                    <td>更新药物模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDrugModel</td>
                    <td>删除模型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">药物通用接口</td>
                    <td>GeneratePocketFile</td>
                    <td>根据center、size、padding参数生成可渲染的口袋文件内容</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GenerateSurfacePoints</td>
                    <td>根据表面离散点坐标集生成可渲染的文件内容</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMolDockingJob</td>
                    <td>单分子预对接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunFastaPreprocess</td>
                    <td>受体预处理(Fasta格式),用于前端计算预期扣费次数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMolBatchDownloadTask</td>
                    <td>创建分子或分子复合物批量下载任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunFormatConverter</td>
                    <td>单分子文件格式转换。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>GenerateComplexCombine</td>
                    <td>将传入的蛋白和小分子拼接成复合物结构</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMolBatchDownloadTask</td>
                    <td>查询分子或分子复合物批量下载任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">虚拟药物筛选</td>
                    <td>Show3dStructureContent</td>
                    <td>获取生成study作业3D结构的内容</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStudyJob</td>
                    <td>创建study作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStudy</td>
                    <td>创建study</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStudyJob</td>
                    <td>列举study所有作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStudy</td>
                    <td>删除study</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExtremumInfo</td>
                    <td>获取study作业的最值信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStudy</td>
                    <td>列举study</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">计算资源扩缩容</td>
                    <td>ListScalingHistory</td>
                    <td>获取策略伸缩历史</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartScaleOutPolicy</td>
                    <td>启动自动扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPolicyEvents</td>
                    <td>获取策略事件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScaleInPolicy</td>
                    <td>修改缩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateScaleOutPolicy</td>
                    <td>创建扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScaleInPolicy</td>
                    <td>查询缩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNodes</td>
                    <td>获取策略关联计算资源列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowScaleOutPolicy</td>
                    <td>获取扩容策略详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteScaleOutPolicy</td>
                    <td>删除扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateScaleOutPolicy</td>
                    <td>修改扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopScaleOutPolicy</td>
                    <td>停用自动扩容策略</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListScaleOutPolicy</td>
                    <td>查询扩容策略列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">计算资源管理内部接口</td>
                    <td>RebootNode</td>
                    <td>重启计算资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSchedule</td>
                    <td>修改计算资源调度信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComputingResourceFlavors</td>
                    <td>查询计算资源规格</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSchedule</td>
                    <td>查询计算资源调度信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteComputingResource</td>
                    <td>删除计算资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartNode</td>
                    <td>启动计算资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateComputingResource</td>
                    <td>购买计算资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLeftQuota</td>
                    <td>获取节点剩余配额</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComputingResources</td>
                    <td>查询计算资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEvsQuota</td>
                    <td>获取EVS配额及使用情况</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBmsDevices</td>
                    <td>查询bms计算资源显卡id列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopNode</td>
                    <td>关闭计算资源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">计算集群管理</td>
                    <td>DeleteComputingCluster</td>
                    <td>解绑计算集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListComputingCluster</td>
                    <td>获取计算集群列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateComputingCluster</td>
                    <td>绑定计算集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCceCluster</td>
                    <td>获取CCE集群列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusterInstallStep</td>
                    <td>查询指定集群安装步骤列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">资产收藏管理</td>
                    <td>ListStar</td>
                    <td>获取收藏资产列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteStar</td>
                    <td>取消收藏</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStar</td>
                    <td>收藏资产</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">资产管理</td>
                    <td>ListAsset</td>
                    <td>获取资产列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAssetVersion</td>
                    <td>删除资产指定版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetVersion</td>
                    <td>查询资产版本详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAssetVersion</td>
                    <td>更新资产指定版本的信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAsset</td>
                    <td>查询资产详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProperty</td>
                    <td>获取属性值列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteAssetAction</td>
                    <td>操作资产发布状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">资源监控数据获取</td>
                    <td>ShowResourceMetricData</td>
                    <td>获取资源监控数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDownloadResourceStatData</td>
                    <td>批量获取资源统计数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">镜像管理</td>
                    <td>ImportImage</td>
                    <td>导入镜像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDockerLogin</td>
                    <td>获取docker login指令</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUserImage</td>
                    <td>获取用户所属空间的镜像列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImageTag</td>
                    <td>获取指定镜像的tag列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteImage</td>
                    <td>删除镜像仓库</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishImage</td>
                    <td>发布镜像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateImage</td>
                    <td>更新镜像描述信息或者类型</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SubscribeImage</td>
                    <td>订阅镜像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateImage</td>
                    <td>创建镜像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTag</td>
                    <td>删除指定镜像tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListImage</td>
                    <td>获取镜像列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteTag</td>
                    <td>批量删除镜像tag</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">靶点优化作业管理</td>
                    <td>CreateTargetOptJob</td>
                    <td>创建靶点优化作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTargetOptJob</td>
                    <td>查询靶点优化作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">靶点口袋分子设计作业管理</td>
                    <td>ShowPocketMolDesignJob</td>
                    <td>查询靶点口袋分子设计作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePocketMolDesignJob</td>
                    <td>创建靶点口袋分子设计作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">靶点口袋发现作业管理</td>
                    <td>ShowPocketDetectionJob</td>
                    <td>查询靶点口袋发现作业详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePocketDetectionJob</td>
                    <td>创建靶点口袋发现作业</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">项目管理</td>
                    <td>BatchDeleteMember</td>
                    <td>批量删除项目成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>TransferProject</td>
                    <td>转移项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMember</td>
                    <td>移除项目成员</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadDataTrace</td>
                    <td>下载近一万条审计日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProject</td>
                    <td>获取项目详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectTrace</td>
                    <td>获取项目审计日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectTracker</td>
                    <td>获取项目审计日志追踪器</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMember</td>
                    <td>更新或者添加项目成员角色</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProject</td>
                    <td>更新项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProject</td>
                    <td>获取项目列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProjectTraceData</td>
                    <td>获取指定审计日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProjectTracker</td>
                    <td>更新项目审计日志追踪器配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProject</td>
                    <td>删除项目</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProject</td>
                    <td>创建项目</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>