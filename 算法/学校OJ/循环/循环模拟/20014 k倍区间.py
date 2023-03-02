n, k = map(int, input().split())
ans = 0
aum = 0
s = [0] * 100010
b = [0] * 100010
b[0] = 1
for i in range(1, n + 1):
    value = int(input())
    aum = value + aum
    s[i] += aum
    temp = s[i] % k
    b[temp] += 1
for i in range(k):
    ans += b[i] * (b[i] - 1) // 2
print(ans)
