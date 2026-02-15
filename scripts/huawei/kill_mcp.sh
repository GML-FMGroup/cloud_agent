#!/bin/bash

KEYWORD="huaweicloud_services_server.mcp_server"

PIDS=$(ps aux | grep "$KEYWORD" | grep -v grep | awk '{print $2}')

if [ -z "$PIDS" ]; then
    echo "No matching process found."
else
    echo "Killing processes: $PIDS"
    kill -9 $PIDS
    echo "Done."
fi
