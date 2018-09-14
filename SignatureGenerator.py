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
    url_resource_part = 'vehicle-alarm/internal/electricHistory/getElectricHistories'
    secret_key = '94a7cbbf8511a288d22d4cf8705d61d0'
    signt = int(time.time()*1000)
    url = "http://jmcuat.jmc.com.cn/"
    # params_map = {
    #     'vin': 'JMCGONGPEN330PHEV',
    #     'startTime': '2018-08-20',
    #     'endTime': '2018-08-21',
    #     'pageIndex': '1',
    #     'pageSize': '20',
    #     'signt':'1534840780000',
    #     #'token': 'vc-server-admin---amZYRk9JODdUWjBwNVlCWHFkdVJkWi91NTJLNk1tY05RWTkrQzZMelMrQThZQWZRNFBHMjdTL2tOY3lDMmJqVlpBbkkzWXpOdUxTRwpXeGZIeUlIdGlRPT0-___1521077726387___2___2___bHs0NMLA4yA60TE3___2',
    #     'appkey': '5732477868'
    # }
    params_map = {
        "appkey":"5732477868",
        'signt':str(signt)
    }
    json = {
        "vins":"JMCGONGPEN330PHEV"
    }
    sign = SignatureGenerator.generate(url_resource_part, params_map)
    print(sign)
    params_map.update(sign=sign)
    headers = {
        "ContentType":"application/x-www-form-urlencoded"
    }
    result = requests.post(url=url+url_resource_part,params=params_map,data=json)
    print(result.url)
    print(result.text)