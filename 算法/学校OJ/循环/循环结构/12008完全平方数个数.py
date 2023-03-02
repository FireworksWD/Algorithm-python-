import math

n = int(input())
ans = 0
for i in range(1, n + 1):
    x = 2020 + 7 * i
    j = int(math.sqrt(x))
    if j * j == x:
        ans += 1
print(ans)
