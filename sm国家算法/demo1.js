const CryptoJs = require('crypto-js');

e = '/api/job/search-pc?api_key=51job&timestamp=1693481259&keyword=python&searchType=2&function=&industry=&jobArea=000000&jobArea2=&landmark=&metro=&salary=&workYear=&degree=&companyType=&companySize=&jobType=&issueDate=&sortType=0&pageNum=4&requestId=c14246c1fed409d0d229824da6e88aff&pageSize=20&source=1&accountId=&pageCode=sou%7Csou%7Csoulb'
sign_key = 'abfc8f9dcf8c3f3d8aa294ac5f2cf2cc7767e5592590f39c3f503271dd68562b'

// 计算 SHA-256
const sha256Hash = CryptoJs.HmacSHA256(e, sign_key);

// 转换为十六进制字符串
const sha256Hex = sha256Hash.toString(CryptoJs.enc.Hex);
console.log(sha256Hex)