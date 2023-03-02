n = int(input())
a = []
for i in range(n):
    x = input()
    a.append([int(x), int(x[0:6]), int(x[6:14]), int(x[14:18])])
a.sort(key=lambda x: x[3], reverse=True)
a.sort(key=lambda x: x[1], reverse=True)
a.sort(key=lambda x: x[2], reverse=True)
for i in range(n):
    print(a[i][0])
