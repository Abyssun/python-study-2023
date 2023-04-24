import jieba
with open("F:\python-study-2023\week8\\threekingdoms-utf8.txt","r",encoding='utf-8') as f:  # 打开文件
        txt = f.read()
# txt = open("F:\python-study-2023\week8\\threekingdoms.txt","r",encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15000):
    word,count = items[i]
    print("{0:<10}{1:<5}".format(word,count))

d1 = items
ans = ",".join(map(str, d1))
# Data = "_".join(d1)
# Data = word,count
File = open('1.txt',mode="w")
File.write(ans)
File.close()