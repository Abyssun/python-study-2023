# 健康食谱输出。列出5种不同食材，输出它们可能组成的所有菜式名称
diet = ['西红柿','花椰菜','黄瓜','牛排','虾仁']
for x in range(0,5):
    for y in range(0,5):
        if not(x == y):
            print("{} {}".format(diet[x],diet[y]))