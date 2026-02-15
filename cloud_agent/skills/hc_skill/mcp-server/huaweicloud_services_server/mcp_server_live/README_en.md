# Live MCP Server 


## Version
v0.1.0

## Overview

Live MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Live. Full-chain management of Live resources can be carried out based on natural language.

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
<td rowspan="15">DataStatisticsAnalysis</td> 
<td>ListDomainTrafficSummary</td> <td>Query the traffic volume within a specified time range. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListQueryHttpCode</td>
<td>Query the HTTP status code for live streaming. Obtain the HTTP return code for the acceleration domain name with 1-minute granularity. The maximum query span cannot exceed 24 hours, and the maximum query period is 7 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListPlayDomainStreamInfo</td>
<td>Query the monitoring data for the playback domain name. Based on the input time point, the bandwidth, number of users, and protocol of all streams at that time are returned. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRecordData</td>
<td>Query the maximum number of concurrent recordings per hour for the live streaming tenant. Calculate the total number of concurrent channels per minute within an hour and take the maximum value as the statistical value. The maximum query span is 31 days, and the maximum query period is 90 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSnapshotData</td>
<td>Query the number of snapshots taken per hour for a live domain. The maximum query span is 31 days, and the maximum query period is 90 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDomainTrafficDetail</td>
<td>Query traffic data for a live domain. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDomainBandwidthPeak</td>
<td>Query the peak bandwidth for live streaming within the specified time range. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListTranscodeData</td>
<td>Query the hourly transcoding duration data for a live domain. The maximum query span is 31 days, and the maximum query period is 90 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListAreaDetail</td>
<td>Query detailed data for a live domain in a global region. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHistoryStreams</td>
<td>Query the historical streaming list. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListBandwidthDetail</td>
<td>Query the bandwidth data for a live domain. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUsersOfStream</td>
<td>Query viewer trends. Maximum query span is 31 days, maximum query period is 1 year. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowUpBandwidth</td>
<td>Query uplink bandwidth data. Maximum query span is 31 days, maximum query period is 1 year. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStreamCount</td>
<td>Query the number of streaming channels per domain name. Maximum query span is 31 days, maximum query period is 1 year. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowStreamPortrait</td>
<td>Query playback portrait information. The maximum query span is 1 day, and the maximum query period is 31 days. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">HTTPS Certificate Management</td>
<td>DeleteDomainHttpsCert</td>
<td>Delete the HTTPS certificate configuration for the specified domain name</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDomainHttpsCert</td>
<td>Query the HTTPS certificate configuration for the specified domain name</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDomainHttpsCert</td>
<td>Modify the HTTPS certificate configuration for the specified domain name</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">OBS Bucket Management</td>
<td>UpdateObsBucketAuthorityPublic</td>
<td>OBS Bucket Authorization and Deauthorization</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="10">OTT Channel Management</td>
<td>ListOttChannelInfo</td>
<td>Query channel information, supports batch query. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyOttChannelInfoEndPoints</td>
<td>Modify channel packaging information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyOttChannelInfoGeneral</td><td>Modify general channel information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyOttChannelInfoStats</td>
<td>Modify channel status. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyOttChannelInfoInput</td>
<td>Modify channel input information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyOttChannelInfoEncoderSettings</td>
<td>Modify channel transcoding template information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyOttChannelInfoRecordSettings</td>
<td>Modify channel recording information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteOttChannelInfo</td>
<td>Delete channel information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateOttChannelInfo</td>
<td>Channel creation interface, supports creating OTT channels. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowChannelStatistic</td>
<td>Query channel statistics (incoming stream scte35 signal)</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">StreamMonitor</td>
<td>ListSingleStreamFramerate</td>
<td>Query the push stream frame rate data interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSingleStreamBitrate</td>
<td>Query the push stream monitoring bitrate data interface. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListUpStreamDetail</td>
<td>Query the CDN upstream push stream quality data. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSingleStreamDetail</td>
<td>Query the stream monitoring data interface, including frame rate, bitrate, and interruption status. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="14">Domain Management</td>
<td>UpdateDelayConfig</td>
<td>Modify the playback delay configuration of the domain name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateHlsConfig</td>
<td>Modify the domain name HLS configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDomain</td>
<td>Delete a domain name. This can only be deleted when the domain is in the disabled (off) state. </td>
<td>To be tested</td>
</tr>
<tr>
<td>BatchShowIpBelongs</td>
<td>Query IP ownership information. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDomainMapping</td>
<td>Establish a domain name mapping relationship between the user-created playback domain name and the streaming domain name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateDomain</td>
<td>You can create a live broadcast domain name or a streaming domain name separately. Each tenant can configure up to 64 domain name records. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDomainMapping</td>
<td>Delete the domain name mapping between the playback domain name and the streaming domain name.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDomainIp6Switch</td>
<td>Configure the IPV6 switch.</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDomain</td>
<td>Modify domain name information related to live streaming and RTMP streaming acceleration.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListHlsConfig</td>
<td>Query the domain name HLS configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePullSourcesConfig</td>
<td>Modify the live stream pull source configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListDelayConfig</td>
<td>Query the playback domain delay configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDomain</td>
<td>Query the live stream domain name</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowPullSourcesConfig</td>
<td>Query the live stream pull source configuration. </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Recording callback management</td>
<td>ListRecordCallbackConfigs</td>
<td>Query the recording callback configuration list interface. Query the configuration list that meets the specified conditions by specifying the conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRecordCallbackConfig</td><td>Query recording callback configuration interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRecordCallbackConfig</td>
<td>Delete recording callback configuration interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRecordCallbackConfig</td>
<td>Modify recording callback configuration interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateRecordCallbackConfig</td>
<td>Create recording callback configuration interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="6">Recording management</td>
<td>CreateRecordRule</td>
<td>Create a recording rule interface. Recording rules take effect on newly pushed streams, but not on already pushed streams.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowRecordRule</td>
<td>Query recording rule interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateRecordRule</td>
<td>Modify recording rule interface. If a rule is modified, it will be invalid for currently recorded streams but valid for new streams.</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListRecordRules</td>
<td>Query recording rule list interface. Query a list of recording rules that meet specified conditions. </td>
<td>To be tested</td>
</tr>
<tr>
<td>RunRecord</td>
<td>Real-time recording control interface for a single stream. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRecordRule</td>
<td>Delete Recording Rule Interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Recording Index Management</td>
<td>CreateRecordIndex</td>
<td>Create Record Index</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Screenshot Management</td>
<td>CreateSnapshotConfig</td>
<td>Create Live Screenshot Configuration Interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateSnapshotConfig</td>
<td>Modify Live Screenshot Configuration Interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListSnapshotConfigs</td>
<td>Query live snapshot configuration interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteSnapshotConfig</td>
<td>Delete live snapshot configuration interface</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="1">Log management</td>
<td>ListLiveSampleLogs</td>
<td>Get live playback logs, packaged based on domain name with 5-minute granularity, and log content separated by "". </td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="5">Stream management</td>
<td>DeleteStreamForbidden</td>
<td>Restore live streaming interface</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateStreamForbidden</td>
<td>Forbid live streaming</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateStreamForbidden</td>
<td>Modify the banned stream attribute</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListStreamForbidden</td>
<td>Query the banned stream blacklist</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListLiveStreamsOnline</td>
<td>Query live stream information</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="7">Stream connection management</td>
<td>ListFlows</td>
<td>Get a flow list</td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyFlowSources</td>
<td>Modify flow sources</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateFlows</td>
<td>Create a flow</td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyFlowStop</td>
<td>Stop a flow task</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteFlow</td>
<td>Delete flow</td>
<td>To be tested</td>
</tr>
<tr>
<td>ModifyFlowStart</td>
<td>Start flow task</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowFlowDetail</td><td>Get Stream Details</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="4">Transcoding Template Management</td>
<td>UpdateTranscodingsTemplate</td>
<td>Modify Live Transcoding Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteTranscodingsTemplate</td>
<td>Delete Live Transcoding Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowTranscodingsTemplate</td>
<td>Query Live Transcoding Template</td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateTranscodingsTemplate</td>
<td>Create Live Transcoding Template</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="3">Notification Management</td>
<td>ListPublishTemplate</td>
<td>Query Live Stream Notification Configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>DeletePublishTemplate</td>
<td>Delete Live Stream Notification Configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdatePublishTemplate</td>
<td>Add or Overwrite Live Stream Notification Configuration</td>
<td>To be tested</td>
</tr>
<tr>
<td rowspan="11">Authentication Management</td>
<td>ShowRefererChain</td>
<td>Query Referer Hotlink Protection Blacklist and Whitelist</td>
<td>To be tested</td>
</tr>
<tr>
<td>ShowDomainKeyChain</td>
<td>Query the key hotlink protection configuration for the specified domain name</td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateDomainKeyChain</td>
<td>Update the key hotlink protection configuration for the specified domain name</td>
<td>To be tested</td>
</tr>
<tr>
<td>ListIpAuthList</td>
<td>Query the IP blacklist/whitelist for the streaming/playback domain name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteRefererChain</td>
<td>Delete the Referer hotlink protection blacklist and whitelist</td>
<td>To be tested</td>
</tr>
<tr>
<td>SetRefererChain</td>
<td>Set the referer blacklist and whitelist. The live streaming service will identify and filter visitors based on the configured referer blacklist and whitelist. Visitors who meet the requirements can access the content. If they do not meet the requirements, the access request will be denied. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateGeoBlockingConfig</td>
<td>Modify the regional restrictions for the playback domain name and select the region to allow access. </td>
<td>To be tested</td>
</tr>
<tr>
<td>DeleteDomainKeyChain</td>
<td>Delete the key hotlink protection configuration for the specified domain name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>ListGeoBlockingConfig</td>
<td>Query the regional restriction list for the playback domain name. </td>
<td>To be tested</td>
</tr>
<tr>
<td>CreateUrlAuthchain</td>
<td>Generate a URL authentication string. </td>
<td>To be tested</td>
</tr>
<tr>
<td>UpdateIpAuthList</td>
<td>Modify the IP blacklist/whitelist for the streaming/playback domain name. Currently only IPv4 is supported. </td> 
<td>To be tested</td> 
</tr> 
</tbody> 
</table> 
</body>
</html>