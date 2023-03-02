a = [True] * 10 ** 5
res = []
for i in range(2, 10 ** 5):
    if a[i]: res.append(i)
    for j in res:
        if i * j >= 10 ** 5: break
        a[i * j] = False
        if i % j == 0: break
print(res[2018])
