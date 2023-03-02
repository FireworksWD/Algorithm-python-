'''有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出 最优选法的方案数。注意答案可能很大，请输出答案模 109+7 的结果。
输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。
输出格式
输出一个整数，表示 方案数 模 109+7 的结果。
数据范围
0<N,V≤1000
0<vi,wi≤1000'''
n, m = map(int, input().split())
dp, cnt = [0] * 1010, [0] * 1010
mod = 10 ** 9 + 7
for i in range(m + 1):
    cnt[i] = 1
for i in range(n):
    w, v = map(int, input().split())
    for j in range(m, w - 1, -1):
        if dp[j - w] + v > dp[j]:
            dp[j] = dp[j - w] + v
            cnt[j] = cnt[j - w]
        elif dp[j - w] + v == dp[j]:
            cnt[j] = (cnt[j] + cnt[j - w]) % mod
print(cnt[m])
