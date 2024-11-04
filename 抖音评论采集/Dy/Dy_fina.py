# -*- coding: utf-8 -*-

import time
import math
import re
import json
import execjs
# import dy_yzm_copy
import requests
import threading
import subprocess
from log import register_logger
import numpy as np
from flask import Flask, request, jsonify
from loguru import logger
from threading import Thread
from fake_useragent import UserAgent
import urllib
from urllib import parse

from pymysql import err, sys, cursors
# from DBUtils.PooledDB import PooledDB
from dbutils.pooled_db import PooledDB

from functools import partial
from urllib.parse import urlencode
from concurrent.futures import ThreadPoolExecutor


lock = threading.Lock()

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
start_time = int(time.time())

# print(ua.random)

# 注册日志
register_logger()


M = '任务已执行完毕'
app = Flask(__name__)

# 隧道域名:端口号
tunnel = "n203.kdltps.com:15818"

# 用户名密码方式
username = "t19657680529363"
password = "9hhefpg1"
proxies = {
    "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel},
    "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": tunnel}
}



    # connect.close()


def get_code(ID, keywords, match_keywords, masking_keywords, UA,):
    Data = []  
    match_keywords = match_keywords.split(',')
    masking_keywords = masking_keywords.split(',')

    # 打印数据
    logger.info(UA)
    logger.info(keywords)
    logger.info(match_keywords)
    logger.info(masking_keywords)
    get_douyin(Data, ID, UA, keywords, match_keywords, masking_keywords)
    # all_data = json.dumps({'data':Data})
    # all_data = {'data':Data}
    all_data = json.dumps(Data,ensure_ascii=False)
    # all_data = str(all_data)
    # with open('0001.txt','w',encoding='utf-8') as f:
    #     f.write(str(all_data))



def get_douyin(Data, ID, UA, keywords, match_keywords, masking_keywords):
    headers = {
        'authority': 'www.douyin.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': UA,
    }
    url = 'https://www.douyin.com/'
    response = requests.get(url=url, headers=headers)
    __ac_nonce = response.cookies["__ac_nonce"]
    __ac_signature = execjs.compile(open('E:/Dy/Dy_jsvmp.js', 'r', encoding="utf-8").read()).call('get__ac_signature', str(__ac_nonce))
    # logger.info(ac)
    # return ac
    get_second_request(Data, ID, UA, __ac_nonce, __ac_signature, keywords, match_keywords, masking_keywords)


def get_second_request(Data, ID, UA, __ac_nonce, __ac_signature, keywords, match_keywords, masking_keywords):
    cookies = {
        '__ac_nonce': str(__ac_nonce),
        '__ac_signature': str(__ac_signature),
        '__ac_referer': '__ac_blank',
    }

    headers = {
        'authority': 'www.douyin.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'referer': 'https://www.douyin.com/discover',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': UA,
    }

    response = requests.get('https://www.douyin.com/discover', cookies=cookies, headers=headers)
    ttwid = response.cookies["ttwid"]
    get_douyin_list(Data, ID, UA, __ac_nonce, __ac_signature, ttwid, keywords, match_keywords, masking_keywords)

def get_douyin_list(Data, ID, UA, __ac_nonce, __ac_signature, ttwid, keywords, match_keywords, masking_keywords):
    K = urllib.parse.quote(keywords)
    headers = {
        "authority": "www.douyin.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": f"https://www.douyin.com/search/{K}?publish_time=182&sort_type=0&source=tab_search&type=video",
        "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": UA
    }

    cookies = {
        "s_v_web_id": "verify_lmbhexdf_MMmD1pb6_S8cI_4FbR_89EK_NJ2cA3F4MmwS",
        "ttwid": str(ttwid),
        "FORCE_LOGIN": "%7B%22videoConsumedRemainSeconds%22%3A180%7D",
        "passport_csrf_token": "07f3280c428b442a886a2249e37dacac",
        "passport_csrf_token_default": "07f3280c428b442a886a2249e37dacac",
        "bd_ticket_guard_client_data": "eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRC9aa1hIU0JPcWJwY1pMT1gzZFJ5T3JBVFNsUjBVSjFXWlFvOStUZ2RiWnJIZGxUVko4TVhoMDIvVkdCYXh4a3JHV05kTDBQNEZsT0pmc29SQjhIVnc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==",
        "SEARCH_RESULT_LIST_TYPE": "%22single%22",
        "volume_info": "%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D",
        "ttcid": "9b7d93bb3f1d4b4c9eb1b20040118f6873",
        "download_guide": "%223%2F20230915%2F0%22",
        "pwa2": "%220%7C0%7C3%7C0%22",
        "strategyABtestKey": "%221695178807.554%22",
        "stream_recommend_feed_params": "%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A1.55%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A150%7D%22",
        "__ac_nonce": str(__ac_nonce),
        "__ac_signature": str(__ac_signature),
        "home_can_add_dy_2_desktop": "%221%22",
        "msToken": "pdJFWdh6CoE2S8lIgSJuhPt-JQ6uBD8qglv5HqPxccwmx7sevYFE8BYwTmW-KgnH756te4AY0RleqNtQOgHbTxoe7EqGStdZfdWD7Y6R6CtIbgDx30g=",
        "tt_scid": "3scElgg4VQ9JfVOCMS0.XBcEUN3O6MqLdtp2nBWUGRi.b0W8CBlKMqZr9iU0dg4if1d0",
        "IsDouyinActive": "true"
    }

    url = "https://www.douyin.com/aweme/v1/web/search/item/"
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "search_channel": "aweme_video_web",
        "sort_type": "0",
        "publish_time": "182",
        "keyword": f"{keywords}",
        "search_source": "tab_search",
        "query_correct_type": "1",
        "is_filter_search": "1",
        "from_group_id": "",
        "offset": "0",
        "count": "30",
        # "search_id": "2023100610385184C98EB934334530B443",
        "pc_client_type": "1",
        "version_code": "170400",
        "version_name": "17.4.0",
        "cookie_enabled": "true",
        "screen_width": "1920",
        "screen_height": "1080",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Chrome",
        "browser_version": "117.0.0.0",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "117.0.0.0",
        "os_name": "Windows",
        "os_version": "10",
        "cpu_core_num": "4",
        "device_memory": "8",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "50",
        "webid": "7283391793708664377",
        # "msToken": "SVvA0tKtAcd8JvQ8Qvu44P41wikpE-tG5EjmfgNd6dSjaPaYrqlSrw7RGl6lhwCvj2ULMZMYC91liKPSqDNd2VXxXUzn1OPZZnV_samRRtmiHg233a-3mRGQ7oR_P-4=",
        # "X-Bogus": "DFSzswVOYQ0ANt/ltOmHBe9WX7nW"
    }

    user_agent = UA
    url_path = urlencode(params, safe='=')
    params["X-Bogus"] = execjs.compile(open('E:\\Dy\\x-bogus.js', 'r', encoding="utf-8").read()).call('sign',url_path,user_agent)
    # logger.info(params)
    response = requests.post(url=url, headers=headers, cookies=cookies, params=params, proxies=proxies)
    logger.info(response)
    if response.status_code not in [200]:
        logger.info('请求失败')
    else:
        try :
            response.json() or response.json()['data']
        except :
            logger.info('视频信息不是json数据')
            time.sleep(5)
            get_douyin(Data, ID, UA, keywords, match_keywords, masking_keywords)
        data = response.json().get('data', []) or []
        if data != []:
            for i in range(len(data)):
                logger.info(i)
                aweme_info = data[i].get("aweme_info", {})
                author_aweme_id = aweme_info.get("aweme_id", '')
                author_create_time = aweme_info.get("create_time", '')
                if author_create_time != '':
                    # months = start_time - int(author_create_time)                               #相差月份
                    author_user_id = aweme_info.get("author_user_id", '')
                    author_desc = aweme_info.get("desc", '').replace(" ","").replace("\r\n","").replace("\r","").replace("\n","")
                    author = aweme_info.get("author", {})
                    author_uid = author.get("uid", '')
                    author_short_id = author.get("short_id", '')
                    author_nickname = author.get("nickname", '').replace(" ","").replace("\r\n","").replace("\r","").replace("\n","")
                    logger.info(author_nickname)
                    author_sec_uid = author.get("sec_uid", '')
                    author_unique_id = author.get("unique_id", '')
                    author_home=("https://www.douyin.com/user/" + author_sec_uid) if author_sec_uid else ''
                    author_share_url = aweme_info.get("share_info",{}).get("share_url", '')
                    # logger.info('uid = '+ str(author_user_id))
                    # logger.info('uid = '+ author_uid)
                    # logger.info('short_id = '+ author_short_id)
                    logger.info('aweme_id = '+ str(author_aweme_id))
                    # logger.info('姓名 = '+ author_nickname)
                    logger.info('抖音主页 = '+ author_sec_uid)
                    # logger.info('抖音号 = '+ author_unique_id)
                    logger.info('视频标题 = '+ author_desc)
                    # logger.info('视频链接 = '+ author_share_url)
                    # logger.info('月份 = '+ str(months))
                    logger.info('=================================================这是视频的基本信息===================================================') 
                    if not author_aweme_id == '':
                        video_content ={
                            "keywords":f"{keywords}",
                            "province":"",
                            "video_keywords":f"{author_desc}",
                            "video_title":f"{author_desc}",
                            "author_nickname":f"{author_nickname}",
                            "author_douyin_id":f"{author_unique_id}",
                            "author_douyin_uid": f"{author_user_id}",
                            "aweme_id":f"{author_aweme_id}",
                            "send_time":author_create_time,
                            # "updatetime":{a},
                            "comment_list":[]
                        }


                    main_review(__ac_nonce, __ac_signature, ttwid, video_content, start_time, UA, author_aweme_id, author_sec_uid, match_keywords, masking_keywords,)
                    Data.append(video_content)

def get_douyin_list_next(Data, ID, UA, __ac_nonce, __ac_signature, ttwid, keywords, match_keywords, masking_keywords):
    proxies = {
        'http': 'http://112.248.122.204:16996',
    #   'https': 'http://10.10.1.10:5323'
    }
    K = urllib.parse.quote(keywords)

    headers = {
            "authority": "www.douyin.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": f"https://www.douyin.com/search/{K}?aid=a9dc0daf-f353-4aff-89ea-1f35c2c4e94a&publish_time=0&sort_type=0&source=normal_search&type=general",
            "sec-ch-ua": "\"Google Chrome\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": UA
    }
    cookies = {
        "__ac_nonce": str(__ac_nonce),
        "__ac_signature": str(__ac_signature),
        "ttwid": str(ttwid),
        "douyin.com": "",
        "home_can_add_dy_2_desktop": "%221%22",
        "strategyABtestKey": "%221695175549.191%22",
    }

    url = "https://www.douyin.com/aweme/v1/web/general/search/single/"
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "search_channel": "aweme_general",
        "sort_type": "0",
        "publish_time": "1",
        "keyword": f"{keywords}",
        "search_source": "tab_search",
        "query_correct_type": "1",
        "is_filter_search": "1",
        "from_group_id": "",
        "offset": "0",
        "count": "30",
        "pc_client_type": "1",
        "version_code": "190600",
        "version_name": "19.6.0",
        "cookie_enabled": "true",
        "screen_width": "1920",
        "screen_height": "1080",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Edge",
        "browser_version": "117.0.2045.31",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "117.0.0.0",
        "os_name": "Windows",
        "os_version": "10",
        "cpu_core_num": "4",
        "device_memory": "8",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "50",
        "webid": "7276666884769564201",
        "msToken": "pdJFWdh6CoE2S8lIgSJuhPt-JQ6uBD8qglv5HqPxccwmx7sevYFE8BYwTmW-KgnH756te4AY0RleqNtQOgHbTxoe7EqGStdZfdWD7Y6R6CtIbgDx30g=",
        "X-Bogus": "DFSzswVLnLvANVQYtPG1g5ppgiFp"
    }
    # url_path = urlencode(params, safe='=')
    # logger.info(url_path)
    # params["X-Bogus"] = execjs.compile(open('E:\\Dy\\x-bogus.js', 'r', encoding="utf-8").read()).call("get_x_bogus", url_path)
    user_agent = UA
    url_path = urlencode(params, safe='=')
    params["X-Bogus"] = execjs.compile(open('E:\\Dy\\x-bogus.js', 'r', encoding="utf-8").read()).call('sign',url_path,user_agent)
    # logger.info(params)


    # S = 0
    # while True:
    # for i in range(10):
    #     end_time = int(time.time())
    #     if end_time -start_time == 1200:
    #         break
    #     offset = 10 * (i)
    #     # S = S + 1
    #     logger.info(f'视频信息：{offset}')
    #     params['offset'] = offset
    response = requests.post(url=url, headers=headers, cookies=cookies, params=params)
    if response.status_code not in [200]:
        logger.info('请求失败')
        # update_sql_status(task_id=ID)
        # callback_business_system(task_id=ID)
        # break
    else:
        try :
            response.json() or response.json()['data']
        except :
            logger.info('视频信息不是json数据')
            # continue
        else:
            # logger.info(response.json())
            data = response.json().get('data', []) or []
            if data != []:
                for i in range(len(data)):
                    logger.info(str(i))
                    aweme_info = data[i].get("aweme_info", {})
                    author_aweme_id = aweme_info.get("aweme_id", '')
                    author_create_time = aweme_info.get("create_time", '')
                    # logger.info(f'author_create_time:{author_create_time}')
                    # logger.info(f'start_time:{start_time}')
                    if author_create_time != '':
                        months = start_time - int(author_create_time)                               #相差月份
                        author_user_id = aweme_info.get("author_user_id", '')
                        author_desc = aweme_info.get("desc", '').replace(" ","").replace("\r\n","").replace("\r","").replace("\n","")
                        logger.info(f'视频标题为：{author_desc}')
                        author = aweme_info.get("author", {})
                        author_uid = author.get("uid", '')
                        author_short_id = author.get("short_id", '')
                        author_nickname = author.get("nickname", '').replace(" ","").replace("\r\n","").replace("\r","").replace("\n","")
                        logger.info(author_nickname)
                        author_sec_uid = author.get("sec_uid", '')
                        author_unique_id = author.get("unique_id", '')
                        author_home=("https://www.douyin.com/user/" + author_sec_uid) if author_sec_uid else ''
                        author_share_url = aweme_info.get("share_info",{}).get("share_url", '')
                        # logger.info('uid = '+ author_uid)
                        # logger.info('short_id = '+ author_short_id)
                        # logger.info('aweme_id = '+ author_aweme_id)
                        # logger.info('姓名 = '+ author_nickname)
                        # logger.info('抖音主页 = '+ author_sec_uid)
                        # logger.info('抖音号 = '+ author_unique_id)
                        # logger.info('视频标题 = '+ author_desc)
                        logger.info('视频链接 = '+ author_share_url)
                        logger.info('月份 = '+ str(months))
                        logger.info('=================================================这是视频的基本信息===================================================')   
                        # if not author_aweme_id == '' and months <= 2592000:
                        if not author_aweme_id == '':
                            video_content ={
                                "keywords":f"{keywords}",
                                "province":"",
                                "video_keywords":f"{author_desc}",
                                "video_title":f"{author_desc}",
                                "author_nickname":f"{author_nickname}",
                                "author_douyin_id":f"{author_unique_id}",
                                "author_douyin_uid": f"{author_user_id}",
                                "aweme_id":f"{author_aweme_id}",
                                "send_time":author_create_time,
                                # "updatetime":{a},
                                "comment_list":[]
                            }


                        main_review(__ac_nonce, __ac_signature, ttwid, video_content, start_time, UA, author_aweme_id, author_sec_uid, match_keywords, masking_keywords,)
                        Data.append(video_content)



def main_review(__ac_nonce, __ac_signature, ttwid, video_content, start_time, UA, aweme_id, sec_uid, match_keywords, masking_keywords):
    '''
    获取主评论的内容
    '''
    headers = {
    'authority': 'www.douyin.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'no-cache',
    'cookie': 'ttwid=1%7CrrRP1gO3snLMSDHJimAA4Rzen_cQf7SgrVynDjW73v8%7C1693537473%7C0f7a9ab0deaae3ab4140f8042ccd623ebf210decec8cbfb5462be4b1e4fcab01; passport_csrf_token=17a699029a8f170753981f33e18fc657; passport_csrf_token_default=17a699029a8f170753981f33e18fc657; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; s_v_web_id=verify_lm00hlnw_dnn2ODCJ_Gf62_4vhU_8TDo_43pcHxVB3XRS; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTU56M2M1RGNkakJsNDIwTWZNNTREY2dRSFVBcDk4SEJRNUZ1c1lIK1J5SEJzUHFKT3BndURMS21Td04zUXNOcmFzU09YY0p3b0VkNVNpMmJpUm82cUk9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ==; ttcid=d5039f4f8fc64201bd7565c9b7d3724829; SEARCH_RESULT_LIST_TYPE=%22single%22; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; webcast_local_quality=null; strategyABtestKey=%221693618258.757%22; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1694223059377%2C%22type%22%3A1%7D; download_guide=%223%2F20230901%2F1%22; pwa2=%220%7C0%7C3%7C0%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; __ac_nonce=064f2de74001305786fa5; __ac_signature=_02B4Z6wo00f01SV6MygAAIDBpXjJaTiNsQElWjeAAC2vh0LmPpTOOIBvA0LtaVX-tjpEoa7reLYj4M1Z1TnlRTHOFijIcG3u6f5TIym6ruktynJ54Qe2RZaREOCPFHIOsDvpJPT.eIWX7l4B39; IsDouyinActive=true; home_can_add_dy_2_desktop=%221%22; msToken=92WNIudnMEMRkgO7Em66Cu6zeo1Wbf-gmeTfvM__BZNmwbeRiHcvV49Cz8pEyiiXc0T3I6YtgIbzLTMqVHYZPR0gKr4_D2iUFS4qUKGAwq11h05evikrwghO5Q8v; msToken=3eModXsXT_QzqyiPF66glvO0tnidkxJ3q_XhyOe7MGa2ZXzRsoxcGVZqz7FqqCoQl9u4WHOekPeIVuXTl-pZ4FwnUT7m0O08v9aZn8uaM21RSHRgEK7qjk6FTlPK; tt_scid=2IPvlfv01Sq86zEPPYTl0eNXD9WiOhl8yaVQ0z1LKXDuNS9i017dcvcXwh-jPjZwb8b9',
    'pragma': 'no-cache',
    'referer': f'https://www.douyin.com/user/{sec_uid}?modal_id={aweme_id}',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': UA,
    }
    params = {
        'device_platform': 'webapp',
        'aid': '6383',
        'channel': 'channel_pc_web',
        'aweme_id': f'{aweme_id}',
        'cursor': '0',
        'count': '50',
        'item_type': '0',
        'insert_ids': '',
        'rcFT': '',
        'pc_client_type': '1',
        'version_code': '170400',
        'version_name': '17.4.0',
        'cookie_enabled': 'true',
        'screen_width': '1920',
        'screen_height': '1080',
        'browser_language': 'zh-CN',
        'browser_platform': 'Win32',
        'browser_name': 'Chrome',
        'browser_version': '116.0.0.0',
        'browser_online': 'true',
        'engine_name': 'Blink',
        'engine_version': '116.0.0.0',
        'os_name': 'Windows',
        'os_version': '10',
        'cpu_core_num': '4',
        'device_memory': '8',
        'platform': 'PC',
        'downlink': '10',
        'effective_type': '4g',
        'round_trip_time': '100',
        'webid': '7273688015380448825',
        'msToken': '3eModXsXT_QzqyiPF66glvO0tnidkxJ3q_XhyOe7MGa2ZXzRsoxcGVZqz7FqqCoQl9u4WHOekPeIVuXTl-pZ4FwnUT7m0O08v9aZn8uaM21RSHRgEK7qjk6FTlPK',
        # 'X-Bogus': 'DFSzswVuKyhANcTOtyR5Ve9WX7rc',
    }

    user_agent = UA
    url_path = urlencode(params, safe='=')
    params["X-Bogus"] = execjs.compile(open('E:\\Dy\\x-bogus.js', 'r', encoding="utf-8").read()).call('sign',url_path,user_agent)
    # response = requests.get('https://www.douyin.com/aweme/v1/web/comment/list/', params=params, headers=headers)
    # logger.info(response.json()['comments'][0]['text'])
    # cid = response.json()['comments'][0]['cid'] 
    # under_review(aweme_id,cid,sec_uid)
 

    # n = 0
    # while True:
    # for i in range(5):
    #     end_time = int(time.time())
    #     if end_time -start_time >= 1200:
    #         break
    #     cursor = 20 * (i)
    #     # n = n + 1
    #     logger.info(f'主评论：{cursor}')
    #     params['cursor'] = cursor
    #     time.sleep(1)
    response = requests.get('https://www.douyin.com/aweme/v1/web/comment/list/', params=params, headers=headers,proxies=proxies)
    logger.info(response.status_code)
    # logger.info(response.text)
    if response.status_code not in [200]:
        logger.info('请求失败')
    try :
        response.json() or response.json()['comments']
    except :
        logger.info('主评论信息不是json数据')
    else:
        # logger.info(response.json())
        data = response.json().get('comments', []) or []
        if data != []:
            for i in range(len(data)):
                # logger.info(response.json()['comments'][i]['text'])
                logger.info(i)
                cid = data[i].get('cid', '')                                                            #cid
                create_time = data[i].get('create_time', '')                       #创建时间
                # p_create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(create_time))         #格式化创建时间
                now_time = int(time.time())                                                             #现在时间
                # months = (now_time - create_time) // (30 * 24 * 60 * 60)                                #相差月份
                months = start_time - int(create_time)                               #相差月份
                review_addr = data[i].get('ip_label', '')                                               #省份
                review_text = data[i].get('text', '').replace("\r\n","").replace("\r","").replace("\n","")                                                  #评论
                review_text = re.sub(r"\\n", '', review_text)                                                  #评论
                review_uid = data[i].get('user', {}).get('uid', '')                                     #评论者的uid
                review_short_id = data[i].get('user', {}).get('short_id', '')                           #评论者的short_id
                review_unique_id = data[i].get('user', {}).get('unique_id', '')                         #评论者的unique_id
                review_nickname = data[i].get('user', {}).get('nickname', '').replace("\r","").replace("\n","").replace("\r\n","")                           #评论者的名字
                review_nickname = re.sub(r"\\n", '', review_nickname)                           #评论者的名字
                # logger.info('cid:'+ cid)
                logger.info('创建时间='+ str(create_time) )
                # logger.info('格式化创建时间='+ str(p_create_time ))
                logger.info('现在时间='+ str(now_time) )
                logger.info('相差月份='+ str(months) )
                logger.info('省份='+ review_addr )
                logger.info('评论='+ review_text )
                logger.info('评论者的uid='+ review_uid )
                logger.info('评论者的short_id='+ review_short_id )
                logger.info('评论者的抖音号='+ review_unique_id )
                logger.info('评论者的名字='+ review_nickname )
                logger.info('=================================================这是主评论的基本信息===================================================')
                if match_keywords ==[''] and masking_keywords ==['']:
                    if review_text != '':
                    # if months < 15552000 and review_text != '':
                        comment_content = {
                            "comment_id" : f"{cid}",
                            "comment_content" : f"{review_text}",
                            "comment_author_province" : f"{review_addr}",
                            "comment_author_nickname" : f"{review_nickname}",
                            "comment_author_douyin_id" : f"{review_short_id}",
                            "comment_author_uid" : f"{review_uid}",
                            "comment_time" : create_time,
                            # "updatetime" : {now_time},                            
                            }
                        logger.info(comment_content)
                        video_content["comment_list"].append(comment_content)
                if masking_keywords ==[''] and match_keywords !=['']:            
                    if review_text != '' and any(a in review_text for a in match_keywords):
                    # if months < 15552000 and review_text != '' and any(a in review_text and not any(b in review_text for b in masking_keywords) for a in match_keywords):
                        comment_content = {
                            "comment_id" : f"{cid}",
                            "comment_content" : f"{review_text}",
                            "comment_author_province" : f"{review_addr}",
                            "comment_author_nickname" : f"{review_nickname}",
                            "comment_author_douyin_id" : f"{review_short_id}",
                            "comment_author_uid" : f"{review_uid}",
                            "comment_time" : create_time,
                            # "updatetime" : {now_time},                            
                            }
                        logger.info(comment_content)
                        video_content["comment_list"].append(comment_content)
                if match_keywords ==[''] and masking_keywords !=['']:            
                    if review_text != '' and not any(b in review_text for b in masking_keywords):
                    # if months < 15552000 and review_text != '' and any(a in review_text and not any(b in review_text for b in masking_keywords) for a in match_keywords):
                        comment_content = {
                            "comment_id" : f"{cid}",
                            "comment_content" : f"{review_text}",
                            "comment_author_province" : f"{review_addr}",
                            "comment_author_nickname" : f"{review_nickname}",
                            "comment_author_douyin_id" : f"{review_short_id}",
                            "comment_author_uid" : f"{review_uid}",
                            "comment_time" : create_time,
                            # "updatetime" : {now_time},                            
                            }
                        logger.info(comment_content)
                        video_content["comment_list"].append(comment_content)
                if match_keywords !=[''] and masking_keywords !=['']:            
                    if review_text != '' and any(a in review_text and not any(b in review_text for b in masking_keywords) for a in match_keywords):
                    # if months < 15552000 and review_text != '' and any(a in review_text and not any(b in review_text for b in masking_keywords) for a in match_keywords):
                        comment_content = {
                            "comment_id" : f"{cid}",
                            "comment_content" : f"{review_text}",
                            "comment_author_province" : f"{review_addr}",
                            "comment_author_nickname" : f"{review_nickname}",
                            "comment_author_douyin_id" : f"{review_short_id}",
                            "comment_author_uid" : f"{review_uid}",
                            "comment_time" : create_time,
                            # "updatetime" : {now_time},                            
                            }
                        logger.info(comment_content)
                        video_content["comment_list"].append(comment_content)

            
def callback_business_system(task_id,pick_data):
    """通知业务系统，任务已完成"""
    # fin_url = f'https://kehenduo.lifala.net/api/thread/joinThreadJobStore?thread_id={task_id}&secret=kehenduo_join_job'
    logger.info(pick_data)
    # pick_data = json.dumps(pick_data)
    logger.info(type(pick_data))
    with open('0001.txt','w',encoding='utf-8') as f:
        f.write(str(pick_data))
    datas = {
        "thread_id":task_id,
        "pick_data":pick_data,
        "secret":"kehenduo_join_job",
    }
    # fin_url = f'http:192.168.9.69/api/thread/pickDataStore?thread_id={task_id}&pick_data={pick_data}&secret=kehenduo_join_job'
    # fin_url = f'http:192.168.9.69/api/thread/pickDataStore?thread_id=5&pick_data=''&secret=kehenduo_join_job'

    headers = {
        "accept": "application/json, text/plain, */*",        
    }
    try:
        ress = requests.post(url='http://192.168.9.69/api/thread/pickDataStore',data=datas, headers=headers)
        # logger.info(ress.json())
        logger.info(ress.text)
    except Exception as e :
        logger.info(e)
        # logger.info(ress.json())
        logger.info(ress.text)


    logger.info(f"任务: {task_id} 已完成， 即将通知业务系统")
    

@app.route('/scrape', methods=['GET'])
def scrape():
    # dy_yzm_copy.sel_code()
    # 请求进来
    # ID = request.values.get("ID")
    # ID_ = json.loads(ID)
    # logger.info(ID_)
    # id = ID_['id']
    # match_keywords = ID_['match_keywords']
    # masking_keywords = ID_['masking_keywords']
    # keywords = ID_['keywords']

    # print(id, keywords, match_keywords,masking_keywords)
    # logger.info(id, keywords, match_keywords,masking_keywords)
    id = '0002'
    keywords = '近视眼镜'
    match_keywords = ''
    masking_keywords = ''


    # 要访问的目标网页
    target_url = "https://dev.kdlapi.com/testproxy"

    # 使用隧道域名发送请求
    response = requests.get(target_url, proxies=proxies)

    # 获取页面内容
    if response.status_code == 200:
        print(response.text)


    # 随机产生User-Agent
    UA = UserAgent().chrome

    # 异步启动爬虫
    # executor.submit(get_code, args=(id, keywords, match_keywords, masking_keywords, UA,))
    worker_thread = Thread(target=get_code, args=(id, keywords, match_keywords, masking_keywords, UA,))
    worker_thread.start()

    return {
        "status": 200,
        'content':'数据正在获取中......'
        }
    


if __name__ == '__main__':
    app.run(port=1688,debug=False,host='0.0.0.0',threaded = True,processes=False)
