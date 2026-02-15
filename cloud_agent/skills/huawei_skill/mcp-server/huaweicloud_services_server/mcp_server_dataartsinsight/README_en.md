# DataArtsInsight MCP Server


## Version
v0.1.0

## Overview

DataArtsInsight MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DataArtsInsight. Full-chain management of DataArtsInsight resources can be carried out based on natural language.

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
<td rowspan="1">Product examples</td> 
<td>ListInstances</td> <td>Query the user's activated product instance list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Unified dashboard and large screen resources</td>
<td>ListResources</td>
<td>Unified dashboard and large screen resources</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Collaborative authorization</td>
<td>SaveOrUpdateAuthProperties</td>
<td>Save or modify resource property values. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAuthed</td>
<td>Collaboration authorization list</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchSaveAuth</td>
<td>Batch save, modify, and delete specified self-developed collaboration authorization rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAuthProperties</td>
<td>Get resource property values</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Import and export parameters</td>
<td>CreateAndUpdateExportConfig</td>
<td>Configure export parameters</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Workspace</td>
<td>CreateWorkspace</td>
<td>Create workspace</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWorkspace</td>
<td>Delete workspace</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkspaces</td>
<td>Query workspace details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkspace</td>
<td>Modify workspace</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Data Source</td>
<td>DeleteDataConnectionByConnectionId</td>
<td>Delete data source</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataConnection</td>
<td>Get data source list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDataConnection</td>
<td>Add new data source</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDataConnectionByConnectionId</td>
<td>Get Data Source Details</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDataConnection</td>
<td>Update Data Source</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Dataset</td>
<td>ShowDatasetDetail</td>
<td>Get Dataset Details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCubeAndCatalogList</td>
<td>Query Dataset List</td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveDatasetForOpenApi</td>
<td>Save Dataset</td>
<td>To be tested tested</td>
</tr>
<tr>
<td rowspan="5">Dataset Permissions</td>
<td>UpdatePermissionConfig</td>
<td>Turn permissions on/off</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAndUpdatePermission</td>
<td>Configure dataset permissions</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPermissionConfig</td>
<td>Get dataset permission configuration information</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRule</td><td>Delete Permission</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPermission</td>
<td>Get dataset permission list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">User Tag</td>
<td>ListUserTagValue</td>
<td>Get user tag value</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUserTag</td>
<td>Edit user tag</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserTagHead</td>
<td>Get user tag header</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateUserTag</td>
<td>Create a user tag</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteUserTag</td>
<td>Delete a user tag</td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveUserTagValue</td>
<td>Save user tag content (per user)</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Resource Migration</td>
<td>ImportResourcePackage</td>
<td>API import resource package file</td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportResourcePackage</td>
<td>API export resource package</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowImportResourceTaskDetail</td>
<td>Get import task details</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>