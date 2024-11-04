import time
import execjs
from curl_cffi import requests


headers = {
    # "authority": "u.y.qq.com",
    # "accept": "application/json",
    # "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    # "cache-control": "no-cache",
    # "content-type": "application/x-www-form-urlencoded",
    # "origin": "https://y.qq.com",
    # "pragma": "no-cache",
    # "referer": "https://y.qq.com/",
    # "sec-ch-ua": "^\\^Not_A",
    # "sec-ch-ua-mobile": "?0",
    # "sec-ch-ua-platform": "^\\^Windows^^",
    # "sec-fetch-dest": "empty",
    # "sec-fetch-mode": "cors",
    # "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
}
url = "https://u.y.qq.com/cgi-bin/musics.fcg"
timestamp =str(int(time.time()*1000))
data = {
    "comm": {
        "cv": 4747474,
        "ct": 24,
        "format": "json",
        "inCharset": "utf-8",
        "outCharset": "utf-8",
        "notice": 0,
        "platform": "yqq.json",
        "needNewCode": 1,
        "uin": 0,
        "g_tk_new_20200303": 5381,
        "g_tk": 5381
    },
    "req_1": {
        "module": "musicToplist.ToplistInfoServer",
        "method": "GetDetail",
        "param": {
            "topid": 4,
            "offset": 0,
            "num": 20,
            "period": "2023-12-22"
        }
    }
}
js_code = open('./demo.js','r',encoding='utf-8').read()
sign =execjs.compile(js_code).call('get_sign',data)
params = {
    "_": timestamp,
    "sign": sign
}
response = requests.post(url, headers=headers, params=params, json=data)

print(response.text)
print(response)
