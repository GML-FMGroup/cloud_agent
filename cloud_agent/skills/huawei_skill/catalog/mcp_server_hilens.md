# HiLens MCP Server 

## 版本信息
v0.1.0

## 产品描述

HiLens MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务HiLens交互的能力。可以基于自然语言对HiLens资源进行全链路管理。

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
                    <td rowspan="5">作业管理</td>
                    <td>ShowTask</td>
                    <td>通过作业ID查询作业详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTask</td>
                    <td>删除作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateTask</td>
                    <td>编辑作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTasks</td>
                    <td>查询当前部署下所有作业,返回详情列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTask</td>
                    <td>创建作业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">固件管理</td>
                    <td>ListFirmwares</td>
                    <td>查看指定固件历史版本信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">密钥管理</td>
                    <td>DeleteSecret</td>
                    <td>删除密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSecret</td>
                    <td>查询密钥详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSecret</td>
                    <td>创建密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSecrets</td>
                    <td>专业版HiLens控制台密钥管理,根据用户请求条件筛选,查询用户创建的 密钥信息,以列表形式返回。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSecret</td>
                    <td>更新密钥</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">工作空间管理</td>
                    <td>DeleteWorkSpace</td>
                    <td>删除指定ID的工作空间,如果该工作空间下仍有资源,则删除会失败</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWorkSpace</td>
                    <td>创建一个工作空间,其中工作空间名不能与已有的重复</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWorkSpace</td>
                    <td>获取指定workspace_id的工作空间详情,包括创建时间,描述,创建者等信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWorkSpace</td>
                    <td>更改工作空间信息,暂时只能更改描述</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWorkSpaces</td>
                    <td>查询用户名下的所有工作空间信息,并返回列表和总条目数</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">应用部署管理</td>
                    <td>ShowDeployments</td>
                    <td>获取部署列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeployment</td>
                    <td>更新应用部署相关信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartAndStopDeploymentPod</td>
                    <td>启动/停止部署下的指定实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePod</td>
                    <td>删除指定实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeployment</td>
                    <td>获取部署的详情信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDeploymentNodes</td>
                    <td>通过指定设备id列表或者设备标签将应用部署下发到多个设备上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeploymentPods</td>
                    <td>获取用户实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDeployment</td>
                    <td>创建应用部署。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartAndStopDeployment</td>
                    <td>启动/暂停应用部署。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDeployment</td>
                    <td>删除指定应用部署。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDeploymentUsingPatch</td>
                    <td>更新应用部署部分信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">技能市场</td>
                    <td>ShowSkillOrderInfo</td>
                    <td>获取订单详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOrderForm</td>
                    <td>创建免费技能订单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSkillList</td>
                    <td>获取技能列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSkillOrderList</td>
                    <td>获取订单列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetDefaultOrderForm</td>
                    <td>设置默认订单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSkillInfo</td>
                    <td>获取技能详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">标签管理</td>
                    <td>CreateResourceTags</td>
                    <td>专业版HiLens控制台标签管理,添加对应资源的标签列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResourceTag</td>
                    <td>专业版HiLens控制台标签管理,删除对应资源的标签</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceTags</td>
                    <td>专业版HiLens控制台标签管理,查询具体资源的标签,返回标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListResourceTags</td>
                    <td>专业版HiLens控制台标签管理,查询某种资源类型的所有标签,返回标签列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateNodeTags</td>
                    <td>专业版HiLens控制台标签管理,用户选择多个设备,批量添加多个标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">设备告警管理</td>
                    <td>ListDeviceAlarms</td>
                    <td>获取设备告警列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">设备管理</td>
                    <td>UpdateNodeCert</td>
                    <td>设备出现离线或者证书过期时,可通过该接口更新证书,重新让设备连接到云端</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnfreezeNode</td>
                    <td>使用运行服务费激活设备。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNode</td>
                    <td>填写设备信息,将设备注册到HiLens专业版控制台上。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>FreezeNode</td>
                    <td>将激活订单与设备解绑。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpgradeProgress</td>
                    <td>获取设备固件升级进度。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodes</td>
                    <td>专业版HiLens控制台设备管理,根据用户请求条件筛选,查询用户注册的设备信息,以列表形式返回。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlatformManager</td>
                    <td>获取平台管理费列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNode</td>
                    <td>更新设备日志配置,标签以及描述。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNodeFirmware</td>
                    <td>升级设备固件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNode</td>
                    <td>支持查询HiLens专业版控制台上的设备详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowNodeActivationRecords</td>
                    <td>获取激活记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteNode</td>
                    <td>删除专业版HiLens控制台上的设备,并与端侧的设备进行解绑。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchNodeConnection</td>
                    <td>该API用于启用停用设备。被停用的设备将无法连接到云端服务,重新启用设备恢复连接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">设备管理v1</td>
                    <td>ListDevices</td>
                    <td>获取基础版设备列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">配置项管理</td>
                    <td>CreateConfigMap</td>
                    <td>创建配置项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteConfigMap</td>
                    <td>根据配置项id删除某个配置项</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateConfigMap</td>
                    <td>根据配置项id更新配置项信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfigMap</td>
                    <td>根据配置项id查询某个配置项详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListConfigMaps</td>
                    <td>获取配置项详情,以列表形式返回。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>