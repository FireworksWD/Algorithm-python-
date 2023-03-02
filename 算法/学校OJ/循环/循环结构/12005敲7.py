n = int(input())
ans = 0
for i in range(1, n + 1):
    j = i
    if i % 7 == 0:
        ans += 1
        continue
    while j > 0:
        if j % 10 == 7:
            ans += 1
            break
        j //= 10
print(ans)
