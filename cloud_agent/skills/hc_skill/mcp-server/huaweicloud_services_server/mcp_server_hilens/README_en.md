# HiLens MCP Server


## Version
v0.1.0

## Overview

HiLens MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service HiLens. Full-chain management of HiLens resources can be carried out based on natural language.

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
<td rowspan="5">Job management</td> 
<td>ShowTask</td> <td>Query job details by job ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTask</td>
<td>Delete a job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTask</td>
<td>Edit a job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTasks</td>
<td>Query all jobs in the current deployment and return a detailed list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTask</td>
<td>Create a job. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Firmware Management</td>
<td>ListFirmwares</td>
<td>View the specified firmware's historical version information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Key Management</td>
<td>DeleteSecret</td>
<td>Delete a key</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecret</td>
<td>Query key details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSecret</td>
<td>Create a key</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecrets</td>
<td>Key management for the Professional Edition HiLens console. This function filters user-created keys based on user-requested conditions and returns them in a list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecret</td>
<td>Update the secret key</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Workspace Management</td>
<td>DeleteWorkSpace</td>
<td>Delete the workspace with the specified ID. If there are still resources under the workspace, the deletion will fail.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkSpace</td>
<td>Create a workspace. The workspace name cannot be the same as an existing one.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkSpace</td>
<td>Get the workspace details for the specified workspace_id, including creation time, description, creator, and other information.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkSpace</td>
<td>Change workspace information. Currently, only the description can be changed.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkSpaces</td>
<td>Query all workspace information under the user name and return the list and total number of entries.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="11">Application Deployment Management</td>
<td>ShowDeployments</td>
<td>Get a list of deployments.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDeployment</td>
<td>Update application deployment related information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartAndStopDeploymentPod</td>
<td>Start/Stop the specified instance under the deployment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePod</td>
<td>Delete the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeployment</td>
<td>Get deployment details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDeploymentNodes</td>
<td>Deploy an application to multiple devices by specifying a list of device IDs or device tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeploymentPods</td>
<td>Get a list of user instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateeDeployment
<td>Create an application deployment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartAndStopDeployment</td>
<td>Start/stop an application deployment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDeployment</td>
<td>Delete the specified application deployment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDeploymentUsingPatch</td>
<td>Update some application deployment information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Skill Marketplace</td>
<td>ShowSkillOrderInfo</td>
<td>Get order details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrderForm</td>
<td>Create a free skill order</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSkillList</td>
<td>Get a skill list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSkillOrderList</td>
<td>Get an order list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetDefaultOrderForm</td>
<td>Set the default order</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSkillInfo</td>
<td>Get skill details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Tag management</td>
<td>CreateResourceTags</td>
<td>Professional version of HiLens console tag management, add a tag list for the corresponding resource</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteResourceTag</td>
<td>Professional version of HiLens console tag management, delete a tag for the corresponding resource</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowResourceTags</td>
<td>Professional HiLens console tag management: query the tags of a specific resource and return a tag list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListResourceTags</td>
<td>Professional HiLens console tag management: query all tags of a specific resource type and return a tag list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateNodeTags</td>
<td>Professional HiLens console tag management: users can select multiple devices and batch add multiple tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Device alarm management</td>
<td>ListDeviceAlarms</td>
<td>Get device alarm list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="13">Device management</td>
<td>UpdateNodeCert</td>
<td>When a device is offline or its certificate expires, you can use this interface to update the certificate and reconnect the device to the cloud.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UnfreezeNode</td>
<td>Use the operating service fee to activate the device. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateNode</td>
<td>Fill in device information and register the device to the HiLens Professional Edition console. </td>
<td>To be tested</td>
</tr>
<tr>
<td>FreezeNode</td>
<td>Unbind the activation order from the device. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowUpgradeProgress</td>
<td>Get the device firmware upgrade progress. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNodes</td>
<td>Device management in the HiLens Professional Edition console. Filter according to user request conditions, query user-registered device information, and return it in a list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPlatformManager</td>
<td>Get a list of platform managers</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateNode</td>
<td>Update device log configuration, tags, and descriptions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateNodeFirmware</td>
<td>Upgrade device firmware. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNode</td>
<td>Supports querying device details on the HiLens Professional console. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNodeActivationRecords</td>
<td>Get the activation record list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteNode</td><td>Delete the device from the HiLens Professional console and unbind it from the client-side device. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchNodeConnection</td>
<td>This API is used to enable a disabled device. A disabled device will be unable to connect to cloud services. Re-enabling the device will restore connectivity. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Device Management v1</td>
<td>ListDevices</td>
<td>Get the basic version device list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Configuration Item Management</td>
<td>CreateConfigMap</td>
<td>Create a configuration item</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteConfigMap</td>
<td>Delete a configuration item based on the configuration item ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateConfigMap</td>
<td>Update configuration item information based on the configuration item ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowConfigMap</td>
<td>Query the details of a configuration item based on its ID.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConfigMaps</td>
<td>Get the configuration item details and return them as a list.</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>