# GaussDB MCP Server

## Version Information
v0.1.0

## Product Description

GaussDB MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud GaussDB. It enables full-link management of GaussDB resources based on natural language processing.

## Available Tools
Covering the full API, available as needed. The list and status are as follows:

<html>
<head></head>
<body>
<table border="1" cellspacing="0" cellpadding="5">
<tbody>
<tr>
<th>Category</th>
<th>Tool Name</th>
<th>Function Description</th>
<th>Status</th>
</tr>
<tr>
<td rowspan="33">HTAP - Standard Edition</td>
<td>RestartStarrocksInstance</td>
<td>Restart the StarRocks instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHtapDataStore</td>
<td>Query HTAP engine resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckStarrocksParams</td>
<td>Compare instance parameters with the default template</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpgradeSrKernelVersion</td>
<td>Upgrade the StarRocks kernel version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStarrocksInstance</td>
<td>Delete the StarRocks instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStarRocksDatabaseUser</td>
<td>Query the StarRocks database account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStarRocksDatabaseUserPassword</td>
<td>Change the StarRocks database account password. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckStarRocksResource</td>
<td>Check StarRocks resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateStarrocksInstance</td>
<td>Create a StarRocks instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckTableConfig</td>
<td>Verify the HTAP data synchronization table configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStarRocksDataReplications</td>
<td>Query StarRocks data synchronization status information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStarRocksDatabaseUserPermission</td>
<td>Modify StarRocks database account permissions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateStarRocksDataReplication</td>
<td>Create StarRocks data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateStarRocksDatabaseUser</td>
<td>Create a StarRocks database account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStarrocksParams</td>
<td>Query parameters by node type</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHtapFlavor</td>
<td>Query HTAP specification information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStarRocksDbParameters</td>
<td>Query the database parameter configuration for StarRocks data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestartStarrocksNode</td>
<td>Restart the StarRocks node. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SyncStarRocksUsers</td>
<td>Enable row and column splitting for the StarRocks instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStarRocksDataReplicationConfig</td>
<td>Query StarRocks data synchronization configuration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStarRocksDataReplication</td>
<td>Delete StarRocks data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStarRocksDatabaseUser</td>
<td>Delete the StarRocks database account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHtapStorageType</td>
<td>Get the HTAP instance storage type. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStarrocksInstanceInfo</td>
<td>Query the StarRocks instance. </td>
<td>To be tested</td>
</tr><tr>
<td>CheckDataBaseConfig</td>
<td>Verify the HTAP data synchronization database configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PauseStarRocksDataReplication</td>
<td>Pause StarRocks data replication. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResizeStarRocksFlavor</td>
<td>Change the StarRocks instance specifications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStarrocksParams</td>
<td>Modify node parameters by node type</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHtapInstanceInfo</td>
<td>Query the HTAP instance list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyDataSync</td>
<td>Modify the StarRocks data synchronization configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStarRocksDataReplicationConfigByDataBase</td>
<td>Query the StarRocks data synchronization configuration information by target database. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResumeStarRocksDataReplication</td>
<td>Resume StarRocks data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStarRocksDataBases</td>
<td>Query the StarRocks database. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="28">HTAP-Lightweight Edition</td>
<td>DeleteClickHouseDataBaseReplication</td>
<td>Delete data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateClickHouseInstance</td>
<td>Create an instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClickHouseDataBaseParameter</td>
<td>Query the database parameter configuration for data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClickHouseDataBaseReplication</td>
<td>Query data synchronization information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClickHouseInstanceNode</td>
<td>Query error log and slow log node information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RebootClickHouseInstance</td>
<td>Restart the instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteClickHouseDatabaseUser</td>
<td>Delete the database account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateClickHouseSlowLogSensitiveStatus</td>
<td>Change the slow log desensitization status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowClickHouseLtsConfig</td>
<td>Query the instance LTS log configuration list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckClickHouseDataBaseConfig</td>
<td>Verify the data synchronization database configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteClickHouseDataBaseConfig</td>
<td>Stop modifying data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClickHouseInstance</td>
<td>Query instance details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckClickHouseTableConfig</td>
<td>Verify data synchronization table configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowClickHouseDatabaseUser</td>
<td>Query database account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateClickHouseLtsConfig</td>
<td>Batch create LTS log configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateClickHouseDataBaseConfig</td>
<td>Modify data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResizeClickHouseInstance</td>
<td>Instance disk capacity expansion. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowClickHouseSlowLogSensitiveStatus</td>
<td>Query the slow log desensitization status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateClickHouseDatabaseUserPassword</td>
<td>Change the database account password. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResizeClickHouseFlavor</td>
<td>Change the instance specifications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowClickHouseSlowLogDetail</td>
<td>Get kernel slow log information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClickHouseDataBaseReplicationConfig</td>
<td>View the data synchronization configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateClickHouseDataBaseReplication</td>
<td>Create data synchronization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateClickHouseDatabaseUserPermission</td>
<td>Modify database account permissions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteClickHouseLtsConfig</td>
<td>Batch deactivate LTS log configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteClickHouseInstance</td>
<td>Delete an instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateClickHouseDatabaseUser</td>
<td>Create a database account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClickHouseDataBase</td>
<td>Query the database list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Task Center</td>
<td>ShowGaussMySqlJobInfo</td>
<td>Get the task information for the specified ID in the TaurusDB Task Center. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTaskRecord</td>
<td>Delete the specified task record. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScheduleJobs</td>
<td>Get the scheduled task list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelScheduleTask</td>
<td>Cancel a scheduled task</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListImmediateJobs</td>
<td>Get a list of immediate tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteScheduleTask</td>
<td>Delete a scheduled task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="14">Parameter Template Management</td>
<td>DeleteGaussMySqlConfiguration</td>
<td>Delete the specified parameter template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGaussMySqlConfiguration</td>
<td>Create parameter template information, including parameter template name, description, database version information, and parameter values. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListParamsTemplateApplyHistory</td>
<td>Query parameter template application records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGaussMySqlConfiguration</td>
<td>Get parameter information for the specified parameter template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchGaussMySqlConfiguration</td>
<td>Change the parameter template for the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConfigurationsInstances</td>
<td>Query the instances to which the specified parameter template can be applied. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CopyInstanceConfigurations</td>
<td>Copy the instance parameter group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CopyConfigurations</td>
<td>Copy the parameter group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstanceConfigurations</td>
<td>Modify the parameters of the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListModifyHistory</td>
<td>Query parameter modification history. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlConfiguration</td>
<td>Modify the parameter information of the specified parameter template, including the name, description, and value of the specified parameter. </td>
<td>To be tested</td></tr>
<tr>
<td>ListGaussMySqlConfigurations</td>
<td>Get a list of parameter templates, including the default parameter templates for all databases and user-created parameter templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstanceConfigurations</td>
<td>Get parameter information for a specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConfigurationsDifferences</td>
<td>Compare the differences between two parameter templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="14">Backup Management</td>
<td>UpdateGaussMySqlBackupPolicy</td>
<td>Set an automatic backup policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyBackupEncryptStatus</td>
<td>Turn backup encryption on or off. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGaussMySqlBackup</td>
<td>Create a manual backup. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestoreOldInstance</td>
<td>Restore a backup to the current instance or an existing instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGaussMySqlIncrementalBackupList</td>
<td>Query the incremental backup list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DescribeBackupEncryptStatus</td>
<td>Query whether the backup encryption function is enabled on the instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGaussMySqlBackupList</td>
<td>Query the full backup list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGaussMySqlBackup</td>
<td>Delete manual backups. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRestoreTables</td>
<td>Query the table-level point-in-time recovery options. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRestoreTables</td>
<td>Table-level point-in-time recovery. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBackupRestoreTime</td>
<td>Query the instance's recoverable time period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGaussMySqlBackupPolicy</td>
<td>Query the automatic backup policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateBackupOffsitePolicy</td>
<td>Set the cross-region backup policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRestoreAvailableTables</td>
<td>Query table-level point-in-time recovery of available tables. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Multi-tenant feature</td>
<td>UpdateMultiTenant</td>
<td>Enable or disable the multi-tenant feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMultiTenant</td>
<td>Query the multi-tenant feature status. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="47">Instance Management</td>
<td>SwitchGaussMySqlInstanceSsl</td>
<td>Set SSL data encryption for the instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlInstanceName</td>
<td>Modify the instance name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRecycleInstances</td>
<td>Query recycle bin instance information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDedicatedResourceInfo</td>
<td>Query dedicated resource information details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeGaussMySqlInstanceSpecification</td>
<td>Change the database instance specifications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlInstanceInternalIp</td>
<td>Modify the instance's internal network address. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetRecyclePolicy</td>
<td>Set the recycle bin policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>ExpandGaussMySqlInstanceVolume</td>
<td>Expand storage capacity during the period. </td>
<td>To be testedested</td>
</tr>
<tr>
<td>ModifyAutoExpandPolicy</td>
<td>Modify the automatic expansion policy of storage space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestartGaussMySqlNode</td>
<td>Restart the node. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGaussMySqlInstanceDetailInfo</td>
<td>Query instance details in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRecyclePolicy</td>
<td>Query the recycle bin policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlInstanceAlias</td>
<td>Modify the instance annotation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateServerlessPolicy</td>
<td>Set the Serverless configuration policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTaurusNodeDataIp</td>
<td>Modify the read-only node's intranet address. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoExpandPolicy</td>
<td>Query the automatic expansion policy for storage space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlInstanceOpsWindow</td>
<td>Set the maintenance window. It is recommended to set the maintenance window during off-peak hours to avoid unexpected business interruptions during maintenance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGaussMySqlDedicatedResources</td>
<td>Get a list of dedicated resource pools, including information about all dedicated resource pools activated by the user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGaussMysqlDns</td>
<td>Apply for an intranet domain name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceEip</td>
<td>Query the elastic public IP address. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestartGaussMySqlInstance</td>
<td>Restart the database instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstanceMonitor</td>
<td>Set up second-level instance monitoring, including 1-second and 5-second monitoring. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlInstanceSecurityGroup</td>
<td>Modify the specified instance security group. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGaussMySqlInstancesUnifyStatus</td>
<td>Query the instance list based on the specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGaussMySqlInstance</td>
<td>Create a TaurusDB instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetGaussMySqlPassword</td>
<td>Reset the database password. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGaussMySqlInstanceInfoUnifyStatus</td>
<td>Query instance details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceMonitorExtend</td>
<td>Query instance second-level monitoring information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoScalingHistory</td>
<td>Query the automatic scaling history. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAutoScalingPolicy</td>
<td>Set automatic scaling. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGaussMySqlInstanceInfo</td>
<td>Query instance details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceDatabaseVersion</td>
<td>Query kernel version information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGaussMySqlReadonlyNode</td>
<td>Create a read-only node. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelGaussMySqlInstanceEip</td>
<td>Unbind the elastic public IP address from the instance. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CheckResource</td> 
<td>Resource pre-verification. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ModifyNodePriority
<td>Modify the node failover priority. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGaussMySqlInstance</td>
<td>Delete/unsubscribe the database instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoScalingPolicy</td>
<td>Query automatic scaling. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGaussMySqlInstances</td>
<td>Query the instance list based on the specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyGaussMysqlDns</td>
<td>Modify the intranet domain name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlInstancePort</td>
<td>Change the instance database port. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpgradeGaussMySqlInstanceDatabase</td>
<td>Upgrade the kernel version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RenameInstanceNode</td>
<td>Change node names in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGaussMySqlInstanceDetailInfoUnifyStatus</td>
<td>Query instance details in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGaussMySqlReadonlyNode</td>
<td>Delete/unsubscribe the read-only node of the instance. When deleting/unsubscribing a read-only node in multi-AZ mode, ensure that the remaining read-only nodes and the primary node are in different AZs after deletion/unsubscription; otherwise, the read-only node cannot be deleted/unsubscribed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>InvokeGaussMySqlInstanceSwitchOver</td>
<td>Users manually perform a master/slave switchover. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlInstanceEip</td>
<td>Bind an elastic public IP address to the instance for external network connectivity. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="25">Database proxy</td>
<td>ChangeGaussMySqlProxySpecification</td>
<td>Change the database proxy specification. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProxyName</td>
<td>Modify the proxy instance name</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAccessControl</td>
<td>Set access control rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProxyConnectionPoolType</td>
<td>Change the database proxy connection pool type. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProxySessionConsistence</td>
<td>Modify proxy session consistency. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchAccessControl</td>
<td>Turn access control on or off. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShrinkGaussMySqlProxy</td>
<td>Shrink the number of database proxy nodes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProxyConfigurations</td>
<td>Query database proxy kernel parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProxyPort</td>
<td>Change the read/write split port number. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTransactionSplitStatus</td>
<td>Set proxy transaction splitting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGaussMySqlProxyFlavors</td>
<td>Query database proxy specification information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestartProxyInstance</td>
<td>Restart the database proxy.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProxyIpgroup</td>
<td>Query proxy instance access control</td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchGaussMySqlProxySsl</td>
<td>Set SSL data encryption for the database proxy.</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetGaussMySqlProxyWeight</td>
<td>Set the read-write splitting weight. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ShowGaussMySqlProxyList</td><td>Query the database proxy information list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExpandGaussMySqlProxy</td>
<td>Expand the number of database proxy nodes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProxyNewConfigurations</td>
<td>Modify database proxy parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpgradeProxyVersion</td>
<td>Upgrade the database proxy instance kernel version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProxyVersion</td>
<td>Query the proxy instance minor version</td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchGaussMySqlProxyEip</td>
<td>Bind and unbind the proxy elastic public IP address. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGaussMySqlProxy</td>
<td>Enable the database proxy. Only supports ELB mode. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateNewNodeAutoAddSwitch</td>
<td>Enable or disable automatic addition of new nodes to the proxy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyGaussMySqlProxyRouteMode</td>
<td>Set the read-write split routing mode. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGaussMySqlProxy</td>
<td>Disable the database proxy. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Database User Management</td>
<td>UpdateGaussMySqlDatabaseUserComment</td>
<td>Modify the database user comment for the TaurusDB instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetGaussMySqlDatabasePassword</td>
<td>Change the password of the TaurusDB instance database user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGaussMySqlDatabaseUser</td>
<td>Create the TaurusDB instance database user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDatabasePermission</td>
<td>Delete the database permissions of the TaurusDB instance database user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDatabasePermission</td>
<td>Grant the database permissions of the TaurusDB instance database user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGaussMySqlDatabaseUser</td>
<td>Query the database user for the TaurusDB instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGaussMySqlDatabaseUser</td>
<td>Delete the database user for the TaurusDB instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Database Management</td>
<td>CreateGaussMySqlDatabase</td>
<td>Create the database for the TaurusDB instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGaussMySqlDatabase</td>
<td>Query the TaurusDB instance database. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGaussMySqlDatabaseCharsets</td>
<td>Query the available character sets of the cloud database TaurusDB instance database. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlDatabaseComment</td>
<td>Modify the comment of the cloud database TaurusDB instance database. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGaussMySqlDatabase</td>
<td>Delete the TaurusDB instance database. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">Log Management</td>
<td>ListLtsErrorLogDetails</td>
<td>Get a list of error log details for the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAuditLog</td>
<td>Enable or disable full SQL. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateLtsConfigs</td>
<td>Batch create LTS log configurations</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowLtsConfigs</td>
<td>Query the instance LTS log configuration list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSlowLogStatistics</td><td>Query slow log statistics</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAuditLog</td>
<td>Query the full SQL switch status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLtsConfigs</td>
<td>Batch delete LTS log configurations</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLtsSlowlogDetails</td>
<td>Get a list of slow log details for a specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DownloadSlowLogFile</td>
<td>Get the slow log download link</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSlowlogSensitiveSwitch</td>
<td>Enable or disable the slow log desensitization state</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAuditLogDownloadLink</td>
<td>Get the temporary download link for the full SQL statement. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSlowlogSensitiveStatus</td>
<td>Query the slow log desensitization status</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Intelligent Diagnosis</td>
<td>ShowIntelligentDiagnosisAbnormalCountOfInstances</td>
<td>Get the number of abnormal instances for each metric. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowIntelligentDiagnosisInstanceInfosPerMetric</td>
<td>Get abnormal instance information for a particular metric. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Query the database engine version</td>
<td>ShowGaussMySqlEngineVersion</td>
<td>Get the database version information corresponding to the specified database engine. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Query database specifications</td>
<td>ShowGaussMySqlFlavors</td>
<td>Get the specifications information corresponding to the specified database engine version. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Tag management</td>
<td>ListProjectTags</td>
<td>Query all tag sets for instances under the specified project ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstanceTags</td>
<td>Query the tag information of the specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchTagAction</td>
<td>Add or delete tags for the specified instances in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Traffic Management</td>
<td>DeleteSqlFilterRule</td>
<td>Delete the SQL throttling rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetSqlFilterRule</td>
<td>Set the SQL throttling rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSqlFilterControl</td>
<td>Query the SQL throttling switch status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSqlFilterRule</td>
<td>Query the SQL throttling rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSqlFilterControl</td>
<td>Enable or disable SQL throttling. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTaurusDbNodeProcesses</td>
<td>Terminates the specified user session thread in the TaurusDB node. This will exclude the incoming internal session threads. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTaurusDbNodeProcesses</td>
<td>Query the user session threads in the TaurusDB node by page. This corresponds to the show processlist command. The returned results do not include internal session threads. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Quota Management</td>
<td>ShowGaussMySqlQuotas</td>
<td>Get the resource quota for the specified enterprise project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetGaussMySqlQuotas</td>
<td>Set the resource quota for the specified enterprise project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGaussMySqlProjectQuotas</td>
<td>Get the resource quota for the specified tenant. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGaussMySqlQuotas</td>
<td>Modify the resource quota for the specified enterprise project. </td>
<td>To be tested</td>
</tr>
<tr><td>ListEnterpriseProjects</td>
<td>Query enterprise projects. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>