# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
import execjs


with open('demo1.js', 'r', encoding='utf-8') as f:
    script = f.read()

ctx = execjs.compile(script).call('main123')
print(ctx)


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://www.birdreport.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://www.birdreport.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'requestId': ctx['requestId'],
    'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sign': ctx['sign'],
    'timestamp': str(ctx['timestamp']),
}

data = ctx['data']

response = requests.post('https://api.birdreport.cn/front/record/activity/search', headers=headers, data=data).json()
encrypt = response['data']
ctx1 = execjs.compile(script).call('decrypt', encrypt)  # 返回内为字符串
print(ctx1)