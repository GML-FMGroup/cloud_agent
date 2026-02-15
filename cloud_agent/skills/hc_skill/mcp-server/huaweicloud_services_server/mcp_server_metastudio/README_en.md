# MetaStudio MCP Server 

## Version Information
v0.1.0

## Product Description

MetaStudio MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud MetaStudio. It enables full-link management of MetaStudio resources using natural language.

## Available Tools
Covering the full API, available for use as needed. The list and status are as follows:

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
<td rowspan="6">ActiveCodeManagement</td>
<td>ListActiveCode</td>
<td>This API is used to query the activation code list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateActiveCode</td>
<td>This API is used to create an activation code. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetActiveCode</td>
<td>This interface is used to reset the activation code. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteActiveCode</td>
<td>This interface is used to delete the activation code. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowActiveCode</td>
<td>This interface is used to query activation code details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateActiveCode</td>
<td>This interface is used to modify the activation code. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">AgencyManagement</td>
<td>DeleteAgencyWithRoleType</td>
<td>This interface is used to delete a delegate under a project. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAgencyWithRoleType</td>
<td>This interface is used to create a delegate. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAgency</td>
<td>This interface is used to query the agency under the project. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">AsrVocabularyManagement</td>
<td>CreateAsrVocabulary</td>
<td>This interface is used to create a hotword list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAsrVocabulary</td>
<td>This interface is used to query the hotword list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAsrVocabulary</td>
<td>This interface is used to query the hotword list details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAsrVocabulary</td>
<td>This interface is used to modify the hotword list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAsrVocabulary</td>
<td>This interface is used to delete the hotword list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAsrVocabularyAssociation</td>
<td>This interface is used to query the hotword list association details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">DialogManagement</td>
<td>ListSmartChatJob</td>
<td>This interface is used to query the list of digital human intelligent interaction tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopSmartChatJob</td>
<td>This interface is used to end a digital human intelligent interaction task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartSmartChatJob</td>
<td>This interface is used to start a digital human intelligent interaction task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDialogUrl</td>
<td>This interface is used to create a dialog link. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSmartChatJob</td>
<td>This interface is used to query digital human intelligent interaction tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">DialogReportConfigManagement</td>
<td>CreateDialogReportConfig</td>
<td>This interface is used to create a dialog result reporting configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDialogReportConfig</td>
<td>This interface is used to modify a dialog result reporting configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDialogReportConfig</td>
<td>This interface is used to query the dialog result reporting configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDialogReportConfig</td>
<td>This interface is used to delete the conversation result reporting configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">DigitalAssetContentManager</td>
<td>ListAssetSummary</td>
<td>This interface is used to query the summary information of multiple specified assets in the media asset library. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAsset</td>
<td>This interface is used to delete media assets from the asset library. When calling this interface to delete a media asset, the media asset is placed in the recycle bin and is not completely deleted. To completely delete the asset, add the "mode=force" parameter. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDigitalAsset</td>
<td>This interface is used to update media asset information in the asset library. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAssets</td>
<td>This interface is used to query the list of media assets in the asset library. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RestoreAsset</td>
<td>This interface is used to restore media assets that have been deleted from the Recycle Bin. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAssetReplicationInfo</td>
<td>When replicating assets from Region A to Region B, first call this interface in Region A to query asset replication information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDigitalAsset</td>
<td>This interface is used to add and upload new media assets to the asset library. Uploadable asset types include: avatar models, background images, source images, source videos, and PPT presentations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAssetByReplicationInfo</td>
<td>This API is used to replicate a specified asset from Region A to Region B. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchExecuteAssetAction</td>
<td>This API operates on batch assets. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAsset</td>
<td>This API is used to query the details of a specified media asset in the asset library. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">DigitalHumanBusinessCard</td>
<td>UpdateDigitalHumanBusinessCard</td>
<td>This interface is used to update the digital human business card creation task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDigitalHumanBusinessCard</td>
<td>This interface is used to query the digital human business card creation task list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDigitalHumanBusinessCard</td>
<td>This interface is used to delete the digital human business card creation task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDigitalHumanBusinessCard</td>
<td>This interface is used to query the details of the digital human business card creation task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDigitalHumanBusinessCard</td>
<td>This interface is used to create the digital human business card task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">DigitalHumanVideoManager</td>
<td>ListDigitalHumanVideo</td>
<td>This interface is used to query the video creation task list. You can query the video creation list for the avatar digital human, the photo digital human video creation list, etc. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">DigitalHumanVideoManagerFor2D</td>
<td>Show2DDigitalHumanVideo</td>
<td>This interface is used to query the details of the digital human video production task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Create2DDigitalHumanVideo</td>
<td>This interface is used to create a digital human video production task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Cancel2DDigitalHumanVideo</td>
<td>This interface is used to cancel the pending digital human video production task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">DigitalHumanVideoManagerForPhoto</td>
<td>ShowPhotoDetection</td>
<td>This interface is used to query the details of the photo detection task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPhotoDigitalHumanVideo</td>
<td>This interface is used to query the details of the photo avatar digital human video production task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelPhotoDigitalHumanVideo</td>
<td>This interface is used to cancel the pending photo avatar digital human video production task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePhotoDigitalHumanVideo</td>
<td>This API is used to create a digital human video production task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePhotoDetection</td>
<td>This API is used to create a photo detection task.Task: Check whether a photo meets the requirements for creating a digital human. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">FileManager</td>
<td>DeleteFile</td>
<td>This interface is used to delete a specified file from the media asset library. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateFile</td>
<td>This interface is used to create a file and obtain an upload URL. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateLargeFile</td>
<td>This interface is used to create a large file (over 5GB) and obtain a multipart upload URL. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ConfirmFileUpload</td>
<td>After the asset file is uploaded, confirm the upload completion through this interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">HotQuestionManagement</td>
<td>CreateHotQuestion</td>
<td>This interface is used to create a hot question. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteHotQuestion</td>
<td>This interface is used to delete a hot question. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowHotQuestion</td>
<td>This interface is used to query hot question details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateHotQuestion</td>
<td>This interface is used to modify hot questions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHotQuestion</td>
<td>This interface is used to query the hot question list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">HotWordsManagement</td>
<td>ShowHotWords</td>
<td>This interface is used to query hot word record details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateHotWordsSwitch</td>
<td>This interface is used to modify the hot word function switch. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateHotWords</td>
<td>This interface is used to modify hot word records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteHotWords</td>
<td>This interface is used to delete hot word records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHotWords</td>
<td>This interface is used to query the hot word record list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateHotWords</td>
<td>This interface is used to create hot word records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowHotWordsSwitch</td>
<td>This interface is used to query the hotwords function switch. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">InteractionRuleGroupManager</td>
<td>UpdateInteractionRuleGroup</td>
<td>This interface is used to update the smart live broadcast room interaction rule library. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateInteractionRuleGroup</td>
<td>This interface is used to create the smart live broadcast room interaction rule library. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListInteractionRuleGroups</td>
<td>This interface is used to list the interaction rule library for the smart live broadcast room. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteInteractionRuleGroup</td>
<td>This interface is used to delete the interaction rule library for the smart live broadcast room. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">KnowledgeIntentManagement</td>
<td>DeleteKnowledgeIntent</td>
<td>This interface is used to delete a knowledge base intent. For detailed interface usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateKnowledgeIntent</td>
<td>This API is used to create a knowledge base intent. An intent contains a topic, an answer, and several questions. For details about API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateKnowledgeIntent</td>
<td>This API is used to modify a knowledge base intent. For details about API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowKnowledgeIntent</td>
<td>This API is used to query knowledge base intent details. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListKnowledgeIntent</td>
<td>This API is used to query the knowledge base intent list. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml).io_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateIntentAndQuestion</td>
<td>This API is used to create knowledge base intents and questions. An intent contains a topic, an answer, and several questions. For details about API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">KnowledgeQuestionManagement</td>
<td>UpdateKnowledgeQuestion</td>
<td>This API is used to modify knowledge base questions. For details about API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowKnowledgeQuestion</td>
<td>This API is used to query knowledge base question details. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateBatchKnowledgeQuestion</td>
<td>This API is used to batch create knowledge base questions. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateBatchKnowledgeQuestion</td>
<td>This API is used to batch modify knowledge base questions. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteKnowledgeQuestion</td>
<td>This API is used to delete a knowledge base question. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListKnowledgeQuestion</td>
<td>This API is used to query the knowledge base question list. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateKnowledgeQuestion</td>
<td>This API is used to create a knowledge base question. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">KnowledgeSkillManagement</td>
<td>UpdateKnowledgeSkill</td>
<td>This API is used to modify knowledge base skills. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteKnowledgeSkill</td>
<td>This API is used to delete knowledge base skills. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListKnowledgeSkill</td>
<td>This API is used to query the knowledge base skill list. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowKnowledgeSkill</td>
<td>This API is used to query knowledge base skill details. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateKnowledgeSkill</td>
<td>This API is used to create a knowledge base skill. A skill is used for interactive question-and-answer sessions in a specific scenario and contains several intents. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExportKnowledgeSkill</td>
<td>This API is used to export knowledge base skills. For details on API usage restrictions, see [API Usage Restrictions](metastudio_02_0000.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">LivePlatformManage</td>
<td>CreateLivePlatform</td>
<td>This API is used to create a third-party live streaming platform. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLivePlatform</td>
<td>This API is used to delete third-party live streaming platform information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateLivePlatform</td>
<td>This interface is used to update third-party live streaming platform information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLivePlatforms</td>
<td>This interface is used to query the list of live streaming platforms. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowLivePlatform</td>
<td>This interface is used to query third-party live streaming platform information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLivePlatformProducts</td>
<td>This interface is used to query the product list of third-party live streaming platforms. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">OnceCodeManagement</td>
<td>CreateOnceCode</td>
<td>This interface is used to create a one-time authentication code, valid for 5 minutes. The authentication code can only be used once and needs to be obtained again after each use. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">OrderInterface</td>
<td>CreateMetaStudioOrders</td>
<td>This interface is used to order MetaStudio service packages, one-time packages, and on-demand packages.</td><td>To be tested</td>
</tr>
<tr>
<td rowspan="11">PacifyWordsManagement</td>
<td>DeletePacifyWords</td>
<td>This interface is used to delete appeasement words. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePacifyWords</td>
<td>This interface is used to modify appeasement words. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPacifyWordsIntent</td>
<td>This interface is used to query appeasement word intents. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeletePacifyWords</td>
<td>This interface is used to delete appeasement words in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePacifyWords</td>
<td>This interface is used to create a pacify word. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPacifyWords</td>
<td>This interface is used to query the pacify word list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPacifyWordsTriggerTime</td>
<td>This interface is used to query the trigger wait time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPacifyWords</td>
<td>This interface is used to query pacify word details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePacifyWordsTriggerTime</td>
<td>This API is used to modify the waiting time for the soothing words trigger. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPacifyWordsSwitch</td>
<td>This API is used to query the soothing words function switch. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePacifyWordsSwitch</td>
<td>This API is used to modify the soothing words function switch. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">PictureModeling</td>
<td>CreatePictureModelingByUrlJob</td>
<td>This API is used to retrieve an image from a URL for a photo modeling task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePictureModelingJob</td>
<td>This API is used to create a stylized photo modeling task. Generate a stylized digital human model by uploading a photo. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPictureModelingJob</td>
<td>This API is used to query the details of a stylized photo modeling task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPictureModelingJobs</td>
<td>This interface is used to query the list of stylized photo modeling jobs. </td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td rowspan="6">ProductManager</td> 
<td>ListProducts</td> 
<td>Query product list</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>SetProductAsset</td> 
<td>Commodity asset portfolio allocation</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>CreateProduct</td> 
<td>Create product</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>DeleteProduct</td> 
<td>Delete product</td> 
<td>To be tested</td> 
</tr> 
<tr> 
<td>ShowProduct</td> 
<td>Show product</td> <td>To be tested</td>
</tr>
<tr>
<td>UpdateProduct</td>
<td>Update product</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">RobotManagement</td>
<td>ShowRobot</td>
<td>This interface is used to query application details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRobot</td>
<td>This interface is used to create an application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ValidateRobot</td>
<td>This interface is used to validate an application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRobot</td>
<td>This interface is used to delete an application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRobot</td>
<td>This interface is used to query the application list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRobot</td>
<td>This interface is used to modify an application. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">SmartChatRoomManager</td>
<td>CreateSmartChatRoom</td>
<td>This interface is used to create a smart interaction conversation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSmartChatRoom</td>
<td>This interface is used to delete a smart interaction conversation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSmartChatRoom</td>
<td>This interface is used to query smart interaction conversation details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSmartChatRooms</td>
<td>This interface is used to list smart interaction conversations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSmartChatRoom</td>
<td>This interface is used to update smart chat room information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">SmartLiveJobManager</td>
<td>ListSmartLiveJobs</td>
<td>This interface is used to query the list of all digital human smart live broadcast tasks for a tenant. </td>
<td>To be tested</td>
</tr>
<tr>
<td>LiveEventReport</td>
<td>This interface is used to report live broadcast room events. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteSmartLiveCommand</td>
<td>This interface is used to control the digital human live broadcast process. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopSmartLive</td>
<td>This interface is used to end the digital human smart live broadcast task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSmartLive</td>
<td>This interface is used to query the live broadcast task list of a specific smart live broadcast room. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSmartLive</td>
<td>This interface is used to query the details of the digital human smart live broadcast task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartSmartLive</td>
<td>This interface is used to start the digital human smart live broadcast task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">SmartLiveRoomManager</td>
<td>UpdateSmartLiveRoom</td>
<td>This interface is used to retrieve smart live room information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSmartLiveRooms</td>
<td>This interface is used to list smart live rooms. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSmartLiveRoom</td>
<td>This interface is used to delete a smart live room. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSmartLiveRoom</td>
<td>This interface is used to query smart live room script details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSmartLiveRoom</td>
<td>This API is used to create a smart live room. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">StyleManager</td>
<td>ListStyles</td>
<td>Query the digital human style list</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">SubtitleFileManager</td>
<td>ShowSubtitleFile</td>
<td>This API is used to query the subtitle file task details for the digital human video. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSubtitleFile</td>
<td>This interface is used to create a subtitle file for a digital human video. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">TTSA</td>
<td>ListTtsaJobs</td>
<td>This interface is used to query the list of tasks that drive the digital human's expressions, actions, and voice. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTtsaData</td>
<td>This interface is used to obtain the generated digital human driving data, including voice, expressions, actions, etc. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTtsa</td>
<td>This interface is used to create tasks that drive digital human expressions, movements, and voices. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateFacialAnimations</td>
<td>This interface is used to create tasks that drive digital human expressions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListFacialAnimationsData</td>
<td>This interface is used to obtain generated digital human expression driving data. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">TenantManager</td>
<td>ListTenantResources</td><td>View the tenant resource list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CountTenantResources</td>
<td>Count the number of periodic and one-time resources that are about to expire within the specified time period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowResourceUsage</td>
<td>Query tenant one-time and periodic (yearly/monthly) resource usage information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="14">TrainingJobManager</td>
<td>ShowTenantDurationCfg</td>
<td>Query the user-configured personalized audio duration</td>
<td>To be tested</td>
</tr>
<tr>
<td>CommitVoiceTrainingJob</td>
<td>Submit the training job. After executing this API, the job will enter the review state and will wait for training after the review is complete. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowVoiceTrainingJob</td>
<td>Query voice training task details</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetJobBatchName</td>
<td>User sets task batches. This API is used for batch task management scenarios. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTrainingAdvanceJob</td>
<td>User creates a voice training advanced version task. This API returns an OBS upload URL for uploading voice files. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTrainingBasicJob</td>
<td>This task creates a basic voice training job. This API returns an OBS upload URL for uploading voice files. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTrainingMiddleJob</td>
<td>This task creates an advanced voice training job. This API returns an OBS upload URL for uploading voice files. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowJobAuditResult</td>
<td>Get the audit results of the voice training job. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ConfirmTrainingSegment</td>
<td>Confirm the online recording result. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTrainingSegmentInfo</td>
<td>Get the online recording confirmation result. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteVoiceTrainingJob</td>
<td>Delete voice training task</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowJobUploadingAddress</td>
<td>Get the voice file upload address</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListVoiceTrainingJob</td>
<td>Query the voice training task list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListJobOperationLog</td>
<td>Query the task operation log</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">TrainingJobManage</td>
<td>Delete2dModelTrainingJob</td>
<td>This interface is used to delete an avatar digital human model training task. The training video, ID photo, authorization documents, model assets, etc. associated with the training task must also be deleted. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Update2dModelTrainingJob</td>
<td>This interface is used to update an avatar digital human model training task. This is used to update the training video, ID photo, etc. if the task fails automatic or manual review. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Show2dModelTrainingJob</td>
<td>This interface is used to query the details of an avatar digital human model training task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Execute2dModelTrainingCommandByUser</td>
<td>This interface is used by tenants to execute avatar digital human model training task commands, such as submitting training for review. </td>
<td>To be tested</td>
</tr>
<tr>
<td>List2dModelTrainingJob</td>
<td>This interface is used to query the list of avatar digital human model training tasks. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Create2dModelTrainingJob</td>
<td>This interface is used to create an avatar digital human model training task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Ttsc</td>
<td>ShowAsyncTtsJob</td>
<td>This interface is used to obtain the TTS audio file download link. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveTtscVocabularyConfigs</td>
<td>This interface is used to modify TTS tenant-level custom pronunciation configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTtscVocabularyConfigs</td>
<td>This interface is used to set TTS tenant-level custom pronunciation configuration. </td>
<td>To be tested</td></tr>
<tr>
<td>CreateTtsAudition</td>
<td>This API is used to create a task that generates a voice audition file for the announcement. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTtscVocabularyConfigs</td>
<td>This API is used to obtain TTS tenant-level custom pronunciation configurations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTtsAuditionFile</td>
<td>This API is used to obtain a download link for a TTS audition file. The returned list contains the currently generated audition files. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTtsPhoneticSymbol</td>
<td>Returns a list of phonetic symbols corresponding to an English word</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTtscVocabularyConfigs</td>
<td>This interface is used to delete TTS tenant-level custom pronunciation configurations. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAsyncTtsJob</td>
<td>This interface is used to generate audio files externally. For details on the billing standards for each preset tone, see [Preset Tone Billing Standards](metastudio_02_0060.xml). </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">VideoMotionCapture</td>
<td>CreateVideoMotionCaptureJob</td>
<td>This interface is used to create a video driver task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ExecuteVideoMotionCaptureCommand</td>
<td>This interface is used to control the digital human driver. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopVideoMotionCaptureJob</td>
<td>This interface is used to stop the video driver task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowVideoMotionCaptureJob</td>
<td>This interface is used to query the video driver task details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListVideoMotionCaptureJobs</td>
<td>This interface is used to query the video driver task list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">VideoScriptManager</td>
<td>UpdateVideoScript</td>
<td>This interface is used to update the video production script. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CopyVideoScripts</td>
<td>This interface is used to copy the video production script. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteVideoScript</td>
<td>This interface is used to delete a video script. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowVideoScript</td>
<td>This interface is used to query video script details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateVideoScripts</td>
<td>This interface is used to create a video script. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListVideoScripts</td>
<td>This interface is used to query a list of video scripts. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">WelcomeSpeechManagement</td>
<td>ShowWelcomeSpeech</td>
<td>This interface is used to query the details of the welcome speech. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListWelcomeSpeech</td>
<td>This interface is used to query the list of welcome speeches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWelcomeSpeech</td>
<td>This interface is used to delete a welcome speech. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWelcomeSpeech</td>
<td>This interface is used to create a welcome speech. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWelcomeSpeechSwitch</td>
<td>This interface is used to query the welcome speech function switch. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWelcomeSpeech</td>
<td>This interface is used to modify the welcome speech function switch. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateWelcomeSpeechSwitch</td>
<td>This interface is used to modify the welcome speech function switch. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>