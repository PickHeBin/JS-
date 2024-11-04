# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import requests

cookies = {
    'RECOMMEND_TIP': 'true',
    'user_trace_token': '20230831203439-36aa960b-d3fa-4735-ae7e-99221d8beb16',
    'LGUID': '20230831203439-313b18e6-6611-4f45-8885-dbcf311f3a7c',
    '_ga': 'GA1.2.261575767.1693485282',
    '_gid': 'GA1.2.905687865.1693485282',
    'privacyPolicyPopup': 'false',
    'index_location_city': '%E5%85%A8%E5%9B%BD',
    'JSESSIONID': 'ABAAAECABIEACCA99CD5DEA5F8188107CE17C9AC04635A1',
    'WEBTJ-ID': '20230901150809-18a4f9218bc45-0553388715fd82-26031f51-1462042-18a4f9218bd23ad',
    'PRE_UTM': '',
    'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F',
    '_gat': '1',
    'LGSID': '20230901150804-bda717bd-830e-4872-9b60-1bf42446cd0d',
    'PRE_HOST': 'www.google.com.hk',
    'PRE_SITE': 'https%3A%2F%2Fwww.google.com.hk%2F',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1693485282,1693552090',
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1693552090',
    'sensorsdata2015session': '%7B%7D',
    '_ga_DDLTLJDLHH': 'GS1.2.1693552090.2.0.1693552090.60.0.0',
    'TG-TRACK-CODE': 'index_search',
    'LGRID': '20230901150807-cd252f75-35a5-459d-a291-8213ddb0bab7',
    'X_HTTP_TOKEN': 'e1b568f96c31ed547802553961cdb3ef2741a34b26',
    'X_MIDDLE_TOKEN': '9a1e9a18bc30b6f186fa734799e9fb91',
    '__lg_stoken__': 'd778bc664feea90b0b2e3ca1c6c94a86468972308a2404594a5934d2b3515f6f84bef1068f62e8f8b47fa456123a10172a0979be9a9d4cb8cd1a47e783e448f64234484ab0be',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218a4b96b27217c-00da66e0cffa74-26031f51-1468898-18a4b96b2732483%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22116.0.0.0%22%7D%2C%22%24device_id%22%3A%2218a4b96b27217c-00da66e0cffa74-26031f51-1468898-18a4b96b2732483%22%7D',
}

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'RECOMMEND_TIP=true; user_trace_token=20230831203439-36aa960b-d3fa-4735-ae7e-99221d8beb16; LGUID=20230831203439-313b18e6-6611-4f45-8885-dbcf311f3a7c; _ga=GA1.2.261575767.1693485282; _gid=GA1.2.905687865.1693485282; privacyPolicyPopup=false; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAAECABIEACCA99CD5DEA5F8188107CE17C9AC04635A1; WEBTJ-ID=20230901150809-18a4f9218bc45-0553388715fd82-26031f51-1462042-18a4f9218bd23ad; PRE_UTM=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _gat=1; LGSID=20230901150804-bda717bd-830e-4872-9b60-1bf42446cd0d; PRE_HOST=www.google.com.hk; PRE_SITE=https%3A%2F%2Fwww.google.com.hk%2F; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1693485282,1693552090; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1693552090; sensorsdata2015session=%7B%7D; _ga_DDLTLJDLHH=GS1.2.1693552090.2.0.1693552090.60.0.0; TG-TRACK-CODE=index_search; LGRID=20230901150807-cd252f75-35a5-459d-a291-8213ddb0bab7; X_HTTP_TOKEN=e1b568f96c31ed547802553961cdb3ef2741a34b26; X_MIDDLE_TOKEN=9a1e9a18bc30b6f186fa734799e9fb91; __lg_stoken__=d778bc664feea90b0b2e3ca1c6c94a86468972308a2404594a5934d2b3515f6f84bef1068f62e8f8b47fa456123a10172a0979be9a9d4cb8cd1a47e783e448f64234484ab0be; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218a4b96b27217c-00da66e0cffa74-26031f51-1468898-18a4b96b2732483%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22116.0.0.0%22%7D%2C%22%24device_id%22%3A%2218a4b96b27217c-00da66e0cffa74-26031f51-1468898-18a4b96b2732483%22%7D',
    'Origin': 'https://www.lagou.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/wn/jobs?labelWords=&fromSearch=true&suginput=&kd=python',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'X-K-HEADER': 'vJrgW622+qgY+18bZjVazX8tCfDOtIp6HI6Inokq+5yWZDjfa5pkd3MXnbcnPGsh',
    'X-S-HEADER': 'EfHJytS98JUzgfKSxsCI/hXjiSkP3AWaMrGW0u9c5dkKA6Ows4eewnfBT6mAfWXNmPWkLaz/lIKrNBqT4x2H/tf7YBBtw1vJORVOfTdl+7VOSvXF9EeH6n0ji7QQbt+sGpJ/agR03Yx9bHqhhbrCoA==',
    'X-SS-REQ-HEADER': '{"secret":"vJrgW622+qgY+18bZjVazX8tCfDOtIp6HI6Inokq+5yWZDjfa5pkd3MXnbcnPGsh"}',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Brave";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'traceparent': '00-ec960f0ffb6a9edea34225b64b395b8a-0ecb30a12377d94c-01',
    'x-anit-forge-code': '0',
    'x-anit-forge-token': 'None',
}

data = {
    'data': '0E/iMjy2tXaQMUFaV1FjqFBX8Mwyv71PoEcQdTNjEM8vfy4xX808z1wbtFQ66FXUr8MUbVJbsgYFkREy4q2Iw1HAWMv5tgdexQlJ1jhKvn2BUxlXW67RoMya+IFgZlR6757eLfRyxpomoIUexCWWyg==',
}

response = requests.post('https://www.lagou.com/jobs/v2/positionAjax.json', cookies=cookies, headers=headers, data=data).json()
print(response)
