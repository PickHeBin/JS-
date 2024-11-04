import execjs

arg = [
    0,
    1,
    14,
    "device_platform=webapp&aid=6383&channel=channel_pc_web&update_version_code=170400&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=2560&screen_height=1440&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=124.0.0.0&browser_online=true&engine_name=Blink&engine_version=124.0.0.0&os_name=Windows&os_version=10&cpu_core_num=24&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=100&webid=7365164801045464603&msToken=yDg-WhJQr4PExmOuVFUCSIYj3dG1gVmy5MHF6jMpmUG7vxWjaMxryHnfAy18UePyxPJYr3MSsQsoLhVeMu4CRKAcyRd9pS8nioBy-jH13KVNvIEXrbSaWLQ3Hgw93w%3D%3D&msToken=yDg-WhJQr4PExmOuVFUCSIYj3dG1gVmy5MHF6jMpmUG7vxWjaMxryHnfAy18UePyxPJYr3MSsQsoLhVeMu4CRKAcyRd9pS8nioBy-jH13KVNvIEXrbSaWLQ3Hgw93w%3D%3D",
    "",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
]

js_file_path = 'bogusCode.js'

# with open(file=js_file_path, mode='r',encoding='gbk') as f:
#     js_source = f.read()
# ctx = execjs.compile(js_source)
# result = ctx.call('get_a_bogus', arg)
# print(result)

with open(file=js_file_path, mode='r',encoding='utf-8') as f:
    js_source = f.read()
ctx = execjs.compile(js_source)
result = ctx.call('get_ab', arg)
print(result)