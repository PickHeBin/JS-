const JSEncrypt = require('jsencrypt')

var encrypt = new JSEncrypt();
encrypt.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQClW5JGDbUNKLf8XdsDaQzCPiEsPevILUr24TNZRPKBve5cZw6/jns/FLkxl4i8Y/hF4qPUfJqRzqx2YXh/nrHOMPDI65OQBamzJYZOHv45KB6ctGFe76IezNSqvo6TSpzloajac7PdcRlZon0nscmwh03te0ghj0oT2dv/vLvBlQIDAQAB");
var password = encrypt.encrypt('123123123');
var name = encrypt.encrypt('1231231231');

console.log(name, password);