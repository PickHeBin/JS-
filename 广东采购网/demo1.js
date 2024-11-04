const CryptoJs = require('crypto-js');
const JSEncrypt = require('jsencrypt'); // 魔改的对象  版本问题

function getCommon() {
    return "/freecms";
}


function signReturn() {
    var url = getCommon() + '/rest/v1/notice/selectInfoMoreChannel.do';
    var nowTime = new Date().getTime();
    // sign的生成结果
    var encryptContent = CryptoJs.MD5(CryptoJs.SHA1(nowTime+'_'+String(url).split('?')[0]+'_bosssoft_platform_095285').toString()).toString();
    return encryptContent
}


function encryptByRSA(value) {
    var encrypt = new JSEncrypt();
    var RSAPublicKey = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCS2TZDs5+orLYCL5SsJ54+bPCV\n" + "s1ZQQwP2RoPkFQF2jcT0HnNNT8ZoQgJTrGwNi5QNTBDoHC4oJesAVYe6DoxXS9Nl\n" + "s8WbGE8ZNgOC5tVv1WVjyBw7k2x72C/qjPoyo/kO7TYl6Qnu4jqW/ImLoup/nsJp\n" + "pUznF0YgbyU/dFFNBQIDAQAB";
    encrypt.setPublicKey('-----BEGIN PUBLIC KEY-----' + RSAPublicKey + '-----END PUBLIC KEY-----')
    // 放置自己的公钥
    return encrypt.encrypt(value)
}
function RSAReturn() {
    // RSA加密
    Nsssjss = encryptByRSA(getCommon() + '/rest/v1/notice/selectInfoMoreChannel.do' + '$$'+ new Date().getTime())
    return Nsssjss
}









