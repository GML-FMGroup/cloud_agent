# Live MCP Server 

## 版本信息
v0.1.0

## 产品描述

Live MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务Live交互的能力。可以基于自然语言对Live资源进行全链路管理。

## 可用工具
覆盖全量API, 按需使用，列表以及状态如下：

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="15">DataStatisticsAnalysis</td>
                    <td>ListDomainTrafficSummary</td>
                    <td>查询指定时间范围内流量汇总量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryHttpCode</td>
                    <td>查询直播拉流HTTP状态码接口。 获取加速域名1分钟粒度的HTTP返回码 最大查询跨度不能超过24小时,最大查询周期7天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPlayDomainStreamInfo</td>
                    <td>查询播放域名下的监控数据,根据输入时间点,返回查询该时间点所有流的带宽、在线人数、协议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecordData</td>
                    <td>查询直播租户每小时录制的最大并发数,计算1小时内每分钟的并发总路数,取最大值做为统计值。 最大查询跨度31天,最大查询周期90天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotData</td>
                    <td>查询直播域名每小时的截图数量。 最大查询跨度31天,最大查询周期90天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainTrafficDetail</td>
                    <td>查询播放域名流量数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDomainBandwidthPeak</td>
                    <td>查询指定时间范围内播放带宽峰值。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTranscodeData</td>
                    <td>查询直播域名每小时的转码时长数据。 最大查询跨度31天,最大查询周期90天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAreaDetail</td>
                    <td>查询直播全球区域维度的详细数据接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistoryStreams</td>
                    <td>查询历史推流列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBandwidthDetail</td>
                    <td>查询播放域名带宽数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsersOfStream</td>
                    <td>查询观众趋势。 最大查询跨度31天,最大查询周期一年。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUpBandwidth</td>
                    <td>查询上行带宽数据。 最大查询跨度31天,最大查询周期1年。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStreamCount</td>
                    <td>查询域名维度推流路数接口。 最大查询跨度31天,最大查询周期1年。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStreamPortrait</td>
                    <td>查询播放画像信息。 最大查询跨度1天,最大查询周期31天。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">HTTPS证书管理</td>
                    <td>DeleteDomainHttpsCert</td>
                    <td>删除指定域名的https证书配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainHttpsCert</td>
                    <td>查询指定域名的https证书配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainHttpsCert</td>
                    <td>修改指定域名的https证书配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OBS桶管理</td>
                    <td>UpdateObsBucketAuthorityPublic</td>
                    <td>OBS桶授权及取消授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">OTT频道管理</td>
                    <td>ListOttChannelInfo</td>
                    <td>查询频道信息,支持批量查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyOttChannelInfoEndPoints</td>
                    <td>修改频道打包信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyOttChannelInfoGeneral</td>
                    <td>修改频道通用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyOttChannelInfoStats</td>
                    <td>修改频道状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyOttChannelInfoInput</td>
                    <td>修改频道入流信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyOttChannelInfoEncoderSettings</td>
                    <td>修改频道转码模板信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyOttChannelInfoRecordSettings</td>
                    <td>修改频道录制信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteOttChannelInfo</td>
                    <td>删除频道信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateOttChannelInfo</td>
                    <td>创建频道接口,支持创建OTT频道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowChannelStatistic</td>
                    <td>查询频道的统计信息(入流scte35信号)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">StreamMonitor</td>
                    <td>ListSingleStreamFramerate</td>
                    <td>查询推流帧率数据接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSingleStreamBitrate</td>
                    <td>查询推流监控码率数据接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUpStreamDetail</td>
                    <td>查询CDN上行推流质量数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSingleStreamDetail</td>
                    <td>查询流监控数据接口,包括帧率码率断流情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">域名管理</td>
                    <td>UpdateDelayConfig</td>
                    <td>修改播放域名延时配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHlsConfig</td>
                    <td>修改域名HLS配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomain</td>
                    <td>删除域名。只有在域名停用(off)状态时才能删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowIpBelongs</td>
                    <td>查询IP归属信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDomainMapping</td>
                    <td>将用户已创建的播放域名和推流域名建立域名映射关系</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDomain</td>
                    <td>可单独创建直播播放域名或推流域名,每个租户最多可配置64条域名记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomainMapping</td>
                    <td>将播放域名和推流域名的域名映射关系删除</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainIp6Switch</td>
                    <td>配置IPV6开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomain</td>
                    <td>修改直播播放、RTMP推流加速域名相关信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHlsConfig</td>
                    <td>查询域名HLS配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePullSourcesConfig</td>
                    <td>修改直播拉流回源配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDelayConfig</td>
                    <td>查询播放域名延时配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomain</td>
                    <td>查询直播域名</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPullSourcesConfig</td>
                    <td>查询直播拉流回源配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">录制回调管理</td>
                    <td>ListRecordCallbackConfigs</td>
                    <td>查询录制回调配置列表接口。通过指定条件,查询满足条件的配置列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordCallbackConfig</td>
                    <td>查询录制回调配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecordCallbackConfig</td>
                    <td>删除录制回调配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecordCallbackConfig</td>
                    <td>修改录制回调配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordCallbackConfig</td>
                    <td>创建录制回调配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">录制管理</td>
                    <td>CreateRecordRule</td>
                    <td>创建录制规则接口,录制规则对新推送的流生效,对已经推送中的流不生效</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordRule</td>
                    <td>查询录制规则接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecordRule</td>
                    <td>修改录制规则接口,如果规则修改后,修改后的规则对正在录制的流无效,对新的流有效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecordRules</td>
                    <td>查询录制规则列表接口,通过指定条件,查询满足条件的录制规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RunRecord</td>
                    <td>对单条流的实时录制控制接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecordRule</td>
                    <td>删除录制规则接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">录制索引管理</td>
                    <td>CreateRecordIndex</td>
                    <td>Create Record Index</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">截图管理</td>
                    <td>CreateSnapshotConfig</td>
                    <td>创建直播截图配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSnapshotConfig</td>
                    <td>修改直播截图配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSnapshotConfigs</td>
                    <td>查询直播截图配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSnapshotConfig</td>
                    <td>删除直播截图配置接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">日志管理</td>
                    <td>ListLiveSampleLogs</td>
                    <td>获取直播播放日志,基于域名以5分钟粒度进行打包,日志内容以 "" 进行分隔。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">流管理</td>
                    <td>DeleteStreamForbidden</td>
                    <td>恢复直播推流接口</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateStreamForbidden</td>
                    <td>禁止直播推流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStreamForbidden</td>
                    <td>修改禁推属性</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListStreamForbidden</td>
                    <td>查询禁播黑名单列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLiveStreamsOnline</td>
                    <td>查询直播中的流信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">流连接管理</td>
                    <td>ListFlows</td>
                    <td>获取流列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyFlowSources</td>
                    <td>修改流来源</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFlows</td>
                    <td>创建流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyFlowStop</td>
                    <td>停止流任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteFlow</td>
                    <td>删除流</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyFlowStart</td>
                    <td>启动流任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFlowDetail</td>
                    <td>获取流详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">转码模板管理</td>
                    <td>UpdateTranscodingsTemplate</td>
                    <td>修改直播转码模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTranscodingsTemplate</td>
                    <td>删除直播转码模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTranscodingsTemplate</td>
                    <td>查询直播转码模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTranscodingsTemplate</td>
                    <td>创建直播转码模板</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">通知管理</td>
                    <td>ListPublishTemplate</td>
                    <td>查询直播推流通知配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePublishTemplate</td>
                    <td>删除直播推流通知配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublishTemplate</td>
                    <td>新增、覆盖直播推流通知配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">鉴权管理</td>
                    <td>ShowRefererChain</td>
                    <td>查询Referer防盗链黑白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDomainKeyChain</td>
                    <td>查询指定域名的Key防盗链配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDomainKeyChain</td>
                    <td>更新指定域名的Key防盗链配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListIpAuthList</td>
                    <td>查询推流/播放域名的IP黑/白名单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRefererChain</td>
                    <td>删除Referer防盗链黑白名单</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRefererChain</td>
                    <td>设置Referer黑白名单,直播服务会根据配置的referer黑白名单,对访问者的身份进行识别和过滤,符合规则的可以顺利访问到该内容。如果不符合规则,该访问请求将会被禁止。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGeoBlockingConfig</td>
                    <td>修改播放域名的地域限制,选中地域允许接入。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDomainKeyChain</td>
                    <td>删除指定域名的Key防盗链配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGeoBlockingConfig</td>
                    <td>查询播放域名的地域限制列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUrlAuthchain</td>
                    <td>生成URL鉴权串</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIpAuthList</td>
                    <td>修改推流/播放域名的IP黑/白名单,当前仅支持ipv4。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>