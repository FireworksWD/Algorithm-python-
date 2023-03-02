n = 2021041820210418
ans, lis = 0, []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        lis.append(i)
        if n // i != i:
            lis.append(n // i)
for i in lis:
    for j in lis:
        for k in lis:
            if i * j * k == n:
                ans += 1
print(ans)
