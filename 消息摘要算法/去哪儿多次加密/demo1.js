// npm install crypto-js
const CryptoJs = require('crypto-js');


function MD5encrypt(text) {
    return CryptoJs.MD5(text)
}

function SHA1encrypt(text) {
    return CryptoJs.SHA1(text)
}


function encrypt() {
    var t = '5e12102c-7746-47ac-b02e-886e1a6f69b4'  // 获取前端的html 提取这个值
        , n = new Date().getTime()
        , r = n % 2;  //  /除法 r  要么0 要么1
    // encryptFunction 下标  取出来的内容进行加密 t + n
    return encryptFunction()[r](t + n)
}


function encryptFunction() {
    // 0
    return [function (e) {
        var t = SHA1encrypt(e).toString();
        return MD5encrypt(t).toString()
    }
        // 1  f为md5加密  u为sha1加密算法
        , function (e) {
            var t = MD5encrypt(e).toString();
            return SHA1encrypt(t).toString()
        }
    ]
}


__m__ = MD5encrypt(encrypt()).toString();
console.log(__m__)


function getRandomKey(t) {
    var n = "";
    var r = ("" + t).substr(4); //
    r.split("").forEach(function(e) {
        n += e.charCodeAt()
    });
    var i = MD5encrypt(n).toString();
    return i.substr(-6)
}

// 头部参数参数加密
// this.getQtTime((0, s.default)(this.dencryptCode(this.qtTime)))  时间戳
function getToken() {
    var t = {};
    t[getRandomKey(new Date().getTime())] = encrypt();
    return t
}

console.log(getToken())

// t的赋值  被处理的内容  方法或者函数
// 115 = q   119 = u
// 数组固定
// this.tokenStr = [115, 119, 112, 99, 116, 97, 99, 114, 107, 97, 118, 113, 109, 103, 112]
// {
//     key: "getTokenStr",
//     value: function() {
//         var t = "qunar_api_token";
//         // document 内置方法 id选择器的获取
//         var n = document.getElementById('qunar_api_token').innerHTML;
//         return n ? n : (0,
//         s.default)(this.dencryptCode(this.cookieToken))
//     }
// }


