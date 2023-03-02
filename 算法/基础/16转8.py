n = int(input('转换数据的个数'))
li = []
for i in range(n):
    if 1 <= n <= 10:
        s = input()
        if len(s) < 100000:
            res1 = int(s, 16)
            res2 = oct(res1)
            li.append(res2[2:])
for i in li:
    print(i, end='\n')