# WorkspaceApp MCP Server 


## Version
v0.1.0

## Overview

WorkspaceApp MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service WorkspaceApp. Full-chain management of WorkspaceApp resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="8">AppWareHouse</td>
                    <td>DeleteWarehouseApp</td>
                    <td>删除应用仓库中的指定应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AuthorizeObs</td>
                    <td>获取上传至OBS桶的临时ak/sk。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWarehouseApp</td>
                    <td>在应用仓库中新增应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBucketOrAcl</td>
                    <td>添加桶或者桶授权。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWarehouseApps</td>
                    <td>查询租户应用仓库中的应用列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWarehouseApp</td>
                    <td>修改应用仓库中的指定应用信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadWarehouseAppIcon</td>
                    <td>在应用仓库中上传图标文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteWarehouseApp</td>
                    <td>批量删除应用仓库中的指定应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">Application</td>
                    <td>DeleteAppIcon</td>
                    <td>删除自定义应用应用图标,恢复使用默认应用图标,重复执行会按照成功处理(响应200)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadAppIcon</td>
                    <td>修改自定义应用图标。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchEnableApp</td>
                    <td>批量启用应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublishedApp</td>
                    <td>查询已发布的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPublishableApp</td>
                    <td>查询应用组下可发布的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishApp</td>
                    <td>批量发布应用,不允许发布同名的应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateApp</td>
                    <td>编辑修改应用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDisableApp</td>
                    <td>批量禁用应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppDetail</td>
                    <td>查询应用详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnpublishApp</td>
                    <td>批量取消应用发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">ApplicationConfig</td>
                    <td>InitializeTenant</td>
                    <td>租户服务激活。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTenantProfile</td>
                    <td>查询租户信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListCorpConfigInfo</td>
                    <td>配置加载顺序: 查询企业级配置--&gt; 查不到则赋默认阿波罗配置--&gt; 阿波罗没有则不返回。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">ApplicationGroup</td>
                    <td>CreateAppGroup</td>
                    <td>该API用于创建应用组。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAppGroupDetail</td>
                    <td>查询应用组详情。</td>
                    <td>To be tested</td>
                </tr>
     <tr>
<td>ListAppGroup</td>
<td>Query user-created app groups, paginated by name and authorization type. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAppGroup</td>
<td>Modify an app group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAppGroup</td>
<td>Delete the specified app group. Repeated execution will be treated as successful (response 200). </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteAppGroup</td>
<td>Delete app groups in batches. Repeated execution will be treated as successful (response 200). </td>
<td>To be tested</td>
</tr>
<tr>
<td>DisassociateAppGroup</td>
<td>Disassociate all application groups from the service group. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">ApplicationOrder</td>
<td>CreateOrder</td>
<td>Create an order. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">ApplicationProduct</td>
<td>ListProduct</td>
<td>Query cloud application packages and filter by conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSessionTypes</td>
<td>This interface is used to query the list of session packages. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSessionType</td>
<td>This interface is used to query the list of session packages. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Authorization</td>
<td>BatchDeleteAppGroupAuthorization</td>
<td>Removes the authorization of a specified user within an application group. After the user authorization is deleted, the user will no longer have access to any applications within the application group. Note: Repeating the operation will result in the same successful operation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppGroupAuthorization</td>
<td>Query the list of authorized users within the application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddAppGroupAuthorization</td>
<td>Add user authorization to an application group. After authorization, the user gains access to all published applications under the application group. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">AvailabilityZone</td>
<td>ListAz</td>
<td>This interface is used to query the list of supported availability zones, categorized by site. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAvailabilityZone</td>
<td>This interface is used to query the list of supported availability zones. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">ImageServer</td>
<td>CreateImageServer</td>
<td>Create an image instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RecreateServerImage</td>
<td>Build a cloud application image. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowImageServer</td>
<td>Query the specified image instance. The query data for this interface is consistent with the list query. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteImageServer</td>
<td>Batch delete image instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLatestAttachedServerApp</td>
<td>Query the list of recently distributed software. Returns a list of IDs, not specific information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListImageServers</td>
<td>Query the list of image instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateImageServer</td>
<td>Modify the image instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AttachImageServerApp</td>
<td>Distribute application software information to the image instance. Administrators can download and install the application software on demand. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Job</td>
<td>ShowJob</td>
<td>Query the execution status of the job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListImageSubJobs</td>
<td>This interface is used to query the execution status of asynchronous subtasks. Offset and limit will not take effect when sub_job_ids is not empty. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteAppSubJobs</td>
<td>Batch deletes subtasks, ignoring non-existent servers and returning a successful response. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListImageJobs</td>
<td>This interface is used to query the execution status of a tenant's asynchronous tasks.<td>To be tested</td>
</tr>
<tr>
<td>CountSubJobs</td>
<td>This interface is used to query the number of asynchronous subtasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowJobDetail</td>
<td>Query the execution status of a job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSubJobs</td>
<td>This interface is used to query the execution status of asynchronous subtasks. Offset and limit will not take effect if sub_job_ids is not empty. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowImageJob</td>
<td>This interface is used to query the execution status of asynchronous tasks, such as querying the execution status of the image instance creation task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteImageSubJobs</td>
<td>Batch delete subtasks, ignoring non-existent servers and returning a successful response. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Mail</td>
<td>ListAuthorizationMailRecord</td>
<td>Query the application group authorization email sending records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendAuthorizationMail</td>
<td>Resend the application group authorization email (based on the authorization email record). </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendAuthorizedMail</td>
<td>Resends the application group authorization email (based on the authorization record). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="14">Persistent</td>
<td>CreateShareFolder</td>
<td>Create a shared storage directory. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSfs3Storage</td>
<td>Query SFS3.0 storage. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePersistentStorage</td>
<td>Create WKS storage. Currently, only SFS3.0 capacity-based file systems are supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeletePersistentStorage</td>
<td>Delete WKS storage. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePersistentStorage</td>
<td>Deleting shared storage will only disassociate the NAS from the file system; the file system and its data will not be deleted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrUpdateStoragePolicyStatement</td>
<td>Add or update a custom policy for storage directory access permissions (if a custom policy already exists, the existing policy will be updated). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPersistentStorage</td>
<td>Query WKS storage. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListShareFolder</td>
<td>Query shared storage directories. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteUserStorageAttachment</td>
<td>Delete a personal storage directory. The data in the personal storage directory will also be permanently deleted and cannot be recovered. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateShareFolderAssignment</td>
<td>Add or remove shared directory members in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStorageAssignment</td>
<td>Query personal storage directories. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStorageClaim</td>
<td>Delete a shared storage directory. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStoragePolicyStatement</td>
<td>Query the storage directory access permission policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUserFolderAssignment</td>
<td>Create a personal storage directory. If the corresponding directory already exists, simply updating the policy will not create a duplicate directory. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="13">PolicyGroup</td>
<td>UpdatePolicyTemplate</td>
<td>Modify the information of the specified policy template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePolicyTemplate</td>
<td>Add a new policy template. After creating a policy template, users can adjust the configuration based on the existing policy template when creating a policy group, quickly completing the creation of the policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyGroup</td>
<td>Query the policy group summary information, including the application objects and detailed policy items. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePolicyGroup</td>
<td>Deletes the specified policy group, including the policy information and application targets for the policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePolicyGroup</td>
<td>Modifies the information of the specified policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyOfPolicyGroup</td>
<td>Query the policy items within the specified policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePolicyTemplate</td>
<td>Deletes the specified policy template, including the policy information and application targets for the policy template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePolicyGroup</td>
<td>Create a new policy group. This policy group allows for flexible control of client access and policies, such as file, clipboard, and session access. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTargetsOfPolicyGroup</td>
<td>Query the objects to which a specified policy group applies. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyGroupDetailInfo</td>
<td>Contains policy information and applicable object information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPolicyGroup</td>
<td>Query detailed information about a policy group based on its ID, including policy information and applicable object information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyTemplate</td>
<td>Query the policy template summary information list, including policy information and application object information. When creating a policy group, users can adjust the configuration based on existing policy templates as needed to quickly complete the policy group creation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOriginalPolicyInfo</td>
<td>Query the initial policy item. The initial policy item is the default configuration for all protocol policy configuration items. Users can modify the specified configuration based on the initial policy item to create a new policy group. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Quota</td>
<td>CheckQuota</td>
<td>Quota verification. Before purchasing a server, you can call this API to verify whether the resources for the server you are creating are sufficient. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">ScalingPolicy</td>
<td>CreateOrUpdateScalingPolicy</td>
<td>Add/modify an elastic scaling policy. Only supported for on-demand servers. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteScalingPolicy</td>
<td>Delete an elastic scaling policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowScalingPolicy</td>
<td>Query the server group's auto-scaling policy. If no policy is configured for the server, the default policy will be used. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">ScheduleTask</td>
<td>ListScheduleTasks</td>
<td>Query the list of scheduled tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateScheduleTask</td>
<td>Modify a scheduled task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateScheduleTask</td>
<td>Add a new scheduled task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFutureExecutions</td>
<td>List of future execution times. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteScheduleTask</td>
<td>Delete a task, ignoring non-existent tasks and returning a successful response. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTaskExecuteDetail</td>
<td>Query the list of scheduled task execution subtasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteScheduleTask</td>
<td>Delete scheduled tasks in batches, ignoring non-existent server groups and returning a successful response. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowScheduleTask</td>
<td>Query the details of a specified scheduled task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTaskExecuteHistory</td>
<td>Query the scheduled task execution list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="25">Server</td>
<td>BatchUpgradeHdaVersion</td>
<td>Batch upgrade server HDA versions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServerHdaDetails</td>
<td>Query the server's HDA-related information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServerMetricData</td>
<td>Query monitoring data of a specified metric and a specified granularity within a specified time range. Parameters can be used to specify the data dimension to be queried. </td>
<td>To be tested</td>
</tr><tr>
<td>BatchStartServer</td>
<td>Starts a server. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteServer</td>
<td>Deletes a server, ignoring non-existent servers and returning a successful response. Called after an order is successfully canceled. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateServer</td>
<td>Modifies a server. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServer</td>
<td>Query the specified server. The query data for this interface is consistent with the list query data. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteServer</td>
<td>Delete servers in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateTsvi</td>
<td>Updates server virtual session IP configurations in batches, restarting servers as needed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServerHdaUpgradeRecords</td>
<td>Query the server's HDA upgrade tracking records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServers</td>
<td>Query the server list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRejoinDomain</td>
<td>Rejoins servers to the AD domain in batches. This is generally used to resolve server domain disconnections. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeServerImage</td>
<td>Change the server image. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAppServers</td>
<td>Create the cloud server interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchMigrateHostsServer</td>
<td>Migrate the servers under the cloud office host to the target cloud office host. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccessAgentLatestVersion</td>
<td>Query the latest version of all HDAs for the tenant. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRebootServer</td>
<td>Restart the server. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchChangeServerImage</td>
<td>Batch change the server image. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServerVnc</td>
<td>Get the VNC remote login address. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAccessAgentLatestVersion</td>
<td>Query the latest version of the tenant's HDA. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchStopServer</td>
<td>Shut down the server. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchReinstallServer</td>
<td>Reinstall servers in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServerMetricData</td>
<td>This interface can retrieve data (such as CPU usage, memory usage, user online time, etc.) for a specific computer over a period of time (range: 1 hour to 30 days). The maximum data retention period cannot exceed 180 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ReinstallServer</td>
<td>Reinstall the server. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchChangeServerMaintainMode</td>
<td>Marks the server in maintenance mode. Servers in maintenance mode will no longer be allocated traffic. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">ServerGroup</td>
<td>ShowServerGroupState</td>
<td>Query the status of servers in the specified server group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateServerGroup</td>
<td>Create a server group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateServerGroup</td>
<td>Modify a server group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTenantServerGroups</td>
<td>Query the basic information list of tenant server groups (used to bind server groups when creating application groups). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServerGroup</td>
<td>Query the specified server group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServerGroups</td>
<td>Query the server group list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteServerGroups</td>
<td>Delete a server group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServerGroupRestrict</td>
<td>Specify tenant server group restriction query. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Session</td>
<td>ListUserConnection</td>
<td>Query user login records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>LogoffUserSession</td>
<td>Log off a user session. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSessions</td>
<td>Query the user session list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppConnection</td>
<td>Query the application usage history. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSessionByUserName</td>
<td>Query the current session by username. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Tag</td>
<td>BatchDeleteServerGroupTags</td>
<td>This interface is idempotent:</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteServerGroupTags</td>
<td>This interface is idempotent:</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServerGroupTag</td>
<td>Query the tag information of a specified server group</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateServerGroupTags</td>
<td>This interface is idempotent:</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateServerGroupTags</td>
<td>This interface is idempotent:</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServerGroupTag</td>
<td>Query the set of resource tags for all server groups of a tenant.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">VolumeType</td>
<td>ListVolumeType</td>
<td>This interface is used to query available disk types.</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>