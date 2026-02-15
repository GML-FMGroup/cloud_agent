# EC MCP Server


## Version
v0.1.0

## Overview

EC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service EC. Full-chain management of EC resources can be carried out based on natural language.

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
<td rowspan="4">EcnAccessPoint</td> 
<td>UpdateEcnAccessPoint</td> <td>Update access points based on enterprise connection network ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateEcnAccessPoint</td>
<td>Add a new access point</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEcnAccessPointByEcnId</td>
<td>Query all access points under an enterprise connection network ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEcnAccessPoint</td>
<td>Delete access points based on enterprise connection network ID</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">EnterpriseConnectNetwork</td>
<td>ListEcnWithIeg</td>
<td>Query the binding relationship between the enterprise connection network and the smart enterprise gateway based on the enterprise connection network ID.</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddEcnWithIeg</td>
<td>Bind the smart enterprise gateway to the enterprise connection network</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEcn</td>
<td>Query the tenant's enterprise connection network list</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEcn</td>
<td>Update the enterprise connection network based on the enterprise connection network ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEcnInfo</td>
<td>Query the enterprise connection network based on the enterprise connection network ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEcnWithIeg</td>
<td>Query the binding relationship between the enterprise connection network and a single smart enterprise gateway</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEcnWithIeg</td>
<td>Unbind the smart enterprise gateway from the enterprise connection network</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Equipment</td>
<td>ShowEquipmentInfo</td>
<td>Query the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEquipmentSpecificConfig</td>
<td>Query the basic specifications and configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEquipmentInfo</td>
<td>Update the Smart Enterprise Gateway Device</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateEquipment</td>
<td>Activate the Smart Enterprise Gateway Device</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEquipment</td>
<td>Remove the Smart Enterprise Gateway Device</td>
<td>To be tested</td>
</tr>
<tr>
<td>RebootEquipment</td>
<td>Reboot the Smart Enterprise Gateway Device</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEquipmentEsn</td>
<td>Modify the Smart Enterprise Gateway Device ESN</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEquipments</td>
<td>Query the list of smart enterprise gateway devices based on the smart enterprise gateway ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>GenerateInitialConfiguration</td>
<td>Generate the initial configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">EquipmentLan</td>
<td>ShowEquipmentDnsInfo</td>
<td>Query the primary and backup DNS configurations of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEquipmentLanInfo</td>
<td>Query the LAN port configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEquipmentInterfaceName</td>
<td>Query the configured interface names of the Smart Enterprise Gateway</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEquipmentLanConfig</td>
<td>Delete the LAN port configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateEquipmentLanConfig</td>
<td>Create the LAN port configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEquipmentLanConfig</td>
<td>Update the LAN port configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEquipmentDnsInfo</td>
<td>Update the primary and backup DNS configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">EquipmentOspf</td>
<td>ShowEquipmentOspf</td>
<td>Query the OSPF configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEquipmentOspf</td>
<td>Configure the OSPF protocol on the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">EquipmentStaticRoute</td>
<td>UpdateEquipmentStaticRouteConfig</td>
<td>Update the static route configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEquipmentStaticRouteInfo</td>
<td>Query the static route configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateEquipmentStaticRouteConfig</td>
<td>Create a static route configuration for the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEquipmentStaticRouteConfig</td>
<td>Delete a static route configuration for the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">EquipmentWan</td>
<td>ShowEquipmentWanInfo</td>
<td>Query the WAN port configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEquipmentWanConfig</td>
<td>Update the WAN port configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">EquipmentWlan</td>
<td>ShowEquipmentWlan</td>
<td>Query the Wi-Fi configuration of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEquipmentWlan</td>
<td>Configure the Wi-Fi of the smart enterprise gateway device</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">ErRelationship</td>
<td>DeleteEcnWithEr</td>
<td>Disassociate the enterprise router from the enterprise connection network</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddEcnWithEr</td>
<td>Associate the enterprise router with the enterprise connection network</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEcnWithEr</td>
<td>Based on the enterprise connection network ID, query the association between the enterprise connection network and the enterprise router</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">IntelligentEnterpriseGateway</td>
<td>ChangeIegPassword</td>
<td>Change the IEG device admin account password</td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchEquipmentHaType</td>
<td>Switch dual-node active/standby attributes</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListIeg</td>
<td>Query the tenant's Smart Enterprise Gateway list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowIegInfo</td>
<td>Query the tenant's Smart Enterprise Gateway based on the Smart Enterprise Gateway ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateIeg</td>
<td>Update the Smart Enterprise Gateway based on the Smart Enterprise Gateway ID</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Quota</td>
<td>ShowQuotasInfo</td>
<td>Query the quota of a specified tenant related to an EC</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">VpcRelationship</td>
<td>AddEcnWithVpc</td>
<td>Associate a Virtual Private Cloud with an Enterprise Connection Network</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEcnWithVpc</td>
<td>Query the association between an enterprise connection network and a Virtual Private Cloud based on the enterprise connection network ID</td>
<td>To be tested</td></tr>
<tr>
<td>UpdateEcnWithVpc</td>
<td>Update the association between the virtual private cloud and the enterprise connection network</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteEcnWithVpc</td>
<td>Disassociate the virtual private cloud from the enterprise connection network</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">VrrpConfig</td>
<td>UpdateVrrpConfig</td>
<td>Update the VRRP configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteVrrpConfig</td>
<td>Delete the VRRP configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowVrrpConfig</td>
<td>Query the VRRP configuration list</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddVrrpConfig</td>
<td>Create a VRRP configuration</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>