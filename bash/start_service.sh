#!/bin/bash

# 拉取数据
cd /home/ubuntu/service/spider_monitor_api

# Kill Process
ps -ef | grep api\_main\.py | awk {'print $2'} | xargs kill -s 9

# Start Process
nohup /usr/bin/python3 ./api_main.py >> /home/ubuntu/service/spider_monitor_api/api_main.log &