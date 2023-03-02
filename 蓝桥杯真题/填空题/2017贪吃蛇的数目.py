x = [list(input()) for _ in range(20)]
ans = 0
for i in x:
    for j in i:
        if j == '#': ans += 1
        if j == '@': ans += 2
print(ans + 2)
