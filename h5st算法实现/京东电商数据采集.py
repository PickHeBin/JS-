import requests


headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "origin": "https://union.jd.com",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://union.jd.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "x-referer-page": "https://union.jd.com/proManager/index",
    "x-rp-client": "h5_1.0.0"
}
cookies = {
    "__jdu": "17156551507101203907074",
    "shshshfpa": "02958496-bae8-8466-a3b5-4226a4787e0c-1715655151",
    "shshshfpx": "02958496-bae8-8466-a3b5-4226a4787e0c-1715655151",
    "3AB9D23F7A4B3C9B": "DDDZ76BLTYYHX5YWYGKROZ6SM3OZCVM4QSE43FCHNBEF6THHTDZKBMRQ4Y577YB5B255JDYNI6T5ERMH7KJIUXVMWI",
    "ipLoc-djd": "1-72-55653-0",
    "__jda": "209449046.17156551507101203907074.1715655151.1716427449.1717397458.13",
    "__jdc": "209449046",
    "__jdv": "209449046|direct|-|none|-|1717397457890",
    "3AB9D23F7A4B3CSS": "jdd03DDDZ76BLTYYHX5YWYGKROZ6SM3OZCVM4QSE43FCHNBEF6THHTDZKBMRQ4Y577YB5B255JDYNI6T5ERMH7KJIUXVMWIAAAAMP3TOZHDAAAAAACPCDWSJUV6CMK4X",
    "__jdb": "209449046.2.17156551507101203907074|13.1717397458",
    "RT": "\"z=1&dm=jd.com&si=kadbqqmvdb&ss=lwym3r3e&sl=2&tt=1vj&ld=3ja\"",
    "shshshfpb": "BApXcwjrV3-pAYyqGSK9q0hF8K1Efvs_WBlckVn5v9xJ1MkzqX4C2"
}
url = "https://api.m.jd.com/api"
params = {
    "functionId": "unionSearch",
    "appid": "unionpc",
    "_": "1717397471373",
    "loginType": "3",
    "uuid": "17156551507101203907074",
    "x-api-eid-token": "jdd03DDDZ76BLTYYHX5YWYGKROZ6SM3OZCVM4QSE43FCHNBEF6THHTDZKBMRQ4Y577YB5B255JDYNI6T5ERMH7KJIUXVMWIAAAAMPUMGGUAAAAAAACKVNC5AWUQNYVEX",
    "h5st": "20240603150853702;6996g99gtiy5nmm2;586ae;tk03wb3e71ce518nlkwVEg0lTMXjpXT7BlH3mG1rNMdUI_KMmAm6fWkt1HXXvWs3acWS-8UeIzeg7JveNhJusWrkQtHt;3e3518c8f7d27f9357896dae396b732c31386236cdffbe51147ec17c98fc4801;4.7;1717398533702;TKmWAT6a5z6giLN51qeo-kJjJABOv4GsSM21tQJgnXD06pI4w81x_afp7AIU-ngzZ0Vypkqzgkm7lJHXis3qanI4LwrjslJnlP7luP4A8xYodkFDcgu31x3Sk0u4at3JitCN5VOB_zJUuG442R35b-ktK8Fa21C-7mNsyYQIWqt4p47GNYuKl5YxizGICBWE-TL29Uu-BSl6Jp4_jdTQrcVqrFgbgsAfa2fV3NG9kLVKbTrkcgaaP5sOLg17qAArrj5Gt46lZt-I04Cz-3MzWk2-CdGmYOeJ1j5Ok_tadIckFg4CY53VYs6qiz_Kv1PhWs5RggE7nDk8PeheJO0dl8zjLad9Prk3hGJ0DQIeqffFGvzEemLTD52YgeDqWQHLXbk3",
    "body": "{\"funName\":\"querySearchInfoByEliteId\",\"param\":{\"pageNo\":2,\"pageSize\":60,\"eliteId\":22},\"clientPageId\":\"jingfen_pc\"}"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params)

print(response.text)
print(response)

