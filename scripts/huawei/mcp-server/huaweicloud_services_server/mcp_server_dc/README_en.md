# DC MCP Server


## Version
v0.1.0

## Overview

DC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service DC. Full-chain management of DC resources can be carried out based on natural language.

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
<td rowspan="3">BindingGlobalEip</td> 
<td>UnbindGlobalEips</td> <td>Unbind GEIP</td>
<td>To be tested</td>
</tr>
<tr>
<td>BindGlobalEips</td>
<td>Bind GEIP</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGlobalEips</td>
<td>Query the list of bound GEIPs</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">ConnectGateway</td>
<td>DeleteConnectGateway</td>
<td>Delete Internet Gateway</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateConnectGateway</td>
<td>Update Internet Gateway</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateConnectGateway</td>
<td>Create an Internet gateway</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListConnectGateways</td>
<td>Query the Internet gateway list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowConnectGateway</td>
<td>Query Internet gateway details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">DirectConnect</td>
<td>UpdateDirectConnect</td>
<td>Update physical connection information, including name, description, etc.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateHostedDirectConnect</td>
<td>Partner updates hosted dedicated line.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHostedDirectConnects</td>
<td>Query the list of hosted direct connections created by partners.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDirectConnect</td>
<td>Query physical connection details.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowHostedDirectConnect</td>
<td>Query the hosted direct connection type of a valid partner.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDirectConnect</td>
<td>Delete a physical connection. This interface is only applicable to pay-as-you-go direct connections. For dedicated connections purchased on a subscription basis, delete the physical connection by canceling the order.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateHostedDirectConnect</td>
<td>Used by a partner user to create a hosted direct connection for the tenant.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteHostedDirectConnect</td>
<td>Partner deletes a hosted direct connection.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDirectConnects</td>
<td>Query all direct connect objects created by the tenant.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">DirectConnectLocation</td>
<td>ShowDirectConnectLocation</td>
<td>Query the details of the specified direct connection access point.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDirectConnectLocations</td>
<td>Query information about all dedicated line access points in this area. The parameters used for paging queries are marker and limit. Marker and limit are effective only when used together; using them alone is invalid.

<td>To be tested</td>

<tr>
<td rowspan="2">GdgwRoutetable</td>
<td>UpdateGdgwRouteTable</td>
<td>Supported modification operations: add, delete, modify</td>
<td>To be tested</td>

<tr>
<td>ListGdgwRouteTables</td>
<td>Query the global access gateway routing table</td>
<td>To be tested</td>

</tr>
<tr>
<td rowspan="5">GlobalDcGateway</td>
<td>ShowGlobalDcGateway</td>
<td>Query the details of the dedicated global access gateway instance</td><td>To be tested</td>
</tr>
<tr>
<td>UpdateGlobalDcGateway</td>
<td>Update the name, description, and other information of the dedicated global DC-gateway access gateway.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGlobalDcGateway</td>
<td>Delete the dedicated global DC-gateway access gateway instance.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGlobalDcGateway</td>
<td>Create a dedicated global DC-gateway access gateway instance (global-dc-gateway) for accessing global ER instances.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGlobalDcGateways</td>
<td>To query the global dedicated line access gateway list, it is recommended to use paging query. The parameters used for paging query are marker and limit. This option is effective only when used with a marker and limit; it is invalid when used alone.

<td>To be tested</td>

<tr>
<td rowspan="5">PeerLink</td>
<td>DeletePeerLink</td>
<td>Delete the peer-link associated with the global access gateway and the ER.

<td>To be tested</td>

</tr>

<tr>
<td>ShowPeerLink</td>
<td>Query the details of the specified peer link associated with the specified access gateway.

<td>To be tested</td>

</tr>

<tr>
<td>CreatePeerLink</td>
<td>Create a peer-link associated with the dedicated global access gateway, used to connect to enterprise routers or other access gateways.

<td>To be tested</td>

</tr>

<tr>
<td>UpdatePeerLink</td>
<td>Updates the peer-link link between the access gateway and ER.
<td>To be tested</td>
</tr>
<tr>
<td>ListPeerLinks</td>
<td>Query the list of links between the global access gateway and ER objects. The paginated query uses the marker and limit parameters. Marker and limit are effective only when used together; using them alone is invalid.
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">QuotaManager</td>
<td>ShowQuotas</td>
<td>Query the usage of various tenant resources, such as DirectConnect usage and virtual interface usage. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">TagManage</td>
<td>CreateResourceTag</td>
<td>- A resource can have a maximum of 10 tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowResourceTag</td>
<td>Query resource tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteResourceTag</td>
<td>When deleting, the tag character set is not validated. Before calling the API, you must encodeURI. The server must decode the API URI. If the deleted key does not exist, a 404 error will be reported. Key cannot be empty or an empty string. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListProjectTags</td>
<td>- Query the set of all resource tags for instance types in a specified project for a tenant. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateResourceTags</td>
<td>- Add or remove tags for specified instances in batches</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTagResourceInstances</td>
<td>Query resource instances by tag</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">VirtualGateway</td>
<td>DeleteVirtualGateway</td>
<td>Delete the specified virtual gateway</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListVirtualGateways</td>
<td>Query the virtual gateway list</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateVirtualGateway</td>
<td>Update virtual gateway information</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateVirtualGateway</td>
<td>Create a virtual gateway</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowVirtualGateway</td>
<td>Query detailed information of a specified virtual gateway</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">VirtualInterface</td>
<td>UpdateVirtualInterface</td>
<td>Update detailed information of a virtual interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchoverTest</td>
<td>Customers with dual dedicated lines need to support automatic switching between the two lines to facilitate functional testing. Switching tests on virtual interfaces will cause the interface to shut down, disrupting service traffic. For virtual interfaces, two operations are supported: "closing the interface" and "opening the interface." 1. Closing the interface: Issue the shutdown command to shut down the interface. 2. Opening the interface: Issue the undo_shutdown command to enable the interface. When the shutdown command is selected for the switching test, the virtual interface status is ADMIN_SHUTDOWN, which prohibits other operations on the virtual interface. When the undo_shutdown command is selected for the switching test, the virtual interface status is ACTIVE. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateVifPeer</td>
<td>Each virtual interface supports two peers: IPv4 and IPv6. When creating a virtual interface, an IPv4 peer is created by default. This interface is generally used to add an IPv6 peer. After creating the virtual interface, you can query the configuration results through the virtual interface. This interface is only available in regions that support IPv6. If you need to use it, please contact customer service.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteVirtualInterface</td>
<td>Delete virtual interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSwitchoverTestRecords</td>
<td>Query the switchover test record list. Only records with operate_status set to COMPELTE are displayed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowVirtualInterface</td>
<td>Query virtual interface details</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteVifPeer</td>
<td>Delete virtual interface peer information. A virtual interface must contain at least one peer; the last peer cannot be deleted. This interface is only available in regions that support IPv6. If you need to use it, please contact customer service.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateVirtualInterface</td>
<td>Configure the virtual interface for the physical dedicated line, including IP and routing information, to connect to the customer.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListVirtualInterfaces</td>
<td>Query a list of all tenant virtual interfaces</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateVifPeer</td>
<td>Update virtual interface peer information, including remote subnet, name, and description. This interface is only available in regions that support IPv6. Please contact customer service if you need to use it.</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>