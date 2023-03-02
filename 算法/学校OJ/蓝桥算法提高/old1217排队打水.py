n, r = map(int, input().split())
t = list(map(int, input().split()))
s = [0] * (r + 1)
t.sort()
j = ans = 0
for i in range(n):
    j += 1
    if j == r + 1:
        j = 1
    s[j] += t[i]
    ans += s[j]
print(ans)
