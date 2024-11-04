const CryptoJS = require('crypto-js');


function SHA256encrypt(text) {
    encrypt1 = CryptoJS.SHA256(text).toString()
    return encrypt1
}


userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36' + (new Date).getDate() + 'list'
console.log(SHA256encrypt('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.3620list'))


