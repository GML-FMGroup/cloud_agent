# IdentityCenterOIDC MCP Server


## Version
v0.1.0

## Overview

IdentityCenterOIDC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IdentityCenterOIDC. Full-chain management of IdentityCenterOIDC resources can be carried out based on natural language.

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
<td rowspan="1">Client</td> <td>RegisterClient</td>
<td>Registers the client with the IAM Identity Center. This allows the client to initiate device authorization. The output should be persisted for easy reuse in authentication requests.
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">DeviceAuthorization</td>
<td>StartDeviceAuthorization</td>
<td>Initiate a device authorization request</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Token</td>
<td>CreateToken</td>
<td>Obtain an access token</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>