ai = list(map(int, input().split()))
n = ai[0]
res = []
res.append(ai[1])
for i in range(2, len(ai)):
    while ai[i] in res:
        ai[i] += 1
    res.append(ai[i])
for i in res:
    print(i, end=' ')
