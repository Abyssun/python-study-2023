# Hamlet词频统计
def getText():
    with open("F:\python-study-2023\week8\hamlet.txt", "r") as f:  # 打开文件
        txt = f.read()  # 读取文件
    #print(txt)
    # txt = open("F:\\python-study-2023\\week8\hamlet.txt","rw").read
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        txt = txt.replace(ch," ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1

items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))