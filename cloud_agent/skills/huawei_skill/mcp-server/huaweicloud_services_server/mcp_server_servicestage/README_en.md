# ServiceStage MCP Server


## Version
v0.1.0

## Overview

ServiceStage MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ServiceStage. Full-chain management of ServiceStage resources can be carried out based on natural language.

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
<td rowspan="8">Application</td> 
<td>ModifyApplication</td> <td>This API modifies application information by application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApplications</td>
<td>Get all application information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApplicationInfo</td>
<td>This API gets application details by application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyApplicationConfiguration</td>
<td>This API modifies application configuration by application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApplicationConfiguration</td>
<td>This API gets application configuration information by application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateApplication</td>
<td>An application is a relatively complete business system, consisting of one or more feature-related components. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApplication</td>
<td>This API deletes an application by application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApplicationConfiguration</td>
<td>This API deletes an application configuration by application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Component</td>
<td>ShowComponentRecords</td>
<td>This API is used to retrieve records by component ID.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowComponentsInApplication</td>
<td>Use this API to retrieve all application components in the application.</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateComponent</td>
<td>This API is used to create a component in the application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowComponents</td>
<td>This API is used to obtain all components.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteComponent</td>
<td>This API deletes a component by its ID.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyComponent</td>
<td>This API modifies component information by its ID.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowComponentInfo</td>
<td>Obtain component information by its ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateComponentAction</td>
<td>Issue component tasks by component ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Environment</td>
<td>ShowEnvironmentInfo</td>
<td>This API retrieves detailed environment information by environment ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateEnvironment</td>
<td>An environment is a collection of computing, storage, and network infrastructure used for application deployment and operation. Servicestage combines a CCE cluster in the same VPC with multiple ELB, RDS, and DCS instances into an environment, such as a development environment, a test environment, a pre-production environment, or a production environment. Network connectivity within an environment allows for resource management and service deployment by environment, reducing the complexity of infrastructure operations and maintenance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEnvironmentResources</td>
<td>This API is used to query environment resources based on the environment ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyEnvironment</td>
<td>This API is used to modify an environment using its environment ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyResourceInEnvironment</td>
<td>This API is used to modify environment resources using its environment ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEnvironments</td>
<td>This API is used to retrieve all created environments. </td>
<td>To be tested</td>ested</td>
</tr>
<tr>
<td>DeleteEnvironment</td>
<td>This API deletes an environment by its environment ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">GIT repository</td>
<td>ListHooks</td>
<td>Get all hooks for the specified project</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateProject</td>
<td>Create a software repository project under the specified organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNamespaces</td>
<td>Get the repository's namespaces. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListProjects</td>
<td>Get all projects under the specified organization. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTag</td>
<td>Create a tag for the specified project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateHook</td>
<td>Create a hook for the specified project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBranches</td>
<td>Get a list of all branches for the specified project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTags</td>
<td>Get all tags for the specified project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTag</td>
<td>Delete the tag for the specified project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteHook</td>
<td>Delete the hook for the specified project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCommits</td>
<td>Get the latest 10 commit records for the specified project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProjectDetail</td>
<td>Get repository information using the specified clone url. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">GIT repository file</td>
<td>CreateFile</td>
<td>Create a file in the specified repository project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteFile</td>
<td>Delete a file in the specified project repository. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateFile</td>
<td>Update the file contents in the specified project repository. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTrees</td>
<td>Get a list of files in the specified project repository. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowContent</td>
<td>Get the contents of a file in the specified project repository. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">GIT Authorization</td>
<td>CreatePersonalAuth</td>
<td>Create a private token authorization for the specified Git repository type. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePasswordAuth</td>
<td>Create a password authorization for the specified Git repository type. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOAuth</td>
<td>Create an OAuth authorization for the specified Git repository type. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAuthorizations</td>
<td>Get all Git repository authorization information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRedirectUrl</td>
<td>Get the authorized redirect URL for the specified Git repository type. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAuthorize</td>
<td>Delete a repository authorization by name. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Job</td>
<td>ShowJobInfo</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Meta</td>
<td>ListRuntimes</td>
<td>This API is used to obtain all supported application component runtime types. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFlavors</td>
<td>Use this API to obtain supported application resource specifications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTemplates</td><td>This API is used to retrieve all built-in application component templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">RuntimeStack</td>
<td>ShowRuntimeStacks</td>
<td>Get runtime information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Cloud Application Model</td>
<td>UpdateTemplate</td>
<td>Update Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstanceById</td>
<td>Delete Instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeployInstance</td>
<td>Deploy Instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCamInstance</td>
<td>Create and Update Instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTemplate</td>
<td>Delete Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTemplate</td>
<td>Create Template</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Instance</td>
<td>ChangeInstance</td>
<td>Use this API to modify an application component instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstance</td>
<td>Use this API to delete an application component instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstances</td>
<td>Use this API to obtain all component instances under a component. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstanceSnapshots</td>
<td>Use this API to obtain application component instance snapshot information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInstance</td>
<td>This API is used to create an application component instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstanceDetail</td>
<td>This API obtains instance details by instance ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInstanceAction</td>
<td>Use this API to obtain operations on component instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Application</td>
<td>ShowApplicationDetail</td>
<td>This API retrieves application details by application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApplications</td>
<td>This API retrieves all created applications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeApplication</td>
<td>This API modifies application information by application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeApplicationConfiguration</td>
<td>This API modifies application configuration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Environment</td>
<td>ChangeResourceInEnvironment</td>
<td>This API is used to modify environment resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEnvironmentDetail</td>
<td>This API obtains environment details by environment ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeEnvironment</td>
<td>This API modifies environment information by environment ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListEnvironments</td>
<td>This API obtains all created environments. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Components</td>
<td>ListComponents</td>
<td>Use this API to obtain all application components under the application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowComponentDetail</td>
<td>Obtain application component information by component ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeComponent</td>
<td>This API modifies component information by component ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListComponentOverviews</td>
<td>Use this API to obtain deployment information for all application components under the application. </td> 
<td>To be tested</td> 
</tr> 
<tr><td rowspan="1">Deployment Job</td>
<td>ShowJobDetail</td>
<td>Get deployment job details through this API. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>