# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo123.py
# @Project  : pythonProject2
import requests


# 直接排除
cookies = {
    'user_trace_token': '20230831203439-36aa960b-d3fa-4735-ae7e-99221d8beb16',
    'LGUID': '20230831203439-313b18e6-6611-4f45-8885-dbcf311f3a7c',
    '_ga': 'GA1.2.1359034317.1694614912',
    'X_HTTP_TOKEN': 'e1b568f96c31ed544807774961cdb3ef2741a34b26',
    'JSESSIONID': 'ABAAAECABIEACCAD048EC969916FEDAAD30DF4C6F430963',
    'WEBTJ-ID': '20230922192445-18abca29236195d-0ec628c66cc6c6-26031e51-2073600-18abca292371df8',
    'RECOMMEND_TIP': 'true',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1694614912,1694958254,1695130051,1695381886',
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1695381886',
    'sensorsdata2015session': '%7B%7D',
    '_gid': 'GA1.2.2142859191.1695381886',
    'privacyPolicyPopup': 'false',
    '_ga_DDLTLJDLHH': 'GS1.2.1695381886.4.0.1695381886.60.0.0',
    'index_location_city': '%E5%85%A8%E5%9B%BD',
    'TG-TRACK-CODE': 'index_search',
    'LGSID': '20230922200552-e7dc82e5-4d9e-41c5-bd5b-c799c9d998a9',
    'PRE_UTM': '',
    'PRE_HOST': 'www.google.com',
    'PRE_SITE': 'https%3A%2F%2Fwww.google.com%2F',
    'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
    'LGRID': '20230922200552-1e7da128-a2bd-45a5-84f9-d8392f153ed3',
    '__lg_stoken__': 'b3b9a75a0a432713d91744ffa60714b750f1309cbf77cb5af326d9f44d873555fdc59d7628a17751342cfed61f715cfbaa8832253983fb9eb2bf1928b8c1adc42ce36f1bc141',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218a4b96b27217c-00da66e0cffa74-26031f51-1468898-18a4b96b2732483%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22117.0.0.0%22%7D%2C%22%24device_id%22%3A%2218a4b96b27217c-00da66e0cffa74-26031f51-1468898-18a4b96b2732483%22%7D',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'user_trace_token=20230831203439-36aa960b-d3fa-4735-ae7e-99221d8beb16; LGUID=20230831203439-313b18e6-6611-4f45-8885-dbcf311f3a7c; _ga=GA1.2.1359034317.1694614912; X_HTTP_TOKEN=e1b568f96c31ed544807774961cdb3ef2741a34b26; JSESSIONID=ABAAAECABIEACCAD048EC969916FEDAAD30DF4C6F430963; WEBTJ-ID=20230922192445-18abca29236195d-0ec628c66cc6c6-26031e51-2073600-18abca292371df8; RECOMMEND_TIP=true; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1694614912,1694958254,1695130051,1695381886; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1695381886; sensorsdata2015session=%7B%7D; _gid=GA1.2.2142859191.1695381886; privacyPolicyPopup=false; _ga_DDLTLJDLHH=GS1.2.1695381886.4.0.1695381886.60.0.0; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; LGSID=20230922200552-e7dc82e5-4d9e-41c5-bd5b-c799c9d998a9; PRE_UTM=; PRE_HOST=www.google.com; PRE_SITE=https%3A%2F%2Fwww.google.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20230922200552-1e7da128-a2bd-45a5-84f9-d8392f153ed3; __lg_stoken__=b3b9a75a0a432713d91744ffa60714b750f1309cbf77cb5af326d9f44d873555fdc59d7628a17751342cfed61f715cfbaa8832253983fb9eb2bf1928b8c1adc42ce36f1bc141; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218a4b96b27217c-00da66e0cffa74-26031f51-1468898-18a4b96b2732483%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22117.0.0.0%22%7D%2C%22%24device_id%22%3A%2218a4b96b27217c-00da66e0cffa74-26031f51-1468898-18a4b96b2732483%22%7D',
    'Origin': 'https://www.lagou.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/wn/jobs?cl=false&fromSearch=true&labelWords=sug&suginput=%E7%88%AC%E8%99%AB%E9%80%86%E5%90%91&kd=%E7%88%AC%E8%99%AB%E9%80%86%E5%90%91',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
    'X-K-HEADER': 'xmi6+t9rIJKMkexhrPFCxPEeAjzZ8OvU3oBI8C9YqoscvVPRa+ciFsSSLynac8UV',
    'X-S-HEADER': '/mToNJHZWyRiKHocpBb9duIFiATVfCHKYSfgnnsqRDN3pfSs6800+mzqUWP9fepyzdQaNgLP04oy+el5s17wGM93zPGY7zT8Ksd4OhKUasOOMAMQmCFqkKj+rO/TlD4B8+v6vZSNyXJXRcmuNHwRAQ==',
    'X-SS-REQ-HEADER': '{"secret":"xmi6+t9rIJKMkexhrPFCxPEeAjzZ8OvU3oBI8C9YqoscvVPRa+ciFsSSLynac8UV"}',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'traceparent': '00-c105b73bf0d4be1726737a5ed5da394b-b8bf97e69d7390fb-01',
    'x-anit-forge-code': '0',
    'x-anit-forge-token': 'None',
}

# 请求体内容  提交给服务器
data = {
    'data': 'pSUwyd8ooRdUULqR2CtWonCOSAwVB4QQTKHHXtzyihN70XOG9rMUCgBRjeCl2ehh6NFaOnJak3p+TavTTzFuWrEo2ikKRgFgcxxW2S/F+pbEg4L0lzHn65FfVAbSrVYdFfNpSyk17ENoBMv5k2R8+2S4Het9t8fpno+6FK5FEM+1t2wLKKmjNj3RhWauA8BWeQdbN6eDFlL3drA0Opg03PhsLdBzcCmV5UtbKXNs9Co=',
}

# 返回数据是加密的
response = requests.post('https://www.lagou.com/jobs/v2/positionAjax.json', cookies=cookies, headers=headers, data=data)
