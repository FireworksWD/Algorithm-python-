n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
for i in range(n):
    if a[i] > m + 30:
        ans += 1
    else:
        break
print(ans)
