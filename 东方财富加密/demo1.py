# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
import re
import execjs

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://guba.eastmoney.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'type': '0',
    'sort': '0',
    'page': '3',
    'v': '2023_12_21_17_12',
}

response = requests.get('https://gbcdn.dfcfw.com/rank/popularityList.js', params=params, headers=headers).text
popularityList = re.findall("popularityList='(.*?)'", response)[0]
scriptData = execjs.compile(open('./demo1.js', 'r', encoding='utf-8').read()).call('main123', popularityList)
for i in scriptData:
    print(i)

