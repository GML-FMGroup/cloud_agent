# ModelArts MCP Server


## Version
v0.1.0

## Overview

ModelArts MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service ModelArts. Full-chain management of ModelArts resources can be carried out based on natural language.

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
<td rowspan="5">AI application management</td> 
<td>ShowModel</td> <td>Query AI application details. Query detailed information about an AI application based on its AI application ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteModel</td>
<td>Delete an AI application. Delete a specified AI application based on its AI application ID. If cascade is set to true, in addition to deleting the AI application specified by the AI application ID, other AI applications with the same name but different versions will also be deleted. By default, only the AI application corresponding to the current AI application ID is deleted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowModelEngineAndRuntime</td>
<td>Query the model AI engine and runtime. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateModel</td>
<td>Import the metamodel to create an AI application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListModels</td>
<td>Query the AI application list, which can be searched based on different search parameters. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="20">APP Authentication Management</td>
<td>CreateAndAuthAppAuthApi</td>
<td>Register the API and authorize the API to the app. Only Huawei Cloud users with update permissions for the service can call it. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetApigAppSecret</td>
<td>Reset the AppSecret of the specified API gateway application. Only the user who created the app can reset the AppSecret. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetServiceAppAuthApiAuthInfo</td>
<td>Query the service's authorized API and app information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApiAppAuth</td>
<td>Remove the specified API authorization from the app. The requesting user must have update permissions for the service to which the API belongs. Same URL: /v1/{project_id}/app-auth/{service_id}/apis/{api_id}/auths</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateApigAppCode</td>
<td>Create a new AppCode for the specified API Gateway application. Only the user who created the app can create an AppCode, and only apps with the shared or exclusive APIG version can create an AppCode. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApigApp</td>
<td>Query the details of the specified app. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApisBindToApp</td>
<td>Get the list of APIs bound to the user's app. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateApigApp</td>
<td>Create an API gateway application (APP). Each user can only create up to 5 apps. You can apply for a higher quota if needed. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAppAuthApi</td>
<td>Create an API, but do not authorize the API to the app. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetApigAppCode</td>
<td>Resets the specified AppCode for a specified API Gateway application. Only the user who created the app can reset the AppCode, and only apps with the shared/exclusive APIG version support the AppCode. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AuthorizeApiToApigApps</td>
<td>Authorizes the specified API to the app. The API authentication method must be app authentication. The user who created the app must be the creator of the service to which the API belongs, and the requesting user must have update permissions for the service to which the API belongs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApigApps</td>
<td>Get a list of basic information for APIG apps. Users can only retrieve information for apps they have created. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ApigAppExists</td>
<td>Query whether the app exists. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetAppAuthApisInfo</td>
<td>Query the app's API authentication information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApiAuthInfos</td>
<td>Get the list of authorization relationships between the specified API and the app. The API authentication method must be app authentication. Administrators can obtain authorization information for all APIs, while ordinary users can only obtain authorization information for APIs under services to which they have access permissions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetAppAuthApiInfo</td>
<td>Query the details of the specified API.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApigApp</td>
<td>Deletes the specified app. Only the user who created the app can delete the app, and the app has no bound APIs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAppAuthApi</td>
<td>Deletes the specified API. Only users with delete permissions for the service to which the API belongs can delete the API. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApigAppCode</td>
<td>Deletes the specified AppCode for the specified API Gateway application. Only the user who created the app can delete the AppCode, and only apps with the shared/exclusive APIG version support AppCode. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAuthApiToApigApps</td>
<td>Update the API authorization relationship. The API authentication method must be APP authentication. The user who created the APP must be the creator of the service to which the API belongs, and the requesting user must have update permissions for the service to which the API belongs. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">DevServer Management</td>
<td>StartDevServer</td>
<td>Start the DevServer instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDevServer</td>
<td>Delete the DevServer instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDevServer</td>
<td>Create a DevServer. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SyncDevServers</td>
<td>Synchronize the status of all user DevServer instances in real time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDevServers</td>
<td>Query the list of all user DevServer instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopDevServer</td>
<td>Stop a DevServer instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDevServer</td>
<td>Query the DevServer instance details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="13">Notebook instance management</td>
<td>ListFlavors</td>
<td>Query the list of valid flavors supported by running the Notebook instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartNotebook</td>
<td>Start the Notebook instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateNotebook</td>
<td>Create a Notebook instance. This function creates a notebook based on the instance specifications, different AI engine images, storage, and other parameters you specify. You can access the notebook instance through the web page and an SSH client. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateNotebook</td>
<td>This API is used to update a notebook instance, including its name, description, specifications, and image ID. This API can only be used when the notebook instance is stopped. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteNotebook</td>
<td>Deletes a notebook instance. Deletes resources including the notebook container and all corresponding storage resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNotebook</td>
<td>Query the details of a Notebook instance, including the instance ID, name, specifications, image, instance status, and the URLs available for opening the instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSwitchableFlavors</td>
<td>Query the list of switchable flavors supported for creating a Notebook instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateImage</td>
<td>A running instance can be saved as a container image. Installed dependencies (pip packages) are not lost in the saved image. In the VS Code remote development scenario, plugins installed on the server are not lost. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAllNotebooks</td>
<td>Query the list of all Notebook instances. Users can query the list of Notebook instances that meet the requirements on demand. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RenewLease</td>
<td>This interface is used to extend the running time of a running Notebook instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowLease</td>
<td>This interface is used to query the available time of a running Notebook instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopNotebook</td>
<td>Stop a Notebook instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNotebooks</td>
<td>Query the list of Notebook instances. Users can query the list of Notebook instances that meet the requirements on demand. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Notebook Tag Management</td>
<td>ShowNotebookTags</td>
<td>Query the tags of the notebook instance type in the user's current project. By default, the query queries all workspaces. Tag data will not be returned if the user does not have permission. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteNotebookTags</td>
<td>Delete tags from the specified notebook resource. Batch deletion is supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateNotebookTags</td>
<td>Add tags to the specified notebook resource. Batch addition is supported. If the added tag key already exists, the value of the tag will be overwritten. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Workflow</td>
<td>ShowWorkflow</td>
<td>Query workflow details by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkflowsOverview</td>
<td>Get workflow statistics. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWorkflow</td>
<td>Delete a workflow by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkflow</td>
<td>Update workflow information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkflows</td>
<td>Show a list of workflows. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflowServiceAuth</td>
<td>Billing workflow online service authentication. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflow</td>
<td>Create a workflow. Refer to [How to Develop a Workflow](https://support.huaweicloud.com/usermanual-standard-modelarts/modelarts_workflow_0292.html) to create a workflow. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflowPurchasePool</td>
<td>Billing workflow purchases resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkflowsTodolist</td>
<td>Get the Workflow todo list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">WorkflowExecution</td>
<td>ShowWorkflowExecution</td>
<td>Query the details of a Workflow Execution by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWorkflowExecution</td>
<td>Delete a Workflow Execution by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflowExecutionsActions</td>
<td>This interface supports stopping or rerunning a workflow execution. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflowExecution</td>
<td>Create a workflow execution. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkflowExecutions</td>
<td>Query the list of execution records under a workflow. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkflowExecution</td>
<td>Update a workflow execution by ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflowStepExecutionsActions</td>
<td>This interface supports retry, stop, and continue operations on a Workflow StepExecution. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkflowStepExecutionMetrics</td>
<td>Get metrics information for a Workflow node. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">WorkflowSchedule</td>
<td>UpdateWorkflowSchedule</td>
<td>Update WorkflowSchedule information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflowSchedule</td>
<td>Create a workflow schedule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWorkflowScheduleId</td>
<td>Delete workflow schedule information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkflowSchedule</td>
<td>Query workflow schedule details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">WorkflowSubscription</td>
<td>DeleteWorkflowSubscription</td>
<td>Delete a subscribed message subscription. </td> 
<td>To be tested</td> 
</tr> 
<tr><td>UpdateWorkflowSubscription</td>
<td>Updates the Workflow's subscription information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkflowSubscription</td>
<td>Query the Workflow's subscription details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflowSubscriptions</td>
<td>Adds message subscription functionality to the Workflow. When events to which the workflow has subscribed occur, a message notification will be generated. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Event Management</td>
<td>ListEvents</td>
<td>Query the event list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Dynamically mount OBS</td>
<td>ShowAttachableObs</td>
<td>Get details of a dynamically mounted OBS instance. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AttachObs</td>
<td>In a running Notebook instance, you can mount the OBS Parallel File System to a specified directory within the instance. After mounting, you can read and write OBS Parallel File System objects in the container using file system operations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelObs</td>
<td>After unmounting, the objects in the OBS storage remain unchanged, but you can no longer operate on the OBS objects within the Notebook container. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAttachableObSs</td>
<td>Get a list of dynamically attached OBS instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Workspace Management</td>
<td>UpdateWorkspace</td>
<td>Modify a workspace. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkspaceQuotas</td>
<td>Modify a workspace quota. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkspace</td>
<td>Query workspace details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkspace</td>
<td>Query the workspace list. The response message body contains detailed information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWorkspace</td>
<td>Delete a workspace. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkspaceQuotas</td>
<td>Query the workspace quota. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkspace</td>
<td>Create a workspace ("default" is the default workspace name reserved by the system and cannot be used). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Authorization Management</td>
<td>CreateModelArtsAgency</td>
<td>Create a ModelArts delegation that includes dependent services such as OBS, SWR, and IEF. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAuthorization</td>
<td>Configure ModelArts authorization. Without authorization, ModelArts training management, development environment, data management, online services, and other features will not function properly. This API allows administrators to set delegation for IAM sub-users and set access keys for the current user. Calling this API requires Security Administrator permissions configured in the IAM system. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAuthorizations</td>
<td>Delete authorizations for a specific user or for all users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>GetAuthorizations</td>
<td>View the authorization list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Plugin template management</td>
<td>ShowPluginTemplate</td>
<td>Get detailed information about the specified plugin template. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="17">Service management</td>
<td>BatchDeleteServiceTags</td>
<td>Delete service tags (currently only supports online services). Batch deletion is supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServiceMonitorInfo</td>
<td>Query service monitoring information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateEdgeNodeStatus</td>
<td>Start and stop edge node service instances. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateServiceByProperty</td>
<td>Update a single property of a model service. Currently, only instance_count (updates the number of model service instances) is supported. This operation is only available for online services in the running, alarm, or exception states. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServiceSpecifications</td>
<td>Query a list of supported service deployment specifications. </td> 
<td>To be tested</td>
</tr>
<tr>
<td>CreateService</td>
<td>Deploy the model as a service. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClusters</td>
<td>Query the list of dedicated resource pools. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCreateServiceTags</td>
<td>Add tags to the specified service (currently only supports online services). If the added tag key already exists, the tag value will be overwritten. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServiceUpdateLogs</td>
<td>Query the real-time service update log. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServices</td>
<td>Query the model service list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowService</td>
<td>Query model service details, query service details by service ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PatchServiceV2</td>
<td>Update the service through the patch operation. The patch format can refer to the json patch. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListServiceTags</td>
<td>Query the inference service tags under the current project. By default, all workspaces are queried. Tag data will not be returned if the user does not have permission. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteService</td>
<td>Delete a model service. Only services under your name can be deleted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowServiceEvents</td>
<td>Query the service event log, which includes service operation records, key actions during deployment, and reasons for deployment failures. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInternalChannelVpcepApi</td>
<td>This API is used to query the inference VPC access channel. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateService</td>
<td>Update the model service configuration. This API can also be used to start and stop the service. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Algorithm management</td>
<td>ListAlgorithms</td>
<td>Query the algorithm list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSearchAlgorithms</td>
<td>Get supported hyperparameter search algorithms. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeTrainingExperiment</td>
<td>Update the training experiment information by experiment ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeAlgorithm</td>
<td>Update the algorithm. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAlgorithmByUuid</td>
<td>Query the specified algorithm by algorithm ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAlgorithm</td>
<td>Delete the algorithm. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAlgorithm</td>
<td>Create an algorithm. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Network Management</td>
<td>ListNetworks</td>
<td>Query the list of network resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateNetwork</td>
<td>Create a network resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PatchNetwork</td>
<td>Update the specified network resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteNetwork</td>
<td>Delete the specified network resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNetwork</td>
<td>Query detailed information about the specified network resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Node pool management</td>
<td>ListNodePoolNodes</td>
<td>Query the node pool's node list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateNodePool</td>
<td>Create a node pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNodePools</td>
<td>Query the node pool list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNodePool</td><td>Query the details of a specified node pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PatchNodePool</td>
<td>Update a node pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteNodePool</td>
<td>Delete a node pool. This is not supported for periodic resource pools. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Node Management</td>
<td>ListPoolNodes</td>
<td>Query the list of nodes in a resource pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRebootPoolNodes</td>
<td>Batch restart nodes in the specified resource pool</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeletePoolNodes</td>
<td>Batch delete nodes in the specified resource pool, leaving at least one node in the pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Node Configuration Template</td>
<td>ShowNodeConfigTemplate</td>
<td>Get detailed information about the specified node configuration template. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="22">Training job management</td>
<td>ShowTrainJobTags</td>
<td>Query training job tags. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSaveImageJob</td>
<td>Query training job image save tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTrainJobTags</td>
<td>Delete training job tags. Batch deletion is supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTrainingJobEvents</td>
<td>Get a list of training job events. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoSearchTrials</td>
<td>Query the results of the hyperparameter search for all trials. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoSearchYamlTemplatesInfo</td>
<td>Get information about the automated search job YAML template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangeTrainingJobDescription</td>
<td>Update the training job description. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTrainingJobDetails</td>
<td>Query the training job details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTrainingJob</td>
<td>Delete the training job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTrainingJobLogsPreview</td>
<td>Query the logs of the specified task of the training job (preview). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoSearchYamlTemplateContent</td>
<td>Get the content of the automated search job YAMl template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSaveImageJob</td>
<td>Create the image saving task of the training job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTrainJobTags</td>
<td>Create training job tags. Supports batch addition. If the added tag key already exists, the value of the tag will be overwritten. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTrainingJobMetrics</td>
<td>Query the running metrics of the specified task in the training job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowObsUrlOfTrainingJobLogs</td>
<td>Query the logs of the specified task in the training job (OBS temporary link, valid for 5 minutes). You can view the entire log or download it directly. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoSearchPerTrial</td>
<td>Query the search results for the specified trial based on the passed trial_id. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopTrainingJob</td>
<td>Terminate a training job. Only jobs that are being created, waiting, or running can be terminated. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTrainingJob</td>
<td>Create a training job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoSearchParamsAnalysis</td>
<td>Get a summary table of hyperparameter sensitivity analysis results. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTrainingJobs</td>
<td>Query the list of training jobs created by the user based on the specified query conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoSearchParamAnalysisResultPath</td>
<td>Get the save path of a hyperparameter sensitivity analysis image. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoSearchTrialEarlyStop</td>
<td>Terminate a trial of an automated search job early. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Resource and engine specifications</td>
<td>ShowTrainingJobEngines</td>
<td>Get the AI pre-configured frameworks supported by the training job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTrainingJobFlavors</td>
<td>Get the common specifications supported by the training job. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Resource metrics</td>
<td>ShowPoolRuntimeMetrics</td>
<td>Query the real-time utilization of all resource pools in the current project. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Resource tag management</td>
<td>ShowPoolTags</td>
<td>Query the tags of a specified resource pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPoolTags</td>
<td>Query all tags of resource pools in the user's current project. By default, all workspaces are queried. Tag data is not returned for workspaces without permission. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Resource pool job management</td>
<td>ShowWorkloadStatistics</td>
<td>Query the statistics of dedicated resource pool jobs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkloads</td>
<td>Query the list of dedicated resource pool jobs. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Resource pool management</td>
<td>ListPools</td>
<td>Query the list of resource pools. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePool</td>
<td>Delete the specified resource pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPool</td>
<td>Query detailed information about the specified resource pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPoolMonitor</td>
<td>Get monitoring information for the resource pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPoolStatistics</td>
<td>Get statistics for the resource pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PatchPool</td>
<td>Update the specified resource pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePool</td>
<td>Create a resource pool. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Resource specification management</td>
<td>ListResourceFlavors</td>
<td>Query the resource specification list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Configuration management</td>
<td>ShowOsConfig</td>
<td>Get the configuration parameters of the ModelArts OS service, such as network segments and user resource quotas. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Quota Management</td>
<td>ShowOsQuota</td>
<td>Get quotas for some resources in the ModelArts OS service, such as resource pool quotas and network quotas. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Image Management</td>
<td>DeleteImage</td>
<td>Delete an image object. For private images, you can also delete the SWR image content by specifying a parameter. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowImage</td>
<td>Query image details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListImage</td>
<td>Query all images that meet the specified conditions in pagination. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListImageGroup</td>
<td>Query an overview of user image information, using image name as the aggregate information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RegisterImage</td>
<td>Register a user-defined image in the ModelArts image management. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>