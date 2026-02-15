# DeH MCP Server


## Version
v0.1.0

## Overview

DeH MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DeH. Full-chain management of DeH resources can be carried out based on natural language.

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
<td rowspan="2">Query API version information</td> 
<td>ShowDehVersion</td> <td>Returns information about the specified version of a dedicated host. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDehVersions</td>
<td>Returns a list of all currently available versions of a dedicated host. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Tag Management</td>
<td>BatchCreateDedicatedHostTags</td>
<td>Add tags to specified dedicated hosts in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteDedicatedHostTags</td>
<td>Delete tags from specified dedicated hosts in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDedicatedHostTags</td>
<td>Query the tag information of a specified dedicated host. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDedicatedHostsByTags</td>
<td>Filter the list of dedicated hosts by tags and return all tags used by dedicated hosts. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Lifecycle Management</td>
<td>ShowDedicatedHost</td>
<td>Query the details of a specific dedicated host. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServersDedicatedHost</td>
<td>Query information about cloud servers deployed on a dedicated host. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDedicatedHost</td>
<td>This API is used to change the "auto_placement" and "name" properties of a dedicated host. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDedicatedHostTypes</td>
<td>Query the types of dedicated hosts available in a specific AZ. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDedicatedHosts</td>
<td>Use this API to query the list of dedicated hosts. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Quota Settings</td>
<td>ShowQuotaSets</td>
<td>This interface is used to query a tenant's dedicated host quota. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>