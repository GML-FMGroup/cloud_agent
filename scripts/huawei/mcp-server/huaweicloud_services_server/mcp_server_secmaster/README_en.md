# SecMaster MCP Server 


## Version
v0.1.0

## Overview

SecMaster MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service SecMaster. Full-chain management of SecMaster resources can be carried out based on natural language.

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
<td rowspan="3">Event relationship management</td> 
<td>DeleteDataobjectRelations</td> <td>Disassociate Dataobject</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataobjectRelations</td>
<td>Query the list of associated Dataobjects</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDataobjectRelations</td>
<td>Associate Dataobject</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Incident Management</td>
<td>CreateIncident</td>
<td>Create an incident</td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeIncident</td>
<td>Edit an incident and update it based on the modified properties. Unmodified columns will not be updated.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListIncidents</td>
<td>Search the incident list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowIncident</td>
<td>Get incident details</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteIncident</td>
<td>Delete incident</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Playbook action management</td>
<td>CreatePlaybookAction</td>
<td>Create playbook action</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPlaybookActions</td>
<td>Query the playbook action list</td>
<td>To be tested tested</td>
</tr>
<tr>
<td>DeletePlaybookAction</td>
<td>Delete playbook action</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePlaybookAction</td>
<td>Update playbook action</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Playbook instance management</td>
<td>ShowPlaybookInstance</td>
<td>Show playbook instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangePlaybookInstance</td>
<td>Operate playbook instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPlaybookTopology</td>
<td>Query playbook topology relationships</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPlaybookInstances</td>
<td>Query playbook instance list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPlaybookAuditLogs</td>
<td>Query playbook instance audit logs</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Playbook Approval Management</td>
<td>ListPlaybookApproves</td>
<td>Query playbook approval results</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePlaybookApprove</td>
<td>Approve playbook</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Playbook Version Management</td>
<td>ListPlaybookVersions</td>
<td>Query the playbook version list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPlaybookVersion</td>
<td>Show playbook version</td>
<td>To be tested</td>
</tr>
<tr>
<td>CopyPlaybookVersion</td>
<td>Clone playbook and version</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePlaybookVersion</td>
<td>Delete playbook version</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePlaybookVersion</td>
<td>Update playbook version</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePlaybookVersion</td>
<td>Create playbook version</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Playbook management</td>
<td>CreatePlaybook</td>
<td>Create playbook</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPlaybook</td>
<td>Query playbook details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPlaybookMonitors</td>
<td>Playbook operation monitoring</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPlaybooks</td>
<td>Query playbook list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePlaybook</td>
<td>Delete playbook</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPlaybookStatistics</td>
<td>Playbook statistics</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePlaybook</td>
<td>Modify playbook</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Playbook rule management</td>
<td>UpdatePlaybookRule</td>
<td>Update playbook rule</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePlaybookRule</td>
<td>Delete playbook rule</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPlaybookRule</td>
<td>Query playbook rule details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePlaybookRule</td>
<td>Create playbook rule</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Alarm Management</td>
<td>CreateAlert</td>
<td>Create Alert</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateBatchOrderAlerts</td>
<td>Convert Alert to Event</td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeAlert</td>
<td>Edit an alert and update it based on the modified properties. Unmodified columns will not be updated.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAlerts</td>
<td>Search the alert list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAlert</td>
<td>Get alert details</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAlert</td>
<td>Delete an alert</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="11">Alarm rule management</td> 
<td>CreateAlertRuleSimulation</td> 
<td>Simulate alert rule</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ShowAlertRuleTemplate</td> 
<td>List alert rule templates</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ListAlertRuleTemplates</td> 
<td>List alert rule templates</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>DeleteAlertRule</td> 
<td>Delete alert rule</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ShowAlertRule</td> 
<td>View alert rules Get alert rule</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>DisableAlertRule</td> 
<td>Disable alert rule</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ListAlertRuleMetrics</td> 
<td>List alert rule metrics</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateAlertRule</td> 
<td>Create alert rule</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ListAlertRules</td> 
<td>List alert rules</td> 
<td>To be tested</td>
</tr>
<tr>
<td>EnableAlertRule</td>
<td>Enable alert rule</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAlertRule</td>
<td>Update alert rule</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Baseline Check</td>
<td>SearchBaseline</td>
<td>Search Baseline Check Results List</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Threat Intelligence Management</td>
<td>DeleteIndicator</td>
<td>Delete Threat Intelligence</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateIndicator</td>
<td>Create Threat Intelligence</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListIndicators</td>
<td>Query Threat Intelligence List</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowIndicatorDetail</td>
<td>Query Threat Intelligence Details</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateIndicator</td>
<td>Update Threat Intelligence</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Workspace Management</td>
<td>DeleteWorkspace</td>
<td>Delete Workspace</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkspace</td>
<td>Update workspace name, description, and other information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkspaces</td>
<td>Filter tenant workspaces by workspace name, description, creation time, and other criteria. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkspace</td>
<td>Query workspace name, description, and other details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkspace</td>
<td>Before using Security Cloud Brain's baseline check, alert management, security analysis, and security orchestration features, you need to create a workspace. This divides resources into different work scenarios, avoiding redundant resources that can be inconvenient to find and affect daily use. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Metric query</td>
<td>BatchSearchMetricHits</td>
<td>Batch query metric results</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Dataspace management</td>
<td>CreateDataspace</td>
<td>Create dataspace</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Dataclass management</td>
<td>ListDataclass</td>
<td>Query dataclass list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataclassFields</td>
<td>Query field list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Process instance management</td>
<td>OperateWorkflowInstance</td>
<td>Operate process instance</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Process management</td>
<td>ListWorkflows</td>
<td>Query process list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Pipeline management</td>
<td>CreatePipe</td>
<td>Create data pipeline</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Metering and billing management</td>
<td>CreatePostPaidOrder</td>
<td>Activate the Secure Cloud Brain On-Demand Service</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>