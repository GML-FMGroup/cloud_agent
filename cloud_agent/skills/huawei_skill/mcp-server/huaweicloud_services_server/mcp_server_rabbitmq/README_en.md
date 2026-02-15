# RabbitMQ MCP Server


## Version
v0.1.0

## Overview

RabbitMQ MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service RabbitMQ. Full-chain management of RabbitMQ resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html> 
<head></head> 
<body> 
<table border="1" cellspacing="0" cellpadding="5"> 
<tbody> 
<tr> 
<th>Category</th> 
<th>Tool name</th> 
<th>Function description</th> 
<th>Status</th> 
</tr> 
<tr> 
<td rowspan="3">Binding management</td> 
<td>CreateBinding</td> 
<td>Add binding. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteBinding</td>
<td>Delete a binding. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBindings</td>
<td>Query the list of Exchange binding information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Exchange Management</td>
<td>ListExchanges</td>
<td>Query the list of Exchanges. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateExchange</td>
<td>Create an Exchange. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteExchanges</td>
<td>Batch delete specified exchanges. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Queue management</td>
<td>DeleteQueueInfo</td>
<td>Clear queue information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateQueue</td>
<td>Create a queue. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowQueueDetails</td>
<td>Query the details of a specified queue. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteQueues</td>
<td>Batch deletes the specified queues. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQueues</td>
<td>Query the list of queues under the corresponding Vhost. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Vhost Management</td>
<td>ListVhosts</td>
<td>Query the Vhost list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteVhosts</td>
<td>Batch deletes the specified Vhosts. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateVhost</td>
<td>Create a Vhost. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Other interfaces</td>
<td>ShowCesHierarchy</td>
<td>Query the monitoring hierarchy of an instance in CES. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEngineProducts</td>
<td>Query the product specification list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMaintainWindows</td>
<td>Query the maintenance window start and end times. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRabbitMqProductCores</td>
<td>Query the number of cores in the RabbitMQ product specification. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAvailableZones</td>
<td>When creating an instance, you need to configure the availability zone ID of the instance. You can query the availability zone ID through this interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Background Task Management</td>
<td>ListBackgroundTasks</td>
<td>Query the background task list of the instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBackgroundTask</td>
<td>Query the specified record in the background task management. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteBackgroundTask</td>
<td>Delete the specified record in the background task management. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Instance Management</td>
<td>UpdatePlugins</td>
<td>Enable or disable plug-ins. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPlugins</td>
<td>Query the plugin list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetPassword</td>
<td>Reset password. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Tag management</td>
<td>ShowRabbitMqProjectTags</td>
<td>Query project tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateOrDeleteRabbitMqTag</td>
<td>Add or delete instance tags in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRabbitMqTags</td>
<td>Query instance tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Lifecycle Management</td>
<td>UpdateInstance</td>
<td>Modify the instance name and description. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstance</td>
<td>Query detailed information about a specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePostPaidInstanceByEngine</td>
<td>Create an instance. This interface supports creating instances with both on-demand and periodic billing methods. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstance</td>
<td>Delete the specified instance and release all its resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRestartOrDeleteInstances</td>
<td>Delete instances in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>EnableDns</td>
<td>After enabling the RabbitMQ instance domain name access feature, clients can connect to the RabbitMQ instance using the domain name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstancesDetails</td>
<td>Query the tenant's instance list, supporting queries based on conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">User Management</td>
<td>ListUser</td>
<td>Query the user list (supported only in the AMQP version). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateUser</td>
<td>Create a user (supported only in the AMQP version). </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUser</td>
<td>Modify user parameters (supported only in the AMQP version). </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteUser</td>
<td>Delete a user (supported only in the AMQP version). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Specification change management</td>
<td>ShowEngineInstanceExtendProductInfo</td>
<td>Query the list of instances with new specifications that can be expanded</td>
<td>To be tested</td>
</tr>
<tr>
<td>ResizeEngineInstance</td>
<td>Instance specification changes. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>