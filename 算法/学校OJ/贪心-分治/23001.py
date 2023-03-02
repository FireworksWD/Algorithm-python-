al = list(map(int, input().split()))
n, c = al[0], al[1]
w = al[2:]
res = 0
w.sort()
value = 0
for i in range(n):
    if value + w[i] <= c:
        res += 1
        value += w[i]
print(res)
