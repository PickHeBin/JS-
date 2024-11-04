# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
import execjs
import json


cookies = {
    'cngizm2ziytq3mwy': 'J9584VSqCF7xUFitAEO9TUW9HUC0F062EUzjEkWdbTHPPzPNUg==',
    'fogq4n2exnzc0otg': 'AgEDPgcEBFoEV1xYXlpRWVpYRxBFTBAXEUdERhscHhwbS3UjDw==',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'cngizm2ziytq3mwy=J9584VSqCF7xUFitAEO9TUW9HUC0F062EUzjEkWdbTHPPzPNUg==; fogq4n2exnzc0otg=AgEDPgcEBFoEV1xYXlpRWVpYRxBFTBAXEUdERhscHhwbS3UjDw==',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'en2uwnjgxodjhogi': '1',
    'rdmje1ymjkyzrknj': 'CgYHOR5KDBACGgwXAigOBxxWQFQ6EQERERVhb28vNWh/ZxAjJiAgODJufnwzIzQhJz0pHjs/Nzw4fxUAYkBOSUIGBgRIXEdHQ39aVx8KFF5QAgALWVYOXVVYYDc1ZW42Z2w8OTJtO2A5aHomdH0gNTU2eXd3b3JtQ3mHwdfChNOGhoGJjNzZidmKkM2SwsLBl86eycDKz5Gbn/fxpPnl6+ugr7C9pqyiv+Lptby8pb/597KsvbqrnL21wcXizt7I0IqRmdhS',
    'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'xhnjc3odeyndrhmj': 'AwYIOT0qJCgQER87AxsbBhoHPA==',
}

jscode = open('./demo1.js', 'r', encoding='utf-8').read()
# 分页参数
param = execjs.compile(jscode).call('main123', 3)

params = {
    'qmze1yzvhyzcyyjr': param,
}

response = requests.get(
    'https://adworld.xctf.org.cn/api/event/release_event/list/',
    params=params,
    cookies=cookies,
    headers=headers,
).text

data1 = execjs.compile(jscode).call('_0x354c5e', response)
data_list = json.loads(data1)['data']['rows']
for data in data_list:
    print(data['release_name'],data['release_sponsor'])
