# -*- coding: utf-8 -*-
# @Author   : HeLaoshi
# @File     : demo1.py
# @Project  : pythonProject2
import hashlib


md5 = hashlib.md5()
md5.update('api/product/getproductsearch?flag=top&page=3&per_page=12&timestamp=1692105973076&key=6rnrdpjjv6wz2sspxqeibesov1itxddc'.encode('utf-8'))
print(md5.hexdigest())
