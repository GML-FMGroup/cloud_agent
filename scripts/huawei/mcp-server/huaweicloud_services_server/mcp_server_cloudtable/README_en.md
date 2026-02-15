# CloudTable MCP Server


## Version
v0.1.0

## Overview

CloudTable MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CloudTable. Full-chain management of CloudTable resources can be carried out based on natural language.

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
<td rowspan="9">CloudTable cluster management interface</td> 
<td>ShowClusterDetail</td> <td>Use the cluster ID to uniquely identify a cluster. Query the details of a specific CloudTable cluster using the cluster ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCluster</td>
<td>Create a CloudTable cluster. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RebootCloudTableCluster</td>
<td>Restart the cluster API. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCluster</td>
<td>Use the cluster ID to uniquely identify a cluster. Delete the specified cluster using the cluster ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClusters</td>
<td>View the list of user-created clusters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateClusterSetting</td>
<td>Modify cluster configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>ExpandClusterComponent</td>
<td>Expand cluster nodes of a specified type</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowClusterSetting</td>
<td>Query cluster configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>EnableComponent</td>
<td>Enable the opentsdb component</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">CloudTable cluster management interface v3</td>
<td>CreateCloudTableCluster</td>
<td>Create a CloudTable cluster. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>