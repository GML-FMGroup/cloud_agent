# CodeArtsArtifact MCP Server


## Version
v0.1.0

## Overview

CodeArtsArtifact MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CodeArtsArtifact. Full-chain management of CodeArtsArtifact resources can be carried out based on natural language.

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
<td rowspan="2">Warehouse related projects</td> <td>ShowProjectList</td>
<td>Query project management related repositories</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateProjectRelatedRepository</td>
<td>Create project management related repositories</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Warehouse capacity</td>
<td>ShowStorage</td>
<td>Warehouse usage query</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Warehouse management</td>
<td>ModifyRepository</td>
<td>Edit repository</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRepository</td>
<td>Delete repository to recycle bin</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateMavenRepo</td>
<td>Create Maven repository</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMavenInfo</td>
<td>Query tenant Maven repository list and account password, supports cross-tenant</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDockerRepositories</td>
<td>Create Docker repository</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateArtifactory</td>
<td>Create non-Maven repository</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateArtifactory</td>
<td>Edit non-Maven repository information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRepositoryInfo</td>
<td>View repository information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Repository details</td>
<td>ListArtifactoryStorageStatistic</td>
<td>Query storage capacity trends</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRepository</td>
<td>Query detailed information for a single repository, which will count the number of artifacts in the repository</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAllRepositories</td>
<td>Query warehouse details. Does not count the number of artifacts in the warehouse.</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Follow</td>
<td>CreateAttention</td>
<td>Follow/Unfollow a component</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAttentions</td>
<td>Query the attention list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Release library file query</td>
<td>ShowReleaseProjectFiles</td>
<td>Get a list of file version information under the project</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProjectReleaseFiles</td>
<td>Get a list of file version information under a project</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Recycle Bin</td>
<td>BatchRestoreRepo</td>
<td>Batch Restore Recycle Bin</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteTrashes</td>
<td>Batch Delete Recycle Bin</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Audit Log</td>
<td>ShowAudit</td>
<td>Query the audit log information of a repository or file</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Search</td>
<td>SearchByChecksum</td>
<td>Searching for files by checksum</td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchArtifacts</td>
<td>Coordinated Search</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">File Management</td>
<td>ShowFileTree</td>
<td>Query Repository Folder Directory</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListArtifactoryComponent</td>
<td>Query Repository File Details</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteArtifactFile</td>
<td>Non-Maven Delete File</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Permission View</td>
<td>ShowUserPrivileges</td>
<td>Query user permissions under the project</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">User Management</td>
<td>ResetUserPassword</td>
<td>Reset user password</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>