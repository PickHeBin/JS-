# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
'''
账号: 实名 手机验证

做兼职: 第一个月 大部分 2k左右  熟悉平台 流程
        第二个月第三个月  学费就赚回来了

零基础  5- 6个月  时间多 提前学习 (1-2小时    3 -4)



'''
import requests

cookies = {
    'tt_webid': '7262710108152383031',
    'csrftoken': 'cce58cdcac416ad9aff39faf253200a5',
    's_v_web_id': 'verify_lotykn97_71HbjEMJ_NKfZ_47sQ_Bv4p_oU9rGUkD6HVO',
    'local_city_cache': '%E9%95%BF%E6%B2%99',
    'tt_scid': 'yFKA5EFIgYTo4G2jIyO1Sjw.fcVeinvouxahXIR7cuQdaAsLkjkfk43YimujmLm9be1b',
    'ttwid': '1%7C-XIN-4HgYmuibmxUqrJbir3jXPgBtX9-1mXMecIvve8%7C1699704147%7Ced06e406416e10f16a579400a04eeca894f1d8d9e483347df16b5a06790c5017',
}

headers = {
    'authority': 'www.toutiao.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'tt_webid=7262710108152383031; csrftoken=cce58cdcac416ad9aff39faf253200a5; s_v_web_id=verify_lotykn97_71HbjEMJ_NKfZ_47sQ_Bv4p_oU9rGUkD6HVO; local_city_cache=%E9%95%BF%E6%B2%99; tt_scid=yFKA5EFIgYTo4G2jIyO1Sjw.fcVeinvouxahXIR7cuQdaAsLkjkfk43YimujmLm9be1b; ttwid=1%7C-XIN-4HgYmuibmxUqrJbir3jXPgBtX9-1mXMecIvve8%7C1699704147%7Ced06e406416e10f16a579400a04eeca894f1d8d9e483347df16b5a06790c5017',
    'pragma': 'no-cache',
    'referer': 'https://www.toutiao.com/?wid=1659882176248',
    'sec-ch-ua': '"Brave";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://www.toutiao.com/api/pc/list/feed?channel_id=3189398999&min_behot_time=0&offset=0&refresh_count=1&category=pc_profile_channel&client_extra_params=%7B%22short_video_item%22:%22filter%22%7D&aid=24&app_name=toutiao_web&_signature=_02B4Z6wo001019vY6xgAAIDBFma4iTN-3g.b.O-AAJPC1xxwUStFg5O6t0.vitTx.acBG14v0zNI62vYogLoqCQ1U4ScHXXhjWNgJupPm5Y4T7DIznJrHm7DuN4aSy3o4YNlV1PMMKKbDD2U71',
    cookies=cookies,
    headers=headers,
)
print(response.text)
