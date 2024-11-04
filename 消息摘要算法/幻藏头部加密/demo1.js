// npm install crypto-js
const CryptoJs = require('crypto-js');

function md5encrypt(text) {
    encrypt1 = CryptoJs.MD5(text).toString()
    return encrypt1
}

var Ci = {
    objKeySort: A=>{
        for (var i = Object.keys(A).sort(), e = {}, t = 0; t < i.length; t++)
            (A[i[t]] || "0" == A[i[t]]) && (e[i[t]] = A[i[t]]);
        return e
    }
    ,
    getparam: A=>{
        var i = "?";
        for (var e in A)
            i += e,
            i += "=",
            i += A[e],
            i += "&";
        return i = i.substr(0, i.length - 1)
    }
    ,
    getQueryVariable: A=>{
        for (var i = window.location.hash.substring(1), e = (i = i.split("?")[1]).split("&"), t = 0; t < e.length; t++) {
            var I = e[t].split("=");
            if (I[0] == A)
                return I[1]
        }
        return !1
    }
    ,
    formatDate: A=>{
        if (A) {
            let i = Math.floor(A / 1e3 / 60 / 60)
              , e = Math.floor(A / 1e3 / 60 % 60)
              , t = Math.floor(A / 1e3 % 60);
            return i = i < 10 ? "0" + i : i,
            e = e < 10 ? "0" + e : e,
            t = t < 10 ? "0" + t : t,
            i + "h " + e + "m " + t + "s"
        }
    }
    ,
    contract: (A,i=4,e=3)=>A && A.replace(new RegExp("(.{" + i + "}).*(.{" + e + "})"), "$1******$2"),
    toast: (A,i="error")=>{
        L({
            message: A,
            type: i,
            customClass: "huancang"
        })
    }
    ,
    copyText: A=>{
        let i = document.createElement("textarea");
        i.value = A,
        document.body.appendChild(i),
        i.select(),
        document.execCommand("Copy"),
        L({
            message: "复制成功",
            type: "success",
            customClass: "huancang"
        }),
        i.remove()
    }
    ,
    setStorage: (A,i)=>{
        "string" == typeof i ? localStorage.setItem(A, i) : localStorage.setItem(A, JSON.stringify(i))
    }
    ,
    getStorage: A=>{
        let i = localStorage.getItem(A);
        return i ? 0 == i.indexOf("{") || 0 == i.indexOf("[") ? JSON.parse(i) : i : ""
    }
    ,
    routerTo: A=>{
        Fi.push(A)
    }
    ,
    navTo: A=>{
        A.indexOf && 0 == A.indexOf("http") ? null != window.open(A) || (window.location.href = A) : Fi.push(A)
    }
    ,
    strTrim: (A,i)=>{
        let e;
        return e = A.replace(/(^\s+)|(\s+$)/g, ""),
        i && "g" == i.toLowerCase() && (e = e.replace(/\s/g, "")),
        e
    }
    ,
    getImg: A=>{
        const i = `/src/assets/img/${A}`;
        let e;
        return A.indexOf("svg/") > -1 ? (e = {
            "/src/assets/img/svg/no-data.svg": Ui
        },
        e[i] && e[i].default) : (e = {
            "/src/assets/img/2022.png": q,
            "/src/assets/img/address.png": _,
            "/src/assets/img/alipay.png": $,
            "/src/assets/img/b-title-l.png": AA,
            "/src/assets/img/b-title-r.png": iA,
            "/src/assets/img/balance.png": eA,
            "/src/assets/img/bank.png": IA,
            "/src/assets/img/banner-collection.jpg": cA,
            "/src/assets/img/banner1.jpg": mA,
            "/src/assets/img/bg-l.png": MA,
            "/src/assets/img/bg-r.png": bA,
            "/src/assets/img/bh.png": ZA,
            "/src/assets/img/bh2-1.png": GA,
            "/src/assets/img/bh2.png": RA,
            "/src/assets/img/check.png": gA,
            "/src/assets/img/close.png": dA,
            "/src/assets/img/cz.png": aA,
            "/src/assets/img/default-avatar.png": YA,
            "/src/assets/img/delete.png": NA,
            "/src/assets/img/dizuo.png": jA,
            "/src/assets/img/ewm.png": nA,
            "/src/assets/img/exchangebg.jpg": hA,
            "/src/assets/img/fm.png": DA,
            "/src/assets/img/footer-logo.png": pA,
            "/src/assets/img/ga.png": WA,
            "/src/assets/img/gaw.jpg": zA,
            "/src/assets/img/gift-on.png": yA,
            "/src/assets/img/gift.png": uA,
            "/src/assets/img/hcbg.jpg": SA,
            "/src/assets/img/hclogo2.png": EA,
            "/src/assets/img/hcys.png": sA,
            "/src/assets/img/icp.jpg": TA,
            "/src/assets/img/inviteFriends-on.png": LA,
            "/src/assets/img/inviteFriends.png": UA,
            "/src/assets/img/jc.png": vA,
            "/src/assets/img/js.png": VA,
            "/src/assets/img/lock.png": CA,
            "/src/assets/img/logo.png": rA,
            "/src/assets/img/more.png": BA,
            "/src/assets/img/no-sc.png": HA,
            "/src/assets/img/notice-on.png": PA,
            "/src/assets/img/notice.jpg": XA,
            "/src/assets/img/notice.png": fA,
            "/src/assets/img/orders-on.png": KA,
            "/src/assets/img/orders.png": qA,
            "/src/assets/img/play.png": $A,
            "/src/assets/img/qb.png": ii,
            "/src/assets/img/sandpay.png": ei,
            "/src/assets/img/set-on.png": ti,
            "/src/assets/img/set.png": Ii,
            "/src/assets/img/sy.png": li,
            "/src/assets/img/synthesis-on.png": mi,
            "/src/assets/img/synthesis.png": Mi,
            "/src/assets/img/tx.png": Zi,
            "/src/assets/img/uncheck.png": Gi,
            "/src/assets/img/user.png": Ri,
            "/src/assets/img/userCenter-on.png": gi,
            "/src/assets/img/userCenter.png": di,
            "/src/assets/img/v.png": Yi,
            "/src/assets/img/wallet-on.png": oi,
            "/src/assets/img/wallet.png": Ni,
            "/src/assets/img/wb.png": ji,
            "/src/assets/img/wechat_pay.png": ni,
            "/src/assets/img/wx.png": Di,
            "/src/assets/img/xs.png": pi,
            "/src/assets/img/ysp.jpg": wi,
            "/src/assets/img/zeng.png": zi,
            "/src/assets/img/zl.png": ui,
            "/src/assets/img/zm.png": Si,
            "/src/assets/img/zs.png": Ei,
            "/src/assets/img/zs1.png": si,
            "/src/assets/img/zz.jpg": Ti,
            "/src/assets/img/zz.png": Li
        },
        e[i] && e[i].default)
    }
    ,
    formatImgUrl: A=>{
        const {proxy: i} = b();
        if (A)
            return -1 == A.indexOf("base64") && 0 != A.indexOf("http") && (A = (A = `${i.$fileUrl}${A}`).replace("//uploads", "/uploads")),
            A
    }
    ,
    date: (A,i)=>{
        i = "" + i.length <= 10 ? 1e3 * +i : +i;
        let e = new Date(i)
          , t = e.getFullYear()
          , I = e.getMonth() + 1
          , c = e.getDate()
          , l = e.getHours()
          , m = e.getMinutes()
          , M = e.getSeconds();
        return I = I < 10 ? "0" + I : I,
        c = c < 10 ? "0" + c : c,
        l = l < 10 ? "0" + l : l,
        m = m < 10 ? "0" + m : m,
        M = M < 10 ? "0" + M : M,
        A.replace(/[YmdHis]/g, (A=>({
            Y: t,
            m: I,
            d: c,
            H: l,
            i: m,
            s: M
        }[A])))
    }
    ,
    checkStr: (A,i)=>{
        switch (i) {
        case "mobile":
            return /^1[3|4|5|6|7|8|9][0-9]{9}$/.test(A);
        case "tel":
            return /^(0\d{2,3}-\d{7,8})(-\d{1,4})?$/.test(A);
        case "card":
            return /(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)/.test(A);
        case "mobileCode":
            return /^[0-9]{4}$/.test(A);
        case "bankAccount":
            return /^[0-9]{16}$/.test(A);
        case "pwd":
            return /^([a-zA-Z0-9_]){6,18}$/.test(A);
        case "payPwd":
            return /^[0-9]{6}$/.test(A);
        case "postal":
            return /[1-9]\d{5}(?!\d)/.test(A);
        case "QQ":
            return /^[1-9][0-9]{4,9}$/.test(A);
        case "email":
            return /^[\w-]+(\.[\w-]+)*@[\w-]+(\.[\w-]+)+$/.test(A);
        case "money":
            return /^\d*(?:\.\d{0,2})?$/.test(A);
        case "URL":
            return /(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?/.test(A);
        case "IP":
            return /((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d))/.test(A);
        case "date":
            return /^(\d{4})\-(\d{2})\-(\d{2}) (\d{2})(?:\:\d{2}|:(\d{2}):(\d{2}))$/.test(A) || /^(\d{4})\-(\d{2})\-(\d{2})$/.test(A);
        case "number":
            return /^[0-9]$/.test(A);
        case "english":
            return /^[a-zA-Z]+$/.test(A);
        case "chinese":
            return /^[\\u4E00-\\u9FA5]+$/.test(A);
        case "lower":
            return /^[a-z]+$/.test(A);
        case "upper":
            return /^[A-Z]+$/.test(A);
        case "HTML":
            return /<("[^"]*"|'[^']*'|[^'">])*>/.test(A);
        default:
            return !0
        }
    }
};


let i = (new Date).getTime()
data = {
    "page": 2,
    "per_page": 12,
    "flag": "top",
    "timestamp": i
}
data = Ci.getparam(Ci.objKeySort(data));
data = `${data}&key=${"6RNRDpjjV6wZ2ssPxqeIBeSoV1ITXDdC"}`
path = 'api/product/getProductSearch'
e = (path + data).toLowerCase()


signature = md5encrypt(md5encrypt("7Tv7LrinK2bsNAi9TF2uui3ZIcoxK1WT"))
console.log(signature)

