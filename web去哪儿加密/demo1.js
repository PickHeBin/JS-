// (0, l["default"])(h["default"].encrypt()).toString()

// h["default"].encrypt()
// (0, l["default"])(h["default"].encrypt()).toString()


function encrypt() {
    var t = '5e12102c-7746-47ac-b02e-886e1a6f69b4'
        , n = 1694005066257
        , r = n % 2;
    return encryptFunction()[r](t + n)
}
function encryptFunction() {
    return [function(e) {
        var t = (0,
        s["default"])(e).toString();// SHA1
        return (0,
        u["default"])(t).toString()// md5加密
    }

    , function(e) {
        var t = (0,
        u["default"])(e).toString(); // md5加密
        return (0,
        s["default"])(t).toString()  // SHA1
    }
    ]
}

console.log(encrypt())