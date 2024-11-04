"""
案例网址：https://zc-paimai.taobao.com/wow/pm/default/pc/4b80fa?&scm=20140647.julang.pm.sem&a_keywordid=408409593247&bd_vid=8230115899146061516&page=2

逆向参数：sign

分析过程：

    1.页面有翻页，将开发者工具调到XHR，翻两页，出现两个接口
    2.对比发现请求参数，时间戳和sign是变化的，搜索关键词sign: 进入js文件，发现sign是p生成的
    3.往上翻找到p生成的位置，扣进js代码里来
    4.将一些参数补进来，a是时间戳
    5.在p前面先断点，重新翻页，获取s的值，s是appKey，固定的值
    6.在n.data前面下断点，释放程序，获取n.data的值，发现就是请求参数
    7.运行程序，提示token is not defined p函数是自调用函数，将参数怼到console.log()里
    8.执行无问题，写python代码


反思：
    p是自调用函数，参数没有扣进来，win7的谷歌无法折叠代码

"""

import requests
import execjs
import time

# 时间戳
a = int(time.time() * 1000)


# 请求头
headers = {
    "cookie": "cna=3mN4HauA7XACAXLmoD1az/Jj; t=00866fe420ee7fb83c28eb6a26259162; _m_h5_tk=f266b0f771458772683c07d2e9b3afcf_1693556390869; _m_h5_tk_enc=62fb7e46282683d26a3ebf4a688eee3d; xlly_s=1; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; _uetsid=1c34d3e0488b11eeb2337b132e42795a; _uetvid=1c3543f0488b11ee8a395f24fa5ee876; _gid=GA1.2.1126030714.1693547281; _ga_JBTWV3NHSY=GS1.1.1693547281.1.0.1693547281.60.0.0; _ga=GA1.1.507794041.1693547280; _ga_YFVFB9JLVB=GS1.1.1693547280.1.0.1693547282.0.0.0; tfstk=d9NkJ3Mvk8kSjCzhxQh5ZSOKW5XvP3GISkdKvXnF3moXJ7Ur9Xf3Dk4-LDB7xvqLcvP-wzEDYozs4DU-a2A3jkv-9Dhz8Dmq7wtETwGHPSqM9QI5FyRn9XSOX1CTP4GITGneEdHWRXx9aZUG6zaSOUxFW-5t-Y5P0GoenMZBFS-jdcYLvNP9sFJ_WzoDsrNmzInP1cRECSuSEWWicOWD3d-4KBgVJSJBdYujocCJE1ZF.; l=fBPlC1pPNtcdqL_aBO5anurza77t4BAf5sPzaNbMiIEGC6edNYpGn5-Q2TGzFKtRR8XPiTTB45k_ZiptNeqU-y8XiCxiGjFUtiT9CeTIK7Nk_; isg=BBQUy5kPDDahLZj6Kzgc9goF5VKGbThXTcL4FK7z9xyxmb3j1nxy5sJfmZEBYXCv",
    "referer": "https://zc-paimai.taobao.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

# 接口网址
url = "https://h5api.m.taobao.com/h5/mtop.taobao.datafront.invoke.auctionwalle/1.0/"

# 请求参数
data = {
    "data": "{\"dfApp\":\"auctionwalle\",\"dfApiName\":\"auctionwalle.datou.getPageModulesData\",\"dfVariables\":\"{\\\"pageId\\\":1410667,\\\"moduleIds\\\":\\\"9018433170:items\\\",\\\"context\\\":{\\\"_b_9018433170:items\\\":\\\"{\\\\\\\"scm\\\\\\\":\\\\\\\"20140647.julang.pm.sem\\\\\\\",\\\\\\\"a_keywordid\\\\\\\":\\\\\\\"408409593247\\\\\\\",\\\\\\\"bd_vid\\\\\\\":\\\\\\\"8230115899146061516\\\\\\\",\\\\\\\"page\\\\\\\":\\\\\\\"4\\\\\\\",\\\\\\\"userInfo\\\\\\\":{},\\\\\\\"appendMap\\\\\\\":{\\\\\\\"sid\\\\\\\":\\\\\\\"5320375177_1693550180876\\\\\\\"}}\\\",\\\"userInfo\\\":\\\"{}\\\",\\\"device\\\":\\\"pc\\\",\\\"sceneCode\\\":\\\"20200713C5R32B6N\\\"}}\",\"dfUniqueId\":\"1410667.9018433170:items\",\"dfVariablesRecover\":\"{}\"}"
}
token = "f266b0f771458772683c07d2e9b3afcf"
data123  = token + "&" + str(a) + "&" + s + "&" + str(data)

# 读取文件
with open('./alfc.js', mode='r', encoding='utf-8') as f:
    js_code = f.read()

obj = execjs.compile(js_code)
sign = obj.call('sign', data)
print(sign)

params = {
    "jsv": "2.6.1",
    "appKey": "12574478",
    "t": a,
    "sign": sign,
    "bxPageId": "1410667",
    "api": "mtop.taobao.datafront.invoke.auctionwalle",
    "v": "1.0",
    "type": "originaljson",
    "dataType": "json",
    "requiredParams": "dfApiName,dfUniqueId"
}

response = requests.post(url, headers=headers, params=params, data=data)

print(response.text)
