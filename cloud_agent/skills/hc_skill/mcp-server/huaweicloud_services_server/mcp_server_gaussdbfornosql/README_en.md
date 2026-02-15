# GaussDBforNoSQL MCP Server


## Version
v0.1.0

## Overview

GaussDBforNoSQL MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service GaussDBforNoSQL. Full-chain management of GaussDBforNoSQL resources can be carried out based on natural language.

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
<td rowspan="1">Task management</td> <td>ListJobs</td>
<td>Query the task list and details. The default query is the task list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Enterprise Project Management</td>
<td>ListEpsQuotas</td>
<td>Query the enterprise project quota. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyEpsQuotas</td>
<td>Modify the enterprise project quota. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="18">Parameter Template Management</td>
<td>UpdateConfiguration</td>
<td>Modify the parameter template parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConfigurationDatastores</td>
<td>Query information about interfaces that support parameter templates</td>
<td>To be tested</td>
</tr>
<tr>
<td>ApplyConfigurationToInstances</td>
<td>Apply a parameter template to instances. You can specify one or more instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CopyConfiguration</td>
<td>Copy a parameter template</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstanceConfiguration</td>
<td>Modify the parameters of a specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConfigurations</td>
<td>Get a list of parameter templates, including default parameter templates for all databases and user-created parameter templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateConfiguration</td>
<td>Create a parameter template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ApplyConfiguration</td>
<td>Apply a parameter template to an instance. You can specify one or more instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteConfiguration</td>
<td>Delete a specified parameter template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstanceConfigurations</td>
<td>Modify the parameters of the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetParamGroupTemplate</td>
<td>Reset the custom parameter template</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceConfiguration</td>
<td>Query the instance parameter configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConfigurationTemplates</td>
<td>Get a list of parameter templates, including the default parameter templates for all databases and user-created parameter templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowConfigurationDetail</td>
<td>Get detailed information about the specified parameter template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApplyHistory</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td>CompareConfiguration</td>
<td>Compare the differences between two parameter templates</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowModifyHistory</td>
<td>Query the modification history of instance parameters</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApplicableInstances</td>
<td>Query the list of instances to which the parameter template can be applied. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="22">Backup and Restore</td>
<td>ShowBackupPolicies</td>
<td>Query automatic backup policies. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteBackup</td>
<td>Delete manual backups</td><td>To be tested</td>
</tr>
<tr>
<td>ShowAllInstancesBackups</td>
<td>Query the backup list based on the specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopBackup</td>
<td>Supports stopping backups in an emergency. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRedisPitrInfo</td>
<td>Query the storage space used by Redis instances for restores at a specified point in time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteManualBackup</td>
<td>Batch delete manual backups of database instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRestoreTime</td>
<td>Query the instance's recoverable time period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRestoreDatabases</td>
<td>Get database information for table-level recovery of a GeminiDB (for Cassandra) instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestoreRedisPitr</td>
<td>Restore the current Redis instance to a specified point in time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRedisPitrPolicy</td>
<td>Query the Redis restore policy to a specified point in time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAllInstancesBackupsNew</td>
<td>Query the backup list based on the specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRestoreTables</td>
<td>Get table information for table-level recovery of a GeminiDB (for Cassandra) instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRedisPitrRestoreTime</td>
<td>Query the Redis restoreable time point. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetBackupPolicy</td>
<td>Set the automatic backup policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestoreExistingInstance</td>
<td>Restore to an existing instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateBack</td>
<td>Create a manual backup. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetRecyclePolicy</td>
<td>Set the number of days to retain deleted instances. Instances deleted after the retention period is changed will be retained for the new number of days. Instances already in the recycle bin before the change remain unchanged. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRecyclePolicy</td>
<td>Query the recycle policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRecycleInstances</td>
<td>Query the list of instances of all engines in the recycle bin. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRestorableList</td>
<td>Query the list of user-restoreable instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBackupPolicy</td>
<td>Query the automatic backup policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetRedisPitrPolicy</td>
<td>Set the Redis restore policy to a specified point in time. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="52">Instance management</td>
<td>UpdatePasswordlessConfig</td>
<td>Supports modifying the password-free configuration of GeminiDB Redis. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDbCacheMappings</td>
<td>Query the list and details of memory acceleration mapping relationships based on specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRedisDisabledCommands</td>
<td>Query Redis disabled commands. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveRedisDisabledCommands</td>
<td>Set Redis disabled commands. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAvailableFlavorInfos</td>
<td>Query the instance's changeable specifications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyPort</td>
<td>Modify the database instance's port. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEnlargeFailNode</td>
<td>Delete the node that failed to enlarge the capacity. </td>
<td>To be tested</td>
</tr>
<tr><td>CheckWeekPassword</td>
<td>Check for weak passwords. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyPublicIp</td>
<td>Bind/unbind an Elastic Public IP address to/from an instance node. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNosqlTaskList</td>
<td>Query a list of scheduled tasks based on specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRedisDisabledCommands</td>
<td>Delete disabled Redis commands. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDbCacheMapping</td>
<td>Create a memory-accelerated mapping. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelInstanceScheduleWindow</td>
<td>Cancel the scheduled task</td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchOver</td>
<td>Switch the instance between the primary and backup nodes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowHighRiskCommands</td>
<td>Query Redis high-risk commands</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpgradeDbVersion</td>
<td>Upgrade the database patch version</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShrinkInstanceNode</td>
<td>Shrink the number of nodes of the specified cluster instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchSecondLevelMonitoring</td>
<td>Turn on or off 5-second level monitoring for the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstance</td>
<td>Delete the database instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetPassword</td>
<td>Change the instance administrator password. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstanceMaintenanceWindow</td>
<td>Query the instance maintenance window. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetAutoEnlargePolicy</td>
<td>Set the disk auto-enlargement policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRedisBigKeys</td>
<td>Supports querying big keys in Redis instances. String keys whose value length exceeds the bigkeys-string-threshold parameter, or hash/list/zset/set/stream keys whose element count exceeds the bigkeys-composite-threshold parameter, are considered big keys. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateHighRiskCommands</td>
<td>Batch modify high-risk commands</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDbCacheRule</td>
<td>Deletes memory acceleration rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDbCacheRules</td>
<td>Query the memory acceleration rule list and details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstances</td>
<td>Query the database instance list and details based on the specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstancesSession</td>
<td>Get the node session list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRedisHotKeys</td>
<td>Supports querying the hot keys of a Redis instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstanceName</td>
<td>Change the instance name</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityGroup</td>
<td>Change the security group associated with the instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpgradeDatabaseVersion</td>
<td>Batch upgrade the database patch version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowIpNumRequirement</td>
<td>Query the number of IP addresses required when creating an instance or scaling a node</td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchSsl</td>
<td>Switch the instance's SSL switch.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyVolume</td>
<td>Change the instance's storage capacity</td>
<td>To be tested</td></tr>
<tr>
<td>ResizeColdVolume</td>
<td>Expand cold data storage. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInstance</td>
<td>Create a database instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResizeInstanceVolume</td>
<td>Expand the instance's storage capacity. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDbCacheMapping</td>
<td>Remove the specified memory acceleration mapping. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExpandInstanceNode</td>
<td>Expand the number of nodes in the specified cluster instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetInstanceDataDump</td>
<td>Turn instance data export on/off. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoEnlargePolicy</td>
<td>Query the disk auto-enlargement policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateColdVolume</td>
<td>‘Create cold data storage’</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecondLevelMonitoringStatus</td>
<td>Query the second-level monitoring configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPasswordlessConfig</td>
<td>Get the password-free configuration for GeminiDB Redis. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDbCacheRule</td>
<td>Create a memory acceleration rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResizeInstance</td>
<td>Change instance specifications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestartInstance</td>
<td>Restart the database service for an instance or node. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyInstanceMaintenanceWindow</td>
<td>Sets the maintenance window for a specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateClientNetwork</td>
<td>Modifies the replica set's cross-segment access configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDbCacheRule</td>
<td>Modifies the specified memory acceleration rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>OfflineNodes</td>
<td>When an underlying failure causes a node to fail to operate normally, you can shut down the node. After shutdown, other nodes will take over the service. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Instance Load Balancing Management</td>
<td>ShowElbIpGroup</td>
<td>Query the IP access blacklist and whitelist for instance load balancing. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchIpGroup</td>
<td>Set the IP access blacklist and whitelist for instance load balancing. You can only select one of the blacklist and whitelist. Each call to this interface will overwrite the previous setting. If disabled, the source IP address of the connection is not restricted. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="13">Disaster Recovery Management</td>
<td>ShowPauseResumeStatus</td>
<td>Get the data synchronization status of the disaster recovery instance, the IDs of the primary and standby instances, the data synchronization index values, and the RPO and RTO index values in the switchover and failover scenarios. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDisasterRecovery</td>
<td>Remove the disaster recovery relationship between the instance and the specific instance. This API must be called once for each of the two instances in the disaster recovery relationship. Both calls must succeed to successfully remove the disaster recovery relationship. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDisasterRecoverySettings</td>
<td>Query the percentage of failed nodes in the instance's disaster recovery failover. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceBiactiveRegions</td>
<td>Query the regions where the instance can establish an active-active relationship. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGeminiDbDualActive</td>
<td>Remove cross-region active-active. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetDisasterRecoverySettings</td>
<td>Set the ratio of failed nodes for instance disaster recovery failover. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceRole</td>
<td>This interface is used to obtain the active/standby role information of the disaster recovery instance, so that it can be used to call the subsequent interfaces for promoting the backup instance to active or demotion to a backup. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PauseResumeDataSynchronization</td><td>This interface is used to pause/resume data synchronization for instances in a disaster recovery relationship. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckDisasterRecoveryOperation</td>
<td>Checks whether an instance can establish/remove a disaster recovery relationship with a specified instance. If the interface returns success, it indicates that a disaster recovery relationship can be established/removed with the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGeminiDbDualActive</td>
<td>To achieve cross-region instance data synchronization, GeminiDB provides a geo-active dual-active feature, which creates a geo-active dual-active instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchToMaster</td>
<td>This interface is used to upgrade a backup instance to the master instance for an instance that has already established a disaster recovery relationship. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDisasterRecovery</td>
<td>Establishes a disaster recovery relationship between an instance and a specific instance. This API must be called once for each instance in the disaster recovery relationship. Both calls must succeed for the relationship to be successfully established. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchToSlave</td>
<td>This API is used to downgrade the primary instance to a backup instance for an instance that has already established a disaster recovery relationship. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">Log Management</td>
<td>ListRedisSlowLogs</td>
<td>Query the slow log information of the GeminiDB (for Redis) database, supporting log keyword searches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInfluxdbSlowLogs</td>
<td>Query the slow log information of the GeminiDB (for InfluxDB) database, supporting log keyword search. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMongodbErrorLogs</td>
<td>Query the error log information of the GeminiDB (for Mongo) database, supporting log keyword search. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveLtsConfigs</td>
<td>- Associate the instance log with the LTS log stream. The backend will automatically upload the instance log to the associated LTS log stream. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchSlowlogDesensitization</td>
<td>Set the slow log desensitization status</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMongodbSlowLogs</td>
<td>Query the slow log information of the GeminiDB (for Mongo) database. Log keyword search is supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSlowLogDesensitization</td>
<td>Query the slow log desensitization status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLtsConfigs</td>
<td>Query the LTS log configuration information associated with the instance by page. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLtsConfigs</td>
<td>Disassociate the instance log from the LTS log stream. The backend will stop uploading the instance log to the LTS log stream. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowErrorLog</td>
<td>Query the database error log</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCassandraSlowLogs</td>
<td>Query the GeminiDB (for Cassandra) database slow log information. Log keyword search is supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSlowLogs</td>
<td>Query the database slow log information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Query API version</td>
<td>ListApiVersion</td>
<td>Query the list of currently supported API versions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApiVersion</td>
<td>Query the specified API version information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Query the list of dedicated resources</td>
<td>ListDedicatedResources</td>
<td>Query the list of dedicated resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Query all instance specifications</td>
<td>ListFlavors</td>
<td>Query all instance specifications under the specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFlavorInfos</td>
<td>Query instance specifications under the specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Query database version information</td>
<td>ListDatastores</td>
<td>Query database version information for a specified instance type. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Tag management</td>
<td>ListInstanceTags</td>
<td>Query the tag information of the specified instance. </td>
<td>To be tested</td>
</tr>
<tr><td>ListProjectTags</td>
<td>Query the tag information of the specified project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstancesByTags</td>
<td>Query the specified database instances by tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstancesByResourceTags</td>
<td>Query the specified database instances by tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchTagAction</td>
<td>Add or remove tags for specified database instances in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Manage databases and users</td>
<td>UpdateDatabases</td>
<td>Operate the GeminDB instance database</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstanceDatabases</td>
<td>Get a list of Redis instance databases. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetDbUserPassword</td>
<td>Reset the Redis database account password. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDbUser</td>
<td>Create a database account in the Redis instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyDbUserPrivilege</td>
<td>Modify the Redis database account privileges. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDbUsers</td>
<td>Get a list of Redis database accounts and their details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDbUser</td>
<td>Delete the database account for the Redis instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Connection Management</td>
<td>ListInstanceSessions</td>
<td>Get the instance session. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstancesSessionStatistics</td>
<td>Query instance node session statistics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ClearInstanceSessions</td>
<td>Close all instance node sessions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstancesSession</td>
<td>Close instance node sessions. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Quota Management</td>
<td>ShowQuotas</td>
<td>Query the resource quotas of a single tenant under the GeminiDB service. </td> 
<td>To be tested</td> 
</tr> 
</tbody> 
</table> 
</body>
</html>