# IoTAnalytics MCP Server

## Version Information
v0.1.0

## Product Description

The IoTAnalytics MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud IoTAnalytics. It enables full-link management of IoTAnalytics resources using natural language processing.

## Available tools
Covering the entire API, use as needed. The list and status are as follows:

<html>
<head></head>
<body>
<table border="1" cellspacing="0" cellpadding="5">
<tbody>
<tr>
<th>Category</th>
<th>Tool Name</th>
<th>Function Description</th>
<th>Status</th>
</tr>
<tr>
<td rowspan="5">AssetModel</td>
<td>UpdateAssetModel</td>
<td>Modify Asset Model</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAssetModel</td>
<td>Create Asset Model</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAssetModels</td>
<td>Get Asset Model List</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAssetModel</td>
<td>Delete asset model</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAssetModel</td>
<td>Get asset model details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">AssetNew</td>
<td>DeleteAssetNew</td>
<td>Delete asset</td>
<td>To be tested</td>
</tr>
<tr>
<td>PublishRootAsset</td>
<td>Publish asset</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAssetsNew</td>
<td>Get asset list</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAssetNew</td>
<td>Modify asset</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAssetNew</td>
<td>Create asset</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAssetNew</td>
<td>Get asset details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">AssetProperty</td>
<td>ShowLastPropertyValue</td>
<td>Get the latest value of an asset property</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPropertyRawValue</td>
<td>Get asset property historical value</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMetricValue</td>
<td>Get asset property aggregate value</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">DataSource</td>
<td>ShowAllDataSource</td>
<td>Query data source list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDatasource</td>
<td>Create data source</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDataSource</td>
<td>Query data source details</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDataSource</td>
<td>Modify data source</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDatasource</td>
<td>Delete data source</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">DataStoreGroupManagement</td>
<td>UpdateGroup</td>
<td>Update storage group</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteGroup</td>
<td>Delete storage group</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGroups</td>
<td>Query storage group list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGroup</td>
<td>Create a storage group</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">DataStoreManagement</td>
<td>DeleteDataStore</td>
<td>Delete a store</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataStores</td>
<td>Query the store list</td>
<td>To be tested</td></tr>
<tr>
<td>UpdateDataStore</td>
<td>Update storage</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">DataStoreQuery</td>
<td>ListHistory</td>
<td>Query device history values based on tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMetrics</td>
<td>Aggregate and query data based on tags</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPropertyValues</td>
<td>Query the latest status value of device properties</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">DataStoreTags</td>
<td>ListTagValues</td>
<td>Query the tag value list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">DevData</td>
<td>AddDevData</td>
<td>Report device data through the API data source</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">PipelineManagement</td>
<td>StopPipelineJob</td>
<td>Stop a running pipeline job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPipelineJobs</td>
<td>Get all pipeline jobs under the user, supports paging. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPipelineJob</td>
<td>Get details of a specified pipeline job</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddPipelineJob</td>
<td>When creating a new pipeline job, specify the job to update in the URL. The job body will contain complete job information. (For detailed configuration of each operator in the job, refer to the Operator Configuration section.) The check parameter indicates whether the job configuration should be checked. If false, the job will not be checked and saved as a draft. If true, the job configuration will be checked. If the check fails, the job status will be changed to Draft. If the check passes, the job status will be changed to Ready and a success message will be returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePipelineJob</td>
<td>Delete the user-specified pipeline job</td>
<td>To be tested</td>
</tr>
<tr>
<td>StartPipelineJob</td>
<td>Submit the pipeline job to the runtime environment, receive data from the data source in real time, and process the data according to the user-defined data cleansing logic. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePipelineJob</td>
<td>When updating a pipeline job, specify the job to update in the URL. The complete job information will be included in the body. (Detailed configuration of pipeline jobs. Each job can select different operator combinations. For detailed instructions on using each operator, see the Data Pipeline Operator Configuration Guide.) The check parameter indicates whether the job configuration needs to be checked. If false, no check is performed and the job is saved as a draft. If true, the job configuration is checked. If the check fails, the job status is changed to draft; if the check passes, the job status is changed to ready and a success message is returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">RTAManagement</td>
<td>UpdateStreamingJob</td>
<td>When updating a job, specify the job to update in the URL. The complete job information will be included in the body. The check parameter indicates whether the job configuration should be checked. If false, the job is not checked and saved as a draft. If true, the job configuration is checked and, regardless of whether the check passes, the job and configuration information are saved as a draft. If the check fails, a failure and error message are returned. If the check passes, the job status is changed to ready and a success message is returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateStreamingJob</td>
<td>Except for the name and description, detailed job configuration information is not required. The check parameter indicates whether the job configuration should be checked. If false, the job is not checked and saved as a draft. If true, the job configuration is checked and, regardless of whether the check passes, the job and configuration information are saved as a draft. If the check fails, a failure and error message are returned. If the check passes, the job status is changed to ready and a success message is returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowJobs</td>
<td>Get all real-time analysis jobs under the user, supports paging. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowJobById</td>
<td>Get details of a specified job</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStreamingJobById</td>
<td>Delete a user-specified job</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">RTAOperation</td>
<td>StartJob</td>
<td>Submit the job to the runtime environment, receive data in real time, and process the data according to user-defined business logic. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopJob</td>
<td>Stop a running job</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">computingResource</td>
<td>DeleteComputingResource</td>
<td>Delete a batch computing resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateComputingResource</td>
<td>Create a batch computing resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListComputingResources</td>
<td>Query a list of batch computing resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">dataset</td>
<td>ImportData</td>
<td>Import data from a file into an OBS table. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportDataset</td>
<td>Download the SQL query results to your local computer. Only query results for "QUERY" type jobs are supported. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDataset</td>
<td>After the SQL query job completes, view the results of the job. Currently, only the results of "QUERY" type jobs are supported. This API only supports viewing the first 1000 result records. To view all result records, you must first export the query results and then view them. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ValidateSql</td>
<td>Check the offline job SQL syntax. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">job</td>
<td>DeleteBatchJob</td>
<td>Delete the offline job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateBatchJob</td>
<td>Create the offline job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBatchJob</td>
<td>Query the offline job details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateBatchJob</td>
<td>Modify offline jobs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBatchJobs</td>
<td>Query the offline job list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">run</td>
<td>ListRuns</td>
<td>Query the offline job run list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRun</td>
<td>Query offline job run details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRun</td>
<td>Stops a submitted or running offline job. If the job has already completed or failed, it cannot be stopped. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRun</td>
<td>Executes the offline job. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">table</td>
<td>ShowTablePreview</td>
<td>Preview the offline data table contents. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTableSchema</td>
<td>Query the offline data table structure. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTable</td>
<td>Create an offline data table. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTables</td>
<td>Query the list of offline data tables. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTable</td>
<td>Delete an offline data table. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>