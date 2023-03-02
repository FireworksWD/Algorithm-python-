n, s = map(int, input().split())
ti = list(map(int, input().split()))
ti.sort()
total = [0] * (s + 1)
ans, j = 0, 0
for i in range(n):
    j += 1
    if (j == s + 1):
        j = 1
    total[j] += ti[i]
    ans += total[j]
print(ans//n)
