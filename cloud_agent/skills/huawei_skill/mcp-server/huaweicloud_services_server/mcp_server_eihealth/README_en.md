# eiHealth MCP Server

## Version Information
v0.1.0

## Product Description

The eiHealth MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud eiHealth. It enables full-link management of eiHealth resources based on natural language processing.

## Available Tools
Cover the entire API, available as needed. The list and status are as follows:

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
<td rowspan="2">ADMET</td>
<td>ShowAdmetWithCustomProps</td>
<td>Calculates the physicochemical properties of small molecules, including default absorption, distribution, metabolism, excretion, and toxicity, as well as user-defined properties. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAdmetProperties</td>
<td>Calculate the physicochemical properties of small molecules, including adsorption, distribution, metabolism, excretion, and toxicity. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">CPI</td>
<td>CreateCpiTask</td>
<td>Input a protein sequence and a small molecule library to create a molecule-protein interaction prediction task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCpiTaskResult</td>
<td>Query the CPI task status and results using the CPI task ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">CPI job management</td>
<td>CreateCpiJob</td>
<td>Create a CPI job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCpiJob</td>
<td>Query CPI job details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">CSS cluster management</td>
<td>DeleteCssCluster</td>
<td>Unbind a CSS cluster</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCssCluster</td>
<td>Bind a CSS cluster</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTermTenantCssCluster</td>
<td>Get the final tenant CSS cluster list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ValidateCssConnection</td>
<td>Test CSS cluster connection</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCssCluster</td>
<td>Get the CSS cluster list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">CustomProps</td>
<td>ShowCustomPropsTaskResult</td>
<td>Query the task status and result using the custom property task ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCustomPropsTask</td>
<td>Enter the task data for custom properties and create a custom property modeling task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Generation</td>
<td>ShowGenerationTaskResult</td>
<td>Query the status and results of the molecule generation task using the molecule generation task ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGenerationTask</td>
<td>Enter the molecule property constraints and create a molecule generation task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="14">IDrugCommonController</td>
<td>CreateDrugLigandInteraction2dSvg</td>
<td>Generates a 2D interaction graph. If a ligand file is not provided, the receptor file must contain the ligand. If a ligand file is provided, the ligand in the receptor (if any) will be ignored.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDrugLigandSimilarityGraphTask</td>
<td>Query the ligand similarity graph calculation task</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDrugLigandSdf</td>
<td>Generate a 3D SDF structure of the molecule</td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckDrugLigandDifference</td>
<td>Calculate 3D structural differences between ligands</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDrugLigandSimilarityGraphTask</td>
<td>Delete ligand similarity graph calculation task</td>
<td>To be tested</td>
</tr>
<tr>
<td>ParseDrugReceptorInfo</td>
<td>Parse receptor information. If there are multiple receptor proteins, only the first one will be processed. If a receptor protein binds to multiple ligands, only the first 10 will be processed at most. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDrugLigandPreviewTask</td><td>Create a ligand file preview task, supporting SMI, SDF, PDB, and MOL2.
<td>To be tested.
</tr>
<tr>
<td>ShowDrugLigandPreviewTask</td>
<td>Query the ligand file preview task.
<td>To be tested.
</tr>
<tr>
<td>RunDrugReceptorPreprocess</td>
<td>Receptor preprocessing, used to display preprocessed receptors on the front end.
<td>To be tested.
</tr>
<tr>
<td>RecognizeDrugReceptorPocket</td>
<td>Detect receptor pockets, including ligand-based, amino acid residue-based, automatic detection, custom, and global docking.
<td>To be tested.
</tr>
<tr>
<td>CreateDrugLigandSimilarityGraphTask</td>
<td>Create a ligand similarity graph calculation task</td>
<td>To be tested</td>
</tr>
<tr>
<td>RunDrugLigandToSmilesConversion</td>
<td>Convert the ligand format to SMILES. If there are multiple molecules in the ligand file, only the first one will be returned.</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDrugLigandPreviewTask</td>
<td>Delete the ligand file preview task</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDrugLigandSvg</td>
<td>Generate a molecular SVG graph</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">IObsController</td>
<td>DownloadData</td>
<td>File Download</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">IOverviewController</td>
<td>ShowOverview</td>
<td>Get Medical Platform Information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Nextflow Task Management</td>
<td>ListNextflowTask</td>
<td>Get Task List</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNextflowTaskLog</td>
<td>Get Nextflow Task Log</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNextflowTaskDetail</td>
<td>Get task details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Nextflow job management</td>
<td>ShowNextflowJobLog</td>
<td>Get Nextflow job log</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteNextflowJob</td>
<td>Delete Nextflow job</td>
<td>To be tested</td>
</tr>
<tr>
<td>StopNextflowJob</td>
<td>Stop Nextflow job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNextflowJob</td>
<td>Query the nextflow job list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNextflowJob</td>
<td>Get Nextflow job details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateNextflowJob</td>
<td>Create nextflow job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNextflowJobReports</td>
<td>Get Nextflow job report</td>
<td>To be tested</td>
</tr>
<tr>
<td>RetryNextflowJob</td>
<td>Retry Nextflow job</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Nextflow engine lifecycle management</td>
<td>InstallNextflow</td>
<td>Install Nextflow (either the file or version parameter must be provided)</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNextflowVersion</td>
<td>Query the Nextflow version list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNextflow</td>
<td>Query Nextflow configuration details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CleanNextflowCache</td>
<td>Clean NextflowCache</td>
<td>To be tested</td>
</tr>
<tr>
<td>UninstallNextflow</td>
<td>Uninstall Nextflow</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Nextflow Workflow Management</td>
<td>ShowNextflowWorkflow</td><td>Get Workflow Details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNextflowWorkflow</td>
<td>Get Workflow List</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteNextflowWorkflow</td>
<td>Delete Workflow</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateNextflowWorkflow</td>
<td>Update Workflow</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateNextflowWorkflow</td>
<td>Create Workflow</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">OBS Bucket Management</td>
<td>DownloadPublicData</td>
<td>File Download</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListObsBucketObject</td>
<td>Get objects in the user's OBS bucket</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListObsBucket</td>
<td>Get the user's OBS bucket list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Optimization</td>
<td>CreateOptimizationTask</td>
<td>Enter the starting small molecule and property constraints to create a molecular optimization task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOptimizationTaskResult</td>
<td>Query the status and results of the molecular optimization task by the molecular optimization task ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Search</td>
<td>CreateSearchTask</td>
<td>Enter the molecule to be searched and the search conditions to create a molecular search task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSearchTaskResult</td>
<td>Query the status and results of the molecular search task by the molecular search task ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Synthesis</td>
<td>CreateSynthesisTask</td>
<td>Input the molecule for synthesis path planning and output the number of feasible solutions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSynthesisTaskResult</td>
<td>Query the status and results of the molecular synthesis path planning task by its ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Notebook Development Environment</td>
<td>ListUserNotebook</td>
<td>Get a list of notebooks in the user's space. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ListNotebook</td> 
<td>Get notebook list</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateNotebook</td> 
<td>Create notebook</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ListNotebookTool</td> 
<td>Get notebook working environment</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>UpdateNotebook</td> 
<td>Update notebook</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>DeleteNotebook</td> 
<td>Delete notebook</td> 
<td>To be tested</td>
</tr>
<tr>
<td>StopOrStartNotebook</td>
<td>Start or stop notebook</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNotebook</td>
<td>Get notebook details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowNotebookToken</td>
<td>Get notebook authentication information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Business delegation management</td>
<td>ShowAgency</td>
<td>Get business delegation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAgency</td>
<td>Update the business delegation. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Job cleanup configuration</td>
<td>ShowJobConfig</td>
<td>Get the job configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateJobConfig</td>
<td>Set the job configuration. Currently, you can modify the number of jobs saved (10,000 to 10 million). The default setting is 5 million. </td>
<td>To be tested</td></tr>
<tr>
<td rowspan="18">Job Management</td>
<td>ExecuteJob</td>
<td>Start a job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskInstanceEvents</td>
<td>Get events for instances in a subtask</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateJob</td>
<td>Update a job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskInstances</td>
<td>Get subtask instance information</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchRetryJob</td>
<td>Batch retry job</td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelJob</td>
<td>Cancel or force job scheduling</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowJobEvent</td>
<td>Get job events</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTaskInstancePod</td>
<td>Get pod information for instances in a subtask</td>
<td>To be tested</td>
</tr>
<tr>
<td>RetryJob</td>
<td>Retry a job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListJob</td>
<td>Get a job list</td>
<td>To be tested tested</td>
</tr>
<tr>
<td>ShowTaskEvents</td>
<td>Get subtask start events</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserJob</td>
<td>Get a list of jobs for the space to which the user belongs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchCancelJob</td>
<td>Batch cancel job</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteJob</td>
<td>Batch delete job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowJobLog</td>
<td>Get job log</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowJob</td>
<td>Get job details</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteJob</td>
<td>Delete job</td>
<td>To be tested tested</td>
</tr>
<tr>
<td>ShowTaskInstanceMetricData</td>
<td>Get resource monitoring data for instances in a subtask</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Vendor management</td>
<td>ListVendor</td>
<td>Get vendor list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Molecular optimization job management</td>
<td>CreateOptmJob</td>
<td>Create molecular optimization job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOptmJob</td>
<td>Query molecular optimization job details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Molecular synthesis path planning job management</td>
<td>CreateSynthesisJob</td>
<td>Create molecular synthesis path planning job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSynthesisJob</td>
<td>Query molecular synthesis path planning job details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Molecular docking job management</td>
<td>CreateDockingJob</td>
<td>Create molecular docking job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDockingJob</td>
<td>Query molecular docking job details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Molecular attribute prediction job management</td>
<td>ShowAdmetJob</td>
<td>Query molecular attribute prediction job details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAdmetJob</td>
<td>Create a molecular attribute prediction job</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Molecular search job management</td>
<td>CreateSearchJob</td>
<td>Create a molecular search job</td>
<td>TTo be tested</td>
</tr>
<tr>
<td>ShowSearchJob</td>
<td>Query molecule search job details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Molecule generation job management</td>
<td>ShowGenJob</td>
<td>Query molecule generation job details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateGenJob</td>
<td>Create molecule generation job</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Initialize platform</td>
<td>InitializePlatform</td>
<td>Initialize platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Storage resource query</td>
<td>ListStorageResources</td>
<td>Query storage resources</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Application management</td>
<td>PublishApp</td>
<td>Publish application</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApp</td>
<td>Delete application</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchImportApp</td>
<td>Batch import application</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserApp</td>
<td>Gets a list of apps in the user's space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateApp</td>
<td>Update app</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateApp</td>
<td>Create app</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApp</td>
<td>Get app details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApp</td>
<td>Get app list</td>
<td>To be tested</td>
</tr>
<tr>
<td>SubscribeApp</td>
<td>Subscribe app</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Performance Acceleration Resource Management</td>
<td>ListPerformanceResources</td>
<td>Query Performance Acceleration Resources</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePerformanceResource</td>
<td>Purchase Performance Acceleration Resources</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSfsTurbos</td>
<td>Get a list of sfs-turbo resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePerformanceResource</td>
<td>Delete performance acceleration resource</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePerformanceResource</td>
<td>Update performance acceleration resource configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Favorite Management</td>
<td>CreateFavorite</td>
<td>Add to favorites. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteFavorite</td>
<td>Cancel favorites. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFavorite</td>
<td>Get the favorites list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Data job management</td>
<td>CancelDataJob</td>
<td>Cancel data job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCheckpoint</td>
<td>Get data job execution log</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDataJob</td>
<td>Get data job details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDataJob</td>
<td>Get data job list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DownloadDataJobLog</td>
<td>Download data job execution log</td>
<td>To be tested</td>
</tr>
<tr>
<td>RetryDataJob</td>
<td>Retry data job</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDataJob</td>
<td>Delete data job</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">Database management</td>
<td>QuoteInstance</td>
<td>Quote database instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDatabaseData</td>
<td>Delete the specified row of data</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDatabaseData</td>
<td>Update data</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDatabaseData</td>
<td>Insert a single row of data</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowInstance</td>
<td>Query instance details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInstance</td>
<td>Create a database instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInstance</td>
<td>Delete an instance</td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportDatabaseData</td>
<td>Import data</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDatabaseData</td>
<td>Query data</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInstance</td>
<td>Get instance list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Database resource management</td>
<td>DeleteDatabaseResource</td>
<td>Delete database resource</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDatabaseResource</td>
<td>Query database resource</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDatabaseResource</td>
<td>Purchase database resource</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDatabaseResourceFlavor</td>
<td>Get database resource flavor list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Data Archiving</td>
<td>DeleteBackup</td>
<td>Delete the specified archive</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBackupPath</td>
<td>Get the full data list of the archive based on the archive ID</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateBackup</td>
<td>Copy important data to be archived to the data archive bucket</td>
<td>To be tested</td>
</tr>
<tr>
<td>RestoreBackup</td>
<td>Copy the specified archive data to a directory in the target project</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBackup</td>
<td>Paged query of all historical archive records for user-managed projects</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="16">Data management</td>
<td>ShowDataPolicy</td>
<td>Query project-level data permission control policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>SubscribeData</td>
<td>Subscribe to asset market data</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateData</td>
<td>Create a folder</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDataPolicy</td>
<td>Set project-level permission control policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBucket</td>
<td>Get a bucket list (including the current project bucket and referenced project buckets)</td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportNetworkData</td>
<td>Import network data</td>
<td>To be tested</td>
</tr>
<tr>
<td>CopyData</td>
<td>Copy project data</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteData</td>
<td>Batch delete project data</td>
<td>To be tested</td>
</tr>
<tr><td>ImportData</td>
<td>Import project data</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBucketStorage</td>
<td>Get bucket storage information</td>
<td>To be tested</td>
</tr>
<tr>
<td>QuoteData</td>
<td>Quote project data</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowData</td>
<td>Get detailed information about a specified data object</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDataPathPolicy</td>
<td>Set data object policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>PublishData</td>
<td>Publish data assets</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListData</td>
<td>Query the data list under the specified directory. If not specified, the default query root directory is used.
<td>To be tested</td>
</tr>
<tr>
<td>UploadData</td>
<td>Upload data files</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Tag management</td>
<td>ListLabel</td>
<td>Get a tag list</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLabel</td>
<td>Delete a tag</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateLabel</td>
<td>Create a label</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteLabel</td>
<td>Batch delete labels</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Label page management</td>
<td>CreateLabelPage</td>
<td>Create a label page</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLabelPage</td>
<td>Delete a label page</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLabelPage</td>
<td>Get a list of label pages</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Template Management</td>
<td>ShowTemplate</td>
<td>Query Template Details</td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadTemplate</td>
<td>Upload Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTemplate</td>
<td>Create Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTemplate</td>
<td>Query Template List</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTemplate</td>
<td>Delete Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportTemplate</td>
<td>Import a template from another project</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Process Management</td>
<td>DeleteWorkflow</td>
<td>Delete a process</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWorkflow</td>
<td>Create a process</td>
<td>To be tested</td>
</tr>
<tr>
<td>PublishWorkflow</td>
<td>Publish a process</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkflow</td>
<td>Get a list of processes</td>
<td>To be tested</td>
</tr>
<tr>
<td>SubscribeWorkflow</td>
<td>Subscribe to a workflow</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserWorkflow</td>
<td>Get a list of workflows in the user's space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWorkflow</td>
<td>Update a workflow</td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportWorkflow</td>
<td>Import a workflow</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWorkflow</td><td>Get process details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Process statistics management</td>
<td>ListPerformanceResourceStat</td>
<td>Get statistics on performance acceleration resources</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWorkflowStatistic</td>
<td>Count applications, processes, and jobs</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGlobalWorkflowStatistic</td>
<td>Count global process and job information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="13">Message center management</td>
<td>CheckEmailConnection</td>
<td>Mailbox Connectivity Test</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMessageStatistics</td>
<td>Message Statistics</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMessageEmailConfig</td>
<td>Set Message Email Configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteNotice</td>
<td>Batch Delete Notification Messages</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNotice</td>
<td>Get Notification Message List</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMessageReceiveConfig</td>
<td>Set user email configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateNotice</td>
<td>Batch update messages</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListMessage</td>
<td>Get a list of messages that the current user has permission to view from the message center</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMessageClearRule</td>
<td>Get message clearing rules</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMessageReceiveConfig</td>
<td>Get user email configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMessageEmailConfig</td>
<td>Get message email configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMessageClearRuleRequestBody</td>
<td>Set message cleanup rules, supports modifying the number of records (10,000-1,000,000)</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteMessageEmailConfig</td>
<td>Delete message email configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="19">User Management</td>
<td>ListMfa</td>
<td>Get available authentication methods</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUserByDomain</td>
<td>Modify sub-users in the final tenant</td>
<td>To be tested tested</td>
</tr>
<tr>
<td>ListIamGroups</td>
<td>Query the IAM user group list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckTokenVerification</td>
<td>Verify that the token can access the current environment</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowUserSetting</td>
<td>Query user settings</td>
<td>To be tested</td>
</tr>
<tr>
<td>ValidateCode</td>
<td>Pre-authentication</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUserSetting</td>
<td>Update user settings</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUser</td>
<td>Modify user basic information (email, phone number)</td>
<td>To be tested</td>
</tr>
<tr>
<td>ImportUser</td>
<td>Import user</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUserRole</td>
<td>Update user role</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListIamGroupUsers</td>
<td>Query the user list of the IAM user group</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateCode</td>
<td>Send verification code</tdd>
<td>To be tested</td>
</tr>
<tr>
<td>ListUser</td>
<td>Get user list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowUser</td>
<td>Get specified user details</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteUser</td>
<td>Delete user</td>
<td>To be tested</td>
</tr>
<tr>
<td>ChangePassword</td>
<td>Change password</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateUser</td>
<td>Create user</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateInitPassword</td>
<td>Reset password for new users</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListIamUsers</td>
<td>Query the IAM user list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Pangu drug molecule model billing management</td>
<td>ListDrugModelResource</td>
<td>Query the Pangu drug molecule model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDrugModelResource</td>
<td>Create the Pangu drug molecule model. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDrugModelResource</td>
<td>Unsubscribe from Pangu Drug Molecule Model. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Space Management</td>
<td>UpdateTopProject</td>
<td>Pin the space to the top. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Space Statistics Interface</td>
<td>ListProjectStatistics</td>
<td>Get the current user's space resource statistics. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">System configuration internal interface</td>
<td>ListArchiveConfigs</td>
<td>Get cross-domain archive configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowVendor</td>
<td>Get vendor configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEnv</td>
<td>Get system configuration list</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateVendor</td>
<td>Set vendor configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateArchiveConfig</td>
<td>Modify cross-domain archive settings</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Get system quotas and resource usage</td>
<td>ListQuota</td>
<td>Get current system quotas and resource usage</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Clustering analysis job management</td>
<td>CreateClusteringJob</td>
<td>Create a clustering analysis job.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowClusteringJob</td>
<td>Query clustering analysis job details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">AutoJob Management</td>
<td>StartAutoJob</td>
<td>Start an AutoJob</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAutoJob</td>
<td>Query AutoJob Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAutoJob</td>
<td>Get AutoJob Template List</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAutoJob</td>
<td>Create an AutoJob Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAutoJob</td>
<td>Delete AutoJob Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>StopAutoJob</td>
<td>Stop AutoJob</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAutoJob</td>
<td>Update AutoJob Template</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Free EnergyPerturbation Job Management
<td>CreateFepJob</td>
<td>Create a free energy perturbation job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowFepJob</td>
<td>Query free energy perturbation job details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Node Label Management</td>
<td>ListPresetLabel</td>
<td>Get a list of preset labels</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateNodeLabel</td>
<td>Set node labels</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNodeLabel</td>
<td>Get Node Label Set</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClusterAllNodeLabel</td>
<td>Get Node Label Set</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Drug Job Management</td>
<td>DeleteDrugJob</td>
<td>Delete Drug Job</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateClusterJob</td>
<td>Create Molecular Clustering Job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDrugJob</td>
<td>Get Drug Job List</td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelDrugJob</td>
<td>Cancel a drug job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserDrugJob</td>
<td>Get a list of drug jobs for the user's space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDrugJob</td>
<td>Update drug job</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Drug database management</td>
<td>DeleteDrugDatabase</td>
<td>Delete database</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDrugDatabase</td>
<td>Update drug database</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDrugDatabaseFile</td>
<td>Add database file</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDrugDatabase</td>
<td>Get database list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDrugDatabase</td>
<td>Create database</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Drug model management</td>
<td>ListDrugModel</td>
<td>Get model list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBaseModel</td>
<td>Get base model list</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDrugModel</td>
<td>Create model</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDrugModel</td>
<td>Update the drug model</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDrugModel</td>
<td>Delete the model</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Drug Common Interface</td>
<td>GeneratePocketFile</td>
<td>Generate renderable pocket file content based on center, size, and padding parameters</td>
<td>To be tested</td>
</tr>
<tr>
<td>GenerateSurfacePoints</td>
<td>Generate renderable file content based on a set of discrete surface point coordinates</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateMolDockingJob</td>
<td>Single-molecule pre-docking. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RunFastaPreprocess</td>
<td>Acceptor pre-processing (Fasta format), used by the front-end to calculate the expected number of deductions</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateMolBatchDownloadTask</td>
<td>Create a batch download task for molecules or molecular complexes</td>
<td>To be tested</td>
</tr>
<tr>
<td>RunFormatConverter</td>
<td>Single-molecule file format conversion. </td>
<td>To be tested</td></tr>
<tr>
<td>GenerateComplexCombine</td>
<td>Assemble the incoming protein and small molecule into a complex structure</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMolBatchDownloadTask</td>
<td>Query the batch download task details for molecules or molecular complexes</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Virtual Drug Screening</td>
<td>Show3dStructureContent</td>
<td>Get the content of the generated study job 3D structure</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateStudyJob</td>
<td>Create a study job</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateStudy</td>
<td>Create a study</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStudyJob</td>
<td>List all study jobs</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStudy</td>
<td>Delete a study</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowExtremumInfo</td>
<td>Get the maximum value information of the study job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStudy</td>
<td>List a study</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">Compute Resource Scaling</td>
<td>ListScalingHistory</td>
<td>Get Policy Scaling History</td>
<td>To be tested</td>
</tr>
<tr>
<td>StartScaleOutPolicy</td>
<td>Start the automatic scaling policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPolicyEvents</td>
<td>Get Policy Events</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateScaleInPolicy</td>
<td>Modify the scaling policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateScaleOutPolicy</td>
<td>Create a scaling policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowScaleInPolicy</td>
<td>Query the scale-in policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListNodes</td>
<td>Get a list of computing resources associated with the policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowScaleOutPolicy</td>
<td>Get scale-out policy details</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteScaleOutPolicy</td>
<td>Delete the scale-out policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateScaleOutPolicy</td>
<td>Modify the scale-out policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>StopScaleOutPolicy</td>
<td>Stop the automatic scale-out policy</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListScaleOutPolicy</td>
<td>Query the scale-out policy list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">Computing resource management internal interface</td>
<td>RebootNode</td>
<td>Restart the computing resource</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSchedule</td>
<td>Modify computing resource scheduling information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListComputingResourceFlavors</td>
<td>Query computing resource specifications</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSchedule</td>
<td>Query computing resource scheduling information</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteComputingResource</td>
<td>Delete computing resources</td>
<td>To be tested</td>
</tr>
<tr>
<td>StartNode</td>
<td>Start computing resources</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateComputingResource</td>
<td>Purchase computing resources</td>
<td>To be tested</td>
</tr>
<tr> 
<td>ShowLeftQuota
<td>Get the remaining node quota</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListComputingResources</td>
<td>Query computing resources</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowEvsQuota</td>
<td>Get EVS quota and usage</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowBmsDevices</td>
<td>Query the list of BMS computing resource graphics card IDs</td>
<td>To be tested</td>
</tr>
<tr>
<td>StopNode</td>
<td>Stop computing resources</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Computing Cluster Management</td>
<td>DeleteComputingCluster</td>
<td>Unbind a computing cluster. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListComputingCluster</td>
<td>Get a list of computing clusters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateComputingCluster</td>
<td>Bind a computing cluster. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListCceCluster</td>
<td>Get a list of CCE clusters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListClusterInstallStep</td>
<td>Query the list of installation steps for a specified cluster. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Asset collection management</td>
<td>ListStar</td>
<td>Get a list of collected assets</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteStar</td>
<td>Cancel a collection</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStar</td>
<td>Collect an asset</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Asset management</td>
<td>ListAsset</td>
<td>Get a list of assets</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAssetVersion</td>
<td>Delete a specific asset version</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAssetVersion</td>
<td>Query asset version details</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAssetVersion</td>
<td>Update asset version information</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAsset</td>
<td>Query asset details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListProperty</td>
<td>Get a list of property values</td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteAssetAction</td>
<td>Operate asset publishing status</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Get resource monitoring data</td>
<td>ShowResourceMetricData</td>
<td>Get resource monitoring data</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDownloadResourceStatData</td>
<td>Get resource statistics data in batches</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">Image management</td>
<td>ImportImage</td>
<td>Import image</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDockerLogin</td>
<td>Get the docker login command</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUserImage</td>
<td>Get the image list of the user's space. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListImageTag</td>
<td>Get the tag list of the specified image</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteImage</td>
<td>Delete the image repository</td>
<td>To be tested</td>
</tr>
<tr>
<td>PublishImage</td>
<td>Publish an image</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateImage</td>
<td>Update the image descriptionInformation or type</td>
<td>To be tested</td>
</tr>
<tr>
<td>SubscribeImage</td>
<td>Subscribe to an image</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateImage</td>
<td>Create an image</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTag</td>
<td>Delete a specified image tag</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListImage</td>
<td>Get an image list</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteTag</td>
<td>Batch delete image tags</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Target Optimization Job Management</td>
<td>CreateTargetOptJob</td>
<td>Create Target Optimization Job</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTargetOptJob</td>
<td>Query Target Optimization Job Details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Target Pocket Molecule Design Job Management</td>
<td>ShowPocketMolDesignJob</td>
<td>Query Target Pocket Molecule Design Job Details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePocketMolDesignJob</td>
<td>Create Target Pocket Molecule Design Job</td>
<td>To be tested tested</td>
</tr>
<tr>
<td rowspan="2">Target Pocket Detection Job Management</td>
<td>ShowPocketDetectionJob</td>
<td>Query Target Pocket Detection Job Details</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePocketDetectionJob</td>
<td>Create Target Pocket Detection Job</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="14">Project Management</td>
<td>BatchDeleteMember</td>
<td>Batch Delete Project Members</td>
<td>To be tested</td>
</tr>
<tr>
<td>TransferProject</td>
<td>Transfer Project</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteMember</td>
<td>Remove project members</td>
<td>To be tested</td>
</tr>
<tr>
<td>DownloadDataTrace</td>
<td>Download nearly 10,000 audit logs</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProject</td>
<td>Get project details</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProjectTrace</td>
<td>Get project audit log</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProjectTracker</td>
<td>Get project audit log tracker</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMember</td>
<td>Update or add project member roles</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProject</td>
<td>Update a project</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListProject</td>
<td>Get a list of projects</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProjectTraceData</td>
<td>Get a specified audit log</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProjectTracker</td>
<td>Update the project audit log tracker configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteProject</td>
<td>Delete Project</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateProject</td>
<td>Create Project</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>