# KooMap MCP Server


## Version
v0.1.0

## Overview

KooMap MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KooMap. Full-chain management of KooMap resources can be carried out based on natural language.

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
<td rowspan="8">Satellite image task management</td> 
<td>ShowTaskOverview</td> <td>View the task overview under the shared workspace, including the total number of tasks and the number of tasks in successful, running, failed, and archived status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTask</td>
<td>Used to delete tasks. Only tasks in the failed, not running, or stopped status can be deleted. After successful deletion, the task will no longer be displayed in the task list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTask</td>
<td>Create a new data processing task in the shared workspace. The "Result Image Name" parameter for the new task can be obtained from the "Verify Original Image File" interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateTaskArchivedStatus</td>
<td>Archive and unarchive tasks. After successful archiving, the task will no longer be displayed in the task list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopTask</td>
<td>Stop the task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ValidateImage</td>
<td>Verifies whether the original image file meets the matching criteria (one-to-one correspondence between panchromatic and multispectral, or all multispectral) and returns the resulting image name. If the matching criteria are not met, an error message will be displayed to the user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTaskInfo</td>
<td>Query tasks by page based on the set filter conditions (task status). </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartTask</td>
<td>Start the task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Satellite image data management</td>
<td>ListImageBaseInfo</td>
<td>Query the satellite image information list based on the filter conditions. Filter conditions include: image name, upload date, image alias, image level, image status, whether it is output data, paging offset, and number of items displayed per page. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Satellite image usage statistics</td>
<td>ListUsageInfo</td>
<td>You can query usage statistics for spatiotemporal storage services or satellite image production services. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Realistic 3D Task Management</td>
<td>UpdateReal3DTask</td>
<td>This API is used to update task information, including name, type, description, modeling image ID, modeling parameters, and modeling coordinate system. After a successful task update, the status is updated to Initialization (INIT). Only tasks in the non-running and uncompleted state can be updated: </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateReal3DTask</td>
<td>When creating a real-world 3D modeling task, you must bind it to a shared workspace. Each shared workspace is limited to 500 tasks. Task names must be unique and case-insensitive. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopReal3DTask</td>
<td>Can stop a task in the PENDING, STARTING, or RUNNING states. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskOverviewInWorkspace</td>
<td>This interface is used to display an overview of tasks within the workspace. Includes: </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartReal3DTask</td>
<td>This interface is used to start a task. After this interface is successfully executed, the task status is updated to PENDING, and the task is added to the startup queue, waiting for resources to become available. Once resources are ready, the task status changes to STARTING. If the task successfully starts, it changes to RUNNING. If the task fails, it changes to START_FAILED. For controlled modeling, aerial triangulation of the imagery is required to improve point-piercing efficiency. To perform aerial triangulation, set the "run_AT_only" field in the request body to "true." After successful triangulation, the task status changes to BUNDLE_SUCCESS. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTasksInWorkspace</td>
<td>Paged query of tasks within a single workspace, supporting filtering conditions: </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteReal3DTask</td>
<td>This interface is used to delete tasks with a status of Initialization (INIT), Start Failure (START_FAILED), Run Failure (FAILED), Stopped (STOP_SUCCESS), or Run Success (SUCCESS). Note: Deleting a task does not affect the image data of the completed 3D model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateReal3DTaskArchivedStatus</td>
<td>This interface is used to archive a successfully executed task or cancel the archived status of a task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Real-world 3D spur point management</td>
<td>DeleteSpurPoint</td>
<td>Delete spur points on the image based on their IDs. </td><td>To be tested</td>
</tr>
<tr>
<td>ListSpurPoints</td>
<td>Get all spur point information in a single image. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSpurCount</td>
<td>Based on the GCP information, query the number of spur points that have been punctured on the image. The number is equal to the number of punctured images. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddSpurPoint</td>
<td>The process of selecting GCP information from the production data list and marking it on the image is called spur point puncturing. This API is used to add a new marker to an image. The specific information for the marker includes:

<td>To be tested</td>

<tr>
<td>CreateMarkerInfo</td>
<td>Generates the marker information file required for algorithm execution based on the marker information of all images in the current task. Note: This API call requires an empty request body "{}".

<td>To be tested</td>

<tr>
<td rowspan="5">Realistic 3D Data Management</td>
<td>ListReal3DRefineProducts</td>
<td>Query the data list of real-world 3D refinement post-processing results. Supported filter parameters:

<td>To be tested</td>

</tr>
<tr>
<td>ListFolder</td>
<td>Query the basic information list of the current tenant's oblique imagery based on the filter conditions. Filtering conditions include: image name, image alias, image upload start and end time, image status, image description, paging offset, number of items displayed per page, and image sorting rules. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteReal3DProduct</td>
<td>Delete a real 3D product image. This function can only be deleted when the product image status is "available." After executing this interface, the product image status is updated to "deleting." After deletion, the product image is deleted and the data cannot be restored. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteReal3DRefineProduct</td>
<td>Call this interface to delete the real 3D refinement post-processing product data. Currently, deletion is only supported when the product data status is "available." After executing this interface, the product data status is updated to "deleting." </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListReal3DProducts</td>
<td>Query the list of real 3D product images. The returned image query results are sorted in reverse order by update time. Querying based on the following conditions is supported: </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Real 3D Usage Statistics</td>
<td>ShowReal3DUsage</td>
<td>You can query the usage statistics for the Real 3D production service's spatiotemporal dedicated storage or image modeling. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Real 3D Refinement Post-Processing Task Management</td>
<td>DeleteReal3DSubTask</td>
<td>This API can be used to delete a refinement post-processing task whose status is Initialization (INIT), Upload Success (UPLOAD_SUCCESS), Upload Failure (UPLOAD_FAILED), Start Failure (START_FAILED), Run Success (SUCCESS), Run Failure (FAILED), or Stopped (STOP_SUCCESS). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListReal3DSubTasks</td>
<td>Query the post-processing tasks within a single real-life 3D modeling task by page. Filter conditions are supported: </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartReal3DSubTask</td>
<td>This API is used to start a post-processing task. After this API is successfully executed, the task status is updated to PENDING. The task is then added to the startup queue, awaiting the readiness of resources. Once resources are ready, the status is updated to STARTING. After successful startup, the status is updated to RUNNING. If the startup fails, the status is updated to START_FAILED. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopReal3DSubTask</td>
<td>This interface is used to stop a refinement post-processing task in the PENDING, STARTING, or RUNNING states. After the task is stopped, the status update rules are as follows: </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateReal3DSubTask</td>
<td>Each refinement post-processing task must be bound to a completed task of the "Explicit Radiation Field" modeling type. A single task is limited to creating a maximum of 10 refinement post-processing tasks, and names must be unique (case-insensitive). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Shared Workspace</td>
<td>CreateCommonWorkspace</td>
<td>This interface supports the creation of shared workspaces, facilitating categorized management of tasks. A tenant can create up to 500 shared workspaces, and shared workspace names must be unique (case-insensitive). </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCommonWorkspace</td>
<td>This interface is used to delete a shared workspace. Before deleting, ensure that the space is not pinned and contains no tasks; otherwise, the deletion will fail. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCommonWorkspace</td>
<td>This interface is used to update shared workspace information. The following content can be updated:

<td>To be tested</td>

<tr>
<td>ListCommonWorkspace</td>
<td>This API is used to query the shared workspace list in a paginated manner and supports filtering conditions:

<td>To be tested</td>

</tr>
<tr>
<td rowspan="1">Spatial Positioning</td>
<td>StartVps</td>
<td>Visual positioning is a technology that determines the location of a device based on images coupled with GPS data. A map is created by capturing a series of images with known locations and analyzing their key visual features (such as the outlines of buildings or bridges). This creates a large-scale, rapidly searchable index of these visual features. By comparing features in the device images with those in the index, the pose of the target device can be determined. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Spatial Navigation</td>
<td>StartNavi</td>
<td>AR navigation is a new type of map navigation method. It uses real-time camera-captured images to translate map navigation information into digital content.The shape is superimposed on the real scene, generating a virtual 3D navigation guide. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>