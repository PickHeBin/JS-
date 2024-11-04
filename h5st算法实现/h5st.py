import requests, random, time, hashlib, execjs
import json
import base64
from Crypto.Cipher import AES


def timestamp_to_custom_format(timestamp):
    # 将时间戳转换为struct_time
    time_struct = time.localtime(timestamp)

    # 根据指定格式生成字符串
    custom_format = "{:04d}{:02d}{:02d}{:02d}{:02d}{:02d}{:02d}".format(
        time_struct.tm_year, time_struct.tm_mon, time_struct.tm_mday,
        time_struct.tm_hour, time_struct.tm_min, time_struct.tm_sec,
        int((timestamp - int(timestamp)) * 1e6)
    )

    return custom_format


def pad(text):
    """
    #填充函数，使被加密数据的字节码长度是block_size的整数倍
    """
    count = len(text.encode('utf-8'))
    add = 16 - (count % 16)
    entext = text + (chr(add) * add)
    return entext.encode('utf-8')


def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# aes加密函数
def encrypt(text):
    # key 好像变了
    # key = 'wm0!@w_s#ll1flo('.encode('utf-8')
    key = 'HL4|FW#Chc3#q?0)'.encode('utf-8')
    iv = '0102030405060708'.encode('utf-8')
    text = add_to_16(text)
    cryptos = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    cipher_text = cryptos.encrypt(text).hex()
    # msg = str(base64.b64encode(cipher_text), encoding="utf8")
    return cipher_text


def pfive(colorParamSign, ts, fp, ai, tk, algo):
    # 这里不传入algo，函数会自动寻找这个algo = require('crypto-js')
    algo = algo.replace(',algo', '').replace(';}', '.toString();}')
    jscode = "const algo = require('crypto-js');" + algo
    jscode = json.loads(json.dumps(jscode))
    t = execjs.compile(jscode).call('test', tk, fp, ts, ai)

    # 字符串排列是有顺序的
    field = ['appid', 'body', 'client', 'clientVersion', 'functionId', 't']
    p = '&'.join([f'{i}:{colorParamSign[i]}' for i in field])

    # 这是加密的内容
    fin = t + p + t

    res = hashlib.md5(fin.encode()).hexdigest()

    return res


def peight(_fp, random1, user=""):
    n = f'''{{
      "sua": "Windows NT 10.0; Win64; x64",
      "pp": {{
        "p2": {user}
      }},
      "extend": {{
        "pm": 0,
        "wd": 0,
        "l": 0,
        "ls": 5,
        "wk": 0
      }},
      "random": {random1},
      "referer": "",
      "v": "v1.6.1",
      "fp": {_fp}
    }}'''

    return encrypt(n)


def get_fp():
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for _ in range(16))


def get_expandParams(_fp, _appId, random1):
    # js是以2个空格缩进
    data = f'''{{
  "wc": 0,
  "wd": 0,
  "l": "zh-CN",
  "ls": "zh-CN,en,en-GB,en-US",
  "ml": 2,
  "pl": 5,
  "av": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57",
  "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57",
  "sua": "Windows NT 10.0; Win64; x64",
  "pp": {{}},
  "extend": {{
    "pm": 0,
    "wd": 0,
    "l": 0,
    "ls": 5,
    "wk": 0
  }},
  "pp1": "_t=8TJ04o40hKxnO+2EO92XJjjrvkrBtKPDhGlcNDSll6k=; wlfstk_smdl=b4g9fi442vvrievig181uih1iuohp6x0; __jda=122270672.1697878324081130103773.1697878324.1697878324.1697878324.1; __jdb=122270672.1.1697878324081130103773|1.1697878324; __jdc=122270672; __jdv=122270672|direct|-|none|-|1697878324082; __jdu=1697878324081130103773; 3AB9D23F7A4B3C9B=JDG2SP5D2UJ23OUY3OGNHNJJVW55HVLBYJETTMA6AVRDYMHTQHTPCJKMLXAAKGSVAESEY2XK6OCWCW7YTNRGBEDMEU",
  "pm": {{
    "ps": "prompt",
    "np": "default"
  }},
  "w": 1504,
  "h": 1003,
  "ow": 1504,
  "oh": 955,
  "url": "https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fsearch.jd.com%2FSearch%3Fkeyword%3D%25E6%2589%258B%25E6%259C%25BA%26enc%3Dutf-8%26wq%3D%25E6%2589%258B%25E6%259C%25BA%26pvid%3D8858151673f941e9b1a4d2c7214b2b52",
  "og": "https://passport.jd.com",
  "pr": 1.5,
  "re": "",
  "random": {random1},
  "referer": "",
  "v": "v1.6.1",
  "ai": {_appId},
  "fp": {_fp},
}}'''

    return encrypt(data)


_fp = get_fp()
_appId = '73806'
random1 = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))
_expandParams = get_expandParams(_fp, _appId, random1)

#  第一次请求获取tk，algo
headers = {
    "authority": "cactus.jd.com",
    "accept": "application/json",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "origin": "https://passport.jd.com",
    "pragma": "no-cache",
    "referer": "https://passport.jd.com/",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Microsoft Edge\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57"
}
url = "https://cactus.jd.com/request_algo?g_ty=ajax"
_timestamp = int(time.time() * 1000)
data = {
    "version": "4.1",
    "fp": _fp,  # "nnnnmi9z6t3gn5c4",
    "appId": _appId,  # "73806",
    "timestamp": _timestamp,  # 1697871402885,
    "platform": "web",
    "expandParams": _expandParams,
    # "5e2976855ec13d55dbffcc514b657c9ec71b38bcd7d88f101ff260cf6b8a04fae8a99396e1282784963bc1d386b5684f19ff8d380cb911c1ff78c73f146daab96e0221221d9d000daab152be86bf4f0ed9c1b3d547d431a50d613e58431bef33e01ea7d3704fd6f1f6bd6e70c1646c68bf91309f66dcff0b5ea066beb1bc7db1189ffabb2ab64aea44005942412ad88397d22ad7b33e353d1fd833c6df4fc1ee6376552c02cbfe3c416fb8477294f888d8ba3c6fdc74eaa87919f274f130a2626aa9bd0d5b15db94cfcc7db7f3018270200699e555cd23cd0f09db0cb1affeef7b03dd1118630339f133349ac3b4f2ff11ca10e6fb225a1c329df6a46a57f7aa21f9463b5c804e52ca9479f4dc2be9c18a4610e3e57dceaece3c9e871c39541f515c6bcdd64f0a3e937d056af7406a4792aa0d4d6ced80a7503034e27284a872f8e48c1f24dddd97d026fd149c86c5fb5f9602a56f789d1b22da20f1cf4ced6df3e64db3584dc2d2a16a478a6427d6a988541f23e381427b47da9739acaa85d5035a9d86479f4ce3b8e4833b6d2ac21b674363164d8ed5ac8779983519153f43bf8c4837be52bef76597ca2151477168721a20dc2ac645920bc36ae722cb763752a92f535a2b74791f28f626f0e4945cf5123dfa37bd78b60daf93394632f5e9675f00860e733b3a7a373a2d06e5a4a710bb3a4623867b889506686e3471c6ece99e4fd534ade79c3c431e2d95227fce9d173467acddd4bd99db1c6eabbab72b66278eac32230b0d428456cc4a080feb6d1c31fac4e110eb06a879e16cc6c36fb47b73d6ba48b30cf5d8a8b2015d23175632f80e2ca8af3ed2d269a0a0ef57bec7dfa835046c9bb371bcf0b17d9a49631e267ea339931691f80c4e2d53d33a0f7f7f3c416e09b435dc02e76b748f72f5f04e53403edbcbddb57e88fc486d1fd1f487829a5c13552c42b28f742bc643a0749c8746f64fe68e5a8e13d0120755fe3c58696c4535cd7ac32fda99f3b744faaf124cf3ed7f50f22024a4471b22b270282bd98de40fa797401554234179b4f5f1a2c2ec145613818b616b9d3e65f4c6f6a9784c9de250b935e155150d5f9c47e85e5f7b8a4082c52848427d26b7f30cce4cbcccd1fa560fdfcdfff3a6d4c6fd9b7d4bbf0c5d3fab6e19eed4d30c5ba4183086ddb9108d03c33263496eab89b24b6a5a32ead26b0333d48de111926b0f70448335adadf5253f7f7d64c7a77b2dadde6d7afb656607bf2f91a4edb8c161a09e1351dc45053b947b25a11e4d68396185937801af75af67dc610bfe21bfcf6e006a3c1aa0d804cad05a3273e658c3d0c4d88bff5294e13f3608ebdee0f7bafe7cfca80029ca3ddc3914703c3cf80db942de1c4496081777942308c0e6180f9d7661508328ed538dd6f061c85aae0feceb16a898678fadde7f8c3543b5b3f05cb5e756cd9f8b0a20e3b1b870e5697ac6849c94934703055e7df8e0daa569e14dcaa2d91b06b08cc576d2df9764cdf3b92900b50079904b00fb92017f02091ac2cc6fd2bbeffff9f3ba922df7304c77d24eab9c729d5b3be12a40eff798541906e018c2a4729186bde6c75ea97a1f33597356be18fdd23c7a3af6a7c06a2aa58f7986e76ebbf86a37759e7136c1cc302bdef0995592425acca206bba3c9c66fa39c4051820c32569a8886e51aad8bf8352d9f2471bdcfbb7423cbc6de74f7e01aac562765b2cc1c696efbe787c69acdc0666fe6678272fb00d5a73c52c635a1fe878d90833a7ca75d96a17fd2cb237907d348c2e7ff819cc147d53b67e737dbd7b5a7b51690990f5c19f2dda2ab90aabbc53c7a128c601bb74949c2b4498f7095241b42dbe5062a4f3c57793032f394458b8c7baf8a2333f5c84d6cb37d5d8d108e4d96d445843a8e02e54cec914ead3fb7c2d6ff069942f12d860c471d25a2ab538c320e20b87964e6cf36736cf3cb3b55dccc7bc1b7cd6920693276877c65ab1d2c15c5414cddf63ba04e04c3709656928ae35e715bef245a2291f59da504efeda9ca8f5b59dc6d06de5807b75315e78298c8875df5b4d5877513af8de2805b0f1e3a04a24972314b94d72d5c43525d8f04f729c29c4ad5b423c553a121e277019a81987eba4dbcce1bc0feade6545ff208b30bf67a1215bcca6e66e1cf34b7ffabf2990766cbb42760ff539c0bff34e2eb3321edda21914bf228e6c24d23b69f3a2e4aeed154069c4253aea87286eabe9e8f70d58ac17e3b1e5cb75c3bc959f055e17e4c2ffa24e10b4f24fbe911dc6735826c62d5866291af7433f8ad1a885c2ebbdbaaf0e48c3ef50bdbfeff6a3f70504efcb255b5805311151d6fad6427d02cda25a3602067cadd1557d79cfac024f69a9c022f0f9461e0926def771ca0134e68d19645dce21809cf90dabdf44d5f290642a2342375abfc0f8e1c14695ee8ee498428c6e663dae0ed53197e9d48b65498a32b1c1979f15cea137197ad739212279ef570f8b3f1bb3c9d330bc9c83a594016dde50198498a7aa68432817084b8a3e612d926ff3b9ce8ea6bee26ebe755df95efea6cd07cdb31c8377f031ca33e88c2e299c41869a8c29616412274069a0195701c5920aaf8e47ab1e320a3061a45fd1ad3dd46831f7f052a3da4b86ccc3da03172659ab2d77c67128e0ce962cfdf5645b6c68c317135ba44a81f6caf2f2ccef2e3383a221c2c1cb405d45205c92b61d16fed06b874d65785e2b1c7ed46cd2555ef19668de5dbd90837e4d3c48ca1980b4752f5d841bce071c69ebdfab17bf57e4a6c3e949516e52f3da1f3b5da59bd3767ffd091d92b75263ab33fa281106f86c318e11a3f7263747df4b76565f9e5f3ee0021d6dee7a11e05dc",
    "fv": "v1.6.1"
}
# 去掉空格？
data = json.dumps(data, separators=(',', ':'))

res1 = requests.post(url, headers=headers, data=data)
# test = {"status":200,"message":"","data":{"version":"4.1","result":{"tk":"tk03w959e1b8c18n0qC9NBCedJadHQw7IqkKTbk8m5nWq0HubjxBh12CyjFFdZ0HFx_rUHbF41pmziMAA3PLXWmU-4fV","algo":"function test(tk,fp,ts,ai,algo){var rd='wv1vBZsx2uWX';var str=\"\".concat(tk).concat(fp).concat(ts).concat(ai).concat(rd);return algo.MD5(str);}","fp":"fjzpozz8kal7e9u1"}}}
test = json.loads(res1.text)['data']

_timestamp1 = time.time()
# 模拟js生成相应的载荷
colorParam = {
    "appid": "search-pc-java",
    "functionId": "pc_search_batch_stock",
    "client": "pc",
    "clientVersion": "1.0.0",
    "t": int(_timestamp1 * 1000),
    "body": "{\"sku\":\"10088894655557,10088894655567,10086987438005,10086987438002,10086987438003,10088985427554,10088985427564,10088985427602,10088985427583,10088985446819,10088985427593,10088987226989,10088987190396,10088987190366,10088987190407,10088987226913,10088987226995,10088987190374,10088987190342,10085216711936,10085216711950,10085216711940,10085216711947,10085216711951,10085216711946,10085216711939,10085216711948,10085216711941,10085216711942,10088418986269\",\"yushouFlag\":\"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\"}",
}

colorParamSign = json.loads(json.dumps(colorParam))
colorParamSign['body'] = hashlib.sha256(colorParam['body'].encode('utf-8')).hexdigest()
colorParam['loginType'] = '3'
colorParam['uuid'] = '122270672.16956463376741194422935.1695646337.1697785789.1697811907.10'
colorParam['area'] = '22_1930_0_0'

random2 = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(10))

p1 = timestamp_to_custom_format(_timestamp1)
p2 = get_fp()
p3 = 'f06cc'  # appid  这个每个平台不一样
p4 = test['result']['tk']  # 第一次请求返回的
# 通过test中的加密运算（algo中）得到t，p为传入的参数（原来的6个）用‘&’拼接起来。p5 = md5(t+p+t)
# "appid:search-pc-java&body:90155b191e797eb0e9fb8ee277e277caed5ea3f2ea40e08cd928f57cfa656545&client:pc&clientVersion:1.0.0&functionId:pc_search_batch_stock&t:1697988702046"
p5 = pfive(colorParamSign, p1, p2, p3, p4, test['result']['algo'])
p6 = test['version']  # h5st的版本
p7 = str(int(_timestamp1 * 1000))
p8 = peight(p2, random2, user="xsstc000")  # 一段aes加密的数据

# 生成h5st
colorParam['h5st'] = ';'.join([p1, p2, p3, p4, p5, p6, p7, p8])
print(colorParam)

# x-api-eid-token 其实是jsToken，通过https://gia.jd.com/jsTk.do?...  获取。目前如果不影响，先不管
colorParam[
    'x-api-eid-token'] = "jdd03Y6QMWTR4V7DY46PB4QYKRAY2MFWM6GDF6IODVKU5FAJRN266M7XD2VL3RZJVNIZDTWTLPURHIWPJ7DIDSNBGA6ZW7YAAAAMLLBRUIFQAAAAACMVRBZ5L3XMOD4X"
# print(colorParam)

headers2 = {
    "authority": "api.m.jd.com",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "origin": "https://list.jd.com",
    "pragma": "no-cache",
    "referer": "https://list.jd.com/",
    "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "x-referer-page": "https://list.jd.com/list.html",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "__jdu": "2044398698",
    "areaId": "22",
    "ipLoc-djd": "22-1930-0-0",
    "PCSYCityID": "CN_510000_510100_0",
    "shshshfpa": "d9905620-c484-eaa4-c836-df0c61efb4fb-1679896337",
    "shshshfpx": "d9905620-c484-eaa4-c836-df0c61efb4fb-1679896337",
    "TrackID": "1StDs13AOQkqghHvRYDLNpP1CkuSEnOkcYO7Fnr6P6na4osATNptcC3JL_iQxSjc0E0OlBY54VE9pWHj9vrrjpKBooc6nPByr4aQeVOPxZjQ",
    "thor": "138DFC9246DE168DDD361D10AC8D4AF3ED86E3477EB83A07032CF28EC40584615E95A25C3080BC0DEE22C2A674555A18A1EEED30589FF82320B75DCEA2DE607A81FCF5CBEE224804869A6F76E71C8A21476D6398C542C3D17C27866D18AD701AC39EA412D8BFA276B9D1A6A9D6A7ADC9BE172579A2538EFB1646D9E2E26B0905C5803EF0A841F4496568B4E682F8A72F",
    "flash": "2_Ya8fKKupVHK5cuTcIjhj2uY6hc-9kAS47wwN5GDp0ELLhkfHNo2S-lexAvAzogaSLNln96b6sWDgBisDuEyF0deHpEGWPx7xu4L2gZgoZdp*",
    "pinId": "kxrI2hz-gZi1ffsfn98I-w",
    "pin": "xsstc000",
    "unick": "xsstc000",
    "_tp": "tSbJApggcDGFM2%2Bst99zjw%3D%3D",
    "_pst": "xsstc000",
    "unpl": "JF8EAK9nNSttWkxXDU4KGxRFTVlUW11fGB9TbmYBXFRdQgFVSwMdRhh7XlVdXxRLFh9sZBRXX1NJVA4aBysSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrARoXFUlVXVlVAXsWM2hXNWRYWkNTBSsDKxMgCQkIWlgOSh4KImQEUVhaQ10CEwsrEyBI",
    "__jdv": "76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_3629d917d75141fb9a0059848daa07e9|1697988664421",
    "__jdc": "122270672",
    "jsavif": "1",
    "3AB9D23F7A4B3C9B": "Y6QMWTR4V7DY46PB4QYKRAY2MFWM6GDF6IODVKU5FAJRN266M7XD2VL3RZJVNIZDTWTLPURHIWPJ7DIDSNBGA6ZW7Y",
    "__jda": "122270672.2044398698.1697889522.1697992810.1697994981.7",
    "__jdb": "122270672.2.2044398698|7.1697994981",
    "shshshsID": "c6cc29c594c9864c47d5a4a0216103cc_1_1697994982127",
    "3AB9D23F7A4B3CSS": "jdd03Y6QMWTR4V7DY46PB4QYKRAY2MFWM6GDF6IODVKU5FAJRN266M7XD2VL3RZJVNIZDTWTLPURHIWPJ7DIDSNBGA6ZW7YAAAAMLLBRUIFQAAAAACMVRBZ5L3XMOD4X",
    "shshshfpb": "AAt1EY1iLEpBWIMSE6qTINt8MYe-0-xZ5iWM3fwAAAAA"
}
url = "https://api.m.jd.com/"

# params = {
#     "appid": "search-pc-java",
#     "functionId": "pc_search_batch_stock",
#     "client": "pc",
#     "clientVersion": "1.0.0",
#     "t": "1697994982236",
#     "body": "{\"sku\":\"10088894655557,10088894655567,10086987438005,10086987438002,10086987438003,10088985427554,10088985427564,10088985427602,10088985427583,10088985446819,10088985427593,10088987226989,10088987190396,10088987190366,10088987190407,10088987226913,10088987226995,10088987190374,10088987190342,10085216711936,10085216711950,10085216711940,10085216711947,10085216711951,10085216711946,10085216711939,10085216711948,10085216711941,10085216711942,10088418986269\",\"yushouFlag\":\"0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000\"}",
#     "loginType": "3",
#     "uuid": "122270672.2044398698.1697889522.1697992810.1697994981.7",
#     "area": "22_1930_0_0",
#     "h5st": "20231023012526735;z95595nmit6g39u2;f06cc;tk03wdef11d4818ngbFTYpsnindY0jFXRcesWyNkgpbmOrSJCNbck1x4AW-Kig1-aeX7Nt58pu9-3vhkmeQzAKmyDsni;97e1acafdf3e5f9b6a4e95cf06ce228e;4.1;1697995526735;ee3cf7f6b94dc20e9265d83066bb9ceece4bb89e2b7e8bf5afb1bfd928788174bfa06c210ddd4437d8a2e234330c3a393d3a32715073dcb713466b4ec88cfd1bd1615f0c6b2e305df2d7402480a94f99bfea2c7acb9dceb093035d133dcb7268d3f11b1c6221032a4db725c2ae4874eb831172a84ee0ed68f0cbe44637505302bbd6c775b9c70bcaf68b4d91590bfbf990ecc2a6772dbbb48f017aecbc38bd642890ec4b3f3941464ea57e2b82b5b49036b7c893084a1ca94e31c52556aacf663884a5f9bd65037716279cb0ab5ab95f80824dc3f39bd3a1db55227f8ffb08626d4841bc83f8908b5aeec1a59e07e2b7fd6a335a3932f5912d52cfb85e39a02e",
#     "x-api-eid-token": "jdd03Y6QMWTR4V7DY46PB4QYKRAY2MFWM6GDF6IODVKU5FAJRN266M7XD2VL3RZJVNIZDTWTLPURHIWPJ7DIDSNBGA6ZW7YAAAAMLLBRUIFQAAAAACMVRBZ5L3XMOD4X"
# }

# colorParam = json.dumps(colorParam, separators=(',', ':'))
# # print(colorParam)
# response = requests.get(url, headers=headers2, cookies=cookies, params=colorParam)
#
# print(response.text)
# print(response.status_code)
