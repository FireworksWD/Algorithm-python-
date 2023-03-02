'''有 N 种物品和一个容量是 V 的背包。
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。
输入格
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
输出格式
输出一个整数，表示最大价值。'''
n, m = list(map(int, input().split()))
goods = []
f = [0] * 2010
for i in range(n):
    v, w, s = list(map(int, input().split()))
    k = 1
    while k <= s:
        s -= k
        goods.append([v * k, w * k])
        k <<= 1
    if s > 0:
        goods.append([v * s, w * s])
for good in goods:
    for j in range(m, good[0] - 1, -1):
        f[j] = max(f[j], f[j - good[0]] + good[1])
print(f[m])
