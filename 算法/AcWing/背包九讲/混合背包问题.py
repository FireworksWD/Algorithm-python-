'''有 N 种物品和一个容量是 V 的背包。
物品一共有三类：
第一类物品只能用1次（01背包）；
第二类物品可以用无限次（完全背包）；
第三类物品最多只能用 si 次（多重背包）；
每种体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。
输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。
si=−1 表示第 i 种物品只能用1次；
si=0 表示第 i 种物品可以用无限次；
si>0 表示第 i 种物品可以使用 si 次；
输出格式
输出一个整数，表示最大价值。'''
n, m = map(int, input().split())
dp = [0] * 1010
for i in range(n):
    w, v, s = map(int, input().split())
    if not s:
        for j in range(w, m + 1):
            dp[j] = max(dp[j], dp[j - w] + v)
    else:
        s = abs(s)
        k = 1
        while k <= s:
            j = m
            while j >= w * k:
                dp[j] = max(dp[j], dp[j - w * k] + v * k)
                j -= 1
            s -= k
            k <<= 1
        if s:
            j = m
            while j >= w * s:
                dp[j] = max(dp[j], dp[j - w * s] + v * s)
                j -= 1
print(dp[m])
