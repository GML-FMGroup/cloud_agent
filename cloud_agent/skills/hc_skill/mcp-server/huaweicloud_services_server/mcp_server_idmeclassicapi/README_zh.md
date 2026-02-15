# iDMEClassicAPI MCP Server 

## 版本信息
v0.1.0

## 产品描述

iDMEClassicAPI MCP Server 是一个模型上下文协议(Model Context Protocol)服务器，为MCP客户端(如Claude Desktop、Cline、Cursor)提供与华为云服务iDMEClassicAPI交互的能力。可以基于自然语言对iDMEClassicAPI资源进行全链路管理。

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
                    <td rowspan="1">业务编码生成器</td>
                    <td>GenerateBusinessCode</td>
                    <td>调用该接口为指定模型的数据实例生成业务编码。在调用该接口前请确保数据模型具有“业务编码生成器”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="5">关系实体服务</td>
                    <td>ListQueryRelatedObjects</td>
                    <td>调用该接口查询指定关系实体所关联的源/目标模型的所有实例信息,包含具体的属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteTarget</td>
                    <td>调用该接口输入源模型的数据实例ID和目标模型的英文名称,删除对应关系实体的数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryRelationship</td>
                    <td>调用该接口输入数据实例的ID和对应的关系角色(源/目标模型),查询并返回对应关系实体的数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListBatchQueryRelatedObjects</td>
                    <td>调用该接口批量查询指定关系实体所关联的源/目标模型的所有实例信息,包含具体的属性。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryTarget</td>
                    <td>调用该接口输入源模型的数据实例ID,查询并返回与该实例关联的目标模型数据实例的信息,实例信息包含对应数据实例的“列表属性”。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="24">基础数据服务</td>
                    <td>ShowLogicalDeleteUsingPost</td>
                    <td>根据数据实例的唯一编码,软删除指定数据模型中的一个数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListUsingPost</td>
                    <td>根据查询条件分页返回模型基本属性信息且不级联查询(不支持扩展属性作为查询条件)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteLogicalUsingPost</td>
                    <td>根据数据实例的唯一编码,批量软删除指定数据模型中的多个数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStaticsPage</td>
                    <td>分页查询数据实例的统计信息,支持分组和简单函数分页统计。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CountUsingPost</td>
                    <td>根据指定的查询条件,统计指定数据模型中的实例总数。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteUsingPost</td>
                    <td>根据数据实例的唯一编码,批量删除指定数据模型中的多个数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryUsingPost</td>
                    <td>当数据模型中存在“列表属性”为“是”的属性时,可通过此接口查询数据模型中的实例数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowLogicalDeleteByConditionUsingPost</td>
                    <td>通过此接口,软删除指定条件查询返回的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateUsingPost</td>
                    <td>创建指定数据模型的数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateUsingPost</td>
                    <td>批量创建指定数据模型的数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveAsUsingPost</td>
                    <td>版本对象的另存为接口(saveAs)用于创建一条与原版本对象实例数据相同的数据实例。该实例数据会完全复制原实例现有的数据,包括与其关联的主对象和分支对象,且新实例数据的版本号从初始值开始计算。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteUsingPost</td>
                    <td>根据数据实例的唯一编码,删除指定数据模型中的一个数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGetByUniqueKey</td>
                    <td>当数据模型中存在“唯一键”为“是”的属性时,可根据该属性查询实例数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchShowGetUsingPost</td>
                    <td>根据多个数据实例的唯一编码,批量查询实例的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteByConditionUsingPost</td>
                    <td>通过此接口,删除满足指定条件的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateUsingPost</td>
                    <td>批量更新指定数据模型中的多个实例数据。如果某个实例的唯一编码不存在,该实例不做任何更新操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateByConditionUsingPost</td>
                    <td>根据指定条件更新指定模型的实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListSelectUsingPost</td>
                    <td>根据查询条件及指定属性分页返回(不支持扩展属性作为选定属性列)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowStaticsUsingPost</td>
                    <td>根据指定函数,统计指定数据模型的实例信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowFindUsingPost</td>
                    <td>分页查询指定数据模型中的所有实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveUsingPost</td>
                    <td>当数据模型中存在“唯一键”为“是”的属性时,可根据该属性的英文名称更新该数据模型中实例的指定字段数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateUsingPost</td>
                    <td>更新指定数据模型中的一个实例数据。如果实例的唯一编码不存在,则不做任何更新操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGetUsingPost</td>
                    <td>根据一个数据实例的唯一编码,查询实例的详细信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>SaveAllUsingPost</td>
                    <td>当数据模型中存在“唯一键”为“是”的属性时,可根据该属性的英文名称更新该数据模型中实例的所有字段数据。如果更新的实例不存在,系统将自动创建该实例数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">多维视图和多维分支</td>
                    <td>UpdateView</td>
                    <td>调用该接口更新指定M-V模型实体的多维视图。在调用该接口前请确保数据模型具有“多维视图&amp;多维分支”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateView</td>
                    <td>调用该接口批量创建指定M-V模型实体的多维视图。在调用该接口前请确保数据模型具有“多维视图&amp;多维分支”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateView</td>
                    <td>调用该接口创建指定M-V模型实体的多维视图。在调用该接口前请确保数据模型具有“多维视图&amp;多维分支”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">失效管理</td>
                    <td>EnableDataInstance</td>
                    <td>调用该接口生效指定模型的数据实例,同时返回生效成功的实例数量。在调用该接口前请确保数据模型具有“失效管理”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DisableDataInstance</td>
                    <td>调用该接口失效指定模型的数据实例,同时返回失效成功的实例数量。在调用该接口前请确保数据模型具有“失效管理”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">数据分类管理</td>
                    <td>RemoveFromCategory</td>
                    <td>将数据分类数据实例从数据分类对象数据实例中移除。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddToCategory</td>
                    <td>将数据分类对象数据实例添加至数据分类数据实例中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">标签管理</td>
                    <td>ShowTag</td>
                    <td>调用该接口查询指定模型的数据实例对应标签信息。在调用该接口前请确保数据模型具有“标签管理”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>AddTag</td>
                    <td>调用该接口为指定模型的数据实例绑定标签。在调用该接口前请确保数据模型具有“标签管理”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RemoveTag</td>
                    <td>调用该接口为指定数据模型的数据实例解绑标签。在调用该接口前请确保数据模型具有“标签管理”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="7">树形结构</td>
                    <td>BatchAddChildNode</td>
                    <td>调用该接口批量为指定数据实例添加子节点。在调用该接口前请确保数据模型具有“树形结构”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGetRoot</td>
                    <td>调用该接口获取指定数据实例的根节点。在调用该接口前请确保数据模型具有“树形结构”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGetChildList</td>
                    <td>调用该接口获取指定数据实例的子节点,同时返回其列表属性。在调用该接口前请确保数据模型具有“树形结构”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Refresh</td>
                    <td>调用该接口刷新指定数据实例对应的节点全路径。在调用该接口前请确保数据模型具有“树形结构”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGetAllParentList</td>
                    <td>调用该接口获取指定数据实例的所有父节点,同时返回其列表属性。在调用该接口前请确保数据模型具有“树形结构”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowGetParent</td>
                    <td>调用该接口获取指定数据实例的父节点,同时返回其列表属性。在调用该接口前请确保数据模型具有“树形结构”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchRemoveChildNode</td>
                    <td>调用该接口批量移除指定数据实例的所有子节点。在调用该接口前请确保数据模型具有“树形结构”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="30">版本服务</td>
                    <td>BatchUpdateByAdmin</td>
                    <td>管理员通过此接口批量更新指定M-V模型的指定实例数据。如果某个实例的唯一编码不存在,则不做任何更新操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAndCheckin</td>
                    <td>通过此接口更新指定M-V模型实例,并检入该实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckoutAndUpdate</td>
                    <td>根据主对象ID检出并更新M-V模型数据实例,即检出后生成一个新的数据实例的同时,更新该新实例的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckoutUndoByAdmin</td>
                    <td>管理员通过此接口撤销指定M-V模型实例的检出,将实例数据还原至检出前的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogicalLatestVersion</td>
                    <td>根据主对象ID,软删除版本对象下最新分支的最新版本实例数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLatestVersion</td>
                    <td>根据主对象ID,删除版本对象下最新分支的最新版本实例数据。请您谨慎使用删除操作,删除后该数据将无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowVersionByMaster</td>
                    <td>根据主对象ID、迭代版本和版本号,查询M-V模型实例的详细版本信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckout</td>
                    <td>根据主对象ID批量检出M-V模型数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckin</td>
                    <td>根据主对象ID批量检入M-V模型数据实例。已检入的数据实例会生成一个新的迭代版本,并将数据存储至系统中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckoutAndUpdate</td>
                    <td>根据主对象ID批量检出并更新M-V模型数据实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListAllVersions</td>
                    <td>根据主对象ID,获取对应M-V模型实例的所有版本信息(包含对应版本下的属性信息)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateAndCheckin</td>
                    <td>通过此接口批量更新指定M-V模型实例,并检入这些实例。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteBranch</td>
                    <td>根据父模型ID和版本对象,删除最新大版本下的所有小版本。请您谨慎使用删除操作,删除后该数据将无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateVersion</td>
                    <td>根据M-V模型实体的唯一编码,批量将该实体下实例的版本号更新至最新版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ExecuteRevise</td>
                    <td>通过此接口修订指定M-V模型实例。修订后,该实例的“version.修订版本”会更新为新的修订版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckoutUndo</td>
                    <td>通过此接口批量撤销指定M-V模型实例的检出,将实例数据批量还原至检出前的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteLogicalBranch</td>
                    <td>根据主对象ID,批量软删除最新大版本下的所有小版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareBusinessVersion</td>
                    <td>通过此接口可以对比某个M-V模型数据实例的不同版本的属性和关系。建议使用数据建模引擎(xDM Foundation,简称xDM-F)新增的差异对比功能,即使用instance-attrs-comparison和instance-relation-comparison接口,更多内容可在应用运行态的“数据服务管理 &gt; 全量数据服务 &gt; 系统管理API &gt; 属性对比API”中查看。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateByAdmin</td>
                    <td>管理员通过此接口更新指定M-V模型的指定实例数据。如果实例的唯一编码不存在,则不做任何更新操作。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteLogicalLatestVersion</td>
                    <td>根据主对象ID,批量软删除版本对象下最新分支的最新版本实例数据。单次调用此接口时,建议最多设置不超过100个主对象ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteLatestVersion</td>
                    <td>根据主对象ID,批量删除版本对象下最新分支的最新版本实例数据。单次调用此接口时,建议最多设置不超过100个主对象ID。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Checkin</td>
                    <td>根据主对象ID检入M-V模型数据实例。已检入的数据实例会生成一个新的迭代版本,并将数据存储至系统中。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CheckoutUndo</td>
                    <td>通过此接口撤销指定M-V模型实例的检出,将实例数据还原至检出前的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAndRevise</td>
                    <td>根据主对象ID修订并更新M-V模型数据实例,即修订后实例的“version.修订版本”更新为新的修订版本,并同时更新该实例的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteLogicalBranch</td>
                    <td>根据父模型ID和版本对象,软删除M-V模型实例下最新分支的所有小版本数据。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateAndRevise</td>
                    <td>根据主对象ID批量修订并更新M-V模型数据实例,即修订后实例的“version.修订版本”更新为新的修订版本,并同时更新该实例的信息。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCheckoutUndoByAdmin</td>
                    <td>管理员通过此接口批量撤销指定M-V模型实例的检出,将实例数据批量还原至检出前的内容。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchExecuteRevise</td>
                    <td>通过此接口批量修订指定M-V模型实例。修订后,实例的“version.修订版本”会更新为新的修订版本。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteBranch</td>
                    <td>根据主对象ID和父模型ID,批量软删除最新大版本下的所有小版本。请您谨慎使用删除操作,删除后该数据将无法恢复。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Checkout</td>
                    <td>根据主对象ID检出M-V模型数据实例,检出后会生成一个新的数据实例,该实例会完全复制原实例现有的信息,且状态修改为已检出。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">生命周期管理</td>
                    <td>SwitchLifecycleTemplate</td>
                    <td>调用该接口切换指定模型的数据实例绑定的生命周期模板。切换生命周期模板时,需为数据实例指定生命周期的状态。在调用该接口前请确保数据模型具有“生命周期管理”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateState</td>
                    <td>调用该接口修改或切换数据实例绑定的生命周期状态。在调用该接口前请确保数据模型具有“生命周期管理”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">系统版本</td>
                    <td>ListHistoryData</td>
                    <td>调用该接口输入指定模型的统计时间区间(开始时间和结束时间)后,会以数据实例的最后修改时间作为查询条件,分页查询该实例的历史版本信息。在调用该接口前请确保数据模型具有“系统版本”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CollectHistoryData</td>
                    <td>输入指定模型的统计时间区间(开始时间和结束时间),即可获取该模型的统计数据,包含创建实例、删除实例、软删除实例和更新实例的数据。在调用该接口前请确保数据模型具有“系统版本”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CompareVersion</td>
                    <td>通过此接口可以对比某个模型数据实例的不同版本的属性和关系。建议使用数据建模引擎(xDM Foundation,简称xDM-F)新增的差异对比功能,即使用instance-attrs-comparison和instance-relation-comparison接口,更多内容可在应用运行态的“数据服务管理 &gt; 全量数据服务 &gt; 系统管理API &gt; 属性对比API”中查看。在调用该接口前请确保数据模型具有“系统版本”功能。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">结构化文档管理</td>
                    <td>ShowGetTokens</td>
                    <td>该接口可以用于通过文档ID和认证类型的方式进行认证来获取结构化文档的Token。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryDocuments</td>
                    <td>查询结构化文档。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQueryShareDocs</td>
                    <td>查询结构化文档分享授权列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDocument</td>
                    <td>更新文档标题。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteShareDocs</td>
                    <td>批量删除结构化文档分享权限。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchCreateShareDocs</td>
                    <td>批量创建分享结构化文档。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchDeleteStructuredDocument</td>
                    <td>批量删除结构化文档。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDocument</td>
                    <td>创建结构化文档。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>BatchUpdateDocument</td>
                    <td>批量更新结构化文档。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>