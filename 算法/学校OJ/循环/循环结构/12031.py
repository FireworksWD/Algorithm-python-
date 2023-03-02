n = int(input())
res = 0
for i in range(2, n + 1):
    ans = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            ans += j
    if ans + 1 == i:
        res += 1
print(res)
