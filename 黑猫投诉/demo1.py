# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
import execjs
import time


time1 = round(time.time() * 1000)

cookies = {
    'SINAGLOBAL': '175.0.53.237_1693913429.417604',
    'UOR': 'www.google.com.hk,tousu.sina.com.cn,',
    'U_TRS1': '00000034.72d39f16.650a9f78.d69a1814',
    'Apache': '113.246.104.4_1695209487.57988',
    'ULV': '1695209497686:4:4:4:113.246.104.4_1695209487.57988:1695209489253',
    'SCF': 'Al3dGww3PXIN4ToF5BYiiks2n4oUbjeHJC2sgX75pC6YO64v5Td4b1HHKBiVdGUI5pQ7YsgrNpa0TBqa7BNvNeM.',
    'SUB': '_2A25IDqhMDeRhGeBG41AY-CjNzjSIHXVrfZ6ErDV_PUNbm9ANLXSskW9NQfpvXy9PmstgPKS1te1gXjyEycYh99nG',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WWTiHyxhFzE2Bej8S73jGqR5NHD95Qc1hnE1KnceK-RWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNShqEehnpSozNe5tt',
    'ALF': '1697801500',
    'U_TRS2': '00000004.c291428.650ad81d.d9d9557b',
}

headers = {
    'authority': 'hunan.tousu.sina.com.cn',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.5',
    'cache-control': 'no-cache',
    # 'cookie': 'SINAGLOBAL=175.0.53.237_1693913429.417604; UOR=www.google.com.hk,tousu.sina.com.cn,; U_TRS1=00000034.72d39f16.650a9f78.d69a1814; Apache=113.246.104.4_1695209487.57988; ULV=1695209497686:4:4:4:113.246.104.4_1695209487.57988:1695209489253; SCF=Al3dGww3PXIN4ToF5BYiiks2n4oUbjeHJC2sgX75pC6YO64v5Td4b1HHKBiVdGUI5pQ7YsgrNpa0TBqa7BNvNeM.; SUB=_2A25IDqhMDeRhGeBG41AY-CjNzjSIHXVrfZ6ErDV_PUNbm9ANLXSskW9NQfpvXy9PmstgPKS1te1gXjyEycYh99nG; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWTiHyxhFzE2Bej8S73jGqR5NHD95Qc1hnE1KnceK-RWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNShqEehnpSozNe5tt; ALF=1697801500; U_TRS2=00000004.c291428.650ad81d.d9d9557b',
    'pragma': 'no-cache',
    'referer': 'https://hunan.tousu.sina.com.cn/index/search/?keywords=%E5%85%BB%E8%80%81%E9%87%91&t=1',
    'sec-ch-ua': '"Brave";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
keywords = input('输入搜索关键字:')
for page in ran(1, 11):
    sign = execjs.compile(open('./demo1.js', 'r', encoding='utf-8').read()).call('main123', keywords, time1)
    print(sign)
    params = {
        'ts': time1,
        'rs': sign['p'],
        'signature': sign['sign'],
        'keywords': keywords,
        'page_size': '10',
        'page': i,
    }
    print(params)
    response = requests.get('https://hunan.tousu.sina.com.cn/api/index/s', params=params, cookies=cookies,
                            headers=headers)
    print(response.json())