#!/bin/bash

# 拉取数据
REPO_ROOT = "/home/ubuntu/service/spider_monitor_api"
cd $REPO_ROOT
git pull origin master

# Kill Process
ps -ef | grep api\_main\.py | awk {'print $2'} | xargs kill -s 9
ps -ef | grep hook\_.py | awk {'print $2'} | xargs kill -s 9

# Start Process
nohup python3 ./api_main.py >> api_main.log &
nohup python3 ./extra/hook.py >> hook.log &
