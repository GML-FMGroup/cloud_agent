# KooMessage MCP Server


## Version
v0.1.0

## Overview

KooMessage MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service KooMessage. Full-chain management of KooMessage resources can be carried out based on natural language.

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
<td rowspan="2">AIMCallBack</td> 
<td>AddCallBack</td> <td>After creating a receipt interface as required, users can call this interface to register. Note: This interface is only available to users with the te_admin role. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAimCallbacks</td>
<td>After registering a receipt interface, users can use this interface to query all registered receipt interfaces. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">AIMResolveTask</td>
<td>ListResolveTasks</td>
<td>After creating a resolution task, users can query the resolution task status information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckMobileCapability</td>
<td>Before sending smart messages, users can use this interface to batch query the smart message resolution capabilities of corresponding mobile phones. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAimResolveDetails</td>
<td>Query personalized resolution details based on user-provided filtering conditions, including: sending task ID, sending mobile phone number, etc. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateResolveTask</td>
<td>Generate a short chain for resolution. A maximum of 100 short chains for resolution can be generated at a time. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">AIMSendTask</td>
<td>ListAimSendDetails</td>
<td>Query a list of sending details based on user-provided filtering conditions, including: sending task ID, sending mobile phone number, etc. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAimSendTask</td>
<td>Sends an intelligent message based on the customer's parameters, including the task name and intelligent message template ID. A maximum of 100 intelligent messages can be sent at a time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAimSendTasks</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAimSendReports</td>
<td>Query intelligent message sending reports. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">AIMTemplate</td>
<td>ListAimTemplates</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadAimTemplateMaterial</td>
<td>Supports users to upload images or videos for templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAimPersonalTemplate</td>
<td>Deletes the personal template for the smart message based on the template ID provided by the user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTemplateMaterial</td>
<td>Deletes the template material based on the template ID provided by the user. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetPrimaryVideoThumbnail</td>
<td>Sets the video template's cover image based on the user-provided video cover image resource ID and AIM video resource ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAimPersonalTemplate</td>
<td>Used for users to create personal templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAimTemplateMaterials</td>
<td>Query the template material list based on the user-provided filter criteria. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTemplateVideoThumbnail</td>
<td>Query the list of video template cover image resources based on the user-provided filter criteria. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAimTemplateReports</td>
<td>Query the number of times a specified smart information template has been parsed based on the user-specified filter criteria. Data for the current day will only be available after 4:00 PM the next day. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePersonalTemplateState</td>
<td>Enable or disable a personal smart information template based on the template ID provided by the user. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">AimSaMenu</td>
<td>ListMenus</td>
<td>Query the service number menu based on the filter conditions provided by the user. </td>
<td>To be tested</td></tr>
<tr>
<td>UpdateMenu</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">AimSaPort</td>
<td>ListPortInfos</td>
<td>Supports querying the channel number list and channel number binding information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RegisterPort</td>
<td>Register a channel number. </td>
<td>To be tested</td>
</tr>
<tr>
<td>LockPort</td>
<td>Bind a channel number to a service number. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePortInfo</td>
<td>Delete a channel number. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UnlockPort</td>
<td>Unbind the channel number from the service number. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">AimSaPortal</td>
<td>UpdatePortalInfo</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPortalInfos</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">AimSaPub</td>
<td>ListPubInfos</td>
<td></td>
<td>To be tested</td>
</tr>
<tr>
<td>UnfreezePub</td>
<td>Unfreeze the service account. This requires review and will take effect upon approval. </td>
<td>To be tested</td>
</tr>
<tr>
<td>FreezePub</td>
<td>Supports users to freeze service accounts through this API. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePubInfo</td>
<td>Supports users to update service account information. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">AimSaPubUnify</td>
<td>PushPortalInfo</td>
<td>Supports users to request review based on a homepage ID through this API. A homepage can only be requested for review after its associated service account has been approved. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PushMenuInfo</td>
<td>This API allows users to request review based on a menu ID. A menu can only be requested after its associated service account has been approved. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreatePubInfo</td>
<td>One-stop service account creation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadMedia</td>
<td>Supports users to upload image resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">AimSmsApp</td>
<td>ListAimMsgApp</td>
<td>This API allows users to query created SMS apps. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAimMsgApp</td>
<td>This interface is used by users to modify SMS applications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateSmsApp</td>
<td>This interface is used by users to create SMS applications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAimMsgAppDetail</td>
<td>This interface is used by users to obtain details of created SMS applications. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">AimSmsSend</td>
<td>SendAimBatchMessages</td>
<td>Sends SMS messages with the same content to one or multiple users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendAimBatchDifferentMessages</td>
<td>This interface is used to send SMS messages with different content to different users. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">AimSmsSignature</td>
<td>ListAimMsgSignatureDetail</td>
<td>This interface is used to obtain the details of a created SMS signature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAimMsgSignature</td>
<td>This interface is used to update SMS signature information. Currently, it only supports revising SMS signatures that have failed review. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadAimMsgSignatureFile</td>
<td>This interface is used by users to upload the business license/authorization document required to create a SMS signature. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAimMsgSignatureFileInfo</td>
<td>This interface is used by users to query the business license/authorization document information uploaded when creating a SMS signature. </td>
<td>To be tested</td>
</tr>
<tr><td>ListAimMsgSignature</td>
<td>This interface is used to query created SMS signatures. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAimMsgSignature</td>
<td>This interface is used to delete created SMS signatures. Deleting an approved signature will also delete the corresponding channel number and all SMS templates associated with it. Please proceed with caution. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddAimMsgSignature</td>
<td>This interface is used to create SMS signatures. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">AimSmsTemplate</td>
<td>UpdateAimMsgTemplate</td>
<td>This interface is used to modify SMS template information. Currently, only SMS templates that have failed review can be modified. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAimMsgTemplate</td>
<td>This interface is used to create SMS templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAimMsgTemplateDetail</td>
<td>This interface is used to obtain the details of a created SMS template. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowAimMsgTemplateVariable</td>
<td>This interface is used to query SMS template variables. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAimMsgTemplate</td>
<td>This interface is used to query created SMS templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAimMsgTemplate</td>
<td>This interface is used to delete created SMS templates. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">VMSSendTask</td>
<td>AddVmsCallBack</td>
<td>After creating a Smart Messaging Basic version receipt interface as required, users can call this interface to register it. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListVmsSendTasks</td>
<td>Supports users to query the Smart Messaging Basic version task list based on filtering criteria, including sending task name, Smart Messaging Basic version template ID, etc. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListVmsCallbacks</td>
<td>Query all registered Smart Messaging Basic version receipt interfaces. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateVmsSendTask</td>
<td>Supports users to send Smart Message Basic tasks through this interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">VmsTemplate</td>
<td>ListVmsTemplateStatus</td>
<td>Query the Smart Message Basic template status list based on the user-provided filter criteria. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateVmsTemplate</td>
<td>Supports users to create Smart Message Basic templates through this interface. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>