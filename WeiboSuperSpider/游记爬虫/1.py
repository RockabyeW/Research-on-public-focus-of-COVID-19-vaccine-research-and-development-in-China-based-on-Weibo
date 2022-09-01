# coding=utf-8
# author=zhangjingyuan
# python3

import urllib.request
import urllib.parse
import re
import time
import io
import gzip
import random

#页数范围
min = 74
max = 456


headerS={
'Cookie':'__jsluid_h=0e6a56702d4f8ae879f6d65447ac14f4; __jsl_clearance=1630425589.555|0|qEHjeB8PgJ026wssZZB0qV6C0T8%3D; PHPSESSID=v8gteku8rnbi0sellm3qrkqlq4; mfw_uuid=612e51f7-7a1d-38ea-396a-cc7a815200a4; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-08-31+23%3A59%3A51%22%3B%7D; __mfwc=direct; __mfwa=1630425592150.29215.1.1630425592150.1630425592150; __mfwlv=1630425592; __mfwvn=1; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1630425592; uva=s%3A91%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1630425591%3Bs%3A10%3A%22last_refer%22%3Bs%3A23%3A%22http%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1630425591%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=612e51f7-7a1d-38ea-396a-cc7a815200a4; UM_distinctid=17b9cf035d517-05867d55554981-c343365-144000-17b9cf035d7750; login=mafengwo; mafengwo=a2775bd562b94428c9f9e87e6ea4e966_89598849_612e533cea31f7.56912359_612e533cea3255.77473555; uol_throttle=89598849; mfw_uid=89598849; __omc_chl=; __omc_r=; CNZZDATA30065558=cnzz_eid%3D769255033-1630415109-http%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1630409746; bottom_ad_status=0; __mfwb=e535eac1c390.5.direct; __mfwlt=1630425929; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1630425930',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
file = open("pages.txt", 'a')
for i in range(min,max):
    try:
        url="http://www.mafengwo.cn/yj/10684/2-0-"+str(i)+".html"
        request = urllib.request.Request(url,data=None,headers=headerS)
        response = urllib.request.urlopen(request)
        page = response.read()
        iopage=io.BytesIO(page)
        depage = gzip.GzipFile(fileobj=iopage, mode="rb")
        #gzip解压缩
        html=depage.read().decode('utf-8')
        print(i)
        pattern = re.compile('/i/.*?.html', re.S)
        #查找其中形如/i/…….html的链接
        result = re.findall(pattern, html)
        print(result)
        for item in result:
            file.write(item+'\n')
        time.sleep(random.random())
    except urllib.request.URLError as e:
        if hasattr(e, 'reason'):
            print('出错：' + str(e.reason))
        print('pass')
print("爬取完毕了！honey~~~~~~~~~~~~~~")
file.close()
