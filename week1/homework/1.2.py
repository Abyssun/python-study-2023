# 整数序列求和。
# 用户输入一个正整数N，计算从1到N（包含1和N）相加之后的结果

n = input("请输入整数N：")
sum = 0
for i in range(int(n)):
    sum += i + 1
print("1到N求和结果：", sum)