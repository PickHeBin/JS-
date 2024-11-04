const CryptoJs = require('crypto-js')

window = global;

var o = CryptoJs.MD5("getUtilsFromFile")
a = CryptoJs.enc.Utf8.parse(o);
var u = CryptoJs.enc.Utf8.parse("getClassFromFile");
window.d = function(t) {
    return CryptoJs.AES.decrypt(t, a, {
        iv: u,
        mode: CryptoJs.mode.CBC,
        padding: CryptoJs.pad.Pkcs7
    }).toString(CryptoJs.enc.Utf8).toString()
}


function main123(popularityList) {
    scriptData = window.d(popularityList)
    scriptData = eval(scriptData)
    return scriptData
}

