#!/usr/bin/python3
# -*- coding: utf-8 -*-

from util.common.config import ConfigParser

def default_config(key, value):
    return key

def get_config():

    print("开始配置数据库连接...")
    # 数据库配置
    idx = 0
    while True:
        flag = input("添加数据库信息？(Y/N)")
        if flag == "Y":
            idx += 1
            print("开始配置数据库%d..."%idx)
            db_host = input("请输入数据库的host（跳过为localhost）")
            db_user = input("请输入数据库的user（跳过为root）")
            db_port = input("请输入数据库的端口（跳过为3306）")
            db_pwd = input("请输入数据库的pwd（跳过为root）")
            db_db = input("请输入数据库的数据库名（跳过为spider_db）")

            if len(db_host) == 0:
                db_host = "127.0.0.1"
            if len(db_user) == 0:
                db_user = "root"
            if len(db_pwd) == 0:
                db_pwd = "root"
            if len(db_db) == 0:
                db_db = "spider_db"
            if len(db_port) == 0:
                db_port = "3306"
            
            yield {
                "db%d"%idx:dict(
                    host=db_host, user=db_user, passwd=db_pwd, db=db_db, port=db_port
            )}
        else:
            break
            
    # Redis配置
    idx = 0
    print("开始配置Redis连接...")
    while True:
        idx += 1
        flag = input("添加Redis信息？(Y/N)")
        if flag == "Y":
            print("开始配置Redis%d...", idx)
            redis_host = input("请输入Redis的host（跳过为localhost）")
            if len(redis_host) == 0:
                redis_host = "127.0.0.1"
            redis_port = input("请输入Redis端口号（跳过为6379）")
            if len(redis_port) == 0:
                redis_port = "6379"
            redis_port = int(redis_port)
            redis_db = input("请输入Redis的数据库名称（跳过为0）")
            if len(redis_db) == 0:
                redis_db = "0"

            yield {
                "rds%d"%idx: dict(
                    host=redis_host, port=redis_port, db=redis_db
            )}
        else:
            break

    # HTTP请求配置
    idx = 0
    print("开始配置HTTP API...")
    while True:
        idx += 1
        print("开始配置HTTP API%d..."%idx)
        flag = input("添加HTTP API信息？(Y/N)")
        if flag == "Y":
            http_host = input("请输入HTTP请求的URL（跳过为http://0.0.0.0）")
            if len(http_host) == 0:
                http_host = "http://0.0.0.0"
            http_port = input("请输入HTTP API端口号（跳过为80）")
            if len(http_port) == 0:
                http_port = "80"
            http_port = int(http_port)
            http_handler = input("请输入HTTP API的Handler（跳过为/）")
            if len(http_handler) == 0:
                http_handler = ""
            http_method = input("请输入HTTP API的请求方式（跳过为GET）")
            if len(http_method) == 0:
                http_method = "GET"

            yield {
                "api%d"%idx: dict(
                    url="%s:%d/%s"%(http_host, http_port, http_handler), method=http_method
            )}
        else:
            break
    
if __name__ == "__main__":
    # 配置文件基础
    cp = ConfigParser(config_file="base.cfg")
    config_dicts = get_config()

    for config_dict in config_dicts:
        # 填写配置文件
        for k in config_dict.keys():
            cp.add_section(k)
            for k_inner in config_dict[k]:
                cp.set_kv(k_inner, config_dict[k][k_inner])