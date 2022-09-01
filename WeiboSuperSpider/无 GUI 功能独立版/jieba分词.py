import jieba.analyse
import re
import os
#   提取特征词所用
# if os.path.exists('topic/分词结果.csv'):
#     os.remove('topic/分词结果.csv')
num = 5    #特征词个数
fout = open('分词结果~'+str(num)+'-1.csv', 'w', encoding='utf-8')
if __name__ == '__main__':
    with open('laji_zh.csv', 'r', encoding='utf-8') as fp:
        lists = fp.readlines()
        jieba.analyse.TextRank()
        #print(lists)
        for ll in lists:
            line = ll.split('\t')
            try:
                jieba.analyse.set_stop_words('topic/stop_words.txt')
                str = ",".join(jieba.analyse.textrank(line[2],topK=num,withWeight=False,allowPOS=('ns','n','vn','v')))
                fout.writelines(str+'\n')          #7是微博正文
            except Exception as re:
                print(re)
print("特征词提取完成！")