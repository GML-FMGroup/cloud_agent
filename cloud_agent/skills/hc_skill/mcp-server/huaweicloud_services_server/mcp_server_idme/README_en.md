# iDME MCP Server


## Version
v0.1.0

## Overview

iDME MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service iDME. Full-chain management of iDME resources can be carried out based on natural language.

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
<td rowspan="4">Application management</td> 
<td>CreateXdmApplication</td> <td>This interface is used to create an Industrial Digital Model Engine (iDME) application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApps</td>
<td>This interface is used to obtain a tenant's list of applications in the Industrial Digital Model Engine (iDME). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyApplication</td>
<td>This interface is used to modify an Industrial Digital Model Engine (iDME) application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteXdmApplication</td>
<td>This interface is used to delete an Industrial Digital Model Engine (iDME) application. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Run Service Management</td>
<td>SubscribeCloudService</td>
<td>This interface is used to activate an Industrial Digital Model Engine (iDME) instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCloudService</td>
<td>This interface is used to delete an Industrial Digital Model Engine (iDME) instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeployApplication</td>
<td>This interface is used to deploy an Industrial Digital Model Engine (iDME) application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEnvs</td>
<td>This interface is used to obtain a tenant's list of running services in the Industrial Digital Model Engine (iDME). </td>
<td>To be tested</td>
</tr>
<tr>
<td>Uninstall</td>
<td>This interface is used to uninstall the Industrial Digital Model Engine (iDME) application under the specified running service. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>