# IoTDA MCP Server 

## 版本信息
v0.1.0

## 产品描述

IoTDA MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IoTDA交互的能力。可以基于自然语言对IoTDA资源进行全链路管理。

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
                    <td rowspan="1">AccessCodeManagement</td>
                    <td>CreateAccessCode</td>
                    <td>接入凭证是用于客户端使用AMQP等协议与平台建链的一个认证凭据。只保留一条记录,如果重复调用只会重置接入凭证,使得之前的失效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AmqpQueueManagement</td>
                    <td>AddQueue</td>
                    <td>应用服务器可调用此接口在物联网平台创建一个AMQP队列。每个租户只能创建100个队列,若超过规格,则创建失败,若队列名称与已有的队列名称相同,则创建失败。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteQueue</td>
                    <td>应用服务器可调用此接口在物联网平台上删除指定AMQP队列。若当前队列正在使用,则会删除失败。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQueue</td>
                    <td>应用服务器可调用此接口查询物联网平台中指定队列的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowQueue</td>
                    <td>应用服务器可调用此接口查询物联网平台中的AMQP队列信息列表。可通过队列名称作模糊查询,支持分页。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ApplicationManagement</td>
                    <td>AddApplication</td>
                    <td>资源空间对应的是物联网平台原有的应用,在物联网平台的含义与应用一致,只是变更了名称。应用服务器可以调用此接口创建资源空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApplication</td>
                    <td>资源空间对应的是物联网平台原有的应用,在物联网平台的含义与应用一致,只是变更了名称。应用服务器可以调用此接口查询指定资源空间详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApplication</td>
                    <td>应用服务器可以调用此接口更新资源空间的名称</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApplication</td>
                    <td>删除指定资源空间。删除资源空间属于高危操作,删除资源空间后,该空间下的产品、设备等资源将不可用,请谨慎操作!</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApplications</td>
                    <td>资源空间对应的是物联网平台原有的应用,在物联网平台的含义与应用一致,只是变更了名称。应用服务器可以调用此接口查询资源空间列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">AsyncCommandManagement</td>
                    <td>ListAsyncHistoryCommands</td>
                    <td>查询设备下发的历史异步命令,包含EXPIRED、SUCCESSFUL、FAILED、TIMEOUT、DELIVERED五种状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAsyncCommand</td>
                    <td>设备的产品模型中定义了物联网平台可向设备下发的命令,应用服务器可调用此接口向指定设备下发异步命令,以实现对设备的控制。平台负责将命令发送给设备,并将设备执行命令结果异步通知应用服务器。 命令执行结果支持灵活的数据流转,应用服务器通过调用物联网平台的创建规则触发条件(Resource:device.command.status,Event:update)、创建规则动作并激活规则后,当命令状态变更时,物联网平台会根据规则将结果发送到规则指定的服务器,如用户自定义的HTTP服务器,AMQP服务器,以及华为云的其他储存服务器等, 详情参考[设备命令状态变更通知](https://support.huaweicloud.com/api-iothub/iot_06_v5_01212.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountAsyncHistoryCommands</td>
                    <td>统计设备下的历史命令总数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAsyncCommands</td>
                    <td>查询设备下队列中的命令(处理中的命令),包含PENDING、SENT、DELIVERED三种状态,注意:DELIVERED状态的命令经过系统设定的一段时间(具体以系统配置为准)仍然没有更新,就会从队列中移除,变为历史命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAsyncDeviceCommand</td>
                    <td>物联网平台可查询指定id的命令。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">BacklogPolicyManagement</td>
                    <td>ListRoutingBacklogPolicy</td>
                    <td>应用服务器可调用此接口查询在物联网平台设置的数据流转积压策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRoutingBacklogPolicy</td>
                    <td>应用服务器可调用此接口在物联网平台修改指定数据流转积压策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRoutingBacklogPolicy</td>
                    <td>应用服务器可调用此接口在物联网平台删除指定数据流转积压策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRoutingBacklogPolicy</td>
                    <td>应用服务器可调用此接口在物联网平台创建数据流转积压策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRoutingBacklogPolicy</td>
                    <td>应用服务器可调用此接口在物联网平台查询指定数据流转积压策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">BatchTask</td>
                    <td>ListBatchTasks</td>
                    <td>应用服务器可调用此接口查询物联网平台中批量任务列表,每一个任务又包括具体的任务内容、任务状态、任务完成情况统计等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBatchTask</td>
                    <td>应用服务器可调用此接口为创建批量处理任务,对多个设备进行批量操作。当前支持批量软固件升级、批量创建设备、批量删除设备、批量冻结设备、批量解冻设备、批量创建命令、批量创建消息任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryBatchTask</td>
                    <td>应用服务器可调用此接口重试批量任务,目前只支持task_type为firmwareUpgrade,softwareUpgrade。如果task_id对应任务已经成功、停止、正在停止、等待中或初始化中,则不可以调用该接口。如果请求Body为{},则调用该接口后会重新执行所有状态为失败、失败待重试和已停止的子任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBatchTask</td>
                    <td>应用服务器可调用此接口删除物联网平台中已经完成(状态为成功,失败,部分成功,已停止)的批量任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowBatchTask</td>
                    <td>应用服务器可调用此接口查询物联网平台中指定批量任务的信息,包括任务内容、任务状态、任务完成情况统计以及子任务列表等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopBatchTask</td>
                    <td>应用服务器可调用此接口停止批量任务,目前只支持task_type为firmwareUpgrade,softwareUpgrade。如果task_id对应任务已经完成(成功、失败、部分成功,已经停止)或正在停止中,则不可以调用该接口。如果请求Body为{},则调用该接口后会停止所有正在执行中、等待中和失败待重试状态的子任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">BatchTaskFile</td>
                    <td>DeleteBatchTaskFile</td>
                    <td>应用服务器可调用此接口删除批量任务文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBatchTaskFiles</td>
                    <td>应用服务器可调用此接口查询批量任务文件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadBatchTaskFile</td>
                    <td>应用服务器可调用此接口上传批量任务文件,用于创建批量任务。当前支持批量创建设备任务、批量删除设备任务、批量冻结设备任务、批量解冻设备任务的文件上传。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">BridgeManagement</td>
                    <td>AddBridge</td>
                    <td>应用服务器可调用此接口在物联网平台创建一个网桥,仅在创建后的网桥才可以接入物联网平台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBridges</td>
                    <td>应用服务器可调用此接口在物联网平台查询网桥列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetBridgeSecret</td>
                    <td>应用服务器可调用此接口在物联网平台上重置网桥密钥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBridge</td>
                    <td>应用服务器可调用此接口在物联网平台上删除指定网桥。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">BroadcastManagement</td>
                    <td>BroadcastMessage</td>
                    <td>应用服务器可调用此接口向订阅了指定Topic的所有在线设备发布广播消息。应用将广播消息下发给平台后,平台会先返回应用响应结果,再将消息广播给设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">CertificateManagement</td>
                    <td>ListCertificates</td>
                    <td>应用服务器可调用此接口在物联网平台获取设备CA证书列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCertificate</td>
                    <td>应用服务器可调用此接口在物联网平台删除设备CA证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCertificate</td>
                    <td>应用服务器可调用此接口在物联网平台上传设备CA证书</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCertificate</td>
                    <td>应用服务器可调用此接口在物联网平台上更新CA证书。仅标准版实例、企业版实例支持该接口调用,基础版不支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckCertificate</td>
                    <td>应用服务器可调用此接口在物联网平台验证设备的CA证书,目的是为了验证用户持有设备CA证书的私钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">CommandManagement</td>
                    <td>CreateCommand</td>
                    <td>设备的产品模型中定义了物联网平台可向设备下发的命令,应用服务器可调用此接口向指定设备下发命令,以实现对设备的同步控制。平台负责将命令以同步方式发送给设备,并将设备执行命令结果同步返回, 如果设备没有响应,平台会返回给应用服务器超时,平台超时时间是20秒。如果命令下发需要超过20秒,建议采用[消息下发](https://support.huaweicloud.com/api-iothub/iot_06_v5_0059.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DeviceAuthorizer</td>
                    <td>UpdateDeviceAuthorizer</td>
                    <td>应用服务器可调用此接口在物联网平台更新指定id的自定义鉴权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceAuthorizer</td>
                    <td>应用服务器可调用此接口在物联网平台查询指定自定义鉴权ID的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeviceAuthorizer</td>
                    <td>应用服务器可调用此接口在物联网平台创建一个自定义鉴权。自定义鉴权是指用户可以通过函数服务自定义实现鉴权逻辑,以对接入平台的设备进行身份认证。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceAuthorizer</td>
                    <td>应用服务器可调用此接口在物联网平台上删除指定自定义鉴权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeviceAuthorizers</td>
                    <td>应用服务器可调用此接口在物联网平台查询自定义鉴权列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">DeviceGroup</td>
                    <td>CreateOrDeleteDeviceInGroup</td>
                    <td>应用服务器可调用此接口管理设备组中的设备。单个设备组内最多添加20,000个设备,一个设备最多可以被添加到10个设备组中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeviceGroups</td>
                    <td>应用服务器可调用此接口查询物联网平台中的设备组信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDeviceGroup</td>
                    <td>应用服务器可调用此接口新建设备组,一个华为云账号下最多可有1,000个设备组,包括父设备组和子设备组。设备组的最大层级关系不超过5层,即群组形成的关系树最大深度不超过5。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceGroup</td>
                    <td>应用服务器可调用此接口查询指定设备组详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceGroup</td>
                    <td>应用服务器可调用此接口删除指定设备组,如果该设备组存在子设备组或者该设备组中存在设备,必须先删除子设备组并将设备从该设备组移除,才能删除该设备组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceGroup</td>
                    <td>应用服务器可调用此接口修改物联网平台中指定设备组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDevicesInGroup</td>
                    <td>应用服务器可调用此接口查询指定设备组下的设备列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">DeviceManagement</td>
                    <td>ListDeviceGroupsByDevice</td>
                    <td>应用服务器可调用此接口查询物联网平台中的某个设备加入的设备组信息列表。仅标准版实例、企业版实例支持该接口调用,基础版不支持。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevice</td>
                    <td>应用服务器可调用此接口在物联网平台上删除指定设备。若设备下连接了非直连设备,则必须把设备下的非直连设备都删除后,才能删除该设备。该接口仅支持删除单个设备,如需批量删除设备,请参见 [创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnfreezeDevice</td>
                    <td>应用服务器可调用此接口解冻设备,解除冻结后,设备可以连接上线。该接口仅支持解冻单个设备,如需批量解冻设备,请参见 [创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeGateway</td>
                    <td>应用服务器可调用此接口在物联网平台修改子设备网关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchDevices</td>
                    <td>#### 接口说明</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDevice</td>
                    <td>应用服务器可调用此接口修改物联网平台中指定设备的基本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetDeviceSecret</td>
                    <td>应用服务器可调用此接口重置设备密钥,携带指定密钥时平台将设备密钥重置为指定的密钥,不携带密钥时平台将自动生成一个新的随机密钥返回。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDevice</td>
                    <td>应用服务器可调用此接口查询物联网平台中指定设备的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDevice</td>
                    <td>应用服务器可调用此接口在物联网平台创建一个设备,仅在创建后设备才可以接入物联网平台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevices</td>
                    <td>应用服务器可调用此接口查询物联网平台中的设备信息列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetFingerprint</td>
                    <td>应用服务器可调用此接口重置设备指纹。携带指定设备指纹时将之重置为指定值;不携带时将之置空,后续设备第一次接入时,该设备指纹的值将设置为第一次接入时的证书指纹。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>FreezeDevice</td>
                    <td>应用服务器可调用此接口冻结设备,设备冻结后不能再连接上线,可以通过解冻设备接口解除设备冻结。注意,当前仅支持冻结与平台直连的设备。该接口仅支持冻结单个设备,如需批量冻结设备,请参见 [创建批量任务](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DeviceProxy</td>
                    <td>ShowDeviceProxy</td>
                    <td>应用服务器可调用此接口查询物联网平台中指定设备代理的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeviceProxy</td>
                    <td>应用服务器可调用此接口在物联网平台创建一个动态设备代理规则,用于子设备自主选择网关设备上线和上报消息,即代理组下的任意网关下的子设备均可以通过代理组里其他设备上线([网关更新子设备状态](https://support.huaweicloud.com/api-iothub/iot_06_v5_3022.html) )然后进行数据上报([网关批量设备属性上报](https://support.huaweicloud.com/api-iothub/iot_06_v5_3006.html) )。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDeviceProxies</td>
                    <td>应用服务器可调用此接口查询物联网平台中的设备代理列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeviceProxy</td>
                    <td>应用服务器可调用此接口修改物联网平台中指定设备代理的基本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceProxy</td>
                    <td>应用服务器可调用此接口在物联网平台上删除指定设备代理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">DeviceShadow</td>
                    <td>UpdateDeviceShadowDesiredData</td>
                    <td>应用服务器可调用此接口配置设备影子的预期属性(desired区),当设备上线或者设备上报属性时把属性下发给设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceShadow</td>
                    <td>应用服务器可调用此接口查询指定设备的设备影子信息,包括对设备的期望属性信息(desired区)和设备最新上报的属性信息(reported区)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">FlowControlPolicyManagement</td>
                    <td>UpdateRoutingFlowControlPolicy</td>
                    <td>应用服务器可调用此接口在物联网平台修改指定数据流转流控策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRoutingFlowControlPolicy</td>
                    <td>应用服务器可调用此接口在物联网平台创建数据流转流控策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoutingFlowControlPolicy</td>
                    <td>应用服务器可调用此接口查询在物联网平台设置的数据流转流控策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRoutingFlowControlPolicy</td>
                    <td>应用服务器可调用此接口在物联网平台查询指定数据流转流控策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRoutingFlowControlPolicy</td>
                    <td>应用服务器可调用此接口在物联网平台删除指定数据流转流控策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">FunctionServiceManagement</td>
                    <td>AddFunctions</td>
                    <td>提供创建编解码函数的功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFunctions</td>
                    <td>提供查询编解码函数的功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFunctions</td>
                    <td>提供删除编解码函数的功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">MessageManagement</td>
                    <td>ListDeviceMessages</td>
                    <td>应用服务器可调用此接口查询平台下发给设备的消息,平台为每个设备默认最多保存20条消息,超过20条后, 后续的消息会替换下发最早的消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceMessage</td>
                    <td>应用服务器可调用此接口删除平台下发给设备的指定消息id的消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceMessage</td>
                    <td>应用服务器可调用此接口查询平台下发给设备的指定消息id的消息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMessage</td>
                    <td>物联网平台可向设备下发消息,应用服务器可调用此接口向指定设备下发消息,以实现对设备的控制。应用将消息下发给平台后,平台返回应用响应结果,平台再将消息发送给设备。平台返回应用响应结果不一定是设备接收结果,建议用户应用通过订阅[设备消息状态变更通知](https://support.huaweicloud.com/api-iothub/iot_06_v5_01203.html),订阅后平台会将设备接收结果推送给订阅的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">OtaPackageManagement</td>
                    <td>ShowOtaPackage</td>
                    <td>用户可调用此接口查询关联OBS对象的升级包详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOtaPackage</td>
                    <td>用户可调用此接口创建升级包关联OBS对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOtaPackage</td>
                    <td>用户可调用此接口删除关联OBS对象的升级包信息,不会删除OBS上对象</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOtaPackageInfo</td>
                    <td>用户可调用此接口查询关联OBS对象的升级包列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">PolicyManagement</td>
                    <td>ShowDevicePolicy</td>
                    <td>应用服务器可调用此接口在物联网平台查询指定策略ID的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BindDevicePolicy</td>
                    <td>应用服务器可调用此接口在物联网平台上为批量设备绑定目标策略,目前支持绑定目标类型为:设备、产品,当目标类型为产品时,该产品下所有设备都会生效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDevicePolicy</td>
                    <td>应用服务器可调用此接口在物联网平台创建一个策略,该策略需要绑定到设备和产品下才能生效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDevicePolicies</td>
                    <td>应用服务器可调用此接口在物联网平台查询策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnbindDevicePolicy</td>
                    <td>应用服务器可调用此接口在物联网平台上解除指定策略下绑定的目标对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDevicePolicy</td>
                    <td>应用服务器可调用此接口在物联网平台更新策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTargetsInDevicePolicy</td>
                    <td>应用服务器可调用此接口在物联网平台上查询指定策略ID下绑定的目标列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDevicePolicy</td>
                    <td>应用服务器可调用此接口在物联网平台上删除指定策略,注意:删除策略同时会解绑该策略下所有绑定对象。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ProductManagement</td>
                    <td>CreateProduct</td>
                    <td>应用服务器可调用此接口创建产品。此接口仅创建了产品,没有创建和安装插件,如果需要对数据进行编解码,还需要在平台开发和安装插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListProducts</td>
                    <td>应用服务器可调用此接口查询已导入物联网平台的产品模型信息列表,了解产品模型的概要信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProduct</td>
                    <td>应用服务器可调用此接口删除已导入物联网平台的指定产品模型。此接口仅删除了产品,未删除关联的插件,在产品下存在设备时,该产品不允许删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProduct</td>
                    <td>应用服务器可调用此接口修改已导入物联网平台的指定产品模型,包括产品模型的服务、属性、命令等。此接口仅修改了产品,未修改和安装插件,如果修改了产品中的service定义,且在平台中有对应的插件,请修改并重新安装插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProduct</td>
                    <td>应用服务器可调用此接口查询已导入物联网平台的指定产品模型详细信息,包括产品模型的服务、属性、命令等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">PropertiesManagement</td>
                    <td>ListProperties</td>
                    <td>设备的产品模型中定义了物联网平台可向设备下发的属性,应用服务器可调用此接口向设备发送指令用以查询设备的实时属性, 并由设备将属性查询的结果同步返回给应用服务器。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProperties</td>
                    <td>设备的产品模型中定义了物联网平台可向设备下发的属性,应用服务器可调用此接口向指定设备下发属性。平台负责将属性以同步方式发送给设备,并将设备执行属性结果同步返回。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">ProvisioningTemplateManagement</td>
                    <td>ListProvisioningTemplates</td>
                    <td>应用服务器可调用此接口在物联网平台查询预调配模板列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProvisioningTemplate</td>
                    <td>应用服务器可调用此接口在物联网平台上删除指定预调配模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProvisioningTemplate</td>
                    <td>应用服务器可调用此接口在物联网平台更新指定id的预调配模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProvisioningTemplate</td>
                    <td>应用服务器可调用此接口在物联网平台创建一个预调配模板。用户的设备未在平台注册时,可以通过预调配模板在设备首次接入物联网平台时将设备信息自动注册到物联网平台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProvisioningTemplate</td>
                    <td>应用服务器可调用此接口在物联网平台查询指定预调配模板ID的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">RoutingRuleManagement</td>
                    <td>UpdateRoutingRule</td>
                    <td>应用服务器可调用此接口修改物联网平台中指定规则条件的配置参数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRoutingRule</td>
                    <td>应用服务器可调用此接口查询物联网平台中指定规则条件的配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRuleAction</td>
                    <td>应用服务器可调用此接口删除物联网平台中的指定规则动作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRoutingRule</td>
                    <td>应用服务器可调用此接口在物联网平台创建一条规则触发条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRuleAction</td>
                    <td>应用服务器可调用此接口在物联网平台创建一条规则动作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRuleAction</td>
                    <td>应用服务器可调用此接口修改物联网平台中指定规则动作的配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRuleAction</td>
                    <td>应用服务器可调用此接口查询物联网平台中指定规则动作的配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRoutingRules</td>
                    <td>应用服务器可调用此接口查询物联网平台中设置的规则条件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRoutingRule</td>
                    <td>应用服务器可调用此接口删除物联网平台中的指定规则条件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRuleActions</td>
                    <td>应用服务器可调用此接口查询物联网平台中设置的规则动作列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">RuleManagement</td>
                    <td>ShowRule</td>
                    <td>应用服务器可调用此接口查询物联网平台中指定规则的配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRules</td>
                    <td>应用服务器可调用此接口查询物联网平台中设置的规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRule</td>
                    <td>应用服务器可调用此接口在物联网平台创建一条规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRule</td>
                    <td>应用服务器可调用此接口修改物联网平台中指定规则的配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRule</td>
                    <td>应用服务器可调用此接口删除物联网平台中的指定规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeRuleStatus</td>
                    <td>应用服务器可调用此接口修改物联网平台中指定规则的状态,激活或者去激活规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TagManagement</td>
                    <td>TagDevice</td>
                    <td>应用服务器可调用此接口为指定资源绑定标签。当前支持标签的资源有Device(设备)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourcesByTags</td>
                    <td>应用服务器可调用此接口查询绑定了指定标签的资源。当前支持标签的资源有Device(设备)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UntagDevice</td>
                    <td>应用服务器可调用此接口为指定资源解绑标签。当前支持标签的资源有Device(设备)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">TunnelManagement</td>
                    <td>ListDeviceTunnels</td>
                    <td>用户可通过该接口查询某项目下的所有设备隧道,以实现对设备管理。应用服务器可通过此接口向平台查询设备隧道建立的情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTunnel</td>
                    <td>用户可以通过该接口创建隧道(WebSocket协议),应用服务器和设备可以通过该隧道进行数据传输。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceTunnel</td>
                    <td>用户可通过该接口查询某项目中的某个设备隧道,查看该设备隧道的信息与连接情况。应用服务器可调用此接口向平台查询设备隧道建立情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CloseDeviceTunnel</td>
                    <td>应用服务器可通过该接口关闭某个设备隧道。关闭后可以再次连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeviceTunnel</td>
                    <td>用户可通过该接口删除某个设备隧道。删除后该通道不存在,无法再次连接。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>