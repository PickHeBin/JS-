var window =global;
var document ={
    document:{},
    navigator:{}
}
window.location={
    "ancestorOrigins": {},
    "href": "https://y.qq.com/n/ryqq/search?w=%E4%BA%88%E4%BD%A0&t=song&remoteplace=txt.yqq.center",
    "origin": "https://y.qq.com",
    "protocol": "https:",
    "host": "y.qq.com",
    "hostname": "y.qq.com",
    "port": "",
    "pathname": "/n/ryqq/search",
    "search": "?w=%E4%BA%88%E4%BD%A0&t=song&remoteplace=txt.yqq.center",
    "hash": ""
}

window.navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}
require('./webpack')
!function(e) {
    function t(t) {
        for (var r, n, d = t[0], f = t[1], i = t[2], l = 0, b = []; l < d.length; l++)
            n = d[l],
            Object.prototype.hasOwnProperty.call(o, n) && o[n] && b.push(o[n][0]),
            o[n] = 0;
        for (r in f)
            Object.prototype.hasOwnProperty.call(f, r) && (e[r] = f[r]);
        for (u && u(t); b.length; )
            b.shift()();
        return c.push.apply(c, i || []),
        a()
    }
    function a() {
        for (var e, t = 0; t < c.length; t++) {
            for (var a = c[t], r = !0, n = 1; n < a.length; n++) {
                var f = a[n];
                0 !== o[f] && (r = !1)
            }
            r && (c.splice(t--, 1),
            e = d(d.s = a[0]))
        }
        return e
    }
    var r = {}
      , n = {
        20: 0
    }
      , o = {
        20: 0
    }
      , c = [];
    function d(t) {
        if (r[t])
            return r[t].exports;
        var a = r[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(a.exports, a, a.exports, d),
        a.l = !0,
        a.exports
    }
    window.exports_f = d
    d.e = function(e) {
        var t = [];
        n[e] ? t.push(n[e]) : 0 !== n[e] && {
            1: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1,
            19: 1,
            21: 1,
            22: 1,
            23: 1,
            24: 1,
            25: 1
        }[e] && t.push(n[e] = new Promise((function(t, a) {
            for (var r = "css/" + ({
                1: "common",
                3: "album",
                4: "albumDetail",
                5: "album_mall",
                6: "category",
                7: "cmtpage",
                8: "index",
                9: "msg_center",
                10: "mv",
                11: "mvList",
                12: "mv_toplist",
                13: "notfound",
                14: "player",
                15: "player_radio",
                16: "playlist",
                17: "playlist_edit",
                18: "profile",
                19: "radio",
                21: "search",
                22: "singer",
                23: "singer_list",
                24: "songDetail",
                25: "toplist"
            }[e] || e) + "." + {
                1: "2e3d715e72682303d35b",
                3: "5cf0d69eaf29bcab23d2",
                4: "798353db5b0eb05d5358",
                5: "df4c243f917604263e58",
                6: "20d532d798099a44bc88",
                7: "e3bedf2b5810f8db0684",
                8: "ea0adb959fef9011fc25",
                9: "020422608fe8bfb1719a",
                10: "8bdb1df6c5436b790baa",
                11: "47ce9300786df1b70584",
                12: "4aee33230ba2d6b81dce",
                13: "e6f63b0cf57dd029fbd6",
                14: "1d2dbefbea113438324a",
                15: "d893492de07ce97d8048",
                16: "9484fde660fe93d9f9f0",
                17: "67fb85e7f96455763c83",
                18: "5e8c651e74b13244f7cf",
                19: "3befd83c10b19893ec66",
                21: "b2d11f89ea6a512a2302",
                22: "c7a38353c5f4ebb47491",
                23: "df0961952a2d3f022894",
                24: "4c080567e394fd45608b",
                25: "8edb142553f97482e00f"
            }[e] + ".chunk.css?max_age=2592000", o = d.p + r, c = document.getElementsByTagName("link"), f = 0; f < c.length; f++) {
                var i = (u = c[f]).getAttribute("data-href") || u.getAttribute("href");
                if ("stylesheet" === u.rel && (i === r || i === o))
                    return t()
            }
            var l = document.getElementsByTagName("style");
            for (f = 0; f < l.length; f++) {
                var u;
                if ((i = (u = l[f]).getAttribute("data-href")) === r || i === o)
                    return t()
            }
            var b = document.createElement("link");
            b.rel = "stylesheet",
            b.type = "text/css",
            b.onload = t,
            b.onerror = function(t) {
                var r = t && t.target && t.target.src || o
                  , c = new Error("Loading CSS chunk " + e + " failed.\n(" + r + ")");
                c.code = "CSS_CHUNK_LOAD_FAILED",
                c.request = r,
                delete n[e],
                b.parentNode.removeChild(b),
                a(c)
            }
            ,
            b.href = o,
            0 !== b.href.indexOf(window.location.origin + "/") && (b.crossOrigin = "anonymous"),
            document.getElementsByTagName("head")[0].appendChild(b)
        }
        )).then((function() {
            n[e] = 0
        }
        )));
        var a = o[e];
        if (0 !== a)
            if (a)
                t.push(a[2]);
            else {
                var r = new Promise((function(t, r) {
                    a = o[e] = [t, r]
                }
                ));
                t.push(a[2] = r);
                var c, f = document.createElement("script");
                f.charset = "utf-8",
                f.timeout = 120,
                d.nc && f.setAttribute("nonce", d.nc),
                f.src = function(e) {
                    return d.p + "js/" + ({
                        1: "common",
                        3: "album",
                        4: "albumDetail",
                        5: "album_mall",
                        6: "category",
                        7: "cmtpage",
                        8: "index",
                        9: "msg_center",
                        10: "mv",
                        11: "mvList",
                        12: "mv_toplist",
                        13: "notfound",
                        14: "player",
                        15: "player_radio",
                        16: "playlist",
                        17: "playlist_edit",
                        18: "profile",
                        19: "radio",
                        21: "search",
                        22: "singer",
                        23: "singer_list",
                        24: "songDetail",
                        25: "toplist"
                    }[e] || e) + ".chunk." + {
                        1: "67e5eabd93ea08dd2bbf",
                        3: "57adeab72a3ec5a6940c",
                        4: "fb9a0df49aac1081fd8b",
                        5: "ce88bd122dac655490ca",
                        6: "3c9e9ce78ed1a42f485f",
                        7: "ca787dcf6db83f6a4d11",
                        8: "306c7ad24389b8338e1f",
                        9: "b5cd5a77da26782764c2",
                        10: "55a52c1b91e872677fbe",
                        11: "c925c75c1a05b9bd0958",
                        12: "bc1e3a73e2aacd27011a",
                        13: "e8b9a6dad95b623cab82",
                        14: "16f4f61d208558a7c17c",
                        15: "7264ef7ff4b6052f4c01",
                        16: "039db3b85d472916677b",
                        17: "72dfb28846b85bcce963",
                        18: "7f8ac1ee0d0077c0d960",
                        19: "89e9600c87d40494d2a0",
                        21: "157aa8a8c67606f0d243",
                        22: "07c7b21c4be040114330",
                        23: "d0f42e091f31e2cd3a85",
                        24: "4e38573b87120e0a3b0a",
                        25: "f89cca2cc643a79036f5"
                    }[e] + ".js?max_age=2592000"
                }(e),
                0 !== f.src.indexOf(window.location.origin + "/") && (f.crossOrigin = "anonymous");
                var i = new Error;
                c = function(t) {
                    f.onerror = f.onload = null,
                    clearTimeout(l);
                    var a = o[e];
                    if (0 !== a) {
                        if (a) {
                            var r = t && ("load" === t.type ? "missing" : t.type)
                              , n = t && t.target && t.target.src;
                            i.message = "Loading chunk " + e + " failed.\n(" + r + ": " + n + ")",
                            i.name = "ChunkLoadError",
                            i.type = r,
                            i.request = n,
                            a[1](i)
                        }
                        o[e] = void 0
                    }
                }
                ;
                var l = setTimeout((function() {
                    c({
                        type: "timeout",
                        target: f
                    })
                }
                ), 12e4);
                f.onerror = f.onload = c,
                document.head.appendChild(f)
            }
        return Promise.all(t)
    }
    ,
    d.m = e,
    d.c = r,
    d.d = function(e, t, a) {
        d.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: a
        })
    }
    ,
    d.r = function(e) {
        "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }),
        Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }
    ,
    d.t = function(e, t) {
        if (1 & t && (e = d(e)),
        8 & t)
            return e;
        if (4 & t && "object" === typeof e && e && e.__esModule)
            return e;
        var a = Object.create(null);
        if (d.r(a),
        Object.defineProperty(a, "default", {
            enumerable: !0,
            value: e
        }),
        2 & t && "string" != typeof e)
            for (var r in e)
                d.d(a, r, function(t) {
                    return e[t]
                }
                .bind(null, r));
        return a
    }
    ,
    d.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        }
        : function() {
            return e
        }
        ;
        return d.d(t, "a", t),
        t
    }
    ,
    d.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }
    ,
    d.p = "/ryqq/",
    d.oe = function(e) {
        throw e
    }
    ;
    var f = window.webpackJsonp = window.webpackJsonp || []
      , i = f.push.bind(f);
    f.push = t,
    f = f.slice();
    for (var l = 0; l < f.length; l++)
        t(f[l]);
    var u = i;
    a()
}([]);

data = {
    "comm": {
        "cv": 4747474,
        "ct": 24,
        "format": "json",
        "inCharset": "utf-8",
        "outCharset": "utf-8",
        "notice": 0,
        "platform": "yqq.json",
        "needNewCode": 1,
        "uin": 0,
        "g_tk_new_20200303": 5381,
        "g_tk": 5381
    },
    "req_1": {
        "module": "musicToplist.ToplistInfoServer",
        "method": "GetDetail",
        "param": {
            "topid": 4,
            "offset": 0,
            "num": 20,
            "period": "2023-12-22"
        }
    }
}
function get_sign(data){
    return window.exports_f(350).default(data)
    // return ddd(350).default(data)
}

console.log(get_sign(data))

