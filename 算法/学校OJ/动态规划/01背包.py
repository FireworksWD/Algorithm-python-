n, m = map(int, input('输入物品个数和背包容量：').split())
bag = []
for i in range(n):
    bag.append(list(map(int, input('输入重量和价值：').split())))
res1 = [[0] * (m + 1) for _ in range(n + 1)]
bag.insert(0, [0, 0])
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if bag[i][0] <= j:
            res1[i][j] = max(res1[i - 1][j], res1[i - 1][j - bag[i][0]] + bag[i][1])
        else:
            res1[i][j] = res1[i - 1][j]
print(res1[-1][-1])
