# IdentityCenterStore MCP Server


## Version
v0.1.0

## Overview

IdentityCenterStore MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IdentityCenterStore. Full-chain management of IdentityCenterStore resources can be carried out based on natural language.

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
<td rowspan="6">Group</td> <td>DescribeGroup</td>
<td>Query the details of an IAM Identity Center user group based on the user group ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGroups</td>
<td>Query the list of IAM Identity Center user groups under the specified identity source. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGroup</td>
<td>Delete the corresponding IAM Identity Center user group based on the user group ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGroup</td>
<td>Create an IAM Identity Center user group in the specified identity source. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGroup</td>
<td>Updates the attributes of the corresponding IAM Identity Center user group based on the user group ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetGroupId</td>
<td>Query the user group ID based on the display name or external identity source ID using an exact match. Either the display name or the external identity source ID is supported; both cannot be passed in simultaneously. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">GroupMembership</td>
<td>ListGroupMemberships</td>
<td>Lists the users in a user group based on the user group ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>IsMemberInGroups</td>
<td>Based on the user ID and group ID list, query whether the user is a member of the group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGroupMembershipsForMember</td>
<td>Based on the user ID, list the groups the user is a member of. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetGroupMembershipId</td>
<td>Based on the user ID and group ID, query the corresponding relationship ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGroupMembership</td>
<td>Add the user to a group. The user and group must be in the same identity source. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DescribeGroupMembership</td>
<td>Query the details of the relationship based on the relationship ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGroupMembership</td>
<td>Unbind the user from the user group based on the relationship ID, that is, remove the user from the user group. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">User</td>
<td>DeleteUser</td>
<td>Delete the corresponding IAM Identity Center user based on the user ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUsers</td>
<td>Query the list of IAM Identity Center users under the specified identity source. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateUser</td>
<td>Create an IAM Identity Center user in the specified identity source. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUser</td>
<td>Update the attributes of the corresponding IAM Identity Center user based on the user ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DescribeUser</td>
<td>Query the detailed information of the corresponding IAM Identity Center user based on the user ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetUserId</td>
<td>Query the user ID based on the user name or external identity source ID, using an exact match. Either the user name or the external identity source ID is selected; both cannot be passed in at the same time. </td> 
<td>To be tested</td> 
</tr> 
</tbody> 
</table> 
</body>
</html>