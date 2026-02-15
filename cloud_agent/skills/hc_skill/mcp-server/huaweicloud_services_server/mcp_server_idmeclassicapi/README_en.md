#iDMEClassicAPI MCP Server


## Version
v0.1.0

## Overview

iDMEClassicAPI MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service iDMEClassicAPI. Full-chain management of iDMEClassicAPI resources can be carried out based on natural language.

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
<td rowspan="1">Business code generator</td> <td>GenerateBusinessCode</td>
<td>Call this API to generate a business code for a data instance of a specified model. Before calling this API, ensure that the data model has the "Business Code Generator" function. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Relationship Entity Service</td>
<td>ListQueryRelatedObjects</td>
<td>Call this API to query all instance information of the source/target models associated with a specified relationship entity, including specific properties. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTarget</td>
<td>Call this API to enter the data instance ID of the source model and the English name of the target model to delete the data instance of the corresponding relationship entity. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQueryRelationship</td>
<td>Call this interface to enter the data instance ID and the corresponding relationship role (source/target model) to query and return the data instance of the corresponding relationship entity. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBatchQueryRelatedObjects</td>
<td>Call this interface to batch query all instance information of the source/target model associated with the specified relationship entity, including specific attributes. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQueryTarget</td>
<td>Call this interface to enter the data instance ID of the source model to query and return the data instance information of the target model associated with the instance. The instance information includes the "list attributes" of the corresponding data instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="24">Basic Data Service</td>
<td>ShowLogicalDeleteUsingPost</td>
<td>Soft-delete a data instance in the specified data model based on the data instance's unique ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUsingPost</td>
<td>Returns basic model attribute information in pages based on query conditions, without cascading queries (extended attributes are not supported as query conditions). </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteLogicalUsingPost</td>
<td>Soft-delete multiple data instances in the specified data model based on their unique IDs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStaticsPage</td>
<td>Query statistical information of data instances by page, supporting grouping and simple function paging statistics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountUsingPost</td>
<td>Count the total number of instances in the specified data model based on the specified query conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteUsingPost</td>
<td>Batch delete multiple data instances in the specified data model based on their unique IDs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQueryUsingPost</td>
<td>When the data model has a property with "List Attribute" set to "Yes", this interface can be used to query instance data in the data model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowLogicalDeleteByConditionUsingPost</td>
<td>Use this interface to soft-delete instances returned by a query with a specified condition. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateUsingPost</td>
<td>Create a data instance for the specified data model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateUsingPost</td>
<td>Create data instances of the specified data model in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveAsUsingPost</td>
<td>The version object's saveAs interface (saveAs) is used to create a data instance with the same data as the original version object instance. This instance data completely copies the existing data of the original instance, including its associated master and branch objects, and the version number of the new instance data is calculated starting from the initial value. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteUsingPost</td>
<td>Delete a data instance in the specified data model based on the data instance's unique identifier. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGetByUniqueKey</td>
<td>When a property with "Unique Key" set to "Yes" exists in the data model, instance data can be queried based on that property. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchShowGetUsingPost</td>
<td>Batch query instance details based on the unique codes of multiple data instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteByConditiontionUsingPost
<td>Use this interface to delete instances that meet the specified conditions.</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateUsingPost</td>
<td>Batch update multiple instance data in a specified data model. If the unique code for an instance does not exist, no update is performed on that instance.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateByConditionUsingPost</td>
<td>Update instances of the specified model based on the specified conditions.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSelectUsingPost</td>
<td>Returns pages based on the query conditions and specified properties (extended properties are not supported as selected property columns). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStaticsUsingPost</td>
<td>According to the specified function, statistics are collected for instances of the specified data model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowFindUsingPost</td>
<td>Query all instances in the specified data model by page. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveUsingPost</td>
<td>When a data model has an attribute with a "unique key" value of "yes", the data in the specified field of the instance in the data model can be updated based on the English name of the attribute. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUsingPost</td>
<td>Updates the data of an instance in the specified data model. If the instance's unique code does not exist, no update is performed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGetUsingPost</td>
<td>Query the detailed information of a data instance based on its unique code. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveAllUsingPost</td>
<td>When a property with "Unique Key" set to "Yes" exists in the data model, all fields in the instance in the data model can be updated based on the property's English name. If the updated instance does not exist, the system will automatically create the instance data. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Multidimensional View and Multidimensional Branch</td>
<td>UpdateView</td>
<td>Call this interface to update the multidimensional view of the specified M-V model entity. Before calling this interface, ensure that the data model has the "Multidimensional View & Multidimensional Branch" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateView</td>
<td>Call this interface to batch create multidimensional views of the specified M-V model entities. Before calling this interface, ensure that the data model has the "Multidimensional View & Multidimensional Branch" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateView</td>
<td>Call this interface to create multidimensional views of the specified M-V model entities. Before calling this interface, ensure that the data model supports the "Multi-dimensional View & Multi-dimensional Branching" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Invalidation Management</td>
<td>EnableDataInstance</td>
<td>Call this interface to enable data instances of the specified model and return the number of successfully enabled instances. Before calling this interface, ensure that the data model supports the "Invalidation Management" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DisableDataInstance</td>
<td>Call this interface to disable data instances of the specified model and return the number of successfully disabled instances. Before calling this interface, ensure that the data model supports the "Invalidation Management" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Data category management</td>
<td>RemoveFromCategory</td>
<td>Remove a data category instance from a data category object instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddToCategory</td>
<td>Add a data category object instance to a data category instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Tag management</td>
<td>ShowTag</td>
<td>Call this API to query the tag information corresponding to the data instance of the specified model. Before calling this API, ensure that the data model has the "Tag management" function. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddTag</td>
<td>Call this API to bind a tag to a data instance of a specified model. Before calling this API, ensure that the data model has the "Tag Management" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RemoveTag</td>
<td>Call this API to unbind a tag from a data instance of a specified model. Before calling this API, ensure that the data model has the "Tag Management" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Tree Structure</td>
<td>BatchAddChildNode</td>
<td>Call this API to batch add child nodes to a specified data instance. Before calling this API, ensure that the data model has the "Tree Structure" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGetRoot</td>
<td>Call this interface to get the root node of the specified data instance. Before calling this interface, ensure that the data model has the "tree structure" function. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGetChildList</td>
<td>Call this interface to get the child nodes of the specified data instance and return its list property. Before calling this interface, ensure that the data model has the "tree structure" function. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Refresh</td>
<td>Call this interface to refresh the full path of the node corresponding to the specified data instance. Before calling this interface, ensure that the data model has the "tree structure" function. </td>
<td>To be tested</td></tr>
<tr>
<td>ListGetAllParentList</td>
<td>Call this interface to retrieve all parent nodes of a specified data instance and return their list properties. Before calling this interface, ensure that the data model supports the "tree structure" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGetParent</td>
<td>Call this interface to retrieve the parent nodes of a specified data instance and return their list properties. Before calling this interface, ensure that the data model supports the "tree structure" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRemoveChildNode</td>
<td>Call this interface to batch remove all child nodes of a specified data instance. Before calling this interface, ensure that the data model supports the "tree structure" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="30">Version Service</td>
<td>BatchUpdateByAdmin</td>
<td>Administrators use this interface to batch update the data of specified instances of a specified M-V model. If the unique ID of an instance does not exist, no update operation is performed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAndCheckin</td>
<td>Use this interface to update a specified M-V model instance and check it in. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckoutAndUpdate</td>
<td>Checks out and updates an M-V model data instance based on the primary object ID. This means that after checking out, a new data instance is generated and the information of the new instance is updated. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckoutUndoByAdmin</td>
<td>An administrator uses this interface to undo the checkout of a specified M-V model instance, restoring the instance data to its pre-checkout state. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLogicalLatestVersion</td>
<td>Soft-deletes the latest version of the instance data in the latest branch under the version object based on the master object ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLatestVersion</td>
<td>Deletes the latest version of the instance data in the latest branch under the version object based on the master object ID. Use the delete operation with caution, as deleted data cannot be recovered. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowVersionByMaster</td>
<td>Query detailed version information for the M-V model instance based on the master object ID, iteration version, and version number. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCheckout</td>
<td>Batch check out M-V model data instances based on the master object ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCheckin</td>
<td>Batch check in M-V model data instances based on the master object ID. A new iteration version is generated for the checked-in data instances, and the data is stored in the system. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCheckoutAndUpdate</td>
<td>Batch checkout and update M-V model data instances based on the master object ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAllVersions</td>
<td>According to the master object ID, obtain all version information (including attribute information under the corresponding version) for the corresponding M-V model instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateAndCheckin</td>
<td>Use this interface to batch update specified M-V model instances and check them in. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteBranch</td>
<td>Deletes all minor versions under the latest major version based on the parent model ID and version object. Please use the delete operation with caution, as the data cannot be recovered after deletion. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateVersion</td>
<td>Based on the unique ID of an M-V model entity, batch updates the version numbers of instances under that entity to the latest version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteRevise</td>
<td>Use this interface to revise a specified M-V model instance. After revision, the instance's "version.revision" will be updated to the new revision. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCheckoutUndo</td>
<td>Use this interface to batch undo the checkout of a specified M-V model instance, restoring the instance data to the content before the checkout. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteLogicalBranch</td>
<td>Based on the master object ID, batch soft-delete all minor versions under the latest major version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CompareBusinessVersion</td>
<td>Use this interface to compare the attributes and relationships of different versions of an M-V model data instance. We recommend using the new difference comparison feature in the data modeling engine (xDM Foundation, xDM-F), using the instance-attrs-comparison and instance-relation-comparison APIs. For more information, see "Data Service Management > Full Data Service > System Management API > Attribute Comparison API" in the running application.

<td>To be tested</td>

<tr>
<td>UpdateByAdmin</td>
<td>Administrators use this API to update the data of a specified instance in a specified M-V model. If the instance's unique identifier does not exist, no update is performed.

<td>To be tested</td>

</tr>
<tr>
<td>BatchDeleteLogicalLatestVersion</td>
<td>Soft-deletes the latest version of the instance data in the latest branch of a version object based on its master object ID. It is recommended that no more than 100 master object IDs be set in a single call to this API. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>BatchDeleteLatestVersion</td>
<td>Batch deletes the latest version instance data of the latest branch under a version object based on the master object ID. It is recommended that no more than 100 master object IDs be set in a single call to this API. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Checkin</td>
<td>Check in the M-V model data instance based on the master object ID. A new iteration version is generated for the checked-in data instance, and the data is stored in the system. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckoutUndo</td>
<td>Use this API to undo the checkout of a specified M-V model instance, restoring the instance data to its pre-checkout state. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAndRevise</td>
<td>Revises and updates the M-V model data instance based on the master object ID. That is, the "version.revision" of the revised instance is updated to the new revision, and the instance information is updated at the same time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLogicalBranch</td>
<td>Soft-deletes all iterations of the latest branch under the M-V model instance based on the parent model ID and version object. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateAndRevise</td>
<td>Revises and updates the M-V model data instance in batches based on the master object ID. That is, the "version.revision" of the revised instance is updated to the new revision, and the instance information is updated at the same time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCheckoutUndoByAdmin</td>
<td>Administrators use this interface to batch-undo checkouts of specified M-V model instances, restoring the instance data to the pre-checkout state. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchExecuteRevise</td>
<td>Use this interface to batch-revise specified M-V model instances. After revision, the instance's "version.revision" will be updated to the new revision. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteBranch</td>
<td>Batch-soft-delete all minor versions under the latest major version based on the master object ID and parent model ID. Use the delete operation with caution, as deleted data cannot be recovered. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Checkout</td>
<td>Checks out the M-V model data instance based on the primary object ID. After checkout, a new data instance is generated, completely replicating the existing information of the original instance and changing its status to checked out. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Lifecycle Management</td>
<td>SwitchLifecycleTemplate</td>
<td>Call this interface to switch the lifecycle template bound to the data instance of the specified model. When switching the lifecycle template, you must specify the lifecycle state for the data instance. Before calling this interface, ensure that the data model has the "Lifecycle Management" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateState</td>
<td>Call this interface to modify or switch the lifecycle state of the data instance. Before calling this API, ensure that the data model has the "Lifecycle Management" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">System Version</td>
<td>ListHistoryData</td>
<td>After calling this API and entering the statistical time interval (start and end time) for a specified model, historical version information for that instance will be retrieved in pages using the last modification time of the data instance as the query condition. Before calling this API, ensure that the data model has the "System Version" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CollectHistoryData</td>
<td>After entering the statistical time interval (start and end time) for a specified model, statistical data for that model will be retrieved, including data on created, deleted, soft-deleted, and updated instances. Before calling this API, ensure that the data model has the "System Version" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CompareVersion</td>
<td>This API allows you to compare the attributes and relationships of different versions of a model data instance. We recommend using the new difference comparison functionality of the data modeling engine (xDM Foundation, xDM-F), namely the instance-attrs-comparison and instance-relation-comparison APIs. For more information, see "Data Service Management > Full Data Service > System Management API > Attribute Comparison API" in the application runtime state. Before calling this API, ensure that the data model has the "System Version" feature. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Structured Document Management</td>
<td>ShowGetTokens</td>
<td>This API can be used to obtain a structured document token by authenticating using the document ID and authentication type. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQueryDocuments</td>
<td>Query structured documents. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQueryShareDocs</td>
<td>Query the list of structured document sharing permissions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDocument</td>
<td>Update the document title. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteShareDocs</td>
<td>Batch delete structured document sharing permissions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateShareDocs</td>
<td>Create shared structured documents in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteStructuredDocument</td>
<td>Delete structured documents in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDocument</td>
<td>Create structured documents. </td>
<td>To be tested</td>
</tr>
<tr><td>BatchUpdateDocument</td>
<td>Batch updates structured documents. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>