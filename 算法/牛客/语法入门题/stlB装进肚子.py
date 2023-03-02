n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
c = []
for i in range(n):
    c.append([A[i], B[i]])
c.sort(key=lambda x: x[1] - x[0])
ans = 0
for i in range(k):
    ans += c[i][0]
for i in range(k, n):
    ans += c[i][1]
print(ans)
