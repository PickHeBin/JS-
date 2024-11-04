# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
import execjs

cookies = {
    'the_codes': '440001',
    'the_codesIndex': '%E7%9C%81%E6%9C%AC%E7%BA%A7',
    'cityOrArea': '',
}

jscode = open('./demo1.js', 'r', encoding='utf-8').read()
sign = execjs.compile(jscode).call('signReturn')
nsssjss = execjs.compile(jscode).call('RSAReturn')

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=utf-8',
    # 'Cookie': 'the_codes=440001; the_codesIndex=%E7%9C%81%E6%9C%AC%E7%BA%A7; cityOrArea=',
    'Pragma': 'no-cache',
    'Referer': 'https://gdgpo.czt.gd.gov.cn/cms-gd/site/guangdong/tzgg/index.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    # RSA
    'nsssjss': nsssjss,
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': sign, # 消息摘要
    'time': '1710769556677',
    'url': '/freecms/rest/v1/notice/selectInfoMoreChannel.do',
}

response = requests.get(
    'https://gdgpo.czt.gd.gov.cn/freecms/rest/v1/notice/selectInfoMoreChannel.do?&siteId=cd64e06a-21a7-4620-aebc-0576bab7e07a&channel=5b3bf6bc-011e-4211-b320-f8d5c2290872&currPage=2&pageSize=10&regionCode=440001&operationStartTime=&operationEndTime=2024-03-18%2023:59:59&title=&cityOrArea=&selectTimeName=noticeTime',
    cookies=cookies,
    headers=headers,
).json()
print(response)