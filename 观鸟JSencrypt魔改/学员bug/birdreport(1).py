# -*- coding: utf-8 -*-            
# @Time : 2023/10/9 0009 10:38
#  :小东
# @FileName: birdreport.py
# @Software: PyCharm说明：
import json

import requests
# pip install pyexecjs2   安装
# pip install PyExecJS
# pip uninstall PyExecJS  删除
import execjs
import time
from lxml import etree

class Spider(object):
    def __init__(self):
        from_data = '{"limit":"20","page":"3"}'

        with open('./birdreport标头.js', 'r', encoding='utf-8') as f:
            js_code = f.read()
        # print(js_code)
        ctx = execjs.compile(js_code)
        get_sign = ctx.call('get_sign', from_data)
        print(get_sign)
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://www.birdreport.cn',
            'Pragma': 'no-cache',
            'Referer': 'http://www.birdreport.cn/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
            'requestId': get_sign,
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sign': get_sign,
            # 'timestamp': str(int(time.time()*1000)),
            'timestamp': str(get_sign),
        }

    def parse_start_url(self):
        # data = '{"limit":"20","page":"3"}'
        data = {
            'limit': '20',
            'page': '3'
        }
        data_str = json.dumps(data)
        print(data_str)
        datas = execjs.compile(open('birdreport载荷.js', 'r', encoding='utf-8').read()).call('get', data_str)
        # data = 'SqV2tfBiESR13KUVGjrKxdFZzJARrTFnZKinW9cnVYAJmlE01DHTom8rgIB5h5Af+iqhzBr166bIJoKYLscI81yP2Dd7ToMFWcuVol4fuunwpazXn50rwR8CnwksonaCGAkUNcErwllPwnQusquenVWcvSE//N+GzIdfMbH8qVE='
        print(datas)

        response = requests.post('https://api.birdreport.cn/front/activity/search', headers=self.headers, data=datas).json()
        # print(response)
        self.parse_response_js(response)

    def parse_response_js(self, response):
        print(response)
        data_list = execjs.compile(open('birdreport预览.js', 'r', encoding='utf-8').read()).call('decode', response)
        print(data_list)

    def parse_response_data(self, response):
        pass

    def parse_save(self, response):
        pass

if __name__ == '__main__':
    s = Spider()
    s.parse_start_url()