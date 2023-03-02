n = int(input('个数'))
if 1 <= n <= 200:
    a = list(map(int, input('数据个数').split()))
    a.sort()
    for i in range(len(a)):
        print(a[i], end=" ")

