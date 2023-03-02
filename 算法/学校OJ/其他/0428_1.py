import math

n = int(input())
ans = 0
for i in range(1, n):
    if math.gcd(i, n) == 1:
        ans += 1
print(ans)
