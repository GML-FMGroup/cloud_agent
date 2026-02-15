# LakeFormation MCP Server


## Version
v0.1.0

## Overview

LakeFormation MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service LakeFormation. Full-chain management of LakeFormation resources can be carried out based on natural language.

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
<td rowspan="13">Access</td> 
<td>ShowSyncPolicy</td> <td>Get synchronization permission policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchAuthorizeInterface</td>
<td>Batch authorization interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAccessClient</td>
<td>Delete service access client by ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAccessClient</td>
<td>Update service access client by ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInterfaces</td>
<td>Query interface by filter condition</td>
<td>To be tested</td>
</tr>
<tr>
<td>ApplyForAccess</td>
<td>Apply for access service</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAccessClient</td>
<td>Get service access client details based on ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAccessClient</td>
<td>Create a service access client.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicy</td>
<td>Get synchronization permission policies by page</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccessClientInfos</td>
<td>Get a list of access client information related to a service instance based on a LakeFormation instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAccessInfos</td>
<td>Get access information related to the service instance based on the LakeFormation instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCancelAuthorizationInterface</td>
<td>Batch Cancel Authorization Interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCheckPermission</td>
<td>Batch Authentication</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Agency</td>
<td>ShowAgency</td>
<td>Agency Query</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAgency</td>
<td>DeleteAgency</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAgency</td>
<td>Create a delegate</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Catalog</td>
<td>UpdateCatalog</td>
<td>Modify catalog information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCatalogs</td>
<td>List catalog details based on wildcards in the catalog name</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCatalog</td>
<td>Get catalog information</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCatalog</td>
<td>Delete an empty catalog object. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCatalog</td>
<td>Creating a catalog will create a default database under the catalog. The default database name is: default</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Configuration</td>
<td>ListConfigs</td>
<td>Get all user-visible tenant configurations</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Credential</td>
<td>ShowCredential</td>
<td>Get a temporary key and securityToken. The expiration time is greater than or equal to 1 hour. Please renew it within 1 hour.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Database</td>
<td>ListDatabases</td>
<td>List database information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDatabaseNames</td>
<td>List database name information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDatabase</td>
<td>Get database</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDatabase</td>
<td>Modify database properties</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDatabase</td>
<td>Delete the specified database. Deleting the default database for the catalog is not allowed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDatabase</td>
<td>Create a database</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Function</td>
<td>DeleteFunction</td>
<td>Delete a function</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAllFunctions</td>
<td>Get all functions in the catalog</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateFunction</td>
<td>Modify function properties</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFunctionNames</td>
<td>Query all function names in the database</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowFunction</td>
<td>Query function information based on function name</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFunctions</td>
<td>List functions</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateFunction</td>
<td>Create function</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">GrantAccess</td>
<td>AuthorizeAccessService</td>
<td>Access service authorization</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAccessService</td>
<td>Query the tenant's current access service authorization</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAgreement</td>
<td>User authorization and delegation</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAgreement</td>
<td>Query the tenant's current agreement and delegation information</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAgreement</td>
<td>User cancels authorization, and authorized users delete delegation</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAgreementRule</td>
<td>Query the current system agreement</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Info</td>
<td>CountMetaObj</td>
<td>Metadata quantity counting interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Instance</td>
<td>DeleteLakeFormationInstance</td>
<td>Delete the LakeFormation instance based on the instance ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateLakeFormationInstance</td>
<td>Modify LakeFormation instance information</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateLakeFormationInstanceScale</td>
<td>Change LakeFormation instance scale</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateLakeFormationInstance</td>
<td>Create a LakeFormation instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLakeFormationInstances</td>
<td>Query the list of instances created by the user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowLakeFormationInstance</td>
<td>Use the instance ID to query LakeFormation instance details</td>
<td>To be tested</td>
</tr>
<tr>
<td>MoveLakeFormationInstanceOutRecycleBin</td>
<td>Restore the LakeFormation instance from the recycle bin</td>
<td>Tobe tested</td>
</tr>
<tr>
<td>UpdateLakeFormationInstanceDefault</td>
<td>Set as the default instance. Only non-default instances can be set as the default instance.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">OBS</td>
<td>ListObsObject</td>
<td>Query the OBS bucket object list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListObsBuckets</td>
<td>Query the OBS bucket list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Partition</td>
<td>BatchUpdatePartition</td>
<td>All partitions must exist. If a partition does not exist, a failure is returned.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPartitionNamesWithoutLimit</td>
<td>Traverses the partition name list and returns the full data. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchListPartitionByValues</td>
<td>Get partition information in batches</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeletePartition</td>
<td>Non-transactional table: If data deletion is set, the data in the partition data path will be deleted immediately. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPartitions</td>
<td>Traverses the partition list under the specified data table. For transactional tables, supports traversing the partition list based on a specific table version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddPartitions</td>
<td>Add partition information in batches</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPartitionNames</td>
<td>Traverse the partition name list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">PartitionColumnStatistic</td>
<td>BatchShowPartitionColumnStatistics</td>
<td>Get partition column statistics in batches</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetPartitionColumnStatistics</td>
<td>Set partition statistics in batches</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePartitionColumnStatistics</td>
<td>Delete partition column statistics</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">QM</td>
<td>ListQuotas</td>
<td>Query user quota information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">Role</td>
<td>UpdatePrincipals</td>
<td>Update principals in a role</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRole</td>
<td>Create a role</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRole</td>
<td>Get a role</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRole</td>
<td>Modify role information</td>
<td>To be tested</td>
</tr>
<tr>
<td>AssociatePrincipals</td>
<td>Add one or more users/user groups to a role</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRoles</td>
<td>Return all roles</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPrincipals</td>
<td>Query users/user groups under a role</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRoleNames</td>
<td>Query a list of all role names</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRole</td>
<td>Delete a specified role</td>
<td>To be tested</td>
</tr>
<tr>
<td>RevokePrincipals</td>
<td>Remove one or more users/user groups from a role</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Specification</td>
<td>ListSpecs</td>
<td>Query a list of specifications</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">TAG</td>
<td>ListLakeFormationInstanceTags</td>
<td>Query all resource tags for instance types in a tenant's specified project</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateLakeFormationInstanceTags</td>
<td>Batch updates tags for a specified instance</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Table</td>
<td>ListTablesByName</td>
<td>Query a list of tables in the database by name</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTable</td>
<td>Get table information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTables</td>
<td>Returns metadata information for tables in the database that meet the query criteria. Transaction operations are not supported.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTable</td>
<td>Modify table information</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTable</td>
<td>Create table operation</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTableMeta</td>
<td>Use database and table wildcards to find tables that meet the requirements and return their description information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTableNames</td>
<td>Query the list of all table names in the database</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTable</td>
<td>Delete a table and its partitions</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">TableColumnStatistic</td>
<td>DeleteTableColumnStatistics</td>
<td>Delete statistics for a specified table column</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTableColumnStatistics</td>
<td>Get table column statistics</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetTableColumnStatistics</td>
<td>Update table column statistics</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">User</td>
<td>UpdateRoles</td>
<td>Update roles in a user</td>
<td>To be tested</td>
</tr>
<tr>
<td>AssociateRoles</td>
<td>Grant multiple roles to a user</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUsers</td>
<td>Get a list of users</td>
<td>To be tested</td>
</tr>
<tr>
<td>RevokeRoles</td>
<td>Remove one or more roles from a user</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserRoles</td>
<td>Query the user's role list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">UserGroup</td>
<td>ListGroupsForDomain</td>
<td>Get the tenant's user groups</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>