# IdentityCenterPortalAPI MCP Server


## Version
v0.1.0

## Overview

IdentityCenterPortalAPI MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IdentityCenterPortalAPI. Full-chain management of IdentityCenterPortalAPI resources can be carried out based on natural language.

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
<td rowspan="1">Account</td> <td>ListAccounts</td>
<td>List all accounts assigned to the user</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Agency</td>
<td>ListAccountAgencies</td>
<td>List all delegates or trust delegates assigned to the user</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Credential</td>
<td>GetAgencyCredentials</td>
<td>Get the STS short-term credentials for the specified delegate or trust delegate assigned to the user</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Token</td>
<td>Logout</td>
<td>Sends an API call to the IAM Identity Center service to invalidate the corresponding server-side IAM Identity Center login session. </td> 
<td>To be tested</td> 
</tr> 
</tbody> 
</table> 
</body>
</html>