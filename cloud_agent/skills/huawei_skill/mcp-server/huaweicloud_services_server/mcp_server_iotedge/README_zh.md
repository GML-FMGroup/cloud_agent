# IoTEdge MCP Server 

## 版本信息
v0.1.0

## 产品描述

IoTEdge MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IoTEdge交互的能力。可以基于自然语言对IoTEdge资源进行全链路管理。

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
                    <td rowspan="4">App</td>
                    <td>ShowApp</td>
                    <td>应用服务器可调用此接口查询物联网平台中指定批量任务的信息,包括任务内容、任务状态、任务完成情况统计以及子任务列表等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>应用服务器可调用此接口删除应用模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApps</td>
                    <td>应用服务器可调用此接口查询应用模板列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApp</td>
                    <td>应用服务器可调用此接口为创建批量处理任务,对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结、批量解冻、批量下发同步命令、批量下发异步命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">AppInstance</td>
                    <td>DeleteAppInstance</td>
                    <td>应用服务器可调用此接口为删除应用实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppInstanceHistory</td>
                    <td>应用服务器可调用此接口查询应用实例的历史版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppInstances</td>
                    <td>应用服务器可调用此接口查询应用实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppInstance</td>
                    <td>应用服务器可调用此接口为创建应用实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAppInstance</td>
                    <td>应用服务器可调用此接口为更新应用实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">AppVersion</td>
                    <td>ListAppImage</td>
                    <td>应用服务器可调用此接口查询应用版本包含的镜像列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppVersion</td>
                    <td>应用服务器可调用此接口为创建应用版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAppVersions</td>
                    <td>应用服务器可调用此接口查询应用版本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppVersion</td>
                    <td>应用服务器可调用此接口查询应用版本详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppVersion</td>
                    <td>应用服务器可调用此接口删除应用版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DownloadAppVersion</td>
                    <td>应用服务器可调用此接口下载应用版本Chart包。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">BasicNode</td>
                    <td>CreateEdgeNode</td>
                    <td>创建边缘节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeNode</td>
                    <td>删除指定边缘节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeNode</td>
                    <td>查询边缘节点详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeNodeHostsInfo</td>
                    <td>查询边缘节点下的主机详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstallCmd</td>
                    <td>生成边缘节点安装命令,命令有效时间30分钟,超过后需要重新生成</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeNode</td>
                    <td>修改边缘节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListEdgeNodes</td>
                    <td>查询边缘节点列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">Cluster</td>
                    <td>DeleteCluster</td>
                    <td>应用服务器可调用此接口删除边缘集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateClusterInstallCmd</td>
                    <td>应用服务器可调用此接口生成边缘集群安装命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListClusters</td>
                    <td>应用服务器可调用此接口查询边缘集群列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateCluster</td>
                    <td>应用服务器可调用此接口为创建边缘集群。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCluster</td>
                    <td>应用服务器可调用此接口查询边缘集群详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DeviceControls</td>
                    <td>ExecuteDeviceControlsSet</td>
                    <td>设备控制设置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDeviceControlDefaultValues</td>
                    <td>设备控制默认值</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPropertyActiveControls</td>
                    <td>获取属性执行中的控制</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteDeviceControlsRelease</td>
                    <td>设备控制释放</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DeviceManager</td>
                    <td>ListDevices</td>
                    <td>查询设备列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDevice</td>
                    <td>添加设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDevice</td>
                    <td>修改设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevice</td>
                    <td>删除设备</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProductConfig</td>
                    <td>获取协议配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">EdgeAppConfigsTemplateManagement</td>
                    <td>BatchListAppConfigsTemplates</td>
                    <td>查询应用配置模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppConfigsTemplate</td>
                    <td>查询应用配置模板详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAppConfigsTemplates</td>
                    <td>添加应用配置模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppConfigsTemplate</td>
                    <td>删除应用配置模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddGeneralAppConfigsTemplate</td>
                    <td>导入标准应用配置模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">EdgeAppManagement</td>
                    <td>ShowEdgeApp</td>
                    <td>查询应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListEdgeApps</td>
                    <td>查询应用列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeApp</td>
                    <td>删除应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeApp</td>
                    <td>创建应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">EdgeAppVersionManagement</td>
                    <td>UpdateEdgeApplicationVersionState</td>
                    <td>更新应用版本状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEdgeApplicationVersion</td>
                    <td>创建应用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateEdgeApplicationVersion</td>
                    <td>修改应用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEdgeApplicationVersion</td>
                    <td>查询应用版本详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListEdgeAppVersions</td>
                    <td>查询应用版本列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEdgeApplicationVersion</td>
                    <td>删除应用版本</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">EdgeDcDsManagement</td>
                    <td>CreateDs</td>
                    <td>用户通过Console接口在指定边缘节点上创建数据源配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDcDs</td>
                    <td>修改数据源配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SynchronizeDcConfigs</td>
                    <td>下发数采配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDcDs</td>
                    <td>查询数据源配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDcDs</td>
                    <td>删除数据源配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListDcDs</td>
                    <td>查询数据源配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">EdgeDcPointManagement</td>
                    <td>BatchListDcDevices</td>
                    <td>查询数采连接下子设备列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDcPoint</td>
                    <td>删除点位表配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDcPoint</td>
                    <td>查询点位表配置详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDcPoint</td>
                    <td>修改点位表配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListDcPoints</td>
                    <td>查询点位表配置列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDcPoints</td>
                    <td>批量删除点位表配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDcPoint</td>
                    <td>用户通过Console接口在指定边缘节点上点位表配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">EdgeExternals</td>
                    <td>DeleteExternalEntity</td>
                    <td>删除节点下外部实体</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateExternalEntity</td>
                    <td>用户通过在指定边缘节点上设置外部实体的接入信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExternalEntity</td>
                    <td>用户在指定边缘节点上查询外部实体列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateExternalEntity</td>
                    <td>用户通过在指定边缘节点上修改指定外部实体的接入信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">EdgeModuleManagement</td>
                    <td>CreateModule</td>
                    <td>用户通过Console接口在指定边缘节点上创建边缘模块</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListModules</td>
                    <td>用户通过Console接口查询指定边缘节点上边缘模块列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateModule</td>
                    <td>用户通过Console接口查询指定边缘节点上指定边缘模块</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateModuleState</td>
                    <td>用户通过Console接口启停数采连接</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteModule</td>
                    <td>用户通过过Console接口在指定边缘节点上删除边缘模块</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InvokeModuleMsg</td>
                    <td>iotedge通过该接口透明代理用户到模块的请求</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowModule</td>
                    <td>用户通过Console接口查询指定边缘节点上指定边缘模块</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">EdgeModuleShadow</td>
                    <td>UpdateModuleShadow</td>
                    <td>更新模块影子信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowModuleShadow</td>
                    <td>获取模块影子信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">EdgeNodeRouteService</td>
                    <td>UpdateRoutes</td>
                    <td>用户通过在指定边缘节点上设置边缘路由</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoutes</td>
                    <td>用户在指定边缘节点上查询边缘路由列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">EdgeOtTemplateManagement</td>
                    <td>AddOtTemplates</td>
                    <td>添加数采模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOtTemplate</td>
                    <td>查询数采模板详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOtTemplate</td>
                    <td>删除数采模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddGeneralOtTemplate</td>
                    <td>导入标准数采模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchListOtTemplates</td>
                    <td>查询数采模板列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">EdgePointTemplatesManagement</td>
                    <td>ShowPointTemplate</td>
                    <td>查询点位表模板文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ImportPoints</td>
                    <td>用户通过Console接口在指定边缘节点上点位表配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPoints</td>
                    <td>查询点位表模板文件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">EdgeScheduleManagement</td>
                    <td>DeleteSchedule</td>
                    <td>用户通过北向接口删除边缘节点上调度计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSchedule</td>
                    <td>用户通过北向接口修改边缘节点上调度计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSchedule</td>
                    <td>用户通过北向接口在指定边缘节点上创建调度计划</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">HttpRequestProxy</td>
                    <td>InvokePatchProxy</td>
                    <td>北向NA调用南向第三方应用的PATCH方法时使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InvokePutProxy</td>
                    <td>北向NA调用南向第三方应用的PUT方法时使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InvokeDeleteProxy</td>
                    <td>北向NA调用南向第三方应用的DELETE方法时使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InvokeGetProxy</td>
                    <td>北向NA调用南向第三方应用的GET方法时使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InvokePostProxy</td>
                    <td>北向NA调用南向第三方应用的POST方法时使用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">IaConfigManagement</td>
                    <td>UpdateIaConfig</td>
                    <td>创建&amp;更新南向3rdIA配置项信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchImportConfigs</td>
                    <td>批量导入南向3rdIA配置项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIaConfigs</td>
                    <td>查询南向3rdIA配置项列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchConfirmConfigsNew</td>
                    <td>南向3rdIA对下发的配置项进行批量确认</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteIaConfig</td>
                    <td>删除南向3rdIA配置项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowIaConfig</td>
                    <td>查询南向3rdIA配置项详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">NaManagement</td>
                    <td>DeleteNa</td>
                    <td>删除北向NA信息,如果有边缘节点已分配该NA信息,会通知到该边缘节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNaAuthorizedNodes</td>
                    <td>查询该北向NA信息的已分配节点</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNa</td>
                    <td>创建&amp;更新北向NA信息,当更新北向NA信息时,会通知到已分配该北向NA的所有边缘节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchAssociateNaToNodes</td>
                    <td>批量授权北向NA信息到边缘节点。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNas</td>
                    <td>查询北向NA信息列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNa</td>
                    <td>查询北向NA信息详情</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>