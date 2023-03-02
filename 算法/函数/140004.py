n, m = map(int, input().split())
res = 0


def f4(k):
    ans = 0
    i = 1
    while i * i < k:
        if k % i == 0:
            ans += 2
        if i * i == k:
            ans += 1
        i += 1
    return ans


for i in range(1, n + 1):
    if f4(i) == m:
        res += 1
print(res)
