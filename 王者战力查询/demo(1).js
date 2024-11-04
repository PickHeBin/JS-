

var Hay = {
    hexcase: 0,
    hex_md5: function (_0x150983) {
        return this.rstr2hex(this.rstr_md5(this.str2rstr_utf8(_0x150983)));
    },
    hex_hmac_md5: function (_0x3d4cd9, _0x1d5aa4) {
        return this.rstr2hex(this.rstr_hmac_md5(this.str2rstr_utf8(_0x3d4cd9), this.str2rstr_utf8(_0x1d5aa4)));
    },
    md5_vm_test: function () {
        return this.hex_md5("abc").toLowerCase() == "900150983cd24fb0d6963f7d28e17f72";
    },
    rstr_md5: function (_0x23d3eb) {
        return this.binl2rstr(this.binl_md5(this.rstr2binl(_0x23d3eb), _0x23d3eb.length * 8));
    },
    rstr_hmac_md5: function (_0x439de4, _0x2ed21b) {
        var _0x230bbe = this.rstr2binl(_0x439de4);
        if (_0x230bbe.length > 16) {
            _0x230bbe = this.binl_md5(_0x230bbe, _0x439de4.length * 8);
        }
        var _0x3fe1bc = Array(16);
        var _0x4102c2 = Array(16);
        for (var _0x3769d1 = 0; _0x3769d1 < 16; _0x3769d1++) {
            _0x3fe1bc[_0x3769d1] = _0x230bbe[_0x3769d1] ^ 909522486;
            _0x4102c2[_0x3769d1] = _0x230bbe[_0x3769d1] ^ 1549556828;
        }
        var _0x443ff1 = this.binl_md5(_0x3fe1bc.concat(this.rstr2binl(_0x2ed21b)), 512 + _0x2ed21b.length * 8);
        return this.binl2rstr(this.binl_md5(_0x4102c2.concat(_0x443ff1), 640));
    },
    rstr2hex: function (_0x8a8f9c) {
        try {
            hexcase;
        } catch (_0x334be1) {
            hexcase = 0;
        }
        var _0x1cc58d = hexcase ? "0123456789ABCDEF" : "0123456789abcdef";
        var _0x55b834 = "";
        var _0x1d36a2;
        for (var _0x37acdf = 0; _0x37acdf < _0x8a8f9c.length; _0x37acdf++) {
            _0x1d36a2 = _0x8a8f9c.charCodeAt(_0x37acdf);
            _0x55b834 += _0x1cc58d.charAt(_0x1d36a2 >>> 4 & 15) + _0x1cc58d.charAt(_0x1d36a2 & 15);
        }
        return _0x55b834;
    },
    str2rstr_utf8: function (_0x3a38d6) {
        var _0x24532a = "";
        var _0x510cb3 = -1;
        var _0x21f0cb;
        var _0x179dc7;
        while (++_0x510cb3 < _0x3a38d6.length) {
            _0x21f0cb = _0x3a38d6.charCodeAt(_0x510cb3);
            _0x179dc7 = _0x510cb3 + 1 < _0x3a38d6.length ? _0x3a38d6.charCodeAt(_0x510cb3 + 1) : 0;
            if (_0x21f0cb >= 55296 && _0x21f0cb <= 56319 && _0x179dc7 >= 56320 && _0x179dc7 <= 57343) {
                _0x21f0cb = 65536 + ((_0x21f0cb & 1023) << 10) + (_0x179dc7 & 1023);
                _0x510cb3++;
            }
            if (_0x21f0cb <= 127) {
                _0x24532a += String.fromCharCode(_0x21f0cb);
            } else if (_0x21f0cb <= 2047) {
                _0x24532a += String.fromCharCode(_0x21f0cb >>> 6 & 31 | 192, _0x21f0cb & 63 | 128);
            } else if (_0x21f0cb <= 65535) {
                _0x24532a += String.fromCharCode(_0x21f0cb >>> 12 & 15 | 224, _0x21f0cb >>> 6 & 63 | 128, _0x21f0cb & 63 | 128);
            } else if (_0x21f0cb <= 2097151) {
                _0x24532a += String.fromCharCode(_0x21f0cb >>> 18 & 7 | 240, _0x21f0cb >>> 12 & 63 | 128, _0x21f0cb >>> 6 & 63 | 128, _0x21f0cb & 63 | 128);
            }
        }
        return _0x24532a;
    },
    rstr2binl: function (_0x486760) {
        var _0x23f392 = Array(_0x486760.length >> 2);
        for (var _0x49d49a = 0; _0x49d49a < _0x23f392.length; _0x49d49a++) {
            _0x23f392[_0x49d49a] = 0;
        }
        for (var _0x49d49a = 0; _0x49d49a < _0x486760.length * 8; _0x49d49a += 8) {
            _0x23f392[_0x49d49a >> 5] |= (_0x486760.charCodeAt(_0x49d49a / 8) & 255) << _0x49d49a % 32;
        }
        return _0x23f392;
    },
    binl2rstr: function (_0x180269) {
        var _0x2299e4 = "";
        for (var _0x2525d3 = 0; _0x2525d3 < _0x180269.length * 32; _0x2525d3 += 8) {
            _0x2299e4 += String.fromCharCode(_0x180269[_0x2525d3 >> 5] >>> _0x2525d3 % 32 & 255);
        }
        return _0x2299e4;
    },
    binl_md5: function (_0x54475e, _0x37f886) {
        _0x54475e[_0x37f886 >> 5] |= 128 << _0x37f886 % 32;
        _0x54475e[(_0x37f886 + 64 >>> 9 << 4) + 14] = _0x37f886;
        var _0xa6de8f = 1732584193;
        var _0x182d60 = -271733879;
        var _0x5bfef8 = -1732584194;
        var _0x4c12cf = 271733878;
        for (var _0x12d6cb = 0; _0x12d6cb < _0x54475e.length; _0x12d6cb += 16) {
            var _0x2975a7 = _0xa6de8f;
            var _0x3b8507 = _0x182d60;
            var _0x19f391 = _0x5bfef8;
            var _0x5c11b4 = _0x4c12cf;
            _0xa6de8f = this.md5_ff(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 0], 7, -680876936);
            _0x4c12cf = this.md5_ff(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 1], 12, -389564586);
            _0x5bfef8 = this.md5_ff(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 2], 17, 606105819);
            _0x182d60 = this.md5_ff(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 3], 22, -1044525330);
            _0xa6de8f = this.md5_ff(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 4], 7, -176418897);
            _0x4c12cf = this.md5_ff(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 5], 12, 1200080426);
            _0x5bfef8 = this.md5_ff(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 6], 17, -1473231341);
            _0x182d60 = this.md5_ff(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 7], 22, -45705983);
            _0xa6de8f = this.md5_ff(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 8], 7, 1770035416);
            _0x4c12cf = this.md5_ff(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 9], 12, -1958414417);
            _0x5bfef8 = this.md5_ff(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 10], 17, -42063);
            _0x182d60 = this.md5_ff(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 11], 22, -1990404162);
            _0xa6de8f = this.md5_ff(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 12], 7, 1804603682);
            _0x4c12cf = this.md5_ff(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 13], 12, -40341101);
            _0x5bfef8 = this.md5_ff(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 14], 17, -1502002290);
            _0x182d60 = this.md5_ff(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 15], 22, 1236535329);
            _0xa6de8f = this.md5_gg(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 1], 5, -165796510);
            _0x4c12cf = this.md5_gg(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 6], 9, -1069501632);
            _0x5bfef8 = this.md5_gg(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 11], 14, 643717713);
            _0x182d60 = this.md5_gg(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 0], 20, -373897302);
            _0xa6de8f = this.md5_gg(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 5], 5, -701558691);
            _0x4c12cf = this.md5_gg(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 10], 9, 38016083);
            _0x5bfef8 = this.md5_gg(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 15], 14, -660478335);
            _0x182d60 = this.md5_gg(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 4], 20, -405537848);
            _0xa6de8f = this.md5_gg(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 9], 5, 568446438);
            _0x4c12cf = this.md5_gg(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 14], 9, -1019803690);
            _0x5bfef8 = this.md5_gg(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 3], 14, -187363961);
            _0x182d60 = this.md5_gg(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 8], 20, 1163531501);
            _0xa6de8f = this.md5_gg(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 13], 5, -1444681467);
            _0x4c12cf = this.md5_gg(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 2], 9, -51403784);
            _0x5bfef8 = this.md5_gg(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 7], 14, 1735328473);
            _0x182d60 = this.md5_gg(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 12], 20, -1926607734);
            _0xa6de8f = this.md5_hh(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 5], 4, -378558);
            _0x4c12cf = this.md5_hh(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 8], 11, -2022574463);
            _0x5bfef8 = this.md5_hh(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 11], 16, 1839030562);
            _0x182d60 = this.md5_hh(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 14], 23, -35309556);
            _0xa6de8f = this.md5_hh(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 1], 4, -1530992060);
            _0x4c12cf = this.md5_hh(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 4], 11, 1272893353);
            _0x5bfef8 = this.md5_hh(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 7], 16, -155497632);
            _0x182d60 = this.md5_hh(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 10], 23, -1094730640);
            _0xa6de8f = this.md5_hh(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 13], 4, 681279174);
            _0x4c12cf = this.md5_hh(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 0], 11, -358537222);
            _0x5bfef8 = this.md5_hh(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 3], 16, -722521979);
            _0x182d60 = this.md5_hh(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 6], 23, 76029189);
            _0xa6de8f = this.md5_hh(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 9], 4, -640364487);
            _0x4c12cf = this.md5_hh(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 12], 11, -421815835);
            _0x5bfef8 = this.md5_hh(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 15], 16, 530742520);
            _0x182d60 = this.md5_hh(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 2], 23, -995338651);
            _0xa6de8f = this.md5_ii(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 0], 6, -198630844);
            _0x4c12cf = this.md5_ii(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 7], 10, 1126891415);
            _0x5bfef8 = this.md5_ii(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 14], 15, -1416354905);
            _0x182d60 = this.md5_ii(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 5], 21, -57434055);
            _0xa6de8f = this.md5_ii(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 12], 6, 1700485571);
            _0x4c12cf = this.md5_ii(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 3], 10, -1894986606);
            _0x5bfef8 = this.md5_ii(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 10], 15, -1051523);
            _0x182d60 = this.md5_ii(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 1], 21, -2054922799);
            _0xa6de8f = this.md5_ii(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 8], 6, 1873313359);
            _0x4c12cf = this.md5_ii(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 15], 10, -30611744);
            _0x5bfef8 = this.md5_ii(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 6], 15, -1560198380);
            _0x182d60 = this.md5_ii(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 13], 21, 1309151649);
            _0xa6de8f = this.md5_ii(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf, _0x54475e[_0x12d6cb + 4], 6, -145523070);
            _0x4c12cf = this.md5_ii(_0x4c12cf, _0xa6de8f, _0x182d60, _0x5bfef8, _0x54475e[_0x12d6cb + 11], 10, -1120210379);
            _0x5bfef8 = this.md5_ii(_0x5bfef8, _0x4c12cf, _0xa6de8f, _0x182d60, _0x54475e[_0x12d6cb + 2], 15, 718787259);
            _0x182d60 = this.md5_ii(_0x182d60, _0x5bfef8, _0x4c12cf, _0xa6de8f, _0x54475e[_0x12d6cb + 9], 21, -343485551);
            _0xa6de8f = this.safe_add(_0xa6de8f, _0x2975a7);
            _0x182d60 = this.safe_add(_0x182d60, _0x3b8507);
            _0x5bfef8 = this.safe_add(_0x5bfef8, _0x19f391);
            _0x4c12cf = this.safe_add(_0x4c12cf, _0x5c11b4);
        }
        return Array(_0xa6de8f, _0x182d60, _0x5bfef8, _0x4c12cf);
    },
    md5_cmn: function (_0x2e0d69, _0x167bb5, _0x1866de, _0x5e453a, _0x5763ab, _0x3fd71a) {
        return this.safe_add(this.bit_rol(this.safe_add(this.safe_add(_0x167bb5, _0x2e0d69), this.safe_add(_0x5e453a, _0x3fd71a)), _0x5763ab), _0x1866de);
    },
    md5_ff: function (_0xcca110, _0x436da3, _0x114760, _0x57ccc2, _0x58020a, _0xb9e27b, _0x4917a1) {
        return this.md5_cmn(_0x436da3 & _0x114760 | ~_0x436da3 & _0x57ccc2, _0xcca110, _0x436da3, _0x58020a, _0xb9e27b, _0x4917a1);
    },
    md5_gg: function (_0x43270e, _0x42db8f, _0x106e49, _0x950146, _0x56a5df, _0xc10ca5, _0x35182d) {
        return this.md5_cmn(_0x42db8f & _0x950146 | _0x106e49 & ~_0x950146, _0x43270e, _0x42db8f, _0x56a5df, _0xc10ca5, _0x35182d);
    },
    md5_hh: function (_0x3542e2, _0x2d709d, _0x38081c, _0x44f816, _0x213714, _0x42ba31, _0x42379c) {
        return this.md5_cmn(_0x2d709d ^ _0x38081c ^ _0x44f816, _0x3542e2, _0x2d709d, _0x213714, _0x42ba31, _0x42379c);
    },
    md5_ii: function (_0x394230, _0x44db95, _0x3e5f2c, _0x4311af, _0x493f10, _0x2ed6fb, _0x1c4d45) {
        return this.md5_cmn(_0x3e5f2c ^ (_0x44db95 | ~_0x4311af), _0x394230, _0x44db95, _0x493f10, _0x2ed6fb, _0x1c4d45);
    },
    safe_add: function (_0x367ddc, _0x4561d5) {
        var _0x544557 = (_0x367ddc & 65535) + (_0x4561d5 & 65535);
        var _0x3e0df6 = (_0x367ddc >> 16) + (_0x4561d5 >> 16) + (_0x544557 >> 16);
        return _0x3e0df6 << 16 | _0x544557 & 65535;
    },
    bit_rol: function (_0x5aaee3, _0x537163) {
        return _0x5aaee3 << _0x537163 | _0x5aaee3 >>> 32 - _0x537163;
    },
    base64_encode: function (_0x26509e) {
        var _0x5ca930 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        var _0x1e634c;
        var _0x263dcf;
        var _0x46760c;
        var _0x4b3c98;
        var _0x1b7bc1;
        var _0x1492ee;
        _0x46760c = _0x26509e.length;
        _0x263dcf = 0;
        _0x1e634c = "";
        while (_0x263dcf < _0x46760c) {
            _0x4b3c98 = _0x26509e.charCodeAt(_0x263dcf++) & 255;
            if (_0x263dcf == _0x46760c) {
                _0x1e634c += _0x5ca930.charAt(_0x4b3c98 >> 2);
                _0x1e634c += _0x5ca930.charAt((_0x4b3c98 & 3) << 4);
                _0x1e634c += "==";
                break;
            }
            _0x1b7bc1 = _0x26509e.charCodeAt(_0x263dcf++);
            if (_0x263dcf == _0x46760c) {
                _0x1e634c += _0x5ca930.charAt(_0x4b3c98 >> 2);
                _0x1e634c += _0x5ca930.charAt((_0x4b3c98 & 3) << 4 | (_0x1b7bc1 & 240) >> 4);
                _0x1e634c += _0x5ca930.charAt((_0x1b7bc1 & 15) << 2);
                _0x1e634c += "=";
                break;
            }
            _0x1492ee = _0x26509e.charCodeAt(_0x263dcf++);
            _0x1e634c += _0x5ca930.charAt(_0x4b3c98 >> 2);
            _0x1e634c += _0x5ca930.charAt((_0x4b3c98 & 3) << 4 | (_0x1b7bc1 & 240) >> 4);
            _0x1e634c += _0x5ca930.charAt((_0x1b7bc1 & 15) << 2 | (_0x1492ee & 192) >> 6);
            _0x1e634c += _0x5ca930.charAt(_0x1492ee & 63);
        }
        return _0x1e634c;
    },
    base64_decode: function (_0x187c35) {
        var _0x3550f9 = new Array(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1, -1, -1);
        var _0x28e72a;
        var _0x577c6b;
        var _0x59ec4e;
        var _0x397aad;
        var _0x3987e6;
        var _0x3a78d5;
        var _0x3455d2;
        _0x3a78d5 = _0x187c35.length;
        _0x3987e6 = 0;
        _0x3455d2 = "";
        while (_0x3987e6 < _0x3a78d5) {
            do {
                _0x28e72a = _0x3550f9[_0x187c35.charCodeAt(_0x3987e6++) & 255];
            } while (_0x3987e6 < _0x3a78d5 && _0x28e72a == -1);
            if (_0x28e72a == -1) {
                break;
            }
            do {
                _0x577c6b = _0x3550f9[_0x187c35.charCodeAt(_0x3987e6++) & 255];
            } while (_0x3987e6 < _0x3a78d5 && _0x577c6b == -1);
            if (_0x577c6b == -1) {
                break;
            }
            _0x3455d2 += String.fromCharCode(_0x28e72a << 2 | (_0x577c6b & 48) >> 4);
            do {
                _0x59ec4e = _0x187c35.charCodeAt(_0x3987e6++) & 255;
                if (_0x59ec4e == 61) {
                    return _0x3455d2;
                }
                _0x59ec4e = _0x3550f9[_0x59ec4e];
            } while (_0x3987e6 < _0x3a78d5 && _0x59ec4e == -1);
            if (_0x59ec4e == -1) {
                break;
            }
            _0x3455d2 += String.fromCharCode((_0x577c6b & 15) << 4 | (_0x59ec4e & 60) >> 2);
            do {
                _0x397aad = _0x187c35.charCodeAt(_0x3987e6++) & 255;
                if (_0x397aad == 61) {
                    return _0x3455d2;
                }
                _0x397aad = _0x3550f9[_0x397aad];
            } while (_0x3987e6 < _0x3a78d5 && _0x397aad == -1);
            if (_0x397aad == -1) {
                break;
            }
            _0x3455d2 += String.fromCharCode((_0x59ec4e & 3) << 6 | _0x397aad);
        }
        return _0x3455d2;
    },
    utf16to8: function (_0x4122cb) {
        var _0x43dd38;
        var _0x403dfb;
        var _0x2107ec;
        var _0x1db979;
        _0x43dd38 = "";
        _0x2107ec = _0x4122cb.length;
        for (_0x403dfb = 0; _0x403dfb < _0x2107ec; _0x403dfb++) {
            _0x1db979 = _0x4122cb.charCodeAt(_0x403dfb);
            if (_0x1db979 >= 1 && _0x1db979 <= 127) {
                _0x43dd38 += _0x4122cb.charAt(_0x403dfb);
            } else if (_0x1db979 > 2047) {
                _0x43dd38 += String.fromCharCode(_0x1db979 >> 12 & 15 | 224);
                _0x43dd38 += String.fromCharCode(_0x1db979 >> 6 & 63 | 128);
                _0x43dd38 += String.fromCharCode(_0x1db979 >> 0 & 63 | 128);
            } else {
                _0x43dd38 += String.fromCharCode(_0x1db979 >> 6 & 31 | 192);
                _0x43dd38 += String.fromCharCode(_0x1db979 >> 0 & 63 | 128);
            }
        }
        return _0x43dd38;
    },
    utf8to16: function (_0x249ca6) {
        var _0x2ba3da;
        var _0x174ef1;
        var _0x711fb1;
        var _0x2faeb1;
        var _0x1b4e05;
        var _0x8a6001;
        _0x2ba3da = "";
        _0x711fb1 = _0x249ca6.length;
        _0x174ef1 = 0;
        while (_0x174ef1 < _0x711fb1) {
            _0x2faeb1 = _0x249ca6.charCodeAt(_0x174ef1++);
            switch (_0x2faeb1 >> 4) {
                case 0:
                case 1:
                case 2:
                case 3:
                case 4:
                case 5:
                case 6:
                case 7:
                    _0x2ba3da += _0x249ca6.charAt(_0x174ef1 - 1);
                    break;
                case 12:
                case 13:
                    _0x1b4e05 = _0x249ca6.charCodeAt(_0x174ef1++);
                    _0x2ba3da += String.fromCharCode((_0x2faeb1 & 31) << 6 | _0x1b4e05 & 63);
                    break;
                case 14:
                    _0x1b4e05 = _0x249ca6.charCodeAt(_0x174ef1++);
                    _0x8a6001 = _0x249ca6.charCodeAt(_0x174ef1++);
                    _0x2ba3da += String.fromCharCode((_0x2faeb1 & 15) << 12 | (_0x1b4e05 & 63) << 6 | (_0x8a6001 & 63) << 0);
                    break;
            }
        }
        return _0x2ba3da;
    },
    encryptcode: function (_0x4f17d5, _0x5d8a7f, _0x1e6c73, _0x20b569) {
        var _0x5d8a7f = _0x5d8a7f ? _0x5d8a7f : "DECODE";
        var _0x1e6c73 = _0x1e6c73 ? _0x1e6c73 : "";
        var _0x20b569 = _0x20b569 ? _0x20b569 : 0;
        var _0x5a289c = 4;
        _0x1e6c73 = this.md5(_0x1e6c73);
        var _0x5dda25 = this.md5(_0x1e6c73.substr(0, 16));
        var _0x2cf2d8 = this.md5(_0x1e6c73.substr(16, 16));
        if (_0x5a289c) {
            if (_0x5d8a7f == "DECODE") {
                var _0x2376aa = _0x4f17d5.substr(0, _0x5a289c);
            } else {
                var _0x1e9200 = this.md5(this.microtime());
                var _0x461985 = _0x1e9200.length - _0x5a289c;
                var _0x2376aa = _0x1e9200.substr(_0x461985, _0x5a289c);
            }
        } else {
            var _0x2376aa = "";
        }
        var _0x4416d6 = _0x5dda25 + this.md5(_0x5dda25 + _0x2376aa);
        var _0x7c95ac;
        if (_0x5d8a7f == "DECODE") {
            _0x4f17d5 = _0x4f17d5.substr(_0x5a289c);
            _0x7c95ac = this.base64_decode(_0x4f17d5);
        } else {
            _0x20b569 = _0x20b569 ? _0x20b569 + time() : 0;
            tmpstr = _0x20b569.toString();
            if (tmpstr.length >= 10) {
                _0x4f17d5 = tmpstr.substr(0, 10) + this.md5(_0x4f17d5 + _0x2cf2d8).substr(0, 16) + _0x4f17d5;
            } else {
                var _0x3c141e = 10 - tmpstr.length;
                for (var _0x47088f = 0; _0x47088f < _0x3c141e; _0x47088f++) {
                    tmpstr = "0" + tmpstr;
                }
                _0x4f17d5 = tmpstr + this.md5(_0x4f17d5 + _0x2cf2d8).substr(0, 16) + _0x4f17d5;
            }
            _0x7c95ac = _0x4f17d5;
        }
        var _0x7d47ce = new Array(256);
        for (var _0x47088f = 0; _0x47088f < 256; _0x47088f++) {
            _0x7d47ce[_0x47088f] = _0x47088f;
        }
        var _0x233b4a = new Array();
        for (var _0x47088f = 0; _0x47088f < 256; _0x47088f++) {
            _0x233b4a[_0x47088f] = _0x4416d6.charCodeAt(_0x47088f % _0x4416d6.length);
        }
        for (var _0x4e0f8a = _0x47088f = 0; _0x47088f < 256; _0x47088f++) {
            _0x4e0f8a = (_0x4e0f8a + _0x7d47ce[_0x47088f] + _0x233b4a[_0x47088f]) % 256;
            tmp = _0x7d47ce[_0x47088f];
            _0x7d47ce[_0x47088f] = _0x7d47ce[_0x4e0f8a];
            _0x7d47ce[_0x4e0f8a] = tmp;
        }
        var _0x4c681d = "";
        _0x7c95ac = _0x7c95ac.split("");
        for (var _0x411d51 = _0x4e0f8a = _0x47088f = 0; _0x47088f < _0x7c95ac.length; _0x47088f++) {
            _0x411d51 = (_0x411d51 + 1) % 256;
            _0x4e0f8a = (_0x4e0f8a + _0x7d47ce[_0x411d51]) % 256;
            tmp = _0x7d47ce[_0x411d51];
            _0x7d47ce[_0x411d51] = _0x7d47ce[_0x4e0f8a];
            _0x7d47ce[_0x4e0f8a] = tmp;
            _0x4c681d += this.chr(this.ord(_0x7c95ac[_0x47088f]) ^ _0x7d47ce[(_0x7d47ce[_0x411d51] + _0x7d47ce[_0x4e0f8a]) % 256]);
        }
        if (_0x5d8a7f == "DECODE") {
            if ((_0x4c681d.substr(0, 10) == 0 || _0x4c681d.substr(0, 10) - this.time() > 0) && _0x4c681d.substr(10, 16) == this.md5(_0x4c681d.substr(26) + _0x2cf2d8).substr(0, 16)) {
                _0x4c681d = _0x4c681d.substr(26);
            } else {
                _0x4c681d = "";
            }
        } else {
            _0x4c681d = this.base64_encode(_0x4c681d);
            var _0x3a1df9 = new RegExp("=", "g");
            _0x4c681d = _0x4c681d.replace(_0x3a1df9, "");
            _0x4c681d = _0x2376aa + _0x4c681d;
        }
        return _0x4c681d;
    },
    time: function () {
        var _0x5e6229 = new Date().getTime();
        return parseInt(_0x5e6229 / 1000);
    },
    microtime: function (_0x3e992f) {
        var _0x32e452 = new Date().getTime();
        var _0x3f3a6f = parseInt(_0x32e452 / 1000);
        if (_0x3e992f) {
            return _0x32e452 / 1000;
        } else {
            return (_0x32e452 - _0x3f3a6f * 1000) / 1000 + " " + _0x3f3a6f;
        }
    },
    chr: function (_0x5d2005) {
        return String.fromCharCode(_0x5d2005);
    },
    ord: function (_0x40e629) {
        return _0x40e629.charCodeAt();
    },
    md5: function (_0x938fc0) {
        return this.hex_md5(_0x938fc0);
    },
    loadmode: function (_0x392af, _0x35f6fd, _0x12fb7e) {
        try {
            var _0x121fe8 = {
                url: "/static/javascript/mode/" + _0x392af + ".js",
                dataType: "script",
                cache: false
            };
            $.ajax(_0x121fe8).done(function () {
                if (_0x35f6fd) {
                    _0x35f6fd(_0x392af);
                }
            }).error(function (_0x2da6d7, _0x2212c6, _0x2b85a6) {
                if (_0x12fb7e) {
                    _0x12fb7e(_0x392af, _0x2da6d7, _0x2212c6, _0x2b85a6);
                }
            });
        } catch (_0xb0989e) {
            if (typeof Hay.config() !== "undefined" && Hay.config().debug == "open") {
                console.error("加载模块异常：" + _0xb0989e);
            }
        }
    },
    cipherconfig: function (_0x4612e6, _0x15f342) {
        try {
            var _0xf6f200 = new Date(new Date().getTime() + new Date().getTimezoneOffset() * 60 * 1000 + 28800000);
            var _0xfa7dc4 = Hay.md5("HayConfigHay" + document.domain + "hAy" + _0xf6f200.getFullYear() + "-" + parseInt(_0xf6f200.getMonth() + 1) + "-" + _0xf6f200.getDate() + "haY");
            if (_0x15f342 == "encode") {
                return Hay.base64_encode(Hay.encryptcode(Hay.base64_encode(Hay.utf16to8(_0x4612e6)), "ENCODE", _0xfa7dc4));
            } else {
                return Hay.utf8to16(Hay.base64_decode(Hay.encryptcode(Hay.base64_decode(_0x4612e6), "DECODE", _0xfa7dc4)));
            }
        } catch (_0x37e5cc) {
            if (typeof Hay.config() !== "undefined" && Hay.config().debug == "open") {
                console.error("加密模块异常：" + _0x37e5cc);
            }
        }
    },
    ciphertext: function (_0x36f3ac, _0xa5318a) {
        try {
            var _0x2a6eac = new Date(new Date().getTime() + new Date().getTimezoneOffset() * 60 * 1000 + 28800000);
            var _0xf2fe9a = Hay.md5(`Haypvp.hayfuon.cnhAy${_0x2a6eac.getFullYear()}-${_0x2a6eac.getMonth() + 1}-${_0x2a6eac.getDate()}haY`);
            if (_0xa5318a == "encode") {
                return Hay.base64_encode(Hay.encryptcode(Hay.base64_encode(Hay.utf16to8(_0x36f3ac)), "ENCODE", _0xf2fe9a));
            } else {
                return Hay.utf8to16(Hay.base64_decode(Hay.encryptcode(Hay.base64_decode(_0x36f3ac), "DECODE", _0xf2fe9a)));
            }
        } catch (_0x22385d) {
            if (typeof Hay.config() !== "undefined") {
                if (Hay.config().debug == "open") {
                    console.error("加密模块异常：" + _0x22385d);
                }
            }
        }
    },
    asyninte: function (_0x2e2259, _0x41f2f1) {
        try {
            if (_0x41f2f1 == "issue") {
                if (true) {
                    var _0xe1d093 = {};
                    _0xe1d093.data = Hay.ciphertext(JSON.stringify(_0x2e2259), "encode");
                    return _0xe1d093;
                } else {
                    return _0x2e2259;
                }
            } else if (true) {
                return JSON.parse(Hay.ciphertext(_0x2e2259.data, "decode"));
            } else {
                return _0x2e2259;
            }
        } catch (_0x3f4364) {
            if (typeof Hay.config() !== "undefined" && Hay.config().debug == "open") {
                console.error("传输模块异常：" + _0x3f4364);
            }
            return {
                code: "-1",
                msg: "服务器信息传输异常[-2]"
            };
        }
    },
    config: function () {
        if (typeof HayOccult !== "undefined") {
            if (Hay.cipherconfig(HayOccult, "decode")) {
                eval(Hay.cipherconfig(HayOccult, "decode"));
                return HayConfig;
            }
        }
    }
};


function GetEnc(params){
    _data = Hay.asyninte(params, "issue")
    return _data
}
zaihe = {
    "hero": "507",
    "server": "1",
    "area": "stron"
}
console.log(GetEnc(zaihe));

function GetDec(enc_data) {
    data = Hay.asyninte(enc_data, "receiver")
    return data
}

// enc_data = {
//     "data": 'NTIwZGdoSzB5SDI0T2Nzd1kvVi9SQjZYMmdSSUkzS1U1MW9zVGJ1d1dUMkJrMk9jOUQvVlFsNHpBb0FFQ2xsTVhPWkgwM3ludVVGOUR1Z3ZrYjNEbHRnVDZzVW5BYlR1RmZsSDBmS0kxN21DaGpFKzdtcTdSVVhMTXhqMmc3MFg1aXFSR0toWVBlUW5xYXBhNmhsdzdNNHFIclJsdUdMN2dFRFZReTh0ZHlyZEpkc2w3VXdDbUFPMy9oSTVZNTBUWEJMb1N4cE1GQVBpaTdwbWNSNHdkYkE3LzlwcWhVdVdJRHhzWVNXakZQUXhocWFwend6dnNVaWNoS3hkeFRHbVlQWEN1M05BODIybUdZc280RU5CNTlRUDVvRzlkcWVJUEl2R2FleThaNm4xdkN0c2lwVjdSYTlienR2UnIwY0g0eFB1M1pr'
// }
// console.log(GetDec(enc_data)) [ ]

