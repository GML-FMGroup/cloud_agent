# Workspace MCP Server


## Version
v0.1.0

## Overview

Workspace MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Workspace. Full-chain management of Workspace resources can be carried out based on natural language.

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
<td rowspan="2">AccessConfig</td> 
<td>ListAccessAddressBackupConfig</td> <td>This interface is used to obtain the backup configuration of the cloud office service access address. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAccessAddressBackupConfig</td>
<td>This interface is used to modify the backup configuration of the cloud office service access address. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">AccessPolicy</td>
<td>CreateAccessPolicy</td>
<td>This interface is used to create an access policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccessPolicies</td>
<td>This interface is used to query access policies. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAccessPolicyObjects</td>
<td>This interface is used to update the application objects of a specified access policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteAccessPolicies</td>
<td>This interface is used to delete the specified access policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAccessPolicy</td>
<td>This interface is used to update the specified access policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccessPolicyObjects</td>
<td>This interface is used to query the application objects of a specified access policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Agency</td>
<td>ListAgencies</td>
<td>Query the delegation function. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAgencies</td>
<td>Activate the delegation function. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Alarms</td>
<td>ListAlarmStatistics</td>
<td>Return the number of alarms of each severity. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAlarms</td>
<td>Query the alarm list from CES. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="18">AppCenter</td>
<td>ListJobs</td>
<td>Query application installation job information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateAppAuthorizations</td>
<td>Set application authorizations in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAppAuthorizations</td>
<td>Set application authorizations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApps</td>
<td>Query applications by name in a paginated manner. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDisableApps</td>
<td>Batch settings are not visible. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUploadedApp</td>
<td>Modify the app. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchEnableApps</td>
<td>Batch settings are visible. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadApp</td>
<td>Add an app. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApp</td>
<td>Delete the app. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RetryJobs</td>
<td>Retry specified failed jobs (only failed jobs are retried; retrying other types of jobs will result in an error response). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppAuthorizations</td>
<td>Query application authorization information. </td>
<td>To be tested</td></tr>
<tr>
<td>CreateBucketCredential</td>
<td>Generate bucket credential information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteApps</td>
<td>Batch delete applications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchInstallApps</td>
<td>Automatically install applications in batches (applications must support silent installation or unzip installation). </td>
<td>To be tested</td>
</tr>
<tr>
<td>InstallApp</td>
<td>Automatically install applications (applications must support silent installation or unzip installation). </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteJobs</td>
<td>Batch delete jobs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAndAuthorizeBucket</td>
<td>Add and authorize a default bucket. If the bucket does not exist, an OBS bucket will be automatically created. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppCatalogs</td>
<td>Query application category information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">AppRule</td>
<td>EnableRuleRestriction</td>
<td>Enable rule control. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRestrictedRule</td>
<td>Query the list of control rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAppRule</td>
<td>Modify the application rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAppRule</td>
<td>Create the application rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppRule</td>
<td>Query the list of control rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetRuleRestriction</td>
<td>Set the control rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAppRule</td>
<td>Delete application rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteAppRules</td>
<td>Delete rules in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRestrictedRule</td>
<td>Delete control rules in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRuleRestriction</td>
<td>Query control rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddRestrictedRule</td>
<td>Add a control rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DisableRuleRestriction</td>
<td>Disable rule control. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">AuthConfig</td>
<td>ShowAuthConfig</td>
<td>Query authentication login method configuration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAssistAuthConfig</td>
<td>Query auxiliary authentication configuration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAssistAuthMethodConfig</td>
<td>Update the auxiliary authentication policy configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAuthMethodConfig</td>
<td>Update the authentication policy configuration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">AvailabilityZone</td>
<td>ListAzs</td>
<td>This interface is used to query the list of available zones supported by the cloud desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAzDetails</td>
<td>This interface is used to query the list of available zones supported by the cloud desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAvailabilityZones</td>
<td>This interface is used to query the list of available zones supported by the cloud desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Connection</td>
<td>ExportUserLoginInfoNew</td>
<td>This interface is used to export connection records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLoginRecordsNew</td><td>This interface is used to query login information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHistoryOnlineInfoNew</td>
<td>This interface is used to query the number of logged-in users. Note that the query parameters cannot be empty. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstancesStatus</td>
<td>This interface is used to query the desktop login status. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="37">Desktop</td>
<td>CancelRemoteAssistance</td>
<td>Cancel remote assistance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeDesktopToImage</td>
<td>Change the desktop to an image. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResizeDesktop</td>
<td>Changes cloud desktop specifications. Only CPU and memory changes are supported. Disk changes are not supported. Changing between the same specifications is not supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RegisterDomain</td>
<td>This interface is used to rejoin a Windows desktop to an AD domain. It is generally used to resolve desktop disconnections. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopsDetail</td>
<td>Query a list of desktop details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchChangeDesktopNetwork</td>
<td>Batch changes desktop VPCs, subnets, IP addresses, and security groups. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchInstallAgent</td>
<td>Install the agent for desktops in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AttachInstances</td>
<td>Assign desktops to users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchLogoffDesktops</td>
<td>Log off desktops in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteDesktops</td>
<td>Delete desktops in batches. Deleted desktops cannot be restored. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopsConnectStatus</td>
<td>Query the desktop connection status list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRemoteConsoleAddress</td>
<td>Used to directly obtain the remote login console address. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDesktopNetworks</td>
<td>Query the desktop VPC, subnet, privateIP, EIP, and security group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAgentsInstallCondition</td>
<td>Display desktop installation agent details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeUserPrivilegeGroup</td>
<td>Batch modify user privilege groups. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDetachInstances</td>
<td>Batch detach desktops from users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesktop</td>
<td>Modify desktop properties. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetMaintenanceMode</td>
<td>Batch set desktop administrator maintenance mode. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRemoteAssistance</td>
<td>Create remote assistance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDesktopMonitorData</td>
<td>This interface can retrieve data (such as CPU usage, memory usage, user online time periods, etc.) for a specific computer over a period of time (range: 1 hour to 30 days). The maximum data retention period cannot exceed 180 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRebuildDesktopsSystemDisk</td>
<td>Rebuild desktop system disks in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesktopUsername</td>
<td>In AD scenarios, desktops can be associated with new usernames. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDesktopNetwork</td>
<td>Query a desktop's VPC, subnet, privateIP, EIP, and security group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDesktopDetail</td>
<td>Specify a desktop ID to query detailed information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesktop</td>
<td>Create a desktop and assign it to a user. After the desktop is successfully created, the user can log in and use it. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopActions</td>
<td>Get desktop startup and shutdown information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRunDesktops</td>
<td>Batch desktop operations, including startup, shutdown, hibernation, and restart. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDesktop</td>
<td>Delete a single desktop. Once deleted, it cannot be restored. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDesktopRemoteAssistanceInfo</td>
<td>Query remote assistance information based on the desktop ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchAssociateInstances</td>
<td>Pre-batch assign desktops to users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeDesktopNetwork</td>
<td>Change desktop VPC, subnet, IP address, and security group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSysprepInfo</td>
<td>Query Sysprep version information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesktopSids</td>
<td>This interface is used to update the desktop SID to make it consistent with the SID in Windows AD when the desktop SID is different from the SID in Windows AD. It is generally used to resolve desktop delocalization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DetachInstances</td>
<td>Detach a desktop from a user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchAttachInstances</td>
<td>Batch assign desktops to users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendNotifications</td>
<td>Used by the administrator to send notification messages to desktops. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktops</td>
<td>This interface is used to query the desktop virtual machine list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">DesktopNamePolicy</td>
<td>CreateDesktopNamePolicy</td>
<td>Create a desktop name policy for automatically generating desktop names. A maximum of 50 names are allowed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteDesktopNamePolicy</td>
<td>Batch delete desktop name policies. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopNamePolicy</td>
<td>Get the desktop name policy, used for automatically generating desktop names. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesktopNamePolicy</td>
<td>Update the desktop name policy, used for automatically generating desktop names. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="18">DesktopPool</td>
<td>ResizeDesktopPool</td>
<td>Change the desktop pool specifications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopPoolAuthorizedObjects</td>
<td>This interface is used to query the authorized users and user groups of a specified desktop pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPoolDesktopsDetail</td>
<td>This interface is used to query desktop information under a desktop pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDesktopPoolVolumes</td>
<td>Add disks to a desktop pool in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteDesktopPoolAction</td>
<td>Operate desktop pools, used to batch power on, shut down, restart, and hibernate desktops within the desktop pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteDesktopPoolScript</td>
<td>Execute scripts in batches within desktop pools. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesktopPool</td>
<td>Create a desktop pool. This desktop pool can be assigned to users or user groups. When a user logs in, one of the desktops will be bound to the pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RebuildDesktopPool</td>
<td>Rebuild the system disk for the desktop pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDesktopPool</td>
<td>When there are no desktops in the desktop pool, you can delete the desktop pool. Once deleted, the desktop pool cannot be restored. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendDesktopPoolNotifications</td>
<td>Used by the administrator to send notification messages to desktops. </td>
<td>To be tested</td></tr>
<tr>
<td>DeleteDesktopPoolVolumes</td>
<td>Deletes disks from a desktop pool in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesktopPool</td>
<td>Modifies desktop pool properties. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDesktopPoolsScriptExecTasks</td>
<td>Lists script execution tasks for the desktop pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDesktopPoolDetail</td>
<td>Specifies the desktop pool ID to query detailed information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesktopPoolAuthorizedObjects</td>
<td>This interface is used to authorize users and user groups to a desktop pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExpandDesktopPool</td>
<td>Expand the desktop pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExpandDesktopPoolVolumes</td>
<td>Expand the desktop pool's disk capacity in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopPools</td>
<td>This interface is used to query the desktop pool list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">DesktopTag</td>
<td>BatchChangeTags</td>
<td>Batch add or remove tags for specified desktops. When creating, if the created tag already exists (same key), it will be overwritten. When deleting, if the deleted tag does not exist, the default process is successful. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchAddDesktopsTags</td>
<td>Batch add tags to multiple desktops simultaneously. If the created tag already exists (same key), it will be overwritten. Supports up to 100 desktops, with a maximum of 20 tags per desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTag</td>
<td>This interface is used to create a tag for a desktop. A desktop can have up to 10 tags. During creation, if the tag already exists (with the same key), it will be overwritten. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTagByDesktopId</td>
<td>Query the tag information of a specified desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListProjectTags</td>
<td>Query all tags in a tenant. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTag</td>
<td>This interface is used to delete a desktop tag. When deleting, if the tag to be deleted does not exist, the default process succeeds. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteDesktopsTags</td>
<td>Add tags to multiple desktops simultaneously. When deleting, if the tag to be deleted does not exist, the default process succeeds. Supports up to 100 desktops, with a maximum of 20 tags per desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopByTags</td>
<td>Filter desktops by tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Group</td>
<td>DeleteUserGroup</td>
<td>Delete a user group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteUserGroups</td>
<td>This interface is used to delete user groups in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUserGroup</td>
<td>This interface is used to modify user group information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RunActionsOnGroup</td>
<td>Operate on user groups, such as adding and deleting users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserGroups</td>
<td>Query the user group list, supports paging. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateUserGroup</td>
<td>This interface is used to create a user group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUsersOfGroup</td>
<td>This interface is used to query the users in a user group. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Image</td>
<td>ListImages</td>
<td>This interface is used to query the list of product images supported by the cloud desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Images</td>
<td>ListMarketImages</td>
<td>Get the list of cloud market images. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Inquiry</td>
<td>EstimateChangeImages</td>
<td>Inquiry for batch package periodic desktop image switching (changing from free image to paid image). </td>
<td>To be tested/td>
</tr>
<tr>
<td>EstimateDesktopPoolAddVolume</td>
<td>Inquire for bulk pricing for adding a single disk to a periodic desktop pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>EstimateAddResources</td>
<td>Inquire for bulk pricing for adding and changing periodic desktop configurations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>EstimateDesktopPoolChangeImage</td>
<td>Inquire for bulk pricing for switching image sizes (from a free image to a paid image) for periodic desktop pools. </td>
<td>To be tested</td>
</tr>
<tr>
<td>EstimateDesktopPoolExtendVolume</td>
<td>Inquire for bulk pricing for expanding disks in periodic desktop pools. </td>
<td>To be tested</td>
</tr>
<tr>
<td>EstimateDesktopPoolResize</td>
<td>Request a quote for changing the specifications of a desktop pool for a specific period. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Job</td>
<td>RunActionsOnWorkspaceJob</td>
<td>This interface is used to retry failed tasks. Currently, only account opening and account cancellation tasks are supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Jobs</td>
<td>ShowJob</td>
<td>This interface is used to query the execution status of asynchronous tasks, such as the execution status of the create desktop task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteSubJobs</td>
<td>This interface is used to delete subtasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListItaSubJobs</td>
<td>This interface is used to query the execution status of asynchronous tasks, such as the execution status of desktop creation. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">NatMappingConfigs</td>
<td>UpdateNatMappingConfigs</td>
<td>Modify the tenant's NAT mapping configuration items. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNatMappingConfigs</td>
<td>Query the tenant's NAT mapping configuration items. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="15">Network</td>
<td>ListPorts</td>
<td>Query the port list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AssociateDesktopsEip</td>
<td>Associate a desktop with an EIP. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ApplySubnetBandwidth</td>
<td>Create on-demand cloud office bandwidth. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopsEips</td>
<td>Query bound desktops and unbound EIPs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSubnetBandwidthControlList</td>
<td>Modify the cloud office bandwidth control configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowUsingSubnets</td>
<td>Query the subnet IDs currently in use by the desktop based on the subnet ID list and return the subnet ID list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInternet</td>
<td>Query the Internet access function. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ApplyInternet</td>
<td>Enable the Internet access function. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNatGateways</td>
<td>Query the NAT gateway list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDisassociateDesktopsEip</td>
<td>Batch disassociate desktops from EIPs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSubnetBandwidths</td>
<td>Query the cloud office bandwidth list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ApplyDesktopsInternet</td>
<td>Enable desktop Internet access. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSubnetBandwidth</td>
<td>Modify the cloud office bandwidth. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSubnetBandwidth</td>
<td>Delete the cloud office bandwidth. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSubnetBandwidthControlList</td>
<td>Query the cloud office bandwidth control configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Order</td><td>CreateSubnetBandwidthChangeOrder</td>
<td>Place an order for periodic cloud office bandwidth changes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrder</td>
<td>Place an order for periodic resources (desktops, disks). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateChangeOrder</td>
<td>Change specifications and expand disk capacity. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesktopBatchOrder</td>
<td>Place a periodic desktop batch change order. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesktopOrder</td>
<td>Create a desktop order. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesktopPoolChangeOrder</td>
<td>Place a batch change order for desktop pools for a periodic period. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Ou</td>
<td>ListOuDetails</td>
<td>Query the OU list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateOuInfo</td>
<td>Update OU information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAdOus</td>
<td>Query the OU list in AD. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddOu</td>
<td>This interface is used to create an OU. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAdOuUsers</td>
<td>Query user information under an OU. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteOu</td>
<td>This interface is used to delete OU information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="11">PolicyGroup</td>
<td>BatchUpdateTargetOfPolicyGroup</td>
<td>Add or delete application objects to a specified policy group in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTargetOfPolicyGroup</td>
<td>Query the objects to which a specified policy group applies. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyDetailInfoById</td>
<td>Query detailed information about a policy group by its ID, including policy information and applicable object information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePoliciesOfPolicyGroup</td>
<td>Modify some or all policy items in a policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyGroupInfo</td>
<td>Contains policy information and applicable object information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyGroup</td>
<td>Query the policy group summary information list, excluding policy information and application object information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePolicyGroup</td>
<td>Delete the specified policy group, including the corresponding policy information and application object information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPoliciesOfPolicyGroup</td>
<td>Query the policy items within the specified policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePolicyGroup</td>
<td>Modify the information of the specified policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePolicyGroup</td>
<td>Create a new policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOriginalPolicyInfo</td>
<td>Query the initial policy item. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Product</td>
<td>ListProducts</td>
<td>This interface is used to query the list of product packages supported by the cloud desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSharerProducts</td>
<td>This interface is used to query the list of shared packages. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHourPackagesType</td>
<td>This interface is used to query the types of hourly packages that can be ordered. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Profile</td>
<td>UpdateTenantProfile</td>
<td>Enable or disable tenant functionality. </td>
<td>To be tested</td>
</tr>
<tr><td>ListTenantProfiles</td>
<td>Query tenant feature status. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Quota</td>
<td>ShowQuotaDetails</td>
<td>Query tenant single site quota details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowQuotas</td>
<td>Console Framework and WKSDesktopManager call this interface to query tenant quotas. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">ScheduledTask</td>
<td>CreateScheduledTasks</td>
<td>Create scheduled tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScheduledTasksRecords</td>
<td>Query scheduled task execution records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowScheduledTasks</td>
<td>Query scheduled task details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScheduledTasks</td>
<td>Query the scheduled task list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteScheduledTasks</td>
<td>Delete a scheduled task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteScheduledTasks</td>
<td>Batch delete scheduled tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateScheduledTasks</td>
<td>Modify scheduled tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTimeZones</td>
<td>Get time zone configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFutureExecutions</td>
<td>A list of future execution times. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScheduledTasksRecordsDetails</td>
<td>Query the details of scheduled task execution records. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">ScreenRecord</td>
<td>BatchDeleteScreenRecords</td>
<td>Batch delete screen recording records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopOperations</td>
<td>Query the list of desktop key events. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDownloadAddress</td>
<td>Query the list of download addresses. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScreenRecords</td>
<td>Query the screen recording record list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowScreenRecord</td>
<td>Query the screen recording details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="11">Script</td>
<td>ShowScriptRecordDetail</td>
<td>Query the script execution record details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateScript</td>
<td>Update the script. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScriptRecords</td>
<td>Query the script execution record list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateScript</td>
<td>Create a new script. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RetryScriptExecution</td>
<td>Retry a script or execute a failed script. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopScriptExecution</td>
<td>Stop a script or command execution task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteScript</td>
<td>Delete the script. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowScriptDetail</td>
<td>Query script details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScriptTasks</td>
<td>Query the script task list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScripts</td>
<td>Query the script list. </td>
<td>To be testedd</td>
</tr>
<tr>
<td>ExecuteScriptOrCommand</td>
<td>Execute scripts or commands in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">ShareDesktop</td>
<td>DeleteDesktopSubResources</td>
<td>Delete desktop subresources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDesktopSubResources</td>
<td>Purchase subresources for existing desktops. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">ShareSpaceConfig</td>
<td>UpdateShareSpaceConfig</td>
<td>Set the default user configuration for the collaborative desktop (this feature is currently in beta testing. Please contact your administrator to request access). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowShareSpaceConfig</td>
<td>Query the default user configuration for the collaborative desktop (this feature is currently in beta testing. Please contact your administrator to request access). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Site</td>
<td>UpdateAccessMode</td>
<td>Used to modify the site access mode. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWksEdgeSites</td>
<td>Query the list of edge sites. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSite</td>
<td>Interface for deleting a site. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddSite</td>
<td>Interface for querying site information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSiteConfigs</td>
<td>Interface for querying site information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSubnetIds</td>
<td>Used to modify the site's service subnet. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Snapshot</td>
<td>ListDesktopSnapshot</td>
<td>Query the snapshot list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRestoreDesktopSnapshot</td>
<td>Restore snapshots in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteDesktopSnapshot</td>
<td>Delete snapshots in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateDesktopSnapshot</td>
<td>Create snapshots in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="17">Statistics</td>
<td>ListMetricNotifyRecord</td>
<td>Query whether there are records that meet the notification rules for the corresponding metric dimension; </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGrowthRate</td>
<td>Query the month-over-month value of the metric. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopsStatistics</td>
<td>Counts the status of common desktops and desktop pools under a tenant. By default, only the total number is counted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppUserAccessData</td>
<td>Query cloud application access statistics. Query data for up to 30 days at a time, including the most recent 30 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMetrics</td>
<td>Query metrics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRunState</td>
<td>Tenant desktop run state statistics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMetricNotifyRule</td>
<td>Query the notification rule for the corresponding metric. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowUserAccessStages</td>
<td>Query the duration of each stage of access to a cloud desktop or cloud application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddMetricNotifyRule</td>
<td>Add a notification rule for the corresponding metric; a notification is sent when the corresponding metric meets the corresponding rule conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesktopUsageMetric</td>
<td>Query desktop usage statistics; </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteMetricNotifyRule</td>
<td>Delete a notification rule for the corresponding metric; a notification is sent when the corresponding metric meets the corresponding rule conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLoginState</td>
<td>Query tenant desktop login status statistics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMetricNotifyRule</td>
<td>Updates the notification rule for the corresponding metric; a notification is sent when the corresponding metric meets the corresponding rule conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUnusedDesktops</td>
<td>Query desktops that have not been used in the specified time period. Deprecated and not recommended. For statistics, we recommend using the [Query Desktop Usage Statistics API](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api=ListDesktopUsageMetric) and the [Query User Usage Statistics API](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api=ListUserUsageMetric). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMetricsTrend</td>
<td>Query metric trends. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUsedDesktopInfo</td>
<td>Query the duration of desktop usage. Deprecated and not recommended. For statistics, we recommend using the [Query Desktop Usage Statistics API](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api=ListDesktopUsageMetric) and [Query User Usage Statistics API](https://console.huaweicloud.com/apiexplorer/#/openapi/Workspace/doc?api=ListUserUsageMetric). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserUsageMetric</td>
<td>Query user usage statistics;</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Subnet</td>
<td>ShowAvailableIp</td>
<td>Query available IP addresses under a subnet based on the subnet ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Tenant</td>
<td>ListTenantConfigs</td>
<td>Query the tenant configuration list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTenantConfig</td>
<td>Modify the tenant configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Terminal</td>
<td>DeleteTerminalsBindingDesktops</td>
<td>Delete the terminal and desktop binding configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTerminalsBindingDesktopsConfig</td>
<td>Set the switch configuration for terminal and desktop binding. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTerminalsBindingDesktopsConfig</td>
<td>Query the switch configuration information for terminal and desktop binding. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTerminalsBindingDesktops</td>
<td>Query the terminal and desktop binding configuration list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTerminalsBindingDesktops</td>
<td>Modify the terminal and desktop binding configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTerminalsBindingDesktops</td>
<td>Add terminal and desktop binding configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">User</td>
<td>ListUsers</td>
<td>This interface is used to query the desktop user list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUserInfo</td>
<td>This interface is used to modify desktop user information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteOtpDevices</td>
<td>This interface is used to unbind a user's OTP devices. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendEmail</td>
<td>This API is used to resend an email. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetRandomPassword</td>
<td>This API is used to reset a user's password. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeUserStatus</td>
<td>This API is used to manipulate users and includes three operations: lock, unlock, and reset passwords. (For password resets, it is recommended to use the /v2/{project_id}/users/{user_id}/random-password API. If notification is not available, the /v2/{project_id}/users/{user_id}/random-password API must be used.) </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesktopUser</td>
<td>This interface is used to create a desktop user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserDetail</td>
<td>This interface is used to query the details of a specified desktop user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteUser</td>
<td>Delete a specified desktop user. </td><td>To be tested</td>
</tr>
<tr>
<td>BatchCreateUsers</td>
<td>This interface is used to create users in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteUser</td>
<td>This interface is used to delete desktop users in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOtpDevicesByUserId</td>
<td>This interface is used to query the OTP devices associated with the corresponding user. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">UserEvents</td>
<td>SetUserEventsLtsConfigurations</td>
<td>Configure user event LTS. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserEvents</td>
<td>Query user events, up to 30 days at a time, supporting data queries for the last 30 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserEventsLtsConfigurations</td>
<td>Query user event LTS configurations. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Volume</td>
<td>ListVolumeProductInfo</td>
<td>Query disk product information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDesktopVolumes</td>
<td>Delete desktop data disks. Deletion cannot be restored. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExpandDesktopVolume</td>
<td>Expand the disk. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddVolumes</td>
<td>Add desktop disks in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDesktopVolumes</td>
<td>Add a disk to a single desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExpandVolumes</td>
<td>Expand the desktop disk. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Workspace</td>
<td>CancelWorkspace</td>
<td>This API is used to log out of the Cloud Office service. Before logging out, ensure that the current user's cloud desktop has been deleted; it cannot be restored after logging out. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkspaces</td>
<td>This API is used to query Cloud Office service details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkspace</td>
<td>This API currently supports modifying Cloud Office service properties. Only one property type can be modified in a single request. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkspaceLock</td>
<td>Query whether the Cloud Office service is locked. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ApplyWorkspace</td>
<td>This interface is used to activate the Cloud Office service. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEnterpriseId</td>
<td>Modify the tenant's enterprise ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UnlockWorkspace</td>
<td>This interface currently supports unlocking the Cloud Office service. </td> 
<td>To be tested</td> 
</tr> 
</tbody> 
</table> 
</body>
</html>