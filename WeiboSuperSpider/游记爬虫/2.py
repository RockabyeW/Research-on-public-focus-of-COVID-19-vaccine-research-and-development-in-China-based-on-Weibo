# coding=utf-8
# author=zhangjingyuan
# python3
from html.parser import HTMLParser
import lxml
from lxml import etree
import urllib.request
import urllib.parse
import re
import time
import io
import gzip
import random
import codecs


min = 50
max = 500

headerS={
'Cookie':'__jsluid_h=0e6a56702d4f8ae879f6d65447ac14f4; __jsl_clearance=1630425589.555|0|qEHjeB8PgJ026wssZZB0qV6C0T8%3D; PHPSESSID=v8gteku8rnbi0sellm3qrkqlq4; mfw_uuid=612e51f7-7a1d-38ea-396a-cc7a815200a4; oad_n=a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222021-08-31+23%3A59%3A51%22%3B%7D; __mfwc=direct; __mfwa=1630425592150.29215.1.1630425592150.1630425592150; __mfwlv=1630425592; __mfwvn=1; Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0=1630425592; uva=s%3A91%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1630425591%3Bs%3A10%3A%22last_refer%22%3Bs%3A23%3A%22http%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B; __mfwurd=a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1630425591%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D; __mfwuuid=612e51f7-7a1d-38ea-396a-cc7a815200a4; UM_distinctid=17b9cf035d517-05867d55554981-c343365-144000-17b9cf035d7750; login=mafengwo; mafengwo=a2775bd562b94428c9f9e87e6ea4e966_89598849_612e533cea31f7.56912359_612e533cea3255.77473555; uol_throttle=89598849; mfw_uid=89598849; __omc_chl=; __omc_r=; CNZZDATA30065558=cnzz_eid%3D769255033-1630415109-http%253A%252F%252Fwww.mafengwo.cn%252F%26ntime%3D1630409746; bottom_ad_status=0; __mfwb=e535eac1c390.5.direct; __mfwlt=1630425929; Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0=1630425930',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
list=open("pages.txt",'r')
file=codecs.open("rsult.csv",'a','utf-8')
i=0
for line in list:
    i = i + 1
    print(i)
    if(i%2==0):
        continue
    content=""
    print(line)
    url="http://www.mafengwo.cn"+line
    request = urllib.request.Request(url,data=None,headers=headerS)
    response = urllib.request.urlopen(request)
    page = response.read()
    iopage=io.BytesIO(page)
    depage = gzip.GzipFile(fileobj=iopage, mode="rb")
    html=depage.read().decode('utf-8')
    Htree = etree.HTML(html)
    print(etree.tostring(Htree))
    body=Htree[1]
    #print(etree.tostring(body))
    main=body[1]
    #print(etree.tostring(main))
    view=main[3]
    #此处使用etree以获取游记正文部分
    content = content + etree.tostring(view).decode('utf-8')
    content=HTMLParser().unescape(content)
    dr = re.compile(r'<[^>]+>', re.S)
    dd = dr.sub('', content)
    dr = re.compile('\n', re.S)
    dd = dr.sub('', dd)
    dr = re.compile(' ', re.S)
    res = dr.sub('', dd)
    #去除富文本标签、换行符、空格等
    print(res)
    file.write(str(res)+'\n')
    time.sleep(random)
file.close()
