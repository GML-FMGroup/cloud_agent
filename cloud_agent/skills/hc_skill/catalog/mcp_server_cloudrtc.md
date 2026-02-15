# CloudRTC MCP Server 

## 版本信息
v0.1.0

## 产品描述

CloudRTC MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CloudRTC交互的能力。可以基于自然语言对CloudRTC资源进行全链路管理。

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
                    <td rowspan="3">OBS桶管理</td>
                    <td>UpdateObsBucketAuthority</td>
                    <td>OBS桶授权及取消授权</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObsBuckets</td>
                    <td>查询OBS桶列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListObsBucketObjects</td>
                    <td>查询OBS桶下对象列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">RtcStatisticsDataApi</td>
                    <td>ListRtcRealtimeScale</td>
                    <td>获取规模相关的指标在某一时间段内每分钟的统计数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcHistoryUsage</td>
                    <td>查询过去的某一时间段内各种业务的用量数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcUserList</td>
                    <td>指定事件范围查询这段期间加入房间的用户列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcRoomList</td>
                    <td>指定事件范围查询这段期间创建的房间列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcAbnormalEvents</td>
                    <td>查询指定APP下通话的异常明细数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcClientQosDetails</td>
                    <td>查询用户通话质量指标数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcHistoryScale</td>
                    <td>查询指标过去每天的规模数量,可查询最近31天的数据。当天未结束,无法查到当天的房间数与用户数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcAbnormalEventDimension</td>
                    <td>查询指定APP下指定时间内的通话异常明细数据分布情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcRealtimeNetwork</td>
                    <td>获取实时网络数据相关指标在某一时间段内每分钟的统计数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcRealtimeScaleDimension</td>
                    <td>对规模相关的数据,根据指定维度按在线用户数排名,获取规模相关的指标在指定维度下的统计数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcHistoryQuality</td>
                    <td>查询质量指标过去每天的体验数据,可查询最近31天的数据。当天未结束,无法查询到当天的体验数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcRealtimeQuality</td>
                    <td>获取实时质量数据的相关指标在某一时间段内每分钟的统计数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">单流任务管理</td>
                    <td>ShowIndividualStreamJob</td>
                    <td>调用此接口查询单流任务状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIndividualStreamJob</td>
                    <td>调用此接口接口启动单流任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateIndividualStreamJob</td>
                    <td>调用此接口修改单流任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopIndividualStreamJob</td>
                    <td>调用此接口停止单流任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">合流任务管理</td>
                    <td>CreateMixJob</td>
                    <td>调用此接口创建合流转码任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMixJob</td>
                    <td>调用此接口更新合流任务布局。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMixJob</td>
                    <td>调用此接口查询合流转码任务状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopMixJob</td>
                    <td>调用此接口停止已下发的合流转码任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">应用回调管理</td>
                    <td>ShowRecordCallback</td>
                    <td>调用此接口查询增值(录制)事件回调配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecordCallback</td>
                    <td>调用此接口配置增值(录制)事件上报回调。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">应用管理</td>
                    <td>StopApp</td>
                    <td>调用此接口停用单个应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApp</td>
                    <td>调用此接口创建应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListApps</td>
                    <td>调用此接口查询应用列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartApp</td>
                    <td>调用此接口启用单个应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowApp</td>
                    <td>调用此接口查询单个应用详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteApp</td>
                    <td>调用此接口删除单个应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">录制规则管理</td>
                    <td>UpdateRecordRule</td>
                    <td>调用此接口更新录制规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecordRule</td>
                    <td>调用此接口删除录制规则,对于正在使用的录制规则,不允许删除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecordRule</td>
                    <td>调用此接口创建或更新录制规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRecordRules</td>
                    <td>调用此接口查询录制规则列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordRule</td>
                    <td>调用此接口查询指定录制规则。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">房间管理</td>
                    <td>RemoveRoom</td>
                    <td>调用此接口解散房间,将该房间中所有用户踢出房间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveUsers</td>
                    <td>调用此接口强制用户离开房间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">数据统计分析</td>
                    <td>ListRtcEvent</td>
                    <td>查询指定APP下通话的异常明细数据。可查询5天内的数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRtcAbnormalEvent</td>
                    <td>查询指定APP下通话的异常明细数据。可查询5天内的数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">自动录制配置</td>
                    <td>ShowAutoRecord</td>
                    <td>调用此接口查询自动录制配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAutoRecord</td>
                    <td>更新自动录制配置,租户可以开启自动单流录制或者停用自动单流录制。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>