'''有 N 种物品和一个容量是 V 的背包。
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。
输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
输出格式
输出一个整数，表示最大价值'''
n, v = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(n)]
bag.insert(0, [0, 0, 0])
dp = [[0] * (v + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(0, v + 1):
        for k in range(0, bag[i][2] + 1):
            if k * bag[i][0] <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * bag[i][0]] + k * bag[i][1])
print(dp[n][v])
