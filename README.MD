# spider_monitor_api

## Basic Info
Author | CreateDate | ProjectName | ChineseName
--- | --- | --- | ---
TauWoo | 2018-05-03 | spider_monitor_api | 基于Flask的爬虫数据监控API

## BaseURL
http://0.0.0.0:20000/

## Handlers
### MENU
- [Test Handlers](https://github.com/TauWu/spider_monitor_api#test-handlers)
    - [Test Page](https://github.com/TauWu/spider_monitor_api#test-page)
- [Lianjia Spider Handlers](https://github.com/TauWu/spider_monitor_api#lianjia-spider-handlers)
    - [CMD Handlers](https://github.com/TauWu/spider_monitor_api#cmd-handlers)
    - [Count Handlers](https://github.com/TauWu/spider_monitor_api#count-handlers)
    - [List Handlers](https://github.com/TauWu/spider_monitor_api#list-handlers)
    - [Detail Handlers](https://github.com/TauWu/spider_monitor_api#detail-handlers)

### Test Handlers
#### Test Page
- [x] 1.test
> `GET` 测试接口，用于测试服务是否跑通，返回指定日期的指定日出日落时间
```py
req_url = "http://0.0.0.0:20000/test?date=2018-01-01"
resp >> test.html
```

### Lianjia Spider Handlers
#### CMD Handlers
- [ ] 1.spider/lianjia/cmd_spider
> `GET` 监控链家爬虫程序进程运行情况
```py
req_url = "http://0.0.0.0:20000/spider/lianjia/cmd_spider?proc_name=spider_lianjia"
resp_data = {

}
```
#### Count Handlers
- [ ] 2.spider/lianjia/count_spider_create
> `GET` 监控链家爬虫程序进程运行情况
```py
req_url = "http://0.0.0.0:20000/spider/lianjia/count_spider_create?date=2018-04-04"
resp_data = {

}
```
- [ ] 3.spider/lianjia/count_spider_page
> `GET` 监控链家爬虫程序进程运行情况
```py
req_url = "http://0.0.0.0:20000/spider/lianjia/count_spider_page?date=2018-04-04"
resp_data = {

}
```
- [ ] 4.spider/lianjia/count_spider_stat
> `GET` 监控链家爬虫程序进程运行情况
```py
req_url = "http://0.0.0.0:20000/spider/lianjia/count_spider_stat?date=2018-04-04"
resp_data = {

}
```
- [ ] 5.spider/lianjia/count_spider
> `GET` 监控链家爬虫程序进程运行情况
```py
req_url = "http://0.0.0.0:20000/spider/lianjia/count_spider?date=2018-04-04"
resp_data = {

}
```

#### List Handlers

#### Detail Handlers



## 软件依赖
```bash
# 安装 Python3 和 pip
apt-get install python3
apt-get install python3-pip

# 安装依赖库
pip3 install flask
pip3 install PyMySQL

```