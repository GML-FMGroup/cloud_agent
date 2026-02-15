# APIExplorer MCP Server 


## Version
v0.1.0

## Overview

APIExplorer MCP Server is a Model Context Protocol (MCP) server that enables MCP clients (such as Claude Desktop, Cline, and Cursor) to interact with Huawei Cloud Service APIExplorer. It supports end-to-end management of APIExplorer resources using natural language.

## Available Tools
Covers all APIs, available on demand. The list and status are as follows:

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
 <td rowspan="1">ApiServerV2</td>
 <td>ListApis</td>
 <td>Retrieve the API list for a specified product, or perform fuzzy matching of API lists based on API names in Chinese or English, with pagination support</td>
 <td>To be tested</td>
 </tr>
 <tr>
 <td rowspan="1">ApiServerV3</td>
 <td>ShowApi</td>
 <td>Retrieve detailed API information based on product short name, API name, and region ID</td>
                    <td>To be tested</td>
 </tr>
 <tr>
 <td rowspan="1">GroupServer</td>
 <td>ListGroups</td>
 <td>Retrieve all group information for a product based on the product short name</td>
 <td>To be tested</td>
 </tr>
 <tr>
 <td rowspan="1">MockServer</td>
 <td>ShowMockData</td>
 <td>Retrieve mock data based on the example returned by the API in YAML</td>
 <td>To be tested</td>
                </tr>
 <tr>
 <td rowspan="1">ProductServerV4</td>
 <td>ListProductsV4</td>
 <td>Query the list of cloud services</td>
 <td>To be tested</td>
 </tr>
 <tr>
 <td rowspan="1">RegionServerV4</td>
 <td>ListRegionsV4</td>
 <td>- Retrieve the list of regions for which the user has debugging permissions in this API</td>
 <td>To be tested</td>
 </tr>
 </tbody>
 </table>
 </body>
</html>