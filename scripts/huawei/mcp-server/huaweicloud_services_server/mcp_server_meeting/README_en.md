# Meeting MCP Server

## Version Information
v0.1.0

## Product Description

The Meeting MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud Meeting. It enables full-link management of meeting resources using natural language processing.

## Available Tools
Covering the entire API, available as needed. The list and status are as follows:

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
<td rowspan="6">OpenQosMetrics</td>
<td>SearchQosHistoryMeetings</td>
<td>This API is used to query QoS alarms for historical meetings within the enterprise. Only Enterprise Administrators in Ultimate and Standard Editions have permission to query. Data within the last three months can be queried. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowQosThreshold</td>
<td>This API is used to query QoS alarm thresholds. Only enterprise administrators of Ultimate/Standard Edition have permission to query this information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchQosOnlineMeetings</td>
<td>This interface is used to query QoS alarms for ongoing meetings within the enterprise. Only enterprise administrators of Ultimate/Standard Edition have permission to query this information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchQosParticipantDetail</td>
<td>This interface is used to query QoS data for participants in online or historical meetings within the enterprise. Only enterprise administrators of Ultimate/Standard Edition have permission to query this information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchQosParticipants</td>
<td>This interface is used to query QoS alarms for participants in online or historical meetings within the enterprise. Only Enterprise Administrators of Ultimate/Standard Edition have permission to query this.

<td>To be tested</td>

<tr>
<tr>
<td>SetQosThreshold</td>
<td>This interface is used to set the QoS alarm threshold. Only Enterprise Administrators of Ultimate/Standard Edition have permission to set this threshold. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">OpenStatisticMetrics</td>
<td>SearchStatisticConferenceInfo</td>
<td>This interface is used to query the following information within the enterprise:</td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchStatisticConferenceParticipant</td>
<td>This interface is used to query the following information within the enterprise:</td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchStatisticResourceInfo</td>
<td>This interface is used to query the following information within the enterprise:</td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchStatisticUserInfo</td>
<td>This interface is used to query enterprise user data statistics:</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Cloud Conference Room Management</td>
<td>AssociateVmr</td>
<td>Enterprise administrators use this interface to assign cloud conference rooms to users, professional conference terminals (TE10, TE20, HUAWEI Board, HUAWEI Bar 500, and HUAWEI Box series), smart TVs, electronic whiteboards (SmartRooms), and IdeaHubs.</td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchCorpVmr</td>
<td>Enterprise administrators use this interface to query the enterprise's cloud conference rooms in a paged manner. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMemberVmr</td>
<td>After logging in, enterprise users can modify their assigned cloud conference rooms and personal conference IDs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchMemberVmr</td>
<td>Enterprise users use this interface to query their assigned cloud conference rooms and personal conference IDs. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DisassociateVmr</td>
<td>Enterprise administrators use this interface to reclaim cloud conference rooms. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCorpVmr</td>
<td>Enterprise administrators use this interface to delete their enterprise's cloud conference rooms. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Enterprise application management</td>
<td>UpdateAppId</td>
<td>Enterprise default administrator modifies enterprise applications</td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchSearchAppId</td>
<td>Enterprise default administrator queries enterprise applications by page</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAppId</td>
<td>Enterprise administrator deletes enterprise applications</td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetAppKey</td>
<td>Enterprise default administrator resets enterprise application appkey</td>
<td>To be tested</td>
</tr>
<tr>
<td>AddAppId</td>
<td>Enterprise default administrators add applications. After adding an application, the returned information is recorded. You can later obtain an accessToken by [Performing App ID Authentication](https://support.huaweicloud.com/api-meeting/meeting_21_0311.html)</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Enterprise Management</td><td>ShowCorpBasicInfo</td>
<td>Entity administrators use this interface to query enterprise registration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddCorp</td>
<td>Create an enterprise, assign default administrators, and allocate resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchCorp</td>
<td>SP administrators can search for enterprises using pagination. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCorp</td>
<td>Modify an enterprise. If any parameter is null or not present, the enterprise will not be modified. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCorp</td>
<td>Get an enterprise. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateCorpBasicInfo</td>
<td>Enterprise administrators use this interface to modify enterprise registration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowCorpResource</td>
<td>Enterprise administrators use this interface to query enterprise resources and business permissions, including querying used resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteCorp</td>
<td>Delete an enterprise. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchCorpResources</td>
<td>Enterprise administrators use this interface to query enterprise resource order lists based on conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Enterprise Administrator Management</td>
<td>ShowCorpAdmin</td>
<td>Use this interface to query enterprise administrators. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddCorpAdmin</td>
<td>Add enterprise default administrators. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchCorpAdmins</td>
<td>Use this interface to query enterprise administrators by page. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteCorpAdmins</td>
<td>Use this interface to delete enterprise administrators in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Enterprise-level conference event push settings</td>
<td>UpdateWebHookConfigStatus</td>
<td>This interface is used by administrators to change the subscription configuration status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWebHookConfig</td>
<td>This interface is used by administrators to query enterprise event subscription configuration information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWebHookConfig</td>
<td>This interface is used by administrators to delete configured event push settings. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetWebHookConfig</td>
<td>This interface is used by administrators to set enterprise-level conference event subscription configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Enterprise Resource Management</td>
<td>AddResource</td>
<td>Adds new resources to the enterprise. This interface also supports modification. With a resourceId, it checks whether the resource exists. If it exists, it is modified (see the modification interface for supported parameters). Otherwise, it is treated as a new resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchResourceOpRecord</td>
<td>The SP queries the enterprise's resource operation records based on conditions, supporting fuzzy searches based on resourceId. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchResource</td>
<td>The SP searches for enterprise resource items based on conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteResource</td>
<td>The enterprise deletes a resource item. After deleting a resource item, the total number of enterprise resources will automatically decrease. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSpResource</td>
<td>The SP administrator searches for all SP resources, including used resources. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateResource</td>
<td>The enterprise modifies the expiration time and deactivated status of a resource. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Enterprise Department Management</td>
<td>UpdateDepartment</td>
<td>Enterprise administrators use this interface to modify departments. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeptAndChildDept</td>
<td>Enterprise administrators use this interface to query a list of departments and their first-level sub-departments. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDepartment</td>
<td>Query department information by department code. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchDepartmentByName</td>
<td>Enterprise administrators use this interface to query all departments by name. </td><td>To be tested</td>
</tr>
<tr>
<td>DeleteDepartment</td>
<td>Enterprise administrators use this interface to delete departments. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDepartment</td>
<td>Enterprise administrators use this interface to add departments. Up to 10 levels of departments are supported, with each level supporting up to 100 sub-departments. The default maximum number of departments in an enterprise is 10,000. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="48">Conference Control</td>
<td>MuteMeeting</td>
<td>This interface is used to set the mute/unmute status of all participants (except the host) in the entire conference. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AllowClientRecord</td>
<td>This API is used to set whether to allow or disallow local recording (non-cloud recording) on the participant's client. </td>
<td>To be tested</td>
</tr>
<tr>
<td>InviteOperateVideo</td>
<td>This API is used to invite a specified participant to turn on or off their camera. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStartedConfConfig</td>
<td>This API is used to modify conference configuration, including whether conference sharing is locked and the range of allowed call-in. </td>
<td>To be tested</td>
</tr>
<tr>
<td>InviteWithPwd</td>
<td>This API is used to invite participants using a conference ID and password. This interface is typically used when the app knows the conference ID and guest password, obtains the SIP number of other endpoints by scanning a QR code, and then invites them to the conference. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMgmtSiteStatus</td>
<td>The endpoint queries the conference management status through the conference control. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchMoveToWaitingRoom</td>
<td>The host uses this interface to move users to the waiting room in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SwitchMode</td>
<td>This interface is used to switch the video display policy in a conference, including broadcast multi-screen, broadcast single-screen, and voice-activated multi-screen. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRecordInfo</td>
<td>Query a single conference recording file information</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetAttendeeLanChannel</td>
<td>The host uses this interface to set the language channel for certain attendees (including the host). </td>
<td>To be tested</td>
</tr>
<tr>
<td>SaveLayout</td>
<td>This interface is used to save a multi-screen layout. A saved multi-screen layout can only be used in the current conference and will be released after the conference ends. </td>
<td>To be tested</td>
</tr>
<tr>
<td>PauseConference</td>
<td>The host uses this interface to control pause/unpause. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteAttendees</td>
<td>This interface is used to delete attendees. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AllowGuestUnmute</td>
<td>This interface is used to set whether attendees can unmute themselves. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchHand</td>
<td>This interface is used to set the hand-raising/hand-lowering status of guests in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>InviteShare</td>
<td>This interface is used to invite/uninvite specific attendees to share their desktop. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Live</td>
<td>This interface is used to start or stop the live broadcast of the conference. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BroadcastParticipant</td>
<td>This interface is used to broadcast a specified participant. Only one participant can be broadcast at a time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowLayout</td>
<td>This interface is used to query the saved multi-screen layouts for the current conference. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetRole</td>
<td>This interface is used to set or release a moderator. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetMmrRecord</td>
<td>Usage scenario: Administrators or UC account chairpersons can use this interface to start/stop MMR conference recording. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RollcallParticipant</td>
<td>This interface is used to call a specific participant. Calling a participant's name will unmute all participants except the host, while uncalled participants will be muted. Only one participant can be called at a time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ProlongMeeting</td>
<td>This interface is used to extend the meeting time. By default, meetings are automatically extended. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Record</td>
<td>This interface is used to start or stop conference cloud recording. </td>
<td>To be tested</td>
</tr><tr>
<td>AllowAudienceJoin</td>
<td>The host uses this interface to control whether audience members are allowed to join the meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetInterpreterGroup</td>
<td>The host uses this interface to set an interpretation group. Each interpretation group supports two languages and multiple interpreters. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetMmrLive</td>
<td>Usage scenario: The meeting host can use this interface to start/stop Mmr conference live streaming. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RenameParticipant</td>
<td>Rename a participant. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetCustomMultiPicture</td>
<td>This interface is used to set the multi-screen mode in a meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AllowWaitingParticipant</td>
<td>This interface is used to allow participants in the waiting room to join the meeting. You can allow all participants or specify participants. </td>
<td>To be tested</td>
</tr>
<tr>
<td>MoveToWaitingRoom</td>
<td>This interface is used to move a specified participant from the meeting to the waiting room. </td>
<td>To be tested</td>
</tr>
<tr>
<td>InviteParticipant</td>
<td>This interface is used to invite participants to join the meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>MuteParticipant</td>
<td>This API is used to set the mute/unmute status of a specified participant. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetParticipantView</td>
<td>This API is used to select other participants using professional conference terminals (such as the TE series). </td>
<td>To be tested</td>
</tr>
<tr>
<td>LockMeeting</td>
<td>This API is used to lock or unlock a conference. After a conference is locked, new guests are not allowed to join the conference. Joining the conference using the host password/host link, or inviting guests by the host, is not affected by the lock. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRealTimeInfoOfMeeting</td>
<td>This interface is used to query the real-time information of an ongoing meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopMeeting</td>
<td>This interface is used to end an ongoing meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelBroadcast</td>
<td>This interface is used to cancel a broadcast, including canceling a broadcast of multiple screens, canceling a broadcast of a venue, and canceling a roll call of a venue. </td>
<td>To be tested</td>
</tr>
<tr>
<td>LockView</td>
<td>This interface is used to lock or unlock the video source of an online venue. Applicable only to professional conference terminals (such as the TE series). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResumeSimultaneousInterpretation</td>
<td>This interface allows the conference chair to start/stop simultaneous interpretation. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetHostView</td>
<td>This interface is used for host polling, host selection of multiple screens, and host selection of venues. Applicable only to scenarios where a professional conference terminal (such as the TE series) is the host. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWebSocketToken</td>
<td>This interface is used to obtain a temporary token for establishing a WebSocket connection for conference control. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateConfToken</td>
<td>This interface is used to obtain the conference control token for an ongoing conference (calling this interface for an unstarted conference will fail). The token is valid for half an hour. </td>
<td>To be tested</td>
</tr>
<tr>
<td>Hand</td>
<td>This interface is used to set the hand-raised/hand-lowered status of a specified participant. </td>
<td>To be tested</td>
</tr>
<tr>
<td>HangUp</td>
<td>This interface is used to hang up a participant in a call. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetCohost</td>
<td>This interface is used to set or release a co-host. Guests can only be set as co-hosts. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteLayout</td>
<td>This API is used to delete the saved multi-view layout for the current meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SetMultiPicture</td>
<td>Set the multi-view layout for the meeting. This API is deprecated. Please use the "[Set Custom Multi-View](https://support.huaweicloud.com/api-meeting/meeting_21_0418.html)" API. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="29">Conference Management</td>
<td>CreateAuthRandom</td>
<td>Returns a random number based on the conference ID and password authentication. If called from a mini-program, the enterprise must support mini-program functionality.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowConfOrg</td>
<td>The SP administrator queries the enterprise ID to which the conference belongs based on the conference ID.</td><td>To be tested</td>
</tr>
<tr>
<td>UpdateRecurringSubMeeting</td>
<td>This interface is used to modify a sub-meeting of a scheduled recurring meeting. Once the meeting has started, it cannot be modified. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckCallNumberInConf</td>
<td>Use this interface to check if a call number is in a meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelRecurringMeeting</td>
<td>This interface is used to cancel a recurring meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchRecordings</td>
<td>This interface is used to query the meeting recording list. Administrators can query all recordings within their enterprise, while regular users can only query recordings of meetings they created. Without query parameters, the default query is for recordings within the scope of permissions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRecordings</td>
<td>This interface is used to delete meeting recordings in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchAttendanceRecordsOfHisMeeting</td>
<td>This interface is used to query attendee records for a specified historical meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOrgRes</td>
<td>Entity administrators query resource usage information for their enterprise. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelRecurringSubMeeting</td>
<td>This interface is used to cancel a sub-meeting of a recurring meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRecordingFileDownloadUrls</td>
<td>This interface allows users to query the download links for a specified meeting recording file. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRecurringMeeting</td>
<td>This interface is used to modify a scheduled recurring meeting. A meeting cannot be modified after it has started. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMeeting</td>
<td>This interface is used to modify a scheduled meeting. After a meeting starts, it cannot be modified. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchCtlRecordsOfHisMeeting</td>
<td>This interface is used to query the meeting control records of a specified historical meeting. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRegionInfoOfMeeting</td>
<td>This interface is used to query the IP and domain name of the region where the meeting is located. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowOnlineMeetingDetail</td>
<td>This interface is used to query the details of an ongoing meeting. Administrators can query the details of all online meetings within the enterprise. Ordinary users can only query the details of online meetings created by their own account or that they need to attend. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchMeetings</td>
<td>This API is used to query for meetings that have not yet ended. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartMeeting</td>
<td>This API is used to activate a meeting using the meeting ID and password. All meeting control APIs must be called after the meeting is activated. You can use this API to activate the meeting first. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchHisMeetings</td>
<td>This API is used to query for meetings that have ended. Administrators can query all historical meetings within the enterprise, while ordinary users can only query historical meetings they created or were invited to. Without query parameters, the default query is for historical meetings within the scope of the permission. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAnonymousAuthRandom</td>
<td>This interface is used to authenticate anonymous users for conference entry. It requests authentication based on the conference ID and password and returns an authentication random number (which can be used to retrieve anonymous user information, conference information, etc.). </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRecordingDetail</td>
<td>This interface is used to query the details of a conference recording. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRecurringMeeting</td>
<td>This interface is used to schedule recurring meetings. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMeetingDetail</td>
<td>Query offset</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateMeeting</td>
<td>This API is used to create immediate and scheduled meetings. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchOnlineMeetings</td>
<td>This API is used to query the list of ongoing meetings. Administrators can query all online meetings within the enterprise, while regular users can only query online meetings created or required to be attended by their current account. Without query parameters, the default query is to query all online meetings within the authorized scope, sorted in ascending order by start time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSpRes</td>
<td>The SP administrator queries the shared resource usage information of the SP to which they belong. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOnlineConfAttendee</td>
<td>This interface is used to query the online attendee information of a specified conference. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowHisMeetingDetail
<td>This interface allows users to query the details of a specified historical meeting. Administrators can query the details of all historical meetings within the company, while ordinary users can only query the details of historical meetings they created or to which they were invited. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CancelMeeting</td>
<td>This interface is used to cancel a scheduled meeting. Company administrators can cancel meetings created by users within the company, while ordinary users can only cancel meetings they created themselves. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Meeting Minutes</td>
<td>ShowMeetingFileList</td>
<td>After the user scans the QR code with their phone, the phone requests the server, which instructs the specified IdeaHub to open the specified user's meeting minutes file list. QR code content: cloudlink://cloudlink.huawei.com/h5page?action=OPEN_MEETING_FILE_LIST&key1=value1&key2=value2. The number of key/value pairs may vary. After parsing, the terminal should save all key/value pairs as a map and use them as input parameters when initiating subsequent requests. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddToPersonalSpace</td>
<td>After the user scans the QR code with their phone, the phone requests the server to save the current meeting minutes file to their personal cloud space. QR code content: cloudlink://cloudlink.huawei.com/h5page?action=SAVE_MEETING_FILE&key1=value1&key2=value2. The number of key/value pairs may vary. After parsing, the terminal should save all key/value pairs as a map and use them as input parameters when initiating subsequent requests. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMeetingFile</td>
<td>Users query the details of a single meeting minute. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchMeetingFileList</td>
<td>Users query their own meeting minute list. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Information window publication management</td>
<td>ShowPublication</td>
<td>Get publication details based on ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePublication</td>
<td>Modify information window publication. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchPublications</td>
<td>Get information window publications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeletePublications</td>
<td>Delete information window publications. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddPublication</td>
<td>Add information window publications. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Information window material management</td>
<td>UpdateMaterial</td>
<td>Update information window material. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteMaterials</td>
<td>Delete information window materials. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddMaterial</td>
<td>Add information window materials (upload material files). </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchMaterials</td>
<td>Search information window materials by page. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Information window program management</td>
<td>AddProgram</td>
<td>Add information window program. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateProgram</td>
<td>Update the information window program. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowProgram</td>
<td>Get program details based on the ID. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeletePrograms</td>
<td>Delete the information window program. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchPrograms</td>
<td>Get the information window program. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Query the enterprise address book</td>
<td>SearchCorpExternalDir</td>
<td>Enterprise users (including administrators) use this interface to query the enterprise's external contacts or personal external contacts. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchCorpDir</td>
<td>Enterprise users (including administrators) use this interface to query the enterprise's address book. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Activation Code Management</td>
<td>ResetActivecode</td>
<td>When the hard terminal activation code expires, the enterprise administrator can reset the activation code through this interface and use the newly obtained activation code to activate the terminal. Reactivation is allowed up to five times every 24 hours. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteVisionActiveCode</td>
<td>Enterprise administrators can delete activation codes in batches. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchVisionActiveCode</td><td>Enterprise administrators can query activation codes by page, supporting fuzzy queries for activation codes and device names. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateVisionActiveCode</td>
<td>Enterprise administrators can generate activation codes for smart screens, electronic whiteboards (SmartRooms), and Ideahub. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetVisionActiveCode</td>
<td>Enterprise administrators can reset the activation code for an account. After resetting, the original device will be unbound and must be reactivated. If the mobile email address is not entered, a new activation code will not be sent. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">User profile image management</td>
<td>SetProfileImage</td>
<td>User profile image settings</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetUserProfileImage</td>
<td>Set profile images for users within the enterprise (only administrators can call this)</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">User password management</td>
<td>UpdatePwd</td>
<td>Enterprise members use this interface to provide user password modification functionality. The server receives the request, modifies the user's password, and returns the result. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendSlideVerifyCode</td>
<td>This API sends a slider verification code. Upon receiving the request, the server returns the cutout image and the original image after the cutout. The cutout image and the original image after the cutout need to be displayed on the front-end interface, and the user can use the slider to match the image. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckVerifyCode</td>
<td>This API checks the verification code. Upon receiving the request, the server returns the result. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetPwdByAdmin</td>
<td>Entity administrators use this API to reset the passwords of enterprise members. When the server receives a password reset request, it sends the new password to the enterprise member's email or SMS and returns the result. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendVeriCodeForChangePwd</td>
<td>This API allows you to send a verification code. Upon receiving the request, the server sends the verification code to an email address or SMS and returns the result. After the user completes the slider verification on the front-end interface, they can then send the verification code. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckSlideVerifyCode</td>
<td>This API allows you to verify the slider verification code. Upon receiving the request, the server returns the verification result. The user uses the slider to match the image on the front-end interface, ensuring that the cutout image matches the original image. The server then verifies the slider verification code. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ResetPwd</td>
<td>This API allows you to reset your password. Upon receiving the request, the server resets the user's password and returns the result. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="13">User Management</td>
<td>ShowMyInfo</td>
<td>Enterprise users use this interface to query their own information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SendVeriCodeForUpdateUserInfo</td>
<td>When modifying a user's phone number or email address, a verification code is required. Enterprise users use this interface to obtain a verification code, which the system will send to the user's phone number or email address. The verification code is valid for 1 minute. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMyInfo</td>
<td>Enterprise users use this interface to modify their own information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateContact</td>
<td>Enterprise users who modify their phone number or email address through this interface must first obtain a verification code. Repeated verification failures will result in the modification being prohibited. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckVeriCodeForUpdateUserInfo</td>
<td>Enterprise users use this interface to verify the verification code corresponding to their phone number and email address. The number of attempts recorded within a minute cannot exceed 5. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchUsers</td>
<td>Enterprise administrators use this interface to query enterprise users in a paged manner. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateUser</td>
<td>Enterprise administrators use this interface to modify enterprise users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowUserDetail</td>
<td>Enterprise administrators use this interface to query enterprise user details. </td>
<td>To be tested</td>
</tr>
<tr>
<td>InviteUser</td>
<td>Invite users to join the enterprise by phone number or email address. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateUserStatus</td>
<td>Enterprise administrators use this interface to modify user status in batches. When user account resources or electronic whiteboard (SmartRooms) resources expire, if the number of user accounts for the corresponding resources in the enterprise exceeds the limit, the system will automatically deactivate them. In this case, this interface can be used to modify user status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddUser</td>
<td>Enterprise administrators use this interface to add enterprise users. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchShowUserDetails</td>
<td>Batch query user details, supporting querying details using a specified third-party account. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteUsers</td>
<td>Enterprise administrators use this interface to delete enterprise users in batches. When deleting multiple users, all deletions succeed or all deletions fail. </td><td>To be tested</td>
</tr>
<tr>
<td rowspan="9">Login Authentication</td>
<td>SetSsoConfig</td>
<td>This interface is used to set the authentication configuration for SSO login. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CheckToken</td>
<td>This interface provides token validation. After receiving the request, the server verifies the token's validity and returns the result. If the parameter needGenNewToken is true, a new token is generated and returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateProxyToken</td>
<td>This interface uses a third-party account for proxy authentication. After authentication is successful, an Access Token is generated. Currently supported third-party proxy accounts include:

<td>To be tested</td>

<tr>
<td>CreateToken</td>
<td>This API uses the Huawei Cloud Meeting account and password for authentication. After authentication, an Access Token is generated.

<td>To be tested</td>

</tr>
<tr>
<td>CreatePortalRefNonce</td>
<td>Use the Access Token to generate the nonce information for redirecting to the Huawei Cloud Meeting portal without logging in. After obtaining the nonce information, use the link https://meeting.huaweicloud.com/?lang=zh-CN&nonce=xxxxxxxxxxxxx#/login to redirect without logging in. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateAppIdToken</td>
<td>This API uses App ID authentication. After authentication, an Access Token is generated. For an introduction to the principles of App ID authentication, please refer to [App ID Authentication Introduction](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html). </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteToken</td>
<td>This API provides logout functionality. After receiving the request, the server deletes the token. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowSsoConfig</td>
<td>This API is used to query the authentication configuration for SSO login. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateToken</td>
<td>This interface provides token refresh functionality. Based on the passed token, it refreshes the token expiration time and returns the result. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="8">Hard Terminal Management</td>
<td>UpdateDevice</td>
<td>Enterprise administrators use this interface to modify professional conference terminals. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchDeleteDevices</td>
<td>Enterprise administrators use this interface to batch delete professional conference terminals and return a list of failed deletions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeviceStatus</td>
<td>This API can be used to query the status of hard terminals. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchUpdateDevicesStatus</td>
<td>Enterprise administrators use this API to batch-update the status of professional conference terminals. When hard terminal resources expire, if the number of hard terminals within the enterprise exceeds the limit, the system will automatically deactivate them. In this case, this API can be used to modify the status of professional conference terminals. </td>
<td>To be tested</td>
</tr>
<tr>
<td>SearchDevices</td>
<td>Enterprise administrators use this API to query professional conference terminal information in pages. </td>
<td>To be tested</td>
</tr>
<tr>
<td>AddDevice</td>
<td>Enterprise administrators use this interface to add professional conference endpoints. Professional conference endpoints include the DP300/HUAWEI Bar series/HUAWEI Board/TE series. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeviceTypes</td>
<td>Enterprise administrators use this interface to obtain all professional conference endpoint types. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDeviceDetail</td>
<td>Enterprise administrators use this interface to query professional conference endpoint details. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">Webinar Management</td>
<td>ListUpComingWebinars</td>
<td>This API is used to query upcoming webinars. Administrators can query upcoming webinars within the company, while non-administrators can query upcoming webinars they have scheduled. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowWebinar</td>
<td>This API is used to query the details of a specified webinar. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteWebinar</td>
<td>This API is used to cancel a scheduled webinar. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHistoryWebinars</td>
<td>This interface is used to query historical webinars. Administrators can query historical webinars within the company, while non-administrators can query personal historical webinars. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListOngoingWebinars</td>
<td>This interface is used to query ongoing webinars. Administrators can query ongoing webinars within the company, while non-administrators can query ongoing webinars they have scheduled. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRoomSetting</td>
<td>This interface is used to set advanced settings for a specified webinar. Administrators can set advanced settings for company-wide webinars, while non-administrators can only set advanced settings for their own scheduled webinars. </td> 
<td>To be tested</td> 
</tr><tr>
<td>UpdateWebinar</td>
<td>This API is used to modify a created webinar. Modifications are not possible after the webinar has started. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRoomSetting</td>
<td>This API is used to query the advanced settings of a specified webinar. Administrators can query the advanced settings of webinars within their organization; non-administrators can only query the advanced settings of their own scheduled webinars. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UploadFile</td>
<td>This API allows users to upload images for advanced webinar settings. Images can be used for webinar cover art and logos. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateWebinar</td>
<td>This API is used to create a webinar. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Network quality</td>
<td>ListNetworkQuality</td>
<td>Query the venue network quality</td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>