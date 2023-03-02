lis1 = list(map(int, input().split()))
lis = lis1[1:]
t = list(set(lis))
t.sort()
for i in t:
    print(i, end=' ')
