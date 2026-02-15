# Anti-DDoS MCP Server 


## Version
v0.1.0

## Overview

Anti-DDoS MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service Anti-DDoS. Full-chain management of Anti-DDoS resources can be carried out based on natural language.

## Available Tools
Cover all APIs, use as needed, the list and status are as follows:

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
                    <td rowspan="1">DDoS Task Management</td>
                    <td>ShowNewTaskStatus</td>
                    <td>Users can query the specified Anti-DDoS protection configuration task to obtain the current execution status of the task. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="12">DDoS Protection Management</td>
                    <td>ShowLogConfig</td>
                    <td>Query full log settings</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDailyLog</td>
                    <td>Query abnormal event information for the specified EIP within the past 24 hours. Abnormal events include cleaning events and blackhole events. The query latency is within 5 minutes. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateLogConfig</td>
                    <td>Update user full log settings</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDDosStatus</td>
                    <td>Query the Anti-DDoS protection status of a specified EIP.</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDDosStatus</td>
                    <td>Query the Anti-DDoS protection status information for all user EIPs. The user's EIPs can be queried regardless of whether they are bound to cloud servers. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>EnableDefensePolicy</td>
                    <td>Enable DDoS service</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNewConfigs</td>
                    <td>Query the available range of Anti-DDoS protection policy configurations supported by the system. Users can select the appropriate protection policy from the list to perform Anti-DDoS traffic cleaning based on their business needs. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListWeeklyReports</td>
                    <td>Query the weekly statistics of all Anti-DDoS protection for users, including the number of DDoS interceptions and attacks within a week, as well as ranking information based on the number of attacks. The system supports querying weekly statistics for the past four weeks prior to the current time. Requests exceeding this timeframe will not be able to retrieve statistical data. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListDailyReport</td>
                    <td>Query the protection traffic information for the specified EIP within the past 24 hours, with a traffic interval of 5 minutes. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDDos</td>
                    <td>Query the configured Anti-DDoS protection strategy. Users can query the Anti-DDoS protection strategy for a specified EIP. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListQuota</td>
                    <td>Query the quota</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateDDos</td>
                    <td>Update the Anti-DDoS protection strategy configuration for a specified EIP. A successful call only indicates that the service node has received the request to close the update configuration. To determine whether the operation was successful, you need to query the execution status of the task through the task query interface. For details, please refer to Query Anti-DDoS Tasks. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="2">Alert Configuration Management</td>
                    <td>ShowAlertConfig</td>
                    <td>Query user configuration information. Users can use this interface to query whether to receive certain types of alerts and configure whether to receive alert information via SMS or email. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateAlertConfig</td>
                    <td>Update user configuration information. Users can use this interface to update whether to receive certain types of alerts and configure whether to receive alert information via SMS or email. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="3">Default Protection Policy Management</td>
                    <td>DeleteDefaultConfig</td>
                    <td>Delete the user's default protection policy configuration. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowDefaultConfig</td>
                    <td>Query the user's default protection policy configuration. </td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateDefaultConfig</td>
                    <td>Configure the user's default protection policy. After configuring the protection policy, newly purchased resources will be configured according to this default protection policy when protection is automatically enabled. </td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
