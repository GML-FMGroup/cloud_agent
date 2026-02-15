# IdentityCenter MCP Server


## Version
v0.1.0

## Overview

IdentityCenter MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IdentityCenter. Full-chain management of IdentityCenter resources can be carried out based on natural language.

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
<td rowspan="7">AccountAssignment</td> <td>DeleteAccountAssignment</td>
<td>Deletes access permissions from the specified account using the specified permission set. The principal can be an IAM Identity Center user or group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAccountAssignment</td>
<td>Assigns access permissions to the corresponding principal using the specified permission set. The principal can be an IAM Identity Center user or group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccountAssignments</td>
<td>Lists the users or groups associated with the specified account and the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccountAssignmentDeletionStatus</td>
<td>Query the deletion status of account assignments under the specified IAM Identity Center instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DescribeAccountAssignmentDeletionStatus</td>
<td>Query the account assignment deletion status details under the specified IAM Identity Center instance based on the request ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DescribeAccountAssignmentCreationStatus</td>
<td>Query the account assignment creation status details under the specified IAM Identity Center instance based on the request ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccountAssignmentCreationStatus</td>
<td>Query the account assignment creation status list under the specified IAM Identity Center instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Instance</td>
<td>ListInstances</td>
<td>Query the list of instances in IAM Identity Hub. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">InstanceAccessControlAttributeConfiguration</td>
<td>CreateInstanceAccessControlAttributeConfiguration</td>
<td>Enable access control features for the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstanceAccessControlAttributeConfiguration</td>
<td>Updates the IAM Identity Hub identity source attributes that can be used with an IAM Identity Hub instance for attribute-based access control (ABAC). </td>
<td>To be tested</td>
</tr>
<tr>
<td>DescribeInstanceAccessControlAttributeConfiguration</td>
<td>Returns a list of IAM Identity Hub identity source attributes that are configured for use with Attribute-Based Access Control (ABAC) for the specified IAM Identity Hub instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstanceAccessControlAttributeConfiguration</td>
<td>Disables Attribute-Based Access Control (ABAC) for the specified IAM Identity Hub instance and deletes all configured attribute mappings. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="19">PermissionSet</td>
<td>ListPermissionSetProvisioningStatus</td>
<td>Query the provisioning status of permission sets in the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AttachManagedPolicyToPermissionSet</td>
<td>Add the system identity policy to the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPermissionSets</td>
<td>Query the list of permission sets under the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCustomRoleFromPermissionSet</td>
<td>Delete the custom policy from the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ProvisionPermissionSet</td>
<td>Pre-assign the specified permission set to the specified account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePermissionSet</td>
<td>Update the properties of the specified permission set based on the permission set ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetCustomRoleForPermissionSet</td>
<td>Get the custom policy assigned to the permission set</td>
<td>To be tested</td>
</tr>
<tr>
<td>DescribePermissionSetProvisioningStatus</td><td>Query the details of the provisioned status of a permission set based on the request ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePermissionSet</td>
<td>Create a permission set in the specified IAM Identity Center instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PutCustomPolicyToPermissionSet</td>
<td>Add a custom identity policy to the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCustomPolicyFromPermissionSet</td>
<td>Delete a custom identity policy from the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPermissionSetsProvisionedToAccount</td>
<td>Query the list of permission sets assigned to the specified account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetCustomPolicyForPermissionSet</td>
<td>Query the details of the custom identity policy in the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DescribePermissionSet</td>
<td>Query the details of the specified permission set based on the permission set ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DetachManagedPolicyFromPermissionSet</td>
<td>Delete the system identity policy in the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListManagedPoliciesInPermissionSet</td>
<td>Get a list of system identity policies added to the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PutCustomRoleToPermissionSet</td>
<td>Append a custom policy to the permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePermissionSet</td>
<td>Delete the specified permission set based on the permission set ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccountsForProvisionedPermissionSet</td>
<td>Query the list of accounts associated with the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Tag</td>
<td>ListTagResources</td>
<td>Lists the tags bound to the specified resource. Currently supports adding tags to permission sets. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTagResource</td>
<td>Deletes the specified tag from the specified resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTagResource</td>
<td>Adds one or more tags to the specified resource. Currently supports adding tags to permission sets. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">UnexposedPermissionSet</td>
<td>DetachManagedRoleFromPermissionSet</td>
<td>Delete the system policy from the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AttachManagedRoleToPermissionSet</td>
<td>Add the system policy to the specified permission set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListManagedRolesInPermissionSet</td>
<td>Get a list of system policies added to the specified permission set. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>