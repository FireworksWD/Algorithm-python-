a1 = list(map(int, input().split()))
n = a1[0]
time = []
for i in range(1, len(a1) - 1, 2):
    time.append([a1[i], a1[i + 1]])
res = []
time.sort(key=lambda x: x[1])
res.append(time[0])
for i in range(1, n):
    if res[-1][1] <= time[i][0]:
        res.append(time[i])
print(len(res))
