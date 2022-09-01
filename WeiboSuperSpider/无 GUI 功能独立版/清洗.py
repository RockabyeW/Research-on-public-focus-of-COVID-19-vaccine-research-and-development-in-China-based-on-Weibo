import re
import os

def clean(text):
    text = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
    text = re.sub(r"\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDE4F]|\uD83D[\uDE80-\uDEFF]|[\u2700-\u27BF]\uFE0F"," ",text)
    # text = re.sub(r"#\S+#", "", text)      # 保留话题内容
    URL_REGEX = re.compile(
        r'(?i)((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    text = re.sub(URL_REGEX, "", text)       # 去除网址
    text = text.replace("转发微博", "")       # 去除无意义的词语
    text = re.sub(r"\s+", " ", text) # 合并正文中过多的空格
    return text.strip()

if os.path.exists('topic/过滤id1.csv'):
    os.remove('topic/过滤id1.csv')
fout = open('topic/过滤id1.csv', 'a', encoding='utf-8')
if __name__ == '__main__':
    with open('topic/过滤id.csv', 'r', encoding='utf-8') as fp:
        lists = fp.readlines()
        for ll in lists:
            l = clean(ll)  # 数据清洗
            fout.writelines(l+'\n')  # 写入文件
    fout.close()