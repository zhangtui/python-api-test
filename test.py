#-*- coding: UTF-8 -*-
import hashlib
from urllib import parse
import time
import requests
# url = "http://jmcuat.jmc.com.cn/vehicle-alarm/internal/alarmHistory/getAlarmHistoryPageCondition?"
# a = "vehicle-alarm/internal/alarmHistory/getAlarmHistoryPageCondition"
# signt = int(time.time()*1000)
# print(signt)
# secretkey="94a7cbbf8511a288d22d4cf8705d61d0"
# datas = {"appkey":"5732477868","vin":"JMCGONGPEN330PHEV","pageIndex":"1","pageSize":"20","signt":""}
# datas["signt"]= str(signt)
# listdata = list(datas.items())
# listdats=[]
# for i in listdata:
#     strdata=("=").join(i)
#     listdats.append(strdata)
# listdats.sort()
# listdats.insert(0,a)
# listdats.append(secretkey)
# print(listdats)
# strdatas =("_").join(listdats)
# print(strdatas)
# dat = parse.quote_plus(strdatas,encoding="utf-8")
# print(dat)
# s = map(int, dat)
# for x in range(0,100):
#     n =s[x]
#     print(n)
# print(s)
# sign= hashlib.md5(strdatas.encode('utf-8'))
# print(sign)
# signs = sign.hexdigest()
#
# print(signs)
# signs1=int(len(signs)/2)
# print(signs1)
#
# # urldata = {"appkey":"5732477868","vin":"JMCGONGPEN330PHEV","pageIndex":"1","pageSize":"20","signt":"","sign":""}
# # urldata["signt"]= str(signt)
# # urldata["sign"]= str(signs)
# # print(urldata)
# #
# # request = requests.get(url=url,params=urldata)
# # result =request.content
# # print(request.url)
# # print(result)


import http.client

conn = http.client.HTTPConnection("jmhuat,landwind,com")

payload = "avnSn=22222&appId=AVN001&vin=LVDDB6666666666BD"

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    }

conn.request("POST", "vehicle-customer,auth,checkAvn", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))