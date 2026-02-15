# CC MCP Server


## Version
v0.1.0

## Overview

CC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CC. Full-chain management of CC resources can be carried out based on natural language.

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
<td rowspan="5">Authorisation</td> 
<td>UpdateAuthorisation</td> 
<td>Update authorization instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPermissions</td>
<td>The tenant that owns the cloud connection instance queries its permissions to load other tenants' network instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAuthorisations</td>
<td>The tenant that owns the network instance views the permissions it has granted to other tenants. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAuthorisation</td>
<td>The tenant that owns the network instance grants the tenant that owns the cloud connection instance permission to load its network instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAuthorisation</td>
<td>The tenant that owns the network instance revokes the permission granted to the tenant that owns the cloud connection instance to load its network instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="11">BandwidthPackage</td>
<td>ListBandwidthPackageTags</td>
<td>Query the bandwidth package tag information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBandwidthPackage</td>
<td>Query the bandwidth package instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DisassociateBandwidthPackage</td>
<td>Disassociate the bandwidth package instance from the cloud connection instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateBandwidthPackage</td>
<td>Create a bandwidth package instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteBandwidthPackage</td>
<td>Delete a bandwidth package instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBandwidthPackages</td>
<td>Query the bandwidth package list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AssociateBandwidthPackage</td>
<td>Associate a bandwidth package instance to a cloud connection instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBandwidthPackagesByTags</td>
<td>Filter bandwidth package instances by tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>TagBandwidthPackage</td>
<td>Create a bandwidth package tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateBandwidthPackage</td>
<td>Update a bandwidth package instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UntagBandwidthPackage</td>
<td>Delete a bandwidth package tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="14">CentralNetwork</td>
<td>ApplyCentralNetworkPolicy</td>
<td>Apply a central network policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCentralNetworkTags</td>
<td>Query the tag information of the central network. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCentralNetwork</td>
<td>Create the central network. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCentralNetwork</td>
<td>Delete the central network. Please clear the attachments before deleting the central network. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCentralNetwork</td>
<td>Update the central network details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCentralNetworkPolicy</td>
<td>Delete the central network policy version. You cannot delete a central policy that is currently being applied. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCentralNetworkPolicyChangeSet</td>
<td>Query the changesets associated with the currently applied central network policy. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCentralNetworkPolicies</td>
<td>Query the list of all versions of central network policies. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCentralNetworkPolicy</td>
<td>Create a read-only central network policy. If you modify the policy document, you will need to create a new version based on this version. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCentralNetworks</td>
<td>Query the list of central networks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UntagCentralNetwork</td>
<td>Delete the central network tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCentralNetwork</td>
<td>Query central network details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>TagCentralNetwork</td>
<td>Create a central network tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCentralNetworksByTags</td>
<td>Filter central network instances by tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">CentralNetworkAttachment</td>
<td>ShowCentralNetworkGdgwAttachment</td>
<td>Query central network GDGW attachment details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCentralNetworkErRouteTableAttachment</td>
<td>Create a central network's route table attachment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCentralNetworkAttachment</td>
<td>Delete a central network attachment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCentralNetworkErRouteTableAttachment</td>
<td>Update a central network's ER route table attachment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCentralNetworkAttachments</td>
<td>Query the list of central network attachments. The parameters used for paging queries are marker and limit. The default value of limit is 0. If no marker is specified, the first data entry is returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCentralNetworkGdgwAttachment</td>
<td>Update the central network GDGW attachment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCentralNetworkGdgwAttachment</td>
<td>Create the central network GDGW attachment. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCentralNetworkErRouteTableAttachments</td>
<td>Query the list of central network ER route table attachments. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCentralNetworkGdgwAttachments</td>
<td>Query the central network GDGW attachment list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCentralNetworkErRouteTableAttachment</td>
<td>Query the central network ER route table attachment details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">CentralNetworkCapabilities</td>
<td>ListCentralNetworkCapabilities</td>
<td>Query the central network capability list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">CentralNetworkConnection</td>
<td>ListCentralNetworkConnections</td>
<td>Query the central network connection list interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCentralNetworkConnection</td>
<td>Update the central network connection interface (only supports updating bandwidth). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">CentralNetworkQuotas</td>
<td>ListCentralNetworkQuotas</td>
<td>Query the central network quota. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">CloudConnection</td>
<td>TagCloudConnection</td>
<td>Create a cloud connection instance tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UntagCloudConnection</td>
<td>Remove a cloud connection instance tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCloudConnection</td>
<td>Create a cloud connection instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCloudConnectionsByTags</td>
<td>Filter cloud connection instances by tag. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCloudConnectionTags</td>
<td>Query the tag information of a cloud connection instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCloudConnection</td>
<td>Update a cloud connection instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCloudConnection</td>
<td>Delete a cloud connection instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCloudConnections</td>
<td>Query the cloud connection list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCloudConnection</td>
<td>Query cloud connection instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">CloudConnectionCapabilities</td>
<td>ListCloudConnectionCapabilities</td>
<td>Query the cloud connection capability list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">CloudConnectionQuotas</td>
<td>ListCloudConnectionQuotas</td>
<td>Query cloud connection quotas. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">CloudConnectionRoute</td>
<td>ShowCloudConnectionRoutes</td>
<td>Query the list of cloud connection route entries. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCloudConnectionRoutes</td>
<td>Query the list of cloud connection route entries. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">GcbTagManager</td>
<td>CreateGcbResourceTag</td>
<td>Add an account-wide interconnection bandwidth resource tag</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateGcbResourceTags</td>
<td>Add resource tags in TMS batches</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGcbResourceTag</td>
<td>Delete an account-wide interconnection bandwidth resource tag</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteGcbResourceTags</td>
<td>Batch Delete Account Global Interconnect Bandwidth Resource Tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>CountGcbResourceByTag</td>
<td>Query the Number of Account Global Interconnect Bandwidth Resource Tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGcbTenantTags</td>
<td>Query All Account Global Interconnect Bandwidth Resource Tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGcbResourceByTag</td>
<td>Query a List of Account Global Interconnect Bandwidth Resource Instances</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGcbResourceTags</td>
<td>Query the account's global interconnection bandwidth resource tags.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">GlobalConnectionBandwidth</td>
<td>UpdateGlobalConnectionBandwidth</td>
<td>Update global interconnection bandwidth details.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGlobalConnectionBandwidth</td>
<td>Delete global interconnection bandwidth.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSupportBindingConnectionBandwidths</td>
<td>Query the list of global interconnection bandwidths that meet the binding conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGlobalConnectionBandwidthLineLevels</td>
<td>Query the line level list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowGlobalConnectionBandwidth</td>
<td>Query the global interconnect bandwidth details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AssociateGlobalConnectionBandwidthInstance</td>
<td>Global interconnect bandwidth binding instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGlobalConnectionBandwidths</td>
<td>Query the global interconnect bandwidth list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGlobalConnectionBandwidthSpecCodes</td>
<td>Query the line specification list. Tenant whitelist control, default is empty. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DisassociateGlobalConnectionBandwidthInstance</td>
<td>Disassociate the global interconnection bandwidth instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGlobalConnectionBandwidth</td>
<td>Create the global interconnection bandwidth. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGlobalConnectionBandwidthSites</td>
<td>Query the site list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGlobalConnectionBandwidthConfigs</td>
<td>Query the global interconnection bandwidth tenant configuration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">InterRegionBandwidth</td>
<td>ListInterRegionBandwidths</td>
<td>Query the interregion bandwidth list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInterRegionBandwidth</td>
<td>Query the interregion bandwidth instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInterRegionBandwidth</td>
<td>Update the interregion bandwidth instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInterRegionBandwidth</td>
<td>Delete the interregion bandwidth instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInterRegionBandwidth</td>
<td>Create an interregion bandwidth instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">NetworkInstance</td>
<td>ShowNetworkInstance</td>
<td>Query a network instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNetworkInstances</td>
<td>Query a list of network instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateNetworkInstance</td>
<td>Create a network instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateNetworkInstance</td>
<td>Update the network instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteNetworkInstance</td>
<td>Delete the network instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">SiteConnection</td>
<td>AssociateSiteNetworkBandwidth</td>
<td>Associate the branch connection bandwidth. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSiteNetworkBandwidthSize</td>
<td>Change the branch connection bandwidth size. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DisassociateSiteNetworkBandwidth</td>
<td>Disassociate branch connection bandwidth. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSiteNetworkBandwidth</td>
<td>Change branch connection bandwidth package. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">SiteNetwork</td>
<td>DeleteSiteNetwork</td>
<td>Delete a branch network. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSiteNetwork</td>
<td>Query branch network details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateP2PSiteNetwork</td>
<td>Create a P2P branch network. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSiteNetwork</td>
<td>Update branch network details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSiteNetworks</td>
<td>Query the branch network list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">SiteNetworkCapabilities</td>
<td>ListSiteNetworkCapabilities</td>
<td>Query the branch network capability list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">SiteNetworkQuotas</td>
<td>ListSiteNetworkQuotas</td>
<td>Query branch network quotas. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Specifications</td>
<td>ListBandwidthPackageSites</td>
<td>Query bandwidth
List of bandwidth package sites. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBandwidthPackageLines</td>
<td>Query the list of bandwidth package lines. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRegionBandwidthPackageSpecifications</td>
<td>Query the list of bandwidth package specifications for regional interoperability. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBandwidthPackageLevels</td>
<td>Query the list of bandwidth package levels. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAreaBandwidthPackageSpecifications</td>
<td>Query the list of bandwidth package resource specifications for regional interoperability. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRegions</td>
<td>Query the currently supported region list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAreas</td>
<td>Query the currently supported area list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">TagManager</td>
<td>BatchCreateDeleteTags</td>
<td>Batch create and delete tags. This API is deprecated. Please use "Create Cloud Connection Instance Tags," "Create Bandwidth Package Tags," "Delete Cloud Connection Instance Tags," and "Delete Bandwidth Package Tags" first. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListResourceByFilterTag</td>
<td>Query resource instances. This API is a legacy API. Please use "Filter Cloud Connect Instances by Tag" or "Filter Bandwidth Package Instances by Tag" first. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTags</td>
<td>Query resource tags. This API is a legacy API. Please use "Query Cloud Connect Instance Tag Information" or "Query Bandwidth Package Tag Information" first. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDomainTags</td>
<td>Query account resource tags. This API is a legacy API. Please use "Query Cloud Connect Instance Tag Information" or "Query Bandwidth Package Tag Information" first. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTag</td>
<td>Delete a resource tag. This API is a legacy API. Please use "Delete Cloud Connection Instance Tag" or "Delete Bandwidth Package Tag" first. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTag</td>
<td>Add a resource tag. This API is a legacy API. Please use "Create Cloud Connection Instance Tag" or "Create Bandwidth Package Tag" first. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>