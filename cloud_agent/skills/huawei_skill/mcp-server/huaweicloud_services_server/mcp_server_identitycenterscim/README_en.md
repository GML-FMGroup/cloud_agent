# IdentityCenterSCIM MCP Server


## Version
v0.1.0

## Overview

IdentityCenterSCIM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IdentityCenterSCIM. Full-chain management of IdentityCenterSCIM resources can be carried out based on natural language.

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
<td rowspan="5">Group</td> <td>CreateGroup</td>
<td>Use the SCIM protocol to synchronize user groups with the IAM identity center. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetGroup</td>
<td>Query the details of an existing user group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PatchGroup</td>
<td>Modify some properties of an existing user group and manage users in the user group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGroup</td>
<td>Delete an existing user group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGroups</td>
<td>Perform a filtered query on the list of existing user groups. A maximum of 50 results will be returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">ServiceProviderConfig</td>
<td>ServiceProviderConfig</td>
<td>Query the SCIM-related configuration information of the IAM identity center. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">User</td>
<td>PatchUser</td>
<td>Modify some attributes of an existing user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUsers</td>
<td>Perform a filtered query on the existing user list. A maximum of 50 results will be returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteUser</td>
<td>Delete an existing user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PutUser</td>
<td>Update an existing user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetUser</td>
<td>Query the details of an existing user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateUser</td>
<td>Use the SCIM protocol to synchronize users with the IAM identity center. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>