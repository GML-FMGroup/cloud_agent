# KooMap MCP Server 

## 版本信息
v0.1.0

## 产品描述

KooMap MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务KooMap交互的能力。可以基于自然语言对KooMap资源进行全链路管理。

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
                    <td rowspan="8">卫星影像任务管理</td>
                    <td>ShowTaskOverview</td>
                    <td>查看工作共享空间下的任务概览,包括全部任务数量以及成功、执行中、失败、已归档状态的任务数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>用于任务的删除。只有失败、未运行、停止成功状态的任务可以删除,删除成功后任务不在任务列表中显示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>在工作共享空间内新建数据处理任务,新建任务的“成果影像名称”参数可从“校验原始影像文件”接口中获取。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTaskArchivedStatus</td>
                    <td>任务的归档和取消归档操作,归档成功之后的任务不会在任务列表显示。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopTask</td>
                    <td>停止任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateImage</td>
                    <td>校验原始影像文件是否满足匹配规则(全色与多光谱一一对应或全为多光谱)并返回成果影像名称。如果不满足匹配规则,会以报错方式提示用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTaskInfo</td>
                    <td>根据设置的过滤条件(任务状态)分页查询任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartTask</td>
                    <td>启动任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">卫星影像数据管理</td>
                    <td>ListImageBaseInfo</td>
                    <td>根据过滤条件查询卫星影像信息列表。过滤条件有:影像名称、上传日期、影像别名、影像等级、影像状态、是否为成果数据、分页偏移量、每页显示条数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">卫星影像用量统计</td>
                    <td>ListUsageInfo</td>
                    <td>您可以查询时空专属存储服务或卫星影像生产服务的用量统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">实景三维任务管理</td>
                    <td>UpdateReal3DTask</td>
                    <td>该接口用于更新任务信息,包括名称、类型、描述、建模影像ID、建模参数以及建模坐标系。任务更新成功后状态更新为初始化(INIT)。仅支持更新非运行状态且未完成的任务:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateReal3DTask</td>
                    <td>创建实景三维建模任务时,必须绑定工作共享空间。每个工作共享空间内可绑定的任务上限为500个,任务名称需唯一,不能重复(大小写不敏感)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopReal3DTask</td>
                    <td>可停止任务状态为等待中(PENDING)、启动中(STARTING)或者运行中(RUNNING)的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTaskOverviewInWorkspace</td>
                    <td>该接口用于展示工作共享空间内任务的概览信息。包含:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartReal3DTask</td>
                    <td>该接口用于启动任务。该接口运行成功后,任务状态更新为等待中(PENDING),此时任务添加到启动队列中等待运行资源就绪。资源就绪后任务状态更新为启动中(STARTING),启动成功后任务状态更新为运行中(RUNNING),若启动失败则任务状态更新为启动失败(START_FAILED)。当建模任务类型为有控建模时,为了提升刺点效率需要先对影像进行空三建模。执行空三建模需要设置请求体的“run_AT_only”为“true”,空三建模成功后,任务状态更新为空三建模成功(BUNDLE_SUCCESS)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTasksInWorkspace</td>
                    <td>对单个工作共享空间内的任务进行分页查询,支持过滤条件:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReal3DTask</td>
                    <td>该接口用于删除状态为初始化(INIT)、启动失败(START_FAILED)、运行失败(FAILED)、已停止(STOP_SUCCESS)或运行成功(SUCCESS)的任务。注意:删除任务不影响已完成建模的三维成果影像数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateReal3DTaskArchivedStatus</td>
                    <td>该接口用于归档运行成功的任务或取消任务的归档状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">实景三维刺点管理</td>
                    <td>DeleteSpurPoint</td>
                    <td>根据刺点ID,删除图片上的刺点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSpurPoints</td>
                    <td>获取单张图片里的所有刺点信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSpurCount</td>
                    <td>根据像控点信息,查询该像控点在图片上已刺点数量,数量等同于已刺点图片的张数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddSpurPoint</td>
                    <td>用户选择生产资料列表中的像控点信息,并在图片中标记出来的过程叫做刺点。该接口用来在图片上新增刺点,刺点的具体信息包括:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMarkerInfo</td>
                    <td>根据当前任务中的所有图片的刺点信息,生成算法运行时需要的刺点文件。注意:该接口调用需要传递空请求体“{}”。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">实景三维数据管理</td>
                    <td>ListReal3DRefineProducts</td>
                    <td>查询实景三维精修后处理成果的数据列表。支持的过滤参数:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFolder</td>
                    <td>根据过滤条件查询当前租户的倾斜影像基本信息列表。过滤条件有:影像名称、影像别名、影像上传起止时间、影像状态、影像描述、分页偏移量、每页显示条数,影像排序规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReal3DProduct</td>
                    <td>删除实景三维成果影像。仅当成果影像状态为“available”时才可以删除。该接口执行后,成果影像状态更新为“deleting”。在完成删除后成果影像将被删除,且数据不可恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteReal3DRefineProduct</td>
                    <td>调用该接口可删除实景三维精修后处理成果数据。当前仅支持成果数据状态为“available”时才可以删除。执行该接口后,成果数据状态更新为“deleting”。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReal3DProducts</td>
                    <td>查询实景三维成果影像列表。返回成果影像查询结果以更新时间倒序排列,支持根据以下条件查询:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">实景三维用量统计</td>
                    <td>ShowReal3DUsage</td>
                    <td>您可以查询实景三维生产服务时空专属存储或影像建模的用量统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">实景三维精修后处理任务管理</td>
                    <td>DeleteReal3DSubTask</td>
                    <td>该接口可用于删除状态为初始化(INIT)、上传成功(UPLOAD_SUCCESS)、上传失败(UPLOAD_FAILED)、启动失败(START_FAILED)、运行成功(SUCCESS)、运行失败(FAILED)或已停止(STOP_SUCCESS)的精修后处理任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListReal3DSubTasks</td>
                    <td>对单个实景三维建模任务内的精修后处理任务进行分页查询,支持过滤条件:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartReal3DSubTask</td>
                    <td>该接口用于启动精修后处理任务。该接口运行成功后,任务状态更新为等待中(PENDING),此时任务添加到启动队列中等待运行资源就绪,资源就绪后状态更新为启动中(STARTING),启动成功后状态更新为运行中(RUNNING),若启动失败则状态更新为启动失败(START_FAILED)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopReal3DSubTask</td>
                    <td>该接口用于停止状态为等待中(PENDING)、启动中(STARTING)或者运行中(RUNNING)的精修后处理任务。任务停止后,状态更新规则如下:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateReal3DSubTask</td>
                    <td>每个精修后处理任务必须绑定一个已完成的建模类型为“显式辐射场”的任务,且单个任务允许创建的精修后处理任务上限为10个、名称不能重复(大小写不敏感)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">工作共享空间</td>
                    <td>CreateCommonWorkspace</td>
                    <td>该接口支持创建工作共享空间,便于对任务进行分类管理。一个租户创建的工作共享空间上限为500个,工作共享空间名称不能重复(大小写不敏感)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCommonWorkspace</td>
                    <td>该接口用于删除一个工作共享空间。在删除之前,必须保证空间未被置顶且空间内没有任务,否则会删除失败。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCommonWorkspace</td>
                    <td>该接口用于工作共享空间信息的更新。可以更新的内容包括:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCommonWorkspace</td>
                    <td>该接口用于分页查询工作共享空间列表,支持过滤条件:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">空间定位</td>
                    <td>StartVps</td>
                    <td>视觉定位是根据图像耦合GPS数据确定设备的位置的一项技术。首先通过拍摄一系列具有已知位置的图像并分析它们的关键视觉特征(例如建筑物或桥梁的轮廓)来创建地图,以创建这些视觉特征的大规模且可快速搜索的索引。将设备图像中的特征与索引中的特征进行比较,可获得目标设备的位姿。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">空间导航</td>
                    <td>StartNavi</td>
                    <td>AR导航是新型的地图导航方法,基于摄像头实时捕捉的实景画面,将地图导航信息通过数字内容的形态叠加在实景画面中,生成虚拟的3D导航指引。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>