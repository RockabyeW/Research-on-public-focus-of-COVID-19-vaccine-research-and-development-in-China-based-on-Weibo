# -*- coding: utf-8 -*-
# author:           inspurer(月小水长)
# pc_type           lenovo
# create_time:      2019/8/16 16:10
# file_name:        WeiboCommentScrapy.py
# github            https://github.com/inspurer
# qq邮箱            2391527690@qq.com
# 微信公众号         月小水长(ID: inspurer)

import requests

requests.packages.urllib3.disable_warnings()

from lxml import etree

from datetime import datetime, timedelta

from threading import Thread

import csv

from math import ceil

import os

import re
from time import sleep
from random import randint

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Cookie':
        'SINAGLOBAL=1716345528530.0723.1595312694525; ULV=1615100228611:5:4:2:7689363341253.556.1615100228610:1615098572426; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFD-1G7YQqjqIONwLyDvpEw5JpX5KzhUgL.FoM0S0-4ShnNS022dJLoI0qLxK.L1KnLB.qLxKBLB.eLBKqLxK.L1KnLB.qLxKqLB-eLBKMLxK.L1KnLB.qLxKMLB.qL1h2t; UOR=,,login.sina.com.cn; un=15329923834; httpsupgrade_ab=SSL; webim_unReadCount=%7B%22time%22%3A1615103939222%2C%22dm_pub_total%22%3A8%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A52%2C%22msgbox%22%3A0%7D; SCF=AnqUT6xeegmeY0rMYaMaSn4H6lihlusFozurCzRBgI11tHr3TvXpElL4NAZsS6FcR8RnLUFeg8BRK3Kz9z8UF74.; wb_timefeed_6420956726=1; wb_view_log_6420956726=1536*8641.25; SUB=_2A25NQPY9DeRhGeFN7FcY9CbLzD2IHXVuNGD1rDV8PUNbmtAfLRH3kW9NQ8NmWhZtBDS2zIy-uXUPuRwcZL_pwqyL; wb_view_log=1536*8641.25; login_sid_t=723e3675a7ad0f017b7ae70216dcd6b6; cross_origin_proto=SSL; _s_tentry=-; Apache=7689363341253.556.1615100228610; SSOLoginState=1615103555; ALF=1646639595; wvr=6; wb_view_log_7375948771=1536*8641.25'
}

class WeiboCommentScrapy(Thread):

    def __init__(self,wid):
        global headers
        Thread.__init__(self)
        self.headers = headers
        self.result_headers = [
            '评论者主页',
            '评论者昵称',
            '评论者性别',
            '评论者所在地',
            '评论者微博数',
            '评论者关注数',
            '评论者粉丝数',
            '评论内容',
            '评论获赞数',
            '评论发布时间',
        ]
        if not os.path.exists('comment'):
            os.mkdir('comment')
        self.wid = wid
        self.start()

    def parse_time(self,publish_time):
        publish_time = publish_time.split('来自')[0]
        if '刚刚' in publish_time:
            publish_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        elif '分钟' in publish_time:
            minute = publish_time[:publish_time.find('分钟')]
            minute = timedelta(minutes=int(minute))
            publish_time = (datetime.now() -
                            minute).strftime('%Y-%m-%d %H:%M')
        elif '今天' in publish_time:
            today = datetime.now().strftime('%Y-%m-%d')
            time = publish_time[3:]
            publish_time = today + ' ' + time
        elif '月' in publish_time:
            year = datetime.now().strftime('%Y')
            month = publish_time[0:2]
            day = publish_time[3:5]
            time = publish_time[7:12]
            publish_time = year + '-' + month + '-' + day + ' ' + time
        else:
            publish_time = publish_time[:16]
        return publish_time

    def getPublisherInfo(self,url):
        res = requests.get(url=url,headers=self.headers,verify=False)
        html = etree.HTML(res.text.encode('utf-8'))
        head = html.xpath("//div[@class='ut']/span[1]")[0]
        head = head.xpath('string(.)')[:-3].strip()
        keyIndex = head.index("/")
        nickName = head[0:keyIndex-2]
        sex = head[keyIndex-1:keyIndex]
        location = head[keyIndex+1:]

        footer = html.xpath("//div[@class='tip2']")[0]
        weiboNum = footer.xpath("./span[1]/text()")[0]
        weiboNum = weiboNum[3:-1]
        followingNum = footer.xpath("./a[1]/text()")[0]
        followingNum = followingNum[3:-1]
        followsNum = footer.xpath("./a[2]/text()")[0]
        followsNum = followsNum[3:-1]
        print(nickName,sex,location,weiboNum,followingNum,followsNum)
        return nickName,sex,location,weiboNum,followingNum,followsNum

    def get_one_comment_struct(self,comment):
        # xpath 中下标从 1 开始
        userURL = "https://weibo.cn/{}".format(comment.xpath(".//a[1]/@href")[0])

        content = comment.xpath(".//span[@class='ctt']/text()")
        # '回复' 或者只 @ 人
        if '回复' in content or len(content)==0:
            test = comment.xpath(".//span[@class='ctt']")
            content = test[0].xpath('string(.)').strip()

            # 以表情包开头造成的 content == 0,文字没有被子标签包裹
            if len(content)==0:
                content = comment.xpath('string(.)').strip()
                content = content[content.index(':')+1:]
        else:
            content = content[0]

        praisedNum = comment.xpath(".//span[@class='cc'][1]/a/text()")[0]
        praisedNum = praisedNum[2:praisedNum.rindex(']')]

        publish_time = comment.xpath(".//span[@class='ct']/text()")[0]

        publish_time = self.parse_time(publish_time)
        nickName,sex,location,weiboNum,followingNum,followsNum = self.getPublisherInfo(url=userURL)

        return [userURL,nickName,sex,location,weiboNum,followingNum,followsNum,content,praisedNum,publish_time]

    def write_to_csv(self,result,isHeader=False):
        with open('comment/' + self.wid + '.csv', 'a', encoding='utf-8-sig', newline='') as f:
            writer = csv.writer(f)
            if isHeader == True:
                writer.writerows([self.result_headers])
            writer.writerows(result)
        print('已成功将{}条评论写入{}中'.format(len(result),'comment/' + self.wid + '.csv'))

    def run(self):
        res = requests.get('https://weibo.cn/comment/{}'.format(self.wid),headers=self.headers,verify=False)
        commentNum = re.findall("评论\[.*?\]",res.text)[0]
        commentNum = int(commentNum[3:len(commentNum)-1])
        print(commentNum)
        pageNum = ceil(commentNum/10)
        print(pageNum)
        for page in range(pageNum):

            result = []

            res = requests.get('https://weibo.cn/comment/{}?page={}'.format(self.wid,page+1), headers=self.headers,verify=False)

            html = etree.HTML(res.text.encode('utf-8'))

            comments = html.xpath("/html/body/div[starts-with(@id,'C')]")

            print('第{}/{}页'.format(page+1,pageNum))

            for i in range(len(comments)):
                result.append(self.get_one_comment_struct(comments[i]))

            if page==0:
                self.write_to_csv(result,isHeader=True)
            else:
                self.write_to_csv(result,isHeader=False)

            sleep(randint(1,5))

if __name__ =="__main__":
    WeiboCommentScrapy(wid='K4zUJ5chp')

