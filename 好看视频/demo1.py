# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests
import execjs
import time

cookies = {
    'BDUSS': '1zcklpUVlxUU9vaGkwU2d5RzQ4aHlOU05WbWF1bHdsM1RpZzJLR2RkVlVTUGxsSVFBQUFBJCQAAAAAAQAAAAEAAABTuIQaYm9iaW41NTUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFS70WVUu9FlY2',
    'BAIDUID': 'B0E85072366C9669CCF54CCA4B3A0CB5:FG=1',
    'BAIDUID_BFESS': 'B0E85072366C9669CCF54CCA4B3A0CB5:FG=1',
    'BDUSS_BFESS': '1zcklpUVlxUU9vaGkwU2d5RzQ4aHlOU05WbWF1bHdsM1RpZzJLR2RkVlVTUGxsSVFBQUFBJCQAAAAAAQAAAAEAAABTuIQaYm9iaW41NTUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFS70WVUu9FlY2',
    'Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5': '1708266632,1708319261',
    'Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5': '1708323187',
    'ab_sr': '1.0.1_OWQ1MDZhZTM3MmI0ZDEyYzJhOWY1NzY4ODcwOWQ1OGZlZTdkOTg2ODRkMTI0OWJhY2RhZTVhNjk2MmMxMTg1OWFkZmMzMWJkYTEwZjNlMjcyMDIwODE4NmE2MWM4OWFkODM2NTM4NmYyODVhMzFhY2VmMmU2NWYzM2E3MDk3MzE4NThhNDg2OTU4YWEzMzM5ODRlZmFhMTg0MmM1ZDBjZQ==',
    'reptileData': '%7B%22data%22%3A%22aff36232f47d1f215fe5517c3b19cfc87dec1e1ecd37332f84671456081754dc5d37b5f27728271216dcd970ebb356801b33562e0c35fc376df6175919732383d36257dcc351c2d42d56fd839ec1142d8da8f0b65cfe708fd71593462ccc4198%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22eb733ab9%22%7D',
}

headers = {
    'authority': 'haokan.baidu.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'BDUSS=1zcklpUVlxUU9vaGkwU2d5RzQ4aHlOU05WbWF1bHdsM1RpZzJLR2RkVlVTUGxsSVFBQUFBJCQAAAAAAQAAAAEAAABTuIQaYm9iaW41NTUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFS70WVUu9FlY2; BAIDUID=B0E85072366C9669CCF54CCA4B3A0CB5:FG=1; BAIDUID_BFESS=B0E85072366C9669CCF54CCA4B3A0CB5:FG=1; BDUSS_BFESS=1zcklpUVlxUU9vaGkwU2d5RzQ4aHlOU05WbWF1bHdsM1RpZzJLR2RkVlVTUGxsSVFBQUFBJCQAAAAAAQAAAAEAAABTuIQaYm9iaW41NTUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFS70WVUu9FlY2; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1708266632,1708319261; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1708323187; ab_sr=1.0.1_OWQ1MDZhZTM3MmI0ZDEyYzJhOWY1NzY4ODcwOWQ1OGZlZTdkOTg2ODRkMTI0OWJhY2RhZTVhNjk2MmMxMTg1OWFkZmMzMWJkYTEwZjNlMjcyMDIwODE4NmE2MWM4OWFkODM2NTM4NmYyODVhMzFhY2VmMmU2NWYzM2E3MDk3MzE4NThhNDg2OTU4YWEzMzM5ODRlZmFhMTg0MmM1ZDBjZQ==; reptileData=%7B%22data%22%3A%22aff36232f47d1f215fe5517c3b19cfc87dec1e1ecd37332f84671456081754dc5d37b5f27728271216dcd970ebb356801b33562e0c35fc376df6175919732383d36257dcc351c2d42d56fd839ec1142d8da8f0b65cfe708fd71593462ccc4198%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22eb733ab9%22%7D',
    'pragma': 'no-cache',
    'referer': 'https://haokan.baidu.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}
time1 = round(time.time() * 1000) - 2000
para = {}
para['time'] = time1
para = execjs.compile(open('./demo2.js', 'r', encoding='utf-8').read()).call('getSignedParams', time1)
print(para)

response = requests.get('https://haokan.baidu.com/haokan/ui-web/video/feed', params=para, cookies=cookies, headers=headers).json()
for i in response['data']['apiData']:
    title = i['title']
    previewUrlHttp = i['previewUrlHttp']
    print(title, previewUrlHttp)

