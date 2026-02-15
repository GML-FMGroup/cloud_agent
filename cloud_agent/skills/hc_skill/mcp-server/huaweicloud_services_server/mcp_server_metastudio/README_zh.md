# MetaStudio MCP Server 

## 版本信息
v0.1.0

## 产品描述

MetaStudio MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务MetaStudio交互的能力。可以基于自然语言对MetaStudio资源进行全链路管理。

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
                    <td rowspan="6">ActiveCodeManagement</td>
                    <td>ListActiveCode</td>
                    <td>该接口用于查询激活码列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateActiveCode</td>
                    <td>该接口用于创建激活码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResetActiveCode</td>
                    <td>该接口用于重置激活码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteActiveCode</td>
                    <td>该接口用于删除激活码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowActiveCode</td>
                    <td>该接口用于查询激活码详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateActiveCode</td>
                    <td>该接口用于修改激活码。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">AgencyManagement</td>
                    <td>DeleteAgencyWithRoleType</td>
                    <td>该接口用于删除项目下委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAgencyWithRoleType</td>
                    <td>该接口用于创建委托。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAgency</td>
                    <td>该接口用于查询项目下委托</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">AsrVocabularyManagement</td>
                    <td>CreateAsrVocabulary</td>
                    <td>该接口用于创建热词表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAsrVocabulary</td>
                    <td>该接口用于查询热词表列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAsrVocabulary</td>
                    <td>该接口用于查询热词表详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAsrVocabulary</td>
                    <td>该接口用于修改热词表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAsrVocabulary</td>
                    <td>该接口用于删除热词表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAsrVocabularyAssociation</td>
                    <td>该接口用于查询热词表关联详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DialogManagement</td>
                    <td>ListSmartChatJob</td>
                    <td>该接口用于查询数字人智能交互任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSmartChatJob</td>
                    <td>该接口用于结束数字人智能交互任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartSmartChatJob</td>
                    <td>该接口用于启动数字人智能交互任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDialogUrl</td>
                    <td>该接口用于创建对话链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSmartChatJob</td>
                    <td>该接口用于查询数字人智能交互任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">DialogReportConfigManagement</td>
                    <td>CreateDialogReportConfig</td>
                    <td>该接口用于创建对话结果上报配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDialogReportConfig</td>
                    <td>该接口用于修改对话结果上报配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDialogReportConfig</td>
                    <td>该接口用于查询对话结果上报配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDialogReportConfig</td>
                    <td>该接口用于删除对话结果上报配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="10">DigitalAssetContentManager</td>
                    <td>ListAssetSummary</td>
                    <td>该接口用于查询媒体资产库中指定的多个资产的概要信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteAsset</td>
                    <td>该接口用于删除资产库中的媒体资产。调用该接口删除媒体资产时,媒体资产会放入回收站中,不会彻底删除。如需彻底删除资产,需增加“mode=force”参数配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDigitalAsset</td>
                    <td>该接口用于更新资产库中的媒体资产信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAssets</td>
                    <td>该接口用于查询资产库中的媒体资产列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RestoreAsset</td>
                    <td>该接口用于恢复被删除至回收站的媒体资产。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAssetReplicationInfo</td>
                    <td>当需要将资产从A Region复制到B Region时,先要在A Region调用该接口用于查询资产复制信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDigitalAsset</td>
                    <td>该接口用于在资产库中添加上传新的媒体资产。可上传的资产类型包括:分身数字人模型、背景图片、素材图片、素材视频、PPT等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAssetByReplicationInfo</td>
                    <td>该接口用于在Region B复制Region A的指定资产。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchExecuteAssetAction</td>
                    <td>该接口用批量资产操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowAsset</td>
                    <td>该接口用于查询资产库中指定媒体资产的详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DigitalHumanBusinessCard</td>
                    <td>UpdateDigitalHumanBusinessCard</td>
                    <td>该接口用于更新数字人名片制作任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDigitalHumanBusinessCard</td>
                    <td>该接口用于查询数字人名片制作任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteDigitalHumanBusinessCard</td>
                    <td>该接口用于删除数字人名片制作任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDigitalHumanBusinessCard</td>
                    <td>该接口用于查询数字人名片制作任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDigitalHumanBusinessCard</td>
                    <td>该接口用于数字人名片制作任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">DigitalHumanVideoManager</td>
                    <td>ListDigitalHumanVideo</td>
                    <td>该接口用于查询视频制作任务列表。可查询分身数字人视频制作列表,照片数字人视频制作列表等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">DigitalHumanVideoManagerFor2D</td>
                    <td>Show2DDigitalHumanVideo</td>
                    <td>该接口用于查询分身数字人视频制作任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Create2DDigitalHumanVideo</td>
                    <td>该接口用于创建分身数字人视频制作任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Cancel2DDigitalHumanVideo</td>
                    <td>该接口用于取消等待中的分身数字人视频制作任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">DigitalHumanVideoManagerForPhoto</td>
                    <td>ShowPhotoDetection</td>
                    <td>该接口用于查询照片检测任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPhotoDigitalHumanVideo</td>
                    <td>该接口用于查询照片分身数字人视频制作任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CancelPhotoDigitalHumanVideo</td>
                    <td>该接口用于取消等待中的照片分身数字人视频制作任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePhotoDigitalHumanVideo</td>
                    <td>该接口用于创建照片分身数字人视频制作任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePhotoDetection</td>
                    <td>该接口用于创建照片检测任务,检测照片是否满足制作照片数字人的要求。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">FileManager</td>
                    <td>DeleteFile</td>
                    <td>该接口用于删除媒体资产库中指定的文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFile</td>
                    <td>该接口用于创建文件并获取上传URL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLargeFile</td>
                    <td>该接口用于创建大文件(超过5G),获取分段上传URL。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConfirmFileUpload</td>
                    <td>资产文件上传完毕后,通过该接口确认上传完成。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">HotQuestionManagement</td>
                    <td>CreateHotQuestion</td>
                    <td>该接口用于创建热点问题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHotQuestion</td>
                    <td>该接口用于删除热点问题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHotQuestion</td>
                    <td>该接口用于查询热点问题详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHotQuestion</td>
                    <td>该接口用于修改热点问题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHotQuestion</td>
                    <td>该接口用于查询热点问题列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">HotWordsManagement</td>
                    <td>ShowHotWords</td>
                    <td>该接口用于查询热词记录详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHotWordsSwitch</td>
                    <td>该接口用于修改热词功能开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateHotWords</td>
                    <td>该接口用于修改热词记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHotWords</td>
                    <td>该接口用于删除热词记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListHotWords</td>
                    <td>该接口用于查询热词记录列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHotWords</td>
                    <td>该接口用于创建热词记录。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHotWordsSwitch</td>
                    <td>该接口用于查询热词功能开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">InteractionRuleGroupManager</td>
                    <td>UpdateInteractionRuleGroup</td>
                    <td>该接口用于更新智能直播间互动规则库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInteractionRuleGroup</td>
                    <td>该接口用于创建智能直播间互动规则库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInteractionRuleGroups</td>
                    <td>该接口用于智能直播间互动规则库列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInteractionRuleGroup</td>
                    <td>该接口用于删除智能直播间互动规则库。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">KnowledgeIntentManagement</td>
                    <td>DeleteKnowledgeIntent</td>
                    <td>该接口用于删除知识库意图。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKnowledgeIntent</td>
                    <td>该接口用于创建知识库意图。一个意图包含一个主题,一个答案,若干个问法等。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateKnowledgeIntent</td>
                    <td>该接口用于修改知识库意图。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKnowledgeIntent</td>
                    <td>该接口用于查询知识库意图详情。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKnowledgeIntent</td>
                    <td>该接口用于查询知识库意图列表。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateIntentAndQuestion</td>
                    <td>该接口用于创建知识库意图和问法。一个意图包含一个主题,一个答案,若干个问法等。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">KnowledgeQuestionManagement</td>
                    <td>UpdateKnowledgeQuestion</td>
                    <td>该接口用于修改知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKnowledgeQuestion</td>
                    <td>该接口用于查询知识库问法详情。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateBatchKnowledgeQuestion</td>
                    <td>该接口用于批量创建知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateBatchKnowledgeQuestion</td>
                    <td>该接口用于批量修改知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKnowledgeQuestion</td>
                    <td>该接口用于删除知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKnowledgeQuestion</td>
                    <td>该接口用于查询知识库问法列表。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKnowledgeQuestion</td>
                    <td>该接口用于创建知识库问法。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">KnowledgeSkillManagement</td>
                    <td>UpdateKnowledgeSkill</td>
                    <td>该接口用于修改知识库技能。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteKnowledgeSkill</td>
                    <td>该接口用于删除知识库技能。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListKnowledgeSkill</td>
                    <td>该接口用于查询知识库技能列表。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowKnowledgeSkill</td>
                    <td>该接口用于查询知识库技能详情。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateKnowledgeSkill</td>
                    <td>该接口用于创建知识库技能。一个技能用于特定场景的交互问答,包含若干个意图等。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExportKnowledgeSkill</td>
                    <td>该接口用于导出知识库技能。接口使用限制详见[API使用限制](metastudio_02_0000.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">LivePlatformManage</td>
                    <td>CreateLivePlatform</td>
                    <td>该接口用于创建第三方直播平台。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLivePlatform</td>
                    <td>该接口用于删除第三方直播平台信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLivePlatform</td>
                    <td>该接口用于更新第三方直播平台信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLivePlatforms</td>
                    <td>该接口用于查询直播平台列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLivePlatform</td>
                    <td>该接口用于查询第三方直播平台信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListLivePlatformProducts</td>
                    <td>该接口用于查询第三方直播平台商品列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OnceCodeManagement</td>
                    <td>CreateOnceCode</td>
                    <td>该接口用于创建一次性鉴权码,有效期5分钟,鉴权码只能使用一次,每次使用后需要重新获取。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">OrderInterface</td>
                    <td>CreateMetaStudioOrders</td>
                    <td>该接口用于订购MetaStudio服务的包周期,一次性,按需套餐包产品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="11">PacifyWordsManagement</td>
                    <td>DeletePacifyWords</td>
                    <td>该接口用于删除安抚话术。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePacifyWords</td>
                    <td>该接口用于修改安抚话术。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPacifyWordsIntent</td>
                    <td>该接口用于查询安抚话术意图。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeletePacifyWords</td>
                    <td>该接口用于批量删除安抚话术。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePacifyWords</td>
                    <td>该接口用于创建安抚话术。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPacifyWords</td>
                    <td>该接口用于查询安抚话术列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPacifyWordsTriggerTime</td>
                    <td>该接口用于查询等待触发时长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPacifyWords</td>
                    <td>该接口用于查询安抚话术详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePacifyWordsTriggerTime</td>
                    <td>该接口用于修改安抚话术等待触发时长。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPacifyWordsSwitch</td>
                    <td>该接口用于查询安抚话术功能开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdatePacifyWordsSwitch</td>
                    <td>该接口用于修改安抚话术功能开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="4">PictureModeling</td>
                    <td>CreatePictureModelingByUrlJob</td>
                    <td>该接口用于从URL中获取图片进行照片建模任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreatePictureModelingJob</td>
                    <td>该接口用于创建风格化照片建模任务。通过上传照片,生成风格化数字人模型。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPictureModelingJob</td>
                    <td>该接口用于风格化查询照片建模任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPictureModelingJobs</td>
                    <td>该接口用于查询风格化照片建模任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">ProductManager</td>
                    <td>ListProducts</td>
                    <td>查询商品列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetProductAsset</td>
                    <td>商品资产组合配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateProduct</td>
                    <td>Create product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteProduct</td>
                    <td>删除商品</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowProduct</td>
                    <td>Show product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateProduct</td>
                    <td>Update product</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">RobotManagement</td>
                    <td>ShowRobot</td>
                    <td>该接口用于查询应用详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRobot</td>
                    <td>该接口用于创建应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ValidateRobot</td>
                    <td>该接口用于校验应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteRobot</td>
                    <td>该接口用于删除应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListRobot</td>
                    <td>该接口用于查询应用列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateRobot</td>
                    <td>该接口用于修改应用。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">SmartChatRoomManager</td>
                    <td>CreateSmartChatRoom</td>
                    <td>该接口用于创建智能交互对话。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSmartChatRoom</td>
                    <td>该接口用于删除智能交互对话。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSmartChatRoom</td>
                    <td>该接口用于查询智能交互对话详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSmartChatRooms</td>
                    <td>该接口用于智能交互对话列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateSmartChatRoom</td>
                    <td>该接口用于智能交互对话信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">SmartLiveJobManager</td>
                    <td>ListSmartLiveJobs</td>
                    <td>该接口用于查询租户所有数字人智能直播任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>LiveEventReport</td>
                    <td>该接口用于上报直播间事件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteSmartLiveCommand</td>
                    <td>该接口用于控制数字人直播过程。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopSmartLive</td>
                    <td>该接口用于结束数字人智能直播任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSmartLive</td>
                    <td>该接口用于查询某个智能直播间的直播任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSmartLive</td>
                    <td>该接口用于查询数字人智能直播任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartSmartLive</td>
                    <td>该接口用于启动数字人智能直播任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">SmartLiveRoomManager</td>
                    <td>UpdateSmartLiveRoom</td>
                    <td>该接口用于智能直播间信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSmartLiveRooms</td>
                    <td>该接口用于智能直播间列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteSmartLiveRoom</td>
                    <td>该接口用于删除智能直播间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSmartLiveRoom</td>
                    <td>该接口用于查询智能直播间剧本详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSmartLiveRoom</td>
                    <td>该接口用于创建智能直播间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">StyleManager</td>
                    <td>ListStyles</td>
                    <td>查询数字人风格列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">SubtitleFileManager</td>
                    <td>ShowSubtitleFile</td>
                    <td>该接口用于查询分身数字人视频字幕文件任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateSubtitleFile</td>
                    <td>该接口用于创建分身数字人视频字幕文件任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">TTSA</td>
                    <td>ListTtsaJobs</td>
                    <td>该接口用于查询驱动数字人表情、动作及语音的任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTtsaData</td>
                    <td>该接口用于获取生成的数字人驱动数据,包括语音、表情、动作等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTtsa</td>
                    <td>该接口用于创建驱动数字人表情、动作及语音的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateFacialAnimations</td>
                    <td>该接口用于创建驱动数字人表情的任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListFacialAnimationsData</td>
                    <td>该接口用于获取生成的数字人表情驱动数据</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">TenantManager</td>
                    <td>ListTenantResources</td>
                    <td>查看租户资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountTenantResources</td>
                    <td>统计指定时间段内即将过期的包周期与一次性资源数量。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowResourceUsage</td>
                    <td>查询租户一次性和包周期(包年/包月)资源用量信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="14">TrainingJobManager</td>
                    <td>ShowTenantDurationCfg</td>
                    <td>查询用户配置的个性化音频时长</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CommitVoiceTrainingJob</td>
                    <td>提交训练任务,执行该接口后,任务会进入审核状态,审核完成后会等待训练。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVoiceTrainingJob</td>
                    <td>查询语音训练任务详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SetJobBatchName</td>
                    <td>用户设置任务批次,该接口用于批量任务管理场景,设置任务的批次</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrainingAdvanceJob</td>
                    <td>用户创建语音训练高级版任务,该接口会返回一个obs上传地址,用于上传语音文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrainingBasicJob</td>
                    <td>用户创建语音训练基础版任务,该接口会返回一个obs上传地址,用于上传语音文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTrainingMiddleJob</td>
                    <td>用户创建语音训练进阶版任务,该接口会返回一个obs上传地址,用于上传语音文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobAuditResult</td>
                    <td>获取语音训练任务审核结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ConfirmTrainingSegment</td>
                    <td>确认在线录音结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTrainingSegmentInfo</td>
                    <td>获取在线录音确认结果。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVoiceTrainingJob</td>
                    <td>删除语音训练任务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowJobUploadingAddress</td>
                    <td>获取语音文件上传地址</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVoiceTrainingJob</td>
                    <td>查询语音训练任务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListJobOperationLog</td>
                    <td>查询任务操作日志</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">TraningJobManage</td>
                    <td>Delete2dModelTrainingJob</td>
                    <td>该接口用于删除分身数字人模型训练任务。同时需要删除训练任务相关的训练视频、身份证照片、授权文件、模型资产等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Update2dModelTrainingJob</td>
                    <td>该接口用于更新分身数字人模型训练任务。用于在自动审核或者人工审核不通过情况下,更新训练视频、身份证照片等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Show2dModelTrainingJob</td>
                    <td>该接口用于查询分身数字人模型训练任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Execute2dModelTrainingCommandByUser</td>
                    <td>该接口用于租户执行分身数字人模型训练任务命令,如提交训练审核等。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>List2dModelTrainingJob</td>
                    <td>该接口用于查询分身数字人模型训练任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Create2dModelTrainingJob</td>
                    <td>该接口用于创建分身数字人模型训练任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">Ttsc</td>
                    <td>ShowAsyncTtsJob</td>
                    <td>该接口用于获取TTS音频文件下载链接。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveTtscVocabularyConfigs</td>
                    <td>该接口用于修改TTS租户级自定义读法配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTtscVocabularyConfigs</td>
                    <td>该接口用于设置TTS租户级自定义读法配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateTtsAudition</td>
                    <td>该接口用于创建生成播报内容的语音试听文件任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListTtscVocabularyConfigs</td>
                    <td>该接口用于获取TTS租户级自定义读法配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTtsAuditionFile</td>
                    <td>该接口用于获取TTS试听文件下载链接,返回List中包含当前已生产的试听文件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowTtsPhoneticSymbol</td>
                    <td>根据英文单词返回对应音标列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTtscVocabularyConfigs</td>
                    <td>该接口用于删除TTS租户级自定义读法配置。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAsyncTtsJob</td>
                    <td>该接口用于对外生成音频文件。每个预置音色的计费标准详见[预置音色计费标准](metastudio_02_0060.xml)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">VideoMotionCapture</td>
                    <td>CreateVideoMotionCaptureJob</td>
                    <td>该接口用于创建视频驱动任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteVideoMotionCaptureCommand</td>
                    <td>该接口用于控制数字人驱动。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopVideoMotionCaptureJob</td>
                    <td>该接口用于停止视频驱动任务。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVideoMotionCaptureJob</td>
                    <td>该接口用于查询视频驱动任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVideoMotionCaptureJobs</td>
                    <td>该接口用于查询视频驱动任务列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">VideoScriptManager</td>
                    <td>UpdateVideoScript</td>
                    <td>该接口用于更新视频制作剧本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CopyVideoScripts</td>
                    <td>该接口用于复制视频制作剧本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteVideoScript</td>
                    <td>该接口用于删除视频制作剧本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVideoScript</td>
                    <td>该接口用于查询视频制作剧本详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateVideoScripts</td>
                    <td>该接口用于创建视频制作剧本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListVideoScripts</td>
                    <td>该接口用于查询视频制作剧本列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">WelcomeSpeechManagement</td>
                    <td>ShowWelcomeSpeech</td>
                    <td>该接口用于查询欢迎词详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWelcomeSpeech</td>
                    <td>该接口用于查询欢迎词列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteWelcomeSpeech</td>
                    <td>该接口用于删除欢迎词。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateWelcomeSpeech</td>
                    <td>该接口用于创建欢迎词。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowWelcomeSpeechSwitch</td>
                    <td>该接口用于查询欢迎词功能开关。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWelcomeSpeech</td>
                    <td>该接口用于修改欢迎词。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateWelcomeSpeechSwitch</td>
                    <td>该接口用于修改欢迎词功能开关。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>