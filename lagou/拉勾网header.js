
const CryptoJs = require('crypto-js')
window ={}

Kt = function () {
    var t = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : ""
        , r = "";
    return -1 < t.indexOf("?") && t.split("?")[1].split("&").filter(function (t) {
        return !!t
    }).map(function (t, e) {
        t && (t = t.split("="),
            r += (0 === e ? "?" : "&").concat(t[0], "=").concat(encodeURIComponent(decodeURIComponent(t[1]))))
    }),
        r = t.split("?")[0] + r
}
    , Zt = function () {
    var t = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {}
        , e = ""
        , r = t.method
        , r = void 0 === r ? "get" : r
        , t = t.body;
    return "post" === r.toLowerCase() && t && (t = Gt(t) ? JSON.parse(t) : (0,
        _t.$Z)("?".concat(t)),
        e = Object.keys(t).length ? JSON.stringify(t) : ""),
        e
}


Pt = {
    "words": [
        1664431416,
        1198600281,
        1363882577,
        1433161059
    ],
    "sigBytes": 16
}


It = function(t) {
    kt = CryptoJs.enc.Utf8.parse('ZzhOpckwNeUQqZWgCkHNPlUIVcNmpaQh'),
        t = CryptoJs.enc.Utf8.parse(t);
    t = CryptoJs.AES.encrypt(t, kt, {
        iv: Pt,
        mode: CryptoJs.mode.CBC,
                        padding: CryptoJs.pad.Pkcs7
                    });
                    return t.toString()
                }

Ut = function () {
    var t = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {}
        , e = t.url
        , r = (void 0 === e ? "" : e).replace("https://gate.lagou.com", "").replace("https://activity.lagou.com", "")
        , e = {
        deviceType: 1
    }
        , t = "".concat(JSON.stringify(e)).concat(Kt(r)).concat(Zt(t))
        , t = (t = t,
        null === (t = CryptoJs.SHA256(t).toString()) || void 0 === t ? void 0 : t.toUpperCase());
    return It(JSON.stringify({
        originHeader: JSON.stringify(e),
        code: t
    }))
}


//t = '65515D5485F2072D317C99C2F046BF35BEE3E205FB97F8C8A2664229F3A6EAB4'
e = {
    "method": "get",
    "headers": {
        "content-type": "application/json;charset=UTF-8",
        "x-l-req-header": "{deviceType:1}"
    },
    "credentials": "include",
    "url": "https://gate.lagou.com/v1/entry/position/getPositionInfo?positionId=11248515"
}

console.log(Ut(e))


//0zJPWgVmcYzYEk/1lD2bOQd0yZ9vPy3rp//us2XeK/OCzxpsgsK0+W9kPs2vB2LOWTRO/YPq1y2nr/hL+sfUhpTh5zuIZAeGNDxLHpcQ4xei8m6nMoQgf/c9/N/mT7cx2Mh7RAtecL30JnSggXLqy6+Vi8xrRm1JN+d0M7rMFWRdNj6r4S3QvVvvNUlFQ8MT
//t8Un6cSVmInr21TbuQi/gCtuyTWzJUdqXWHFOkrnncZH2rLR0Lvhlw2NbRrEmcbQuZLIgrTMOEB2QPz8BGuEFVZzGPy3rVexhJuYx81hK2a9VywIa+Zb5ZISY2EfHC/W3Csiyww22rmut3FU3XjAeA==
//t8Un6cSVmInr21TbuQi/gCtuyTWzJUdqXWHFOkrnncabWIckA52ajA6j4ftjDIpATtsUkb5fLZ+E1bMfzyGq8J0z7lb6vOgTj/Ld5qmk53sG8k4wjNag+S0rXEqQal/btcMY86RAhW8ew0gzT0PWXA==
//'t8Un6cSVmInr21TbuQi/gCtuyTWzJUdqXWHFOkrnncZ7iE715bWQcmXO4RKE4ga7SPBH/+gWwiknmytBUbQOtSwxV471arP4s+cr8KAZ4BNsXv8VOSa8DLKSm9BMBx2pUesVy9+LKxVOrvZuwHN10w=='
//t8Un6cSVmInr21TbuQi/gCtuyTWzJUdqXWHFOkrnncaAw7o4VQAlEBnWLj4uOAalZzADSMdUQDj/S3bMxVn5HtJoIIaQtdY5M8gp8nLA74+29BcXYDOoH6GI/Ir9WhDW+hrvUnJBYaqJhoz0HrlVsA==



//t8Un6cSVmInr21TbuQi/gCtuyTWzJUdqXWHFOkrnncamWzv7ZCJ85E/zURJCejix0CLeBbBpin9cN30A1UXWNOmAbcEJuqvk3u4zlLGHVxGoVGlDT6RPFefEn+Oc+Oi+6GuuO+1eb26BuzIpGpajMQ==
//t8Un6cSVmInr21TbuQi/gCtuyTWzJUdqXWHFOkrnncamWzv7ZCJ85E/zURJCejix0CLeBbBpin9cN30A1UXWNOmAbcEJuqvk3u4zlLGHVxGoVGlDT6RPFefEn+Oc+Oi+6GuuO+1eb26BuzIpGpajMQ==