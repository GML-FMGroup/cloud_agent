# Organizations MCP Server


## Version
v0.1.0

## Overview

Organizations MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Organizations. Full-chain management of Organizations resources can be carried out based on natural language.

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
<td rowspan="11">Account</td> 
<td>ListCloseAccountStatus</td> <td>Lists account closure requests in the organization with a specified status. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>MoveAccount</td>
<td>Moves an account from its current source location (root or organizational unit) to the specified target location (root or organizational unit). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCreateAccountStatus</td>
<td>Retrieves the current status of an asynchronous request to create an account. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCreateAccountStatuses</td>
<td>Lists account creation requests in the organization with a specified status. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>InviteAccount</td>
<td>Sends an invitation to another account. The invited account will join your organization as a member account. This operation can only be called by an administrative account of the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RemoveAccount</td>
<td>Remove the specified account from the organization. The removed account will become an independent account and will not be a member of any organization. This operation can only be called by an administrative account of the organization. You can only remove an account from an organization if the account has been configured with the information required to operate as an independent account. Note that the account to be removed cannot be a delegated administrator account for any services enabled by the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAccount</td>
<td>Creates an account. The resulting account will automatically become a member of the organization to which the account calling this interface belongs. This operation can only be called by an organization's administrative account. The organization's cloud service will create the required service association delegation and account access delegation in the new account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccounts</td>
<td>Lists the accounts in the organization. This operation can only be called by an organization's administrative account or a member account that is a service delegation administrator. If a parent organizational unit is specified, a list of all accounts that are direct children of the parent will be obtained. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAccount</td>
<td>Updates the specified account information. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CloseAccount</td>
<td>Closes the account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAccount</td>
<td>Query information about the specified account. This operation can only be called by an administrative account of the organization or a member account that is a delegated administrator of a service. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">DelegatedAdministrator</td>
<td>ListDelegatedAdministrators</td>
<td>List accounts designated as delegated administrators in this organization. This operation can only be called by an administrative account of the organization or a member account that is a delegated administrator of a service. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDelegatedServices</td>
<td>List services for which the specified account is a delegated administrator. This operation can only be called by an administrative account of the organization or a member account that is a delegated administrator of a service. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeregisterDelegatedAdministrator</td>
<td>Removes the specified member account as a delegated administrator for the specified service. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RegisterDelegatedAdministrator</td>
<td>Enables the specified member account to manage the organization's features for the specified service. This interface grants the delegated administrator read-only access to the organization's service data. The IAM user in the delegated administrator account still requires IAM permissions to access and manage the service. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Handshake</td>
<td>ShowHandshake</td>
<td>Query information about existing account invitations in the organization. This API can be called by any account in the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListReceivedHandshakes</td>
<td>Lists all invitations received by the account. This operation can be called by any account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeclineHandshake</td>
<td>Reject an invitation request. When the invited account rejects an invitation, the current invitation status is set to rejected, and the invitation is stopped. This API can only be called by the invited account. The initiator of the invitation cannot reactivate a rejected invitation, but can resend a new one. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AcceptHandshake</td>
<td>Sends a response to the initiator of the invitation, accepting the invitation to join the organization. After you accept the invitation, this invitation information will continue to be retained and appear in the return results of related APIs for 30 days. </td>
<td>To be tested</td></tr>
<tr>
<td>ListHandshakes</td>
<td>List invitations sent by the organization. This operation can only be called by an organization management account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelHandshake</td>
<td>Cancel an invitation; the invitation status will be set to canceled. This API can only be called by the account that initiated the invitation. After canceling an invitation, the invitation information will remain and appear in the response results of related APIs for 30 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Misc</td>
<td>ShowEffectivePolicies</td>
<td>Query effective policy information for a specified policy type and account. Currently, this API does not support querying service control policies (service_control_policy). This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServices</td>
<td>Lists all cloud services that can be integrated with the organization's services. After integration, the cloud service becomes a trusted service for the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTagPolicyServices</td>
<td>Lists the resource types that are added to the tag policy enforcement. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQuotas</td>
<td>Lists the organization quotas for the tenant. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEntities</td>
<td>Lists all roots, organizational units, and accounts contained in an organization. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. You can filter entities by specifying the parent ID and child ID parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Organization</td>
<td>ShowOrganization</td>
<td>Query information about the organizations to which an account belongs. This operation can be called by any account in the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>LeaveOrganization</td>
<td>This operation can only be called by an organization's member account. You can leave an organization as a member account only if the organization account has been configured with the information required to operate as a standalone account. The account being left cannot be a delegated administrator account for any service enabled in the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrganization</td>
<td>Create an organization. The account calling this interface will automatically become the administrative account of the new organization. The account credentials used to call this interface must be the credentials of the administrative account of the new organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteOrganization</td>
<td>Delete an organization. You must use an administrative account to delete an organization and first remove all accounts, organizational units, and policies in the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRoots</td>
<td>List the roots of the current organization. This interface can only be called by an administrative account of the organization or a member account that is a delegated administrator of a service. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">OrganizationalUnit</td>
<td>DeleteOrganizationalUnit</td>
<td>Delete an organizational unit from the root or another organizational unit. To do this, you must first remove all member accounts from the organizational unit or move member accounts to other organizational units, and delete all child organizational units from the organizational unit. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOrganizationalUnit</td>
<td>Query information about organizational units. This operation can only be called by an organization's administrative account or a member account that is a service delegate administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrganizationalUnit</td>
<td>Create an organizational unit in the root or parent organizational unit. An organizational unit is a container for accounts, allowing you to group and manage accounts and apply policies based on business requirements. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOrganizationalUnits</td>
<td>Lists all organizational units in the organization. If a parent organizational unit is specified, a list of the parent's direct descendants will be obtained. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateOrganizationalUnit</td>
<td>Renames the specified organizational unit. After the rename, the organizational unit ID remains unchanged, its child organizational units and accounts remain unchanged, and the policies bound to the organizational unit remain unchanged. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">Policy</td>
<td>ListPolicies</td>
<td>Lists all policies in the organization. If a resource ID, such as an organizational unit ID or account ID, is specified, a list of policies bound to that resource will be retrieved. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePolicy</td>
<td>Creates a policy of the specified type. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPolicy</td>
<td>Retrieves information about a policy. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePolicy</td>
<td>Deletes the specified policy from the organization. Before performing this operation, the policy must be unbound from all organizational units, roots, and accounts. This operation can only be called by an administrative account of the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePolicy</td>
<td>Updates a policy. You can update the policy's name, description, or content. If no parameters are provided, the policy remains unchanged. You cannot change the policy's type. This operation can only be called by an administrative account of the organization. </td>
<td>To be tested</td></tr>
<tr>
<td>DisablePolicyType</td>
<td>Disables a policy type in a root. You can bind policies of that type to entities in a root only if policies of that type are enabled in the root. After performing this operation, you can no longer bind policies of the specified type to the root or any organizational units or accounts within it. This is an asynchronous request that is executed in the background. You can use ListRoots to view the status of the policy type for the specified root. This operation can only be called by an administrative account of the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>EnablePolicyType</td>
<td>Enables a policy type in a root. After enabling a policy type in a root, you can bind policies of that type to the root or any organizational units and accounts within it. This is an asynchronous request that is executed in the background. You can use ListRoots to view the status of the policy type for the specified root. This operation can only be called by an administrative account of the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DetachPolicy</td>
<td>Detach a policy from a root, organizational unit, or account. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AttachPolicy</td>
<td>Attach a policy to a root, organizational unit, or individual account. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEntitiesForPolicy</td>
<td>List all roots, organizational units, and accounts bound to the specified policy. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Tag</td>
<td>ListResourceInstances</td>
<td>Query the instance list based on resource type and tag information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>TagResource</td>
<td>Add one or more tags to the specified resource. Currently, you can attach tags to accounts, organizational units, roots, and policies in an organization. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowResourceInstancesCount</td>
<td>Query the number of instances based on resource type and tag information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UntagResource</td>
<td>Removes any tags with the specified primary key from the specified resource. You can bind tags to accounts, organizational units, roots, and policies in an organization. This operation can only be called by an administrative account in the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTagsForResource</td>
<td>Lists tags bound to the specified resource. You can attach tags to accounts, organizational units, roots, and policies in an organization. This operation can only be called by an administrative account in the organization or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTagResources</td>
<td>Lists tags bound to the specified resource type. You can attach tags to accounts, organizational units, roots, and policies in an organization. This operation can only be called by an organization's administrative account or a member account that is a delegated service administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTagResource</td>
<td>Deletes any tags with the specified primary key from the specified resource type. You can attach tags to accounts, organizational units, roots, and policies in an organization. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTagResource</td>
<td>Adds one or more tags to the specified resource type. Currently, you can attach tags to accounts, organizational units, roots, and policies in an organization. This operation can only be called by an organization's administrative account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListResourceTags</td>
<td>Query resource tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">TrustedService</td>
<td>EnableTrustedService</td>
<td>Enables the integration of the service (specified by service_principal) with the organization. Enabling a trusted service allows the specified trusted service to create service-linked delegations for all accounts in the organization. This allows the trusted service to perform operations on your behalf within the organization and its accounts. This interface can only be called by administrative accounts in the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DisableTrustedService</td>
<td>Disables the integration of the service (specified by service_principal) with the organization. Disabling a trusted service prevents the specified service from creating service-linked delegations for new accounts in the organization. This means the service cannot perform operations on your behalf for any new accounts in the organization. The service can still perform operations in old accounts until it is removed from the organization. This interface can only be called by administrative accounts in the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTrustedServices</td>
<td>Returns a list of trusted services enabled for integration with the organization. This operation can only be called by an administrative account of the organization or a member account that is a delegated administrator of the service. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>