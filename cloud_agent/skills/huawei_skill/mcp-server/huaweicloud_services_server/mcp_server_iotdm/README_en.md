# IoTDM MCP Server


## Version
v0.1.0

## Overview

IoTDM MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service IoTDM. Full-chain management of IoTDM resources can be carried out based on natural language.

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
<td rowspan="9">InstanceManagement</td> 
<td>UnbindInstanceTags</td> <td>Delete the instance tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeInstanceChargeMode</td>
<td>Change the billing mode of the device access instance. Supports changing the on-demand billing mode to the annual/monthly billing mode. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInstance</td>
<td>Users can call this API to create a device access instance. For supported instance specifications, see [Product Specifications](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResizeInstance</td>
<td>Change the specifications of the device access instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstances</td>
<td>Users can call this API to query the device access instance list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstance</td>
<td>Query device access instance details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BindInstanceTags</td>
<td>Add instance tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstance</td>
<td>Modify device access instance information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstance</td>
<td>Deletes a device access instance. Constraint: This API only supports deleting pay-as-you-go instances. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>