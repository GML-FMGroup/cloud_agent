# IoTDM MCP Server 

## 版本信息
v0.1.0

## 产品描述

IoTDM MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务IoTDM交互的能力。可以基于自然语言对IoTDM资源进行全链路管理。

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
                    <td rowspan="9">InstanceManagement</td>
                    <td>UnbindInstanceTags</td>
                    <td>删除实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ChangeInstanceChargeMode</td>
                    <td>修改设备接入实例的计费模式,支持将按需计费模式修改为包年/包月计费模式。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>用户可以调用此接口创建一个设备接入实例。支持的实例规格请参见[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeInstance</td>
                    <td>修改设备接入实例的规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>用户可以调用此接口查询设备接入实例列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询设备接入实例详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BindInstanceTags</td>
                    <td>添加实例标签。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstance</td>
                    <td>修改设备接入实例信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除设备接入实例。约束:此接口仅支持删除按需计费的实例。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>