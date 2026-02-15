# IoTDA MCP Server

## Version Information
v0.1.0

## Product Description

The IoTDA MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud IoTDA. It enables full-link management of IoTDA resources based on natural language processing.

## Available Tools
Cover the entire API, available as needed. The list and status are as follows:

<html>
<head></head>
<body>
<table border="1" cellspacing="0" cellpadding="5">
<tbody>
<tr>
<th>Category</th>
<th>Tool Name</th>
<th>Function Description</th>
<th>Status</th>
</tr>
<tr>
<td rowspan="1">AccessCodeManagement</td>
<td>CreateAccessCode</td>
<td>An access code is an authentication credential used by the client to establish a connection with the platform using protocols such as AMQP. Only one record is retained; repeated calls will only reset the access code, rendering the previous one invalid. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">AmqpQueueManagement</td>
<td>AddQueue</td>
<td>The application server can call this API to create an AMQP queue on the IoT platform. Each tenant can only create 100 queues. If the limit is exceeded, creation will fail. If the queue name is the same as an existing queue, creation will fail. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteQueue</td>
<td>The application server can call this API to delete a specified AMQP queue on the IoT platform. If the queue is currently in use, deletion will fail. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowQueue</td>
<td>The application server can call this API to query detailed information about a specified queue on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchShowQueue</td>
<td>Application servers can call this API to query the AMQP queue list on the IoT platform. Fuzzy queries can be performed by queue name, and paging is supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">ApplicationManagement</td>
<td>AddApplication</td>
<td>Resource spaces correspond to existing applications on the IoT platform. Their meaning on the IoT platform is the same as that of applications, only the name has been changed. Application servers can call this API to create resource spaces. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApplication</td>
<td>Resource spaces correspond to existing applications on the IoT platform. Their meaning on the IoT platform is the same as that of applications, only the name has been changed. Application servers can call this interface to query the details of a specified resource space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateApplication</td>
<td>Application servers can call this interface to update the name of a resource space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApplication</td>
<td>Delete a specified resource space. Deleting a resource space is a high-risk operation. After deleting a resource space, products, devices, and other resources in that space will become unavailable. Please proceed with caution! </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApplications</td>
<td>Resource spaces correspond to existing applications on the IoT platform. Their meaning on the IoT platform is the same as applications, only the name has been changed. Application servers can call this interface to query the list of resource spaces. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">AsyncCommandManagement</td>
<td>ListAsyncHistoryCommands</td>
<td>Query the history of asynchronous commands issued by the device, including five states: EXPIRED, SUCCESSFUL, FAILED, TIMEOUT, and DELIVERED. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAsyncCommand</td>
<td>The device's product model defines the commands that the IoT platform can issue to the device. The application server can call this interface to issue asynchronous commands to a specified device to control it. The platform is responsible for sending commands to the device and asynchronously notifying the application server of the device's command execution results. Command execution results support flexible data flow. After the application server calls the IoT platform to create a rule trigger condition (Resource: device.command.status, Event: update), creates a rule action, and activates the rule, when the command status changes, the IoT platform sends the result to the rule-specified server, such as a user-defined HTTP server, AMQP server, or other Huawei Cloud storage servers. For details, see [Device Command Status Change Notification](https://support.huaweicloud.com/api-iothub/iot_06_v5_01212.html). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountAsyncHistoryCommands</td>
<td>Counts the total number of historical commands on the device. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAsyncCommands</td>
<td>Query the commands queued (processing commands) on the device. These commands are in three states: PENDING, SENT, and DELIVERED. Note: If a command in the DELIVERED state is not updated after a system-set period of time (depending on the system configuration), it will be removed from the queue and become a history command. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAsyncDeviceCommand</td>
<td>The IoT platform can query commands with a specified ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">BacklogPolicyManagement</td>
<td>ListRoutingBacklogPolicy</td>
<td>The application server can call this interface to query the list of data flow backlog policies set on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRoutingBacklogPolicy</td>
<td>The application server can call this interface to modify a specified data flow backlog policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRoutingBacklogPolicy</td>
<td>The application server can call this interface to delete a specified data flow backlog policy on the IoT platform. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateRoutingBacklogPolicy</td><td>The application server can call this interface to create a data routing backlog policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRoutingBacklogPolicy</td>
<td>The application server can call this interface to query a specific data routing backlog policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">BatchTask</td>
<td>ListBatchTasks</td>
<td>The application server can call this interface to query the batch task list on the IoT platform. Each task includes specific task content, task status, and task completion statistics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateBatchTask</td>
<td>Application servers can call this API to create batch processing tasks and perform batch operations on multiple devices. Currently, batch firmware upgrades, batch device creation, batch device deletion, batch device freezing, batch device thawing, batch command creation, and batch message creation tasks are supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RetryBatchTask</td>
<td>Application servers can call this API to retry batch tasks. Currently, only task_types of firmwareUpgrade and softwareUpgrade are supported. This API cannot be called if the task corresponding to task_id is already successful, stopped, stopping, waiting, or initializing. If the request body is {}, calling this API will re-execute all subtasks with a status of failed, failed pending retry, or stopped. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteBatchTask</td>
<td>The application server can call this interface to delete completed batch tasks (status: success, failure, partial success, or stopped) on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBatchTask</td>
<td>The application server can call this interface to query information about a specified batch task on the IoT platform, including task content, task status, task completion statistics, and a list of subtasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopBatchTask</td>
<td>The application server can call this interface to stop a batch task. Currently, only the task_types of firmwareUpgrade and softwareUpgrade are supported. If the task corresponding to task_id has already completed (successful, failed, partially successful, stopped) or is currently stopping, this API cannot be called. If the request body is {}, calling this API will stop all subtasks in the executing, waiting, or failed retry states. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">BatchTaskFile</td>
<td>DeleteBatchTaskFile</td>
<td>The application server can call this API to delete batch task files. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBatchTaskFiles</td>
<td>The application server can call this API to query the list of batch task files. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadBatchTaskFile</td>
<td>The application server can call this API to upload batch task files for creating batch tasks. Currently, it supports file uploads for batch creating device tasks, batch deleting device tasks, batch freezing device tasks, and batch thawing device tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">BridgeManagement</td>
<td>AddBridge</td>
<td>The application server can call this API to create a bridge on the IoT platform. Only created bridges can connect to the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBridges</td>
<td>The application server can call this API to query the list of bridges on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetBridgeSecret</td>
<td>The application server can call this API to reset the bridge secret key on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteBridge</td>
<td>The application server can call this API to delete a specified bridge on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">BroadcastManagement</td>
<td>BroadcastMessage</td>
<td>The application server can call this API to publish a broadcast message to all online devices subscribed to the specified topic. After the application sends the broadcast message to the platform, the platform will first return the application's response result and then broadcast the message to the devices. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">CertificateManagement</td>
<td>ListCertificates</td>
<td>The application server can call this interface to obtain the device CA certificate list on the IoT platform.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCertificate</td>
<td>The application server can call this interface to delete the device CA certificate on the IoT platform.</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddCertificate</td>
<td>The application server can call this interface to upload the device CA certificate on the IoT platform.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCertificate</td>
<td>The application server can call this API to update the CA certificate on the IoT platform. This API is only supported by Standard and Enterprise Edition instances; it is not supported by the Basic Edition. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckCertificate</td>
<td>The application server can call this API to verify the device's CA certificate on the IoT platform. This is to verify that the user holds the private key for the device's CA certificate. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">CommandManagement</td>
<td>CreateCommand</td>
<td>The device's product model defines the commands that the IoT platform can issue to the device. The application server can call this API to issue commands to a specified device, enabling synchronous control of the device. The platform is responsible for sending commands to the device synchronously and returning the results of the command execution. If the device does not respond, the platform will timeout to the application server. The platform timeout period is 20 seconds. If the command takes more than 20 seconds to send, it is recommended to use [message sending](https://support.huaweicloud.com/api-iothub/iot_06_v5_0059.html). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">DeviceAuthorizer</td>
<td>UpdateDeviceAuthorizer</td>
<td>The application server can call this API to update the custom authentication ID of a specified ID on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeviceAuthorizer</td>
<td>The application server can call this API to query the detailed information of a specified custom authentication ID on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDeviceAuthorizer</td>
<td>The application server can call this API to create a custom authentication ID on the IoT platform. Custom authentication means that users can customize authentication logic through function services to authenticate devices connected to the platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDeviceAuthorizer</td>
<td>The application server can call this API to delete a specified custom authentication authorization on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDeviceAuthorizers</td>
<td>The application server can call this API to query the list of custom authentication authorizations on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">DeviceGroup</td>
<td>CreateOrDeleteDeviceInGroup</td>
<td>The application server can call this API to manage devices in a device group. A maximum of 20,000 devices can be added to a single device group, and a device can be added to a maximum of 10 device groups. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDeviceGroups</td>
<td>Application servers can call this API to query the device group list on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDeviceGroup</td>
<td>Application servers can call this API to create new device groups. A Huawei Cloud account can have a maximum of 1,000 device groups, including parent and child groups. The maximum hierarchy level of a device group is 5, meaning the maximum depth of the relationship tree formed by a group is 5. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeviceGroup</td>
<td>The application server can call this interface to query the details of a specified device group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDeviceGroup</td>
<td>The application server can call this interface to delete a specified device group. If the device group has child device groups or if there are devices in the device group, the child device groups must be deleted and the devices removed from the device group before the device group can be deleted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDeviceGroup</td>
<td>The application server can call this interface to modify a specified device group in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDevicesInGroup</td>
<td>The application server can call this interface to query the list of devices in a specified device group. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">DeviceManagement</td>
<td>ListDeviceGroupsByDevice</td>
<td>The application server can call this interface to query the list of device groups to which a device belongs on the IoT platform. This interface is only supported by Standard and Enterprise Edition instances; it is not supported by the Basic Edition. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDevice</td>
<td>The application server can call this interface to delete a specified device on the IoT platform. If a device is connected to an indirect device, all indirect devices must be deleted before the device can be deleted. This API only supports deleting a single device. To delete devices in batches, see [Create a batch task](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html). </td>
<td>To be tested</td>
</tr>
<tr>
<td>UnfreezeDevice</td>
<td>The application server can call this API to unfreeze a device. After unfreezing, the device can connect online. This API only supports unfreezing a single device. To unfreeze devices in batches, see [Create a batch task](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeGateway</td>
<td>The application server can call this interface to modify the gateway of a sub-device on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchDevices</td>
<td>#### Interface Description</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDevice</td>
<td>The application server can call this interface to modify the basic information of a specified device on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetDeviceSecret</td>
<td>The application server can call this interface to reset the device secret key. If a specified secret key is provided, the platform will reset the device secret key to the specified secret key. If no secret key is provided, the platform will automatically generate a new random secret key and return it. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDevice</td>
<td>The application server can call this interface to query the detailed information of a specified device on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDevice</td>
<td>The application server can call this interface to create a device on the IoT platform. Only after the device is created can it be connected to the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDevices</td>
<td>The application server can call this interface to query the device information list in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetFingerprint</td>
<td>The application server can call this interface to reset the device fingerprint. If the specified device fingerprint is present, it will be reset to the specified value; if not, it will be left blank. The first time the device connects, the device fingerprint will be set to the certificate fingerprint used at the time of initial access. </td>
<td>To be tested</td>
</tr>
<tr>
<td>FreezeDevice</td>
<td>The application server can call this interface to freeze a device. After freezing, the device cannot connect online. You can unfreeze the device using the thaw device interface. Note that this currently only supports freezing devices directly connected to the platform. This interface only supports freezing individual devices. To freeze devices in batches, see [Create a batch task](https://support.huaweicloud.com/api-iothub/iot_06_v5_0045.html). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">DeviceProxy</td>
<td>ShowDeviceProxy</td>
<td>The application server can call this interface to query the detailed information of a specified device proxy in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDeviceProxy</td>
<td>The application server can call this API to create a dynamic device proxy rule on the IoT platform. This allows sub-devices to autonomously select gateway devices for online access and message reporting. This means that sub-devices under any gateway in a proxy group can go online through other devices in the proxy group ([Gateway updates sub-device status](https://support.huaweicloud.com/api-iothub/iot_06_v5_3022.html)) and then report data ([Gateway batch device attribute reporting](https://support.huaweicloud.com/api-iothub/iot_06_v5_3006.html)). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDeviceProxies</td>
<td>The application server can call this API to query the device proxy list on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDeviceProxy</td>
<td>The application server can call this interface to modify the basic information of a specified device proxy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDeviceProxy</td>
<td>The application server can call this interface to delete a specified device proxy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">DeviceShadow</td>
<td>UpdateDeviceShadowDesiredData</td>
<td>The application server can call this interface to configure the desired attributes (desired area) of the device shadow. These attributes are then sent to the device when it comes online or reports its attributes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeviceShadow</td>
<td>The application server can call this interface to query the device shadow information of a specified device, including the desired attribute information (desired area) and the device's latest reported attribute information (reported area). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">FlowControlPolicyManagement</td>
<td>UpdateRoutingFlowControlPolicy</td>
<td>The application server can call this interface to modify the specified data flow control policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRoutingFlowControlPolicy</td>
<td>The application server can call this interface to create a data flow control policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRoutingFlowControlPolicy</td>
<td>The application server can call this interface to query the list of data flow control policies set on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRoutingFlowControlPolicy</td>
<td>The application server can call this interface to query a specific data flow control policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRoutingFlowControlPolicy</td>
<td>The application server can call this interface to delete a specific data flow control policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">FunctionServiceManagement</td>
<td>AddFunctions</td>
<td>Provides the function of creating codec functions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFunctions</td>
<td>Provides the function of querying codec functions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteFunctions</td>
<td>Provides the function of deleting codec functions. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">MessageManagement</td>
<td>ListDeviceMessages</td>
<td>The application server can call this interface to query the messages sent by the platform to the device. The platform saves a maximum of 20 messages for each device by default. After 20 messages are saved, subsequent messages will replace the oldest messages. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDeviceMessage</td>
<td>The application server can call this interface to delete the message with the specified message ID sent by the platform to the device. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeviceMessage</td>
<td>The application server can call this interface to query the messages with the specified message ID sent by the platform to the device. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateMessage</td>
<td>The IoT platform can send messages to devices. Application servers can call this interface to send messages to specified devices to control them. After the application sends the message to the platform, the platform returns the application's response, which then sends the message to the device. The application's response from the platform is not necessarily the device's received result. We recommend that user applications subscribe to [Device Message Status Change Notification](https://support.huaweicloud.com/api-iothub/iot_06_v5_01203.html). After subscribing, the platform will push the device's received result to the subscribed application. </td>
<td>To be tested</td>
</tr>
<tr><td rowspan="4">OtaPackageManagement</td>
<td>ShowOtaPackage</td>
<td>Users can call this interface to query the upgrade package details associated with the OBS object.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOtaPackage</td>
<td>Users can call this interface to create an upgrade package and associate it with the OBS object.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteOtaPackage</td>
<td>Users can call this interface to delete the upgrade package information associated with the OBS object. The object on the OBS will not be deleted.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOtaPackageInfo</td>
<td>Users can call this interface to query the upgrade package list associated with the OBS object.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">PolicyManagement</td>
<td>ShowDevicePolicy</td>
<td>The application server can call this interface to query the detailed information of a specified policy ID on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BindDevicePolicy</td>
<td>The application server can call this interface to bind target policies to batches of devices on the IoT platform. Currently, supported target types are: device and product. When the target type is product, the policy takes effect on all devices under that product. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDevicePolicy</td>
<td>The application server can call this interface to create a policy on the IoT platform. This policy must be bound to devices and products to take effect. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDevicePolicies</td>
<td>The application server can call this interface to query the policy list on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UnbindDevicePolicy</td>
<td>The application server can call this interface to unbind the target object from a specified policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDevicePolicy</td>
<td>The application server can call this interface to update the policy on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTargetsInDevicePolicy</td>
<td>The application server can call this API to query the list of targets bound to a specified policy ID on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDevicePolicy</td>
<td>The application server can call this API to delete a specified policy on the IoT platform. Note: Deleting a policy will also unbind all bound objects. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">ProductManagement</td>
<td>CreateProduct</td>
<td>The application server can call this API to create a product. This API only creates the product and does not create or install a plugin. If data encoding and decoding is required, a plugin must be developed and installed on the platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListProducts</td>
<td>The application server can call this interface to query the list of product models imported into the IoT platform and obtain a summary of the product models. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteProduct</td>
<td>The application server can call this interface to delete a specific product model imported into the IoT platform. This interface only deletes the product, not the associated plug-ins. If a device exists under the product, the product cannot be deleted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProduct</td>
<td>The application server can call this interface to modify a specific product model imported into the IoT platform, including the product model's services, properties, commands, and so on. This API only modifies the product; it does not modify or install plugins. If you modify the service definition in a product and the corresponding plugin exists on the platform, please modify and reinstall the plugin. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProduct</td>
<td>The application server can call this API to query the detailed information of a specified product model imported into the IoT platform, including the product model's services, properties, commands, and so on. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">PropertiesManagement</td>
<td>ListProperties</td>
<td>The device's product model defines the properties that the IoT platform can deliver to the device. The application server can call this API to send commands to the device to query its real-time properties. The device then synchronously returns the property query results to the application server. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProperties</td>
<td>The device's product model defines the properties that the IoT platform can deliver to the device. Application servers can call this interface to deliver these properties to a specific device. The platform is responsible for synchronously sending these properties to the device and synchronously returning the results of the device executing these properties. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">ProvisioningTemplateManagement</td>
<td>ListProvisioningTemplates</td>
<td>Application servers can call this interface to query the list of provisioning templates on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteProvisioningTemplate</td>
<td>Application servers can call this interface to delete a specific provisioning template on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProvisioningTemplate</td>
<td>The application server can call this interface to update the provisioning template with the specified ID on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateProvisioningTemplate</td>
<td>The application server can call this interface to create a provisioning template on the IoT platform. If the user's device is not registered on the platform, the provisioning template can be used to automatically update the device information when the device first connects to the IoT platform.Register with the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProvisioningTemplate</td>
<td>The application server can call this interface to query the IoT platform for detailed information about a specified provisioning template ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">RoutingRuleManagement</td>
<td>UpdateRoutingRule</td>
<td>The application server can call this interface to modify the configuration parameters of a specified rule condition on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRoutingRule</td>
<td>The application server can call this interface to query the configuration information of a specified rule condition on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRuleAction</td>
<td>The application server can call this interface to delete a specified rule action on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRoutingRule</td>
<td>The application server can call this interface to create a rule trigger condition on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRuleAction</td>
<td>The application server can call this interface to create a rule action on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRuleAction</td>
<td>The application server can call this interface to modify the configuration of a specified rule action on the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRuleAction</td>
<td>The application server can call this interface to query the configuration information of a specified rule action in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRoutingRules</td>
<td>The application server can call this interface to query the list of rule conditions set in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRoutingRule</td>
<td>The application server can call this interface to delete a specified rule condition in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRuleActions</td>
<td>The application server can call this interface to query the list of rule actions set in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">RuleManagement</td>
<td>ShowRule</td>
<td>The application server can call this interface to query the configuration information of a specified rule in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRules</td>
<td>The application server can call this interface to query the list of rules set in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRule</td>
<td>The application server can call this interface to create a rule in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRule</td>
<td>The application server can call this interface to modify the configuration of a specified rule in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRule</td>
<td>The application server can call this interface to delete a specified rule in the IoT platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeRuleStatus</td>
<td>The application server can call this interface to modify the status of a specified rule in the IoT platform, activating or deactivating the rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">TagManagement</td>
<td>TagDevice</td>
<td>The application server can call this interface to bind a tag to a specified resource. Currently, the resource that supports tags is Device. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListResourcesByTags</td>
<td>The application server can call this interface to query the resources bound to the specified tag. Currently, the resource that supports tags is Device. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UntagDevice</td>
<td>The application server can call this interface to unbind a tag from a specified resource. Currently, the resource that supports tags is Device. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">TunnelManagement</td>
<td>ListDeviceTunnels</td>
<td>Users can use this interface to query all device tunnels under a project to manage devices. Application servers can use this interface to query the platform for device tunnel establishment status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddTunnel</td>
<td>Users can use this interface to create a tunnel (WebSocket protocol) through which application servers and devices can communicate data. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeviceTunnel</td>
<td>Users can use this interface to query a device tunnel in a project and view its information and connection status. The application server can call this interface to query the platform about the device tunnel establishment status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CloseDeviceTunnel</td>
<td>The application server can use this interface to close a device tunnel. After closing, it can be reconnected. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDeviceTunnel</td>
<td>Users can use this interface to delete a device tunnel. After deletion, the tunnel no longer exists and cannot be reconnected. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>