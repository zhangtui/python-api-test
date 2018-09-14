#-*- coding: UTF-8 -*-
import requests
def myRequest(method,url,datas,auth=None):
    # 处理请求数据为空的情况
    if datas is not None:
        datas = eval(datas)
    if method == "get":
        # 如果datas 返回的是一个字符串，则需要添加转换成字典，eval()
        result = requests.request(method,url,params=datas,auth=auth)
    elif method == "post":
        result = requests.request(method,url,params=datas,data=datas,auth=auth)
        requests.post(url=url,)
    else:
        result = None
    return result