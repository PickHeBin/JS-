


headers = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-anit-forge-token": "None",
    "x-anit-forge-code": "0"
}

e = {
    async: true,
    body: "first=true&needAddtionalResult=false&city=%E5%85%A8%E5%9B%BD&pn=3&fromSearch=true&kd=python",
    method: "POST",
    password: undefined,
    url: "https://www.lagou.com/jobs/v2/positionAjax.json",
    user: undefined,
    withCredentials: true,
    headers: headers
}
e.headers["X-S-HEADER"] = T.A2(e),
e.headers["X-K-HEADER"] = T.G5()