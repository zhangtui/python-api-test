#-*- coding: UTF-8 -*-
from common import MyExcel
import time
from common.SignatureGenerator import *
from common.read_config import read_config
import requests
import configparser
# 1、从excel 表中读取需要算签名数据
filePath = "E:\\PycharmProjects\\python-api\\TestDatas\\TestData.xlsx"
me = MyExcel.MyExcel(filePath)
caseDatas = me.get_all_testDatas()
print(len(caseDatas))
appkey = read_config().read_config("common.conf", "http", "app_key")
for i in range(0,len(caseDatas)):
    params_map =eval(caseDatas[i]["request_data"])
    url = caseDatas[i]["url"]
    signt = str(int(time.time() * 1000))
    params_map.update(signt=signt,appkey=appkey)
    sign = SignatureGenerator.generate(url, params_map)
    params_map.update(sign=sign)
    caseDatas[i]["request_data"] = str(params_map)
    caseDatas[i]["url"] = read_config().read_config("common.conf", "http", "server_ip")+url
print(caseDatas[1]["expected_data"])
# param_map=eval(caseDatas[0]["request_data"])
# url = caseDatas[0]["url"]
# print(param_map)
print(url)
# 2.进行更新param数据中得signt
# signt =str(int(time.time()*1000))
# param_map.update(signt=signt)
# print(param_map)
#
# # 3、进行签名加密
# sign = SignatureGenerator.generate(url, param_map)
# print(sign)
#
# # 4、更新param_map 字典中得参数
#
# param_map.update(sign=sign)
# print(param_map)
# # 5、gei请求
#
# # 读取配置文件中得ip
# config=configparser.ConfigParser()
# config.read("common.conf")
# urls="http://"+config.get("http","server_ip")+"/"+url
# print(urls)
#
#
# request = requests.get(url=urls,params=param_map)
# result =request.content
# print(request.url)
# print(result)
