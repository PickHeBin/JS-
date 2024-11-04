import requests
import execjs




headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "rdmje1ymjkyzrknj": "AAMGPB5FAxQNERAEGTgVGAxJV0g1GgUaGhVSWF8QClxAXCwQLSArNzJhaWAsOCA6PC06CTswODg3dGlzGTA1NjJ5cXhHV0NMSH9JQA8VCxcaHE0ZVVENCAYCDFAJDQZYXgsPWjcwNDQ6YmVjO21tKiUpbmt4ZHZmSHl0Nic9eyd5fX16h9zShtmFh9GN2dbajN6N3sDFwJWUlMvCn8ne1Nuei5+otoSprqOrh6K6p7ro9Pr4//awtaenur2yqf3nubm0r8DaZw==",
    "xhnjc3odeyndrhmj": "CAgHNz0pJC4VGxMwFw0KFAoMOA=="
}
cookies = {
    "cngizm2ziytq3mwy": "Gslp9gDWIQeAIGu9TGi4EW25RjLnQ2GzETH/BC+qAHz5An+gfA==",
    "fogq4n2exnzc0otg": "AQoKNVVUXgIJDFJVBQ9WUQwCVURMSUYeTBBBTkxHFxsRE0x/Ug=="
}
url = "https://adworld.xctf.org.cn/api/event/release_event/list/"

with open("返回数据加密解析.js",encoding='utf-8')as f:
    js_code = f.read()

js = execjs.compile(js_code)
params = js.call('enc', 2)
data = {
    'qmze1yzvhyzcyyjr' : params
}
print(data)
response = requests.get(url, headers=headers, cookies=cookies, json=data).text
# data_list = response['data']['rows']
datas = js.call('dec',response)
data_list = datas['data']['rows']
for data in data_list:
    print(data['release_name'],data['release_sponsor'])
