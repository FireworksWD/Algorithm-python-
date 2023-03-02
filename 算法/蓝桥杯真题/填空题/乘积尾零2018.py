s = [list(map(int, input().split())) for _ in range(10)]
ans = 1
res = 0
for i in range(10):
    for j in range(10):
        ans *= s[i][j]
for i in str(ans)[::-1]:
    if i == '0':
        res += 1
    else:
        break
print(res)
