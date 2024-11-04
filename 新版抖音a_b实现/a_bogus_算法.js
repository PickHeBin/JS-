
function ne() {
    var e = [
        "W57cKmkGySkr",
        "zNvUy3rPB24",
        "y2H1BMS",
        "W6ddPw0Je8kGhSk5W44aWOhcJrK",
        "gtFcIsu",
        "WQ7cQuS",
        "h8kiyCoBW4VdGu7cM8o2yHhdRr8",
        "ChvZAa",
        "W44WWRdcOgdcMW",
        "zgvMAw5LuhjVCgvYDhK",
        "nJu4nty4ng1Suvvnqq",
        "W67dUrNdTSolBhFcU8oTESogfW",
        "W5i4WRBdTCk2W5RcVSkU",
        "WOf6jmkjWRK",
        "W6FdIK0",
        "W7pcOHKCW6XY",
        "AxrLCMf0B3i",
        "y2fSBa",
        "pexdNrOW",
        "BwLU",
        "CMvN",
        "fhBcVKSa",
        "C2L6zq",
        "W4f/bSklAG",
        "AMv3W7aUW5e",
        "WRZcLSkrWO4t",
        "ChjVDg90ExbL",
        "tConAYLi",
        "WO9dWPP7W7a",
        "W4j7W4/dRd9cF8oA",
        "wCoikSkg",
        "mJGXmZm2neDLrffpEa",
        "WRump8kHW6e8",
        "DGxcUvjjrq",
        "Aw52ywXPzcbQigzVCIbIB29Sigz1BMn0Aw9UieDh",
        "hmo5W4JcR8kwwbT4W4FdLCoIW7ldSSkz",
        "WQ/cUf7cP8kCoG",
        "C2XPy2u",
        "mtGXnJy5nLb2EgTXDG",
        "WPldUbNcPIj5A8k8WQFcTuJdMKa",
        "W4yZDSoMW5W",
        "zM9YrwfJAa",
        "W4BdHeSQlw3dHq",
        "v8oQrwKqWQVdV8k6hWC",
        "vmo2x2K2WRhdV8kQma3cRbG",
        "rmoJFumQ",
        "WRLDW7LmWQq",
        "e8kMprrRW6xcRYxdImkKWPxcTeO",
        "Aw52ywXPzcbQigzVCIbIB29Sigz1BMn0Aw9Uiezg",
        "y2HHCKnVzgvbDa",
        "n8o8fu7cO8oTxH3dRq",
        "WOLIWPBdLSk3W5G",
        "C3rYAw5N",
        "Dg9tDhjPBMC",
        "WPLDWRvPW4iuW7ZdJL/dTv7dHferr8kPW5ddOCkFW4GDz8kfcXW",
        "xaSFj0n0W4jPWOa6cXZdQG",
        "nJm1mJq1nvvTr09NyW",
        "WQ8bWQq",
        "C3LTyM9S",
        "WOtcRSkTeuO",
        "tCoiEc8",
        "y29TChjLC3mGzxjYB3i6ig5VDcbLBM91z2GGzgf0yq",
        "W5vLgSkrymkOEfi",
        "a2hcQW",
        "cbxcV8k/EYS",
        "WQpcNb/cIe4kEM7cOaLsW6hcVW",
        "W5GNWPG",
        "zxjYB3i",
        "BgvUz3rO",
        "mJu1odKXrfHXs0Dn",
        "B2jQzwn0",
        "CMvWzwf0",
        "x2nVBxbYzxnZ",
        "CMvZzxq",
        "W4f2h8kj",
        "uCoRxNCbWQVdQ8k7bW3cUG",
        "sSovlmkaWPy",
        "C3vT",
        "WRXaWP1WW6GO",
        "WOb2lCkj",
        "Dgv+",
        "W4BcGqlcOCog"
    ];   // 这里做了手脚
    return (ne = function () {
            return e
        }
    )()
}

function ce(e, r) {
    var t = ne();
    return ce = function (r, a) {
        var n = t[r -= 145];
        if (void 0 === ce.PLwcmq) {
            ce.cQrRAb = function (e, r) {
                var t, a, n = [], c = 0, i = "";
                for (e = function (e) {
                    for (var r, t, a = "", n = "", c = 0, i = 0; t = e.charAt(i++); ~t && (r = c % 4 ? 64 * r + t : t,
                    c++ % 4) ? a += String.fromCharCode(255 & r >> (-2 * c & 6)) : 0)
                        t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=".indexOf(t);
                    for (var f = 0, o = a.length; f < o; f++)
                        n += "%" + ("00" + a.charCodeAt(f).toString(16)).slice(-2);
                    return decodeURIComponent(n)
                }(e),
                         a = 0; a < 256; a++)
                    n[a] = a;
                for (a = 0; a < 256; a++)
                    c = (c + n[a] + r.charCodeAt(a % r.length)) % 256,
                        t = n[a],
                        n[a] = n[c],
                        n[c] = t;
                a = 0,
                    c = 0;
                for (var f = 0; f < e.length; f++)
                    c = (c + n[a = (a + 1) % 256]) % 256,
                        t = n[a],
                        n[a] = n[c],
                        n[c] = t,
                        i += String.fromCharCode(e.charCodeAt(f) ^ n[(n[a] + n[c]) % 256]);
                return i
            }
                ,
                e = arguments,
                ce.PLwcmq = !0
        }
        var c = r + t[0]
            , i = e[c];
        return i ? n = i : (void 0 === ce.xyTZoP && (ce.xyTZoP = !0),
            n = ce.cQrRAb(n, a),
            e[c] = n),
            n
    }
        ,
        ce(e, r)
}

function ie(e) {
    var r = de;
    return (ie = r(146) == typeof Symbol && r(203) == typeof Symbol[r(161)] ? function (e) {
                return typeof e
            }
            : function (e) {
                var t = ce
                    , a = r;
                return e && a(146) == typeof Symbol && e[t(220, "l^VZ")] === Symbol && e !== Symbol[a(171)] ? t(178, "PLij") : typeof e
            }
    )(e)
}

function fe(e, r) {
    for (var t = ce, a = de, n = 0; n < r[a(213)]; n++) {
        var c = r[n];
        c.enumerable = c[t(188, "l^VZ")] || !1,
            c.configurable = !0,
        t(163, "]YJ*") in c && (c[t(207, "87RN")] = !0),
            Object[t(180, "X%]#")](e, oe(c.key), c)
    }
}

function oe(e) {
    var r = function (e, r) {
        var t = de
            , a = ce;
        if (ie(e) !== a(196, "MS)N") || null === e)
            return e;
        var n = e[Symbol.toPrimitive];
        if (void 0 !== n) {
            var c = n[a(219, "87RN")](e, r || "default");
            if (ie(c) !== t(215))
                return c;
            throw new TypeError("@@toPrimitive must return a primitive value.")
        }
        return (r === a(181, "d6LD") ? String : Number)(e)
    }(e, "string");
    return "symbol" === ie(r) ? r : String(r)
}

function se(e, r, t) {
    var a = ce
        , n = de;
    return e[n(213)] >= r ? e : t[n(216)](r - e[a(209, "hSuQ")]) + e
}

var ue, be = function () {
    var e = ce
        , r = de;

    function t() {
        var e = de
            , r = ce;
        if (function (e, r) {
            if (!(e instanceof r))
                throw new TypeError("Cannot call a class as a function")
        }(this, t),
            !(this instanceof t))
            return new t;
        this[r(202, "@NxI")] = new Array(8),
            this[e(147)] = [],
            this[e(167)] = 0,
            this[e(218)]()
    }

    return function (e, r, t) {
        var a = de;

        r && fe(e[ce(195, "c*I1")], r),
        t && fe(e, t),
            Object[a(154)](e, "prototype", {
                writable: !1
            })
    }(t, [{
        key: r(218),
        value: function () {
            var e = ce
                , t = r;
            this.reg[0] = 1937774191,
                this[t(165)][1] = 1226093241,
                this[t(165)][2] = 388252375,
                this.reg[3] = 3666478592,
                this.reg[4] = 2842636476,
                this[t(165)][5] = 372324522,
                this[e(211, "q&Sq")][6] = 3817729613,
                this[t(165)][7] = 2969243214,
                this[t(147)] = [],
                this[e(224, "d3))")] = 0
        }
    }, {
        key: e(170, "I19)"),
        value: function (t) {
            var a = e
                , n = r
                , c = typeof t === n(197) ? function (e) {
                var r = de
                    , t = ce
                    , a = encodeURIComponent(e)[t(187, "OZDI")](/%([0-9A-F]{2})/g, (function (e, r) {
                        return String[t(189, "l^VZ")]("0x" + r)
                    }
                ))
                    , n = new Array(a[r(213)]);
                return Array[r(171)][r(186)][r(162)](a, (function (e, t) {
                        var a = r;
                        n[t] = e[a(194)](0)
                    }
                )),
                    n
            }(t) : t;
            this[a(205, "dc@U")] += c[a(160, "SJ$(")];
            var i = 64 - this[n(147)][n(213)];
            if (c[a(169, "ZQdZ")] < i)
                this[a(204, "Mkpw")] = this[a(168, "87RN")][a(153, "Lj4N")](c);
            else
                for (this[n(147)] = this.chunk.concat(c[n(182)](0, i)); this.chunk[n(213)] >= 64;)
                    this._compress(this[a(221, "IR3E")]),
                        i < c[a(223, "4RqB")] ? this[n(147)] = c[a(145, "xO0W")](i, Math[n(164)](i + 64, c[a(177, "D%E6")])) : this[n(147)] = [],
                        i += 64
        }
    }, {
        key: r(222),
        value: function (t, a) {
            var n = r
                , c = e;
            t && (this[c(158, "d3))")](),
                this.write(t)),
                this[c(185, "yM$V")]();
            for (var i = 0; i < this.chunk[n(213)]; i += 64)
                this[n(217)](this[n(147)][n(182)](i, i + 64));
            var f = null;
            if ("hex" == a) {
                f = "";
                for (i = 0; i < 8; i++)
                    f += se(this[c(225, "ZQdZ")][i][n(198)](16), 8, "0")
            } else
                for (f = new Array(32),
                         i = 0; i < 8; i++) {
                    var o = this[c(159, "O7yE")][i];
                    f[4 * i + 3] = (255 & o) >>> 0,
                        o >>>= 8,
                        f[4 * i + 2] = (255 & o) >>> 0,
                        o >>>= 8,
                        f[4 * i + 1] = (255 & o) >>> 0,
                        o >>>= 8,
                        f[4 * i] = (255 & o) >>> 0
                }
            return this.reset(),
                f
        }
    }, {
        key: r(217),
        value: function (t) {
            var a = r
                , n = e;
            if (t < 64)
                console[n(190, "sYkq")](a(206));
            else {
                for (var c = function (e) {
                    for (var r = new Array(132), t = 0; t < 16; t++)
                        r[t] = e[4 * t] << 24,
                            r[t] |= e[4 * t + 1] << 16,
                            r[t] |= e[4 * t + 2] << 8,
                            r[t] |= e[4 * t + 3],
                            r[t] >>>= 0;
                    for (var a = 16; a < 68; a++) {
                        var n = r[a - 16] ^ r[a - 9] ^ le(r[a - 3], 15);
                        n = n ^ le(n, 15) ^ le(n, 23),
                            r[a] = (n ^ le(r[a - 13], 7) ^ r[a - 6]) >>> 0
                    }
                    for (a = 0; a < 64; a++)
                        r[a + 68] = (r[a] ^ r[a + 4]) >>> 0;
                    return r
                }(t), i = this[n(208, "@lcn")][n(172, "dc@U")](0), f = 0; f < 64; f++) {
                    var o = le(i[0], 12) + i[4] + le(pe(f), f)
                        , s = ((o = le(o = (4294967295 & o) >>> 0, 7)) ^ le(i[0], 12)) >>> 0
                        , u = he(f, i[0], i[1], i[2]);
                    u = (4294967295 & (u = u + i[3] + s + c[f + 68])) >>> 0;
                    var b = ve(f, i[4], i[5], i[6]);
                    b = (4294967295 & (b = b + i[7] + o + c[f])) >>> 0,
                        i[3] = i[2],
                        i[2] = le(i[1], 9),
                        i[1] = i[0],
                        i[0] = u,
                        i[7] = i[6],
                        i[6] = le(i[5], 19),
                        i[5] = i[4],
                        i[4] = (b ^ le(b, 9) ^ le(b, 17)) >>> 0
                }
                for (var d = 0; d < 8; d++)
                    this[n(150, "d6LD")][d] = (this[a(165)][d] ^ i[d]) >>> 0
            }
        }
    }, {
        key: e(173, "4RqB"),
        value: function () {
            var t = e
                , a = r
                , n = 8 * this.size
                , c = this[a(147)][a(152)](128) % 64;
            for (64 - c < 8 && (c -= 64); c < 56; c++)
                this[a(147)].push(0);
            for (var i = 0; i < 4; i++) {
                var f = Math[t(226, "@8H@")](n / 4294967296);
                this[t(191, "6NTL")][t(175, "IR3E")](f >>> 8 * (3 - i) & 255)
            }
            for (i = 0; i < 4; i++)
                this.chunk[t(149, "p7wA")](n >>> 8 * (3 - i) & 255)
        }
    }]),
        t
}();

function de(e, r) {
    var t = ne();
    return de = function (r, a) {
        var n = t[r -= 145];
        if (void 0 === de.ySkTSd) {
            de.nZVaSF = function (e) {
                for (var r, t, a = "", n = "", c = 0, i = 0; t = e.charAt(i++); ~t && (r = c % 4 ? 64 * r + t : t,
                c++ % 4) ? a += String.fromCharCode(255 & r >> (-2 * c & 6)) : 0)
                    t = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+/=".indexOf(t);
                for (var f = 0, o = a.length; f < o; f++)
                    n += "%" + ("00" + a.charCodeAt(f).toString(16)).slice(-2);
                return decodeURIComponent(n)
            }
                ,
                e = arguments,
                de.ySkTSd = !0
        }
        var c = r + t[0]
            , i = e[c];
        return i ? n = i : (n = de.nZVaSF(n),
            e[c] = n),
            n
    }
        ,
        de(e, r)
}

function le(e, r) {
    return (e << (r %= 32) | e >>> 32 - r) >>> 0
}

function pe(e) {
    var r = ce;
    return 0 <= e && e < 16 ? 2043430169 : 16 <= e && e < 64 ? 2055708042 : void console[de(212)](r(199, "jE3R"))
}

function he(e, r, t, a) {
    var n = de;
    return 0 <= e && e < 16 ? (r ^ t ^ a) >>> 0 : 16 <= e && e < 64 ? (r & t | r & a | t & a) >>> 0 : (console[ce(166, "@lcn")](n(193)),
        0)
}

function ve(e, r, t, a) {
    var n = de;
    return 0 <= e && e < 16 ? (r ^ t ^ a) >>> 0 : 16 <= e && e < 64 ? (r & t | ~r & a) >>> 0 : (console[n(212)](n(179)),
        0)
}

be.prototype.reg = []

function encry_data(encrypt_data, s_num) {
    let s = {
    "s0": "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=",
    "s1": "Dkdpgh4ZKsQB80/Mfvw36XI1R25+WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=",
    "s2": "Dkdpgh4ZKsQB80/Mfvw36XI1R25-WUAlEi7NLboqYTOPuzmFjJnryx9HVGcaStCe=",
    "s3": "ckdp1h4ZKsUB80/Mfvw36XIgR25+WQAlEi7NLboqYTOPuzmFjJnryx9HVGDaStCe",
    "s4": "Dkdpgh2ZmsQB80/MfvV36XI1R45-WUAlEixNLwoqYTOPuzKFjJnry79HbGcaStCe"
    }
    let out = "";
    for (let i = 0; i < encrypt_data.length; i = i + 3) {
        let num1 = encrypt_data.charCodeAt(i) << 16 | encrypt_data.charCodeAt(i + 1) << 8 | encrypt_data.charCodeAt(i + 2)
        out += s[s_num].charAt((num1 & 16515072) >> 18)
        out += s[s_num].charAt((num1 & 258048) >> 12)
        out += s[s_num].charAt((num1 & 4032) >> 6)
        out += s[s_num].charAt((num1 & 63) >> 0)
    }
    return out
}

function main(url_data,houzui_url_data,my_UserAent) {
    new_time = Date.now()
    params_data = url_data+houzui_url_data
    // =============================================================================================================================
    // url需要动态传
    //url_data = "device_platform=webapp&aid=6383&channel=channel_pc_web&pc_client_type=1&version_code=290100&version_name=29.1.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Windows&os_version=10&cpu_core_num=32&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7324536676838295066&msToken=9kUZmcUrgBQoraT-2sjAV-b4J8Zt0CLYQ9Uodh-02CLFf6UYHZouB4KgPMP4L6ApKFNGa0P24SMS1VdNfETDFY5nc3H7mwCoUvbx3SnHFUErSD7wTBvEFB09cWSofw%3D%3D&X-Bogus=DFSzswVOMxGANcVXt54QuqVIViRqcus"
    url_arr_one = be.prototype.sum(params_data)      // url第一次处理得到32位数组，需要再次处理
    // url的32数组
    url_32_aryy = be.prototype.sum(url_arr_one)
    // console.log('params数组：',url_32_aryy)
    url_ind_21 = url_32_aryy[21]
    url_ind_22 = url_32_aryy[22]

    // =============================================================================================================================
    // 后缀，好像可以固定这个(这里还是改为动态传)
    //houzui_url_data = "mix_mode=1&account=2e3d332534323337363d3231363230&password=7f7c34323337363d3231363230&account_type=0&service=https%3A%2F%2Fwww.douyin.com&fixed_mix_mode=1cus"
    houzui_url_arr_one = be.prototype.sum(houzui_url_data)
    // console.log(houzui_url_arr_one)
    // 后缀的32位数组
    houzui_32_arry = be.prototype.sum(houzui_url_arr_one)  // 一样再次变32位数组
    // console.log('body数组:',houzui_32_arry)
    houzui_ind_21 = houzui_32_arry[21]
    houzui_ind_22 = houzui_32_arry[22]

    // // ===============================================================================================================================
    // // ua,可以固定
    // //my_UserAent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    ua_yihuo_arry = [58, 224, 211, 37, 198, 97, 237, 190, 110, 200, 227, 13, 40, 122, 190, 105, 177, 132, 123, 79, 69, 196, 89, 68, 188, 136, 89, 234, 212, 145, 178, 238, 94, 111, 139, 221, 91, 18, 89, 25, 17, 90, 36, 160, 37, 91, 254, 115, 116, 128, 81, 80, 247, 77, 240, 138, 242, 5, 159, 4, 5, 241, 52, 101, 152, 240, 68, 28, 60, 201, 27, 160, 36, 237, 151, 113, 193, 104, 44, 91, 132, 2, 224, 236, 177, 16, 220, 222, 211, 226, 225, 175, 100, 134, 98, 237, 190, 94, 142, 201, 66, 8, 164, 81, 199, 12, 37, 145, 125, 87, 163];
    ua_yh_ency_code = '';
    for (let indx = 0; indx < my_UserAent.length; indx++) {
        aaa = my_UserAent.charCodeAt(indx) ^ ua_yihuo_arry[indx]
        ua_yh_ency_code += String.fromCharCode(aaa)
    }

    UA_32_arry = be.prototype.sum(encry_data(ua_yh_ency_code, 's3'))
    // console.log("ua数组:",UA_32_arry)
    ua_ind_23 = UA_32_arry[23]
    ua_ind_24 = UA_32_arry[24]

    _ary44_1 = (new_time >> 24) & 255
    _ary44_11 = (new_time >> 16) & 255
    _ary44_21 = (new_time >> 8) & 255
    _ary44_26 = new_time & 255

    ayy_45 = (1712846736962 >> 16) & 255     // 1712846736962:navigator.vendorSubs 写死
    aay_46 = (1712846736962 >> 8) & 255
    ayy_47 = 1712846736962 & 255
    arry_44 = [
        44,
        _ary44_1,
        0,
        0,
        0,
        0,
        24,
        url_ind_21, // url_ind_21
        houzui_ind_21, // houzui_ind_21
        0,
        ua_ind_23, // ua_ind_23
        _ary44_11,
        0,
        24,//  固定  (6241>>8)&255
        97,  //固定  6241&255     pageId:6241
        1,
        0,
        239, //   固定 6383&255
        url_ind_22,  // url_ind_22
        houzui_ind_22,  // houzui_ind_22
        ua_ind_24,  // ua_ind_24
        _ary44_21,
        0,
        0,
        0,
        0,
        _ary44_26,
        0,
        0,
        8,
        _ary44_1,
        ayy_45,
        0,
        aay_46,
        ayy_47,
        3,
        398,
        1,
        398,
        1,
        67,
        0,
        0,
        0
    ]
    // console.log(arry_44)

    // arry_67 屏幕参数和电脑 :mac or win
    arry_67 = [ 49, 55, 48, 55, 124, 50, 52, 56, 124, 49, 55, 48, 55, 124, 49, 48, 49, 57, 124, 48, 124, 48, 124, 48, 124, 48, 124, 49, 55, 48, 55, 124, 49, 48, 49, 57, 124, 49, 55, 48, 55, 124, 49, 48, 54, 55, 124, 49, 54, 57, 54, 124, 50, 52, 56, 124, 50, 52, 124, 50, 52, 124, 87, 105, 110, 51, 50 ];

    // arry_di_112  112位数组最后一个添加，用的44位数组来操作的
    arry_di_112 = ((((((((((((((((((((((((((44 ^ _ary44_1) ^ url_ind_21) ^ houzui_ind_21) ^ ua_ind_23) ^ _ary44_11) ^ 1) ^ url_ind_22) ^ houzui_ind_22) ^ ua_ind_24) ^ _ary44_21) ^ _ary44_26) ^ 8) ^ _ary44_1) ^ ayy_45) ^ aay_46) ^ ayy_47) ^ 3) ^ 398) ^ 1) ^ 398) ^ 1) ^ 24) ^ 97) ^ 239) ^ 24) ^ 67)

    arry_112 = arry_44.concat(arry_67).concat([arry_di_112])
    str_112= String.fromCharCode.apply(null, arry_112)

    code_js = ""
    for (var arry_2 of [[3, 45], [1, 0], [1, 7]]) {
        a_1 = Math.random() * 10000
        a_2 = a_1 & 255       // 加  44
        a_3 = (a_1 >> 8) & 255  // 加  19
        a_4 = (a_2 & 170) | (arry_2[0] & 85) // 41  加上
        a_5 = (a_2 & 85) | (arry_2[0] & 170)  // 4    加上
        a_6 = (a_3 & 170) | (arry_2[1] & 85)   //  2
        a_7 = (a_3 & 85) | (arry_2[1] & 170)  // 17
        arry_4_odd = [a_4, a_5, a_6, a_7]
        str_4 = String.fromCharCode.apply(null, arry_4_odd)
        // console.log(arry_4_odd,str_4)2
        code_js += str_4
    }

    var yw_ency_code = "";
    var yw_112_arry = [69, 132, 164, 66, 132, 231, 73, 53, 233, 160, 170, 115, 55, 196, 129, 61, 1, 127, 117, 23, 27, 246, 68, 246, 220, 250, 0, 219, 248, 168, 151, 91, 81, 62, 131, 51, 28, 146, 16, 90, 187, 48, 209, 145, 73, 144, 10, 179, 176, 150, 128, 5, 5, 97, 236, 240, 82, 68, 94, 183, 16, 115, 49, 197, 198, 246, 90, 83, 12, 89, 68, 67, 207, 119, 56, 252, 224, 83, 92, 46, 111, 195, 206, 250, 89, 36, 239, 178, 148, 125, 175, 103, 139, 142, 186, 49, 75, 91, 131, 92, 105, 173, 157, 61, 204, 223, 13, 125, 235, 124, 65, 153]
    for (let indx = 0; indx < str_112.length; indx++) {
        aaa = str_112.charCodeAt(indx) ^ yw_112_arry[indx]
        yw_ency_code += String.fromCharCode(aaa)
    }

    let encrypt_data = code_js + yw_ency_code
    out_data = encry_data(encrypt_data, 's4')
    return out_data.substr(0,out_data.length - 2) + "=="
    }

url_data = 'device_platform=webapp&aid=6383&channel=channel_pc_web&publish_video_strategy_type=2&source=channel_pc_web&sec_user_id=MS4wLjABAAAAWsio_U6flDvc9euioRh2r8L-2WrY_hEZ9aigb9DUceXGAveswp8-2KO21EzZL7GO&personal_center_strategy=1&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1920&screen_height=1080&browser_language=zh-CN&browser_platform=MacIntel&browser_name=Chrome&browser_version=123.0.0.0&browser_online=true&engine_name=Blink&engine_version=123.0.0.0&os_name=Mac+OS&os_version=10.15.7&cpu_core_num=10&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7350586071452124722&msToken=ZvApsQvjq4SBIotyKNCIXLE4nQBQy6CFkU3Sfk-BvwFRCxGECRfuOY1AoiGH5FRb2RcH13no0PirrWhuOCRsy4MQLmAtpOzdwcs5-vZpXrgRisTNl4QJNIKa01x38ojD'
houzui_url_data = "cus"
my_UserAent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

console.log(main(url_data, houzui_url_data, my_UserAent));