# CodeCheck MCP Server

## Version Information
v0.1.0

## Product Description

CodeCheck MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud CodeCheck. It enables full-link management of CodeCheck resources using natural language.

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
<td rowspan="18">Task Management</td>
<td>StopTaskById</td>
<td>Terminate a check task based on its ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTask</td>
<td>Delete the inspection task. Executing tasks cannot be viewed after deletion.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTaskRuleset</td>
<td>Modify the task rule set. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTasklog</td>
<td>Query the task check failure log. If the execute_id is not passed, the most recent check log will be queried.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskSettings</td>
<td>Query the task's advanced options.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckParameters</td>
<td>Query the check parameters of the task rule set.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTaskParameter</td>
<td>Task configuration check parameters.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskPathTree</td>
<td>Get the task's directory tree</td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckRulesetParameters</td>
<td>Query the check parameters of the task's rule set</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTaskSettings</td>
<td>Configure advanced task options, such as custom images</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTask</td>
<td>Create a new check task but do not execute it.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTasksRulesets</td>
<td>Query the list of selected rule sets for the task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProgressDetail</td>
<td>Query the task execution status based on the task ID. Task status: 0 indicates checking, 1 indicates check failure, 2 indicates check success, and 3 indicates task aborted. Progress details are only available for tasks currently being checked. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskListByProjectId</td>
<td>Query the task list for the project under DEVCLOUD_PROJECT_UUID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckRecord</td>
<td>Provides statistics on the number of issues per scan. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTaskRuleset</td>
<td>Query the list of selected rule sets for the task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RunTask</td>
<td>Execute the check task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateIgnorePath</td>
<td>Task configuration shielding directory</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Defect management</td>
<td>ShowTaskDefectsStatistic</td>
<td>Query defect details statistics based on inspection task ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDefectStatus</td>
<td>Change the status of detected defects to resolved or ignored</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskDetail</td>
<td>Query the summary of defect results based on inspection task ID. Includes issue overview, issue status, cyclomatic complexity, code duplication rate, etc. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskCmetrics</td>
<td>Query the Cmetrics defect summary based on the inspection task ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskDefects</td>
<td>Query the defect result details by page based on the inspection task ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Rule Management</td>
<td>ListRulesets</td>
<td>Query the rule set list based on project ID, language, etc. </td>
<td>To be tested</td>
</tr>
<tr><td>CreateRuleset</td>
<td>Flexibly combine rules based on your needs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTemplateRules</td>
<td>Query the rule list based on conditions such as project ID and rule set ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRuleset</td>
<td>Delete a custom rule set. Active or default rule sets cannot be deleted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetDefaulTemplate</td>
<td>Set the default rule set configuration for each project's language. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRules</td>
<td>Query the rule list based on language, question level, etc. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>