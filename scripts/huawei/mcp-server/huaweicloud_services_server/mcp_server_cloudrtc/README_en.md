# CloudRTC MCP Server


## Version
v0.1.0

## Overview

CloudRTC MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CloudRTC. Full-chain management of CloudRTC resources can be carried out based on natural language.

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
<td rowspan="3">OBS bucket management</td> 
<td>UpdateObsBucketAuthority</td> <td>OBS bucket authorization and deauthorization</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListObsBuckets</td>
<td>Query the OBS bucket list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListObsBucketObjects</td>
<td>Query the object list under the OBS bucket</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="12">RtcStatisticsDataApi</td>
<td>ListRtcRealtimeScale</td>
<td>Get minute-by-minute statistics for scale-related metrics within a specific time period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcHistoryUsage</td>
<td>Query usage data for various services within a certain period of time. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcUserList</td>
<td>Specify an event range to query a list of users who joined a room during that period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcRoomList</td>
<td>Specify an event range to query a list of rooms created during that period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcAbnormalEvents</td>
<td>Query abnormal call details for a specified app. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcClientQosDetails</td>
<td>Query user call quality indicator data. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcHistoryScale</td>
<td>Query the daily scale of the indicator. Data for the last 31 days is available. The number of rooms and users for the current day cannot be found until the end of the current day. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcAbnormalEventDimension</td>
<td>Query the distribution of call abnormality details for a specified app within a specified time period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcRealtimeNetwork</td>
<td>Get minute-by-minute statistics for real-time network metrics within a specified time period. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcRealtimeScaleDimension</td>
<td>Ranks scale-related data by the number of online users along a specified dimension, and gets statistics for scale-related metrics within that dimension. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcHistoryQuality</td>
<td>Query the daily experience data for quality metrics. Data for the last 31 days is available. Experience data for the current day cannot be retrieved if the current day has not yet ended. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcRealtimeQuality</td>
<td>Get minute-by-minute statistics of real-time quality data indicators within a specific time period. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Single-stream task management</td>
<td>ShowIndividualStreamJob</td>
<td>Call this interface to query the status of a single-stream task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateIndividualStreamJob</td>
<td>Call this interface to start a single-stream task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateIndividualStreamJob</td>
<td>Call this interface to modify a single-stream task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StopIndividualStreamJob</td>
<td>Call this interface to stop a single-stream task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Mixed Stream Task Management</td>
<td>CreateMixJob</td>
<td>Call this interface to create a mixed stream transcoding task. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateMixJob</td>
<td>Call this interface to update the mixed stream task layout. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowMixJob</td>
<td>Call this API to query the status of the mix transcoding task. </td>
<td>Tobe tested</td>
</tr>
<tr>
<td>StopMixJob</td>
<td>Call this interface to stop the issued confluence transcoding task. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Application callback management</td>
<td>ShowRecordCallback</td>
<td>Call this interface to query the callback configuration for value-added (recording) events. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRecordCallback</td>
<td>Call this interface to configure the callback for reporting value-added (recording) events. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Application Management</td>
<td>StopApp</td>
<td>Call this interface to stop a single application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateApp</td>
<td>Call this interface to create an application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListApps</td>
<td>Call this interface to query the application list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>StartApp</td>
<td>Call this interface to start a single application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowApp</td>
<td>Call this API to query the details of a single application. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteApp</td>
<td>Call this API to delete a single application. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Recording Rule Management</td>
<td>UpdateRecordRule</td>
<td>Call this API to update a recording rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRecordRule</td>
<td>Call this API to delete a recording rule. Deletion is not allowed for recording rules that are currently in use. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRecordRule</td>
<td>Call this API to create or update a recording rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRecordRules</td>
<td>Call this API to query the recording rule list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRecordRule</td>
<td>Call this API to query a specified recording rule. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Room Management</td>
<td>RemoveRoom</td>
<td>Call this API to disband a room and kick all users out. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RemoveUsers</td>
<td>Call this API to force a user to leave the room. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Data Statistics Analysis</td>
<td>ListRtcEvent</td>
<td>Query call exception details for the specified app. Data within the past 5 days can be queried. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRtcAbnormalEvent</td>
<td>Query call exception details for the specified app. Data within the past 5 days can be queried. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="2">Automatic recording configuration</td>
<td>ShowAutoRecord</td>
<td>Call this API to query the automatic recording configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateAutoRecord</td>
<td>Update the automatic recording configuration. Tenants can enable or disable automatic single-stream recording. </td>
<td>To be tested</td>
</tr>
</tbody>
</table>
</body>
</html>