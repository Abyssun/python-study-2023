# 从控制台获取一组数据
from math import sqrt
def getNum():
    nums = []
    iNumStr = input("请输入数值（空值输入时自动退出）：")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input()
    return nums

def mean(numbers):    #计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s / len(numbers)

def dev(numbers,mean):   # 计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return sqrt(sdev / (len(numbers) - 1))

def median(numbers):
    new = sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (new[size//2-1] + new[size//2]) / 2
    else:
        med = new[size//2]
    return med

n  = getNum()
m = mean(n)
print("平均值：{},标准差：{:.2}，中位数：{}".format(m,dev(n,m),median(n)))