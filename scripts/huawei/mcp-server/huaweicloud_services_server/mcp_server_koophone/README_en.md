# KooPhone MCP Server


## Version
v0.1.0

## Overview

KooPhone MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KooPhone. Full-chain management of KooPhone resources can be carried out based on natural language.

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
<td rowspan="9">Instance management</td> <td>AsyncInvokeInstance</td>
<td>Instance execution asynchronous command interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchResetInstance</td>
<td>Instance batch reset. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetVideo</td>
<td>Instance video settings. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelInstance</td>
<td>The prerequisite for calling this API is that the tenant must first purchase a Koophone cloud phone instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteJob</td>
<td>Instance execution batch query task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchShowInstance</td>
<td>Instance status batch query. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ProvisionInstance</td>
<td>The prerequisite for calling this API is that the tenant must first purchase a Koophone cloud phone instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteInstanceAuthToken</td>
<td>Obtain the device_token of the tenant instance before streaming. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SyncInvokeInstance</td>
<td>Instance execution synchronization command interface. The prerequisite for calling this API is that the tenant must first purchase a Koophone cloud phone instance. You can use this API to perform ADB command operations on your Koophone cloud phone instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Instance Order</td>
<td>DeleteInstance</td>
<td>The prerequisite for calling this API is that the tenant must first purchase a Koophone cloud phone instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchShowSku</td>
<td>Instance SKU batch query. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInstance</td>
<td>Tenants can create instances by calling this API. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>