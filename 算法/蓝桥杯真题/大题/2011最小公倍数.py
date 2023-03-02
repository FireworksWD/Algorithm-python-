import math

n = int(input())
ans = 1
for i in range(1, n + 1):
    ans = i * ans // math.gcd(i, ans)
print(ans)
