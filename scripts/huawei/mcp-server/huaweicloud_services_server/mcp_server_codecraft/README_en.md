# CodeCraft MCP Server

## Version Information
v0.1.0

## Product Description

CodeCraft MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud CodeCraft. It enables full-link management of CodeCraft resources based on natural language processing.

## Available Tools
Covering the entire API, available for use as needed. The list and status are as follows:

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
<td rowspan="4">Entry Management</td>
<td>UpdateCompetitionScore</td>
<td>For submissions to the competition platform: After the third-party service scores the entry, it calls this API based on the entry ID and returns information such as the score and status to the competition platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RegisterCompetitionInfo</td>
<td>The third-party service verifies whether the user has registered on the competition platform, formed a team, and can submit a work. If you've registered but haven't formed a team, a virtual team will be created and allowed to submit works. If you've already formed a team, the deadline for submitting works will be used to determine whether you can submit your work. Returns the team ID and whether you can submit your work.

<td>To be tested</td>

</tr>

<tr>
<td>ListCompetitionWorks</td>
<td>A third-party service retrieves information about works submitted during a specific period of time within a competition. The query range is defined as the previous day or hour, using the request parameter read_time as the end time.
<td>To be tested</td>
</tr>
<tr>
<td>CreateCompetitionScore</td>
<td>For third-party submissions: After the third-party service has scored the work, it calls this API to return the work information and score to the competition platform.
<td>To be tested</td>

</tr>

</tbody>

</table>

</body>
</html>