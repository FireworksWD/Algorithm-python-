'''有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出 字典序最小的方案。这里的字典序是指：所选物品的编号所构成的序列。物品的编号范围是 1…N。
输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
输出格式
输出一行，包含若干个用空格隔开的整数，表示最优解中所选物品的编号序列，且该编号序列的字典序最小。
物品编号范围是 1…N。
数据范围
0<N,V≤1000
0<vi,wi≤1000'''
n, m = map(int, input().split())
w, v = [0] * 1010, [0] * 1010
dp = [[0] * 1010 for i in range(1010)]
for i in range(n):
    w[i], v[i] = map(int, input().split())
for i in range(n - 1, -1, -1):
    for j in range(m + 1):
        dp[i][j] = dp[i + 1][j]
        if j >= w[i]:
            dp[i][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])
j = m
for i in range(n):
    if j >= w[i] and dp[i][j] == dp[i+1][j - w[i]] + v[i]:
        print(i + 1, end=' ')
        j -= w[i]
