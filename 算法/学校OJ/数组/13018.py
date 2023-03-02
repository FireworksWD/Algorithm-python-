a = list(map(int, input().split()))
n = a[0]
a.pop(0)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            ans += 1
        else:
            break
print(ans)
