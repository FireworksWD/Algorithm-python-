n, m = map(int, input().split())
ans = 0
for i in range(1, m + 1):
    if n * 10000000000 % i == 0:
        ans += 1
print(ans)
