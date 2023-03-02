n,m=map(int,input().split())

def f(k):
    ans = 0
    for i in range(1, int(k**0.5)+1):
        if k % i == 0:
            ans += 2
        if i * i == k:
            ans += 1
    return ans
res = 0
for i in range(1, n + 1):
    if f(i) == m:
        res += 1
print(res)
