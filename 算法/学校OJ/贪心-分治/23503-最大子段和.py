s = list(map(int, input().split()))
res = [0] * len(s)
res[0] = s[0]
for i in range(1, len(s)):
    res[i] = max(s[i], s[i] + res[i - 1])
print(max(res))
