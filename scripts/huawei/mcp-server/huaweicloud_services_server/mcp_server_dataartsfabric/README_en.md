# DataArtsFabric MCP Server


## Version
v0.1.0

## Overview

DataArtsFabric MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DataArtsFabric. Full-chain management of DataArtsFabric resources can be carried out based on natural language.

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
<td rowspan="3">Agency</td> <td>CreateAgency</td>
<td>Automatically creates a service delegation for a user. A delegation requires the required permission policy to be used. Creating a delegation automatically adds the required permission policy, but you can also specify a required permission policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAgency</td>
<td>Delete a user's service delegation permissions. You can delete the permission policy attached to a delegation by specifying a permission policy. Required permission policies cannot be deleted. If no permission policy is specified, the entire delegation is deleted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAgency</td>
<td>Query whether the user's service delegation details meet the system's required permissions. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Agreement</td>
<td>CreateAgreement</td>
<td>Register tenant agreement</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAgreementRule</td>
<td>Query system agreement</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAgreement</td>
<td>Delete user registration agreement</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAgreement</td>
<td>Query whether the user has registered an agreement</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">ConfigCenter</td>
<td>ListFeatures</td>
<td>Query user supported features. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td rowspan="6">Endpoint</td> 
<td>ShowEndpoint</td> 
<td>Query endpioint details</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>UpdateEndpoint</td> 
<td>Modify Endpoint</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ListEndpoints</td> 
<td>Query Endpoint list</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateEndpoint</td> 
<td>Create Endpoint</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>DeleteEndpoint</td> <td>Delete endpoint</td>
<td>To be tested</td>
</tr>
<tr>
<td>SubscribeEndpoint</td>
<td>Subscribe to an endpoint in the user's Workspace (public endpoint scenario). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Framework</td>
<td>ListFrameworks</td>
<td>Query the Framework list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Health</td>
<td>ShowAdminHealthCheck</td>
<td>Service health check</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Message</td>
<td>ListMessageNotificationPolicy</td>
<td>Query the message notification policy list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateMessageNotificationPolicy</td>
<td>Create a message notification policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteMessageNotificationPolicy</td>
<td>Delete a message notification policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Metric</td>
<td>UpdateMetricsConfig</td>
<td>Update AOM monitoring collection configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">ModelDefinition</td>
<td>CreateModelDefinition</td>
<td>Create model</td>
<td>To be tested</td>
</tr>
<tr><td>ListBaseModels</td>
<td>List base models</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListModelVersions</td>
<td>Query the model version list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteModelVersion</td>
<td>Delete the model version</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListModels</td>
<td>List models</td>
<td>To be tested</td>
</tr>
<tr>
<td>CleanupModel</td>
<td>Clean up unused model definitions</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateModelDefinition</td>
<td>Update the model, generating a new version</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Specification</td>
<td>ListSpecs</td>
<td>Query the service specification list and purchase computing resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">TMS</td>
<td>BatchCreateFabricWorkspaceTags</td>
<td>Batch create resource tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFabricProjectTags</td>
<td>Query project tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTagFabricWorkspaces</td>
<td>Query resource instance list</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteFabricWorkspaceTags</td>
<td>Batch delete resource tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFabricWorkspaceTags</td>
<td>Query resource tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>CountTagFabricWorkspaces</td>
<td>Query the number of resource instances</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Workspace</td>
<td>UpdateWorkspace</td>
<td>Update Workspace</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWorkspace</td>
<td>Delete Workspace</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkspaces</td>
<td>Query the workspace list. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateWorkspace</td> 
<td>Create workspace</td> 
<td>To be tested</td> 
</tr> 
</tbody> 
</table> 
</body>
</html>