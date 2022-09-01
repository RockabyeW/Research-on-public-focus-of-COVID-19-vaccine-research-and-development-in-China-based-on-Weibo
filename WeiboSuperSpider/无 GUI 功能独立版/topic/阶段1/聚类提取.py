import re
file = open("阶段.txt", "r", encoding="utf-8")
text = file.readlines()
dic = {}
sum = 0
for line in text:
    for word in line.split(','):
        word = word.replace("\n",'')
        sum += 1
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
newdic = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)

for k,v in newdic:
    print(k," ",v)