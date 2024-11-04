# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
from curl_cffi import requests

cookies = {
    'UM_distinctid': '189866efeb61e9c-048ca4abeec9b7-26031c51-1be3a0-189866efeb71b4d',
    'CNZZDATA1281116375': '458383281-1690174605-%7C1690174605',
    '_bl_uid': '50lpXknLgj3gpj3752vUop26b5ym',
    'body_collapsed': '0',
    'ASP.NET_SessionId': 'e22zhqqoshdzd4nybr4lpbzo',
    'FEIGUA': 'UserId=dd0ba33dec0d3a97&NickName=3a3e5e0e7578853c&checksum=bebfde913242&thirdPartyAppId=&thirdPartyUserId=&FEIGUALIMITID=796bda200c324145bbe8d9f70e469748',
    '4d5629a800bfe7fa2f4b6a4468b46fb1': '11c014ebad67002f9ba5bc3a4abd90b68375eb04b5f68bd51de5349731f4e8a9f8c57dcdfa6ca8bb888ed6a44be999db8942ae7143ca9156dacbb96bd98b1cf7cf1dc86a43cdb25f3a6eaf8023a6197a71c2bd4f2353c4ebbeeddb95c41efb109cc30e90f2c045ce8bb192cca34a2835',
    'SaveUserName': '',
    '_uab_collina': '169017766204389332690644',
    'Hm_lvt_876e559e9b273a58993289470c10403b': '1688014803,1690177662',
    'Hm_lpvt_876e559e9b273a58993289470c10403b': '1690177662',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'UM_distinctid=189866efeb61e9c-048ca4abeec9b7-26031c51-1be3a0-189866efeb71b4d; CNZZDATA1281116375=458383281-1690174605-%7C1690174605; _bl_uid=50lpXknLgj3gpj3752vUop26b5ym; body_collapsed=0; ASP.NET_SessionId=e22zhqqoshdzd4nybr4lpbzo; FEIGUA=UserId=dd0ba33dec0d3a97&NickName=3a3e5e0e7578853c&checksum=bebfde913242&thirdPartyAppId=&thirdPartyUserId=&FEIGUALIMITID=796bda200c324145bbe8d9f70e469748; 4d5629a800bfe7fa2f4b6a4468b46fb1=11c014ebad67002f9ba5bc3a4abd90b68375eb04b5f68bd51de5349731f4e8a9f8c57dcdfa6ca8bb888ed6a44be999db8942ae7143ca9156dacbb96bd98b1cf7cf1dc86a43cdb25f3a6eaf8023a6197a71c2bd4f2353c4ebbeeddb95c41efb109cc30e90f2c045ce8bb192cca34a2835; SaveUserName=; _uab_collina=169017766204389332690644; Hm_lvt_876e559e9b273a58993289470c10403b=1688014803,1690177662; Hm_lpvt_876e559e9b273a58993289470c10403b=1690177662',
    'EagleEye-SessionID': 'Omlzekw1g8Rg7qdp0uLmywne6hOR',
    'EagleEye-TraceID': 'de4e6f531690178090560101928902',
    'EagleEye-pAppName': 'hmkt38hcqz@a77d49c22f28902',
    'Pragma': 'no-cache',
    'Referer': 'https://dy.feigua.cn/app/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Brave";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'awemeId': '7256972639133076773',
    'dateCode': '20230718',
    '_': '1690178090553',
}

response = requests.get(
    'https://dy.feigua.cn/api/v1/aweme/detail/portrayalDataV2',
    params=params,
    cookies=cookies,
    headers=headers,
).json()
print(response)
