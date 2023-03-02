from functools import reduce
def multiply(a, b):
    a = list(map(lambda x : int(x), a.strip()))
    b = list(map(lambda x : int(x), b.strip()))
    c = list(map(lambda x : 0, ("0" + str(a) + str(b)).strip()))
    index = len(c) - 1;
    for i in range(len(a) - 1, -1, -1):
        pos = 0
        for j in range(len(b) - 1, -1, -1):
            temp = a[i] * b[j] + c[index - pos] #两个乘数相乘,并加上在此前一次的进位
            c[index - pos] = temp % 10 #保存运算求余结果
            c[index - pos - 1] += temp // 10 #处理进位,进位可以是0或者大于0的数
            pos += 1
        index -= 1
    return int(reduce(lambda x, y : str(x) + str(y), c)) #将list中的内容转换为字符串

a = input()
b = input()
print(multiply(a, b))