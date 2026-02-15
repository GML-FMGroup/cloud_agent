# DataArtsStudio MCP Server

## Version Information
v0.1.0

## Product Description

DataArtsStudio MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud DataArtsStudio. It enables full-link management of DataArtsStudio resources using natural language.

## Available Tools

Covering the full API, available on demand. A list and status are as follows:

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
<td rowspan="17">API Management Interface</td>
<td>PublishApiToInstance</td>
<td>Publish an API. An API can only be called after it's published. When publishing an API, you can send it to a designated gateway. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstanceList</td>
<td>View the instance information corresponding to different API operations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AuthorizeApiToInstance</td>
<td>- API active authorization: The API reviewer can initiate this. Once successful, the app can access the API within its validity period. API authorization includes both authorization and renewal. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DebugApi</td>
<td>Debug the API. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportDataServiceExcelTemplate</td>
<td>Download the Excel template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApis</td>
<td>Query the API list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AuthorizeApiToInstance</td>
<td>After successfully creating an app, you cannot access the API yet. If you want to access an API, you need to authorize the API to the app. After the API is successfully authorized, the app can access the API within the validity period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportDataServiceExcel</td>
<td>Import an Excel file containing API information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateApi</td>
<td>Update the API. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteApiToInstance</td>
<td>- Deactivate the API. After deactivation, all authorizations will be revoked, and the API will no longer be callable. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchDebugInfo</td>
<td>View the debug information for the API on different clusters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchPublishInfo</td>
<td>View the published information for the API on different clusters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateApi</td>
<td>Create an API. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApi</td>
<td>Query API information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportDataServiceExcel</td>
<td>Export an Excel file containing API information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApi</td>
<td>Batch delete APIs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportDataServiceZip</td>
<td>Exports the entire data to an Excel compressed file containing the API. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Business Metrics Interface</td>
<td>ListBizMetrics</td>
<td>Search for business metrics information by name, creator, or modification time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateBizMetric</td>
<td>Create a business metric. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteBizMetric</td>
<td>Delete a business metric. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBizMetricById</td>
<td>View the details of the indicator by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateBizMetric</td>
<td>Update the business indicator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBizMetricOwners</td>
<td>View the indicator owner information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMetricRelations</td>
<td>Get the current indicator map. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBizMetricDimensions</td>
<td>View metric dimension information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Business Asset Interface</td>
<td>ShowBusinessAssetsTree</td>
<td>Query the business asset directory tree level by level, including business objects and logical entities synchronized from the data specification. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBusinessAssets</td>
<td>Business Asset Query Interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Subject Level Interface</td>
<td>ChangeSubjects</td>
<td>Modify or delete a subject level. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSubjectLevels</td>
<td>Get subject levels. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Subject management interface</td>
<td>UpdateSubject</td>
<td>Modify a subject. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSubject</td>
<td>Create a subject. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchSubject</td>
<td>Search for subjects by name (supports fuzzy search), creator, responsible person, status, and modification time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBusiness</td>
<td>Get data asset subject tree information l1, l2, l3. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSubjectNew</td>
<td>Modify subject (new). </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSubject</td>
<td>Delete subject. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSubjectNew</td>
<td>Delete subject (new). </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchSubjectNew</td>
<td>Search for a new subject. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSubjectNew</td>
<td>Create a new subject. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Fact Table Interface</td>
<td>ShowFactLogicTableById</td>
<td>View the details of the fact table by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckFactLogicTableStatus</td>
<td>View the reverse fact table task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDesignFactLogicTable</td>
<td>Delete a fact table based on an ID set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFactLogicTables</td>
<td>Search for fact table information by Chinese and English name, creator, reviewer, status, and modification time. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Enterprise Mode Release Package Management</td>
<td>DeployFactoryPackages</td>
<td>Release Task Package</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowFactoryPackageDetail</td>
<td>Query the details of a specified release package</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFactoryReleasePackages</td>
<td>Query the release package list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelFactoryPackages</td>
<td>Cancel the task package</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Job development interface</td>
<td>RetryFactoryJobInstance</td>
<td>Supports rerunning job instances and upstream and downstream job instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFactoryAlarmInfo</td>
<td>Query alarm notification records</td>
<td>To be tested</td>
</tr>
<tr>
<td>StopFactorySupplementDataInstance</td>
<td>Stop supplement data instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateFactoryJobName</td>
<td>Modify job name</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowFactorySupplementData</td>
<td>Query supplement data instance</td>
<td>To be tested/td>
</tr>
<tr>
<td>CreateFactorySupplementDataInstance</td>
<td>Create a supplementary data instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFactoryJobInstancesByName</td>
<td>Query a list of instances of a specified job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowFactoryFullText</td>
<td>Global search</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetFactoryJobTags</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Information Architecture Interface</td>
<td>ListAllTables</td>
<td>Query various table types from the information architecture, including logical entities, physical tables, dimension tables, fact tables, and summary tables. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Real-time metadata synchronization</td>
<td>BatchSyncMetadata</td>
<td>Real-time metadata synchronization API, supporting batch synchronization. This API is currently in the invitation beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Metadata Collection Task Interface</td>
<td>DeleteTaskInfo</td>
<td>Delete a single collection task</td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteTaskAction</td>
<td>Start, schedule, and stop collection tasks</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceLog</td>
<td>Get task log</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTaskInfo</td>
<td>Edit a collection task</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskInfo</td>
<td>Query the collection task details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskList</td>
<td>Query the collection task list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTask</td>
<td>Create a collection task</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="17">Relational Modeling Interface</td>
<td>CreateTableModel</td>
<td>Create a table model in relational modeling, including logical entities and physical tables. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTableModelRelations</td>
<td>Query all relationships under the model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRelations</td>
<td>Search for relationship information by paging, such as relationship name (supports fuzzy search), creator, start time, and end time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWorkspaces</td>
<td>Delete a model workspace. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkspace</td>
<td>Create a new model workspace. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkspaceDetailById</td>
<td>Query the workspace details of a physical or logical model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTableModelById</td>
<td>Get model table details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTableModels</td>
<td>Search table model information in relational modeling by Chinese and English name, creator, reviewer, status, and modification time, including logical entities, physical tables, and their attributes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchFieldsForRelation</td>
<td>Query the target table and fields (to be deprecated). </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkspace</td>
<td>Update the model workspace. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkspaces</td>
<td>Get all model information in the current workspace. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTableModel</td>
<td>Delete a table model and its attributes, including logical entities and physical tables, in relational modeling. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDesignOperationResult</td>
<td>Get the results of batch operations, such as converting logical models to physical models and reverse database operations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateDesignTableModelsFromLogic</td>
<td>Convert logical models to physical modelsIf the conversion is successful, the converted target model information is displayed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportDesignModelTableDdl</td>
<td>Exports the DDL statements for the specified table based on the model ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRelationById</td>
<td>Gets relationship details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTableModel</td>
<td>In relational modeling, updates a table model and its attributes, including logical entities and physical tables. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Dynamic data masking interface</td>
<td>ShowSecurityDynamicMaskingPolicy</td>
<td>Query detailed information of a masking policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteSecurityDynamicMaskingPolicies</td>
<td>Batch delete dynamic masking policies</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityDynamicMaskingPolicies</td>
<td>Query the list of dynamic data masking policies. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityDynamicMaskingPolicy</td>
<td>Update dynamic data masking policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSecurityDynamicMaskingPolicy</td>
<td>Create dynamic data masking policy</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Atomic Indicator Interface</td>
<td>DeleteDesignAtomicIndex</td>
<td>Batch delete atomic indicators. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAtomicIndexById</td>
<td>Get atomic indicator details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchAtomicIndexes</td>
<td>Search atomic indexes by Chinese and English name, creator, reviewer, status, and modification time. Fuzzy search is supported for Chinese and English names. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesignAtomicIndex</td>
<td>Update a single atomic index. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesignAtomicIndex</td>
<td>Create a new single atomic index. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Release package management</td>
<td>CreateFactoryPendingItemsPackage</td>
<td>Release pending packages</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFactoryPendingItems</td>
<td>Query the list of pending packages</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Compound metric interface</td>
<td>CreateDesignCompoundMetric</td>
<td>Create a new compound metric based on parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDesignCompoundMetric</td>
<td>Delete a compound metric based on an ID set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCompoundMetrics</td>
<td>Search for compound metric information by Chinese/English name, creator, reviewer, status, modification time, and l3Id. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCompoundMetricById</td>
<td>Get compound metric details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesignCompoundMetric</td>
<td>Update a compound metric based on parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Security Administrator Interface</td>
<td>ShowSecurityAdmin</td>
<td>View the security administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifySecurityAdmin</td>
<td>Create or update a security administrator. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Instance management interface</td>
<td>ListDataArtsStudioInstances</td>
<td>Get instance list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Instance specification change interface</td>
<td>ChangeResource</td>
<td>Specification change interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">Approval management interface</td>
<td>SearchApprovals</td>
<td>Get approval forms. </td><td>To be tested</td>
</tr>
<tr>
<td>DeleteDesignLatestApproval</td>
<td>When a published entity is edited, it generates a sub-append. This interface is used to delete the entity's sub-append information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ConfirmApprovals</td>
<td>Approval rejection/approval, single or multiple action-id=reject/resolve. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchDesignLatestApprovalDiff</td>
<td>When a published entity is edited, it generates a sub-append. This interface is used to retrieve the difference between the sub-append information and the published entity. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RollbackApproval</td>
<td>Withdraw the approval form. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchPublish</td>
<td>Batch publish. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApprover</td>
<td>Delete the approver. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchOffline</td>
<td>Batch offline. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApprovers</td>
<td>Query the list of approvers. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateApprover</td>
<td>Create an approver. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Security level management interface</td>
<td>BatchDeleteSecuritySecrecyLevels</td>
<td>Batch delete security levels</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecuritySecrecyLevel</td>
<td>Query security levels based on a specified ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSecuritySecrecyLevel</td>
<td>Delete the security level of a specified ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecuritySecrecyLevel</td>
<td>Modify security levels based on a specified ID</td>
<td>To be tested tested</td>
</tr>
<tr>
<td>CreateSecuritySecrecyLevel</td>
<td>Create a security level</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecuritySecrecyLevels</td>
<td>Get a security level</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Reconciliation job interface</td>
<td>ShowConsistencyTaskDetail</td>
<td>Get reconciliation job details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConsistencyTask</td>
<td>Get a reconciliation job list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Import and export interfaces</td>
<td>ImportModels</td>
<td>Import models, relational modeling, dimensional modeling, code tables, business indicators, and process architecture. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportCatalogs</td>
<td>Used to import themes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportDesignModels</td>
<td>Export business data based on request parameters. Exportable data includes: code tables, data standards, atomic indicators, derived indicators, composite indicators, summary tables, business indicators, themes, processes, logical models, physical models, dimensions, and fact tables. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportDesignResult</td>
<td>Get the Excel export result based on the uuid returned when requesting to export business data (/export-model). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportResult</td>
<td>Query the result of the Excel import process (the parameter uuid is obtained from the result returned by the /design/models/action or /design/catalogs/action interfaces). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Workspace user management interface</td>
<td>DeleteWorkspaceusers</td>
<td>Delete workspace users</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkSpaceUserOrGroup</td>
<td>Edit workspace users or user groups</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkspaceusers</td>
<td>Get workspace user information</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddWorkSpaceUsers</td>
<td>Add workspace users</td>
<td>To be tested</td></tr>
<tr>
<td>ListWorkspaceRoles</td>
<td>Get workspace user roles</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Workspace management interface</td>
<td>CreateManagerWorkSpace</td>
<td>Create a workspace</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkspacesForUser</td>
<td>Get a collection of all workspaces for a specified user</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkSpace</td>
<td>Get information about a single workspace</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListManagerWorkSpaces</td>
<td>Get the workspace list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Application management interface</td>
<td>CreateApp</td>
<td>Create an application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApps</td>
<td>Query the application list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateApp</td>
<td>Update an application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAppInfo</td>
<td>Query application details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApp</td>
<td>Delete the app. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">Overview API</td>
<td>ShowApisOverview</td>
<td>Query the overview of user-related development metrics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApisDetail</td>
<td>Query API statistics details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAppsDetail</td>
<td>Query app statistics details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApisDashboard</td>
<td>Query API dashboard data details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAppsDashboard</td>
<td>Query app dashboard data details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApisTop</td>
<td>Query the topN API service calls. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApiDashboard</td>
<td>Query the specified API dashboard data details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAppsOverview</td>
<td>Query and count user-related overview call metrics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAppsTop</td>
<td>Query the top N app service usage. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApiTopN</td>
<td>Query the top N apps that call a specific API. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Cost management calculation dimension interface</td>
<td>SearchSgcComputeDimensions</td>
<td>Get calculation dimension cost list information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Indicator asset interface</td>
<td>ShowMetricTree</td>
<td>Query indicator asset directory tree</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMetricAssets</td>
<td>Indicator asset query interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Authorization management interface</td>
<td>SearchAuthorizeApp</td>
<td>Query the APIs that have been authorized by the app. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchBindApi</td>
<td>Query the APIs that the app has been authorized to use. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Sensitive data result management interface</td>
<td>ListSecuritySensitiveDataOverviews</td>
<td>Query the sensitive data discovery overview results (by classification and confidentiality level)</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Data warehouse layer interface</td>
<td>UpdateDesignDataLayers</td>
<td>Modify or delete data warehouse layers/td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDesignDataLayers</td>
<td>Get data warehouse layer information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Data classification interface</td>
<td>ImportSecurityBuiltinCategoryGroups</td>
<td>Import preset categories. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityDataCategories</td>
<td>Query the data category list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="16">Data map interface</td>
<td>ShowDataSets</td>
<td>Asset search</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCategoriesTree</td>
<td>Get the asset catalog tree under a space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchTag</td>
<td>Batch tag assets. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLogicEntities</td>
<td>Get the logical entities under the theme catalog. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTableData</td>
<td>Preview of table data, showing 10 data items. This API is in the invite beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceInfos</td>
<td>Query information about the running instances of the job operators associated with the table. This API is in the invite beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNodes</td>
<td>Query a list of job operators associated with the table. This API is in the invite beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDataDetail</td>
<td>Asset details interface. This interface is in the invite beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDatamapLineage</td>
<td>Asset lineage interface. This interface is in the invite beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEntity</td>
<td>Delete an asset by GUID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowQueues</td>
<td>Queue list, showing 10 data items. This API is in the invitation beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowLineageBulk</td>
<td>Batch lineage API, which queries lineage in batches based on job operators by page. This API is in the invitation beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTags</td>
<td>Show search query tags in paginated form</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrUpdateEntities</td>
<td>Create or modify assets. This API is currently in the invitation beta stage and will be gradually released with the public beta. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEntityDetails</td>
<td>Get asset information in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ParseUserBehavior</td>
<td>User behavior analysis</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Data security diagnosis interface</td>
<td>ExecuteSecurityDiagnose</td>
<td>Execute data security diagnosis. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecurityNoMaskingTableResult</td>
<td>Query table information for which static masking tasks have not been performed</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityUnreasonablePermissions</td>
<td>Query unreasonable permission configurations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecuritySensitiveDataDiagnoseResult</td>
<td>Query the diagnostic results of the sensitive data protection module</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecurityDatasourceProtectionDiagnoseResult</td>
<td>Query the diagnostic results of the data source protection module</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecurityPermissionManagementDiagnoseResult</td>
<td>Query the diagnostic results of the data permission control module. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Data permission query interface</td>
<td>ListSecurityRoleActions</td>
<td>Query the intersection of a role's permissions for a set of libraries and tables.

<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Data Standard Interface</td>
<td>CreateStandard</td>
<td>Create a data standard.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStandard</td>
<td>Modify a data standard.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStandard</td>
<td>Delete a data standard.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStandardById</td>
<td>Get data standard details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAllStandards</td>
<td>Get the data standard collection by paging based on the query criteria, sorted in descending order by modification time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetLinkAttributeAndStandard</td>
<td>Associate the attribute with the data standard. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Data Standard Template Interface</td>
<td>CreateStandardTemplate</td>
<td>Create a custom data standard template item in the current workspace. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStandardTemplate</td>
<td>Query the data standard template in the current workspace. </td>
<td>To be tested</td>
</tr>
<tr>
<td>InitializeStandardTemplate</td>
<td>Initialize the data standard template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStandardTemplate</td>
<td>Delete the data standard template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStandardTemplate</td>
<td>Modify the data standard template. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Data source metadata acquisition interface</td>
<td>ListDataTables</td>
<td>Get tables in the data source</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListColumns</td>
<td>Get fields in a table in the data source</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSchemas</td>
<td>Get schemas. Currently, only DWS and RDS data sources using the PostgreSQL driver support schemas. Please confirm whether the data source supports schema fields before calling. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDatabases</td>
<td>Get a list of databases</td>
<td>To be tested tested</td>
</tr>
<tr>
<td rowspan="1">Data Source Interface</td>
<td>SearchDwByType</td>
<td>Get data connection information of the specified type. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Data Connection Management</td>
<td>AuthorizeDataConnection</td>
<td>Data connection cross-domain authorization. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Data connection management interface</td>
<td>ShowDataconnection</td>
<td>Query a single data connection</td>
<td>To be tested</td>
</tr>
<tr>
<td>DebugDataconnection</td>
<td>Test creation of a data connection</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDataconnection</td>
<td>Update data connection information</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateConnections</td>
<td>Create data connections</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDataconnection</td>
<td>Delete data connection</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataconnections</td>
<td>Query data connection list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="13">Service catalog management interface</td>
<td>ListAllCatalogList</td>
<td>Get a list of all types in the current catalog (including APIs and catalogs, all displayed in catalog data format). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPathObjectById</td>
<td>Get a path object by catalog ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteServiceCatalog</td>
<td>Batch delete service catalogs. </td> 
<td>Tobe tested</td>
</tr>
<tr>
<td>CreateServiceCatalog</td>
<td>Create a service catalog. The root catalog is numbered 0. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApiCatalogList</td>
<td>Get a list of APIs in the current catalog. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchIdByPath</td>
<td>Get an ID by path. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCatalogList</td>
<td>Get a list of catalogs in the current catalog (full data, no paging, recommended only for scenarios where paging is not possible, such as generating a directory tree). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataServiceMarketApis</td>
<td>Query the service catalog API list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCatalogDetail</td>
<td>Query the service catalog. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPathById</td>
<td>Get the path by id. </td>
<td>To be tested</td>
</tr>
<tr>
<td>MigrateApi</td>
<td>Batch move APIs to the new catalog. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCatalog</td>
<td>Update the service catalog. </td>
<td>To be tested</td>
</tr>
<tr>
<td>MigrateCatalog</td>
<td>Move the current catalog to the new catalog. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Permission Approval Interface</td>
<td>BatchRejectSecurityApplications</td>
<td>Batch Reject Work Orders</td>
<td>To be tested</td>
</tr>
<tr>
<td>AcceptSecurityApplication</td>
<td>Approve Work Orders</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeclineSecurityApplication</td>
<td>Reject Work Orders</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchApproveSecurityApplications</td>
<td>Batch Approve Work Orders</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityApprovals</td>
<td>Get a list of work orders</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityTableApprovers</td>
<td>Get a list of table permission approvers</td>
<td>To be tested</td>
</tr>
<tr>
<td>ApplySecurityTableAuthority</td>
<td>Submit a table permission application</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Authorization application interface</td>
<td>DebugSecurityDlfDataWareHouses</td>
<td>Test data development connection fine-grained connectivity</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityDlfDataWareHouses</td>
<td>Query the data development fine-grained connection list (full)</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateSecurityDlfDataWareHouses</td>
<td>Batch update the fine-grained authentication status of data development connections</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Permission application interface</td>
<td>UnpublishSecurityApplication</td>
<td>Withdraw work order application</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="19">Permission management interface</td>
<td>CreateSecurityPermissionSetMember</td>
<td>Add a permission set member</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteSecurityPermissionSetPermissions</td>
<td>Delete permissions from a permission set</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityDatasourceUrls</td>
<td>Query URL information</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteSecurityPermissionSetMembers</td>
<td>Batch delete permission set members</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSecurityPermissionSetPermission</td>
<td>Add permissions to a permission set</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityPermissionSetPermissions</td><td>UpdateSecurityPermissionSet</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityPermissionSet</td>
<td>Update a permission set</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityMemberPermission</td>
<td>Query my permissions and space account permissions</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSecurityPermissionSet</td>
<td>Delete a permission set</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateSecurityPermissionSetPermissions</td>
<td>Batch add permissions to a permission set</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecurityPermissionSet</td>
<td>Query permission sets</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityMemberPermissionExpireTime</td>
<td>Batch change permission expiration time</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateSecurityPermissionSetMembers</td>
<td>Batch add permission set members</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityDatasourceConfigurations</td>
<td>Query data source configurable permissions</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityPermissionSets</td>
<td>Query the permission set list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityPermissionSetMembers</td>
<td>Query the permission set member list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityPermissionSetPermissions</td>
<td>Query the permission set permission list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSecurityPermissionSet</td>
<td>Create a permission set</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityDatasourceActions</td>
<td>Query data operation information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Tag interface</td>
<td>ShowGlossaryList</td>
<td>Query the tag list</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddTagToAsset</td>
<td>Associate a tag to an asset</td>
<td>To be tested</td>
</tr>
<tr>
<td>RemoveDesignEntityTags</td>
<td>Remove an asset tag based on the asset (table or attribute) ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDesignEntityTags</td>
<td>Add a tag to an asset based on the asset (table or attribute) ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Overview</td>
<td>CountStandards</td>
<td>View the coverage of a data standard across all model fields, that is, the percentage of fields that use that standard. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountTableModels</td>
<td>Statistics for a single model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountAllModels</td>
<td>Statistics for the outer layer of the relational modeling page. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountOverviews</td>
<td>Overview statistics. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Aggregation Table Interface</td>
<td>ShowAggregationLogicTableById</td>
<td>View the details of the aggregation table by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAggregationLogicTables</td>
<td>Search for aggregation table information by Chinese and English name, creator, reviewer, status, and modification time. Fuzzy queries are supported for Chinese and English names. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesignAggregationLogicTable</td>
<td>Update the aggregation table. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesignAggregationLogicTable</td>
<td>Manually create an aggregation table based on the input parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDesignAggregationLogicTable</td>
<td>Batch delete aggregation tables. Only tables in the Draft, Offline, or Rejected status can be deleted. </td><td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Process Architecture Interface</td>
<td>ListCatalogTree</td>
<td>Get all catalog trees. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchCatalogs</td>
<td>Query the list of process architectures. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCatalog</td>
<td>Create a process architecture. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCatalog</td>
<td>Delete a process architecture. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBizCatalogDetail</td>
<td>Find process architecture details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeCatalog</td>
<td>Modify process architecture. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Message Management Interface</td>
<td>ShowMessageDetail</td>
<td>Get message details. This function is only used to display message details and does not require business processing. Therefore, backend parameters such as the ID are not displayed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMessage</td>
<td>Query the list of notification messages in the review center. Unlike applications, notification messages cannot be rejected and can only be processed within a specified timeframe. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ConfirmMessage</td>
<td>Confirm the received notification message and choose when to process it within a specified timeframe. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Version Information Interface</td>
<td>CompareDesignVersions</td>
<td>Compares the differences between two version IDs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchVersions</td>
<td>Search for version information by name, creator, or modification time. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">User synchronization task interface</td>
<td>ShowSecurityMemberSyncTask</td>
<td>Query a single user synchronization task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">User synchronization interface</td>
<td>ListSecurityMemberSyncTasks</td>
<td>Query the user synchronization list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Application management interface</td>
<td>ListApply</td>
<td>Query the application list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchApproveApply</td>
<td>Apply the application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApplyDetail</td>
<td>Get application details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Monitoring Operations</td>
<td>ListFactoryTaskOverview</td>
<td>Query Instance Running Status</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFactoryTaskCompletion</td>
<td>Query Task Completion Status</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Directory Interface</td>
<td>ListCategory</td>
<td>Get Job Directory</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Directory Management</td>
<td>DeleteDirectory</td>
<td>Delete a directory (data standard, code table). </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDirectory</td>
<td>Modify a directory (data standard, code table). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDirectories</td>
<td>Get all directories (data standard, code table). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDirectory</td>
<td>Create a directory (data standard, code table). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Code table management interface</td>
<td>SearchCodeTableValues</td>
<td>View code table field values. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>UpdateCodeTable</td> 
<td>Modify the code table. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ShowCodeTableById</td> 
<td>View code table details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCodeTable</td>
<td>Delete a code table. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCodeTableValues</td>
<td>Edit code table field values. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchCodeTables</td>
<td>Query the code table list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCodeTable</td>
<td>Create a code table. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Space Resource Permission Policy Management Interface</td>
<td>ShowSecurityResourcePermissionPolicy</td>
<td>Query a single resource permission policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteSecurityResourcePermissionPolicies</td>
<td>Batch delete resource permission policies</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityResourcePermissions</td>
<td>Query a list of space resource permission policies</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSecurityResourcePermissionPolicy</td>
<td>Create a spatial resource permission policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityResourcePermissionPolicy</td>
<td>Update a spatial resource permission policy</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Statistical asset interface</td>
<td>ShowTechnicalAssetsStatistic</td>
<td>Get technical asset statistics</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBusinessAssetsStatistic</td>
<td>Get business asset statistics</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Dimension interface</td>
<td>CreateDesignDimension</td>
<td>Create a new dimension based on the parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDesignDimension</td>
<td>Delete a dimension based on the dimension ID passed in. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesignDimension</td>
<td>Update dimension information based on the parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDimensionGroups</td>
<td>Query dimension granularity. Query all dimensions using tableId. Query all dimension groups granularity without tableId. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDimensionById</td>
<td>View dimension details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckDimensionStatus</td>
<td>Check the reverse dimension table task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDimensions</td>
<td>Search dimension information by Chinese and English name, description, creator, reviewer, status, l3Id, derived indicator idList, and modification time. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Dimension Table Interface</td>
<td>DeleteDesignDimensionLogicTable</td>
<td>Delete a dimension table based on its ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDimensionLogicTableById</td>
<td>View dimension table details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDimensionLogicTables</td>
<td>Search dimension table information by Chinese and English name, creator, reviewer, status, and modification time. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Gateway Management Interface</td>
<td>ListApicGroups</td>
<td>Get gateway groups. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApicInstances</td>
<td>Get gateway instances (exclusive edition). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Script development interface</td>
<td>ListFactoryScripts</td>
<td>This interface is used to query the script list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Custom item interface</td>
<td>SearchCustomizedFields</td>
<td>Query customized items (including table customizations, attribute customizations, theme customizations, and business indicator customizations). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyCustomizedFields</td>
<td>Modify customized fields (including table customizations, attribute customizations, theme customizations, and business indicator customizations). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Lineage Information</td>
<td>ShowUnrelatedTable</td>
<td>Unrelated Table Query</td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportLineage</td>
<td>Lineage Query</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowLineage</td>
<td>Lineage Query</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateLineageInfo</td>
<td>Create Lineage Information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Derivative Indicator Interface</td>
<td>ListDerivativeIndexes</td>
<td>Search for derived indicator information by Chinese/English name, creator, reviewer, status, modification time, and l3Id. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDerivativeIndexById</td>
<td>Get derived indicator details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDesignDerivativeIndex</td>
<td>Delete a derived indicator based on its ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesignDerivativeIndex</td>
<td>Update a derived indicator based on the passed parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDesignDerivativeIndex</td>
<td>Create a new derived index based on the parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Rule group interface</td>
<td>CreateSecurityDataClassificationRuleGroup</td>
<td>Create rule group interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityDataClassificationRuleGroups</td>
<td>Query rule group list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSecurityDataClassificationRuleGroup</td>
<td>Delete rule group interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityDataClassificationRuleGroup</td>
<td>Modify rule group interface</td>
<td>To be tested tested</td>
</tr>
<tr>
<td>ShowSecurityDataClassificationRuleGroup</td>
<td>Query rule group</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Rule template interface</td>
<td>BatchDeleteTemplates</td>
<td>Batch delete rule template</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTemplate</td>
<td>Update rule template</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTemplate</td>
<td>Create rule template</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQualityTemplates</td>
<td>Get rule template list by page</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTemplatesDetail</td>
<td>Get rule template details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">Identification rule interface</td>
<td>UpdateSecurityRuleEnableStatus</td>
<td>Modify identification rule status interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSecurityDataClassificationRule</td>
<td>Query a specific identification rule</td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckSecurityDataClassificationCombineRule</td>
<td>Combined identification rule testing</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityDataClassificationRules</td>
<td>Query the identification rule list</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteSecurityDataClassificationRule</td>
<td>Batch delete identification rule interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSecurityDataClassificationCombineRule</td>
<td>Create a combined identification rule</td><td>To be tested</td>
</tr>
<tr>
<td>DeleteSecurityDataClassificationRule</td>
<td>Delete identification rule</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityDataClassificationCombineRule</td>
<td>Modify combined identification rule</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSecurityDataClassificationRule</td>
<td>Modify identification rule interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSecurityDataClassificationRule</td>
<td>Create identification rule</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Quality work interface</td>
<td>ListQualityTask</td>
<td>Get the quality task list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowQualityTaskDetail</td>
<td>Get the quality task details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQualityTaskLists</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Quality Rule Interface</td>
<td>RemoveDesignQualityInfos</td>
<td>Clear the quality rules in the table. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDesignTableQuality</td>
<td>Updates the table's exception data output configuration, including whether to generate exception data, setting the exception data database or schema, and setting the exception table prefix/suffix. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Instance purchase interface</td>
<td>PayForDgcOneKey</td>
<td>DataArtsStudio instance one-key purchase interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Asset information</td>
<td>ShowDataProfile</td>
<td>Query summary</td>
<td>To be tested</td>
</tr>
<tr>
<td>RenewDataProfile</td>
<td>Specify field collection summary information interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDataPreview</td>
<td>Table data preview</td>
<td>To be tested tested</td>
</tr>
<tr>
<td rowspan="3">Asset Classification Interface</td>
<td>AssociateClassificationToEntity</td>
<td>Associate a classification to one or more assets with a specified GUID</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchAssociateClassificationToEntities</td>
<td>BatchAssociateClassificationToEntities: Only supports adding classifications to data table columns and OBS objects</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteClassificationFromEntities</td>
<td>Remove an asset association classification:</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Asset Leveling Interface</td>
<td>DeleteSecurityLevelFromEntity</td>
<td>Remove asset-associated security level</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchAssociateSecurityLevelToEntities</td>
<td>Batch-associate security levels: associate a single security level with multiple assets</td>
<td>To be tested</td>
</tr>
<tr>
<td>AssociateSecurityLevelToEntity</td>
<td>Associate assets to security levels, associate assets with specified security levels</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Asset Management Interface</td>
<td>UpdateEntityAttribute</td>
<td>Modify specified asset attributes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEntityInfoByGuid</td>
<td>Use the table GUID to obtain table details. Table details include column information. You can also directly obtain column information based on the column GUID.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEntities</td>
<td>Query technical assets</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrUpdateAsset</td>
<td>Add or modify assets</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAsset</td>
<td>Delete assets</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Operation and Maintenance Management Interface</td>
<td>ShowInstanceResult</td>
<td>Get Instance Results</td>
<td>To be tested</td></tr>
<tr>
<td>ListInstances</td>
<td>Get a list of task execution results</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Queue Permission Interface</td>
<td>UpdateSecurityAssignedQueue</td>
<td>Modify the queue resources allocated under the current space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSecurityAssignedQueue</td>
<td>Assign queue resources to the specified space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSecurityAssignedQueue</td>
<td>Delete the queue resources allocated under the current space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSecurityAssignedQueues</td>
<td>Query the queue resources assigned to the current space. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Qualification interface</td>
<td>ShowConditionById</td>
<td>View qualification details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCondition</td>
<td>Search for qualification information by Chinese/English name, description, creator, reviewer, qualification group ID, and modification time status. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Cluster management interface</td>
<td>ShowDataServiceInstance</td>
<td>Query cluster details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataServiceInstancesOverview</td>
<td>Query cluster overview information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataServiceInstancesDetail</td>
<td>Query cluster details. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>