#!/bin/bash

REPO_DIR="/home/ubuntu/service/spider_monitor_api"

# 切换目录
cd $REPO_DIR

# Kill Process
ps -ef | grep api\_main\.py | awk {'print $2'} | xargs kill -s 9

# Start Process
/usr/bin/python3 $REPO_DIR/api_main.py >> $REPO_DIR/api_main.log