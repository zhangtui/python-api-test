#!/usr/bin/env python
# coding=utf-8

"""
              ┏┓    ┏┓
            ┏━┛┻━━━━┛┻━┓
            ┃     ☃    ┃
            ┃   ┳┛ ┗┳  ┃
            ┃     ┻    ┃
            ┗━┓      ┏━┛
              ┃      ┗━━━┓
              ┃  神兽保佑 ┣┓
              ┃　永无BUG！┏┛
              ┗┓┓┏━━━━┳┓┏┛
               ┃┫┫    ┃┫┫
               ┗┻┛    ┗┻┛
"""

from urllib import parse
import hashlib


class SignatureGenerator:

    def __init__(self):
        self.mark = '签名生成类'

    '''
    签名方法
    注意：当参数中有空格时，会造成编码不一致；
    '''
    @staticmethod
    def generate(url_resource_part, params_map, secret_key="94a7cbbf8511a288d22d4cf8705d61d0"):
        # 1. URL参数排序
        keys = list(params_map.keys())
        keys.sort()

        # 2. 拼接字符串
        str = url_resource_part + '_'
        for key in keys:
            str += key + '=' + params_map[key] + '_'
        str += secret_key
        # 3. url编码
        encodeStr = parse.quote_plus(str)
        ''' 
        处理“/”编码的问题 
        Java会将“/”编码为“%2F”，Python不会编码
        '''
        # encodeStr = encodeStr.replace('/', '%2F')

        # 4. md5加密
        '''
        md5 = hashlib.md5()
        md5.update(encodeStr.encode(encoding='utf8'))
        md5Str = md5.hexdigest()
        '''
        md5Str = hashlib.new('md5', encodeStr.encode(encoding='utf8')).hexdigest()

        return md5Str



if __name__ == '__main__':
    import time
    import requests
    secret_key = '94a7cbbf8511a288d22d4cf8705d61d0'
    signt = int(time.time()*1000)
    # url = "https://jmhuat.landwind.com/"
    url = "https://jmhext.landwind.com/"
    # url_resource_part = 'update-center/checkVersion'
    # url_resource_part = 'vehicle-customer/auth/checkAvn'
    url_resource_part = 'update-center/reportUpdateResult'
    # 服务站同步接口
    url_resource_part = 'tdata-sync/internal/syncDealer/importServiceStationInfo'
    params_map = {
        "appkey": "5732477868",
        'signt': str(signt)
    }
    json =[
        {"serviceName": "威信县利达汽修厂", "province": "云南省", "city": "昭通市", "servicePhone": "13887084598",
         "hotLine": "13887097133", "county": "威信县", "longitude": "80", "latitude": "80", "serviceCode": "23242091_01",
         "address": "云南省昭通市威信县扎西镇石龙村黄粉厂旁", "stationStatus": "ALREADY_OPENED", "createdTime": int(time.time() * 1000),
         "status": "1"}
    ]
    sign = SignatureGenerator.generate(url_resource_part, params_map)
    params_map.update(sign=sign)
    print(params_map)
    headers = {
        "ContentType":"application/json",
        # "accept-encoding:":"gzip",
        # "user-agent":"okhttp/3.2.0"
    }
    # result = requests.post(url=url+url_resource_part,params=params_map,json=json)
    # print(result.url)
    # print(result.text)