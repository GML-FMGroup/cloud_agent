# KooMessage MCP Server 

## 版本信息
v0.1.0

## 产品描述

KooMessage MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务KooMessage交互的能力。可以基于自然语言对KooMessage资源进行全链路管理。

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
                    <td rowspan="2">AIMCallBack</td>
                    <td>AddCallBack</td>
                    <td>用户根据要求创建回执接口后,可以调用此接口进行注册,注意:此接口仅允许te_admin角色用户调用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimCallbacks</td>
                    <td>用户注册回执接口之后,可以根据此接口查询所有已注册回执接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AIMResolveTask</td>
                    <td>ListResolveTasks</td>
                    <td>创建解析任务后,客户可以查询解析任务状态信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckMobileCapability</td>
                    <td>用户在下发智能信息前,通过此接口批量查询对应手机的智能信息解析能力。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimResolveDetails</td>
                    <td>根据用户提供的过滤条件查询个性化解析明细,包括:发送任务ID、发送手机号码等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateResolveTask</td>
                    <td>生成解析的短链。一次最多生成100个解析的短链。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AIMSendTask</td>
                    <td>ListAimSendDetails</td>
                    <td>根据用户提供的过滤条件查询发送明细列表,包括:发送任务ID、发送手机号码等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAimSendTask</td>
                    <td>根据客户的参数发送任务名称、智能信息模板ID等进行智能信息发送。一次最多发送100个智能信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimSendTasks</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimSendReports</td>
                    <td>查询智能信息发送报表。</td>
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
                    <td>支持用户上传模板使用的图片或者视频。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAimPersonalTemplate</td>
                    <td>根据用户提供的模板ID,删除智能信息个人模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTemplateMaterial</td>
                    <td>根据用户提供的模板ID,删除模板素材。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetPrimaryVideoThumbnail</td>
                    <td>根据用户提供的视频封面图资源ID和AIM视频资源ID设置视频模板的封面图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAimPersonalTemplate</td>
                    <td>用于用户创建个人模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimTemplateMaterials</td>
                    <td>根据用户提供的过滤条件,查询模板素材列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTemplateVideoThumbnail</td>
                    <td>根据用户提供的过滤条件,查询视频模板封面图资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimTemplateReports</td>
                    <td>根据用户指定过滤条件查询指定智能信息模板的解析次数。当日数据需要次日16:00之后才能查询到。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePersonalTemplateState</td>
                    <td>根据用户提供的模板ID,启用或禁用智能信息个人模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">AimSaMenu</td>
                    <td>ListMenus</td>
                    <td>根据用户提供的过滤条件查询服务号菜单。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateMenu</td>
                    <td></td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">AimSaPort</td>
                    <td>ListPortInfos</td>
                    <td>支持查询通道号列表和通道号绑定信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RegisterPort</td>
                    <td>注册通道号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LockPort</td>
                    <td>通道号绑定服务号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeletePortInfo</td>
                    <td>删除通道号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UnlockPort</td>
                    <td>通道号解绑服务号。</td>
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
                    <td>服务号解结,冻结服务号。需审核,审核通过生效。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>FreezePub</td>
                    <td>支持用户通过此接口冻结服务号。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePubInfo</td>
                    <td>支持用户更新服务号信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AimSaPubUnify</td>
                    <td>PushPortalInfo</td>
                    <td>支持用户通过此接口根据主页ID催审。主页需要在与其关联的服务号审核通过之后才能催审。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PushMenuInfo</td>
                    <td>支持用户通过此接口根据菜单ID催审。菜单需要在与其关联的服务号审核通过之后才能催审。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePubInfo</td>
                    <td>一站式服务号创建。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadMedia</td>
                    <td>支持用户上传图片资源。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">AimSmsApp</td>
                    <td>ListAimMsgApp</td>
                    <td>该接口用于用户查询已创建的短信应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAimMsgApp</td>
                    <td>该接口用于用户修改短信应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSmsApp</td>
                    <td>该接口用于用户创建短信应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimMsgAppDetail</td>
                    <td>该接口用于用户获取已创建的短信应用详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">AimSmsSend</td>
                    <td>SendAimBatchMessages</td>
                    <td>向单个或多个用户发送相同内容的短信。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SendAimBatchDifferentMessages</td>
                    <td>该接口用于向不同用户发送不同内容的短信。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">AimSmsSignature</td>
                    <td>ListAimMsgSignatureDetail</td>
                    <td>该接口用于用户获取已创建的短信签名详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAimMsgSignature</td>
                    <td>该接口用于用户更新短信签名信息,目前仅支持审核不通过的短信签名重新修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadAimMsgSignatureFile</td>
                    <td>该接口用于用户上传创建短信签名所需的营业执照/授权委托书文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAimMsgSignatureFileInfo</td>
                    <td>该接口用于用户查询创建短信签名时上传的营业执照/授权委托书文件信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimMsgSignature</td>
                    <td>该接口用于用户查询已创建的短信签名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAimMsgSignature</td>
                    <td>该接口用于用户删除已创建的短信签名。删除已审核通过的签名,会同步删除该签名对应的通道号和该签名下的所有短信模板,请谨慎操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddAimMsgSignature</td>
                    <td>该接口用于用户创建短信签名。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">AimSmsTemplate</td>
                    <td>UpdateAimMsgTemplate</td>
                    <td>该接口用于用户修改短信模板信息,目前仅支持审核不通过的短信模板重新修改。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAimMsgTemplate</td>
                    <td>该接口用于用户创建短信模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAimMsgTemplateDetail</td>
                    <td>该接口用于用户获取已创建的短信模板详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAimMsgTemplateVariable</td>
                    <td>该接口用于用户查询短信模板变量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAimMsgTemplate</td>
                    <td>该接口用于用户查询已创建的短信模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAimMsgTemplate</td>
                    <td>该接口用于用户删除已创建的短信模板。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">VMSSendTask</td>
                    <td>AddVmsCallBack</td>
                    <td>用户根据要求创建智能信息基础版回执接口后,可以调用此接口进行注册。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVmsSendTasks</td>
                    <td>支持用户根据过滤条件查询智能信息基础版任务列表。包括:发送任务名称、智能信息基础版模板ID等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVmsCallbacks</td>
                    <td>查询所有已注册的智能信息基础版回执接口。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVmsSendTask</td>
                    <td>支持用户通过此接口进行智能信息基础版任务发送。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">VmsTemplate</td>
                    <td>ListVmsTemplateStatus</td>
                    <td>根据用户提供的过滤条件查询智能信息基础版模板状态列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVmsTemplate</td>
                    <td>支持用户通过此接口创建智能信息基础版模板。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>