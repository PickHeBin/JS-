# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
import execjs

cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1692768630,1692792114,1693739476,1694503460',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1694503460',
}
EncKey = execjs.compile(open('./demo1.js', 'r', encoding='utf-8').read()).call('getResCode')
headers = {
    'Accept': '*/*',
    'Accept-EncKey': EncKey,
    'Accept-Language': 'zh-CN,zh;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1692768630,1692792114,1693739476,1694503460; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1694503460',
    'Origin': 'http://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://webapi.cninfo.com.cn/',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'tdate': '2023-09-11',
    'market': 'SZE',
}

response = requests.post(
    'http://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
).text
print(response)