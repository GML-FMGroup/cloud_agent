# Meeting MCP Server 

## 版本信息
v0.1.0

## 产品描述

Meeting MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务Meeting交互的能力。可以基于自然语言对Meeting资源进行全链路管理。

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
                    <td rowspan="6">OpenQosMetrics</td>
                    <td>SearchQosHistoryMeetings</td>
                    <td>该接口用于查询企业内历史会议的QoS告警。仅旗舰版企业/标准版企业的企业管理员有权限查询。可以查询最近3个月内的数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowQosThreshold</td>
                    <td>该接口用于查询QoS告警阈值。仅旗舰版企业/标准版企业的企业管理员有权限查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchQosOnlineMeetings</td>
                    <td>该接口用于查询企业内正在召开会议的QoS告警。仅旗舰版企业/标准版企业的企业管理员有权限查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchQosParticipantDetail</td>
                    <td>该接口用于查询企业内在线会议或历史会议的与会者QoS数据。仅旗舰版企业/标准版企业的企业管理员有权限查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchQosParticipants</td>
                    <td>该接口用于查询企业内在线会议或历史会议的与会者QoS告警。仅旗舰版企业/标准版企业的企业管理员有权限查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetQosThreshold</td>
                    <td>该接口用于设置QoS告警阈值。仅旗舰版企业/标准版企业的企业管理员有权限设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">OpenStatisticMetrics</td>
                    <td>SearchStatisticConferenceInfo</td>
                    <td>该接口用于查询企业内:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchStatisticConferenceParticipant</td>
                    <td>该接口用于查询企业内与会者数据统计:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchStatisticResourceInfo</td>
                    <td>该接口用于查询企业内已购资源使用状况数据统计:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchStatisticUserInfo</td>
                    <td>该接口用于查询企业内用户数据统计:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">云会议室管理</td>
                    <td>AssociateVmr</td>
                    <td>企业管理员通过该接口将云会议室分配给用户、专业会议终端(TE10、TE20、HUAWEI Board、HUAWEI Bar 500及HUAWEI Box系列)、智慧屏TV、电子白板(SmartRooms)、IdeaHub。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchCorpVmr</td>
                    <td>企业管理员通过该接口分页查询企业的云会议室。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMemberVmr</td>
                    <td>企业用户登录后可以修改分配给用户的云会议室及个人会议ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchMemberVmr</td>
                    <td>企业用户通过该接口查询个人已分配的云会议室及个人会议ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisassociateVmr</td>
                    <td>企业管理员通过该接口回收云会议室。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCorpVmr</td>
                    <td>企业管理员通过该接口删除企业的云会议室。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">企业应用管理</td>
                    <td>UpdateAppId</td>
                    <td>企业默认管理员修改企业应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchSearchAppId</td>
                    <td>企业默认管理员分页查询企业应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAppId</td>
                    <td>企业管理员删除企业应用</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetAppKey</td>
                    <td>企业默认管理员重置企业应用appkey</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAppId</td>
                    <td>企业默认管理员添加应用,添加应用后,记录返回信息,后续可通过[执行App ID鉴权](https://support.huaweicloud.com/api-meeting/meeting_21_0311.html) 获取accessToken</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">企业管理</td>
                    <td>ShowCorpBasicInfo</td>
                    <td>企业管理员通过该接口查询企业注册信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCorp</td>
                    <td>创建企业,默认管理员及分配资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchCorp</td>
                    <td>SP管理员分页搜索企业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCorp</td>
                    <td>修改企业,若任一参数为null或者不携带则不修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCorp</td>
                    <td>获取企业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateCorpBasicInfo</td>
                    <td>企业管理员通过该接口修改企业注册信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCorpResource</td>
                    <td>企业管理员通过该接口查询企业内资源及业务权限,包括查询已使用的资源情况。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteCorp</td>
                    <td>删除企业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchCorpResources</td>
                    <td>企业管理员根据条件查询企业资源订单列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">企业管理员管理</td>
                    <td>ShowCorpAdmin</td>
                    <td>通过该接口查询企业管理员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddCorpAdmin</td>
                    <td>企业默认管理员添加企业普通管理员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchCorpAdmins</td>
                    <td>通过该接口分页查询企业管理员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteCorpAdmins</td>
                    <td>通过该接口批量删除企业管理员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">企业级会议事件推送设置</td>
                    <td>UpdateWebHookConfigStatus</td>
                    <td>该接口用于管理员变更订阅配置使用状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWebHookConfig</td>
                    <td>该接口用于管理员查询企业事件订阅配置信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWebHookConfig</td>
                    <td>该接口用于管理员删除已配置的事件推送设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetWebHookConfig</td>
                    <td>该接口用于管理员设置企业级会议事件订阅配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">企业资源管理</td>
                    <td>AddResource</td>
                    <td>企业新增资源发放。该接口同时支持修改,带resourceId后会判断该资源是否存在,存在即修改(支持修改的参数见修改接口),否则按新增处理。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResourceOpRecord</td>
                    <td>SP根据根据条件查询企业的资源操作记录,支持根据resourceId模糊搜索。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchResource</td>
                    <td>SP根据条件查询企业的资源项。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteResource</td>
                    <td>企业删除资源项,删除资源项后,企业资源总数会自动减少。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSpResource</td>
                    <td>SP管理员查询SP的所有资源,包括已使用的资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateResource</td>
                    <td>企业修改资源的过期时间、停用状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">企业部门管理</td>
                    <td>UpdateDepartment</td>
                    <td>企业管理员通过该接口修改部门。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeptAndChildDept</td>
                    <td>企业管理员通过该接口查询部门及其一级子部门列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDepartment</td>
                    <td>通过部门编码查询部门信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchDepartmentByName</td>
                    <td>企业管理员通过该接口按名称查询所有的部门。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDepartment</td>
                    <td>企业管理员通过该接口删除部门。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDepartment</td>
                    <td>企业管理员通过该接口添加部门,最多支持10级部门,每级子部门最多支持100个,默认企业最大部门数量为10000个。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="48">会议控制</td>
                    <td>MuteMeeting</td>
                    <td>该接口用于设置整个会议所有与会者(主持人除外)的静音/取消静音状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowClientRecord</td>
                    <td>该接口用于设置允许/禁止与会者客户端本地录制(非云端录制)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InviteOperateVideo</td>
                    <td>该接口用于邀请指定与会者开启、关闭摄像头。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateStartedConfConfig</td>
                    <td>该接口用于修改会议配置,包括会议共享是否锁定,允许呼入范围。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InviteWithPwd</td>
                    <td>该接口用于通过会议ID和密码邀请与会者。一般用于App已知会议ID和来宾密码,通过扫码等方式获取其他终端的SIP号码后,使用该接口将其他终端邀请加入会议中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMgmtSiteStatus</td>
                    <td>终端通过会控查询会管状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchMoveToWaitingRoom</td>
                    <td>主持人通过该接口批量移动用户到等候室。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SwitchMode</td>
                    <td>该接口用于切换会中视频画面显示策略,包括广播多画面,广播单画面,声控多画面。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordInfo</td>
                    <td>查询单会议录制文件信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetAttendeeLanChannel</td>
                    <td>主持人通过该接口设置某些普通与会者(包括主持人)加入哪个语言频道。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveLayout</td>
                    <td>该接口用于保存多画面布局。保存的多画面布局,只能在当前会议使用,会议结束后,保存的多画面布局就会释放。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PauseConference</td>
                    <td>主持人通过接口控制暂停/取消暂停。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAttendees</td>
                    <td>该接口用于删除与会者。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowGuestUnmute</td>
                    <td>该接口用于设置与会者是否可以自己解除静音。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchHand</td>
                    <td>该接口用于批量设置来宾的举手/放下举手状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InviteShare</td>
                    <td>该接口用于邀请/取消邀请指定与会人共享桌面。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Live</td>
                    <td>该接口用于启动或停止会议直播。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BroadcastParticipant</td>
                    <td>该接口用于广播指定的与会者。同一时间,只允许一个与会者被广播。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLayout</td>
                    <td>该接口用于查询当前会议已保存的多画面布局。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetRole</td>
                    <td>该接口用于设置主持人或释放主持人。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetMmrRecord</td>
                    <td>使用场景:管理员或UC账号主席可以通过该接口启动/停止mmr会议录制</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RollcallParticipant</td>
                    <td>该接口用于点名指定与会者。点名会场的效果是除了主持人外,点名与会者为非静音状态,未点名的与会者统一为静音状态。同一时间,只允许一个与会者被点名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ProlongMeeting</td>
                    <td>该接口用于延长会议时间。默认会议自动延长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Record</td>
                    <td>该接口用于启动或停止会议云录制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowAudienceJoin</td>
                    <td>主持人通过接口控制是否允许观众入会。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetInterpreterGroup</td>
                    <td>主持人通过该接口设置传译组,每个传译组支持两种语言,传译组内支持多个传译员。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetMmrLive</td>
                    <td>使用场景:会议主持人可以通过该接口启动/停止Mmr会议直播</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RenameParticipant</td>
                    <td>重命名某个与会者。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetCustomMultiPicture</td>
                    <td>该接口用于设置会中多画面。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AllowWaitingParticipant</td>
                    <td>该接口用于允许等候室中的成员进入会议。可以允许全部成员进入会议,或者允许指定成员进入会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MoveToWaitingRoom</td>
                    <td>该接口用于将会中的指定与会者移入到等候室。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InviteParticipant</td>
                    <td>该接口用于邀请与会者加入会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>MuteParticipant</td>
                    <td>该接口用于设置指定与会者静音/取消静音状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetParticipantView</td>
                    <td>该接口用于专业会议终端(如TE系列等)选看其他与会者。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LockMeeting</td>
                    <td>该接口用于锁定或解锁会议。锁定会议后,不允许新的来宾主动加入会议。会议锁定后使用主持人密码/主持人链接加入会议或者主持人邀请来宾不受影响。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRealTimeInfoOfMeeting</td>
                    <td>该接口用于查询正在召开的会议实时信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopMeeting</td>
                    <td>该接口用于结束正在召开的会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelBroadcast</td>
                    <td>该接口用于取消广播,包括:取消广播多画面,取消广播会场,取消点名会场。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LockView</td>
                    <td>该接口用于锁定或者解锁某在线会场的视频源。只适用于专业会议终端(如TE系列等)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResumeSimultaneousInterpretation</td>
                    <td>该接口用于会议主席可以通过该接口开启/关闭同声传译。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetHostView</td>
                    <td>该接口用于主持人轮询、主持人选看多画面、主持人选看会场操作。只适用于专业会议终端(如TE系列等)为主持人的场景。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWebSocketToken</td>
                    <td>该接口用于获取会控WebSocket建链的临时Token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateConfToken</td>
                    <td>该接口用于获取正在召开会议的会控Token(未开始的会议调用该接口返回失败)。Token有效期是半个小时。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Hand</td>
                    <td>该接口用于设置指定与会者的举手/放下举手状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>HangUp</td>
                    <td>该接口用于挂断正在通话中的与会者。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetCohost</td>
                    <td>该接口用于设置联席主持人或释放联席主持人。只能将来宾设置为联席主持人。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLayout</td>
                    <td>该接口用于删除当前会议已保存的多画面布局。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetMultiPicture</td>
                    <td>设置会议多画面。该接口废弃不用,请使用“[设置自定义多画面](https://support.huaweicloud.com/api-meeting/meeting_21_0418.html)”接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="29">会议管理</td>
                    <td>CreateAuthRandom</td>
                    <td>根据会议ID + 密码鉴权返回鉴权随机数,如果是小程序调用时,需要企业支持小程序功能</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowConfOrg</td>
                    <td>SP管理员根据会议ID查询该会议归属的企业ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecurringSubMeeting</td>
                    <td>该接口用于修改已预约的周期性会议的子会议。会议开始后,不能被修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckCallNumberInConf</td>
                    <td>通过该接口查询号码,是否在会议中</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelRecurringMeeting</td>
                    <td>该接口用于取消周期性会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchRecordings</td>
                    <td>该接口用于查询会议录制列表。管理员可以查询本企业内所有的录制,普通用户仅能查询自己创建的会议的录制。不带查询参数时,默认查询权限范围内的录制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRecordings</td>
                    <td>该接口用于批量删除会议的录制。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchAttendanceRecordsOfHisMeeting</td>
                    <td>该接口用于查询指定历史会议的与会者记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOrgRes</td>
                    <td>企业管理员查询所属企业的资源使用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelRecurringSubMeeting</td>
                    <td>该接口用于取消周期性会议的子会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordingFileDownloadUrls</td>
                    <td>该接口用户查询指定会议录制文件下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRecurringMeeting</td>
                    <td>该接口用于修改已预约的周期性会议。会议开始后,不能被修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMeeting</td>
                    <td>该接口用于修改已预约的会议。会议开始后,不能被修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchCtlRecordsOfHisMeeting</td>
                    <td>该接口用于查询指定历史会议的会控记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRegionInfoOfMeeting</td>
                    <td>该接口用于查询会议所在区域的IP和域名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowOnlineMeetingDetail</td>
                    <td>该接口用于查询正在召开的会议详情。管理员可以查询本企业内所有的在线会议详情,普通用户仅能查询自己帐号创建或者需要参加的在线会议详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchMeetings</td>
                    <td>该接口用于查询尚未结束的会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartMeeting</td>
                    <td>该接口用于通过会议ID和会议密码激活会议。所有的会控接口都需要在会议激活后才能调用,可以通过该接口先激活会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchHisMeetings</td>
                    <td>该接口用于查询已经结束的会议。管理员可以查询本企业内所有的历史会议,普通用户仅能查询自己创建或者被邀请的历史会议。不带查询参数时,默认查询权限范围内的历史会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAnonymousAuthRandom</td>
                    <td>该接口用于匿名用户入会鉴权。请求根据会议ID和密码鉴权,返回鉴权随机数(可以根据该随机数获取匿名用户信息、会议信息等)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRecordingDetail</td>
                    <td>改接口用于查询某个会议录制的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRecurringMeeting</td>
                    <td>该接口用于预约周期性会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMeetingDetail</td>
                    <td>查询偏移量</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMeeting</td>
                    <td>该接口用于创建立即会议和预约会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchOnlineMeetings</td>
                    <td>该接口用于查询正在召开的会议列表。管理员可以查询本企业内所有在线会议,普通用户仅能查询当前自己帐号创建或者需要参加的在线会议。不带查询参数时,默认查询权限范围内的在线会议,按开始时间升序排列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSpRes</td>
                    <td>SP管理员查询所属SP的共享资源使用信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOnlineConfAttendee</td>
                    <td>该接口用于查询指定会议的在线与会者信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHisMeetingDetail</td>
                    <td>该接口用户查询指定历史会议的详情。管理员可以查询本企业内所有的历史会议详情,普通用户仅能查询自己创建或者被邀请的历史会议详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelMeeting</td>
                    <td>该接口用于取消预约的会议。企业管理员可以取消本企业下用户创建的会议,普通用户只能取消自己创建的会议。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">会议纪要</td>
                    <td>ShowMeetingFileList</td>
                    <td>用户使用手机扫码后,手机端请求服务端,让服务端通知指定IdeaHub打开指定用户的会议纪要文件列表。二维码内容 :cloudlink://cloudlink.huawei.com/h5page?action=OPEN_MEETING_FILE_LIST&amp;key1=value1&amp;key2=value2 。key/value的个数可能变化,终端解析后,在发起后续请求时,将所有key/value存为map,作为入参即可。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddToPersonalSpace</td>
                    <td>用户使用手机扫码后,手机端请求服务端将当前会议纪要文件保存到个人云空间。二维码内容 :cloudlink://cloudlink.huawei.com/h5page?action=SAVE_MEETING_FILE&amp;key1=value1&amp;key2=value2 。key/value的个数可能变化,终端解析后,在发起后续请求时,将所有key/value存为map,作为入参即可。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowMeetingFile</td>
                    <td>用户查询单个会议纪要详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchMeetingFileList</td>
                    <td>用户查询自己的会议纪要列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">信息窗发布管理</td>
                    <td>ShowPublication</td>
                    <td>根据ID获取发布详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePublication</td>
                    <td>修改信息窗发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchPublications</td>
                    <td>获取信息窗发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePublications</td>
                    <td>删除信息窗发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddPublication</td>
                    <td>新增信息窗发布。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">信息窗素材管理</td>
                    <td>UpdateMaterial</td>
                    <td>更新信息窗素材。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteMaterials</td>
                    <td>删除信息窗素材。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddMaterial</td>
                    <td>新增信息窗素材(上传素材文件)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchMaterials</td>
                    <td>分页查询信息窗素材。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">信息窗节目管理</td>
                    <td>AddProgram</td>
                    <td>新增信息窗节目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProgram</td>
                    <td>更新信息窗节目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProgram</td>
                    <td>根据ID获取节目详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePrograms</td>
                    <td>删除信息窗节目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchPrograms</td>
                    <td>获取信息窗节目。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">查询企业通讯录</td>
                    <td>SearchCorpExternalDir</td>
                    <td>企业用户(含管理员)通过该接口查询该企业的外部联系人或者个人外部联系人。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchCorpDir</td>
                    <td>企业用户(含管理员)通过该接口查询该企业的通讯录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">激活码管理</td>
                    <td>ResetActivecode</td>
                    <td>当硬终端激活码失效时,企业管理员可以通过该接口重置激活码,使用重新获取的激活码激活终端,每24小时可重新激活5次。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVisionActiveCode</td>
                    <td>企业管理员批量删除激活码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchVisionActiveCode</td>
                    <td>企业管理员分页查询激活码,支持激活码、终端名称模糊查询。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVisionActiveCode</td>
                    <td>企业管理员生成智慧屏、电子白板(SmartRooms)、Ideahub的激活码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetVisionActiveCode</td>
                    <td>企业管理员重置帐号的激活码,重置后,原设备直接解绑,必须重新激活使用,若手机邮箱不填,则不会发送新的激活码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">用户头像管理</td>
                    <td>SetProfileImage</td>
                    <td>用户设置头像</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetUserProfileImage</td>
                    <td>为企业内的用户设置头像(只允许管理员调用)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">用户密码管理</td>
                    <td>UpdatePwd</td>
                    <td>企业成员通过该接口提供用户修改密码功能,服务器收到请求,修改用户密码并返回结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendSlideVerifyCode</td>
                    <td>该接口提供发送滑块验证码。服务器收到请求,返回抠图以及抠图后的原图等结果。需要在前台界面显示出抠图以及抠图后的原图,用户通过滑块操作来匹配图形。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckVerifyCode</td>
                    <td>该接口提供校验验证码,服务器收到请求,返回结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPwdByAdmin</td>
                    <td>企业管理员通过该接口提供企业管理员重置企业成员密码的功能。当服务器收到重置密码的请求时,发送新的密码到企业成员的邮箱或者短信,并返回结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendVeriCodeForChangePwd</td>
                    <td>该接口提供发送验证码,服务器收到请求,发送验证码到邮箱或者短信并返回结果。用户在前台界面通过滑块验证后,再进行发送验证码操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckSlideVerifyCode</td>
                    <td>该接口提供校验滑块验证码。服务器收到请求,返回校验结果。用户在前台界面通过滑块操作匹配图形,使得抠图和原图吻合。然后服务器进行校验滑块验证码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetPwd</td>
                    <td>该接口提供给用户重置密码功能,服务器收到请求,重新设置用户密码并返回结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="13">用户管理</td>
                    <td>ShowMyInfo</td>
                    <td>企业用户通过该接口查询自己的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendVeriCodeForUpdateUserInfo</td>
                    <td>修改用户手机或邮箱时,需要获取验证码。企业用户通过该接口获取验证码,系统会向用户的手机或邮箱发送,验证码1分钟内有效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMyInfo</td>
                    <td>企业用户通过该接口修改自己的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateContact</td>
                    <td>企业用户通过该接口修改手机或邮箱,需要先获取验证码,验证多次失败会禁止修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckVeriCodeForUpdateUserInfo</td>
                    <td>企业用户通过该接口校验手机和邮箱对应的验证码,一分钟内记录尝试次数不得超过5次。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchUsers</td>
                    <td>企业管理员通过该接口分页查询企业用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUser</td>
                    <td>企业管理员通过该接口修改企业用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowUserDetail</td>
                    <td>企业管理员通过该接口查询企业用户详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>InviteUser</td>
                    <td>通过手机号码或者邮箱地址邀请用户加入企业。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateUserStatus</td>
                    <td>企业管理员通过该接口批量修改用户状态,当用户帐号数资源或者电子白板(SmartRooms)资源到期后,若企业内对应资源的用户帐号超过数量后会被系统随机自动停用,此时可通过该接口修改用户的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddUser</td>
                    <td>企业管理员通过该接口添加企业用户。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowUserDetails</td>
                    <td>批量查询用户详情,支持指定第三方账号查询详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteUsers</td>
                    <td>企业管理员通过该接口批量删除企业用户。删除多个用户时,全部删除成功或者全部删除失败。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">登录鉴权</td>
                    <td>SetSsoConfig</td>
                    <td>该接口用于设置SSO登录的鉴权配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckToken</td>
                    <td>该接口提供校验token合法性功能。服务器收到请求后,验证token合法性并返回结果。如果参数needGenNewToken为true时,生成新的token并返回。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProxyToken</td>
                    <td>该接口使用第三方的帐号进行代理鉴权,鉴权通过后生成一个Access Token。当前支持的第三方代理帐号包括:</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateToken</td>
                    <td>该接口使用华为云会议帐号和密码鉴权,鉴权通过后生成一个Access Token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePortalRefNonce</td>
                    <td>通过Access Token生成页面免登陆跳转到华为云会议的Portal的nonce信息。获取到nonce信息后,通过链接https://meeting.huaweicloud.com/?lang=zh-CN&amp;nonce=xxxxxxxxxxxxx#/login进行免登陆跳转。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAppIdToken</td>
                    <td>该接口使用App ID方式进行鉴权,鉴权通过后生成一个Access Token。App ID鉴权的原理介绍,请参考[App ID鉴权介绍](https://support.huaweicloud.com/devg-meeting/meeting_20_0011.html) 。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteToken</td>
                    <td>该接口提供注销功能。服务器收到请求后,删除该Token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSsoConfig</td>
                    <td>该接口用于查询SSO登录的鉴权配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateToken</td>
                    <td>该接口提供刷新Token功能,根据传入的Token,刷新Token失效时间并返回结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="8">硬终端管理</td>
                    <td>UpdateDevice</td>
                    <td>企业管理员通过该接口修改专业会议终端。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteDevices</td>
                    <td>企业管理员通过该接口批量删除专业会议终端,返回删除失败的列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceStatus</td>
                    <td>调用本接口可以查询硬终端的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateDevicesStatus</td>
                    <td>企业管理员通过该接口批量修改专业会议终端状态。当硬终端资源到期后,若企业内对应资源的硬终端超过数量后会被系统随机自动停用,此时可通过该接口修改专业会议终端的状态。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SearchDevices</td>
                    <td>企业管理员通过该接口分页查询专业会议终端信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddDevice</td>
                    <td>企业管理员通过该接口添加专业会议终端。专业会议终端包括DP300/HUAWEI Bar系列/HUAWEI Board/TE系列。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceTypes</td>
                    <td>企业管理员通过该接口获取所有的专业会议终端类型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDeviceDetail</td>
                    <td>企业管理员通过该接口查询专业会议终端详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">网络研讨会管理</td>
                    <td>ListUpComingWebinars</td>
                    <td>该接口用于查询即将召开的网络研讨会。管理员可查询企业内即将召开网络研讨会,非管理员可查询自己预订的即将召开的网络研讨会。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWebinar</td>
                    <td>该接口用于查询指定网络研讨会的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWebinar</td>
                    <td>该接口用于取消已预约的网络研讨会。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHistoryWebinars</td>
                    <td>该接口用于查询历史网络研讨会。管理员可查询企业内历史网络研讨会,非管理员可查询个人历史网络研讨会。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOngoingWebinars</td>
                    <td>该接口用于查询正在召开的网络研讨会。管理员可查询企业内正在召开网络研讨会,非管理员可查询自己预订的正在召开的网络研讨会。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRoomSetting</td>
                    <td>该接口用于设置指定网络研讨会的高级设置。管理员可设置企业内的网络研讨会高级设置,非管理员只可设置自己预定的网络研讨会的高级设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWebinar</td>
                    <td>该接口用于修改已创建的网络研讨会。网络研讨会开始后不能修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowRoomSetting</td>
                    <td>该接口用于查询指定网络研讨会的高级设置。管理员可查询企业内的网络研讨会高级设置,非管理员只可查询自己预定的网络研讨会的高级设置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadFile</td>
                    <td>该接口用户上传网络研讨会高级设置用的图片。图片可用于网络研讨会的封面和Logo。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWebinar</td>
                    <td>该接口用于创建网络研讨会。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">网络质量</td>
                    <td>ListNetworkQuality</td>
                    <td>查询会场网络质量</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>