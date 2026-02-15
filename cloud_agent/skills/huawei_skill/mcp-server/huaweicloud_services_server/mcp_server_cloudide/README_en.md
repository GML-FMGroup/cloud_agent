# CloudIDE MCP Server


## Version
v0.1.0

## Overview

CloudIDE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CloudIDE. Full-chain management of CloudIDE resources can be carried out based on natural language.

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
<td rowspan="13">IDE instance management</td> 
<td>ShowInstanceStatusInfo</td> <td>Query the status of an IDE instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstance</td>
<td>Delete the IDE instance (also deletes disk data)</td>
<td>To be tested</td>
</tr>
<tr>
<td>StartInstance</td>
<td>Start the IDE instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstance</td>
<td>Query an IDE instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>StopInstance</td>
<td>Stop the IDE instance (does not delete disk data)</td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckName</td>
<td>Check if the IDE instance name is duplicated</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInstanceBy3rd</td>
<td>Create an IDE instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstances</td>
<td>Query the IDE instance list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckInstanceAccess</td>
<td>Check if the user has permission to access a specific IDE instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstanceActivity</td>
<td>Refresh the IDE instance activity status. The instance will automatically shut down after the expiration time set for the instance has expired. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOrgInstances</td>
<td>Query the list of IDE instances under a tenant</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstance</td>
<td>Modify an IDE instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInstance</td>
<td>Create an IDE instance</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">codebreeze</td>
<td>ShowResult</td>
<td>Get the result of the code generation request.</td>
<td>To be tested</td>
</tr>
<tr> 
<td>CreateAcceptance</td> 
<td>create a acceptance</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateApply</td> 
<td>create a join-request</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateLogin</td> 
<td>create a login</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateRequest</td> 
<td>create a code generation request.</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateEvent</td> 
<td>create an event</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td rowspan="3">codebreezetsbot</td>
<td>SyncChat</td>
<td>Asynchronous chat request</td>
<td>To be tested</td>
</tr>
<tr>
<td>StartChat</td>
<td>Start a conversation</td>
<td>To be tested</td>
</tr>
<tr>
<td>SyncGetChatResult</td>
<td>Asynchronous chat result</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Account permission management</td>
<td>ShowAccountStatus</td>
<td>Query current account access permissions</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Technology stackManagement
<td>ListStacks</td>
<td>Get all technology stacks by region</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPrice</td>
<td>Get technology stack billing information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="16">Plugin Market</td>
<td>AddExtensionEvaluation</td>
<td>Add plugin review</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowExtensionTestingResult</td>
<td>Get plugin testing results</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPublisher</td>
<td>Get the publisher list under the current user</td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadExtensionFile</td>
<td>Upload plugin</td>
<td>To be tested</td>
</tr>
<tr>
<td>PublishExtension</td>
<td>Publish plugin</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddExtensionStar</td>
<td>Add new star</td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckMaliciousExtensionEvaluation</td>
<td>Report comment, report reply</td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadFilePublisher</td>
<td>File upload normalization</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCategoryList</td>
<td>Query plugin categories</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEvaluationReply</td>
<td>Delete reply</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowExtensionEvaluation</td>
<td>Query plugin evaluation</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListExtensions</td>
<td>Query plugin list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEvaluation</td>
<td>Delete Comment</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddExtensionEvaluationReply</td>
<td>Add comment reply, reply to comment reply</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowExtensionEvaluationStar</td>
<td>Query plugin star rating</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowExtensionDetail</td>
<td>Query plugin details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Plugin Management</td>
<td>ShowExtensionAuthorization</td>
<td>Query the IDE instance's authorization status for plugins. Plugins that agree to authorization can use the logged-in user's token to call third-party services within the IDE instance.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateExtensionAuthorization</td>
<td>Set the IDE instance's authorization status for plugins. Agree, Disagree, Unknown (will prompt again next time)</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Template Management</td>
<td>ListProjectTemplates</td>
<td>Query the Technology Stack Template Project</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>