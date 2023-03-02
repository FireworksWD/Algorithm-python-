n = int(input())
m = int(input())
x = [i for i in range(1, n + 1)]
res = []
for i in range(n):
    t = [int(l) for l in str(x[i])]
    res.append([sum(t), x[i]])
res.sort(key=lambda x: x[0])
print(res[m - 1][1])
