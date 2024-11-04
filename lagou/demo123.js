const CryptoJs = require('crypto-js');

It = function(t) {
    Pt = CryptoJs.enc.Utf8.parse("c558Gq0YQK2QUlMc"),
    kt = CryptoJs.enc.Utf8.parse('tpfKPE5prwzeW3GQqkghZuQJvP/Z1v5Q'),
    t = CryptoJs.enc.Utf8.parse(t);
    t = CryptoJs.AES.encrypt(t, kt, {
        iv: Pt,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    });
    return t.toString()
};

e = {
    deviceType: 1
}
body = '{"first":"true","needAddtionalResult":"false","city":"全国","pn":"1","cl":"false","fromSearch":"true","labelWords":"sug","suginput":"爬虫逆向","kd":"爬虫逆向"}'
r = "https://www.lagou.com/jobs/v2/positionAjax.json"
t = CryptoJs.SHA256(e + r + body).toString().toUpperCase() // 第一次加密

// X-S-HEADER
X_S_HEADER = It(JSON.stringify({
    originHeader: JSON.stringify(e),
    code: t
}))
console.log(X_S_HEADER)


var s = function(t) {
    var e = 1 < arguments.length && void 0 !== arguments[1] && arguments[1]
      , t = t.substr(t.indexOf("?"))
      , r = new Object;
    if (-1 != t.indexOf("?"))
        for (var n = t.substr(1).split("&"), i = 0; i < n.length; i++) {
            var o = n[i].split("=");
            if ("null" !== o[1] && "undefined" !== o[1])
                try {
                    r[o[0]] = e ? o[1] : decodeURIComponent(o[1])
                } catch (t) {
                    r[o[0]] = o[1]
                }
        }
    return r
}

// 请求体生成
data = It(JSON.stringify(s("?".concat(body))))
console.log(data)