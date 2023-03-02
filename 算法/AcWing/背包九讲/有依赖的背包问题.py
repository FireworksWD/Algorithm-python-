'''有 N 个物品和一个容量是 V 的背包。
物品之间具有依赖关系，且依赖关系组成一棵树的形状。如果选择一个物品，则必须选择它的父节点。
如下图所示：
如果选择物品5，则必须选择物品1和2。这是因为2是5的父节点，1是2的父节点。
每件物品的编号是 i，体积是 vi，价值是 wi，依赖的父节点编号是 pi。物品的下标范围是 1…N。
求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。
输出最大价值。
输入格式
第一行有两个整数 N，V，用空格隔开，分别表示物品个数和背包容量。
接下来有 N 行数据，每行数据表示一个物品。
第 i 行有三个整数 vi,wi,pi，用空格隔开，分别表示物品的体积、价值和依赖的物品编号。
如果 pi=−1，表示根节点。 数据保证所有物品构成一棵树。
输出格式
输出一个整数，表示最大价值。
数据范围
1≤N,V≤100
1≤vi,wi≤100
父节点编号范围：
内部结点：1≤pi≤N;
根节点 pi=−1;'''
from typing import List


class Solution:
    def dfs(self, u: int, g: List[List[int]], dp: List[List[int]]):
        for next in g[u]:
            self.dfs(next, g, dp)
            for j in range(self.V - self.v[u], -1, -1):
                for k in range(j + 1):
                    dp[u][j] = max(dp[u][j], dp[u][j - k] + dp[next][k])
        for j in range(self.V, self.v[u] - 1, -1):
            dp[u][j] = dp[u][j - self.v[u]] + self.w[u]
        for j in range(self.v[u]):
            dp[u][j] = 0

    # 定义三个全局变量这样不用在方法中传递很多的参数
    v, w, V = None, None, None

    def process(self):
        n, V = map(int, input().split())
        self.V = V
        # dp[u][j]表示以u为根节点且体积不超过j的最大价值
        dp = [[0] * (V + 1) for i in range(n + 1)]
        root = -1
        v, w = [0] * (n + 1), [0] * (n + 1)
        # 使用列表来表示图
        g = [list() for i in range(n + 1)]
        for i in range(1, n + 1):
            _v, _w, p = map(int, input().split())
            # p = -1为根节点
            if p == -1:
                root = i
                v[i] = _v
                w[i] = _w
            else:
                v[i] = _v
                w[i] = _w
                g[p].append(i)
        self.v = v
        self.w = w
        self.dfs(root, g, dp)
        return dp[root][V]


if __name__ == "__main__":
    print(Solution().process())
