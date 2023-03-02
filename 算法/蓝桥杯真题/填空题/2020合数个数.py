ans = 0
for i in range(4, 2021):
    for j in range(2, i):
        if i % j == 0:
            ans += 1
            break
print(ans)
