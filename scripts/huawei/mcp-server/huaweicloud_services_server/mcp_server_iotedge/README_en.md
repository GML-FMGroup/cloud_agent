# IoTEdge MCP Server

## Version Information
v0.1.0

## Product Description

The IoTEdge MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud IoTEdge. It enables full-link management of IoTEdge resources based on natural language processing.

## Available Tools
Covering the full API, available for use as needed. The list and status are as follows:

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
<td rowspan="4">App</td>
<td>ShowApp</td>
<td>The application server can call this API to query information about a specified batch task in the IoT platform, including task content, task status, task completion statistics, and a list of subtasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApp</td>
<td>The application server can call this API to delete an application template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApps</td>
<td>The application server can call this interface to query the application template list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateApp</td>
<td>The application server can call this interface to create batch processing tasks and perform batch operations on multiple devices. Currently, batch firmware upgrades, batch device creation, batch device deletion, batch freeze, batch thaw, batch synchronous command issuance, and batch asynchronous command issuance are supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">AppInstance</td>
<td>DeleteAppInstance</td>
<td>The application server can call this interface to delete application instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppInstanceHistory</td>
<td>The application server can call this interface to query the historical version list of an application instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppInstances</td>
<td>The application server can call this interface to query the application instance list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAppInstance</td>
<td>The application server can call this interface to create an application instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAppInstance</td>
<td>The application server can call this interface to update an application instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">AppVersion</td>
<td>ListAppImage</td>
<td>The application server can call this interface to query the image list included in the application version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAppVersion</td>
<td>The application server can call this interface to create an application version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppVersions</td>
<td>The application server can call this interface to query the application version list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAppVersion</td>
<td>The application server can call this interface to query application version details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAppVersion</td>
<td>The application server can call this interface to delete the application version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DownloadAppVersion</td>
<td>The application server can call this interface to download the application version chart package. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">BasicNode</td>
<td>CreateEdgeNode</td>
<td>Create an edge node</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEdgeNode</td>
<td>Delete the specified edge node</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEdgeNode</td>
<td>Query edge node details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEdgeNodeHostsInfo</td>
<td>Query host details under the edge node</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInstallCmd</td>
<td>Generates an edge node installation command. The command is valid for 30 minutes and needs to be regenerated after that.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEdgeNode</td>
<td>Modify an edge node</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEdgeNodes</td>
<td>Query the edge node list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Cluster</td>
<td>DeleteCluster</td>
<td>The application server can call this API to delete an edge cluster.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateClusterInstallllCmd</td>
<td>The application server can call this interface to generate edge cluster installation commands. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClusters</td>
<td>The application server can call this interface to query the edge cluster list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCluster</td>
<td>The application server can call this interface to create an edge cluster. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCluster</td>
<td>The application server can call this interface to query edge cluster details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">DeviceControls</td>
<td>ExecuteDeviceControlsSet</td>
<td>Device control set</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetDeviceControlDefaultValues</td>
<td>Device control defaults</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPropertyActiveControls</td>
<td>Get property active controls</td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteDeviceControlsRelease</td>
<td>Device control release</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">DeviceManager</td>
<td>ListDevices</td>
<td>Query device list</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDevice</td>
<td>Add device</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDevice</td>
<td>Modify device</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDevice</td>
<td>Delete device</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProductConfig</td>
<td>Get protocol configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">EdgeAppConfigsTemplateManagement</td>
<td>BatchListAppConfigsTemplates</td>
<td>Query the application configuration template list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAppConfigsTemplate</td>
<td>Query application configuration template details</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddAppConfigsTemplates</td>
<td>Add application configuration template</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAppConfigsTemplate</td>
<td>Delete application configuration template</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddGeneralAppConfigsTemplate</td>
<td>Import the standard application configuration template</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">EdgeAppManagement</td>
<td>ShowEdgeApp</td>
<td>Query applications</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchListEdgeApps</td>
<td>Query application list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEdgeApp</td>
<td>Delete application</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateEdgeApp</td>
<td>Create application</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">EdgeAppVersionManagement</td>
<td>UpdateEdgeApplicationVersionState</td>
<td>Updates the application version state. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateEdgeApplicationVersion</td>
<td>Create application version</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEdgeApplicationVersion</td>
<td>Modify application version</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEdgeApplicationVersion</td>
<td>Query application version details</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchListEdgeAppVersions</td>
<td>Query application version list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEdgeAppVersionicationVersion
<td>Delete application version</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">EdgeDcDsManagement</td>
<td>CreateDs</td>
<td>User creates a data source configuration on a specified edge node through the console interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDcDs</td>
<td>Modify data source configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>SynchronizeDcConfigs</td>
<td>Send data acquisition configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDcDs</td>
<td>Query data source configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDcDs</td>
<td>Delete data source configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchListDcDs</td>
<td>Query data source configuration list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">EdgeDcPointManagement</td>
<td>BatchListDcDevices</td>
<td>Query the data acquisition connection sub-device list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDcPoint</td>
<td>Delete point table configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDcPoint</td>
<td>Query point table configuration details</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDcPoint</td>
<td>Modify point table configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchListDcPoints</td>
<td>Query point table configuration list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDcPoints</td>
<td>Batch delete point table configurations</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDcPoint</td>
<td>User configures point table on specified edge node through console interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">EdgeExternals</td>
<td>DeleteExternalEntity</td>
<td>Delete an external entity under a node</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateExternalEntity</td>
<td>User sets access information for an external entity on a specified edge node</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListExternalEntity</td>
<td>User queries a list of external entities on a specified edge node</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateExternalEntity</td>
<td>User modifies access information for a specified external entity on a specified edge node</td>
<td>To be tested tested</td>
</tr>
<tr>
<td rowspan="7">EdgeModuleManagement</td>
<td>CreateModule</td>
<td>The user creates an edge module on a specified edge node through the console interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchListModules</td>
<td>The user queries the edge module list on a specified edge node through the console interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateModule</td>
<td>The user queries the specified edge module on a specified edge node through the console interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateModuleState</td>
<td>The user starts and stops the data acquisition connection through the console interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteModule</td>
<td>Users delete edge modules on specified edge nodes through the console interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>InvokeModuleMsg</td>
<td>iotedge transparently proxies user requests to modules through this interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowModule</td>
<td>Users query specified edge modules on specified edge nodes through the console interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">EdgeModuleShadow</td>
<td>UpdateModuleShadow</td>
<td>Update module shadow information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowModuleShadow</td>
<td>Get module shadow information</td>
<td>To be tested</td>
</tr>
<tr><td rowspan="2">EdgeNodeRouteService</td>
<td>UpdateRoutes</td>
<td>User sets edge routes on a specified edge node</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRoutes</td>
<td>User queries the edge route list on a specified edge node</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">EdgeOtTemplateManagement</td>
<td>AddOtTemplates</td>
<td>Add data acquisition template</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOtTemplate</td>
<td>Query data acquisition template details</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteOtTemplate</td>
<td>Delete data acquisition template</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddGeneralOtTemplate</td>
<td>Import standard data acquisition template</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchListOtTemplates</td>
<td>Query data acquisition template list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">EdgePointTemplatesManagement</td>
<td>ShowPointTemplate</td>
<td>Query point table template file</td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportPoints</td>
<td>Users configure the point table on a specified edge node through the console interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPoints</td>
<td>Query the point table template file</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">EdgeScheduleManagement</td>
<td>DeleteSchedule</td>
<td>Users delete the scheduling plan on the edge node through the northbound interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSchedule</td>
<td>Users modify the scheduling plan on the edge node through the northbound interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSchedule</td>
<td>Users create a scheduling plan on a specified edge node through the northbound interface.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">HttpRequestProxy</td>
<td>InvokePatchProxy</td>
<td>Used when the northbound NA calls the PATCH method of a southbound third-party application.</td>
<td>To be tested</td>
</tr>
<tr>
<td>InvokePutProxy</td>
<td>Used when the northbound NA calls the PUT method of a southbound third-party application.</td>
<td>To be tested</td>
</tr>
<tr>
<td>InvokeDeleteProxy</td>
<td>Used when the northbound NA calls the DELETE method of a southbound third-party application.</td>
<td>To be tested</td>
</tr>
<tr>
<td>InvokeGetProxy</td>
<td>Used when the northbound NA calls the GET method of a southbound third-party application.</td>
<td>To be tested</td>
</tr>
<tr>
<td>InvokePostProxy</td>
<td>Used when the northbound NA calls the POST method of a southbound third-party application.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">IaConfigManagement</td>
<td>UpdateIaConfig</td>
<td>Create & update southbound 3rdIA configuration item information.</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchImportConfigs</td>
<td>Batch import southbound 3rdIA configuration items.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListIaConfigs</td>
<td>Query the list of southbound 3rdIA configuration items</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchConfirmConfigsNew</td>
<td>Southbound 3rdIA performs batch confirmation of issued configuration items</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteIaConfig</td>
<td>Delete southbound 3rdIA configuration items</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowIaConfig</td>
<td>Query southbound 3rdIA configuration item details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">NaManagement</td>
<td>DeleteNa</td>
<td>Delete northbound NA information. If an edge node has been assigned this NA information, the edge node will be notified. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNaAuthorizedNodes</td>
<td>Query the assigned nodes for this northbound NA information</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateNa</td>
<td>Creates and updates northbound NA information. When updating northbound NA information, all edge nodes assigned the northbound NA are notified. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchAssociateNaToNodes</td>
<td>Batch-authorizes northbound NA information to edge nodes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNas</td>
<td>Query the northbound NA information list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNa</td>
<td>Query the northbound NA information details</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>