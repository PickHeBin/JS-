p = function (e) {
    function t(e, t) {
        return e << t | e >>> 32 - t
    }

    function n(e, t) {
        var n, o, r, i, s;
        return r = 2147483648 & e, i = 2147483648 & t, s = (1073741823 & e) + (1073741823 & t), (n = 1073741824 & e) & (o = 1073741824 & t) ? 2147483648 ^ s ^ r ^ i : n | o ? 1073741824 & s ? 3221225472 ^ s ^ r ^ i : 1073741824 ^ s ^ r ^ i : s ^ r ^ i
    }

    function o(e, o, r, i, s, a, p) {
        return e = n(e, n(n(function (e, t, n) {
            return e & t | ~e & n
        }(o, r, i), s), p)), n(t(e, a), o)
    }

    function r(e, o, r, i, s, a, p) {
        return e = n(e, n(n(function (e, t, n) {
            return e & n | t & ~n
        }(o, r, i), s), p)), n(t(e, a), o)
    }

    function i(e, o, r, i, s, a, p) {
        return e = n(e, n(n(function (e, t, n) {
            return e ^ t ^ n
        }(o, r, i), s), p)), n(t(e, a), o)
    }

    function s(e, o, r, i, s, a, p) {
        return e = n(e, n(n(function (e, t, n) {
            return t ^ (e | ~n)
        }(o, r, i), s), p)), n(t(e, a), o)
    }

    function a(e) {
        var t, n = "", o = "";
        for (t = 0; 3 >= t; t++) n += (o = "0" + (e >>> 8 * t & 255).toString(16)).substr(o.length - 2, 2);
        return n
    }

    var p, u, c, d, l, f, m, g, y, v;
    for (v = function (e) {
        for (var t, n = e.length, o = n + 8, r = 16 * ((o - o % 64) / 64 + 1), i = new Array(r - 1), s = 0, a = 0; n > a;) s = a % 4 * 8, i[t = (a - a % 4) / 4] = i[t] | e.charCodeAt(a) << s, a++;
        return s = a % 4 * 8, i[t = (a - a % 4) / 4] = i[t] | 128 << s, i[r - 2] = n << 3, i[r - 1] = n >>> 29, i
    }(e = function (e) {
        e = e.replace(/\r\n/g, "\n");
        for (var t = "", n = 0; n < e.length; n++) {
            var o = e.charCodeAt(n);
            128 > o ? t += String.fromCharCode(o) : o > 127 && 2048 > o ? (t += String.fromCharCode(o >> 6 | 192), t += String.fromCharCode(63 & o | 128)) : (t += String.fromCharCode(o >> 12 | 224), t += String.fromCharCode(o >> 6 & 63 | 128), t += String.fromCharCode(63 & o | 128))
        }
        return t
    }(e)), f = 1732584193, m = 4023233417, g = 2562383102, y = 271733878, p = 0; p < v.length; p += 16) u = f, c = m, d = g, l = y, f = o(f, m, g, y, v[p + 0], 7, 3614090360), y = o(y, f, m, g, v[p + 1], 12, 3905402710), g = o(g, y, f, m, v[p + 2], 17, 606105819), m = o(m, g, y, f, v[p + 3], 22, 3250441966), f = o(f, m, g, y, v[p + 4], 7, 4118548399), y = o(y, f, m, g, v[p + 5], 12, 1200080426), g = o(g, y, f, m, v[p + 6], 17, 2821735955), m = o(m, g, y, f, v[p + 7], 22, 4249261313), f = o(f, m, g, y, v[p + 8], 7, 1770035416), y = o(y, f, m, g, v[p + 9], 12, 2336552879), g = o(g, y, f, m, v[p + 10], 17, 4294925233), m = o(m, g, y, f, v[p + 11], 22, 2304563134), f = o(f, m, g, y, v[p + 12], 7, 1804603682), y = o(y, f, m, g, v[p + 13], 12, 4254626195), g = o(g, y, f, m, v[p + 14], 17, 2792965006), f = r(f, m = o(m, g, y, f, v[p + 15], 22, 1236535329), g, y, v[p + 1], 5, 4129170786), y = r(y, f, m, g, v[p + 6], 9, 3225465664), g = r(g, y, f, m, v[p + 11], 14, 643717713), m = r(m, g, y, f, v[p + 0], 20, 3921069994), f = r(f, m, g, y, v[p + 5], 5, 3593408605), y = r(y, f, m, g, v[p + 10], 9, 38016083), g = r(g, y, f, m, v[p + 15], 14, 3634488961), m = r(m, g, y, f, v[p + 4], 20, 3889429448), f = r(f, m, g, y, v[p + 9], 5, 568446438), y = r(y, f, m, g, v[p + 14], 9, 3275163606), g = r(g, y, f, m, v[p + 3], 14, 4107603335), m = r(m, g, y, f, v[p + 8], 20, 1163531501), f = r(f, m, g, y, v[p + 13], 5, 2850285829), y = r(y, f, m, g, v[p + 2], 9, 4243563512), g = r(g, y, f, m, v[p + 7], 14, 1735328473), f = i(f, m = r(m, g, y, f, v[p + 12], 20, 2368359562), g, y, v[p + 5], 4, 4294588738), y = i(y, f, m, g, v[p + 8], 11, 2272392833), g = i(g, y, f, m, v[p + 11], 16, 1839030562), m = i(m, g, y, f, v[p + 14], 23, 4259657740), f = i(f, m, g, y, v[p + 1], 4, 2763975236), y = i(y, f, m, g, v[p + 4], 11, 1272893353), g = i(g, y, f, m, v[p + 7], 16, 4139469664), m = i(m, g, y, f, v[p + 10], 23, 3200236656), f = i(f, m, g, y, v[p + 13], 4, 681279174), y = i(y, f, m, g, v[p + 0], 11, 3936430074), g = i(g, y, f, m, v[p + 3], 16, 3572445317), m = i(m, g, y, f, v[p + 6], 23, 76029189), f = i(f, m, g, y, v[p + 9], 4, 3654602809), y = i(y, f, m, g, v[p + 12], 11, 3873151461), g = i(g, y, f, m, v[p + 15], 16, 530742520), f = s(f, m = i(m, g, y, f, v[p + 2], 23, 3299628645), g, y, v[p + 0], 6, 4096336452), y = s(y, f, m, g, v[p + 7], 10, 1126891415), g = s(g, y, f, m, v[p + 14], 15, 2878612391), m = s(m, g, y, f, v[p + 5], 21, 4237533241), f = s(f, m, g, y, v[p + 12], 6, 1700485571), y = s(y, f, m, g, v[p + 3], 10, 2399980690), g = s(g, y, f, m, v[p + 10], 15, 4293915773), m = s(m, g, y, f, v[p + 1], 21, 2240044497), f = s(f, m, g, y, v[p + 8], 6, 1873313359), y = s(y, f, m, g, v[p + 15], 10, 4264355552), g = s(g, y, f, m, v[p + 6], 15, 2734768916), m = s(m, g, y, f, v[p + 13], 21, 1309151649), f = s(f, m, g, y, v[p + 4], 6, 4149444226), y = s(y, f, m, g, v[p + 11], 10, 3174756917), g = s(g, y, f, m, v[p + 2], 15, 718787259), m = s(m, g, y, f, v[p + 9], 21, 3951481745), f = n(f, u), m = n(m, c), g = n(g, d), y = n(y, l);
    return (a(f) + a(m) + a(g) + a(y)).toLowerCase()
}


token = "157c0493dcfc4fdcd356014e99c24430"
a = (new Date).getTime()
s = '12574478'
data = '{"dfApp":"auctionwalle","dfApiName":"auctionwalle.datou.getPageModulesData","dfVariables":"{\\"pageId\\":1410667,\\"moduleIds\\":\\"9018433170:items\\",\\"context\\":{\\"_b_9018433170:items\\":\\"{\\\\\\"scm\\\\\\":\\\\\\"20140647.julang.pm.sem\\\\\\",\\\\\\"a_keywordid\\\\\\":\\\\\\"408409593247\\\\\\",\\\\\\"bd_vid\\\\\\":\\\\\\"8230115899146061516\\\\\\",\\\\\\"page\\\\\\":\\\\\\"3\\\\\\",\\\\\\"userInfo\\\\\\":{},\\\\\\"appendMap\\\\\\":{\\\\\\"sid\\\\\\":\\\\\\"7444983582_1692098165305\\\\\\"}}\\",\\"userInfo\\":\\"{}\\",\\"device\\":\\"pc\\",\\"sceneCode\\":\\"20200713C5R32B6N\\"}}","dfUniqueId":"1410667.9018433170:items","dfVariablesRecover":"{}"}'
console.log(p(token + "&" + a + "&" + s + "&" + data))
