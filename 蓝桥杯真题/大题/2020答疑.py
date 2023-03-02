n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
a.sort(key=lambda x: sum(x))
ans, t = 0, 0
for i in range(n):
    t += sum(a[i])
    ans += t - a[i][-1]
print(ans)
