# CloudIDE MCP Server 

## 版本信息
v0.1.0

## 产品描述

CloudIDE MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务CloudIDE交互的能力。可以基于自然语言对CloudIDE资源进行全链路管理。

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
                    <td rowspan="13">IDE实例管理</td>
                    <td>ShowInstanceStatusInfo</td>
                    <td>查询某个IDE实例的状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteInstance</td>
                    <td>删除IDE实例(同时删除磁盘数据)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartInstance</td>
                    <td>启动IDE实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowInstance</td>
                    <td>查询某个IDE实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StopInstance</td>
                    <td>停止IDE实例(不删除磁盘数据)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckName</td>
                    <td>查询IDE实例名是否重复</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstanceBy3rd</td>
                    <td>创建IDE实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListInstances</td>
                    <td>查询IDE实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckInstanceAccess</td>
                    <td>查询用户是否有权限访问某个IDE实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstanceActivity</td>
                    <td>刷新IDE实例活跃状态,超过该实例设置的过期时间后实例自动关闭。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListOrgInstances</td>
                    <td>查询某个租户下的IDE实例列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateInstance</td>
                    <td>修改IDE实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateInstance</td>
                    <td>创建IDE实例</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="6">codebreeze</td>
                    <td>ShowResult</td>
                    <td>get the result of the code generation request.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateAcceptance</td>
                    <td>create a acceptance</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateApply</td>
                    <td>create a join-request</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateLogin</td>
                    <td>create a login</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateRequest</td>
                    <td>create a code generation request.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEvent</td>
                    <td>create an event</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">codebreezetsbot</td>
                    <td>SyncChat</td>
                    <td>异步聊天请求</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>StartChat</td>
                    <td>开启对话</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SyncGetChatResult</td>
                    <td>异步聊天获取结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">帐号权限管理</td>
                    <td>ShowAccountStatus</td>
                    <td>查询当前帐号访问权限</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">技术栈管理</td>
                    <td>ListStacks</td>
                    <td>按region获取标签所有技术栈</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPrice</td>
                    <td>获取技术栈计费信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="16">插件市场</td>
                    <td>AddExtensionEvaluation</td>
                    <td>添加插件评论</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExtensionTestingResult</td>
                    <td>获取插件检测结果</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListPublisher</td>
                    <td>获取当前用户下的发布商列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadExtensionFile</td>
                    <td>上传插件</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>PublishExtension</td>
                    <td>插件发布</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddExtensionStar</td>
                    <td>添加新评星</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckMaliciousExtensionEvaluation</td>
                    <td>举报评论,举报回复</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UploadFilePublisher</td>
                    <td>文件上传归一化</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowCategoryList</td>
                    <td>查询插件分类</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEvaluationReply</td>
                    <td>删除回复</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExtensionEvaluation</td>
                    <td>查询插件评价</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListExtensions</td>
                    <td>查询插件列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEvaluation</td>
                    <td>删除评论</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddExtensionEvaluationReply</td>
                    <td>添加评论回复、回复评论回复</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExtensionEvaluationStar</td>
                    <td>查询插件评星</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowExtensionDetail</td>
                    <td>查询插件详细信息</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">插件管理</td>
                    <td>ShowExtensionAuthorization</td>
                    <td>查询ide实例对插件的授权情况,同意授权的插件能在ide实例内携带登陆用户的token调用第三方服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateExtensionAuthorization</td>
                    <td>设置ide实例对插件的授权。同意、不同意、未知(下次重新询问)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">模板管理</td>
                    <td>ListProjectTemplates</td>
                    <td>查询技术栈模板工程</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>