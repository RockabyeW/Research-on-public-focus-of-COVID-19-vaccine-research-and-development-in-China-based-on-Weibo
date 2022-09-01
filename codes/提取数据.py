import json

# with open('D:\学习资料\专家匹配\publications_0415.json', encoding='utf-8') as f:
#     line = f.readline()
#     d = json.loads(line)
#     print(type(d))
#     for i in d:
#         #print(type(i))
#         print(i)
#     f.close()

# {
#  "id":"5e3fd866df1a9c0c41ecef77",
#  "title":"Introduction to Purinergic Signalling in the Brain.",
#  "abstract":"ATP is a cotransmitter with glutamate, noradrenaline...",
# "abstract_zh":"ATP 与谷氨酸、去甲肾上腺素共同传递...",
#  "keywords":["ATP","Adenosine"],
#  "keywords_zh":["三磷酸腺苷"],
#  "year":2019
# }
#
# import json
#
# file = "laji.csv"
# print("开始读取文件")
# f1 = open(file,"w",encoding="utf8")
# with open('D:\\python3-fp-growth-master\\benchmark_experts.json', encoding='utf-8') as f:
#     line = f.readline()
#     total = json.loads(line)
#     print(type(total))
#     for d in total:
#         # print(type(d))
#         # print(d)
#         # print(type(d['publications']))
#         name_en = d['name_en']
#         name_zh = d["name_zh"]
#         # abstract_list = []
#         for i in d['publications']:
#             try:
#                 abstract = i['abstract']
#                 abstract = abstract.replace('\n',' ')
#                 f1.write(name_en + '\t' + name_zh + '\t' + abstract + '\n')
#             except Exception as re:
#                 print(re)
#
#         # title = d['title']
#         # abstract = d['abstract']
#         # abstract_zh = d['abstract_zh']
#         #
#         # print(name_en,name_zh,title,abstract,abstract_zh)
#     print("提取完成！")
#     f.close()


import json

file = "laji_en.csv"
print("开始读取文件")
f1 = open(file,"w",encoding="utf8")
with open('D:\学习资料\机器学习\TFIDF提取关键词\\benchmark_experts.json', encoding='utf-8') as f:
    line = f.readline()
    total = json.loads(line)
    print(type(total))
    for d in total:
        # print(type(d))
        # print(d)
        # print(type(d['publications']))
        name_en = d['name_en']
        name_zh = d["name_zh"]
        # abstract_list = []
        for i in d['publications']:
            try:
                abstract = i['abstract']
                abstract = abstract.replace('\n',' ')
                f1.write(name_en + '\t' + name_zh + '\t' + abstract + '\n')
            except Exception as re:
                print(re)

        # title = d['title']
        # abstract = d['abstract']
        # abstract_zh = d['abstract_zh']
        #
        # print(name_en,name_zh,title,abstract,abstract_zh)
    print("提取完成！")
    f.close()
