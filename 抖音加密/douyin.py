import requests
from functools import partial
import subprocess

subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs
from urllib.parse import urlencode


def get_douyin():
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
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }
    url = 'https://www.douyin.com/'
    response = requests.get(url=url, headers=headers)
    __ac_nonce = response.cookies["__ac_nonce"]
    print(__ac_nonce)
    __ac_signature = execjs.compile(open('抖音_jsvmp.js', 'r', encoding="utf-8").read()).call('get__ac_signature',
                                                                                              str(__ac_nonce))
    print(__ac_signature)
    get_second_request(__ac_nonce, __ac_signature)


def get_second_request(__ac_nonce, __ac_signature):
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
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    response = requests.get('https://www.douyin.com/discover', cookies=cookies, headers=headers)
    # print(response.text)
    # print(response.cookies)
    ttwid = response.cookies["ttwid"]
    get_douyin_list(__ac_nonce, __ac_signature, ttwid)


def get_douyin_list(__ac_nonce, __ac_signature, ttwid):
    headers = {
        "authority": "www.douyin.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "content-length": "0",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.douyin.com",
        "pragma": "no-cache",
        "referer": "https://www.douyin.com/discover",
        "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
    }
    cookies = {
        "__ac_nonce": str(__ac_nonce),
        "__ac_signature": str(__ac_signature),
        "ttwid": str(ttwid),
        "douyin.com": "",
        "home_can_add_dy_2_desktop": "%220%22",
        "strategyABtestKey": "%221685075908.124%22"
    }
    url = "https://www.douyin.com/aweme/v1/web/module/feed/"
    params = {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "module_id": "3003101",
        "count": "20",
        "filterGids": "",
        "presented_ids": "",
        "refer_id": "",
        "refer_type": "10",
        "awemePcRecRawData": "{\"is_client\":false}",
        "Seo-Flag": "0",
        "install_time": "1685075906",
        "pc_client_type": "1",
        "version_code": "170400",
        "version_name": "17.4.0",
        "cookie_enabled": "true",
        "screen_width": "1536",
        "screen_height": "864",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Chrome",
        "browser_version": "114.0.0.0",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "114.0.0.0",
        "os_name": "Windows",
        "os_version": "10",
        "cpu_core_num": "8",
        "device_memory": "8",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "100",
        "webid": "7237345871913076283",
        "msToken": "te2BFr5x25GZ0vk6zP22wGOjJmyTn0zz9JwPEPCuzvPbEGP22aBVXbn5vN53cg3maN9OHVZFc0SKzGvemg4hCYNT1S8F0OfCuIQ4Qo_Fux5WXzZIh677",
    }
    url_path = urlencode(params, safe='=')
    # print(url_path)
    params["X-Bogus"] = execjs.compile(open('douyin.js', 'r', encoding="utf-8").read()).call("get_x_bogus", url_path)
    # print(params)
    response = requests.post(url=url, headers=headers, cookies=cookies, params=params)
    print(response.text)

if __name__ == '__main__':
    get_douyin()
