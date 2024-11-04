const CryptoJs = require('crypto-js')

a = {
    IZRud: function (Y, _) {
        return Y >> _
    },
    nzLeM: function (Y, _) {
        return Y * _
    },
    BzvoD: function (Y, _) {
        return Y & _
    },
    ozvBe: function (Y, _) {
        return Y >> _
    },
    mHMuw: function (Y, _) {
        return Y + _
    },
    JXbhs: function (Y, _) {
        return Y - _
    },
    rlOzS: function (Y, _) {
        return Y(_)
    },
    cMiYr: function (Y, _) {
        return Y < _
    }
};
generateNonce = function (Y) {
    return Array(Y)["fill"](0)["map"](function () {
        var nn = (255 & Math["floor"](12345 * Math["random"]()))["toString"](16);
        return nn["length"] < 2 ? "0"["concat"](nn) : nn;
    })["join"]("");
}

function KegpP(Y, _) {
    return Y / _
}

xorCipher = function (Y, _) {
    for (var nr = "", nu = 0; nu < Y["length"]; nu++) {
        var ni = Y["charCodeAt"](nu)
            , ne = _["charCodeAt"](nu % _["length"]);
        nr += String["fromCharCode"](ni ^ ne)
    }
    return nr
}

function wWUhM(Y, _) {
    return a["JXbhs"](Y, _)
}

function iXHDA(Y, _) {
    return Y & _
}

function exbsF(Y, _) {
    return Y * _
}

str2binl = function (Y, _) {
    void 0 === _ && (_ = 8);
    for (var nu = [], ni = wWUhM(1 << _, 1), ne = 0; ne < Y["length"] * _; ne += _)
        nu[ne >> 5] |= iXHDA(Y["charCodeAt"](ne / _), ni) << ne % 32;
    return nu
}
binl2b64 = function (Y, _) {
    void 0 === _ && (_ = "");
    for (var nr = "", nu = 0; nu < 4 * Y["length"]; nu += 3)
        for (var ni = (Y[a["IZRud"](nu, 2)] >> a["nzLeM"](nu % 4, 8) & 255) << 16 | a["BzvoD"](Y[nu + 1 >> 2] >> (nu + 1) % 4 * 8, 255) << 8 | Y[a["ozvBe"](nu + 2, 2)] >> a["mHMuw"](nu, 2) % 4 * 8 & 255, ne = 0; ne < 4; ne++)
            a["mHMuw"](8 * nu, 6 * ne) > 32 * Y["length"] ? nr += _ : nr += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"["charAt"](ni >> 6 * (3 - ne) & 63);
    return nr
}

getSignedParams = function (Y) {
    Y = Y || {};
    for (var nn = Math["floor"](KegpP(Date["now"](), 1e3)), nu = generateNonce(16), nf = 1, no = 0, nc = [], nv = [], na = 0; na < 3; na++) {
        var nh = Math["floor"](1e3 * Math["random"]()) % 48 + 43
            , ns = Math["floor"](exbsF(1e3, Math["random"]())) % 48 + 43;
        nc["push"](String["fromCharCode"](nh)),
            nv["push"](String["fromCharCode"](ns))
    }
    var ny = [nc["join"](""), 1, 0, 1, nn, nv["join"]("")]["join"]("")
        , nw = xorCipher(ny, "9A6E5AF4B9E7DBF")
        , ng = {};
    ng["hk_nonce"] = nu,
        ng["hk_timestamp"] = nn;
    var nC = CryptoJs.MD5(nu + Object["keys"](Y)["sort"]()["map"](function (nn) {
        return ""["concat"](nn, "=")["concat"](Y[nn])
    })["join"]("") + "guanghui123" + nn).toString();
    console.log(nw)
    return ng["hk_sign"] = nC,
        ng["hk_token"] = binl2b64(str2binl(nw)),
        ng
}

console.log(getSignedParams(1708328032046))
