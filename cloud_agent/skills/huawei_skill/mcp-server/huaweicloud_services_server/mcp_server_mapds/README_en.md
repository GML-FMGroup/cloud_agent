# MapDS MCP Server


## Version
v0.1.0

## Overview

MapDS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service MapDS. Full-chain management of MapDS resources can be carried out based on natural language.

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
<td rowspan="4">Certificate management</td> 
<td>CreateSasToken</td> 
<td>Create SAS Token credentials, used to access tiles. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCredential</td>
<td>This interface is used to create credentials for accessing map data services. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCredential</td>
<td>This interface is used to query credentials for accessing map data services. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCedential</td>
<td>This interface is used to delete credentials for accessing map data services. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Get map tiles</td>
<td>ShowMapTile</td>
<td>This interface is used to get map tiles. </td> 
<td>To be tested</td> 
</tr> 
</tbody> 
</table> 
</body>
</html>