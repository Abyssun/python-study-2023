import jieba
excludes = {"将军","却说","荆州","二人","不可","不能","如此"}
with open("F:\python-study-2023\week8\\threekingdoms-utf8.txt","r",encoding='utf-8') as f:  # 打开文件
        txt = f.read()

words = jieba.lcut(txt)
counts = {}
for word in words:
        if len(word) == 1:
                continue
        elif word == "诸葛亮" or word == "孔明曰":
                rword = "孔明"
        elif word == "关公" or word =="云长":
                rword = "关羽"
        elif word == "玄德" or word == "玄德曰":
                rword = "刘备"
        elif word == "孟德" or word == "孟德曰":
                rword = "曹操"
        elif word == "孟获" or word == "孟获曰":
                rword = "孟获"
        else:
                rword = word
        counts[rword] = counts.get(rword,0) + 1
        for word in excludes:
                
