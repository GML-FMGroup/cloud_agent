# Config MCP Server

## Version Information
v0.1.0

## Product Description

Config MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud Service Config. It enables full-link management of Config resources using natural language.

## Available Tools

Covering the full API, available for on-demand use. The list and status are as follows:

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
<td rowspan="19">Aggregator</td>
<td>RunAggregateResourceQuery</td>
<td>Executes an advanced query on the specified aggregator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAggregateDiscoveredResources</td>
<td>Query the resource aggregator for a list of specific resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAggregatePolicyAssignmentDetail</td>
<td>Return details of the specified aggregate's compliance policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateConfigurationAggregator</td>
<td>Create a resource aggregator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAggregationAuthorization</td>
<td>Grant the resource aggregator account permission to collect data from the source account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePendingAggregationRequest</td>
<td>Delete pending authorization requests from the aggregator account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAggregateComplianceByPolicyAssignment</td>
<td>Query the list of compliant and non-compliant rules, including the number of compliant and non-compliant resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteConfigurationAggregator</td>
<td>Delete a resource aggregator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateConfigurationAggregator</td>
<td>Update a resource aggregator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowConfigurationAggregatorSourcesStatus</td>
<td>Query the status of the aggregation account of the specified resource aggregator. The status includes information about verifying the authorization between the source account and the aggregator account. If failed, the status includes a relevant error code or message. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAggregatePolicyStateComplianceSummary</td>
<td>Query the number of compliant and non-compliant rules for one or more accounts in the aggregator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowConfigurationAggregator</td>
<td>Query the specified resource aggregator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAggregateComplianceDetailsByPolicyAssignment</td>
<td>Returns detailed evaluation results for the specified aggregation compliance rule. This includes which resources were evaluated and whether each resource complies with the rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAggregationAuthorizations</td>
<td>Query the list of authorized resource aggregators. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPendingAggregationRequests</td>
<td>Query the list of all pending aggregation requests. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAggregationAuthorization</td>
<td>Delete the authorization for the specified resource aggregator account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConfigurationAggregators</td>
<td>Query the resource aggregator list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAggregateDiscoveredResourceCounts</td>
<td>Query the resource count for the aggregator account. Supports filtering and GroupByKey. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAggregateResourceConfig</td>
<td>Query the details of a specific resource in the source account. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="18">ConformancePack</td>
<td>ListConformancePackComplianceScores</td>
<td>List the user's compliance rule pack scores. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOrganizationConformancePackDetailedStatuses</td>
<td>View the deployment status details of the specified organization's compliance rule pack in the member account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOrganizationConformancePack</td>
<td>Get the details of a single organization's compliance rule pack by ID. </td>
<td>To be tested</td>
</tr>
<tr><td>CollectConformancePackComplianceSummary</td>
<td>Lists the compliance results summary for the user's compliance rule package. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConformancePackComplianceDetailsByPackId</td>
<td>Lists the compliance rule evaluation results details for the compliance rule package. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConformancePackComplianceByPackId</td>
<td>Lists the compliance rule evaluation results for the compliance rule package. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateOrganizationConformancePack</td>
<td>Updates the user's organization compliance rule package. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOrganizationConformancePacks</td>
<td>Lists the user's organization compliance rule packs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBuiltInConformancePackTemplates</td>
<td>Lists the predefined compliance rule pack templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOrganizationConformancePackStatuses</td>
<td>Lists the user's organization compliance rule pack deployment status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConformancePacks</td>
<td>Lists the user's compliance rule packs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateConformancePack</td>
<td>Create a new compliance rule package. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateConformancePack</td>
<td>Update the user's compliance rule package. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBuiltInConformancePackTemplate</td>
<td>Get a single predefined compliance rule package template by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrganizationConformancePack</td>
<td>Create a new organization compliance rule package. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteConformancePack</td>
<td>Delete the user's compliance rule pack. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteOrganizationConformancePack</td>
<td>Delete the user's organization compliance rule pack. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowConformancePack</td>
<td>Get a single compliance rule pack by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">History</td>
<td>ShowResourceHistory</td>
<td>Query the change history of resources and resource relationships</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="31">Policy</td>
<td>CreateOrganizationPolicyAssignment</td>
<td>Create an organization compliance rule. If the rule name already exists, it will be an update operation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRemediationConfiguration</td>
<td>Delete the compliance rule remediation configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOrganizationPolicyAssignment</td>
<td>Query the compliance rules for a specified organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteRemediationExceptions</td>
<td>Batch delete compliance rule remediation exceptions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePolicyAssignment</td>
<td>Update a user's compliance rules</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyStatesByDomainId</td>
<td>Query all compliance results for a user</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOrganizationPolicyAssignmentDetailedStatus</td>
<td>Query the detailed status of compliance rule deployment for each member account in the organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePolicyAssignments</td>
<td>Create a new compliance rule</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOrganizationPolicyAssignmentStatuses</td>
<td>Query the deployment status of the organization's compliance rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyAssignments</td>
<td>List the user's compliance rules</td>
<td>To be tested</td>
</tr><tr>
<td>DeletePolicyAssignment</td>
<td>Delete this rule by rule ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyStatesByResourceId</td>
<td>Query all compliance results by resource ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOrUpdateRemediationConfiguration</td>
<td>Create or update a compliance rule remediation configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBuiltInPolicyDefinition</td>
<td>Query a single built-in policy by policy ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateRemediationExceptions</td>
<td>Batch create compliance rule remediation exceptions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPolicyAssignment</td>
<td>Get a single rule by rule ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEvaluationStateByAssignmentId</td>
<td>Query the evaluation state of this rule by rule ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>DisablePolicyAssignment</td>
<td>Disable this rule by rule ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyStatesByAssignmentId</td>
<td>Query all compliance results by rule ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePolicyState</td>
<td>Update the compliance assessment results of user-defined compliance rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOrganizationPolicyAssignments</td>
<td>Query the list of organization compliance rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRemediationConfiguration</td>
<td>Query the compliance rule remediation configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRemediationExecutionStatuses</td>
<td>Query the compliance rule remediation execution results. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CollectRemediationExecutionStatusesSummary</td>
<td>List the latest compliance rule remediation records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteOrganizationPolicyAssignment</td>
<td>Delete the organization compliance rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBuiltInPolicyDefinitions</td>
<td>List the user's built-in policies. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RunRemediationExecution</td>
<td>Manually run the compliance rule remediation execution. </td>
<td>To be tested</td>
</tr>
<tr>
<td>EnablePolicyAssignment</td>
<td>Enable this rule by rule ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateOrganizationPolicyAssignment</td>
<td>Update the organization compliance rule</td>
<td>To be tested</td>
</tr>
<tr>
<td>RunEvaluationByPolicyAssignmentId</td>
<td>Evaluate this rule by rule ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRemediationExceptions</td>
<td>Query the remediation exceptions for the compliance rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Query</td>
<td>ListStoredQueries</td>
<td>List all advanced queries</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSchemas</td>
<td>List Schemas</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStoredQuery</td>
<td>Show Resource Query Language</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStoredQuery</td>
<td>Delete a single advanced query</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStoredQuery</td>
<td>Update Custom Query</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateStoredQuery</td>
<td>Create New Advanced Query</td>
<td>To be tested</td>
</tr>
<tr>
<td>RunQuery</td>
<td>Execute an advanced query</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Region</td>
<td>ListRegions</td>
<td>Query user-visible regions</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Relations</td>
<td>ShowResourceRelationsDetail</td>
<td>Specifies a resource ID and queries the relationships between that resource and other resources. The relationship direction can be specified as "in" or "out". This requires the account to have the rms:resources:getRelation permission. Resource relationships depend on enabling the resource recorder. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowResourceRelations</td>
<td>Specify a resource ID and query its relationships with other resources. You can specify the relationship direction as "in" or "out". Resource relationships require the resource logger to be enabled. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="13">Resource</td>
<td>CollectAllResourcesSummary</td>
<td>Query the resource summary of the current account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAllTags</td>
<td>Query the tags of all resources in the current account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAllResources</td>
<td>Returns all resources under the current user. Requires the current user to have the rms:resources:list permission. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowResourceDetail</td>
<td>Query a single resource under the current account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountTrackedResources</td>
<td>Query the number of resources collected by the current user's resource logger. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CollectTrackedResourcesSummary</td>
<td>Query a summary of resources collected by the current user's resource logger. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTrackedResources</td>
<td>Query all resources collected by the current user's resource recorder. Requires the current user to have the rms:resources:list permission. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListProviders</td>
<td>Query the list of cloud services, resources, and regions supported by the Config. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListResources</td>
<td>Returns resources of a specific resource type under the current tenant. Requires the current user to have the rms:resources:list permission. For example, to query cloud servers, the corresponding Config resource type is ecs.cloudservers, where provider is ecs and type is cloudservers. For information on supported services and resource types for Config, see [Supported Services and Regions](https://console.huaweicloud.com/eps/#/resources/supported). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowResourceById</td>
<td>Specifies a resource ID and returns detailed information about that resource. This requires the current user to have the rms:resources:get permission. For example, to query cloud servers, the corresponding Config resource type is ecs.cloudservers, where the provider is ecs and the type is cloudservers. For information on supported services and resource types for Config, see [Supported Services and Regions](https://console.huaweicloud.com/eps/#/resources/supported). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTrackedResourceTags</td>
<td>Query the resource tags collected by the current user's resource logger. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTrackedResourceDetail</td>
<td>Query a single resource collected by the current user's resource recorder. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountAllResources</td>
<td>Query the number of resources in the current account. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Tag</td>
<td>ListTagsForResourceType</td>
<td>Query all resource tag sets for a tenant's instance type in a specified project. The tag management service needs to be able to list all resource tag sets used by the current tenant and provide tag association functionality when tagging resources and filtering instances in each service console. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTagsForResource</td>
<td>Query the tag information of a specified instance. The tag management service needs to use this interface to query all tag data for a specified instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>TagResource</td>
<td>This interface is idempotent. It allows you to add or remove tags in batches for specified instances. The tag management service needs to use this interface to manage instance tags in batches. A resource can have a maximum of 20 tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListResourcesByTag</td>
<td>Use tags to filter instances. The tag management service needs to filter service instances by tag and display them in a list. Each service needs to provide query capabilities. Note: The tags, tags_any, not_tags, and not_tags_any fields support the maximum number of tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UnTagResource</td>
<td>This interface is idempotent. It allows you to add or remove tags in batches for specified instances. The tag management service uses this interface to manage instance tags in batches. A resource can have a maximum of 20 tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountResourcesByTag
<td>To filter instances using tags, the tag management service must filter service instances by tag and display them in a list. Each service must provide query capabilities. Note: The tags, tags_any, not_tags, and not_tags_any fields limit the number of tags supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Tracker</td>
<td>CreateTrackerConfig</td>
<td>Create or update a resource recorder. Only one resource recorder can exist.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTrackerConfig</td>
<td>Delete a resource recorder.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTrackerConfig</td>
<td>Query detailed information about a resource recorder.</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>