const CryptoJS = require('crypto-js')

// 核心加密位置  在函数或者方法当中返回加密内容的地方   加密内容被返回的位置从后往前推
It = function(t) {
    kt = CryptoJS.enc.Utf8.parse("bi8OM3BZJ=XSIZ7Iq1gvg5Y3QiWYH=aO"),
        Pt = CryptoJS.enc.Utf8.parse("c558Gq0YQK2QUlMc")
    t = CryptoJS.enc.Utf8.parse(t);
    t = CryptoJS.AES.encrypt(t, kt, {
        iv: Pt,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return t.toString()
}

// 拼接之后获取的内容
data = '{"deviceType":1}https://www.lagou.com/jobs/v2/positionAjax.json{"first":"true","needAddtionalResult":"false","city":"全国","pn":"3","fromSearch":"true","kd":"python"}'
t = CryptoJS.SHA256(data).toString().toUpperCase();
X_S = It(JSON.stringify({
    originHeader: JSON.stringify('{"deviceType":1}'),
    code: t
}))
console.log(X_S)
