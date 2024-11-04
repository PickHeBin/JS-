const CryptoJs = require('crypto-js');

function main123(time1) {
    // params = 'app=CailianpressWeb&category=&lastTime=' + time1 + '&last_time=' + time1 + '&os=web&refresh_type=1&rn=20&sv=7.7.5'
    t = CryptoJs.SHA1(params).toString()
    sign = CryptoJs.MD5(t).toString()
    return sign
}
params = 'app=CailianpressWeb&category=&lastTime=1712740446&last_time=1712740446&os=web&refresh_type=1&rn=20&sv=7.7.5'
console.log(main123(params))
